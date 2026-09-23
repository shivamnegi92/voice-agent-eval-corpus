#!/usr/bin/env python3
"""Validate a TRG (Timing-Recovery-Grounded) report.

Usage:
    python3 validate_trg.py trg_report.yaml

TRG prescribes which AXES must be reported, not which metric to use. This
checker therefore verifies that each applicable axis is populated and
internally coherent - it does NOT judge whether the numbers are good, which
is the reader's job, not a linter's.

Exit codes:
    0  compliant (warnings may still be printed)
    1  non-compliant
    2  file/parse error
"""

from __future__ import annotations

import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("error: pyyaml required  ->  pip install pyyaml", file=sys.stderr)
    raise SystemExit(2)

STATISTICS = {"mean", "median", "p95", "p99", "max", "min"}


class Report:
    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []

    def error(self, axis: str, msg: str) -> None:
        self.errors.append(f"[{axis}] {msg}")

    def warn(self, axis: str, msg: str) -> None:
        self.warnings.append(f"[{axis}] {msg}")


def blank(value) -> bool:
    return value is None or (isinstance(value, str) and not value.strip()) \
        or (isinstance(value, list) and not value)


def check_timing(data: dict, r: Report) -> None:
    t = data.get("timing") or {}
    for field in ("metric", "value", "conditions"):
        if blank(t.get(field)):
            r.error("T", f"timing.{field} is required")

    stat = (t.get("statistic") or "").strip().lower()
    if blank(stat):
        r.error("T", "timing.statistic is required (mean/median/p95/...)")
    elif stat not in STATISTICS:
        r.warn("T", f"timing.statistic '{stat}' is unusual; expected one of "
                    f"{sorted(STATISTICS)}")

    # A mean alone hides the worst case users actually notice.
    if not t.get("tail_reported") and stat in {"mean", "median"}:
        r.warn("T", "only a central statistic is reported. Tail latency "
                    "(p95/p99) is where users experience the worst case")


def check_recovery(data: dict, r: Report) -> None:
    rec = data.get("recovery") or {}
    if blank(rec.get("disruption_types")):
        r.error("R", "recovery.disruption_types must list at least one "
                     "disruption (interruption/backchannel/false_pause/...)")
    for field in ("metric", "value"):
        if blank(rec.get(field)):
            r.error("R", f"recovery.{field} is required")

    # The axis exists to separate disrupted from undisturbed behaviour.
    if blank(rec.get("baseline_undisrupted")):
        r.warn("R", "no undisrupted baseline given, so the cost of disruption "
                    "cannot be read from this report")


def check_grounded(data: dict, r: Report) -> None:
    g = data.get("grounded_outcome") or {}
    for field in ("verification_method", "state_source", "metric", "value"):
        if blank(g.get(field)):
            r.error("G", f"grounded_outcome.{field} is required")

    # This is the axis's whole point: external state, not self-report.
    if not g.get("self_report_excluded"):
        r.error("G", "self_report_excluded is false. The G axis requires "
                     "success judged from external state, not the agent's "
                     "own account of what it did")


def check_multiparty(data: dict, r: Report) -> None:
    m = data.get("multiparty") or {}
    if not m.get("applicable"):
        if blank(m.get("justification")):
            r.warn("M", "marked not applicable without justification. State "
                        "why the deployment admits only two speakers")
        return

    for field in ("silence_metric", "silence_value",
                  "authority_metric", "authority_value"):
        if blank(m.get(field)):
            r.error("M", f"multiparty.{field} is required when applicable")


def main() -> int:
    if len(sys.argv) != 2:
        print(__doc__)
        return 2

    path = Path(sys.argv[1])
    if not path.exists():
        print(f"error: no such file: {path}", file=sys.stderr)
        return 2

    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    except yaml.YAMLError as exc:
        print(f"error: could not parse YAML: {exc}", file=sys.stderr)
        return 2

    r = Report()
    check_timing(data, r)
    check_recovery(data, r)
    check_grounded(data, r)
    check_multiparty(data, r)

    name = ((data.get("system") or {}).get("name") or "<unnamed system>")
    print(f"TRG compliance check: {name}\n")

    if r.errors:
        print(f"NOT COMPLIANT ({len(r.errors)} error"
              f"{'s' if len(r.errors) != 1 else ''})")
        for e in r.errors:
            print(f"  ERROR   {e}")
    else:
        print("COMPLIANT: all applicable TRG axes are reported")

    for w in r.warnings:
        print(f"  WARNING {w}")

    if not r.errors and not r.warnings:
        print("  (no warnings)")

    return 1 if r.errors else 0


if __name__ == "__main__":
    raise SystemExit(main())

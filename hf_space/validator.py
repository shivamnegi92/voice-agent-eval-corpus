"""Core TRG compliance checks.

TRG prescribes which AXES must be reported, not which metric to use on
each. This module checks that each applicable axis is populated and
internally coherent - it does NOT judge whether the numbers are good,
which is the reader's job, not a linter's.
"""

from __future__ import annotations

import html
from pathlib import Path
from typing import Any

import yaml

STATISTICS = {"mean", "median", "p95", "p99", "max", "min"}


class Report:
    """Accumulates errors (non-compliant) and warnings (compliant but weak)."""

    def __init__(self) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.system_name: str = "<unnamed system>"

    def error(self, axis: str, msg: str) -> None:
        self.errors.append(f"[{axis}] {msg}")

    def warn(self, axis: str, msg: str) -> None:
        self.warnings.append(f"[{axis}] {msg}")

    @property
    def compliant(self) -> bool:
        return not self.errors

    def as_dict(self) -> dict[str, Any]:
        return {
            "system_name": self.system_name,
            "compliant": self.compliant,
            "errors": list(self.errors),
            "warnings": list(self.warnings),
        }


def blank(value: Any) -> bool:
    return (
        value is None
        or (isinstance(value, str) and not value.strip())
        or (isinstance(value, list) and not value)
    )


def check_timing(data: dict, r: Report) -> None:
    t = data.get("timing") or {}
    for field in ("metric", "value", "conditions"):
        if blank(t.get(field)):
            r.error("T", f"timing.{field} is required")

    stat = (t.get("statistic") or "").strip().lower()
    if blank(stat):
        r.error("T", "timing.statistic is required (mean/median/p95/...)")
    elif stat not in STATISTICS:
        r.warn(
            "T",
            f"timing.statistic '{stat}' is unusual; expected one of "
            f"{sorted(STATISTICS)}",
        )

    # A mean alone hides the worst case users actually notice.
    if not t.get("tail_reported") and stat in {"mean", "median"}:
        r.warn(
            "T",
            "only a central statistic is reported. Tail latency "
            "(p95/p99) is where users experience the worst case",
        )


def check_recovery(data: dict, r: Report) -> None:
    rec = data.get("recovery") or {}
    if blank(rec.get("disruption_types")):
        r.error(
            "R",
            "recovery.disruption_types must list at least one "
            "disruption (interruption/backchannel/false_pause/...)",
        )
    for field in ("metric", "value"):
        if blank(rec.get(field)):
            r.error("R", f"recovery.{field} is required")

    # The axis exists to separate disrupted from undisturbed behaviour.
    if blank(rec.get("baseline_undisrupted")):
        r.warn(
            "R",
            "no undisrupted baseline given, so the cost of disruption "
            "cannot be read from this report",
        )


def check_grounded(data: dict, r: Report) -> None:
    g = data.get("grounded_outcome") or {}
    for field in ("verification_method", "state_source", "metric", "value"):
        if blank(g.get(field)):
            r.error("G", f"grounded_outcome.{field} is required")

    # This is the axis's whole point: external state, not self-report.
    if not g.get("self_report_excluded"):
        r.error(
            "G",
            "self_report_excluded is false. The G axis requires "
            "success judged from external state, not the agent's "
            "own account of what it did",
        )


def check_multiparty(data: dict, r: Report) -> None:
    m = data.get("multiparty") or {}
    if not m.get("applicable"):
        if blank(m.get("justification")):
            r.warn(
                "M",
                "marked not applicable without justification. State "
                "why the deployment admits only two speakers",
            )
        return

    for field in ("silence_metric", "silence_value", "authority_metric", "authority_value"):
        if blank(m.get(field)):
            r.error("M", f"multiparty.{field} is required when applicable")


def validate_data(data: dict) -> Report:
    """Run all TRG checks against an already-parsed report dict."""
    r = Report()
    r.system_name = ((data.get("system") or {}).get("name") or "<unnamed system>")
    check_timing(data, r)
    check_recovery(data, r)
    check_grounded(data, r)
    check_multiparty(data, r)
    return r


def validate_file(path: str | Path) -> Report:
    """Parse a TRG YAML report and run all checks against it."""
    path = Path(path)
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    return validate_data(data)


def format_report(r: Report) -> str:
    lines = [f"TRG compliance check: {r.system_name}\n"]
    if r.errors:
        lines.append(f"NOT COMPLIANT ({len(r.errors)} error{'s' if len(r.errors) != 1 else ''})")
        for e in r.errors:
            lines.append(f"  ERROR   {e}")
    else:
        lines.append("COMPLIANT: all applicable TRG axes are reported")

    for w in r.warnings:
        lines.append(f"  WARNING {w}")

    if not r.errors and not r.warnings:
        lines.append("  (no warnings)")

    return "\n".join(lines)


def format_report_html(r: Report) -> str:
    """Same information as format_report, styled for the web UI."""
    if r.compliant:
        badge = (
            '<span style="background:#16a34a;color:#fff;padding:4px 12px;'
            'border-radius:999px;font-weight:600;font-size:13px;">'
            "&#10003; COMPLIANT</span>"
        )
    else:
        n = len(r.errors)
        badge = (
            '<span style="background:#dc2626;color:#fff;padding:4px 12px;'
            'border-radius:999px;font-weight:600;font-size:13px;">'
            f"&#10007; NOT COMPLIANT &middot; {n} error{'s' if n != 1 else ''}</span>"
        )

    parts = [
        '<div style="font-family:system-ui,-apple-system,sans-serif;line-height:1.5;">',
        f'<h3 style="margin:0 0 10px 0;">{html.escape(r.system_name)}</h3>',
        badge,
    ]

    if r.errors:
        parts.append('<p style="margin:14px 0 4px 0;font-weight:600;color:#991b1b;">Errors</p>')
        parts.append('<ul style="margin:0;padding-left:20px;color:#991b1b;">')
        parts += [f"<li>{html.escape(e)}</li>" for e in r.errors]
        parts.append("</ul>")

    if r.warnings:
        parts.append('<p style="margin:14px 0 4px 0;font-weight:600;color:#92400e;">Warnings</p>')
        parts.append('<ul style="margin:0;padding-left:20px;color:#92400e;">')
        parts += [f"<li>{html.escape(w)}</li>" for w in r.warnings]
        parts.append("</ul>")

    if not r.errors and not r.warnings:
        parts.append('<p style="margin:14px 0 0 0;color:#6b7280;">No warnings.</p>')

    parts.append("</div>")
    return "".join(parts)

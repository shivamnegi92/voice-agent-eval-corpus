"""Build a TRG leaderboard from a directory of report YAMLs.

Deliberately does not rank systems by a single score - TRG is a reporting
standard, not a scoring function. What this produces is a side-by-side
comparability table: which axes each system reports, and with what values,
so a reader can compare like-for-like instead of trusting whichever axis a
vendor chose to publish.
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import yaml

from trg_eval.validator import validate_data


def _axis_summary(data: dict, axis: str, fields: list[str]) -> str:
    block = data.get(axis) or {}
    parts = [str(block[f]) for f in fields if not _blank(block.get(f))]
    return " / ".join(parts) if parts else "-"


def _blank(value: Any) -> bool:
    return value is None or (isinstance(value, str) and not value.strip())


def load_reports(examples_dir: str | Path) -> list[dict]:
    """Load every trg_example_*.yaml in a directory into row dicts."""
    rows: list[dict] = []
    for path in sorted(Path(examples_dir).glob("trg_example_*.yaml")):
        data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        report = validate_data(data)
        system = data.get("system") or {}
        rows.append(
            {
                "file": path.name,
                "system": system.get("name", "<unnamed>"),
                "architecture": system.get("architecture", "-"),
                "version": system.get("version", "-"),
                "timing": _axis_summary(data, "timing", ["value", "statistic"]),
                "recovery": _axis_summary(data, "recovery", ["value"]),
                "grounded_outcome": _axis_summary(data, "grounded_outcome", ["value"]),
                "compliant": report.compliant,
                "warnings": len(report.warnings),
                "errors": len(report.errors),
            }
        )
    return rows


def to_markdown(rows: list[dict]) -> str:
    header = (
        "| System | Architecture | Timing (T) | Recovery (R) | Grounded Outcome (G) "
        "| TRG Compliant | Warnings | Source |\n"
        "|---|---|---|---|---|---|---|---|\n"
    )
    lines = []
    for r in rows:
        compliant = "yes" if r["compliant"] else "no"
        source = f"`{r['file']}`"
        lines.append(
            f"| {r['system']} | {r['architecture']} | {r['timing']} | {r['recovery']} "
            f"| {r['grounded_outcome']} | {compliant} | {r['warnings']} | {source} |"
        )
    return header + "\n".join(lines) + "\n"


def to_csv(rows: list[dict]) -> str:
    if not rows:
        return ""
    fields = list(rows[0].keys())
    lines = [",".join(fields)]
    for r in rows:
        lines.append(",".join(str(r[f]).replace(",", ";") for f in fields))
    return "\n".join(lines) + "\n"

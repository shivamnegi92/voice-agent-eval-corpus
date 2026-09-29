"""Build a TRG leaderboard from a directory of report YAMLs.

Vendored copy for the Hugging Face Space, kept dependency-free at runtime.
Canonical source: https://github.com/shivamnegi92/voice-agent-eval-corpus/blob/main/trg_eval/leaderboard.py

Deliberately does not rank systems by a single score - TRG is a reporting
standard, not a scoring function. What this produces is a side-by-side
comparability table: which axes each system reports, and with what values,
so a reader can compare like-for-like instead of trusting whichever axis a
vendor chose to publish.
"""

from __future__ import annotations

import html
from pathlib import Path
from typing import Any

import yaml

from validator import validate_data


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


def _cell(text: str) -> str:
    return f"<td>{html.escape(str(text), quote=False)}</td>"


def to_html(rows: list[dict]) -> str:
    """Styled table for the web UI. Cells wrap rather than truncate: these
    reports carry qualifying context a bare number would flatten, and
    hover-only tooltips are unreadable on keyboard and touch."""
    headers = [
        "System", "Architecture", "Timing (T)", "Recovery (R)",
        "Grounded Outcome (G)", "TRG", "Warnings",
    ]
    header_html = "".join(f"<th>{h}</th>" for h in headers)

    body_rows = []
    for r in rows:
        if r["compliant"]:
            badge = '<span style="color:#16a34a;font-weight:700;">&#10003; pass</span>'
        else:
            badge = '<span style="color:#dc2626;font-weight:700;">&#10007; fail</span>'
        body_rows.append(
            "<tr>"
            + f'<td><strong>{html.escape(str(r["system"]))}</strong><br>'
            f'<code style="font-size:11.5px;color:#4b5563;">{html.escape(r["file"])}</code></td>'
            + _cell(r["architecture"])
            + _cell(r["timing"])
            + _cell(r["recovery"])
            + _cell(r["grounded_outcome"])
            + f'<td style="white-space:nowrap;">{badge}</td>'
            + f'<td style="text-align:center;">{r["warnings"]}</td>'
            + "</tr>"
        )

    style = (
        "<style>"
        ".trg-board{border-collapse:collapse;width:100%;font-family:system-ui,"
        "-apple-system,sans-serif;font-size:13.5px;}"
        ".trg-board th{text-align:left;padding:9px 10px;background:#f3f4f6;"
        "border-bottom:2px solid #d1d5db;white-space:nowrap;}"
        ".trg-board td{padding:9px 10px;border-bottom:1px solid #e5e7eb;"
        "vertical-align:top;overflow-wrap:anywhere;}"
        ".trg-board td:first-child{min-width:220px;overflow-wrap:normal;}"
        ".trg-board tr:hover td{background:#f9fafb;}"
        "</style>"
    )
    return (
        style
        + f'<table class="trg-board"><thead><tr>{header_html}</tr></thead>'
        f"<tbody>{''.join(body_rows)}</tbody></table>"
    )

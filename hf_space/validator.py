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


PLACEHOLDERS = {"not reported", "not measured", "unknown"}


def blank(value: Any) -> bool:
    if isinstance(value, str):
        return not value.strip() or value.strip().lower() in PLACEHOLDERS
    if isinstance(value, list):
        return all(blank(v) for v in value)
    return value is None


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


def check_reporting_version(data: dict, r: Report) -> None:
    version = data.get("reporting_version", 1)
    if type(version) is not int or version not in (1, 2):
        r.error("report", "reporting_version must be 1 or 2")
        return
    if version == 1:
        return

    def require(axis: str, section: dict, fields: tuple[str, ...], path: str) -> None:
        for field in fields:
            value = section.get(field)
            if blank(value) or (isinstance(value, str) and value.strip().lower()
                                in {"not reported", "not measured", "unknown"}):
                r.error(axis, f"{path}.{field} is required by report version 2")

    conditions = data.get("evaluation_conditions") or {}
    for field in ("languages", "accents", "noise", "speaker_configuration", "load", "evaluator"):
        if blank(conditions.get(field)):
            r.error("conditions", f"evaluation_conditions.{field} must be disclosed")

    timing = data.get("timing") or {}
    require("T", timing, ("value", "anchors", "units"), "timing")
    if not isinstance(timing.get("tail_reported"), bool):
        r.error("T", "timing.tail_reported must explicitly disclose measurement status")
    recovery = data.get("recovery") or {}
    require("R", recovery, ("value", "state_definition", "protocol"), "recovery")
    grounded = data.get("grounded_outcome") or {}
    require("G", grounded, ("value",), "grounded_outcome")

    for axis, parent, name, fields in (
        ("T", timing, "appropriateness", ("metric", "value", "protocol")),
        ("G", grounded, "no_action", ("policy", "metric", "value", "verification_method", "action_trace")),
    ):
        section = parent.get(name) or {}
        if not isinstance(section.get("applicable"), bool):
            r.error(axis, f"{name}.applicable must be explicitly true or false")
        elif section["applicable"]:
            require(axis, section, fields, name)
        else:
            require(axis, section, ("justification",), name)
    multiparty = data.get("multiparty") or {}
    if multiparty.get("applicable"):
        require("M", multiparty, ("intervention_metric", "intervention_value"), "multiparty")
    elif blank(multiparty.get("justification")):
        r.error("M", "version 2 requires a justification when multiparty is inapplicable")


def validate_data(data: dict) -> Report:
    """Run all TRG checks against an already-parsed report dict."""
    r = Report()
    r.system_name = ((data.get("system") or {}).get("name") or "<unnamed system>")
    check_timing(data, r)
    check_recovery(data, r)
    check_grounded(data, r)
    check_multiparty(data, r)
    check_reporting_version(data, r)
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


def format_report_html(report: Report) -> str:
    """Render the existing demo presentation without changing validation rules."""
    if report.compliant:
        badge = (
            '<span style="background:#16a34a;color:#fff;padding:4px 12px;'
            'border-radius:999px;font-weight:600;font-size:13px;">'
            "&#10003; COMPLIANT</span>"
        )
    else:
        error_count = len(report.errors)
        badge = (
            '<span style="background:#dc2626;color:#fff;padding:4px 12px;'
            'border-radius:999px;font-weight:600;font-size:13px;">'
            f"&#10007; NOT COMPLIANT &middot; {error_count} error{'s' if error_count != 1 else ''}</span>"
        )
    parts = [
        '<div style="font-family:system-ui,-apple-system,sans-serif;line-height:1.5;">',
        f'<h3 style="margin:0 0 10px 0;">{html.escape(report.system_name)}</h3>',
        badge,
    ]
    if report.errors:
        parts.append('<p style="margin:14px 0 4px 0;font-weight:600;color:#991b1b;">Errors</p>')
        parts.append('<ul style="margin:0;padding-left:20px;color:#991b1b;">')
        parts.extend(f"<li>{html.escape(error)}</li>" for error in report.errors)
        parts.append("</ul>")
    if report.warnings:
        parts.append('<p style="margin:14px 0 4px 0;font-weight:600;color:#92400e;">Warnings</p>')
        parts.append('<ul style="margin:0;padding-left:20px;color:#92400e;">')
        parts.extend(f"<li>{html.escape(warning)}</li>" for warning in report.warnings)
        parts.append("</ul>")
    if not report.errors and not report.warnings:
        parts.append('<p style="margin:14px 0 0 0;color:#6b7280;">No warnings.</p>')
    parts.append("</div>")
    return "".join(parts)

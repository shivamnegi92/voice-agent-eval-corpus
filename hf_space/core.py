"""UI-agnostic logic shared by the static Space (index.html, via Pyodide) and
the optional server-backed Gradio app (app.py). No gradio import here - the
static page must not depend on it."""

from __future__ import annotations

from pathlib import Path

import yaml

from leaderboard import load_reports, to_html
from validator import format_report_html, validate_data

# Under Pyodide / exec() there is no __file__; files sit relative to the cwd.
HERE = Path(__file__).parent if "__file__" in globals() else Path.cwd()
EXAMPLES_DIR = HERE / "examples"

EXAMPLE_FILES = {
    "Blank template": "trg_report_template.yaml",
    "OpenAI gpt-realtime-1.5 (tau-Voice benchmark)": "trg_example_openai_realtime.yaml",
    "Google gemini-live-2.5-flash (tau-Voice benchmark)": "trg_example_gemini_live.yaml",
    "xAI grok-voice-agent (tau-Voice benchmark)": "trg_example_grok_voice.yaml",
    "NemotronLabs VoiceChat (self-reported)": "trg_example_nemotron.yaml",
}

LEADERBOARD_INTRO = """
<p style="color:#374151;">
Three of these four systems (OpenAI, Google, xAI) were benchmarked by a
single third party &mdash;
<a href="https://arxiv.org/abs/2603.13686" target="_blank">tau-Voice</a>
&mdash; under identical conditions, with task success verified against
final database state. TRG does not rank them into one score; it reports
which axes are covered so you can compare like-for-like.
</p>
"""


def load_example(choice: str) -> str:
    filename = EXAMPLE_FILES.get(choice, "trg_report_template.yaml")
    return (EXAMPLES_DIR / filename).read_text(encoding="utf-8")


def validate_text(yaml_text: str) -> str:
    """Validate a TRG report given as YAML text; return an HTML result."""
    if not yaml_text or not yaml_text.strip():
        return '<p style="color:#6b7280;">Paste a TRG report, upload one, or load an example above.</p>'
    try:
        data = yaml.safe_load(yaml_text) or {}
    except yaml.YAMLError as exc:
        return f'<p style="color:#dc2626;">Could not parse YAML: {exc}</p>'
    if not isinstance(data, dict):
        return '<p style="color:#dc2626;">A TRG report must be a YAML mapping at the top level.</p>'
    return format_report_html(validate_data(data))


def build_leaderboard_html() -> str:
    return LEADERBOARD_INTRO + to_html(load_reports(EXAMPLES_DIR))

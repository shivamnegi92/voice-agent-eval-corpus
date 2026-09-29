"""TRG (Timing-Recovery-Grounded) evaluation pipeline - Hugging Face Space.

Companion demo for *Evaluating Real-Time Voice Agents: From Component
Quality to Grounded Outcomes* (arXiv:2609.30798) and the corpus repo:
https://github.com/shivamnegi92/voice-agent-eval-corpus

Two tabs:
1. Validate a TRG report you paste, upload, or load from an example - no
   invented scoring, just a compliance check against the four axes.
2. Baseline leaderboard - four systems, one worked example self-reported and
   three benchmarked side-by-side by a single third party (tau-Voice).
"""

from __future__ import annotations

from pathlib import Path

import gradio as gr
import yaml

from leaderboard import load_reports, to_html
from validator import format_report_html, validate_data

# Gradio-Lite exec()s this file with no __file__; its virtual FS puts the
# inlined files relative to the cwd instead.
_HERE = Path(__file__).parent if "__file__" in globals() else Path.cwd()
EXAMPLES_DIR = _HERE / "examples"

EXAMPLE_FILES = {
    "Blank template": "trg_report_template.yaml",
    "OpenAI gpt-realtime-1.5 (tau-Voice benchmark)": "trg_example_openai_realtime.yaml",
    "Google gemini-live-2.5-flash (tau-Voice benchmark)": "trg_example_gemini_live.yaml",
    "xAI grok-voice-agent (tau-Voice benchmark)": "trg_example_grok_voice.yaml",
    "NemotronLabs VoiceChat (self-reported)": "trg_example_nemotron.yaml",
}
TEMPLATE_TEXT = (EXAMPLES_DIR / "trg_report_template.yaml").read_text(encoding="utf-8")

HEADER_HTML = """
<div style="display:flex;align-items:center;flex-wrap:wrap;gap:10px;margin-bottom:6px;">
  <h1 style="margin:0;font-size:26px;">TRG: Timing &middot; Recovery &middot; Grounded</h1>
</div>
<p style="margin:0 0 10px 0;color:#4b5563;">
  A minimum reporting standard for real-time voice agents &mdash; a report
  cannot claim compliance while staying silent on an axis its deployment
  actually exercises.
</p>
<div style="display:flex;gap:8px;flex-wrap:wrap;margin-bottom:4px;">
  <a href="https://arxiv.org/abs/2609.30798" target="_blank" style="text-decoration:none;">
    <span style="background:#b31b1b;color:#fff;padding:4px 12px;border-radius:999px;font-size:12.5px;font-weight:600;">arXiv:2609.30798</span>
  </a>
  <a href="https://github.com/shivamnegi92/voice-agent-eval-corpus" target="_blank" style="text-decoration:none;">
    <span style="background:#1f2328;color:#fff;padding:4px 12px;border-radius:999px;font-size:12.5px;font-weight:600;">GitHub repo</span>
  </a>
  <a href="https://github.com/shivamnegi92/voice-agent-eval-corpus/blob/main/corpus/leaderboard.md" target="_blank" style="text-decoration:none;">
    <span style="background:#2563eb;color:#fff;padding:4px 12px;border-radius:999px;font-size:12.5px;font-weight:600;">Full leaderboard on GitHub</span>
  </a>
</div>
"""

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


def validate(yaml_text: str, uploaded_file) -> str:
    if uploaded_file is not None:
        yaml_text = Path(uploaded_file.name).read_text(encoding="utf-8")

    if not yaml_text or not yaml_text.strip():
        return '<p style="color:#6b7280;">Paste a TRG report, upload one, or load an example above.</p>'

    try:
        data = yaml.safe_load(yaml_text) or {}
    except yaml.YAMLError as exc:
        return f'<p style="color:#dc2626;">Could not parse YAML: {exc}</p>'

    report = validate_data(data)
    return format_report_html(report)


def build_leaderboard_html() -> str:
    rows = load_reports(EXAMPLES_DIR)
    return LEADERBOARD_INTRO + to_html(rows)


with gr.Blocks(title="TRG Voice Agent Evaluation", theme=gr.themes.Soft(primary_hue="blue")) as demo:
    gr.HTML(HEADER_HTML)

    with gr.Tab("Validate a report"):
        gr.Markdown(
            "Paste a filled-in TRG YAML report, upload one, or load a "
            "worked example below. This checks *coverage*, not quality - "
            "it will not tell you your numbers are good, only that you "
            "reported the axis honestly."
        )
        example_picker = gr.Dropdown(
            choices=list(EXAMPLE_FILES),
            value="Blank template",
            label="Load an example",
        )
        with gr.Row():
            with gr.Column():
                yaml_input = gr.Textbox(
                    label="TRG report (YAML)",
                    value=TEMPLATE_TEXT,
                    lines=26,
                    max_lines=40,
                )
                file_input = gr.File(label="...or upload a .yaml file", file_types=[".yaml", ".yml"])
                run_btn = gr.Button("Validate", variant="primary")
            with gr.Column():
                gr.Markdown("**Result**")
                result = gr.HTML()

        example_picker.change(load_example, inputs=example_picker, outputs=yaml_input)
        run_btn.click(validate, inputs=[yaml_input, file_input], outputs=result)

    with gr.Tab("Baseline leaderboard"):
        gr.HTML(build_leaderboard_html())

if __name__ == "__main__":
    demo.launch()

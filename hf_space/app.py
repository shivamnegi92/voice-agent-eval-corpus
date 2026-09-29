"""TRG (Timing-Recovery-Grounded) evaluation pipeline - Hugging Face Space.

Companion demo for *Evaluating Real-Time Voice Agents: From Component
Quality to Grounded Outcomes* (arXiv:2609.30798) and the corpus repo:
https://github.com/shivamnegi92/voice-agent-eval-corpus

Two tabs:
1. Validate a TRG report you paste or upload - no invented scoring, just a
   compliance check against the four axes.
2. Baseline leaderboard - four systems, one worked example self-reported and
   three benchmarked side-by-side by a single third party (tau-Voice).
"""

from __future__ import annotations

from pathlib import Path

import gradio as gr
import yaml

from leaderboard import load_reports, to_markdown
from validator import format_report, validate_data

EXAMPLES_DIR = Path(__file__).parent / "examples"
TEMPLATE_TEXT = (EXAMPLES_DIR / "trg_report_template.yaml").read_text(encoding="utf-8")


def validate(yaml_text: str, uploaded_file) -> str:
    if uploaded_file is not None:
        yaml_text = Path(uploaded_file.name).read_text(encoding="utf-8")

    if not yaml_text or not yaml_text.strip():
        return "Paste a TRG report (or upload one) to validate."

    try:
        data = yaml.safe_load(yaml_text) or {}
    except yaml.YAMLError as exc:
        return f"error: could not parse YAML: {exc}"

    report = validate_data(data)
    return format_report(report)


def build_leaderboard_markdown() -> str:
    rows = load_reports(EXAMPLES_DIR)
    intro = (
        "Three of these four systems (OpenAI, Google, xAI) were benchmarked "
        "by a single third party - [tau-Voice](https://arxiv.org/abs/2603.13686) "
        "- under identical conditions, with task success verified against "
        "final database state. TRG does not rank them into one score; it "
        "reports which axes are covered so you can compare like-for-like.\n\n"
    )
    return intro + to_markdown(rows)


with gr.Blocks(title="TRG Voice Agent Evaluation") as demo:
    gr.Markdown(
        "# TRG: Timing - Recovery - Grounded\n"
        "A minimum reporting standard for real-time voice agents, from "
        "[*Evaluating Real-Time Voice Agents: From Component Quality to "
        "Grounded Outcomes*](https://arxiv.org/abs/2609.30798). "
        "[Corpus + full pipeline on GitHub]"
        "(https://github.com/shivamnegi92/voice-agent-eval-corpus)."
    )

    with gr.Tab("Validate a report"):
        gr.Markdown(
            "Paste a filled-in TRG YAML report (or upload one) and check "
            "which axes are compliant. This checks *coverage*, not quality - "
            "it will not tell you your numbers are good, only that you "
            "reported the axis honestly."
        )
        with gr.Row():
            with gr.Column():
                yaml_input = gr.Textbox(
                    label="TRG report (YAML)",
                    value=TEMPLATE_TEXT,
                    lines=28,
                )
                file_input = gr.File(label="...or upload a .yaml file", file_types=[".yaml", ".yml"])
                run_btn = gr.Button("Validate", variant="primary")
            with gr.Column():
                result = gr.Textbox(label="Result", lines=28)

        run_btn.click(validate, inputs=[yaml_input, file_input], outputs=result)

    with gr.Tab("Baseline leaderboard"):
        gr.Markdown(build_leaderboard_markdown())

if __name__ == "__main__":
    demo.launch()

"""TRG (Timing-Recovery-Grounded) evaluation pipeline - optional server-backed
Gradio app. The deployed static Space does NOT use this file; it runs core.py
directly on Pyodide (see build_index.py). Run locally: `python app.py`.

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

from core import EXAMPLE_FILES, build_leaderboard_html, load_example, validate_text

TEMPLATE_TEXT = load_example("Blank template")

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

def validate(yaml_text: str, uploaded_file) -> str:
    if uploaded_file is not None:
        yaml_text = Path(uploaded_file.name).read_text(encoding="utf-8")
    return validate_text(yaml_text)


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

---
title: TRG Voice Agent Eval
colorFrom: blue
colorTo: purple
sdk: static
app_file: index.html
pinned: false
license: mit
---

# TRG: Timing - Recovery - Grounded

Interactive demo for the TRG minimum reporting standard, from
[*Evaluating Real-Time Voice Agents: From Component Quality to Grounded
Outcomes*](https://arxiv.org/abs/2609.30798).

This Space runs entirely in your browser via
[Pyodide](https://pyodide.org) (Python on WebAssembly): no server, no cold
starts, free on the `static` Space tier. The first load takes a few seconds
while the Python runtime downloads.

- **Validate a report** - paste or upload a TRG YAML report and see which
  axes are compliant.
- **Baseline leaderboard** - four worked examples, three of them benchmarked
  side-by-side by a single third party.

Full corpus, pipeline source, and CLI tooling:
https://github.com/shivamnegi92/voice-agent-eval-corpus

`index.html` is generated: `build_index.py` takes the UI in `template.html`
and embeds `core.py` / `validator.py` / `leaderboard.py` / `examples/*.yaml`,
which the page loads into Pyodide at startup. The GitHub repo's `trg_eval/`
package is the canonical source; if the two ever disagree, GitHub wins.
Regenerate with `python3 hf_space/build_index.py` instead of hand-editing
`index.html`.

Want a server-backed version instead? `app.py` is a Gradio UI over the same
`core.py`: `pip install gradio pyyaml && python app.py`, or deploy it to a
Space with `sdk: gradio` (needs Hugging Face PRO as of this writing).

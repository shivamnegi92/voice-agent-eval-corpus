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
[Gradio-Lite](https://www.gradio.app/guides/gradio-lite) (Pyodide/WebAssembly)
- no server, no cold starts, free on the `static` Space tier. The first load
takes a few seconds while the Python runtime downloads; after that it's
instant.

- **Validate a report** - paste or upload a TRG YAML report and see which
  axes are compliant.
- **Baseline leaderboard** - four worked examples, three of them benchmarked
  side-by-side by a single third party.

Full corpus, pipeline source, and CLI tooling:
https://github.com/shivamnegi92/voice-agent-eval-corpus

`index.html` inlines a copy of `app.py` / `validator.py` / `leaderboard.py`
for Gradio-Lite's virtual filesystem. The GitHub repo's `trg_eval/` package
is the canonical source - if the two ever disagree, GitHub wins. Regenerate
`index.html` from the plain `.py`/`.yaml` files with the generator noted in
the repo's `CLAUDE.md` rather than hand-editing the embedded copies.

Want a server-backed version instead (e.g. for heavier processing later)?
The original `app.py` here also runs standalone: `pip install gradio pyyaml
&& python app.py`, or deploy it to a Space with `sdk: gradio` if you have a
Hugging Face PRO plan (required for free-tier Gradio/Docker Spaces as of
this writing).

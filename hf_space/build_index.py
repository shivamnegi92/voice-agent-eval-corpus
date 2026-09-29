#!/usr/bin/env python3
"""Regenerate hf_space/index.html from the source files in hf_space/.

The deployed Hugging Face Space is a static Gradio-Lite page (Pyodide/WASM,
no server). Gradio-Lite takes its Python files inlined as
`<gradio-lite-file>` blocks inside the HTML - there is no build step on
HF's side. This script IS that build step, so app.py / validator.py /
leaderboard.py / examples/*.yaml stay the single source of truth instead of
being hand-copied into HTML and drifting out of sync.

Run this after touching any file in hf_space/ (other than index.html itself):

    python3 hf_space/build_index.py
"""

from __future__ import annotations

import html
from pathlib import Path

HERE = Path(__file__).parent

HEAD = """<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>TRG Voice Agent Evaluation</title>
  <!-- Gradio's own maintainer-provided patched build, NOT jsdelivr/npm:
       @gradio/lite (any released npm version, including pinned 5.45.0)
       bundles a broken internal huggingface-hub constraint that has no
       resolvable wasm wheel (github.com/gradio-app/gradio/issues/12262).
       A `huggingface_hub==X` pin in gradio-lite-requirements does NOT fix
       this - it's baked into Lite's own manifest, not a normal pip
       constraint. This S3 URL is the exact patched build the Gradio team
       pointed to in that issue. If it ever 404s, re-check the issue for a
       replacement, or check whether a newer npm @gradio/lite release has
       absorbed the fix (PR #12162) before falling back to this pin. -->
  <script type="module" src="https://gradio-lite-previews.s3.amazonaws.com/PINNED_HF_HUB/dist/lite.js"></script>
  <link rel="stylesheet" href="https://gradio-lite-previews.s3.amazonaws.com/PINNED_HF_HUB/dist/lite.css" />
  <style>
    html, body { margin: 0; padding: 0; height: 100%; }
    gradio-lite { display: block; min-height: 100vh; }
  </style>
</head>
<body>
  <gradio-lite>
    <gradio-lite-requirements>
pyyaml
huggingface_hub==0.33.5
    </gradio-lite-requirements>
"""

TAIL = """  </gradio-lite>
</body>
</html>
"""


def file_block(name: str, path: Path, entrypoint: bool = False) -> str:
    text = path.read_text(encoding="utf-8")
    escaped = html.escape(text, quote=False)
    attr = " entrypoint" if entrypoint else ""
    return f'    <gradio-lite-file name="{name}"{attr}>\n{escaped}\n    </gradio-lite-file>\n'


def main() -> None:
    parts = [HEAD]
    parts.append(file_block("app.py", HERE / "app.py", entrypoint=True))
    parts.append(file_block("validator.py", HERE / "validator.py"))
    parts.append(file_block("leaderboard.py", HERE / "leaderboard.py"))
    for yaml_path in sorted((HERE / "examples").glob("*.yaml")):
        parts.append(file_block(f"examples/{yaml_path.name}", yaml_path))
    parts.append(TAIL)

    out_path = HERE / "index.html"
    out_path.write_text("".join(parts), encoding="utf-8")
    print(f"wrote {out_path} ({out_path.stat().st_size} bytes)")


if __name__ == "__main__":
    main()

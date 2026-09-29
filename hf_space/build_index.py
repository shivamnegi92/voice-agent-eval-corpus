#!/usr/bin/env python3
"""Regenerate hf_space/index.html from template.html + the Python/YAML sources.

The deployed Hugging Face Space is a static page running plain Pyodide
(Python in WebAssembly, no server). template.html holds the UI; this script
embeds core.py / validator.py / leaderboard.py / examples/*.yaml as a JSON
blob that the page writes into Pyodide's virtual filesystem at startup. The
source files stay the single source of truth, so nothing is hand-copied into HTML.

Run after touching template.html or any embedded file:

    python3 hf_space/build_index.py
"""

from __future__ import annotations

import json
from pathlib import Path

HERE = Path(__file__).parent
PLACEHOLDER = "/*__FILES__*/"
PY_FILES = ("core.py", "validator.py", "leaderboard.py")


def collect_files() -> dict[str, str]:
    files = {name: (HERE / name).read_text(encoding="utf-8") for name in PY_FILES}
    for path in sorted((HERE / "examples").glob("*.yaml")):
        files[f"examples/{path.name}"] = path.read_text(encoding="utf-8")
    return files


def main() -> None:
    template = (HERE / "template.html").read_text(encoding="utf-8")
    # Escape "</" so embedded text can never close the <script> tag early.
    payload = json.dumps(collect_files()).replace("</", "<\\/")
    out_path = HERE / "index.html"
    out_path.write_text(template.replace(PLACEHOLDER, payload), encoding="utf-8")
    print(f"wrote {out_path} ({out_path.stat().st_size} bytes)")


if __name__ == "__main__":
    main()

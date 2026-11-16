#!/usr/bin/env python3
"""Validate the Chinese README language switcher and local links."""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def check() -> list[str]:
    english, chinese = ROOT / "README.md", ROOT / "README.zh-CN.md"
    if not chinese.exists():
        return ["README.zh-CN.md is missing"]
    errors = []
    if "[**English**](README.md)" not in english.read_text(encoding="utf-8"):
        errors.append("README.md needs a link to README.zh-CN.md")
    text = chinese.read_text(encoding="utf-8")
    if "[English](README.md)" not in text:
        errors.append("README.zh-CN.md needs a link to README.md")
    for target in re.findall(r"\]\((?!https?://|mailto:|#)([^)#]+)(?:#[^)]*)?\)", text):
        if not (ROOT / target).exists():
            errors.append(f"Chinese README links to missing local path: {target}")
    return errors


if __name__ == "__main__":
    failures = check()
    if failures:
        print("\n".join(f"- {failure}" for failure in failures), file=sys.stderr)
        raise SystemExit(1)
    print("Chinese README switcher and local links are valid.")

#!/usr/bin/env python3
"""Build the TRG baseline leaderboard from trg/trg_example_*.yaml.

Usage:
    python3 scripts/build_leaderboard.py
    trg-leaderboard                        # if installed via pip

Writes corpus/leaderboard.md and corpus/leaderboard.csv.
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from trg_eval.cli import leaderboard_main

if __name__ == "__main__":
    raise SystemExit(leaderboard_main())

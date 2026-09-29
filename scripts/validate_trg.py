#!/usr/bin/env python3
"""Validate a TRG (Timing-Recovery-Grounded) report.

Usage:
    python3 scripts/validate_trg.py trg_report.yaml
    trg-validate trg_report.yaml          # if installed via pip

Exit codes:
    0  compliant (warnings may still be printed)
    1  non-compliant
    2  file/parse error
"""

from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from trg_eval.cli import validate_main

if __name__ == "__main__":
    raise SystemExit(validate_main())

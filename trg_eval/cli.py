"""Console-script entry points for the trg_eval pipeline."""

from __future__ import annotations

import sys
from pathlib import Path

from trg_eval.leaderboard import load_reports, to_csv, to_markdown
from trg_eval.validator import format_report, validate_file

REPO_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_EXAMPLES_DIR = REPO_ROOT / "trg"
DEFAULT_MD_OUT = REPO_ROOT / "corpus" / "leaderboard.md"
DEFAULT_CSV_OUT = REPO_ROOT / "corpus" / "leaderboard.csv"


def validate_main(argv: list[str] | None = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    if len(argv) != 1:
        print(__doc__ or "usage: trg-validate <report.yaml>")
        return 2

    path = Path(argv[0])
    if not path.exists():
        print(f"error: no such file: {path}", file=sys.stderr)
        return 2

    try:
        report = validate_file(path)
    except Exception as exc:  # yaml parse errors, etc.
        print(f"error: could not parse YAML: {exc}", file=sys.stderr)
        return 2

    print(format_report(report))
    return 1 if report.errors else 0


def leaderboard_main(argv: list[str] | None = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    examples_dir = Path(argv[0]) if argv else DEFAULT_EXAMPLES_DIR

    rows = load_reports(examples_dir)
    if not rows:
        print(f"error: no trg_example_*.yaml files found in {examples_dir}", file=sys.stderr)
        return 2

    md = to_markdown(rows)
    csv_text = to_csv(rows)

    DEFAULT_MD_OUT.parent.mkdir(parents=True, exist_ok=True)
    DEFAULT_MD_OUT.write_text(md, encoding="utf-8")
    DEFAULT_CSV_OUT.write_text(csv_text, encoding="utf-8")

    print(md)
    print(f"Wrote {DEFAULT_MD_OUT.relative_to(REPO_ROOT)} and "
          f"{DEFAULT_CSV_OUT.relative_to(REPO_ROOT)} ({len(rows)} systems)")
    return 0

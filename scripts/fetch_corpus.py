#!/usr/bin/env python3
"""Rebuild the voice-agent corpus locally from its metadata.

This corpus ships METADATA ONLY. Of 41 sources, only 1 carries an explicit
open-licence grant (see licence_audit.csv), so redistributing the PDFs would
not be lawful. Instead you fetch them yourself from the original hosts, and
this script verifies that what you received is byte-identical to what the
survey analysed.

Usage:
    python3 fetch_corpus.py                  # fetch all, verify hashes
    python3 fetch_corpus.py --verify-only    # re-check an existing copy
    python3 fetch_corpus.py --out DIR        # default: ./pdfs

Behind a corporate proxy, set the standard environment variables and they
will be honoured automatically:

    export HTTPS_PROXY=http://your-proxy:8080
    python3 fetch_corpus.py

Exit status is non-zero if any file fails verification, so this is safe to
run in CI.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

HERE = Path(__file__).resolve().parent
DEFAULT_CORPUS = HERE.parent / "corpus" / "voice_agent_corpus.csv"
USER_AGENT = "voice-agent-eval-corpus/1.0 (research reproduction script)"
DELAY_SECONDS = 3.0  # be polite to arXiv; they rate-limit aggressively


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for block in iter(lambda: fh.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def pdf_url(row: dict) -> str | None:
    """Best-effort source URL for a row."""
    ident = (row.get("identifier") or "").strip()
    if ident.startswith("arXiv:"):
        return f"https://arxiv.org/pdf/{ident.removeprefix('arXiv:')}"
    if ident.startswith("doi:"):
        return f"https://doi.org/{ident.removeprefix('doi:')}"
    if ident.startswith("aclanthology:"):
        return f"https://aclanthology.org/{ident.removeprefix('aclanthology:')}.pdf"
    url = (row.get("url") or "").strip()
    return url or None


def fetch(url: str, dest: Path) -> tuple[bool, str]:
    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            data = resp.read()
    except (urllib.error.URLError, TimeoutError) as exc:
        reason = getattr(exc, "reason", exc)
        hint = ""
        if "nodename nor servname" in str(reason) or "Name or service" in str(reason):
            hint = "  (DNS failed - behind a proxy? set HTTPS_PROXY)"
        return False, f"fetch failed: {reason}{hint}"
    if not data.startswith(b"%PDF"):
        return False, f"not a PDF (got {len(data)} bytes)"
    dest.write_bytes(data)
    return True, f"{len(data)} bytes"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--corpus", type=Path, default=DEFAULT_CORPUS)
    ap.add_argument("--out", type=Path, default=Path("pdfs"))
    ap.add_argument("--verify-only", action="store_true")
    args = ap.parse_args()

    if not args.corpus.exists():
        print(f"corpus file not found: {args.corpus}", file=sys.stderr)
        return 2

    rows = list(csv.DictReader(args.corpus.open(encoding="utf-8")))
    args.out.mkdir(parents=True, exist_ok=True)

    # urllib reads HTTPS_PROXY/HTTP_PROXY from the environment by default;
    # report it so a proxied run is self-evident in the log
    proxies = urllib.request.getproxies()
    if proxies:
        print(f"using proxy: {proxies.get('https') or proxies.get('http')}\n")

    ok = mismatched = failed = skipped = 0

    for i, row in enumerate(rows, 1):
        name = row["pdf_filename"]
        dest = args.out / name
        expected = row["pdf_sha256"]
        label = f"[{i:2}/{len(rows)}] {name[:52]:52}"

        if dest.exists():
            actual = sha256(dest)
            if actual == expected:
                print(f"{label} OK (cached)")
                ok += 1
            else:
                print(f"{label} HASH MISMATCH")
                print(f"       expected {expected}")
                print(f"       actual   {actual}")
                mismatched += 1
            continue

        if args.verify_only:
            print(f"{label} MISSING")
            skipped += 1
            continue

        url = pdf_url(row)
        if not url:
            print(f"{label} SKIP (no resolvable url)")
            skipped += 1
            continue

        success, detail = fetch(url, dest)
        if not success:
            print(f"{label} FAIL ({detail})")
            failed += 1
        else:
            actual = sha256(dest)
            if actual == expected:
                print(f"{label} OK ({detail})")
                ok += 1
            else:
                # Not necessarily corruption: arXiv silently serves the latest
                # version, so a new revision changes the bytes legitimately.
                print(f"{label} HASH MISMATCH (source may have been revised)")
                mismatched += 1
        time.sleep(DELAY_SECONDS)

    print(f"\nverified OK      : {ok}")
    print(f"hash mismatched  : {mismatched}")
    print(f"fetch failed     : {failed}")
    print(f"skipped          : {skipped}")
    print(f"total            : {len(rows)}")

    return 0 if (mismatched == 0 and failed == 0) else 1


if __name__ == "__main__":
    raise SystemExit(main())

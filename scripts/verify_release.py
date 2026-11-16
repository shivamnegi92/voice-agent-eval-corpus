#!/usr/bin/env python3
"""Verify versioned corpus invariants and published file checksums (no network)."""
from collections import Counter
import csv
import hashlib
import io
import json
from pathlib import Path
import re

import yaml

ROOT = Path(__file__).resolve().parents[1]


def verify(root=ROOT):
    manifest = json.loads((root / "release_manifest.json").read_text())
    version = manifest["version"]
    for name, expected in manifest["sha256"].items():
        path = root / name
        if path.resolve().is_relative_to(root.resolve()) is False:
            raise ValueError("Manifest path escapes repository")
        if hashlib.sha256(path.read_bytes()).hexdigest() != expected:
            raise ValueError(f"Release checksum mismatch: {name}")
    citation = yaml.safe_load((root / "CITATION.cff").read_text())
    if str(citation["version"]) != version:
        raise ValueError("Citation and manifest versions disagree")
    package = (root / "pyproject.toml").read_text()
    module = (root / "trg_eval/__init__.py").read_text()
    if f'version = "{version}"' not in package or f'__version__ = "{version}"' not in module:
        raise ValueError("Package versions disagree")
    rows = list(csv.DictReader(io.StringIO((root / "corpus/voice_agent_corpus.csv").read_text())))
    if rows != json.loads((root / "corpus/voice_agent_corpus.json").read_text()):
        raise ValueError("CSV/JSON mismatch")
    roles = Counter(row["corpus_role"] for row in rows)
    if len(rows) != manifest["corpus"]["total"] or dict(roles) != manifest["corpus"]["roles"]:
        raise ValueError("Manifest corpus totals disagree")
    for field in ("paper_id", "pdf_sha256"):
        if len({row[field] for row in rows}) != len(rows):
            raise ValueError(f"Duplicate {field}")
    for name, field in (("licence_audit.csv", "paper_id"),):
        associated = list(csv.DictReader(io.StringIO((root / "corpus" / name).read_text())))
        if {row[field] for row in associated} != {row["paper_id"] for row in rows}:
            raise ValueError(f"Incomplete associated metadata: {name}")
    grants = sum(row["redistributable"] == "true" for row in rows)
    if grants != manifest["corpus"]["paper_scoped_grants"]:
        raise ValueError("Licence totals disagree")
    if not re.search(str(manifest["corpus"]["total"]), (root / "README.md").read_text()):
        raise ValueError("README corpus total missing")
    print(f"Release v{version}: {len(rows)} records; {len(manifest['sha256'])} checksums verified")


if __name__ == "__main__":
    verify()

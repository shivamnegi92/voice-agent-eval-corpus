# Release notes

## v1.2.0 — 2026-11-16

### Matched corpus and manuscript snapshot
- 140 artifacts: 136 primary, 3 positioning, 1 method; cutoff 2026-10-02.
- Twelve historical evaluation works now accompany the matching manuscript;
  91 evaluation works, 11 meta-evaluation works, 41 primary works with published
  versions. See `corpus/reconciliation.md` for discovery/screening provenance.
- Complete CSV/JSON, reviewed source joins, taxonomy, licence audit, search
  protocol, outcome evidence, source audit and publication-version metadata.
- WearVox year corrected to 2025 from its authoritative first-submission date;
  stable paper ID and analyzed PDF hash unchanged. 90 primary works date to 2026.
- All 140 analyzed PDF hashes/filename-identity checks and 102/102 outcome quote
  checks pass. Live metadata checks match all 141 bibliography entries.
- Two explicit paper-scoped grants found by full-PDF licence scan; 138 PDFs
  without one. No source PDFs are redistributed, regardless of classification.

### TRG tooling
- Reporting schema stays **TRG v2**; existing four legacy reports and their
  published measurements remain unchanged.
- Optional **TRG-Ref 0.1** specification, starter sandbox tasks, offline analyzer,
  matched case-cluster bootstrap uncertainty and 19 regression tests (including
  release-integrity checks).
- Synthetic smoke fixture is software-test data only: no fresh live-agent results,
  performance improvement or independent adoption is claimed.
- Contribution/adoption evidence checklist and release-status documentation.

### Publication boundaries
The replacement manuscript is prepared against this snapshot; the author must
still replace arXiv 2609.30798. The live preprint remains an earlier version until
that happens. GitHub v1.2.0 is an immutable versioned reference; the concept Zenodo
DOI may still resolve to v1.1.1 until its archive integration completes. Do not
attribute v1.2.0 contents to the old archive. See `release_manifest.json` for file
hashes. Hugging Face demo deployment is not updated by this GitHub release.

## v1.1.1 — 2026-10-08

128-source release with four Interspeech citation upgrades; historical schema and
measurements are preserved in the corresponding Git tag/archive.

# Contributor guidance

Public metadata-only companion to arXiv:2609.30798, an unreviewed preprint.
Current release: v1.2.0, 140 artifacts (136 primary, 3 positioning, 1 method),
cutoff 2026-10-02. The prepared manuscript matches this corpus; the public arXiv
replacement remains the author's responsibility. See RELEASE_STATUS.md.

## Release invariants

- Never commit source PDFs, credentials, private audio, or machine-specific data.
- CSV and JSON records must be identical, with unique paper IDs and PDF hashes.
- Reviewed totals in corpus/join_overrides.yaml must match the corpus.
- Identifiers and hashes refer to the analyzed artifact, not necessarily latest.
- Corpus metadata is CC-BY-4.0; code is MIT. Source papers retain their own terms.
- Do not overwrite generated metadata by hand; update reviewed source records and
  regenerate the full matching bundle, including taxonomy and licence audit.

## Independent versions

Package/corpus: 1.2.0. TRG reporting schema: 2. Optional measurement protocol:
TRG-Ref 0.1. These versions are not interchangeable. A checker pass confirms
reporting structure, not evidence truth, measurement validity or system safety.

The four existing reports retain legacy semantics and published measurements.
Three come from one tau-Voice benchmark source; do not pool unrelated benchmarks
as if conditions were identical. Do not fill unreported v2 fields with guesses.
The synthetic reference log is software-test data and never leaderboard evidence.

## Checks

```bash
python -m unittest discover -s tests -v
python scripts/check_zh_readme.py
python -m trg_eval.protocol protocol/synthetic_smoke.jsonl > /tmp/trg-smoke.json
python scripts/validate_trg.py trg/trg_report_template.yaml  # expected failure
python scripts/validate_trg.py trg/trg_example_nemotron.yaml # expected success
python scripts/build_leaderboard.py
```

The generated leaderboard must not change without an intentional report change.
No PDFs may be tracked. CI also checks corpus roles, joins and hashes.

## Hosted demo and scientific claims

hf_space/ is a static Pyodide demo. Its vendored validator/leaderboard and browser
wrapper need compatibility review before updates. Build index.html from sources;
GitHub commits alone do not deploy the hosted Space. `/home/pyodide` is a browser
virtual filesystem, not a personal path.

Do not claim a peer-reviewed publication, new agent experiments or independent
adoption without corresponding evidence. Preserve truthful research-assistance
and screening limitations. Use exact release versions and checksums; verify a
Zenodo archive before claiming it contains current files.

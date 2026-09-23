# CLAUDE.md - voice-agent-eval-corpus

Context for AI agents working in this repo.

## What this is

Public companion resource to an unpublished manuscript on real-time voice
agent evaluation. Ships **metadata for 41 sources** plus **TRG**
(Timing-Recovery-Grounded), a proposed minimum reporting standard.

- **Public:** `github.com/shivamnegi92/voice-agent-eval-corpus`
- **Author:** Shivam Negi, Northeastern University, `negi.sh@northeastern.edu`
- Source repo for the paper is `SLM_PAPER`, which is **private** and lives at
  `../SLM_PAPER` locally.

## The one rule that matters

**Never commit a PDF here.**

A licence audit found exactly **1 of 41** sources carries an explicit
open-licence grant. The other 40 are arXiv-default, which does not give third
parties redistribution rights. Publishing them would be unlawful.

This is enforced twice, deliberately:
- `.gitignore` blocks `*.pdf` and `pdfs/`
- `.github/workflows/validate.yml` fails CI if any `*.pdf` is tracked

Instead of the papers, we ship their **SHA-256 hashes**. `fetch_corpus.py`
downloads from the original hosts and verifies each one, which makes the
corpus auditable without hosting anything.

## Layout

```
corpus/    voice_agent_corpus.csv|.json  41 rows, 15 fields
           schema.md                     field definitions
           reconciliation.md             how 51 yaml -> 41 PDFs -> 38 primary
           licence_audit.csv             per-source redistribution status
           join_overrides.yaml           human-verified filename->bibkey pairs
scripts/   fetch_corpus.py               rebuild local PDFs, hash-verified
           validate_trg.py               TRG compliance checker
trg/       trg_report_template.yaml      fillable
           trg_example_nemotron.yaml     worked example
```

## Counts that must hold

**41 rows = 38 primary + 2 positioning + 1 method.** The 38 split
6/3/8/8/7/6 across six taxonomy categories, matching the paper.

CI enforces: 41 rows, 38 primary, no duplicate `paper_id` or `pdf_sha256`,
every identifier resolvable (`arXiv:` / `doi:` / `aclanthology:` prefixed).

## Regenerating

This repo is **generated**, not hand-edited. Source of truth is
`../SLM_PAPER/voice_agent_research/`:

```bash
cd ../SLM_PAPER/voice_agent_research
python3 scripts/build_corpus.py     # -> corpus_build/voice_agent_corpus.csv
python3 scripts/audit_licences.py   # -> corpus_build/licence_audit.csv
```

Then copy the outputs across. Editing the CSV here directly will be
overwritten on the next build.

## Local checks before pushing

```bash
python3 scripts/validate_trg.py trg/trg_report_template.yaml   # must FAIL (exit 1)
python3 scripts/validate_trg.py trg/trg_example_nemotron.yaml  # must PASS (exit 0)
git ls-files '*.pdf' | wc -l                                   # must be 0
```

The template failing is correct behaviour: a blank report is not compliant.

## Things not to get wrong

- **Citation status is `@unpublished`.** The paper is not peer reviewed or
  accepted anywhere. Do not upgrade it to `@article` until it genuinely is.
- **Identifiers come from `references.bib` in the private repo**, which is
  authoritative. `sources.yaml` there is an incomplete first-pass log and has
  at least one stale identifier. Do not source identifiers from it.
- **Hash mismatches are not necessarily bugs.** arXiv serves the latest
  version, so an author revision legitimately changes bytes. It means you do
  not have the artefact the survey analysed.
- **Proxy needed on the author's corporate network:**
  `export HTTPS_PROXY=http://proxy-intlho.wal-mart.com:8080`, and
  `export GH_HOST=github.com` for `gh` (it defaults to the Walmart host).

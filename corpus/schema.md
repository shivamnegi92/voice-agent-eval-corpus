# Corpus schema

One row per source in `voice_agent_corpus.csv` / `.json`. The current corpus
(cutoff 2026-10-02) has 128 rows. It has not been published as a
new release.

| Field | Type | Description |
|---|---|---|
| `paper_id` | string | Stable key, matching the BibTeX key used in the survey. **Primary key.** |
| `title` | string | Paper title as printed. |
| `authors` | string | Author list, `and`-separated as in BibTeX. |
| `year` | integer | Publication or preprint year. |
| `venue` | string | Journal, conference, or `arXiv preprint`. |
| `identifier` | string | Namespaced identifier: `arXiv:NNNN.NNNNNvN`, `doi:...`, or `aclanthology:...`. New arXiv records pin the analysed version. |
| `url` | string | Landing page, where recorded. May be empty; `identifier` is the reliable field. |
| `category` | enum | Legacy artifact-type group (see below), or `not_applicable` for non-primary roles. |
| `corpus_role` | enum | `primary` (71), `positioning` (3), `method` (1). See `reconciliation.md`. |
| `evidence_role` | enum | `evaluation`, `meta_evaluation`, `system`, `data`, `analysis`, `positioning`, `method`. |
| `capability_axes` | `;`-list | Axis A: `component`, `timing`, `recovery`, `grounded`, `multiparty`. Empty for positioning and method sources. |
| `conditions` | `;`-list | Axis B, evaluation works only: `non_english`, `real_speech`, `acoustic_variation`, `long_session`. |
| `instruments` | `;`-list | Axis B, evaluation works only: `human_reference`, `model_judge`, `state_verification`, `simulation`. |
| `pdf_filename` | string | Canonical filename. Not shipped; `fetch_corpus.py` writes to this name. |
| `pdf_sha256` | string | SHA-256 of the PDF analysed by the survey. |
| `license` | string | Detected licence (see `licence_audit.csv`). |
| `redistributable` | boolean | Whether an explicit paper-scoped grant was found in the PDF. Dataset/model licence mentions do not qualify. Absence is `false`, not proof of a restrictive host licence. |
| `verified` | boolean | Passed first-page identity verification. |
| `verified_date` | date | When that check was last run. |

## `category` values

| Value | Count |
|---|---|
| `end_to_end_s2s` | 10 |
| `cascaded_hybrid` | 6 |
| `turn_taking_vap` | 13 |
| `conversational_benchmarks` | 22 |
| `agentic_evaluation` | 14 |
| `streaming_synthesis_codecs` | 6 |
| `not_applicable` | 4 |

Explicitly assigned in `join_overrides.yaml` under `records`, not inferred
from where a citation appears. The six legacy identifiers are artifact-type
groups kept for continuity; they no longer organise the manuscript.

## Two-axis taxonomy

`taxonomy_coding.yaml` codes every record once, with a short `basis` note for
evaluation works. Axis A records the capability exercised; Axis B records
evaluation conditions and grading instruments. A code is set only when the
analysed PDF states it, so an empty field means "not reported", not "absent".
Codes are nonexclusive and must not be summed across columns.
`build_corpus.py` fails if any record is uncoded or uses an unknown value, and
generates the manuscript coverage table (`taslp/coverage_table.tex`) from it.
The `revision` block records reviewed totals and the cutoff used by CI.

## `corpus_role` values

- **`primary`** (71) - substantive evidence, including evaluator-reliability studies.
- **`positioning`** (3) - closely related surveys, cited to situate this work.
- **`method`** (1) - cited in the methodological note only.

## On `pdf_sha256`

This is what lets the corpus be audited without redistributing anything.
`fetch_corpus.py` downloads from the original host and compares.

A mismatch is **not** necessarily corruption. arXiv serves the latest version
of a paper, so an author revision legitimately changes the bytes. A mismatch
means *you do not have the artefact the survey analysed*, which is exactly
the thing worth knowing; it does not by itself mean something is broken.

# Corpus schema

One row per source in `voice_agent_corpus.csv` / `.json`. 41 rows.

| Field | Type | Description |
|---|---|---|
| `paper_id` | string | Stable key, matching the BibTeX key used in the survey. **Primary key.** |
| `title` | string | Paper title as printed. |
| `authors` | string | Author list, `and`-separated as in BibTeX. |
| `year` | integer | Publication or preprint year. |
| `venue` | string | Journal, conference, or `arXiv preprint`. |
| `identifier` | string | Namespaced identifier: `arXiv:NNNN.NNNNN`, `doi:...`, or `aclanthology:...`. Used by `fetch_corpus.py` to build a download URL. |
| `url` | string | Landing page, where recorded. May be empty; `identifier` is the reliable field. |
| `category` | enum | Taxonomy category (see below), or `not_applicable` for non-primary roles. |
| `corpus_role` | enum | `primary` (38), `positioning` (2), `method` (1). See `reconciliation.md`. |
| `pdf_filename` | string | Canonical filename. Not shipped; `fetch_corpus.py` writes to this name. |
| `pdf_sha256` | string | SHA-256 of the PDF analysed by the survey. |
| `license` | string | Detected licence (see `licence_audit.csv`). |
| `redistributable` | boolean | Whether an explicit open-licence grant was found. **Conservative:** absence of evidence is recorded as `false`. |
| `verified` | boolean | Passed first-page identity verification. |
| `verified_date` | date | When that check was last run. |

## `category` values

| Value | Count |
|---|---|
| `end_to_end_s2s` | 6 |
| `cascaded_hybrid` | 3 |
| `turn_taking_vap` | 8 |
| `conversational_benchmarks` | 8 |
| `agentic_evaluation` | 7 |
| `streaming_synthesis_codecs` | 6 |
| `not_applicable` | 3 |

Assigned by which taxonomy section first cites the work. Discussion,
Limitations, and Conclusion citations are cross-references and do not
reassign a category.

## `corpus_role` values

- **`primary`** (38) - evidence within the taxonomy; the survey's subject matter.
- **`positioning`** (2) - closely related surveys, cited to situate this work.
- **`method`** (1) - cited in the methodological note only.

## On `pdf_sha256`

This is what lets the corpus be audited without redistributing anything.
`fetch_corpus.py` downloads from the original host and compares.

A mismatch is **not** necessarily corruption. arXiv serves the latest version
of a paper, so an author revision legitimately changes the bytes. A mismatch
means *you do not have the artefact the survey analysed*, which is exactly
the thing worth knowing; it does not by itself mean something is broken.

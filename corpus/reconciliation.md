# Corpus reconciliation

Why the repo's several counts differ, and how they add up. Published because
a corpus whose own numbers do not reconcile should not be trusted, and the
discrepancies here are real but explicable.

## Release v1.2.0 corpus (cutoff 2026-10-02)

The verified corpus has **140 PDFs and metadata rows: 136 primary, 3 positioning,
and 1 methodological source**, under the October 2, 2026 cutoff. The coding has
91 evaluation works and 11 meta-evaluation works. Its discovery routes are
reported separately because the searches have different coverage and screening
depths:

- 15 supplied seed papers, 20 papers from eight arXiv API queries, 3 follow-up
  additions, and 3 positioning or method sources (41 artifacts, 38 primary);
- 34 named candidates from supplied literature audits (33 primary, 1
  positioning survey). Audio2Tool and the HumDial full-duplex study were
  resolved through official projects; IRAF and demographic HEAR through
  primary arXiv search. The two HEAR projects remain separate;
- 47 evaluation and meta-evaluation works from the evaluation-focused search
  (`search_protocol.yaml`): 22 logged arXiv queries, backward snowballing from
  reference lists and forward snowballing via Semantic Scholar gave 2,472
  ranked candidates; 49 were proposed by the AI assistant from the top 500
  ranks and accepted by the first author, and 2 were excluded at full text
  (E1). Their codes were drafted by the AI assistant with a verbatim quote per
  code, machine-checked against the cited page, and accepted by the first author;
- 6 evaluation and meta-evaluation works from the 2024--2026 ACL Anthology
  search (`screening/acl_includes.yaml`);
- 12 accepted primary works from historical 2019--2023 searches: 5 ACL
  Anthology (18,058 papers, 74 matches, 73 new candidates screened by title and
  abstract, 5 accepted at full text), 5 ISCA Archive (5,403 papers, 108
  matches, 106 new candidates; 3 accepted at full text first, then a later
  full-text pass read 102 of the remaining 103 (one returned HTTP 404) and
  accepted 2 more evaluation works, with 27 others recorded as include_other
  but not coded), and 2 IEEE-venue
  works from Semantic Scholar metadata results (231 candidates, 115 query
  matches, 79 new; the 2 accepted came from open arXiv full texts). The later
  pass read 40 of the remaining 77 new IEEE candidates and accepted none; the
  other 37 have no open copy (36 need library access, 1 bad PMC link) and were
  not screened beyond metadata. Inclusion and codes for these 12 were
  AI-drafted and accepted by the second author (2026-10-08 for the first 10,
  2026-10-09 for the 2 ISCA works; `search_runs/2026-10-08-backfill/fulltext/`).
  See `search_protocol.yaml`
  and `screening/*_backfill_includes.yaml` for decisions and exact records.

The eight appendix arXiv queries were rerun verbatim on 2026-10-08 with dated
hit counts (`search_runs/2026-10-08-O1-O8-redate/log.csv`), closing the original
provenance gap without pretending the first run had been logged.

The search remains supplied-candidate-led and incompletely screened, not an
exhaustive multi-database review. Primary works with a published version cite
it (41 of 136) without adding sources. The bibliography has 141 entries (140
corpus works plus one uncited external reference). The manuscript (`arr/`)
covers all 140 artifacts. `source_audit.yaml` records the
original discovery and acquisition evidence; `evidence_ledger.md` contains
short PDF excerpts with page locators. PDFs remain private.

| Legacy category | Primary sources |
|---|---:|
| `end_to_end_s2s` | 10 |
| `cascaded_hybrid` | 6 |
| `turn_taking_vap` | 13 |
| `conversational_benchmarks` | 82 |
| `agentic_evaluation` | 19 |
| `streaming_synthesis_codecs` | 6 |
| **Total** | **136** |

Classification and verification come from explicit source records, not
citation order. Artifacts have pinned versions, SHA-256 checks, and recorded
identity-verification dates. All 140 identifiers and hashes are populated with
no duplicates, and the identity alarm reports zero suspects. All 102 outcome
evidence quotes are verified against their cited PDF pages. The PDF-text
licence audit finds two explicit paper-scoped grants and 138 PDFs without one.
No PDF is redistributed regardless of classification.

The following sections document the **historical 2026-09-23 public snapshot**,
not the v1.2.0 counts. WearVox uses its arXiv first-submission year (2025),
verified from the authoritative abstract page; its stable paper key and pinned
identifier are unchanged. This leaves 90 primary works dated 2026.

## The headline numbers

| Count | Value | What it is |
|---|---|---|
| `sources.yaml` entries | 51 | Everything ever considered, including non-papers |
| PDFs in `resource_pages/` | 41 | Papers actually obtained and verified |
| Rows in `voice_agent_corpus.csv` | 41 | One per obtained PDF |
| **Primary sources** | **38** | What the survey's taxonomy covers |
| BibTeX entries | 42 | 41 corpus + 1 external reference paper |

## 51 yaml entries to 41 PDFs

`sources.yaml` records every candidate from the original collection pass,
including material that is not a research paper:

| Section | Entries | With PDF | Why the gap |
|---|---|---|---|
| `arxiv_papers` | 9 | 9 | All obtained |
| `resolved_papers` | 5 | 5 | Identifier corrected, then obtained |
| `unavailable_local_source` | 1 | 0 | Notebook-only document; no retrievable source |
| `web_sources` | 17 | 0 | Blogs, vendor pages, YC directory: archived as HTML, never corpus papers |
| `second_batch` | 19 | 1 | Mostly vendor/provider comparison pages, excluded by policy |
| **Total** | **51** | **15** | |

That accounts for 15 of the 41 PDFs.

### The other 26 PDFs

**`sources.yaml` documents only the first collection pass.** The remaining 26
papers were found in later research passes and were never added back to it.
This is a real gap in the repo's bookkeeping, discovered while building the
join, and it is why the authoritative mapping for the published corpus is
**disk to BibTeX**, not yaml to BibTeX.

The published `voice_agent_corpus.csv` supersedes `sources.yaml` as the
corpus record. `sources.yaml` is retained for provenance of the first pass
only.

## 41 PDFs to 38 primary sources

Three PDFs are in the corpus but deliberately not counted among the 38
primary sources the taxonomy covers:

| `paper_id` | Role | Why not primary |
|---|---|---|
| `cui2024speechlm` | `positioning` | Closest related survey (SpeechLM). Cited to position this work against it, not as evidence within the taxonomy. |
| `gupta2024s2st` | `positioning` | Closest related survey (direct speech-to-speech translation). Same reasoning. |
| `pedinotti2026structsurvey` | `method` | Cited only in the methodological note on automated survey construction. |

`38 primary + 3 = 41`.

## 42 BibTeX entries to 41 corpus rows

One BibTeX entry has no corpus PDF:

| `paper_id` | Why excluded |
|---|---|
| `sahoo2024prompt` | The external reference paper (Sahoo et al., prompt-engineering survey) whose structure this survey's organisation follows. Stored at repo root as `reference_paper.pdf`. Cited for methodology only; not voice-agent literature. |

`41 corpus + 1 external = 42`.

## The 38 primary sources by category

Derived independently from the paper's section structure, not copied from its
prose, and matching the counts it states:

| Category | Count |
|---|---|
| `end_to_end_s2s` | 6 |
| `cascaded_hybrid` | 3 |
| `turn_taking_vap` | 8 |
| `conversational_benchmarks` | 8 |
| `agentic_evaluation` | 7 |
| `streaming_synthesis_codecs` | 6 |
| **Total** | **38** |

Categories are assigned by which taxonomy section first cites a work.
Citations appearing only in the Discussion, Limitations, or Conclusion are
cross-references and do not reassign a category.

## Integrity checks that pass

- 41/41 rows carry a resolvable identifier
- 41/41 rows carry a SHA-256 hash; no duplicate hashes, so no PDF is double-counted
- 41/41 PDFs passed first-page identity verification
- Every non-obvious filename-to-BibTeX pairing was confirmed by reading page 1
  of the PDF and is recorded in `join_overrides.yaml`

## Known limitations of this reconciliation

- `sources.yaml` is incomplete for passes after the first, as described above.
  It is not a reliable index of the corpus and should not be used as one.
- Licence classification is derived from document text and cannot see an
  author's arXiv licence selection, which lives in arXiv metadata. See
  `licence_audit.csv`. Nothing in this release depends on that distinction,
  because no PDF is redistributed.

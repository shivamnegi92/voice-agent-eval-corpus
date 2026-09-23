# Corpus reconciliation

Why the repo's several counts differ, and how they add up. Published because
a corpus whose own numbers do not reconcile should not be trusted, and the
discrepancies here are real but explicable.

All figures verified by script on 2026-09-23, not asserted from memory.

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

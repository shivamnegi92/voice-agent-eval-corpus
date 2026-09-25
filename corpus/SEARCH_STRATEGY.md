# Search strategy and corpus provenance

This file records how the corpus was assembled, so the review built on it can
be reproduced and its coverage assessed. The paper cites this file rather than
reproducing the raw queries inline.

## Provenance

The corpus has two provenances:

| Provenance | Count | Description |
|---|---|---|
| Seed reading list | 15 | Supplied directly as a starting set |
| Systematic search | 20 | Retrieved via the arXiv API over the seed list's themes |
| Follow-up research pass | 3 | A full-duplex tool-calling model and two benchmark extensions identified after initial drafting |
| **Total primary sources** | **38** | |

Three further works are cited for positioning or methodology rather than
counted in the corpus, giving **41 retained and verified PDFs**.

## arXiv API queries

Run verbatim against the arXiv API:

```text
ti:"Voice Activity Projection"
abs:"voice agent" AND abs:"benchmark"
abs:"full-duplex" AND abs:"spoken dialogue"
abs:"speech-to-speech" AND abs:"end-to-end"
abs:"neural audio codec" AND abs:"speech"
abs:"barge-in" OR abs:"interruption handling"
abs:"streaming" AND abs:"text-to-speech" AND abs:"latency"
all:"Full-Duplex-Bench"
```

Candidates were ranked by relevance and screened on title and abstract.

## Inclusion and exclusion criteria

**Included:** work whose primary contribution bears on real-time or
interactive spoken interaction — architectures, turn-taking models,
benchmarks, or streaming synthesis and codecs.

**Excluded**, three classes that appeared among candidates:

1. Vendor comparison articles — marketing artifacts rather than evaluable
   research.
2. Sources whose URLs no longer resolve — unverifiable references cannot be
   audited.
3. One unpublished local document not available to readers.

Retrieved items were retained only if the PDF could be obtained and verified.

## Verification

Each retrieved PDF was checked programmatically for valid PDF structure and
for agreement between its first-page text and the paper it was recorded as.

This step was not ceremonial. One widely circulated identifier for
Full-Duplex-Bench-v3 (`arXiv:2602.05105`) resolves to an unrelated multi-agent
robotics simulator; the correct identifier is `arXiv:2604.04847`.

All 41 retained PDFs pass this check. Per-source verification status and
SHA-256 hashes are in the corpus metadata; `scripts/fetch_corpus.py` rebuilds a
local copy from the original hosts and re-checks every hash.

## Coverage

Current to the retrieval date and weighted toward 2024–2026, because the
full-duplex literature is recent.

| Category | Sources |
|---|---|
| End-to-end and cascaded architectures | 9 |
| Turn-taking, VAP, conversational/multi-speaker benchmarks | 16 |
| Agentic and tool-use evaluation | 7 |
| Streaming synthesis and neural codecs | 6 |

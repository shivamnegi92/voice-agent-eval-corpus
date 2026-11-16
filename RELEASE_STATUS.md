# Publication and release status — v1.2.0

Prepared 2026-11-16. Distinguish the following independently versioned surfaces:

| Surface | Matching snapshot | Remaining boundary |
|---|---|---|
| Corpus/package v1.2.0 | 140 artifacts = 136 primary + 3 positioning + 1 method | Exact file hashes in `release_manifest.json` |
| Prepared replacement manuscript | Same 140 artifacts and counts, same cutoff 2026-10-02 | Author uploads replacement to arXiv |
| Live arXiv 2609.30798 | Original submission verified 2026-11-16 | Not yet the prepared replacement; do not remove this notice before checking posted PDF |
| Zenodo concept DOI 10.5281/zenodo.22924302 | Verified to resolve to v1.1.1 / record 23244804 before this release | Recheck archive integration after GitHub release; cite exact v1.2.0 tag/archive until verified |
| TRG reporting schema | Version 2 | Compliance checks reporting, not truth, safety or score quality |
| TRG-Ref measurement protocol | 0.1 preview | No live adapters, frozen speech assets or measured agent results supplied |
| Existing leaderboard | Four legacy reports, three from one tau-Voice source | Not four fresh v2 evaluations or independent adoption |
| Hugging Face demo | Prior deployment, no changes needed to its checker in this release | GitHub release does not redeploy or version-pin the hosted demo |

## Completed preparation

- Matching full metadata/provenance export with no third-party PDFs.
- Counts, schema, reconciliation, citation/package metadata and release notes aligned.
- Selected-corpus hash/identity checks: 140/140; evidence quotes: 102/102.
- Live bibliography metadata: 141/141 match after WearVox year correction.
- Legacy reports and measurements preserved; new synthetic fixtures kept separate.

## Author handoff

1. Use the prepared non-anonymous replacement PDF and source archive, not the
   anonymous ARR PDF. Replace existing arXiv 2609.30798 rather than opening a new
   submission. arXiv may require the source tarball, not just a PDF.
2. Copy the generated title/abstract/comments metadata supplied with the bundle;
   check author order, affiliations, licence and review/preprint declarations.
3. After arXiv posts, verify source counts, bibliography, TRG description, version
   number and exact v1.2.0 resource link on its live PDF/abstract page.
4. Recheck the Zenodo latest record and record the immutable version DOI only
   after confirming the archived files really match this release.

A concept DOI is a discovery link to a release family, not a frozen experiment
input. No fresh system-performance finding or independent adoption is claimed.

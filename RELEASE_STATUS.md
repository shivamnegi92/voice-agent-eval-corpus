# Release status and publication boundaries

Checked locally and via GitHub repository metadata on 2026-11-16.

| Surface | Verified state | Do not infer |
|---|---|---|
| Public companion corpus working tree | 128 metadata rows: 124 primary, 3 positioning, 1 method; v1.1.1 labels | Does not contain the private 140-row corpus |
| Private manuscript working tree | 140 artifacts / 136 primary; generated count macros agree | Not evidence that arXiv or Zenodo has this revision |
| arXiv 2609.30798 | Repository documentation says replacement has not been uploaded; live version not independently checked in this pass | Local package is not a public replacement |
| Existing public comparison | Four legacy reports; three use the same tau-Voice source, one is self-reported | Not four fresh TRG v2 evaluations or independent TRG adoption |
| TRG-Ref 0.1 | New local protocol, analyzer, tests and synthetic smoke fixture | No measured agent results; no validated benchmark claim |
| GitHub About | Updated live and re-read: 128-source corpus, TRG v2 checker and published-figure comparisons | Public description must not advertise private-only 140 rows |

Package version (1.1.1), reporting schema (TRG v2), measurement recipe
(TRG-Ref 0.1), manuscript version, and corpus row count are different things.
A new file in the working tree is **unreleased** until committed, pushed and
included in a release. No HF Space redeployment is part of these changes.

## Before publishing the next synchronized release

- [ ] Resolve scientific/editorial issues in the canonical private manuscript.
- [ ] Review the 140-row source snapshot, hashes, identifiers, licences and
  screening provenance before exporting metadata. No source PDFs may be copied.
- [ ] Export the complete matching corpus and associated taxonomy, joins, licence
  audit and reconciliation files together, not just the CSV/JSON pair.
- [ ] Regenerate manuscript counts/tables and supplement from that exact snapshot;
  compare all counts, claims and identifiers. Preserve legacy measurements.
- [ ] Update README (including translations), corpus schema/reconciliation,
  CITATION.cff, package/release notes and About with the released counts/version.
- [ ] Run corpus integrity CI, TRG template rejection/legacy example acceptance,
  leaderboard reproducibility, reference analyzer unit and CLI checks, PDF guard.
- [ ] Build arXiv from canonical manuscript and independently compile its source
  archive. Verify abstract, author affiliations, pages, DOI and data availability.
- [ ] Check ARR preprint-status declaration and author/publication approvals.
- [ ] Publish the matching metadata archive/tag and verify its immutable DOI.
- [ ] Author replaces the existing arXiv submission; do not create a new paper.
- [ ] After arXiv posts, verify the live abstract/PDF, actual version number,
  source counts, TRG schema and data link. Only then remove the mismatch notice.
- [ ] Deploy/recheck HF Space separately if its code/data changes are authorized.

For reproducibility cite the exact version DOI/tag/commit used. A concept DOI is
a discovery pointer to the version family; it is not a frozen experiment input.

## Evidence still needed

The empirical gate is three or more real systems under the same frozen protocol,
with raw attempted episodes, external-state verification and paired uncertainty.
The adoption gate is a verifiable external artifact demonstrating independent
application, with author assistance disclosed. Neither can be closed by adding
self-authored YAML examples, synthetic logs, or outreach copy.

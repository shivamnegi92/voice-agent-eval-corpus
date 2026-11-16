# Contributing and independently applying TRG

Corrections, negative results and first-time users are welcome. You do not need
to find a performance improvement or cite the authors to submit a report.
**No independent adoption is verified by the current examples.** Stars,
downloads, author-written reports and expressions of interest are not independent
scientific use. Do not label a report independent without disclosing involvement.

## Choose a contribution

1. **Corpus correction:** identify `paper_id`, disputed field, replacement,
   primary-source URL and supporting page/section. Do not attach third-party PDFs.
2. **Existing-evidence audit:** copy `trg/trg_report_template.yaml`; cite sources,
   preserve original figures and mark missing measurements honestly. A legacy
   report is not automatically a v2 report.
3. **Fresh measurement:** follow [TRG-Ref 0.1](protocol/README.md), or name and
   publish your alternative protocol. Provide report YAML, frozen conditions,
   all attempted episodes, scoring code and trace references. Use synthetic
   fixtures only for software checks, never the empirical comparison table.
4. **Independent application:** provide a public paper, release, evaluation
   report, or commit showing what you actually applied. Merely planning to use
   TRG is not completed adoption.

## Reproduce before submitting

```bash
python -m unittest discover -s tests -v
python scripts/validate_trg.py path/to/report.yaml
# Only for TRG-Ref logs:
python -m trg_eval.protocol path/to/episodes.jsonl > /tmp/summary.json
```

Open a pull request using the checklist. Maintainers review provenance and
comparability separately from schema compliance. A checker pass is neither
endorsement of a system nor proof of the measurements. Keep distinct protocol
versions, conditions, and source benchmarks in separate comparisons.
Never submit secrets, personal customer data, unconsented recordings or PDFs.

## Independent-use evidence record

For a verifiable application, include these fields in your issue/PR:

- Team/institution and public artifact URL/DOI/commit; observation date.
- TRG report version, protocol version, corpus release, tested system versions.
- What changed because of TRG (if anything), with a specific before/after example.
- Contributor/author overlap, funding, collaboration and assistance received;
  author-assisted pilots must be labelled as such, not fully independent.
- Reproduction commands and immutable evidence hashes, or access restrictions.
- Permission to list the application publicly. Do not publish private feedback
  or contact details without consent.

A maintainer should verify the artifact, record precisely what it demonstrates,
and distinguish application, citation, reproduction and downstream modification.
Do not turn an unverified submission into an adoption claim.

## Invitation template (not sent automatically)

> We are seeking external feedback on TRG, a minimum reporting standard for
> timing, recovery and externally grounded outcomes in voice agents. Would you
> try it on an evaluation you already run, record the time/burden, and tell us
> which omissions it reveals or fails to reveal? A negative assessment is useful.
> The optional reference protocol and tooling are available in this repository.
> There is no requirement to endorse, cite, or obtain a favorable result. Any
> author assistance and collaboration should be disclosed in resulting reports.

Prioritize teams already maintaining voice-agent evaluations; request permission
before adding anyone to an adoption list. Independent use must happen and be
verified, not be manufactured by outreach wording.

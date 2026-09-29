# Voice Agent Evaluation Corpus + TRG Evaluation Pipeline

A verified, reproducible metadata corpus of **41 sources** on real-time voice
agents, plus **TRG** (Timing-Recovery-Grounded): a minimum reporting standard,
a compliance checker, and a baseline leaderboard for evaluating them.

Companion resource to [*Evaluating Real-Time Voice Agents: From Component
Quality to Grounded Outcomes*](https://arxiv.org/abs/2609.30798) (arXiv:2609.30798).

**Try it without installing anything:** [Hugging Face Space](https://huggingface.co/spaces/shivamnegi92/trg-voice-agent-eval)

![TRG validator and leaderboard demo: a blank report fails, a real benchmarked system passes with a warning, then all four baseline systems get compared side by side](assets/demo.gif)

*Recorded with [VHS](https://github.com/charmbracelet/vhs); script at `assets/demo.tape`, regenerate with `vhs assets/demo.tape`.*

---

## Why this exists

Two things in voice-agent research are unnecessarily hard:

1. **Knowing which papers exist and what each actually measures.** The
   literature is split across speech foundation modelling, turn-taking
   psycholinguistics, and agentic evaluation, which rarely cite one another.
2. **Comparing systems.** Papers report whichever axis flatters them: latency,
   or turn-taking accuracy, or task success, seldom together.

This repo addresses both: a structured corpus for (1), and TRG for (2).

## What ships here

```
corpus/
  voice_agent_corpus.csv     41 sources, 15 fields
  voice_agent_corpus.json    same data, machine-readable
  schema.md                  field definitions
  reconciliation.md          how the counts add up, and where the gaps are
  licence_audit.csv          per-source redistribution status
  leaderboard.md/.csv        generated TRG baseline comparison (see below)
trg_eval/                    the pipeline as an installable Python package
  validator.py                 TRG compliance checks
  leaderboard.py                builds the comparison table
  cli.py                        console-script entry points
scripts/
  fetch_corpus.py            rebuild your local PDF set, hash-verified
  validate_trg.py            check a TRG report for compliance (CLI wrapper)
  build_leaderboard.py       regenerate corpus/leaderboard.md + .csv
trg/
  trg_report_template.yaml         fill this in for your own system
  trg_example_nemotron.yaml        worked example, self-reported figures
  trg_example_openai_realtime.yaml worked example, third-party benchmarked
  trg_example_gemini_live.yaml     worked example, third-party benchmarked
  trg_example_grok_voice.yaml      worked example, third-party benchmarked
hf_space/                    Gradio app mirrored to the Hugging Face Space
assets/                      demo.gif + demo.tape (the VHS script that recorded it)
pyproject.toml              pip-installable package (trg-validate, trg-leaderboard)
```

## No PDFs here, by design

This corpus ships **metadata only**. Of the 41 sources, exactly **one** carries
an explicit open-licence grant; the rest are arXiv-hosted with no licence
permitting third-party redistribution (see `corpus/licence_audit.csv`).

So instead of hosting papers we should not host, we ship their **SHA-256
hashes**. You fetch from the original source, and verify you received the
identical artefact the survey analysed:

```bash
python3 scripts/fetch_corpus.py           # fetch all 41, verify each hash
python3 scripts/fetch_corpus.py --verify-only   # re-check an existing copy
```

Behind a corporate proxy, the standard variables are honoured:

```bash
export HTTPS_PROXY=http://your-proxy:8080
python3 scripts/fetch_corpus.py
```

A hash mismatch is not necessarily corruption: arXiv serves the newest
version, so an author revision changes the bytes legitimately. It means you
do not have the exact artefact analysed, which is the useful thing to know.

## TRG: Timing - Recovery - Grounded

A minimum reporting standard. A real-time voice agent should be characterised
on all applicable axes, not on whichever one is most flattering:

| Axis | Requirement |
|---|---|
| **T** Timing | A latency measure under intended deployment conditions, stating what it measures and whether it is a mean or a tail statistic. |
| **R** Recovery | Behaviour after interruption, backchannel, or false pause, reported *separately* from undisturbed performance. |
| **G** Grounded outcome | Task success verified against external state, not the agent's own report of what it did. |
| **M** Multiparty *(conditional)* | Where more than two legitimate speakers exist: appropriate silence and authority-aware disclosure. |

TRG is deliberately weak. It prescribes which **axes** must appear, not which
metric to use on each; fixing metrics would ossify a literature whose best
instruments are all under two years old. The claim is only that a report
silent on an applicable axis leaves the system uncharacterised, however strong
its remaining numbers.

```bash
cp trg/trg_report_template.yaml my_report.yaml
# fill it in
python3 scripts/validate_trg.py my_report.yaml
```

Exit code is 0 when compliant and 1 when not, so it drops into CI.

### Install as a package

```bash
pip install -e .
trg-validate my_report.yaml
trg-leaderboard          # regenerates corpus/leaderboard.md and .csv
```

The worked examples are instructive. `trg_example_nemotron.yaml` uses
published figures from the strongest system in the corpus, and it *still*
raises a warning for reporting only a central latency statistic. That gap is
typical.

### Baseline leaderboard

Three of the four worked examples (`trg_example_openai_realtime.yaml`,
`trg_example_gemini_live.yaml`, `trg_example_grok_voice.yaml`) are populated
from a **single third-party benchmark** - tau-Voice (arXiv:2603.13686) -
which tested all three commercial systems under identical conditions and
verified task success against final database state. That is a stronger
comparison than stitching together three vendors' self-reported numbers,
each measured a different way, which is exactly the problem TRG exists to
surface.

[Full generated table: `corpus/leaderboard.md`](corpus/leaderboard.md) -
regenerate it any time with `trg-leaderboard` after adding your own system.

TRG deliberately does not rank these into a single score. It reports which
axes are covered and with what values, so *you* compare like-for-like
instead of trusting whichever axis a vendor chose to publish.

## Corpus at a glance

**38 primary sources** across six categories, plus 3 positioning/method
references:

| Category | n |
|---|---|
| End-to-end speech-to-speech | 6 |
| Cascaded and hybrid pipelines | 3 |
| Turn-taking and voice activity projection | 8 |
| Conversational benchmarks | 8 |
| Agentic and tool-use evaluation | 7 |
| Streaming synthesis and neural codecs | 6 |

Every count is reconciled in `corpus/reconciliation.md`, including where the
repo's own bookkeeping had gaps.

## Provenance and integrity

- 41/41 PDFs passed first-page identity verification, confirming each file
  contains the paper it claims to.
- 41/41 carry a SHA-256; no duplicates.
- Filename-to-BibTeX pairings that were not unambiguous were confirmed by
  reading page 1 of each PDF, recorded in `join_overrides.yaml`.

This matters more than it sounds. During construction, one widely-circulated
arXiv identifier turned out to point at an unrelated robotics paper. Automated
matching alone would have propagated that error into the corpus.

## Citing

**Status:** the companion paper is an arXiv preprint, not yet peer reviewed
or accepted anywhere. Please cite it as such; this entry will be updated if
and when it appears in a venue.

```bibtex
@misc{negi2026voiceagents,
  title         = {Evaluating Real-Time Voice Agents: From Component Quality
                   to Grounded Outcomes},
  author        = {Negi, Shivam and Rawat, Arpit and Jain, Rashi},
  year          = {2026},
  eprint        = {2609.30798},
  archivePrefix = {arXiv},
  primaryClass  = {cs.AI},
  note          = {Preprint, not yet peer reviewed}
}
```

To cite the corpus or TRG tooling specifically, use the metadata in
`CITATION.cff` (GitHub's "Cite this repository" button renders it for you).

## Licence

- **Data** (`corpus/`): CC-BY-4.0, see `LICENSE`
- **Code** (`scripts/`): MIT, see `LICENSE-CODE`

Licences cover *this* metadata and tooling. The papers themselves remain under
their original terms, which is precisely why they are not included here.

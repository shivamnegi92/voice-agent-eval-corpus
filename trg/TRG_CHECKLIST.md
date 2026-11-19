# TRG checklist (report version 2), ready to paste

TRG (Timing-Recovery-Grounded) is a minimum **reporting** standard for
real-time voice agent evaluations. It says which results a report must
disclose. It does not prescribe metrics, rank systems, or certify safety.
Paste one of the blocks below into your paper's appendix or your benchmark
README, then check the boxes that apply.

For a machine-checkable version, fill in
[`trg_report_template.yaml`](trg_report_template.yaml) and run
`python3 scripts/validate_trg.py my_report.yaml`. The script exits with 0 when
the report is complete and 1 when it isn't.

## Markdown

```markdown
### TRG reporting checklist (v2)

**Shared conditions** (state for every result below; "not reported" is allowed)
- [ ] Languages, accents, noise, speaker configuration, system load
- [ ] Evaluator: human (with instructions and agreement), model judge (named), or deterministic check

**T: Timing**
- [ ] Latency with start and end anchors (e.g. end of user speech to first audible agent audio), unit, and statistic
- [ ] Tail latency (p95/p99/max), or a stated reason it was not measured
- [ ] Hardware, hosting (self-hosted or API) and load conditions
- [ ] If the agent decides when to take the floor: context or intent appropriateness of that timing, with its annotation and scoring protocol

**R: Recovery**
- [ ] Named disruption types (interruption, correction, backchannel, noise, ...)
- [ ] Recovery measured separately from undisturbed performance, with the undisturbed baseline
- [ ] Conversational **and** task state after the disruption (stopping audio, resuming speech and restoring the workflow are separate outcomes)

**G: Grounded outcome**
- [ ] Success verified from external state or executed action traces, not from the agent's own report or a transcript judge
- [ ] Verification method and state source (e.g. assertions on a seeded database)
- [ ] When no action is warranted: the eligibility rule, and trace evidence that external state did not change

**M: Multiparty (conditional)**
- [ ] If more than two legitimate participants: warranted speech and silence, missed interventions, speaker attribution, and authority-aware action and disclosure
- [ ] If dyadic only: a one-line justification for why M does not apply
```

## LaTeX

Needs `\usepackage{amssymb}`. Replace `$\square$` with `$\boxtimes$` for
items you report.

```latex
\paragraph{TRG reporting checklist (v2).}
Following TRG~\citep{negi2026voiceagents}, we report:
\begin{itemize}\setlength\itemsep{0pt}
\item[$\square$] \textbf{Conditions:} languages, accents, noise, speaker
  configuration, load, and evaluator, for every result.
\item[$\square$] \textbf{T:} latency with start/end anchors, unit, statistic,
  tail, and hardware/hosting; timing appropriateness and its protocol if the
  agent chooses when to speak.
\item[$\square$] \textbf{R:} named disruptions; conversational and task state
  after disruption, separate from an undisturbed baseline.
\item[$\square$] \textbf{G:} outcome verified from external state or executed
  traces; eligibility rule and unchanged-state evidence for no-action cases.
\item[$\square$] \textbf{M:} multiparty speech, silence, attribution and
  authority, or a justification that the deployment is dyadic.
\end{itemize}
```

## One sentence for your paper

> We report results following the TRG minimum reporting standard
> (Timing, Recovery, Grounded outcome; Negi et al., 2026); the completed
> checklist is in Appendix X.

## Citation

```bibtex
@misc{negi2026voiceagents,
  title         = {Evaluating Real-Time Voice Agents: A Survey from Component
                   Quality to Grounded Outcomes},
  author        = {Negi, Shivam and Rawat, Arpit and Jain, Rashi},
  year          = {2026},
  eprint        = {2609.30798},
  archivePrefix = {arXiv},
  primaryClass  = {cs.AI},
  note          = {Preprint, not yet peer reviewed}
}
```

A completed TRG report says the evaluation is **fully reported**. It does not
say the system is good or safe.

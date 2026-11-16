# TRG-Ref 0.1: matched-episode pilot protocol

**Status: proposed, opt-in reference protocol; not a validated benchmark or a
new TRG requirement. No live agents have been evaluated with this protocol in
this repository.** The analyzer consumes logs; it does not connect to agents,
play audio, authenticate trace evidence, or establish TRG v2 compliance.
The six starter cases are an engineering pilot, not a representative task sample.

TRG remains metric-flexible. This companion fixes one measurement recipe so
teams using *this version and the same frozen assets* can compare results.
Do not pool it with the legacy published-figure leaderboard.

## 1. Preregister before running

Evaluate at least three systems under an identical task/backend/audio setup.
Use approved services/models and licensed or consented speech. Do not upload
private conversations or credentials. Record exact model/API version, date,
region, architecture, configuration, tool schema, prompt hash, temperature,
seeds (or `not exposed`), concurrency, client hardware and software commit.
Include costs, hardware, and unavailable configuration in the report.

Primary question: does the fastest system on clean p50 response latency also
have the highest interrupted grounded success? Primary outcome: each system's
paired interruption-minus-clean grounded success difference. Report both even
if there is no ranking reversal. This is descriptive evidence, not proof that
speed causes failure. Keep a held-out confirmation panel before generalizing.

- Freeze [tasks.json](tasks.json), prompts, user WAVs, noise WAV, backend version,
  scoring projections and manifest with SHA-256 hashes before evaluation.
- Smoke panel: six cases x three repeats x two conditions x three systems =
  **108 attempted episodes**. Useful for debugging, not population inference.
- For an initial study, author at least 30 distinct held-out cases spanning all
  six task families, three repeats, clean/interruption, three systems = **540
  attempted episodes**. This is a planning floor, not a power calculation;
  estimate required sample size from a disjoint pilot and preregister it.
- Randomize system/condition execution order within case/repeat, with a recorded
  seed. Reset sandbox and conversation before each episode. Report all attempts;
  log API errors/timeouts as failures, do not silently retry. A replacement run
  is a new study/run ID and must not overwrite the original.
- Fix English, one adult speaker, one accent, quiet audio, concurrency 1 for the
  minimum panel. These are scope restrictions, **not broad robustness evidence**.
  Run other languages, accents, speakers, noise and load as separate complete
  panels with different `conditions_id` values; never silently pool them.

## 2. Task and grounded-state contract

The starter cases cover three state-changing requests and three justified
no-action requests: no confirmation, no authorization, and ambiguity.
Use a local fictional booking/draft/cart backend; never a production account.
Each condition expresses the same final intent, so expected actions/state are
identical in clean and disrupted runs. An intent-changing interruption requires
a different case/protocol extension, not mislabelling correct new behavior.

For each task, expose read-only lookup, a read-only `prepare` operation, and a
state-changing commit tool. The preparation event writes the normalized pending
operation to evaluator-owned sandbox state; the recovery-state projection is
read from this backend, **not a model's explanation of its hidden state**.
For no-action cases it records `explain_only`, `decline_unauthorized`, or
`clarify_booking`. This constrained tool workflow is part of the test and must
be identical across systems; do not imply it measures unconstrained conversation.
Adapters/backend implementation and frozen audio remain required study assets;
they are not supplied by this starter task file.

- `expected_state` is the preregistered projection of the final backend snapshot.
  `actual_state` must use the identical projection. Ignore only declared volatile
  fields (e.g. random transaction IDs), never unauthorized side effects.
- `actions` is the **ordered, complete mutation-attempt trace**, including denied,
  duplicate and unauthorized attempts, normalized by a frozen mapping to strings
  such as `reschedule:demo-A:11`. Read-only tools have a separate retained trace.
  Comparing final state alone would hide compensating or duplicate mutations.
- `expected_actions` is the preregistered exact sequence. If multiple sequences
  are valid, split into separately specified cases or version the scorer; do not
  edit the expected sequence after inspecting results.
- At 2 seconds after the disruption clip ends (or the matched clean checkpoint),
  read `actual_recovery_state` from the preparation-state projection. `null`
  means absent/unobservable and scores zero, not a dropped trial. This measures
  recovery to an observable workflow checkpoint, not all conversational memory.
- Read final state and full action trace at the fixed 15-second episode deadline,
  including late actions before the deadline. Task success requires status `ok`,
  exact state AND exact mutation trace. No-action success additionally uses the
  preregistered no-action cases; no mutation attempts are permitted.

Retain initial/final state, preparation snapshots, all tool attempts/results,
annotated user/agent audio, client timestamps, API events and errors under a
content-addressed `trace_ref`. A URI's presence is not proof its contents exist.
Independent auditors must check a random 10% and every disputed episode against
these records. Publish redacted metadata and scoring code with access-controlled
consented audio if necessary; record access limitations.

## 3. Clocks, playback and timing appropriateness

Use one client monotonic clock, milliseconds from episode start. `user_end_ms`
is the end of the **initial complete request's audible waveform at client
playout**, excluding known trailing padding, not an ASR-final event. The same
initial clip is used across conditions. `first_audio_ms` is first audible agent
response at client playout, not first network byte; preserve negative gaps as
overlap. Declare any greeting and exclude it by preregistered turn identity.
`deadline_ms` is 15000 in the reference panel, relative to the same origin.

Record raw audio, sample rate (recommend PCM16 mono 24 kHz, identical resampler),
playout calibration, loopback latency and timestamps. Define audible onset as
RMS > -40 dBFS for at least 20 ms and audit against listening on the calibration
set; log detector version. Do not subtract provider compute/network time from
client-experienced latency. Publish p50/p95 gaps and missing-response counts.
The analyzer reports response-conditional latency; it never treats missing
responses as fast or as zero latency. Cross-system latency deltas use only pairs
with observed audio on both sides and disclose the pair count; interpret them
alongside failure and grounded success, not as an overall winner.

Timing appropriateness is separate: two blinded annotators label whether the
response respects the floor, avoids cutting off the user's content, and yields
to an intended takeover without dropping the requested task. Publish annotation
instructions, agreement (raw agreement and Cohen's kappa), disagreements and
adjudication. `timing_appropriate` is the adjudicated boolean; null is an
unannotated attempt and contributes zero to the conservative reported rate.
The analyzer supplies the rate/count only; it does not compute agreement.

For disruption response, retain secondary anchors `disruption_start_ms`,
`disruption_end_ms`, `agent_stop_ms`, and `resume_audio_ms` in the raw trace;
report stop and post-disruption resume latency separately from initial T.
The starter analyzer does not aggregate these secondary anchors.

## 4. Disruption schedule

- **clean:** complete initial utterance, no additional speech. Retain the matched
  checkpoint timestamp for recovery snapshot scheduling.
- **interruption (required):** prompt all systems to give a short read-only plan
  before commit. At first plan audio +300 ms, play the case's interruption clip.
  The sandbox holds commits until clip end +2 seconds (the recovery snapshot),
  in both conditions, and logs all attempts during this hold. This instrumented
  workflow prevents actions racing the checkpoint; disclose the imposed delay.
  Interruption repeats/clarifies intent; clean uses silence of equal duration.
  If there is no plan audio by 5 seconds, mark the episode `timeout`, retain it,
  and record disruption not delivered. Report delivered/attempted counts from
  traces; do not claim an undelivered interruption tested recovery.
- **false_pause (optional separate panel):** insert exactly 600 ms silence at a
  preregistered syntactic non-boundary of the initial clip; no new intent.
- **backchannel (optional separate panel):** play the same 250 ms acknowledgment
  clip at first plan audio +300 ms; user has no takeover intent.
- **noise (optional separate panel):** mix the fixed licensed noise waveform
  into the full initial request at 10 dB SNR, measured over active speech.

Freeze the exact timing/assets and release manifest; these descriptions alone
do not make recordings interchangeable. Optional conditions require a matching
clean run for every case/repeat/system. This protocol is dyadic: M is inapplicable
with that justification, not evidence of multiparty competence.

## 5. Episode log and analyzer

One JSON object per attempted episode. Required fields:

| Fields | Contract |
|---|---|
| `protocol_version` | `trg-ref-0.1` |
| `system`, `system_version` | Stable system label and exact tested version |
| `conditions_id` | Manifest identifier; analyze each configuration separately |
| `task_id`, `case_id`, `repeat` | Matched case and nonnegative repeat index |
| `condition` | `clean`, `interruption`, `false_pause`, `backchannel`, `noise` |
| `evidence_kind` | `measured` or `synthetic`; never mix them |
| `status` | `ok`, `timeout`, `error`; failures stay in denominators |
| `user_end_ms`, `first_audio_ms`, `deadline_ms` | Monotonic playout anchors; first audio null when absent |
| `timing_appropriate`, `no_action` | Boolean (timing may be null); preregister no-action eligibility |
| `expected_state`, `actual_state` | JSON objects from the frozen backend projection |
| `expected_actions`, `actions` | Ordered string lists of mutation attempts |
| `expected_recovery_state`, `actual_recovery_state` | Expected/backend checkpoint objects; actual may be null |
| `trace_ref` | Reference to retained state, action, audio and error evidence |

```bash
# From the repository root; Python >=3.9 and PyYAML are required.
python -m trg_eval.protocol protocol/synthetic_smoke.jsonl --seed 17 --bootstrap 2000 > /tmp/trg-smoke.json
# On your own complete matched logs (not supplied):
python -m trg_eval.protocol measured_episodes.jsonl > /tmp/trg-results.json
# Installed entry point: trg-analyze measured_episodes.jsonl
python -m unittest discover -s tests -v
```

`synthetic_smoke.jsonl` is deliberately toy arithmetic, **not a model run, human
speech study, or empirical finding**. It must never enter the leaderboard.
`measured` is a submitter declaration, not authentication by the analyzer.
No YAML report is generated automatically: fill the TRG v2 template with the
protocol/trace references, conditions and actual metrics, then run `trg-validate`.

The analyzer rejects duplicate/missing panel cells, mixed conditions/provenance,
version drift, changed ground truth, invalid timestamps and malformed values.
It requires at least clean plus one disruption, but does **not** certify the
minimum study size, frozen assets, audio schedule or manifest adherence.

## 6. Uncertainty and the citeable empirical deliverable

Publish per-system/per-condition T, R, G, no-action success, failure rate, and
annotation missingness. The analyzer gives 95% percentile intervals for binary
rates and response-conditional p50/p95 latency using 2,000 bootstrap draws,
resampling **case clusters** with replacement and keeping repeats together.
One case produces no CI. The sampling assumption is exchangeable distinct cases;
repeating six templates does not justify inference to all voice interaction.
No stratification is performed; publish task-family breakdowns in addition to
pooled summaries. A preregistered balanced task mix is essential.

Disrupted-minus-clean grounded success and B-minus-A system differences resample
matched case clusters, preserving pairing. Latency system delta is the mean
within-pair gap difference, not a difference in medians. Report which statistic
is which. Pairwise outputs are exploratory: no multiplicity correction or
significance test is supplied. Do not select a favorable pair after looking.

The paper's empirical deliverable should include the frozen preregistration,
release/manifest hashes, adapter/backend code, all attempted episode records,
blinded annotation protocol, paired interval table and an error taxonomy with
trace IDs. A null result is valid. No new performance claim belongs in the
manuscript until these are real measurements and independently checked.

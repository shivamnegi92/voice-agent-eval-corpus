# PDF Evidence Ledger

Cutoff: 2026-10-02. Quotes below are extracted from the analysed PDFs.
Page numbers refer to PDF pages. Line wrapping is normalised, not paraphrased.
These excerpts support screening and synthesis, not independent replication.

## lu2026duplexsurvey

A Survey of Full-Duplex Spoken Dialogue Systems: Architectural Hierarchy, Interaction Ontology, and Decision State Machine
Analysed artifact: arXiv:2606.19453v1; SHA-256: 04d73c1464fe92b2819faab53f1fe6ec17748addd6cdbf227fb8bff3d76631eb.
Source: https://arxiv.org/pdf/2606.19453v1
Taxonomy axes: none; role: positioning.
Metadata comment (not independent venue verification): 34 pages, 5 figures, 7 tables. Project page and interactive demo: https://github.com/DuplexLM/DuplexSurvey.

> PDF p. 3: §9 + Conclusion + Limitations

> PDF p. 3: Conclusion · Limitations (self-report & L3 unknowns)

## bogavelli2026evabench

EVA-Bench: A New End-to-end Framework for Evaluating Voice Agents
Analysed artifact: arXiv:2605.13841v3; SHA-256: 5afbebfa9df496a216a4a9d61141b9b46d072a45d9595f1c1b8b19abc868c38f.
Source: https://arxiv.org/pdf/2605.13841v3
Taxonomy axes: timing, grounded; role: evaluation.
Metadata comment (not independent venue verification): Accepted to EMNLP 2026 (Findings).

> PDF p. 1: Voice agents are increasingly deployed across enterprise applications. However, no existing benchmark jointly addresses realistic conversation simulation and comprehensive voicespecific evaluation. We present EVA-Bench, an end-to-end evaluation framework that addresses both. On the simulation side, EVABench orchestrates dynamic bot-to-bot audio conversations with automatic simulation validation that detects user simulator error and appropriately regenerates conversations before scoring. On the measurement side, EVABench introduces two composite metrics: EVAA (Accuracy) and EVA-X (Experience).

> PDF p. 2: of dimensions than existing benchmarks provide. Additionally, voice agents are not architecturally uniform: cascade systems chain separate speech-totext (STT), large language model (LLM), and textto-speech (TTS) components, while audio-native systems process audio inputs directly, either end-toend via speech-to-speech (S2S) models, or via hybrid systems that pair a large audio language model (LALM) with a TTS model (full definitions in Appendix A). These architectures have fundamentally different mechanisms, yet must be

> PDF p. 2: metrics. Our contributions: • We introduce EVA-Bench: an end-to-end evaluation framework for voice agents that generates realistic bot-to-bot conversations through

## pahwa2026audio2tool

Audio2Tool: Speak, Call, Act -- A Dataset for Benchmarking Speech Tool Use
Analysed artifact: arXiv:2604.22821v2; SHA-256: c3365e5474f0da450a3d4acaccd985bb8c5a3c169c5bb98dceb96a135669f4c0.
Source: https://arxiv.org/pdf/2604.22821v2
Taxonomy axes: grounded; role: evaluation.
Metadata comment (not independent venue verification): preprint.

> PDF p. 1: Abstract Voice assistants increasingly rely on SpeechLMs to interpret spoken queries and execute complex tasks, yet, existing benchmarks lack domain breadth, acoustic diversity, and compositional reasoning complexity to evaluate tool-calling performance. We introduce Audio2Tool, a large scale dataset comprising 30,000 queries designed to assess tool-calling capabilities of SpeechLMs across three primary domains: Smart Car, Smart Home, and Wearables. Our benchmark features a multitier complexity hierarchy, ranging from simple direct commands

> PDF p. 1: In speech-driven interfaces, a model must not only parse semantic intent but also navigate the inherent phonetic ambiguities and acoustic variabilities of spoken language. While current speech-centric benchmarks such as AudioBench [4], VoiceAgentBench [5] etc., have laid the groundwork for evaluating speech-language models (SLMs), these datasets suffer from limited taxonomic breadth and a lack of acoustic diversity. Many are restricted to high-resource languages or curated laboratory conditions, failing to reflect

> PDF p. 2: 3. Benchmark Agentic tool-oriented interactions require capabilities such as audio-native function calling and mapping speech directly to executable API calls.

## jain2025voiceagentbench

VoiceAgentBench: Are Voice Assistants ready for agentic tasks?
Analysed artifact: arXiv:2510.07978v3; SHA-256: d9a6310f274080b586c83722791da432e73059c0ba63757c61fe0fde8c63bc14.
Source: https://arxiv.org/pdf/2510.07978v3
Taxonomy axes: grounded; role: evaluation.
Metadata comment (not independent venue verification): preprint.

> PDF p. 1: A BSTRACT Large scale Speech Language Models have enabled voice assistants capable of understanding natural spoken queries and performing complex tasks. However, existing speech benchmarks largely focus on isolated capabilities such as transcription or question answering and do not systematically evaluate agentic behavior or adversarial robustness. To address this, we introduce VOICE AGENT B ENCH, a comprehensive benchmark for evaluating SpeechLMs in realistic spoken agentic settings, comprising 6,000+ synthetic spoken

> PDF p. 2: Figure 1: Overview of agentic task categories in VoiceAgentBench. We present representative examples of tool-interaction scenarios covered in the benchmark, including single tool invocation, single tool invocation with retrieval, parallel tool invocation, sequentially dependent tool calls, multi-turn dialogue tool use, and safety evaluation. Examples span both English as well as culturally grounded Indic languages (e.g., Hindi and Marathi). Additional qualitative examples across all task categories are provided in Appendix L.

## xia2026sid

Semantic-Aware Interruption Detection in Spoken Dialogue Systems: Benchmark, Metric, and Model
Analysed artifact: arXiv:2603.24144v1; SHA-256: 925d820ff2dbfb007e1b24a58396f37358f0c4174bf7fd8cf86678b2ace5b40e.
Source: https://arxiv.org/pdf/2603.24144v1
Taxonomy axes: timing; role: evaluation.
Metadata comment (not independent venue verification): Accepted by ICME 2026.

> PDF p. 1: Abstract—Achieving natural full-duplex interaction in spoken dialogue systems (SDS) remains a challenge due to the difficulty of accurately detecting user interruptions. Current solutions are polarized between ”trigger-happy” VAD-based methods that misinterpret backchannels and robust end-to-end models that exhibit unacceptable response delays. Moreover, the absence of real-world benchmarks and holistic metrics hinders progress in the field. This paper presents a comprehensive framework to overcome these limitations. We first introduce SID-Bench, the

> PDF p. 1: To address this, fully automated benchmarks such as full-duplexbench series [17]–[19] and FD-Bench [20] have recently emerged, making significant strides in the systematic evaluation of overlapping speech. However, these advanced works still exhibit several key limitations. Fundamentally, both rely on synthetic data, text generated by LLMs and spoken by TTS. While scalable, this approach fails to capture the intricate blend of timing, prosody, and emotion found in spontaneous human speech,

> PDF p. 2: viding an evaluation framework that not only measures a system’s responsiveness but also, crucially, its ability to differentiate between genuine

## wang2026humdialfd

Full-Duplex Interaction in Spoken Dialogue Systems: A Comprehensive Study from the ICASSP 2026 HumDial Challenge
Analysed artifact: arXiv:2604.21406v2; SHA-256: e0808bdddddcae5d4aa0289280bbb3313f61b774f96a576ca26fe533242e3ea7.
Source: https://arxiv.org/pdf/2604.21406v2
Taxonomy axes: timing, recovery, multiparty; role: evaluation.
Metadata comment (not independent venue verification): 5 pages, 1 figures.

> PDF p. 1: Abstract Full-duplex interaction, where speakers and listeners converse simultaneously, is a key element of human communication often missing from traditional spoken dialogue systems. These systems, based on rigid turn-taking paradigms, struggle to respond naturally in dynamic conversations. The FullDuplex Interaction Track of ICASSP 2026 Human-like Spoken Dialogue Systems Challenge (HumDial Challenge) aims to advance the evaluation of full-duplex systems by offering a framework for handling real-time interruptions, speech overlap, and

> PDF p. 1: or contextual changes. Consequently, system behavior in complex real-world environments often lacks the flexibility and responsiveness required for natural human-like interaction. Although full-duplex interaction has recently attracted increasing attention in both academia and industry, research progress remains constrained by limitations in available datasets and evaluation methodologies. From the perspective of data resources, most public dialogue corpora consist of single-channel recordings or taskoriented scripted interactions that do not fully capture realistic

> PDF p. 3: 5.2. Experimental Results Figure 1: Framework for latency evaluation in interruption scenarios. Latency Evaluation. In addition to evaluating behavioral correctness,

## zhao2026humdial

The ICASSP 2026 HumDial Challenge: Benchmarking Human-like Spoken Dialogue Systems in the LLM Era
Analysed artifact: arXiv:2601.05564v2; SHA-256: 8486a6262040ec52ff5f88ed1f7f429247c9976d6cf0bdf21ea88e82b2fa24fd.
Source: https://arxiv.org/pdf/2601.05564v2
Taxonomy axes: timing, recovery; role: evaluation.
Metadata comment (not independent venue verification): Official summary paper for the ICASSP 2026 HumDial Challenge.

> PDF p. 1: ground. To address this question and provide a fair benchmarking platform, we initiated the first Human-like Spoken Dialogue Systems Challenge (HumDial) at ICASSP 2026. This challenge is designed to assess two tracks of human-like interaction rigorously: (I) Emotional Intelligence, focusing on multi-turn emotional trajectory tracking, causal reasoning, and empathetic response generation; and (II) Full-Duplex Interaction, evaluating the system’s ability to handle interruptions and maintain the natural flow of conversation via

## rajaa2026dualturn

DualTurn: Learning Turn-Taking from Dual-Channel Generative Speech Pretraining
Analysed artifact: arXiv:2603.08216v1; SHA-256: 288056d790f72a0ea0f47e31ca29ad8d743566154e4ec5f5c68419daedc8edaa.
Source: https://arxiv.org/pdf/2603.08216v1
Taxonomy axes: timing; role: system.
Metadata comment (not independent venue verification): Submitted to Interspeech 2026.

> PDF p. 1: Abstract Speech-to-speech models handle turn-taking naturally but offer limited support for tool-calling or complex reasoning, while production ASR–LLM–TTS voice pipelines offer these capabilities but rely on silence timeouts, which lead to unnatural turn-taking. We present DualTurn, which narrows this gap through generative pretraining on dual-channel conversational audio. The model generates both speakers’ future audio autoregressively, implicitly learning conversational dynamics without any labels, and is then fine-tuned to predict interpretable turntaking

> PDF p. 1: latency deployment. However, just detecting speech end is not enough. The model must also anticipate the speaker’s behavior. Voice Activity Projection (VAP) [17] comes closest, offering a self-supervised, dual-channel model that continuously predicts future voice activity from audio alone. But VAP collapses all phenomena into binary voice-activity probabilities and cannot distinguish backchannels from turn ends; its 5.8M-parameter CPC encoder lacks the capacity for semantic modelling and required additional finetuning to

## endpoint2026anticipation

Endpoint Anticipation for Low-Latency Spoken Dialogue
Analysed artifact: arXiv:2606.13450v1; SHA-256: 1e6174f5feb96acc6a760ad072ffca1d877b1ff145635c4276e82c7aec9016c4.
Source: https://arxiv.org/pdf/2606.13450v1
Taxonomy axes: timing; role: system.
Metadata comment (not independent venue verification): Accepted at Interspeech 2026.

> PDF p. 1: Abstract While low-latency interaction is critical for spoken dialogue, cascaded architectures are often bottlenecked by reactive turncompletion detection. We propose Endpoint Anticipation, shifting from reactive detection to proactive forecasting of end-ofturn signals. Our speech-based model anticipates endpoints up to 2.56 seconds in advance, enabling speculative execution of LLM and TTS pipelines on partial context. We introduce metrics to quantify the trade-off between realized latency reduction and computational redundancy. Evaluation across

> PDF p. 1: 1. Introduction Real-time spoken dialogue systems [1] have seen significant growth, driven by advances in large language models (LLMs). These systems [2–9] aim to process audio with low latency to perform complex tasks, often utilizing streaming speech inputs paired with the reasoning capabilities of LLMs to generate responses. While end-to-end training offers a path to low latency [2], many competitive frameworks such as Unmute1 rely on cascaded architectures that control

> PDF p. 2: future voice activity of two speakers to learn general turn-taking abilities, introducing a T URN -S HIFT task to predict

## tau2026multilingual

$τ$-Multilingual: Benchmarking Voice Agents Across Languages
Analysed artifact: arXiv:2609.35820v1; SHA-256: e3a9fc29e2faf80ac79d5376e0a2bf8ad49c81aa3891837588a78aab40b90ebf.
Source: https://arxiv.org/pdf/2609.35820v1
Taxonomy axes: timing, grounded; role: evaluation.
Metadata comment (not independent venue verification): preprint.

> PDF p. 1: ABSTRACT English-only benchmarks expose only a narrow slice of voiceagent behavior. We introduce τ-Multilingual, extending τ-Voice to Spanish, Brazilian Portuguese, Hindi, Korean, and Mandarin with native-speaker review and evaluation of generated language and spoken output. Across 4,500 full-duplex calls and five voice configurations, Spanish, Portuguese, and Hindi remain within 3.2 task-completion points of English, but Korean and Mandarin fall by 14.7 and 8.4 points. The failure modes also vary: Korean

> PDF p. 4: points in Interaction. We do not interpret Generation ranges because Naturalness is not calibrated across languages. • Latency: Higher-reasoning configurations show longer turntaking latency (GPT: 1.12–1.42 s; Gemini: 1.34–1.82 s). Mean call durations are 11.7–14.2 min for GPT/Gemini versus 24.7 min for Grok. 4.6. Validation and Robustness Pooled validation micro-F1 is 97.7% for tool use, 89.4% for naturalness, and 90.2% for speech fidelity; the remaining Interaction components are deterministic. Among

## duplex2026mpe

Duplex-MPE: Benchmarking Multi-Party Interaction in Full-Duplex Dialogue
Analysed artifact: arXiv:2609.31948v1; SHA-256: 125f7c66e2d7b1c6d7e60051abb4028ce5535cc03362d53c4f263c49c7ca265d.
Source: https://arxiv.org/pdf/2609.31948v1
Taxonomy axes: timing, multiparty; role: evaluation.
Metadata comment (not independent venue verification): 27 pages, 3 figures. Project page: https://step-out.github.io/Duplex-MPE-Page/.

> PDF p. 1: Abstract Real-time full-duplex speech models can listen while speaking, enabling natural interaction without rigid turn boundaries. Existing benchmarks evaluate turn-taking, interruption handling and multi-round dialogue, but largely centre on a designated user rather than an assistant participating in a shared conversation among several people. We introduce DuplexMPE to evaluate when such an assistant should answer, remain silent or stop speaking. The benchmark contains 2,000 scenarios with three or four human

> PDF p. 2: Figure 1: Duplex-MPE overview: turn types (left), audio input and metrics (top right), and N4 timing (bottom right). backchannels, side conversations and background speech by introducing overlap into an ongoing user–assistant exchange (Lin et al., 2026a). HumDial includes third-party speech and speech directed at others, but evaluates whether the model rejects these utterances while serving a designated user (Wang et al., 2026). These benchmarks test important duplex behaviours, yet leave

## turnbench2026

TurnBench: A Multi-Domain Benchmark for Turn-Taking Dynamics in Spoken Dialogue
Analysed artifact: arXiv:2608.25218v2; SHA-256: 673cd7d6b5680140b36cbdf7fbc3daffe807e4146fd297d9359dde3dc84b05c3.
Source: https://arxiv.org/pdf/2608.25218v2
Taxonomy axes: timing; role: evaluation.
Metadata comment (not independent venue verification): 8 pages, 2 figures. Accepted to IEEE SLT 2026. v2: camera-ready version.

> PDF p. 1: Abstract—Speakers in natural conversation take turns speaking and listening, deciding in real time when to take, hold, or yield the floor. However, turn-taking evaluation remains limited due to the lack of a consistent, linguistically grounded evaluation protocol and hand-annotated data covering diverse conversation types. To address this, we present T URN B ENCH, a multi-domain benchmark that pairs a 30-hour, hand-labeled corpus of dyadic human conversation with a standardized evaluation

> PDF p. 1: Fig. 1: The turn-taking events T URN B ENCH scores, for two speakers (S1, S2). Dotted lines are human-labeled gold events. Solid lines are model-emitted events, which are true positives (green) inside the solid scoring windows and false positives (red) inside the dashed scoring windows. There are two successful detections, as well as two false positives during a mid-turn pause and on a backchannel. A similar issue affects evaluation. Full-duplex

> PDF p. 2: Evaluation frameworks share a related limitation: their categories are not derived from the conversation-analytic definitions motivating the phenomena they target.

## chen2025mmedfd

MMedFD: A Real-world Healthcare Benchmark for Multi-turn Full-Duplex Automatic Speech Recognition
Analysed artifact: arXiv:2509.19817v3; SHA-256: 5262ccc332d538dab43deeea60b657b1ea259678b6a99a7d672a639d52c143b7.
Source: https://arxiv.org/pdf/2509.19817v3
Taxonomy axes: component; role: evaluation.
Metadata comment (not independent venue verification): preprint.

> PDF p. 1: ABSTRACT Automatic speech recognition (ASR) in clinical dialogue demands robustness to full-duplex interaction, speaker overlap, and low-latency constraints, yet open benchmarks remain scarce. We present MMedFD, the first real-world Chinese healthcare ASR corpus designed for multi-turn, full-duplex settings. Captured from a deployed AI assistant, the dataset comprises 5,805 annotated sessions with synchronized user and mixed-channel views, RTTM/CTM timing, and role labels. We introduce a model-agnostic pipeline for streaming segmentation, speaker

> PDF p. 1: generation for patient care and auditing [2, 3]. ASR remains challenged by real-world healthcare dialogue with multi-turn and highly dynamic content. These conversations include frequent interruptions and overlapping speech and require reliable speaker diarization. Streaming systems also need robust context tracking, recovery after barge-in, and low latency [4]. Recent full-duplex dialogue systems coordinate listening and speaking via learned controllers and substantially reduce latency relative to half-duplex interaction [5]. This motivates

> PDF p. 2: 1. We release a real-world Chinese healthcare dialogue corpus with multi-turn structure, collected with consent and de-identified, annotated with role

## purwar2026judges

Benchmarking LLM Judges for Voice-Agent Evaluation: Reliability, Calibration, and Human Oversight
Analysed artifact: arXiv:2608.24314v2; SHA-256: 5ae4b3c29209d4ba8125572c18107a9fb0e93c18a981bd7392bb7c575fcc1438.
Source: https://arxiv.org/pdf/2608.24314v2
Taxonomy axes: none; role: meta_evaluation.
Metadata comment (not independent venue verification): Extends LLM-as-a-Judge to voice agents across telecom and retail, testing GPT-4.1, GPT-5 and Claude against human raters across 10 safety and efficiency metrics. A correlation-based calibration analysis reveals domain-dependent reliability and identifies Recovery Turn Count and safety-recall metrics as unreliable for fully automated judging.

> PDF p. 1: Abstract—Evaluating conversational voice agents at scale requires reliable assessment methods that capture both observable interaction quality and the contextual judgment typically provided by human evaluators. We investigate LLM-as-a-Judge evaluation by comparing human judgments with GPT-4.1 and GPT-5 on telecom and retail voice-agent conversations, across conversational quality and safety dimensions. The same interactions are scored under three evaluation configurations, p0, p1, and p2, to test whether automated judgments are sensitive to

> PDF p. 1: I. I NTRODUCTION Evaluating conversational voice agents has traditionally relied on human evaluation, which, while providing a reliable measure of interaction quality, is expensive, time-consuming, subjective, and difficult to scale across large volumes of conversations [1] [2] . With the recent advances in Large Language Models (LLMs), automated evaluation using LLMs as judges has emerged as a promising alternative for assessing open-ended conversations across multiple quality dimensions [3] [4]. Prior

> PDF p. 2: characteristics such as domain expertise, ambiguity, and communication behavior. • p2 (dynamically inferred context) - Context Injection: The agent receives

## lee2026hear

HEAR Who Said What: Unlocking Speaker-Attributed Reasoning via Counterfactual Voice Grounding
Analysed artifact: arXiv:2608.29120v1; SHA-256: ba98d412c64bac28c8cae83809bdcac7bd7a568da11a55f1d6ec9b629c56cfe6.
Source: https://arxiv.org/pdf/2608.29120v1
Taxonomy axes: multiparty; role: evaluation.
Metadata comment (not independent venue verification): EMNLP2026 Main Conference.

> PDF p. 1: Abstract Speech Language Models (SLMs) are increasingly deployed in multi-speaker environments, yet their ability to attribute speech to the correct speaker and reason over speaker identities remains unclear. Hence, we introduce HEAR, a conceptually hierarchical benchmark diagnosing the foundational capabilities of speakerattributed reasoning, comprising 2.4K humanverified samples from 887 diverse multi-party audio clips. Evaluating 20 leading SLMs on HEAR reveals they struggle with these foundational tasks, often relying on semantic

> PDF p. 1: foundational abilities required to support it. This makes it difficult to localize where models actually fail: whether they struggle to discriminate between distinct voices, attribute utterances to the correct speakers, or simply lack the reasoning competency for the downstream task. To address this gap, we introduce a benchmark, HEAR, designed to evaluate the foundational abilities underlying speaker-attributed reasoning in SLMs. HEAR is grounded in Erber’s Auditory Hierarchy (Erber, 1982), which

> PDF p. 2: (Figure 2-(A)), CASH yields hard negatives where the correct answer flips solely based on vocal cues, thereby compelling models to

## mitra2026adaptive

Adaptive Turn-Taking for Real-time Multi-Party Voice Agents
Analysed artifact: arXiv:2606.13544v3; SHA-256: f53641eb11981cf0fbc6636a80fb7ca89f340fad924f42aee1ca0a4d00ad7380.
Source: https://arxiv.org/pdf/2606.13544v3
Taxonomy axes: timing, multiparty; role: system.
Metadata comment (not independent venue verification): Accepted for publication at Interspeech 2026.

> PDF p. 1: based, multi-party interaction has been largely overlooked. In this work, we introduce ModeratorLM, a role-playing voice agent for multi-party conversations that conditions both turn-taking decisions and response generation on an explicitly assigned role. Our system is built on a speech LLM that processes multi-speaker audio streams and corresponding text hypotheses in chunk-wise streaming manner. To our knowledge, this is the first role-conditioned voice agent designed for multi-party conversational settings. To

> PDF p. 3: sation context together with the audio chunk under evaluation before invoking generation. Greedy decoding is used by default. When a thinking control token (<think>) is emitted, we switch to sampling mode to generate the reasoning tokens. Similarly, upon emitting a turn-taking control token, sampling is used to generate the assistant’s response. Sampling is performed with Temperature=0.7, TopP=0.8, and TopK=20. Evaluation Metrics. We evaluate predicted turn-taking decisions against ground-truth annotations at

> PDF p. 4: 5. Conclusions In this work, we introduced a role-playing voice agent for multi-party conversations that modulates turn-taking behavior based on

## ceccatelli2026speechjbb

SpeechJBB: Probing Safety Alignment and Comprehension in Large Audio Language Models under Code-Switched Speech
Analysed artifact: arXiv:2606.06037v3; SHA-256: 0c138b1cf233cacd36747fb5f5e9cf5d6d47bc5e78317e155d06200df40eb8d4.
Source: https://arxiv.org/pdf/2606.06037v3
Taxonomy axes: component; role: evaluation.
Metadata comment (not independent venue verification): Accepted to Findings of EMNLP 2026.

> PDF p. 1: Large audio language models (LALMs) are increasingly deployed in real-world applications, yet their safety alignment is still primarily evaluated on monolingual, text-based harmful prompts. This leaves their generalizability under multilingual and spoken settings, particularly code-switched speech, largely underexplored. To address this gap, we introduce SpeechJBB, an audio jailbreak dataset for benchmarking state-of-the-art LALMs across five European languages: English, French, German, Italian, and Spanish, as well as codeswitched variants combining pairs

> PDF p. 1: Large language models (LLMs) have rapidly transitioned from research prototypes to foundational components of modern digital infrastructure, underpinning conversational agents and search platforms. Yet, their widespread adoption has simultaneously intensified concerns surrounding safety, reliability, and alignment with human values (Hendrycks et al., 2021; Bommasani et al., 2022). Previous studies have shown that current models remain susceptible to adversarial prompting strate-

> PDF p. 2: world multilingual communication is rarely strictly monolingual. Instead, speakers frequently engage in code-switching, which is the alternation between multiple languages within a single utterance (Zhang et al., 2023). Such mixing

## braun2026voicelight

Voice-Light: A Full-Duplex Cascaded Voice Agent with Causal Turn-Taking and Speculative Generation
Analysed artifact: arXiv:2609.20995v1; SHA-256: 73951bb3e3c4eba37cc83e11e3aed04e44000fd72b2b62cecf54448e8f9b1b3b.
Source: https://arxiv.org/pdf/2609.20995v1
Taxonomy axes: timing, recovery; role: system.
Metadata comment (not independent venue verification): 9 pages, 4 figures, 6 tables. Code, datasets, and model artifacts: https://github.com/BertilBraun/Voice-Light ; live demo: https://voice.bertil-braun.de.

> PDF p. 1: Abstract Natural spoken interaction requires more than streaming ASR, language generation, and speech synthesis: a system must react to overlap without canceling on every acknowledgment, prepare a response before a turn is certain, and ensure canceled audio cannot enter conversation history. We present Voice-Light, a full-duplex cascaded voice agent that combines immediate acoustic onset, a causal adapter sharing a streaming ASR encoder, reversible playback control, and private speculative response generation.

## shamsaie2026tact

Neither Silence nor Overlap Is Failure: Intent-Conditioned Evaluation of Turn-Taking in Full-Duplex Spoken Dialogue Models
Analysed artifact: arXiv:2609.27372v1; SHA-256: 73147de353cd5718d0f2eeab8b859ad11953af1aa905a378f513aac3e91b6ebc.
Source: https://arxiv.org/pdf/2609.27372v1
Taxonomy axes: timing; role: evaluation.
Metadata comment (not independent venue verification): Accepted to IEEE SLT 2026.

> PDF p. 1: People Make Things {k,i}@peoplemakethings.com Abstract—Benchmarks for full-duplex spoken dialogue models score turn-taking with binary fixed-window rules that reward immediate response or silence by completeness of the prior turn. We argue that the appropriateness of a response offset, whether delayed silence or anticipatory overlap, is conditional on the speaker’s latent intent, identifiable only from that speaker’s behavior. We introduce TACT, a benchmark of 9,728 episodes and 73.2 hours from five dyadic

> PDF p. 1: offset therefore depends on the speaker’s latent intent: the same trailing-off question followed by 1.5 s of silence can demand an immediate answer from one speaker and forbid one from another, and the same mid-clause incoming can be cooperative or disruptive. Crucially, intent is often identifiable only from that speaker’s behavior across interactions, because speakers differ systematically in pause tolerance, backchannel solicitation, and floor-holding style [15], [16]; an evaluation blind

> PDF p. 2: is essentially invariant to the speaker profile while held-out human behavior is not, and the TACT composite correlates with held-out

## zhang2026vgbench

Do Audio LLMs Listen Before They Act? Diagnosing Acoustic-Context Gating in Voice Agents
Analysed artifact: arXiv:2609.32536v1; SHA-256: 71658ea5beea1cf5f9485d825f57b8a545e7645a5ff5bbe79fe9a45e30a8d6db.
Source: https://arxiv.org/pdf/2609.32536v1
Taxonomy axes: grounded, multiparty; role: evaluation.
Metadata comment (not independent venue verification): preprint.

> PDF p. 1: A BSTRACT Audio language models can recognize spoken commands and invoke tools, but an agent must first decide whether the acoustic and conversational context warrants action. We introduce VGB ENCH, a 1,018-item diagnostic benchmark for action-level addressedness across side-talk, self-talk, and speaker-switch scenarios. Each item uses a shared action space comprising silence, a tool call, and a natural-language answer. Speaker-switch pairs hold the specified words fixed while source, distance rendering,

## indic2026fdb

IndicFDB: Benchmarking Full-Duplex Voice Agents across Indian Languages
Analysed artifact: arXiv:2609.31967v1; SHA-256: 6ae1aec9f56a429efe9d37236cd6f2b64bbfb308efa05a6139dd5afe41bd5a91.
Source: https://arxiv.org/pdf/2609.31967v1
Taxonomy axes: timing, recovery; role: evaluation.
Metadata comment (not independent venue verification): preprint.

> PDF p. 1: ABSTRACT Full-duplex voice agents must handle pauses, take turns, backchannel, and respond to user interruptions in real time. Full-DuplexBench evaluates these behaviors, but its English-only corpus and reliance on word-timestamped ASR and an English-prompted LLM judge make it difficult to extend to Indian languages. We introduce IndicFDB, which extends it to ten languages spoken in India with 12,350 samples, nearly 17 times as many as the original. We address three

> PDF p. 1: and to evaluate agent timing, and prompts GPT-4o in English to judge the relevance and quality of agent responses to user interruptions. Ohashi et al. [3] instead use voice activity detection (VAD) to mine samples and define heuristic rewards that improve the same dynamics. We introduce IndicFDB, a full-duplex benchmark covering ten languages spoken in India: Indian English, Hindi, Bengali, Punjabi, Gujarati, Marathi, Kannada, Telugu, Tamil, and Malayalam. We retain

> PDF p. 2: FDB’s word-level timestamping tools do not cover all ten languages [2], we rely on VAD-based heuristics as in [3]. Based

## french2026fdb

From Metrics to Natural Dialogue: French Full-Duplex Benchmark for Spoken Dialogue Models
Analysed artifact: arXiv:2609.10765v1; SHA-256: 09de86078ed9848e3618dfa0b003d2939fe7c62f8a84ac634429cf33dc7a1af8.
Source: https://arxiv.org/pdf/2609.10765v1
Taxonomy axes: timing, recovery; role: evaluation.
Metadata comment (not independent venue verification): 9 pages, 0 figures. Accepted for publication in Proceedings of the Conference on Empirical Methods in Natural Language Processing (EMNLP): Industry Track, 2026.

> PDF p. 1: Abstract Full-duplex spoken dialogue models aim to make voice agents more natural by allowing them to listen, speak, pause, and respond during ongoing conversation. However, it is not clear whether full-duplex benchmarks behave the same way when models are evaluated in a different language. To investigate this, we introduce a French full-duplex benchmark (FDB) with two variants, CALLFC-FDB for Canadian French and MEDIA-FDB for European French, and compare them with

> PDF p. 2: marks have expanded evaluation beyond English (Ma et al., 2025), dedicated benchmarks for French full-duplex dialogue are still missing. French also contains language-specific interactional cues such as euh, ben, ouais, and d’accord, which do not map directly onto English translations. Their meanings and conversational functions depend on context, prosody, and turn-taking. In addition, some existing FDB tasks are based on synthetic speech, which may not fully reflect the variability of

## floor2026necessity

Full-Duplex Speech Models Take the Floor When Asked, Not When Needed
Analysed artifact: arXiv:2609.19596v1; SHA-256: 86f52ee419f03a7e1284472fe9b46cf85b7278adf2282877a0cee2e384798eba.
Source: https://arxiv.org/pdf/2609.19596v1
Taxonomy axes: timing; role: evaluation.
Metadata comment (not independent venue verification): 5 pages.

## zhao2026echo

Same Words, Different Actions: Paired Turn-Taking Evaluation under Rewritten Dialogue Contexts
Analysed artifact: arXiv:2609.17360v2; SHA-256: e19b36a70b7cd7c468487eed89acaf094181cdb508e8244bcb196aa3352ff167.
Source: https://arxiv.org/pdf/2609.17360v2
Taxonomy axes: timing; role: evaluation.
Metadata comment (not independent venue verification): preprint.

> PDF p. 1: Zuoyebang Education Technology ABSTRACT Real-time spoken dialogue systems must distinguish interruptions that require yielding the floor from backchannels that permit continued speaking. Existing benchmarks typically score events independently and may therefore assign high scores to systems with fixed action preferences rather than context-sensitive decision policies. We introduce ECHO, a paired diagnostic benchmark for Chinese turn-taking evaluation. ECHO pairs examples with the same overlap transcript but contrasting preceding multi-turn dialogue contexts,

> PDF p. 2: cling (Fig. 1). The insertion transcript alone therefore does not determine whether the system should yield or continue. This raises our central question: can a spoken dialogue system produce appropriate Y IELD/K EEP decisions across rewritten contexts that share the same insertion transcript? We introduce ECHO (Evaluating Context-conditioned Handling of Overlaps), a paired diagnostic set of Chinese multi-turn dialogues. Linked ECHO instances share the same insertion transcript but use rewritten

> PDF p. 4: Sample-level accuracy can overestimate reliability when a model strongly favors a single action. We therefore define the Pairwise Action Success

## mathur2026dsbifeval

DuplexSpeechBench-IFEval: Evaluating Implicit Instruction Following in Full-Duplex Voice Agents
Analysed artifact: arXiv:2609.03423v2; SHA-256: e6c0ecae82ab1058585130e445b952c5e797533d76c70e3a0fee4b077e7da1f7.
Source: https://arxiv.org/pdf/2609.03423v2
Taxonomy axes: timing; role: evaluation.
Metadata comment (not independent venue verification): Under Submission at ICLR 2027.

> PDF p. 1: A BSTRACT Full-duplex voice agents must continuously decide when to speak, listen, backchannel, interrupt, overlap, and yield the conversational floor. Existing benchmarks evaluate these behaviors through explicit turn-management instructions, whereas voice agents are often configured through roles or personas from which appropriate conversational behavior must be inferred. We introduce DuplexSpeechBench–IFEval (DSB-IFEval), a benchmark for evaluating implicit instruction following in realtime spoken interaction. DSB-IFEval comprises 1,038 test cases derived from 240

> PDF p. 2: models can follow explicit natural-language instructions governing when to interrupt, backchannel, listen, or continue. In practical deployments, however, these behaviors are often not specified as explicit rules. Voice agents are instead configured through roles or personas—such as a tutor, counselor, dispatcher, or interpreter—from which the appropriate conversational behavior must be inferred. This adds a distinct challenge: the model must first infer how the role should behave and then execute that

> PDF p. 3: We introduce DuplexSpeechBench–IFEval benchmark for evaluating instruction following in fullduplex voice agents. We use full-duplex behavior policy to denote the

## hu2025vcb

VCB Bench: An Evaluation Benchmark for Audio-Grounded Large Language Model Conversational Agents
Analysed artifact: arXiv:2510.11098v5; SHA-256: fbc38c4f5b8e99fb8de6795aaeea44fe01e36a3c492594459e685276cdc63f03.
Source: https://arxiv.org/pdf/2510.11098v5
Taxonomy axes: component; role: evaluation.
Metadata comment (not independent venue verification): 25 pages, 9 figures, accepted by ACL 2026 Findings.

> PDF p. 1: Abstract While large audio language models (LALMs) have driven significant progress in multimodal conversational systems, current benchmarks suffer from critical limitations: they are largely English-centric, use synthetic speech, and fail to provide comprehensive, discriminative evaluation across key dimensions. To fill this gap, we present Voice Chat Bot Bench (VCB Bench), a novel, high-quality Chinese benchmark built exclusively on real human speech. VCB Bench assesses LALMs across three complementary axes: instruction

> PDF p. 1: combine speech signal processing with language modeling—have developed rapidly. Emerging systems such as Step-Audio 2 (Wu et al., 2025) and Qwen3-Omni (Xu et al., 2025b) demonstrate endto-end (E2E) speech understanding and generation with capabilities in voice question answering, realtime conversation, and audio content analysis. Consequently, voice conversational agents powered by LALMs are drawing increasing academic and industrial attention, offering more natural and humanlike interactions than text-only systems. Despite these advances,

> PDF p. 2: VCB Bench assesses LALMs across three complementary dimensions: (1) Instruction Following: This extends beyond text-based prompts to include speech-level control

## sharon2026less

Less can be More: What Aspects of Speech Drive End-of-Turn Detection
Analysed artifact: arXiv:2609.11066v1; SHA-256: 334d0e56da5215e3761d8d77dca7f21f83c185a59ccfe852b5c6a0b4e762bfdf.
Source: https://arxiv.org/pdf/2609.11066v1
Taxonomy axes: timing; role: analysis.
Metadata comment (not independent venue verification): preprint.

> PDF p. 1: Abstract In conversational AI, detecting when a speaker has finished talking is crucial for natural turn-taking. While recent work incorporates semantics, the relative contribution of different modalities remains unclear. We present a controlled ablation of acoustic, prosodic, and semantic signals for streaming endof-turn detection using a lightweight trimodal classifier. Under identical training conditions, the acoustic–prosodic combination achieves the best balance of accuracy and latency, achieving utterance F1 of 0.93 with

> PDF p. 1: 1. Introduction In modern voice-driven AI systems, determining when a user has finished speaking is an important component that defines how natural an interaction feels. This end-of-turn (EOT) detection task presents a fundamental trade-off: reacting too early risks interrupting the user, while waiting too long creates unnatural delays that break conversational flow. Poor EOT detection degrades user experience, reduces task completion rates, and limits the usability of voice interfaces in

> PDF p. 4: dates only at non-blank decoder emissions, leaving the representation unchanged across the majority of frames (only the positional encoding changes).

## hu2026frontendbackend

A frontend-backend architecture for tool calls in full-duplex speech models
Analysed artifact: arXiv:2609.19334v2; SHA-256: 6d5fc1902b580e219ddb567e1a95463589a635d633f599bd9a992f9b5cb40cac.
Source: https://arxiv.org/pdf/2609.19334v2
Taxonomy axes: timing, grounded; role: system.
Metadata comment (not independent venue verification): To be submitted to ICASSP'27.

> PDF p. 3: followed by Irrelevance. We also compute tool-call token recall as the fraction of positive tool-call utterances for which the frontend correctly fires the delegation token. Our frontend achieves recall of 97.2%, 92.0%, 95.0%, and 93.5% on Simple, Multiple, Parallel, and Parallel Multiple, respectively. 5.1.2. Full-Duplex-Bench v3 Whereas BFCL contains continuous and fluent TTS-generated user speech, Full-Duplex-Bench v3 (FDB3) [58] consists entirely of naturalistic real human recordings. The corpus contains 100

> PDF p. 4: and use GPT-5.2 to role-play the caller. To adapt to our infrastructure and improve inference availability, we synthesize user text turns with Chatterbox-TTS [59], and the synthesized user speech is streamed chunk by chunk to the frontend implemented using Triton Inference Server [60]. We use GPT-5.2 as the LLM judge for all metrics. To focus on evaluating the quality of our frontend’s STT text output and to compare with other

> PDF p. 4: compute the full result for prefilling. We did not optimize the prefill or serving infrastructure to specifically reduce latency in

## hu2026transcription

Enabling Streaming User Transcription in Full-Duplex Speech-to-Speech Models
Analysed artifact: arXiv:2609.15759v1; SHA-256: 6d2886cf2b2e5dcd53f2e9cf9a0758b607b5f632e9810b43b006406428e10346.
Source: https://arxiv.org/pdf/2609.15759v1
Taxonomy axes: component; role: system.
Metadata comment (not independent venue verification): preprint.

> PDF p. 1: detection and turn-taking modules, but fundamentally rely on explicit turn detection rather than simultaneous processing. Recently, full-duplex S2S models have emerged that enable simultaneous listening and speaking. Moshi [27] and PersonaPlex [28] are full-duplex conversational models that jointly model both user and agent audio streams with depthbased attention mechanisms, but require extensive speech-text pretraining from scratch and do not provide streaming user transcription capabilities. Other approaches like SyncLLM [29] and

> PDF p. 3: a wide range to enable the model to handle various acoustic environments. B. Streaming ASR Head We augment the duplex S2S architecture by introducing a streaming ASR module in parallel to the existing agent text head. This module consists of both a separate embedding layer and a prediction head for user transcription. Both layers are initialized from the original corresponding LLM backbone layers. As illustrated in Figure 1, the ASR

> PDF p. 5: C. Standalone Streaming ASR We also train a standalone streaming ASR model using the same architecture but without the agent

## zhong2026iraf

IRAF: Interference-Resilient Adaptive Fusion for Noise-Robust End-to-End Full-Duplex Spoken Dialogue Systems
Analysed artifact: arXiv:2606.06559v1; SHA-256: 23159fc079cbba86eea4807368b7d44556510ea826ab3b9473b6600fa55bb671.
Source: https://arxiv.org/pdf/2606.06559v1
Taxonomy axes: component, timing; role: system.
Metadata comment (not independent venue verification): preprint.

> PDF p. 1: Abstract Full-duplex spoken dialogue models allow voice agents to listen and speak concurrently, enabling natural interaction with real-time overlap. However, end-to-end dual-channel models that jointly encode user and agent streams may degrade in realistic acoustic environments: interfering speakers leaking into the user microphone can be encoded as part of the user query, corrupting the LLM’s conditioning and causing unstable turntaking and reduced response quality. We propose InterferenceResilient Adaptive Fusion (IRAF),

> PDF p. 1: Figure 1: Full-duplex dialogue in (a) clean and (b) noisy conditions. Interference leaking into the user channel can corrupt conditioning, causing unstable turn-taking and false barge-in. conditions, their robustness can degrade substantially in realworld acoustic environments. For instance, when interfering speakers leak into the user microphone, their speech can be encoded into the user stream and inadvertently treated as part of the user query, thereby contaminating the LLM’s conditioning context.

> PDF p. 2: Figure 2: Overview of the proposed E2E full-duplex model with the Interference-Resilient Adaptive Fusion (IRAF) module. A streaming speech encoder

## tyagi2026steerduplex

SteerDuplex: Steerable Duplex Speech Dialogue Models
Analysed artifact: arXiv:2609.12623v1; SHA-256: c29d2b1042dfa6281f07c114740f989dc68cdc53d1e6aaef3709e6806984e375.
Source: https://arxiv.org/pdf/2609.12623v1
Taxonomy axes: component, timing, recovery; role: system.
Metadata comment (not independent venue verification): 24 pages, 7 figures.

> PDF p. 1: Abstract Full-duplex spoken dialogue models support low-latency turn taking, interruption handling, and backchanneling, yet a key capability remains underexplored: steerability, the ability to reliably shift conversational behavior along attributes such as tone, persona, speaking rate, and voice style in response to user instructions. We introduce a taxonomy of text- and audio-based steerability that identifies substantial gaps in current full-duplex models. To address this gap, we introduce S TEER D UPLEX,

> PDF p. 2: Full-duplex systems listen and speak simultaneously, enabling turn taking, backchanneling, and interruption handling within an ongoing conversation [8, 15, 37]. Early systems established joint two-channel modeling [25] while later work improved synchronization and stream interleaving [36, 39]. Fluent turn taking does not guarantee that systems follow user instructions about tone, persona, or delivery. Hence, a useful interactive system must also be steerable along such attributes. Recent role- and voice-conditioned models

> PDF p. 3: the same judge, M OSHI and P ERSONA P LEX reach audio-steering average pass rates of only 20.55% and 16.44%,

## he2026conversationalvoice

ConversationalVoice: Full-Duplex Speech Data from Real Conversations through Source-Faithful Reconstruction and Conversation-Grounded Expansion
Analysed artifact: arXiv:2609.08147v1; SHA-256: 36f8866f409d626018bd12ea31cffcc7bcc1dc11c6bf7f71daf49097cd7c2fd2.
Source: https://arxiv.org/pdf/2609.08147v1
Taxonomy axes: timing; role: data.
Metadata comment (not independent venue verification): 12 pages, 3 figures, 1 table, preprint.

> PDF p. 1: Abstract Full-duplex speech models require training data that preserves turn-taking, overlap, interruption, and backchannel behavior, yet these signals are entangled across speakers in noisy realworld recordings. We present ConversationalVoice, a pipeline that converts real two-speaker excerpts into three complementary training-data artifacts. (1) Separation recovers speakerspecific tracks with stable speaker assignments, a canonical transcript, and naturally observed interaction timing. (2) Reconstruction generates speech in matched voices from a fixed source transcript,

> PDF p. 1: plicitly, while related benchmarks systematically evaluate them [1–3]; yet real conversations usually arrive as noisy monaural recordings, while prompt-generated dialogue can lose the timing and interaction patterns of actual exchanges. We present ConversationalVoice, an end-to-end pipeline that transforms real-world two-speaker audio excerpts into three complementary forms of full-duplex training data. Qualityverified separation combines diarization, dialogue separation, stable speaker-slot assignment, signal and identity checks, and ASR to recover speaker-specific tracks with

## deng2026qwenagent

Qwen-Audio-Agent Technical Report
Analysed artifact: arXiv:2609.25195v1; SHA-256: bec103d47eee627b8d9c47d90da101f00dc694e3c0775b16bcb92b396034341c.
Source: https://arxiv.org/pdf/2609.25195v1
Taxonomy axes: recovery, grounded; role: system.
Metadata comment (not independent venue verification): preprint.

> PDF p. 1: Abstract We present Qwen-Audio-Agent, a harness that combines full-duplex voice interaction with asynchronous task execution through a foreground–background architecture. A Frontend Agent manages dialogue and selects between direct tool use and delegation, while a Backend Agent carries out delegated tasks in a separate context. An Orchestration Runtime maintains task state, coordinates requests for user input and authorization, and schedules the return of results to the conversation. The runtime separates speech

## yan2026hearbias

HEAR: Real Voices, Real Bias: A Large-Scale Human-Recorded, Demographically Diverse Benchmark for Audio Language Models
Analysed artifact: arXiv:2609.35952v1; SHA-256: 7f0d121621fdeda82e090ee73f909bece0b3a0f2872ad8c718203f0113aa8ba2.
Source: https://arxiv.org/pdf/2609.35952v1
Taxonomy axes: component; role: evaluation.
Metadata comment (not independent venue verification): preprint.

> PDF p. 1: ABSTRACT We introduce HEAR (Human-recorded Evaluation of AudioLLM bias by Real speakers), a large-scale, ecologically valid benchmark comprising 87k real human audio samples from 843 demographically diverse participants. HEAR enables comprehensive evaluation through Multiple Choice Question Answering (MCQA) and open-ended long-form tasks. To our knowledge, this is the first large-scale voice benchmark grounded entirely in authentic human speech. We evaluate model behavior across both real-time speechto-speech and speech-to-text architectures. Our

> PDF p. 1: built on real human voices currently exists, and none evaluates both speech-to-speech and speech-to-text architectures. To address the above gaps, in this work, we propose a voice bias benchmark that consists of all real human recorded audios with diverse demographic representation of the speakers, and the three main contributions: • We introduce and open-source 1 the HEAR (Humanrecorded Evaluation of Audio bias by Real speakers) benchmark dataset, the first large-scale,

> PDF p. 3: where C(qi+ ) and C(qi− ) are the response categories for the non-negative and negative versions of question i, Gspeaker

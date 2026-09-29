| System | Architecture | Timing (T) | Recovery (R) | Grounded Outcome (G) | TRG Compliant | Warnings | Source |
|---|---|---|---|---|---|---|---|
| Google gemini-live-2.5-flash-native-audio | end_to_end | 1.14s / mean | Responsiveness 69%; Interrupt Rate 21%; Selectivity 54% | 26% | yes | 1 | `trg_example_gemini_live.yaml` |
| xAI grok-voice-agent | end_to_end | 1.15s / mean | Responsiveness 83%; Interrupt Rate 84% (highest in the benchmark - interrupting users nearly once per turn); Selectivity 57% (best in the benchmark) | 38% | yes | 1 | `trg_example_grok_voice.yaml` |
| NemotronLabs VoiceChat | end_to_end | not separately reported as a latency figure in the surveyed text / mean | 100% correct takeover on genuine interruption (FDB v1.0); 93% resumption after backchannels (FDB v1.5) | 82.5% | yes | 1 | `trg_example_nemotron.yaml` |
| OpenAI gpt-realtime-1.5 | end_to_end | 0.90s / mean | Responsiveness 100%; Interrupt Rate 14% (turns where the agent speaks before the user finishes); Selectivity 6% (correctly ignoring backchannels/vocal tics/non-directed speech) | 35% | yes | 1 | `trg_example_openai_realtime.yaml` |

"""Regression tests for the opt-in reference protocol (not agent experiments)."""
import copy
import math
from pathlib import Path
import tempfile
import unittest

from trg_eval.protocol import analyze, main, quantile


def episode(system="alpha", condition="clean", case="case-1", **changes):
    row = {
        "protocol_version": "trg-ref-0.1", "system": system,
        "system_version": "fixture-only", "conditions_id": "fixture-en-quiet",
        "task_id": "update", "case_id": case, "repeat": 0,
        "condition": condition, "evidence_kind": "synthetic", "status": "ok",
        "user_end_ms": 1000, "first_audio_ms": 1250, "deadline_ms": 10000,
        "timing_appropriate": True, "no_action": False,
        "expected_state": {"quantity": 2}, "actual_state": {"quantity": 2},
        "expected_actions": ["update:2"], "actions": ["update:2"],
        "expected_recovery_state": {"quantity": 2},
        "actual_recovery_state": {"quantity": 2},
        "trace_ref": "synthetic://fixture",
    }
    row.update(changes)
    return row


def paired():
    return [episode(condition=condition) for condition in ("clean", "interruption")]


class ProtocolTests(unittest.TestCase):
    def test_latency_uses_explicit_clock_anchors(self):
        result = analyze(paired(), bootstrap=50)
        self.assertEqual(result["groups"][0]["latency_ms"]["p50"], 250)
        self.assertFalse(result["empirical_evidence"])
        self.assertIn("SYNTHETIC", result["warning"])

    def test_failure_stays_in_denominator(self):
        rows = paired() + [episode(case="case-2", condition=condition,
                                  status="timeout", first_audio_ms=None,
                                  actual_state={}, actions=[], timing_appropriate=None,
                                  actual_recovery_state=None)
                           for condition in ("clean", "interruption")]
        group = analyze(rows, bootstrap=50)["groups"][0]
        self.assertEqual(group["grounded_success"]["estimate"], 0.5)
        self.assertEqual(group["n"], 2)
        self.assertEqual(group["latency_ms"]["n_observed"], 1)
        self.assertEqual(group["no_response_rate"]["estimate"], 0.5)

    def test_paired_recovery_drop_and_grounded_outcome(self):
        rows = paired()
        rows[1]["actual_state"] = {"quantity": 1}
        rows[1]["actual_recovery_state"] = {"quantity": 1}
        result = analyze(rows, bootstrap=50)
        self.assertEqual(result["recovery_deltas"][0]["grounded_success_delta"]["estimate"], -1)
        disrupted = next(g for g in result["groups"] if g["condition"] == "interruption")
        self.assertEqual(disrupted["recovery_success"]["estimate"], 0)

    def test_duplicate_actions_fail_even_when_final_state_matches(self):
        rows = paired()
        rows[0]["actions"] *= 2
        self.assertEqual(analyze(rows, bootstrap=50)["groups"][0]["grounded_success"]["estimate"], 0)

    def test_no_action_requires_empty_action_trace(self):
        rows = paired()
        for row in rows:
            row.update(no_action=True, expected_actions=[], actions=[])
        self.assertEqual(analyze(rows, bootstrap=50)["groups"][0]["no_action_success"]["estimate"], 1)
        rows[0]["actions"] = ["unauthorized"]
        self.assertEqual(analyze(rows, bootstrap=50)["groups"][0]["no_action_success"]["estimate"], 0)

    def test_rejects_invalid_inputs(self):
        mutations = [
            {"user_end_ms": math.nan}, {"first_audio_ms": -1},
            {"first_audio_ms": True}, {"deadline_ms": 0},
            {"expected_state": None}, {"expected_actions": "update"},
            {"timing_appropriate": "yes"}, {"repeat": True},
            {"trace_ref": ""}, {"evidence_kind": "unknown"},
            {"first_audio_ms": 12000}, {"no_action": True},
            {"system_version": ""}, {"condition": "typo"},
            {"status": "timeout", "timing_appropriate": True},
        ]
        for mutation in mutations:
            with self.subTest(mutation=mutation), self.assertRaises(ValueError):
                rows = paired()
                rows[0].update(mutation)
                analyze(rows, bootstrap=50)

    def test_negative_latency_is_preserved_as_overlap(self):
        rows = paired()
        rows[0]["first_audio_ms"] = 800
        self.assertEqual(analyze(rows, bootstrap=50)["groups"][0]["latency_ms"]["p50"], -200)

    def test_requires_complete_matched_panel(self):
        for rows in ([], paired()[:1], paired() + paired(),
                     paired() + [episode(system="beta")]):
            with self.subTest(rows=rows), self.assertRaises(ValueError):
                analyze(rows, bootstrap=50)

    def test_rejects_mixed_provenance_or_changed_ground_truth(self):
        for field, value in (("evidence_kind", "measured"),
                             ("expected_state", {"quantity": 99}),
                             ("system_version", "changed")):
            rows = paired()
            rows[1][field] = value
            with self.subTest(field=field), self.assertRaises(ValueError):
                analyze(rows, bootstrap=50)

    def test_bootstrap_is_deterministic_and_clustered(self):
        rows = paired() + [episode(case="case-2", condition=c, actual_state={})
                           for c in ("clean", "interruption")]
        self.assertEqual(analyze(rows, seed=5, bootstrap=100),
                         analyze(copy.deepcopy(rows), seed=5, bootstrap=100))
        result = analyze(rows, bootstrap=100)
        self.assertEqual(result["groups"][0]["grounded_success"]["clusters"], 2)
        self.assertEqual(result["groups"][0]["grounded_success"]["ci95"], [0, 1])

    def test_cross_system_paired_comparison(self):
        rows = paired() + [episode(system="beta", condition=c,
                                   first_audio_ms=1500, actual_state={})
                           for c in ("clean", "interruption")]
        comparison = analyze(rows, bootstrap=50)["system_deltas"][0]
        self.assertEqual(comparison["system_b_minus_a"], ["alpha", "beta"])
        self.assertEqual(comparison["grounded_success_delta"]["estimate"], -1)
        self.assertEqual(comparison["latency_delta_ms"]["estimate"], 250)

    def test_quantile_interpolates_and_handles_missing(self):
        self.assertEqual(quantile([100, 200], 0.95), 195)
        self.assertIsNone(quantile([], 0.5))

    def test_measured_label_is_only_a_submitter_declaration(self):
        rows = paired()
        for row in rows:
            row["evidence_kind"] = "measured"
        result = analyze(rows, bootstrap=50)
        self.assertIn("not authenticated", result["warning"])
        self.assertIsNone(result["groups"][0]["grounded_success"]["ci95"])

    def test_order_of_log_rows_does_not_change_results(self):
        rows = paired() + [episode(case="case-2", condition=c)
                           for c in ("clean", "interruption")]
        self.assertEqual(analyze(rows, bootstrap=50), analyze(rows[::-1], bootstrap=50))

    def test_cli_rejects_malformed_json(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "bad.jsonl"
            path.write_text("{not valid json}")
            self.assertEqual(main([str(path)]), 2)

    def test_bootstrap_count_must_be_positive(self):
        with self.assertRaises(ValueError):
            analyze(paired(), bootstrap=0)

    def test_cli_missing_file_returns_usage_error(self):
        self.assertEqual(main(["/does/not/exist.jsonl"]), 2)


if __name__ == "__main__":
    unittest.main()

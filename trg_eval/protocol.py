"""Offline analysis for TRG-Ref 0.1. Logs are assertions, not verified evidence."""
from __future__ import annotations

import argparse
from collections import defaultdict
from itertools import combinations
import json
import math
from pathlib import Path
import random
import statistics
import sys

VERSION = "trg-ref-0.1"
CONDITIONS = {"clean", "interruption", "false_pause", "backchannel", "noise"}


def quantile(values, probability):
    """Linearly interpolated empirical quantile; undefined on an empty sample."""
    if not values:
        return None
    ordered = sorted(values)
    index = (len(ordered) - 1) * probability
    low, high = math.floor(index), math.ceil(index)
    return ordered[low] + (ordered[high] - ordered[low]) * (index - low)


def _number(value):
    return type(value) in (int, float) and math.isfinite(value) and value >= 0


def _validate(rows):
    if not rows:
        raise ValueError("No episodes supplied")
    keys, versions = set(), defaultdict(set)
    for index, row in enumerate(rows, 1):
        if not isinstance(row, dict):
            raise ValueError(f"Episode {index}: expected an object")
        for field in ("system", "system_version", "conditions_id", "task_id", "case_id", "trace_ref"):
            if not isinstance(row.get(field), str) or not row[field].strip():
                raise ValueError(f"Episode {index}: missing {field}")
        if row.get("protocol_version") != VERSION:
            raise ValueError(f"Episode {index}: unsupported protocol_version")
        if row.get("evidence_kind") not in {"synthetic", "measured"}:
            raise ValueError(f"Episode {index}: invalid evidence_kind")
        if row.get("condition") not in CONDITIONS or row.get("status") not in {"ok", "timeout", "error"}:
            raise ValueError(f"Episode {index}: invalid condition or status")
        if type(row.get("repeat")) is not int or row["repeat"] < 0:
            raise ValueError(f"Episode {index}: repeat must be a nonnegative integer")
        if type(row.get("no_action")) is not bool:
            raise ValueError(f"Episode {index}: no_action must be boolean")
        appropriate = row.get("timing_appropriate")
        if appropriate is not None and type(appropriate) is not bool:
            raise ValueError(f"Episode {index}: timing_appropriate must be boolean or null")
        if "timing_appropriate" not in row or (row["status"] != "ok" and appropriate is True):
            raise ValueError(f"Episode {index}: invalid timing annotation for failed episode")
        for field in ("user_end_ms", "deadline_ms"):
            if not _number(row.get(field)):
                raise ValueError(f"Episode {index}: invalid {field}")
        if row["deadline_ms"] <= row["user_end_ms"]:
            raise ValueError(f"Episode {index}: deadline must follow user-end anchor")
        if "first_audio_ms" not in row:
            raise ValueError(f"Episode {index}: first_audio_ms required (null for no response)")
        first = row["first_audio_ms"]
        if first is not None and (not _number(first) or first > row["deadline_ms"]):
            raise ValueError(f"Episode {index}: invalid first_audio_ms")
        if first is None and appropriate is True:
            raise ValueError(f"Episode {index}: absent response cannot be timing-appropriate")
        for field in ("expected_state", "actual_state", "expected_recovery_state"):
            if not isinstance(row.get(field), dict):
                raise ValueError(f"Episode {index}: {field} must be an object")
        recovery = row.get("actual_recovery_state")
        if "actual_recovery_state" not in row or (recovery is not None and not isinstance(recovery, dict)):
            raise ValueError(f"Episode {index}: actual_recovery_state must be object or null")
        for field in ("expected_actions", "actions"):
            if not isinstance(row.get(field), list) or any(not isinstance(a, str) for a in row[field]):
                raise ValueError(f"Episode {index}: {field} must be a string list")
        if row["no_action"] and row["expected_actions"]:
            raise ValueError(f"Episode {index}: no-action task cannot require actions")
        key = (row["system"], *_panel_key(row))
        if key in keys:
            raise ValueError(f"Episode {index}: duplicate panel cell {key}")
        keys.add(key)
        versions[row["system"]].add(row["system_version"])
    if any(len(v) != 1 for v in versions.values()):
        raise ValueError("System versions changed within a panel")
    for field in ("conditions_id", "evidence_kind"):
        if len({r[field] for r in rows}) != 1:
            raise ValueError(f"Analyze each {field} separately; pooling is forbidden")
    systems = sorted(versions)
    panels = [{_panel_key(r) for r in rows if r["system"] == system} for system in systems]
    if any(panel != panels[0] for panel in panels):
        raise ValueError("Systems must have identical complete matched episode panels")
    conditions = {r["condition"] for r in rows}
    if "clean" not in conditions or len(conditions) < 2:
        raise ValueError("Require clean baseline and at least one disruption condition")
    cases = defaultdict(list)
    for row in rows:
        cases[(row["task_id"], row["case_id"], row["repeat"])].append(row)
    for case in cases.values():
        if len(case) != len(systems) * len(conditions):
            raise ValueError("Every case/repeat requires every system and condition")
        for field in ("expected_state", "expected_actions", "expected_recovery_state", "no_action"):
            if any(r[field] != case[0][field] for r in case):
                raise ValueError(f"Matched cases must share {field}")


def _panel_key(row):
    return row["task_id"], row["case_id"], row["repeat"], row["condition"]


def _cluster(row):
    return row["task_id"], row["case_id"]


def _success(row):
    return int(row["status"] == "ok" and row["actual_state"] == row["expected_state"]
               and row["actions"] == row["expected_actions"])


def _latency(row):
    first = row["first_audio_ms"]
    return None if first is None else first - row["user_end_ms"]


def _estimate(samples, bootstrap, seed, statistic=statistics.mean):
    """Resample case clusters, not turns or repeated trials, with replacement."""
    if not samples:
        return {"estimate": None, "ci95": None, "n": 0, "clusters": 0}
    clusters = defaultdict(list)
    for cluster, value in samples:
        clusters[cluster].append(value)
    blocks = [clusters[key] for key in sorted(clusters)]
    rng = random.Random(seed)
    draws = []
    for _ in range(bootstrap):
        values = [v for _ in blocks for v in rng.choice(blocks)]
        draws.append(statistic(values))
    # One cluster cannot support a sampling-uncertainty claim.
    interval = [quantile(draws, 0.025), quantile(draws, 0.975)] if len(blocks) > 1 else None
    return {"estimate": statistic([v for _, v in samples]), "ci95": interval,
            "n": len(samples), "clusters": len(blocks)}


def analyze(rows, *, bootstrap=2000, seed=17):
    """Analyze a complete panel; never infer correctness from agent self-report."""
    if type(bootstrap) is not int or bootstrap < 1:
        raise ValueError("bootstrap must be a positive integer")
    _validate(rows)
    groups = defaultdict(list)
    lookup = {}
    for row in rows:
        groups[(row["system"], row["condition"])].append(row)
        lookup[(row["system"], *_panel_key(row))] = row
    output = []
    def estimate(samples, statistic=statistics.mean):
        return _estimate(samples, bootstrap, seed, statistic)
    for (system, condition), episodes in sorted(groups.items()):
        episodes = sorted(episodes, key=_panel_key)
        def rate(function, subset=None):
            return estimate([(_cluster(r), int(function(r))) for r in
                             (episodes if subset is None else subset)])
        latencies = [(_cluster(r), _latency(r)) for r in episodes if _latency(r) is not None]
        output.append({
            "system": system, "system_version": episodes[0]["system_version"],
            "condition": condition, "n": len(episodes),
            "grounded_success": rate(_success),
            "timing_appropriate": rate(lambda r: r["status"] == "ok" and r["timing_appropriate"] is True),
            "timing_unannotated": sum(r["timing_appropriate"] is None for r in episodes),
            "no_response_rate": rate(lambda r: r["first_audio_ms"] is None),
            "failure_rate": rate(lambda r: r["status"] != "ok"),
            "recovery_success": None if condition == "clean" else rate(
                lambda r: r["status"] == "ok" and r["actual_recovery_state"] == r["expected_recovery_state"]),
            "no_action_success": rate(_success, [r for r in episodes if r["no_action"]]),
            "latency_ms": {"n_observed": len(latencies),
                           "p50": quantile([v for _, v in latencies], 0.5),
                           "p95": quantile([v for _, v in latencies], 0.95),
                           "p50_uncertainty": estimate(latencies, statistics.median),
                           "p95_uncertainty": estimate(latencies, lambda v: quantile(v, 0.95))},
        })
    recovery_deltas = []
    for (system, condition), episodes in sorted(groups.items()):
        if condition == "clean":
            continue
        pairs = [(r, lookup[(system, r["task_id"], r["case_id"], r["repeat"], "clean")])
                 for r in sorted(episodes, key=_panel_key)]
        recovery_deltas.append({"system": system, "condition": condition,
                                "grounded_success_delta": estimate([
                                    (_cluster(r), _success(r) - _success(clean)) for r, clean in pairs])})
    system_deltas = []
    for a, b in combinations(sorted({r["system"] for r in rows}), 2):
        for condition in sorted({r["condition"] for r in rows}):
            pairs = [(r, lookup[(b, *_panel_key(r))])
                     for r in sorted(groups[(a, condition)], key=_panel_key)]
            system_deltas.append({"system_b_minus_a": [a, b], "condition": condition,
                                  "grounded_success_delta": estimate([
                                      (_cluster(x), _success(y) - _success(x)) for x, y in pairs]),
                                  "latency_delta_ms": estimate([
                                      (_cluster(x), _latency(y) - _latency(x)) for x, y in pairs
                                      if _latency(x) is not None and _latency(y) is not None])})
    synthetic = rows[0]["evidence_kind"] == "synthetic"
    return {"protocol_version": VERSION, "evidence_kind": rows[0]["evidence_kind"],
            "empirical_evidence": not synthetic, "conditions_id": rows[0]["conditions_id"],
            "warning": ("SYNTHETIC SOFTWARE FIXTURE: not agent-performance evidence." if synthetic else
                        "MEASURED is submitter-declared; logs and state claims are not authenticated."),
            "uncertainty": {"method": "case-cluster percentile bootstrap", "draws": bootstrap,
                            "seed": seed, "interval": 0.95, "single_cluster_ci": None},
            "groups": output, "recovery_deltas": recovery_deltas, "system_deltas": system_deltas}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("episodes", type=Path, help="JSONL episode logs (see protocol/README.md)")
    parser.add_argument("--bootstrap", type=int, default=2000)
    parser.add_argument("--seed", type=int, default=17)
    args = parser.parse_args(argv)
    try:
        rows = [json.loads(line) for line in args.episodes.read_text().splitlines() if line.strip()]
        result = analyze(rows, bootstrap=args.bootstrap, seed=args.seed)
    except (OSError, ValueError, TypeError) as error:
        print(f"error: {error}", file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2, allow_nan=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

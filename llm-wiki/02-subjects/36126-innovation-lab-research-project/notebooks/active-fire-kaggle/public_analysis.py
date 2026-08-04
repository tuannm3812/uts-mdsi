import pandas as pd
import numpy as np


def headline_summary(exact: pd.DataFrame, buffered: pd.DataFrame) -> dict:
    total_exact = len(exact)
    total_buffered = len(buffered)
    if total_exact != total_buffered:
        raise ValueError("Exact and buffered dataframes must have the same length")
        
    exact_matches = sum(exact["match_class"] != "unmatched")
    exact_unresolved = total_exact - exact_matches
    
    buffered_matches = sum(buffered["match_class"].isin(["bushfire", "prescribed_burn", "other_fire"]))
    buffered_unresolved = total_buffered - buffered_matches
    
    return {
        "total_hotspots": total_exact,
        "exact_matches": int(exact_matches),
        "exact_unresolved": int(exact_unresolved),
        "exact_match_rate": float(exact_matches / total_exact) if total_exact > 0 else 0.0,
        "buffered_matches": int(buffered_matches),
        "buffered_unresolved": int(buffered_unresolved),
        "buffered_match_rate": float(buffered_matches / total_buffered) if total_buffered > 0 else 0.0,
    }


def sensor_summary(matches: pd.DataFrame) -> pd.DataFrame:
    summary_list = []
    grouped = matches.groupby("sensor")
    for sensor, group in grouped:
        total = len(group)
        matched = sum(group["match_class"].isin(["bushfire", "prescribed_burn", "other_fire"]))
        unresolved = total - matched
        summary_list.append({
            "sensor": sensor,
            "total_hotspots": total,
            "matched_hotspots": int(matched),
            "unresolved_hotspots": int(unresolved),
            "match_rate": float(matched / total) if total > 0 else 0.0
        })
    return pd.DataFrame(summary_list)


def event_concentration(matches: pd.DataFrame) -> pd.DataFrame:
    # Filter for matched hotspots only
    matched = matches[matches["match_class"].isin(["bushfire", "prescribed_burn", "other_fire"])]
    if matched.empty:
        return pd.DataFrame(columns=["fire_name", "fire_id", "matched_hotspots", "percentage"])
        
    total_matched = len(matched)
    # Group by fire_name and fire_id (or OBJECTID)
    grouped = matched.groupby(["fire_name", "fire_id"], dropna=False)
    summary_list = []
    for (fire_name, fire_id), group in grouped:
        count = len(group)
        summary_list.append({
            "fire_name": fire_name if pd.notna(fire_name) else "Unknown",
            "fire_id": fire_id if pd.notna(fire_id) else "Unknown",
            "matched_hotspots": count,
            "percentage": float(count / total_matched) if total_matched > 0 else 0.0
        })
    df = pd.DataFrame(summary_list)
    return df.sort_values(by="matched_hotspots", ascending=False).reset_index(drop=True)


def deterministic_display_sample(frame: pd.DataFrame, size: int, seed: int = 36126) -> pd.DataFrame:
    n = min(len(frame), size)
    if n <= 0:
        return frame.copy()
    return frame.sample(n=n, random_state=seed).sort_index()


def compare_refresh(reviewed: dict, refreshed: dict) -> pd.DataFrame:
    comparison_list = []
    for key in reviewed:
        rev_val = reviewed[key]
        ref_val = refreshed.get(key)
        status = "stable" if rev_val == ref_val else "changed"
        comparison_list.append({
            "metric": key,
            "reviewed": rev_val,
            "refreshed": ref_val,
            "status": status
        })
    return pd.DataFrame(comparison_list)


def assert_snapshot_invariants(actual: dict, expected: dict) -> None:
    differences = {key: (expected[key], actual.get(key)) for key in expected if actual.get(key) != expected[key]}
    if differences:
        raise AssertionError(f"Snapshot invariants changed: {differences}")

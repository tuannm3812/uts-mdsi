from pathlib import Path
import sys
import pandas as pd
import pytest

KAG_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(KAG_DIR))

from public_analysis import (
    headline_summary,
    sensor_summary,
    event_concentration,
    deterministic_display_sample,
    compare_refresh,
    assert_snapshot_invariants
)


def exact_fixture():
    # Returns a mock exact matched hotspots dataframe
    return pd.DataFrame([
        {"id": 1, "match_class": "bushfire", "sensor": "VIIRS", "confidence": 80},
        {"id": 2, "match_class": "unmatched", "sensor": "AHI", "confidence": None},
        {"id": 3, "match_class": "unmatched", "sensor": "AHI", "confidence": None},
    ])


def buffered_fixture():
    # Returns a mock buffered matched hotspots dataframe
    return pd.DataFrame([
        {"id": 1, "match_class": "bushfire", "sensor": "VIIRS", "confidence": 80},
        {"id": 2, "match_class": "spatial_only", "sensor": "AHI", "confidence": 50},
        {"id": 3, "match_class": "unmatched", "sensor": "AHI", "confidence": None},
    ])


def test_headline_summary_uses_unresolved_language():
    result = headline_summary(exact_fixture(), buffered_fixture())
    # unmatched (1) + spatial_only (1) = 2 unresolved for buffered
    assert result["buffered_unresolved"] == 2
    assert "false_positive" not in result
    assert "false_alarm" not in result


def test_display_sample_is_deterministic():
    frame = pd.DataFrame({"id": range(100)})
    first = deterministic_display_sample(frame, 10, seed=36126)
    second = deterministic_display_sample(frame, 10, seed=36126)
    pd.testing.assert_frame_equal(first, second)


def test_refresh_comparison_flags_drift_without_raising():
    reviewed = {"total_hotspots": 10, "exact_matches": 5}
    refreshed = {"total_hotspots": 11, "exact_matches": 5}
    comparison = compare_refresh(reviewed, refreshed)
    
    # Check that it identifies the change/drift
    assert comparison.loc[comparison["metric"] == "total_hotspots", "status"].values[0] == "changed"
    assert comparison.loc[comparison["metric"] == "exact_matches", "status"].values[0] == "stable"

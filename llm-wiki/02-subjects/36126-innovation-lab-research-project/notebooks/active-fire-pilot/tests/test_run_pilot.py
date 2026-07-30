from pathlib import Path
import sys


PILOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PILOT_DIR))

from run_pilot import normalize_hotspot, parse_accuracy_km, summarize_matches


def test_normalize_hotspot_uses_properties_and_point_geometry():
    feature = {
        "properties": {
            "id": 12,
            "sensor": "VIIRS",
            "datetime": "2020-01-02T03:00:00Z",
            "confidence": 80,
        },
        "geometry": {"type": "Point", "coordinates": [150.1, -32.9]},
    }
    normalized = normalize_hotspot(feature)
    assert normalized["id"] == 12
    assert normalized["longitude"] == 150.1
    assert normalized["latitude"] == -32.9
    assert normalized["sensor"] == "VIIRS"


def test_summarize_matches_counts_class_and_sensor():
    matches = [
        {"match_class": "bushfire", "sensor": "VIIRS", "confidence": 80},
        {"match_class": "bushfire", "sensor": "AHI", "confidence": 50},
        {"match_class": "unmatched", "sensor": "AHI", "confidence": None},
    ]
    summary = summarize_matches(matches)
    assert summary["total_hotspots"] == 3
    assert summary["match_class_counts"] == {"bushfire": 2, "unmatched": 1}
    assert summary["sensor_counts"] == {"AHI": 2, "VIIRS": 1}
    assert summary["missing_confidence"] == 1


def test_parse_accuracy_km():
    assert parse_accuracy_km("± 0.375km") == 0.375
    assert parse_accuracy_km("± 2km") == 2.0
    assert parse_accuracy_km(None) == 0.0

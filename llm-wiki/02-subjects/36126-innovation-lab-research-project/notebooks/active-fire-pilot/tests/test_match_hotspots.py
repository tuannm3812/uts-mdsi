from datetime import datetime, timezone
import json
from pathlib import Path
import sys


PILOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PILOT_DIR))

from match_hotspots import (
    classify_hotspot,
    geometry_bounds,
    point_in_geometry,
    point_within_geometry_buffer,
    prepare_features,
    within_event_window,
)


FIXTURES = Path(__file__).parent / "fixtures"


def load_features():
    return json.loads((FIXTURES / "fire_polygons.geojson").read_text())["features"]


def test_point_in_polygon_inside_outside_and_boundary():
    geometry = load_features()[0]["geometry"]
    assert point_in_geometry(150.1, -32.9, geometry)
    assert not point_in_geometry(151.0, -32.9, geometry)
    assert point_in_geometry(150.0, -33.0, geometry)


def test_point_in_multipolygon():
    geometry = load_features()[1]["geometry"]
    assert point_in_geometry(150.35, -32.95, geometry)
    assert not point_in_geometry(150.1, -32.9, geometry)


def test_geometry_bounds_and_preparation():
    features = prepare_features(load_features())
    assert geometry_bounds(features[0]["geometry"]) == (150.0, -33.0, 150.2, -32.8)
    assert features[0]["_bbox"] == (150.0, -33.0, 150.2, -32.8)


def test_geometry_buffer_matches_nearby_point_only_at_sufficient_distance():
    geometry = load_features()[0]["geometry"]
    assert point_within_geometry_buffer(150.21, -32.9, geometry, buffer_km=2.0)
    assert not point_within_geometry_buffer(150.21, -32.9, geometry, buffer_km=0.5)


def test_event_window_includes_grace_and_rejects_outside():
    properties = load_features()[0]["properties"]
    inside = datetime(2020, 1, 11, tzinfo=timezone.utc)
    outside = datetime(2020, 1, 13, tzinfo=timezone.utc)
    assert within_event_window(inside, properties, grace_days=1)
    assert not within_event_window(outside, properties, grace_days=1)


def test_missing_extinguish_date_uses_ignition_day_plus_grace():
    properties = {"ignition_date": "2020-01-04T00:00:00Z", "extinguish_date": None}
    observed = datetime(2020, 1, 5, 12, tzinfo=timezone.utc)
    assert within_event_window(observed, properties, grace_days=2)


def test_classification_distinguishes_fire_types_and_unmatched():
    features = load_features()
    bushfire = classify_hotspot(
        {"id": "H1", "longitude": 150.1, "latitude": -32.9, "datetime": "2020-01-06T12:00:00Z"},
        features,
        grace_days=1,
    )
    prescribed = classify_hotspot(
        {"id": "H2", "longitude": 150.35, "latitude": -32.95, "datetime": "2020-01-04T12:00:00Z"},
        features,
        grace_days=1,
    )
    unmatched = classify_hotspot(
        {"id": "H3", "longitude": 151.0, "latitude": -32.9, "datetime": "2020-01-06T12:00:00Z"},
        features,
        grace_days=1,
    )
    assert bushfire["match_class"] == "bushfire"
    assert bushfire["fire_id"] == "B1"
    assert prescribed["match_class"] == "prescribed_burn"
    assert prescribed["fire_id"] == "P1"
    assert unmatched["match_class"] == "unmatched"
    assert unmatched["fire_id"] is None


def test_classification_can_apply_spatial_tolerance():
    features = prepare_features(load_features())
    result = classify_hotspot(
        {"id": "H4", "longitude": 150.21, "latitude": -32.9, "datetime": "2020-01-06T12:00:00Z"},
        features,
        grace_days=1,
        spatial_buffer_km=2.0,
    )
    assert result["match_class"] == "bushfire"

import hashlib
import json
from pathlib import Path
import sys
from urllib.parse import parse_qs, urlparse


PILOT_DIR = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PILOT_DIR))

from fetch_public_data import (
    build_dea_url,
    build_nsw_url,
    create_provenance_record,
)


def test_dea_url_contains_bounded_time_and_space_filter():
    url = build_dea_url(
        bbox=[149.5, -33.7, 151.0, -32.3],
        start="2020-01-01T00:00:00Z",
        end="2020-01-15T00:00:00Z",
    )
    query = parse_qs(urlparse(url).query)
    assert query["typeName"] == ["public:hotspots"]
    assert query["outputFormat"] == ["application/json"]
    assert "datetime >= '2020-01-01T00:00:00Z'" in query["CQL_FILTER"][0]
    assert "BBOX(geometry,149.5,-33.7,151.0,-32.3,'EPSG:4326')" in query["CQL_FILTER"][0]


def test_nsw_url_requests_geojson_with_date_and_envelope():
    url = build_nsw_url(
        bbox=[149.5, -33.7, 151.0, -32.3],
        start="2020-01-01",
        end="2020-01-15",
        lookback_start="2019-07-01",
    )
    query = parse_qs(urlparse(url).query)
    assert query["f"] == ["geojson"]
    assert query["geometry"] == ["149.5,-33.7,151.0,-32.3"]
    assert "ignition_date >= DATE '2019-07-01'" in query["where"][0]
    assert "ignition_date < DATE '2020-01-15'" in query["where"][0]
    assert "extinguish_date >= DATE '2020-01-01'" in query["where"][0]
    assert "extinguish_date IS NULL" in query["where"][0]
    assert query["outSR"] == ["4326"]


def test_provenance_records_bytes_and_sha256(tmp_path):
    path = tmp_path / "sample.json"
    path.write_bytes(b'{"features":[]}')
    record = create_provenance_record(path, "https://example.test/data")
    assert record["bytes"] == 15
    assert record["sha256"] == hashlib.sha256(path.read_bytes()).hexdigest()
    assert record["source_url"] == "https://example.test/data"

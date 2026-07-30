"""Fetch bounded public DEA hotspot and NSW Fire History pilot data."""

import argparse
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
from typing import Dict, Iterable, List
from urllib.parse import urlencode
from urllib.request import Request, urlopen


DEA_WFS = "https://hotspots.dea.ga.gov.au/geoserver/wfs"
NSW_FIRE_QUERY = (
    "https://portal.data.nsw.gov.au/arcgis/rest/services/Hosted/"
    "NSWFireHistory/FeatureServer/0/query"
)


def build_dea_url(bbox: List[float], start: str, end: str) -> str:
    bbox_text = ",".join(str(value) for value in bbox)
    cql = (
        f"datetime >= '{start}' AND datetime < '{end}' "
        f"AND BBOX(geometry,{bbox_text},'EPSG:4326')"
    )
    params = {
        "service": "WFS",
        "version": "1.1.0",
        "request": "GetFeature",
        "typeName": "public:hotspots",
        "outputFormat": "application/json",
        "CQL_FILTER": cql,
    }
    return f"{DEA_WFS}?{urlencode(params)}"


def build_nsw_url(bbox: List[float], start: str, end: str, lookback_start: str) -> str:
    bbox_text = ",".join(str(value) for value in bbox)
    params = {
        "where": (
            f"ignition_date >= DATE '{lookback_start}' AND ignition_date < DATE '{end}' AND "
            f"(extinguish_date >= DATE '{start}' OR extinguish_date IS NULL)"
        ),
        "geometry": bbox_text,
        "geometryType": "esriGeometryEnvelope",
        "inSR": "4326",
        "spatialRel": "esriSpatialRelIntersects",
        "outFields": (
            "fire_id,fire_name,ignition_date,capture_date,extinguish_date,"
            "fire_type,ignition_cause,capt_method,area_ha,perim_km,state,agency"
        ),
        "returnGeometry": "true",
        "outSR": "4326",
        "f": "geojson",
    }
    return f"{NSW_FIRE_QUERY}?{urlencode(params)}"


def download_json(url: str, destination: Path, timeout: int = 180) -> Dict:
    request = Request(url, headers={"User-Agent": "UTS-MDSI-active-fire-pilot/1.0"})
    with urlopen(request, timeout=timeout) as response:
        content_type = response.headers.get("Content-Type", "")
        payload = response.read()
    if "json" not in content_type.lower() and not payload.lstrip().startswith(b"{"):
        raise ValueError(f"Expected JSON from {url}; received {content_type}")
    document = json.loads(payload)
    if document.get("type") != "FeatureCollection" or not isinstance(document.get("features"), list):
        raise ValueError(f"Expected a GeoJSON FeatureCollection from {url}")
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(payload)
    return document


def create_provenance_record(path: Path, source_url: str) -> Dict:
    payload = path.read_bytes()
    return {
        "file": path.name,
        "source_url": source_url,
        "retrieved_at_utc": datetime.now(timezone.utc).isoformat(),
        "bytes": len(payload),
        "sha256": hashlib.sha256(payload).hexdigest(),
    }


def fetch(config_path: Path, output_dir: Path) -> Dict:
    config = json.loads(config_path.read_text())
    bbox = config["bbox_wgs84"]
    start = config["start_utc"]
    end = config["end_utc_exclusive"]
    dea_url = build_dea_url(bbox, start, end)
    nsw_url = build_nsw_url(
        bbox,
        start[:10],
        end[:10],
        config["event_lookback_start"],
    )

    dea_path = output_dir / "dea_hotspots.geojson"
    nsw_path = output_dir / "nsw_fire_history.geojson"
    dea = download_json(dea_url, dea_path)
    nsw = download_json(nsw_url, nsw_path)

    provenance = {
        "config": config,
        "sources": [
            create_provenance_record(dea_path, dea_url),
            create_provenance_record(nsw_path, nsw_url),
        ],
        "record_counts": {
            "dea_hotspots": len(dea["features"]),
            "nsw_fire_history": len(nsw["features"]),
        },
    }
    (output_dir / "provenance.json").write_text(
        json.dumps(provenance, indent=2, sort_keys=True) + "\n"
    )
    return provenance


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, default=Path(__file__).with_name("source-config.json"))
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    print(json.dumps(fetch(args.config, args.output_dir), indent=2))


if __name__ == "__main__":
    main()

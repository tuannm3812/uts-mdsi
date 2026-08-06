"""Fetch DEA Hotspots (MODIS/VIIRS/AHI) for a widened bbox/date window.

Same DEA WFS source and query shape as notebooks/active-fire-pilot/fetch_public_data.py,
kept as a separate copy here because this project explores a different (wider) time
window for exploratory EDA/feature-engineering, not the reproducible reliability pilot.
"""

import argparse
import json
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

DEA_WFS = "https://hotspots.dea.ga.gov.au/geoserver/wfs"


def build_dea_url(bbox: list, start: str, end: str) -> str:
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


def fetch(config_path: Path, output_dir: Path) -> dict:
    config = json.loads(config_path.read_text())
    url = build_dea_url(config["bbox_wgs84"], config["start_utc"], config["end_utc_exclusive"])
    request = Request(url, headers={"User-Agent": "UTS-MDSI-active-fire-datascience/1.0"})
    with urlopen(request, timeout=300) as response:
        payload = response.read()
    document = json.loads(payload)
    if document.get("type") != "FeatureCollection":
        raise ValueError(f"Expected a GeoJSON FeatureCollection from {url}")

    output_dir.mkdir(parents=True, exist_ok=True)
    destination = output_dir / "dea_hotspots_wide.geojson"
    destination.write_bytes(payload)

    print(f"Fetched {len(document['features'])} hotspot features -> {destination}")
    return {"count": len(document["features"]), "path": str(destination), "source_url": url}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, default=Path(__file__).with_name("config.json"))
    parser.add_argument("--output-dir", type=Path, default=Path(__file__).with_name("data"))
    args = parser.parse_args()
    print(json.dumps(fetch(args.config, args.output_dir), indent=2))


if __name__ == "__main__":
    main()

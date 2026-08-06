"""Sample DEA Land Cover (Landsat, ga_ls_landcover) classifications at hotspot
locations via WMS GetFeatureInfo point queries.

One HTTP call per unique location, so this samples/dedups rather than querying
all hotspots -- with 100k+ hotspots in the widened window, one call each would
take hours and mostly repeat the same handful of grid cells anyway (hotspots
cluster spatially). Coordinates are rounded to ~1km (3 decimal places) before
dedup, which also roughly matches the Landsat-derived product's own resolution.
"""

import argparse
import json
import random
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

OWS_URL = "https://ows.dea.ga.gov.au/"
QUERY_BOX_DEG = 0.001  # ~100m half-width query window around each point


def query_point(lat: float, lon: float, layer: str, time: str) -> dict:
    bbox = f"{lat - QUERY_BOX_DEG},{lon - QUERY_BOX_DEG},{lat + QUERY_BOX_DEG},{lon + QUERY_BOX_DEG}"
    params = {
        "service": "WMS", "version": "1.3.0", "request": "GetFeatureInfo",
        "layers": layer, "query_layers": layer, "styles": "",
        "crs": "EPSG:4326", "bbox": bbox, "width": 3, "height": 3,
        "i": 1, "j": 1, "info_format": "application/json", "time": time,
    }
    url = f"{OWS_URL}?{urlencode(params)}"
    request = Request(url, headers={"User-Agent": "UTS-MDSI-active-fire-datascience/1.0"})
    with urlopen(request, timeout=30) as response:
        return json.loads(response.read())


def sample_hotspot_coords(hotspots_path: Path, sample_size: int, seed: int) -> list:
    document = json.loads(hotspots_path.read_text())
    coords = set()
    for feature in document["features"]:
        lon, lat = feature["geometry"]["coordinates"][:2]
        coords.add((round(lat, 3), round(lon, 3)))
    coords = sorted(coords)
    random.Random(seed).shuffle(coords)
    return coords[:sample_size]


def fetch(config_path: Path, hotspots_path: Path, output_dir: Path,
          sample_size: int, seed: int) -> dict:
    config = json.loads(config_path.read_text())
    layer = config["landcover_layer"]
    time = config["landcover_year"]

    sampled = sample_hotspot_coords(hotspots_path, sample_size, seed)
    records = []
    errors = 0
    for lat, lon in sampled:
        try:
            result = query_point(lat, lon, layer, time)
            features = result.get("features", [])
            if not features:
                continue
            props = features[0]["properties"]
            data_points = props.get("data", [])
            if not data_points:
                continue
            bands = data_points[0].get("bands", {})
            description = data_points[0].get("description", {})
            records.append({
                "lat": lat, "lon": lon,
                "level3": bands.get("level3"), "level3_label": description.get("level3_label"),
                "level4": bands.get("level4"), "level4_label": description.get("level4_label"),
            })
        except Exception:
            errors += 1

    output_dir.mkdir(parents=True, exist_ok=True)
    destination = output_dir / "landcover_sample.json"
    destination.write_text(json.dumps(records, indent=2))
    print(f"Land cover: {len(records)} points resolved, {errors} failed, out of {len(sampled)} sampled -> {destination}")
    return {"resolved": len(records), "errors": errors, "sampled": len(sampled), "path": str(destination)}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, default=Path(__file__).with_name("config.json"))
    parser.add_argument("--hotspots", type=Path, default=Path(__file__).with_name("data") / "dea_hotspots_wide.geojson")
    parser.add_argument("--output-dir", type=Path, default=Path(__file__).with_name("data"))
    parser.add_argument("--sample-size", type=int, default=500)
    parser.add_argument("--seed", type=int, default=42)
    args = parser.parse_args()
    print(json.dumps(fetch(args.config, args.hotspots, args.output_dir, args.sample_size, args.seed), indent=2))


if __name__ == "__main__":
    main()

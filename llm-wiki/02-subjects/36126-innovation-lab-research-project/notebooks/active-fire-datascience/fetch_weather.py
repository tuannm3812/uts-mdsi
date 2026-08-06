"""Fetch SILO DataDrill daily weather (rainfall, max/min temp, vapour pressure,
humidity) for a small grid of points spanning the case-study bbox.

SILO (longpaddock.qld.gov.au) is Queensland Government's gridded/interpolated
climate dataset, 1889-present, ~5km resolution. No account/API key required --
`username` just needs to be a plausible email, `password` any string (confirmed
live, 2026-08-06). Wind speed/direction are NOT available from SILO (checked
against SILO's own variable list) -- flagged explicitly rather than silently
omitted; a later pass needs BOM station data or ERA5 for wind.
"""

import argparse
import csv
import io
import json
from pathlib import Path
from urllib.parse import urlencode
from urllib.request import Request, urlopen

SILO_URL = "https://www.longpaddock.qld.gov.au/cgi-bin/silo/DataDrillDataset.php"
VARIABLES = "RXNVDH"  # rainfall, max temp, min temp, vapour pressure, VPD, rh at tmax


def fetch_point(lat: float, lon: float, start: str, end: str, contact_email: str) -> str:
    params = {
        "lat": lat,
        "lon": lon,
        "start": start,
        "finish": end,
        "format": "csv",
        "username": contact_email,
        "password": "apirequest",
        "comment": VARIABLES,
    }
    url = f"{SILO_URL}?{urlencode(params)}"
    request = Request(url, headers={"User-Agent": "UTS-MDSI-active-fire-datascience/1.0"})
    with urlopen(request, timeout=120) as response:
        return response.read().decode("utf-8")


def fetch(config_path: Path, output_dir: Path, contact_email: str) -> dict:
    config = json.loads(config_path.read_text())
    start = config["start_utc"][:10].replace("-", "")
    end = config["end_utc_exclusive"][:10].replace("-", "")

    output_dir.mkdir(parents=True, exist_ok=True)
    results = {}
    for point in config["silo_grid_points"]:
        csv_text = fetch_point(point["lat"], point["lon"], start, end, contact_email)
        rows = list(csv.reader(io.StringIO(csv_text)))
        destination = output_dir / f"silo_weather_{point['name']}.csv"
        destination.write_text(csv_text)
        results[point["name"]] = {"rows": len(rows) - 1, "path": str(destination)}
        print(f"Fetched {len(rows) - 1} weather rows for '{point['name']}' -> {destination}")

    return results


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", type=Path, default=Path(__file__).with_name("config.json"))
    parser.add_argument("--output-dir", type=Path, default=Path(__file__).with_name("data"))
    parser.add_argument("--contact-email", type=str, required=True,
                         help="SILO's API just wants a plausible contact email, no registration")
    args = parser.parse_args()
    print(json.dumps(fetch(args.config, args.output_dir, args.contact_email), indent=2))


if __name__ == "__main__":
    main()

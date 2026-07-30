"""Run the bounded DEA-to-NSW Fire History feasibility pilot."""

import argparse
from collections import Counter, defaultdict
import csv
import json
from pathlib import Path
from typing import Dict, Iterable, List
import re

from match_hotspots import classify_hotspot, prepare_features


MATCH_FIELDS = [
    "id",
    "datetime",
    "longitude",
    "latitude",
    "sensor",
    "satellite",
    "process_algorithm",
    "confidence",
    "accuracy",
    "match_class",
    "fire_id",
    "fire_name",
    "spatial_match_count",
    "temporal_match_count",
]


def normalize_hotspot(feature: Dict) -> Dict:
    properties = feature.get("properties", {})
    coordinates = feature.get("geometry", {}).get("coordinates", [None, None])
    return {
        "id": properties.get("id"),
        "datetime": properties.get("datetime"),
        "longitude": properties.get("longitude", coordinates[0]),
        "latitude": properties.get("latitude", coordinates[1]),
        "sensor": properties.get("sensor"),
        "satellite": properties.get("satellite"),
        "process_algorithm": properties.get("process_algorithm"),
        "confidence": properties.get("confidence"),
        "accuracy": properties.get("accuracy"),
    }


def parse_accuracy_km(value) -> float:
    if value in (None, ""):
        return 0.0
    match = re.search(r"([0-9]+(?:\.[0-9]+)?)", str(value))
    return float(match.group(1)) if match else 0.0


def summarize_matches(matches: Iterable[Dict]) -> Dict:
    rows = list(matches)
    return {
        "total_hotspots": len(rows),
        "match_class_counts": dict(sorted(Counter(row["match_class"] for row in rows).items())),
        "sensor_counts": dict(sorted(Counter(row.get("sensor") or "missing" for row in rows).items())),
        "missing_confidence": sum(row.get("confidence") is None for row in rows),
    }


def _write_matches(path: Path, matches: List[Dict]) -> None:
    with path.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=MATCH_FIELDS, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(matches)


def _write_aggregate(path: Path, matches: List[Dict]) -> None:
    grouped = defaultdict(list)
    for row in matches:
        grouped[(row.get("sensor") or "missing", row["match_class"])].append(row)
    with path.open("w", newline="") as handle:
        fields = ["sensor", "match_class", "hotspot_count", "mean_confidence", "missing_confidence"]
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for (sensor, match_class), rows in sorted(grouped.items()):
            confidence = [float(row["confidence"]) for row in rows if row.get("confidence") is not None]
            writer.writerow(
                {
                    "sensor": sensor,
                    "match_class": match_class,
                    "hotspot_count": len(rows),
                    "mean_confidence": f"{sum(confidence) / len(confidence):.3f}" if confidence else "",
                    "missing_confidence": len(rows) - len(confidence),
                }
            )


def run(
    data_dir: Path,
    output_dir: Path,
    grace_days: int = 1,
    use_sensor_accuracy: bool = False,
) -> Dict:
    dea = json.loads((data_dir / "dea_hotspots.geojson").read_text())
    nsw = json.loads((data_dir / "nsw_fire_history.geojson").read_text())
    features = prepare_features(nsw["features"])
    hotspots = [normalize_hotspot(feature) for feature in dea["features"]]
    matches = [
        classify_hotspot(
            hotspot,
            features,
            grace_days,
            parse_accuracy_km(hotspot.get("accuracy")) if use_sensor_accuracy else 0.0,
        )
        for hotspot in hotspots
    ]

    output_dir.mkdir(parents=True, exist_ok=True)
    _write_matches(output_dir / "matched_hotspots.csv", matches)
    _write_aggregate(output_dir / "pilot_results.csv", matches)

    summary = summarize_matches(matches)
    summary.update(
        {
            "fire_event_count": len(features),
            "temporal_grace_days": grace_days,
            "sensor_accuracy_buffer_applied": use_sensor_accuracy,
            "fire_type_counts": dict(
                sorted(
                    Counter(
                        feature.get("properties", {}).get("fire_type") or "missing"
                        for feature in features
                    ).items()
                )
            ),
            "fire_event_missingness": {
                field: sum(
                    feature.get("properties", {}).get(field) in (None, "")
                    for feature in features
                )
                for field in [
                    "fire_id",
                    "fire_name",
                    "ignition_date",
                    "extinguish_date",
                    "fire_type",
                    "ignition_cause",
                    "area_ha",
                ]
            },
        }
    )
    (output_dir / "pilot_summary.json").write_text(
        json.dumps(summary, indent=2, sort_keys=True) + "\n"
    )
    return summary


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--data-dir", type=Path, required=True)
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--grace-days", type=int, default=1)
    parser.add_argument("--use-sensor-accuracy", action="store_true")
    args = parser.parse_args()
    print(
        json.dumps(
            run(args.data_dir, args.output_dir, args.grace_days, args.use_sensor_accuracy),
            indent=2,
        )
    )


if __name__ == "__main__":
    main()

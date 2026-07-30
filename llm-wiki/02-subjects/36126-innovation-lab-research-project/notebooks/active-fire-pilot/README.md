# Active-Fire Public-Data Pilot

This reproducible pilot tests whether public DEA Hotspots and NSW Fire History data can support a fire-hotspot reliability study.

## Pilot definition

- Region: `149.5–151.0°E, 33.7–32.3°S`
- Hotspot window: 1–14 January 2020 UTC
- Fire-event lookback: 1 July 2019
- Hotspot source: DEA Hotspots public WFS
- Event source: NSW Fire History public ArcGIS Feature Service
- Exact comparison: point inside final event polygon during the recorded event window
- Sensitivity comparison: each hotspot's documented positional accuracy is used as a polygon buffer

The region contains the Gospers Mountain/Greater Blue Mountains fire context but is deliberately described by its bounding box because it also covers adjacent areas and events.

## Requirements

- Python 3.9 or later
- `pytest` for tests
- No geospatial Python package is required

## Run

```bash
python3 fetch_public_data.py \
  --output-dir /path/to/raw-data

python3 run_pilot.py \
  --data-dir /path/to/raw-data \
  --output-dir /path/to/results \
  --grace-days 1 \
  --use-sensor-accuracy
```

## Test

```bash
python3 -m pytest tests -q
```

## Outputs

- `provenance.json`: source URLs, retrieval time, byte count, checksums, and record counts
- `matched_hotspots.csv`: observation-level matching audit
- `pilot_results.csv`: compact sensor-by-match-class results
- `pilot_summary.json`: headline counts and event-field missingness

## Interpretation boundary

An unmatched DEA hotspot is **not automatically a false alarm**. It may reflect incomplete event coverage, final-boundary timing, spatial misalignment, a prescribed burn absent from the selected event sample, industrial heat, or a true satellite commission error. This pilot evaluates reference-data suitability; it does not estimate detector accuracy.

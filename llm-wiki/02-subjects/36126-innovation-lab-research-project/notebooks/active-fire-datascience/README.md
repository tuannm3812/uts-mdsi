# Active-Fire Data Science Exploration (Private)

Exploratory, private work-in-progress — **not** the public reproducibility pipeline (`notebooks/active-fire-kaggle/`). This prototypes bringing in more datasets, EDA, and candidate features ahead of T-033 (the actual multi-decade data foundation for the forecasting model), using a widened but still bounded window so it's fast to iterate on.

- **Kaggle dataset (private):** [nsw-active-fire-datascience-exploration](https://www.kaggle.com/datasets/tuannm3812/nsw-active-fire-datascience-exploration)
- **Kaggle notebook (private):** [nsw-active-fire-data-science-exploration](https://www.kaggle.com/code/tuannm3812/nsw-active-fire-data-science-exploration)

## Scope

- **Region:** same Greater Blue Mountains bbox as the reliability pilot.
- **Window:** 15 Dec 2019 – 15 Jan 2020. Chosen by checking live record counts across several candidate windows first (see `config.json`'s `notes` field) — this one spans the December activity surge into the pilot's quieter January window, rather than a flat peak.
- **Not the confirmed case-study region/horizon** — those are still open questions for Friday's meeting. This is prototyping the *process* (fetch → EDA → features), reusable once scope is frozen.

## Datasets brought in

| Source | Script | What it gives |
|---|---|---|
| DEA Hotspots WFS (MODIS/VIIRS/AHI/AVHRR) | `fetch_hotspots.py` | 133,286 hotspot records for the window — same WFS source as the pilot, wider range |
| SILO (Long Paddock, Qld Gov) | `fetch_weather.py` | Daily rainfall, max/min temp, vapour pressure, humidity, at 3 grid points. **No wind** — confirmed against SILO's own variable list, needs BOM or ERA5 later |
| DEA Land Cover (Landsat) | `fetch_landcover.py` | Annual land-cover classification, sampled at 500 unique hotspot locations (one WMS call per unique location — not exhaustive, hotspots cluster spatially) |

Run in order: `fetch_hotspots.py` → `fetch_weather.py --contact-email <email>` → `fetch_landcover.py`, then `build_notebook.py` to assemble `active_fire_data_exploration.ipynb`, then execute it (`jupyter nbconvert --to notebook --execute --inplace ...`).

## What's in the notebook

Hotspot EDA (temporal, sensor composition, per-sensor confidence) → weather EDA (spatial variation across the 3 points) → a rough hotspot-vs-dryness correlation check → land-cover class distribution at hotspot locations → a candidate-feature list for each of the eventual model's branches (hotspot-history, weather, land-cover, label-confidence) → honest gaps (wind, land-cover is annual not sub-annual condition, 500-point land-cover sample not exhaustive).

## Why private, why a separate folder

Kept private because it's genuinely unfinished/unreviewed exploration, not because the underlying data is sensitive — all three sources are the same public, appropriately-licensed data already used in the public pilot. Kept in a separate folder (not layered into `active-fire-kaggle/`) so it doesn't need the same self-contained/audited discipline as the public artifact — it imports from `analysis.py` directly rather than embedding source as literal strings.

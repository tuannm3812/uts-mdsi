# Active-Fire Detection Reading Library — 29 July 2026

## Scope

This pack supports the supervisor-confirmed topic: **fire-hotspot detection and active-fire monitoring**, not fire-spread prediction. The literature review is geographically broad; later modelling may use NSW or another manageable, fire-prone Australian region.

The downloadable full texts are stored in Google Drive under:

`36126 Innovation Lab Research Project/04 Research Work/01 Literature Review/02 Reading Library`

The repository stores this guide, the literature matrix, and research notes. It deliberately does not duplicate the large PDF files.

## Recommended Reading Order

### Stage 1 — Understand the operational problem

1. **Jones et al., Active Fire Detection Using the Himawari-8 Satellite: Final Project Report** — start here for the Australian operational setting, agency use, and Himawari-8 monitoring.
2. **DEA Hotspots, MyFireWatch, and EFFIS technical pages** — compare how real systems present confidence, latency, sensor limitations, and false alarms.

### Stage 2 — Learn the foundational detection algorithms

3. **Giglio et al. (2016), Collection 6 MODIS active fire detection algorithm and fire products** — understand contextual thermal-anomaly detection and quality flags.
4. **Schroeder et al. (2014), The New VIIRS 375 m Active Fire Detection Data Product** — understand why spatial resolution matters and how VIIRS differs from MODIS.

### Stage 3 — Focus on Australia and multi-sensor monitoring

5. **Zhang et al. (2023), Real-Time Wildfire Detection Algorithm Based on VIIRS Fire Product and Himawari-8 Data** — the closest multi-sensor Australian comparator.
6. **Zhang et al. (2021), Sentinel-2 deep-learning active-fire detection** — useful Australian/global segmentation benchmark.
7. **Singh et al. (2025), Active wildfire detection via satellite imagery and machine learning** — NSW case study and a useful regional baseline.

### Stage 4 — Examine newer modelling and dataset directions

8. **Rad et al. (2024)** — vision transformers and multispectral imagery.
9. **Barco et al. (2024)** — self-supervised temporal hotspot detection.
10. **Sen2Fire (2024)** and **TS-SatFire (2024)** — benchmark datasets, task definitions, and split design.

### Stage 5 — Examine trustworthy explanations

11. **Phan et al. (2022), Real-time wildfire detection with semantic explanations** — evidence that explanations already exist; use it to define what a stronger satellite-monitoring explanation should add.

## Downloaded Full Texts

| Priority | File | Main use |
|---:|---|---|
| 1 | `04-jones-2022-himawari8-final-project-report.pdf` | Australian operational context |
| 2 | `03-zhang-2023-viirs-himawari-real-time-detection.pdf` | Closest Australian multi-sensor method |
| 3 | `06-giglio-2016-modis-collection6-fire.pdf` | MODIS foundation and limitations |
| 4 | `05-schroeder-2014-viirs-375m-active-fire.pdf` | VIIRS foundation and limitations |
| 5 | `02-zhang-2021-sentinel2-deep-active-fire-detection.pdf` | Deep segmentation comparator |
| 6 | `01-singh-2025-active-wildfire-detection-australia.pdf` | NSW/Australian case study |
| 7 | `11-manolakis-2022-real-time-semantic-explanations.pdf` | Explainability comparator |
| 8 | `07-rad-2024-vision-transformer-wildfire-detection.pdf` | Transformer comparator |
| 9 | `08-barco-2024-self-supervised-hotspot-detection.pdf` | Self-supervised temporal learning |
| 10 | `09-xu-2024-sen2fire-dataset.pdf` | External benchmark dataset |
| 11 | `10-zhao-2024-ts-satfire-dataset.pdf` | Time-series and multi-task benchmark |

These 11 files contain **188 pages** in total. Each file was opened with a PDF parser and checked for a valid page count and recognizable first-page text.

## Read Online

- [EFFIS active-fire detection technical background](https://forest-fire.emergency.copernicus.eu/about-effis/technical-background/active-fire-detection) — FIRMS-based operational processing, MODIS/VIIRS resolution, latency, filtering, and limitations.
- [DEA Hotspots overview](https://www.ga.gov.au/scientific-topics/dea/dea-data-and-products/dea-hotspots) and [technical documentation](https://knowledge.dea.ga.gov.au/data/product/dea-hotspots/) — Australian multi-sensor fields, access methods, lineage, and limitations.
- [MyFireWatch map](https://myfirewatch.landgate.wa.gov.au/map.html), [about](https://myfirewatch.landgate.wa.gov.au/about.html), and [limitations](https://myfirewatch.landgate.wa.gov.au/help.html) — public-facing Australian monitoring and caution statements.
- [NASA FIRMS](https://firms.modaps.eosdis.nasa.gov/active_fire/) — source active-fire products and archive access.

## Important Sources Not Included as Local PDFs

- [Kondylatos et al. (2024), *Advancements in remote sensing for active fire detection: A review of datasets and methods*](https://doi.org/10.1016/j.scitotenv.2024.173273) — first-choice recent review; use UTS Library access if the publisher requests authentication.
- [Giglio et al. (2003), *An Enhanced Contextual Fire Detection Algorithm for MODIS*](https://doi.org/10.1016/S0034-4257(03)00184-6) — foundational algorithm; use UTS Library access if needed.
- [FireCluster (2026)](https://www.sciencedirect.com/science/article/pii/S2666017226000611) — recent multi-source event clustering; important for showing that multi-sensor consolidation alone is not novel.

No paywall was bypassed. The local library contains only openly accessible author, repository, publisher, or preprint copies found during this collection pass.

## What to Record While Reading

For each paper, update `literature-matrix.csv` with:

1. the exact detection or monitoring target;
2. sensors, temporal frequency, study region, and label source;
3. data split unit—random pixel, scene, fire event, time period, or geography;
4. baselines and ablations;
5. false-positive and false-negative definitions;
6. probability calibration or uncertainty treatment;
7. explanation method and whether it was evaluated;
8. operational latency and missing-data assumptions;
9. limitations stated by the authors; and
10. one sentence explaining what remains unanswered for an Australian case study.

## Immediate Reading Goal

Read items 1–6 before proposing a final method. Send Dr Arnick a short evidence update only after extracting a comparison table: existing approach, data, validation design, main limitation, and the precise gap your study could test.

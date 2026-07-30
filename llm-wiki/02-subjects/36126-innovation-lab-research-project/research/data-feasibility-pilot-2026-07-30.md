# Public-Data Feasibility Pilot: DEA Hotspots and NSW Fire History

**Date:** 30 July 2026

**Status:** Completed feasibility pilot; not a detector-performance evaluation

## Question

Can public DEA hotspot observations and NSW Fire History polygons support a reproducible active-fire reliability study without first requesting a private dataset from Dr Arnick?

## Short answer

**Partly.** Public access and technical reproducibility are feasible. The main limitation is scientific label validity, not data access.

The pilot retrieved 19,849 DEA hotspots and 14 temporally overlapping NSW fire-event polygons without authentication or manual export. Exact point-in-polygon/time matching associated 2,878 hotspots (14.5%) with a recorded bushfire. Applying each sensor's documented positional tolerance increased this to 3,385 hotspots (17.1%), with three additional spatial-only observations. The remaining 16,461 buffered observations cannot be called false alarms from these data alone.

This result supports continuing the project, but only if it is framed initially as a **reference-data and hotspot-reliability audit**. A supervised true-fire/false-alarm model would require a stronger label design.

## Pilot design

| Item | Definition |
|---|---|
| Region | WGS84 bounding box `149.5–151.0°E, 33.7–32.3°S` |
| Hotspot period | 1–14 January 2020 UTC |
| Context | Gospers Mountain/Greater Blue Mountains fire period plus adjacent events |
| DEA records | 19,849 |
| NSW fire events | 14 |
| Fire-event lookback | 1 July 2019 |
| Exact match | Hotspot point inside final fire polygon and recorded ignition–extinguish interval |
| Sensitivity match | Exact definition plus sensor positional tolerance: VIIRS 0.375 km, MODIS/AVHRR 1 km, AHI 2 km |

## Data composition

| Sensor | Hotspots | Share |
|---|---:|---:|
| AHI / Himawari-8 | 13,674 | 68.9% |
| VIIRS | 4,446 | 22.4% |
| MODIS | 1,678 | 8.5% |
| AVHRR | 51 | 0.3% |
| **Total** | **19,849** | **100%** |

The 14 selected event records were all classified as bushfires. No prescribed-burn event appeared in this two-week event sample. All 14 contained fire ID, name, ignition date, extinguish date, fire type, cause, and area.

## Matching results

### Exact point-in-polygon and time

| Sensor | Matched bushfire | Unmatched | Match rate |
|---|---:|---:|---:|
| AHI | 1,510 | 12,164 | 11.0% |
| VIIRS | 1,026 | 3,420 | 23.1% |
| MODIS | 341 | 1,337 | 20.3% |
| AVHRR | 1 | 50 | 2.0% |
| **Total** | **2,878** | **16,971** | **14.5%** |

### Using documented sensor-position tolerance

| Sensor | Matched bushfire | Unmatched | Match rate |
|---|---:|---:|---:|
| AHI | 1,888 | 11,783 | 13.8% |
| VIIRS | 1,109 | 3,337 | 24.9% |
| MODIS | 385 | 1,293 | 22.9% |
| AVHRR | 3 | 48 | 5.9% |
| **Total** | **3,385** | **16,461** | **17.1%** |

Three AHI observations were spatially close enough after buffering but outside their matched event's recorded time window.

Most matched observations—2,983 of the buffered total—were associated with the `Stockyard Creek; Little` event. This concentration means results are not independent observations from 3,385 separate fires; repeated observations of one large event dominate the sample.

## Important findings

### 1. Access is not the blocker

Both primary sources can be queried programmatically and reproduced. No manual task is required for the current pilot.

### 2. Final fire polygons are an incomplete active-fire reference

A final boundary says where an event ultimately burned, not necessarily where active flame existed at every satellite acquisition. Conversely, an unmatched hotspot may reflect:

- a fire absent or incomplete in the selected event layer;
- temporal or spatial recording uncertainty;
- prescribed or managed burning not captured in the 14-event subset;
- industrial or other non-fire heat;
- a satellite commission error; or
- a true fire outside a final recorded polygon.

Therefore, unmatched must remain an **unresolved class**, not a negative label.

### 3. Positional accuracy explains only part of the mismatch

Sensor-specific buffers increased the matched count by 507, from 2,878 to 3,385. More than four-fifths of observations remained unresolved, so geolocation tolerance alone does not solve the reference problem.

### 4. Confidence is not comparable across algorithms

- AHI confidence was fixed at 50 for all 13,674 observations.
- AVHRR confidence was also fixed at 50.
- VIIRS and MODIS showed broader values, but individual algorithms used different ranges. For example, AFIMG used only values 7–9 while AFMOD used 0–100.

Raw confidence must not be pooled as if it were one probability scale. Calibration needs to be sensor- and algorithm-aware.

### 5. Random hotspot splitting would leak events

Repeated observations of the same large fire dominate the sample. A random row split would place the same event in training and testing and overstate generalisation. Evaluation must hold out complete fire events and future periods.

## Feasibility decision

### Decision: proceed, but modify the initial research task

The public data support:

- multi-sensor descriptive monitoring;
- event-level consolidation;
- sensor/algorithm-specific confidence auditing;
- reference-label quality analysis;
- spatial and temporal sensitivity analysis; and
- event-based validation design.

The current data do **not yet** support:

- labelling every unmatched hotspot as a false positive;
- estimating true detector specificity;
- training a trustworthy true-fire/false-alarm classifier; or
- claiming operational detection accuracy.

## Recommended next practical stage

1. Repeat the audit for several separate NSW events and a prescribed-burn period.
2. Add Historical FESM as an extent cross-check.
3. Search for an archived NSW RFS incident/event feed with point-in-time status.
4. Construct three labels: confirmed event, unresolved, and confirmed non-fire—rather than forcing a binary label.
5. Aggregate repeated hotspots into event candidates before modelling.
6. Compare confidence only within sensor and algorithm families.
7. Use held-out-event and chronological validation.

## What to ask Dr Arnick

Do not ask broadly whether he “has a dataset.” Send the pilot finding and ask one targeted question:

> I ran a public-data pilot using 19,849 DEA hotspots and 14 NSW Fire History events from the January 2020 Greater Blue Mountains period. The sources are accessible and reproducible, but only 17.1% of hotspots matched a recorded fire polygon and time window after applying sensor-specific position tolerances. The unmatched observations cannot be treated as false alarms because the NSW layer contains final event boundaries rather than point-in-time active-fire truth. Do you consider a reference-data and sensor-confidence reliability audit a suitable initial contribution, or do you know of an archived incident or verified active-fire source that could resolve the unmatched class?

This demonstrates completed investigation and identifies the exact evidence gap.

## Reproducibility

The accompanying pipeline records source URLs, retrieval timestamps, byte counts, SHA-256 checksums, query configuration, source counts, and matching outputs. Automated tests cover spatial containment, polygon boundaries, multipolygons, temporal windows, source URL construction, provenance hashing, positional buffering, normalization, and summaries.

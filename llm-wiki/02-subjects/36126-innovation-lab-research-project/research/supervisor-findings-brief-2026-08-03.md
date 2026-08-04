# Fire-Hotspot Reliability in NSW: Findings Update

**Prepared for:** Dr Arnick Abdollahi  
**Prepared by:** Tuan Nguyen  
**Date:** 4 August 2026  
**Status:** Preliminary findings for discussion — not a final literature review or a claim about operational detection accuracy

Following our 29 July meeting, this brief summarises what the literature shows about existing detection methods, transformer and graph-based approaches, data fusion, feature engineering, and explainability/uncertainty, together with a completed public-data feasibility pilot, a proposed research gap, and one question for your guidance.

## Problem statement

**Working title:** *Trustworthy Multi-Source Fire-Hotspot Reliability and Active-Fire Monitoring: An NSW Case Study*

The project focuses on fire-hotspot detection and active-fire monitoring, not fire-spread prediction. The literature and operational systems indicate that multi-sensor detection already exists; a stronger research contribution would investigate whether hotspot confidence is reliable under realistic sensor, event, and time variation.

The recommended initial contribution is a reproducible **reference-data and sensor-confidence reliability audit**, followed by modelling only if the available labels support it.

## Literature reviewed so far

Eleven full texts have been collected and read; the operational sources below have been checked against their official documentation. A small number of items still require full-text and citation-chaining verification, noted where relevant.

| Source | Contribution | Relevance to this project | Main issue still to investigate |
|---|---|---|---|
| Jones et al., *Himawari-8 Final Project Report* (NSW/Vic) | Operational Australian Himawari-8 trial and agency delivery | Establishes that high-frequency Australian hotspot monitoring already exists | Validation details, operational false alarms, latency, how reference events were established |
| Giglio et al. (2016), MODIS Collection 6 | Mature contextual active-fire algorithm and product-quality framework | Foundational operational baseline | Coarse pixels, limited overpasses, obscuration, confidence-flag interpretation |
| Schroeder et al. (2014), VIIRS 375 m | Higher-resolution product, better small-fire sensitivity | Important sensor/confidence baseline | Revisit limits, commission errors, whether confidence is calibrated |
| Zhang et al. (2023), VIIRS–Himawari-8 (Australia) | Real-time cross-sensor detection method | **Closest Australian multi-sensor comparator** | Cross-sensor alignment, label dependence, unseen-event validation, uncertainty |
| Zhang et al. (2021), Sentinel-2 deep detection (E. Australia/W. US) | Deep active-fire segmentation, IoU ~70–72% | Shows Australian deep-learning detection is not new | Semi-manual labels, revisit/cloud constraints, event leakage, transfer |
| Singh et al. (2025), Wolgan Valley NSW | SVM active-fire/burned-area discrimination on Landsat-8 | Direct NSW case-study baseline | Single-region scope, limited fit for continuous monitoring |
| Rad et al. (2024) — transformer | Vision-transformer wildfire detector (North America) | Shows applying a transformer alone is not novel | Geographic transfer, operational latency, calibrated reliability |
| Barbastathis et al. (2024) | Self-supervised temporal hotspot detection (Europe) | Motivates label-efficient temporal learning | Preprint status, Australian transfer, calibration |
| Sen2Fire / TS-SatFire (2024) | International benchmark datasets, detection + time-series task definitions | Useful for benchmark design/pretraining | Dataset shift; whether labels represent Australian operations |
| Manolakis et al. (2022) | Semantic explanations for real-time event-stream detection | Shows explainability already exists elsewhere in detection | Whether explanations are faithful, stable, and applicable to satellite false alarms |
| Kondylatos et al. (2024) — review | Reviews active-fire datasets and methods globally | Primary map of the international landscape | Full-text review and citation chaining still required |

**Transformers.** Rad et al. (2024) and Barbastathis et al. (2024) both confirm that applying a time-series or vision transformer to fire detection is not by itself a novel contribution. The open question is what a transformer would add specifically to reliability rather than raw detection.

**Graph-based/GNN methods.** Two recent papers were identified in the discovery search but have not yet been full-text verified or added to the formal literature matrix: *Explainable global wildfire prediction model using graph neural networks* (graph-based sequence learning for global burned-area forecasts) and *Causal Graph Neural Networks for robust wildfire forecasting across geographic shifts* (geographic generalisation and causal structure — likely the central comparator if a graph approach is pursued). Both indicate graph modelling for wildfire is already represented in the literature, so it would need a specific justification here rather than novelty by architecture alone.

**Multi-source data fusion.** MODIS, VIIRS, Himawari/AHI, Sentinel-2, and Landsat offer complementary spatial resolution, revisit frequency, and latency; Australian operational services (DEA Hotspots, MyFireWatch) already fuse several of these. The research question is therefore not whether to fuse sensors, but whether a specific fusion and reliability design improves outcomes under event, time, and region shifts — this is tested empirically in the pilot below.

**Feature engineering.** Climate, weather, vegetation, and land-use drivers appear across the reviewed set, but no paper in the current matrix isolates feature-engineering choices as its primary contribution. This remains an area for deeper full-text review before firmer conclusions can be drawn.

## Recurring limitations

- **Spatial–temporal resolution trade-off.** High-frequency geostationary sensors miss small or weak fires; finer polar-orbiting sensors have longer revisit intervals; cloud, smoke, and viewing geometry affect both.
- **Reference labels are imperfect.** Training against MODIS/VIIRS products or fire-boundary polygons risks reproducing their own omissions and commission errors — confirmed directly by the pilot below.
- **Validation often does not demonstrate deployment generalisation.** Random splits let the same fire event leak across training and test data.
- **Accuracy metrics alone miss operational cost.** False-alarm burden, detection delay, and calibration are usually not reported together.
- **Confidence is not consistently calibrated** across sensors or algorithms.
- **Explanations are rarely validated** for stability across folds, events, seasons, and regions.

## Candidate research gaps

| Gap | Direction | Main risk |
|---|---|---|
| **A — Trustworthy multi-sensor monitoring** | NSW case study; DEA multi-sensor hotspots; strong contextual/tree baselines plus one sensor-aware temporal model; event-based and chronological holdouts; calibration and stable explanations | Matching hotspots to independently verified events and constructing credible negative labels may be substantial |
| **B — Reliability audit and calibrated detection (recommended starting point)** | One NSW subregion; compare operational confidence against simple and deep baselines under event-based splits; explicit false-alarm taxonomy and calibration | Narrower scope than A, but matches what the data can currently support |
| **C — Label-efficient temporal adaptation** | Self-supervised pretraining on unlabelled Australian observations, fine-tuned on limited verified events | Implementation and dataset scale risk exceeding one semester on top of the reliability work |

The pilot described below is direct empirical evidence for Gap B: it shows the core open problem is reference-label validity, not sensor access or model architecture. Gap B is therefore recommended as the initial contribution, with Gap A's advanced multi-sensor model as a natural extension if stronger point-in-time labels become available, and Gap C set aside for this semester given the additional engineering risk on an already tight timeline.

## Completed public-data feasibility pilot

Public data was tested for feasibility before requesting a private dataset.

| Item | Pilot result |
|---|---:|
| Region and period | Greater Blue Mountains area, 1–14 January 2020 |
| DEA hotspot observations | 19,849 |
| Temporally overlapping NSW Fire History events | 14 |
| Exact polygon-and-time matches | 2,878 (14.5%) |
| Matches after sensor-specific positional buffering | 3,385 (17.1%) |
| Unresolved observations after buffering | 16,461 |

The data sources were publicly accessible and the workflow was reproducible. The scientific limitation is label validity rather than data access.

### Key pilot findings

1. **Unmatched does not mean false alarm.** NSW Fire History polygons describe final event extents rather than point-in-time active flame. An unmatched observation could be a true fire missing from the selected reference, a prescribed burn, non-fire heat, geolocation or temporal uncertainty, or a satellite commission error.
2. **Position tolerance explains only part of the mismatch.** Sensor-specific buffers increased matches by 507, but more than four-fifths of observations remained unresolved.
3. **Confidence values cannot be pooled directly.** AHI and AVHRR confidence was fixed at 50 in this sample, while VIIRS and MODIS algorithms used different ranges. Calibration must therefore be sensor- and algorithm-aware.
4. **Random row splitting would leak fire events.** Most buffered matches — 2,983 — came from one event, `Stockyard Creek; Little`. Evaluation should hold out complete events and future periods.

This pilot is a data-feasibility and reference-quality audit, not an estimate of operational detection accuracy.

## Refined research question

> How reliable are DEA hotspot confidence indicators across sensors, algorithms, fire events, and time in an NSW case study, and can sensor-aware calibration improve their decision usefulness under held-out-event and future-period evaluation?

If stronger point-in-time labels become available, the question could be extended to compare a temporal model against operational-confidence, logistic-regression, and tree-based baselines.

## Feasibility and risk notes

| Risk | Status after the pilot | Mitigation |
|---|---|---|
| No independent active-fire reference | Confirmed as the central issue — only 17.1% of hotspots matched a recorded event even with positional buffering | Treat unmatched as a third, unresolved class rather than a false alarm; a possible archived incident or verified point-in-time source would help resolve this |
| Too few verified events | Confirmed — only 14 events in the pilot window, one of which dominates the matched sample | Expand the audit across more events and seasons before drawing conclusions; hold out complete events in any evaluation |
| Sensor/algorithm confidence not comparable | Confirmed — AHI/AVHRR fixed at 50, VIIRS/MODIS use different ranges | Calibrate within sensor/algorithm families, not pooled |
| Semester timeline | Open | Treat the reliability audit as the minimum publishable contribution; extend to modelling only if labels support it |

## Proposed next stage

1. Repeat the audit across several independent NSW fires and at least one prescribed-burn period.
2. Add Historical Fire Extent and Severity Mapping as a complementary reference.
3. Use transparent labels — **confirmed event**, **unresolved**, and **confirmed non-fire** — rather than forcing unmatched observations into a false-alarm class.
4. Aggregate repeated observations into event candidates.
5. Compare confidence within sensor and algorithm families.
6. Use held-out-event and chronological validation.
7. Add an advanced temporal or graph model only if it answers a demonstrated limitation better than simpler baselines.

## Question for your guidance

> Does a reference-data and sensor-confidence reliability audit (Gap B above), using the three-class treatment described, constitute a suitable initial research contribution? If stronger labels are necessary, is there an archived incident record or verified point-in-time active-fire source that could help resolve the unmatched class?

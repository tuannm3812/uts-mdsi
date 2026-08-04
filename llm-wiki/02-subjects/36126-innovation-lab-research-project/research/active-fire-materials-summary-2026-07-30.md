# Active-Fire Research Materials Summary

**Superseded:** [supervisor-findings-brief-2026-08-03.md](supervisor-findings-brief-2026-08-03.md) is the canonical document for external communication with Dr Arnick. This file is kept as research history.

**Prepared:** 30 July 2026

**Purpose:** Working evidence summary for discussion with Dr Arnick Abdollahi

**Scope:** Fire-hotspot detection and active-fire monitoring; fire-spread modelling is excluded

## Executive summary

The reviewed materials show that active-fire detection is already supported by mature satellite products and operational systems. MODIS, VIIRS, Himawari-8, and Sentinel-2 offer different combinations of spatial detail, observation frequency, and latency. Australian systems already combine several of these sources, and prior Australian studies have applied both conventional machine learning and deep learning.

The main unresolved problem is therefore not simply detecting a bright or hot pixel. It is determining **how reliable a hotspot is under realistic monitoring conditions**: different sensors, repeated observations, missing data, cloud and smoke, non-fire heat sources, new fire events, future time periods, and geographic shifts.

The strongest provisional direction is:

> Evaluate and improve the reliability of multi-source active-fire hotspots for a bounded NSW case study using event-based and temporal validation, calibrated confidence, explicit false-alarm analysis, and stable explanations.

This is a working direction rather than a final novelty claim. Full-text extraction, citation chaining, data inspection, and supervisor confirmation are still required.

## What the operational materials establish

| Source | What it provides | Important limitation or lesson |
|---|---|---|
| Digital Earth Australia Hotspots | Australian hotspot records from sources including MODIS, VIIRS, and Himawari/AHI; acquisition time, algorithm, temperature, power, confidence, state, and positional accuracy | False positives and false negatives occur. Cloud, smoke, canopy, small or cool fires, sensor outages, viewing conditions, and revisit timing affect observations. |
| MyFireWatch | Public Australian map combining recent hotspots with wind, vegetation, fire danger, burnt area, and lightning context | It can miss small or obscured fires, can show industrial heat, does not distinguish prescribed burns, and documents kilometre-scale location uncertainty. |
| EFFIS | FIRMS-based active-fire display using MODIS and VIIRS; contextual filtering based on land cover, urban/artificial surfaces, and source confidence | A thermal anomaly is not proof of a vegetation fire. Small or obscured fires may be missed and other heat sources may be detected. |
| NASA FIRMS | Standard access point for MODIS and VIIRS active-fire products | Near-real-time products are operational evidence, not automatically independent ground truth. |

### Key implication

Contextual false-positive filtering and confidence indicators already exist operationally. A proposal to “add land cover,” “combine hotspots,” or “show confidence” is not sufficiently original without a clearly evaluated improvement.

## Comparison of the most relevant research materials

| Material | Geography and data | Contribution | Relevance to this project | Main issue to investigate |
|---|---|---|---|---|
| Jones et al., Himawari-8 final project report | NSW and Victoria; high-frequency Himawari-8 monitoring | Operational Australian trial and agency delivery context | Establishes that high-frequency Australian hotspot monitoring already exists | Validation details, operational false alarms, latency, and how the reference events were established |
| Giglio et al. (2016), MODIS Collection 6 | Global MODIS thermal data | Mature contextual active-fire algorithm and product-quality framework | Foundational baseline for operational hotspot detection | Coarse pixels, limited overpasses, obscuration, and interpretation of confidence flags |
| Schroeder et al. (2014), VIIRS 375 m | Global VIIRS observations | Higher-resolution active-fire product with improved small-fire sensitivity | Important sensor and confidence baseline | Revisit limitations, commission errors, and whether product confidence is calibrated |
| Zhang et al. (2023), VIIRS–Himawari-8 | Australia; VIIRS product plus Himawari-8 data | Real-time cross-sensor detection method | Closest Australian multi-sensor comparator | Cross-sensor alignment, label dependence, unseen-event validation, and uncertainty |
| Zhang et al. (2021), Sentinel-2 deep detection | Eastern Australia and western United States | Deep active-fire segmentation using Sentinel-2 | Shows that Australian deep-learning detection is not new | Semi-manual labels, revisit and cloud constraints, event leakage, and transfer |
| Singh et al. (2025) | Wolgan Valley, NSW; Landsat-8 bands and spectral indices | SVM-based active-fire and burned-area discrimination | Useful local baseline and potential case-study comparison | Single-region scope and limited suitability for continuous monitoring |
| Rad et al. (2024) | North America; multispectral imagery | Vision-transformer wildfire detector | Shows that applying a transformer is not itself novel | Geographic transfer, operational latency, and calibrated reliability |
| Barbastathis et al. (2024) | European events; temporal remote-sensing data | Self-supervised temporal hotspot detection | Motivates label-efficient temporal learning | Preprint status, Australian transfer, and confidence calibration |
| Sen2Fire and TS-SatFire (2024) | International benchmark datasets | Detection and time-series task definitions | Useful for benchmark design and possible pretraining | Dataset shift and whether benchmark labels represent Australian operations |
| Manolakis et al. (2022) | Real-time event streams | Semantic explanations for wildfire detection | Shows that explainability in real-time fire detection already exists | Whether explanations are faithful, stable, and applicable to satellite false alarms |
| Kondylatos et al. (2024) | Global review | Reviews active-fire datasets and methods | Primary map of the international research landscape | Full-text review and citation chaining are still required |

## Key findings across the materials

### 1. Sensor complementarity is useful but already known

- MODIS provides long-term global coverage but comparatively coarse spatial observations.
- VIIRS provides 375 m active-fire detection and better sensitivity to relatively small fires.
- Himawari-8 offers frequent observations but coarser spatial detail.
- Sentinel-2 and Landsat provide richer spatial and spectral detail but cannot support continuous monitoring because of revisit and cloud constraints.

The research question should test whether a specific sensor-aware design improves reliability; “multi-sensor fusion” alone is too broad.

### 2. Labels are a central scientific risk

Satellite product agreement is not identical to verified fire detection. Training against MODIS or VIIRS may reproduce their omissions and false alarms. Fire boundaries may indicate where an event eventually burned but not the exact location and time of active flame.

A credible study needs to document:

- the reference event source;
- spatial and temporal matching tolerances;
- how prescribed burns and industrial heat are handled;
- how negative examples are constructed; and
- uncertainty in the labels themselves.

### 3. Random pixel splits may overstate performance

Neighbouring pixels or observations from the same fire can appear in both training and test data. A deployment-oriented evaluation should hold out complete fire events and future time periods, with a separate subregional test if data volume permits.

### 4. Standard accuracy metrics are insufficient

Operational usefulness also depends on:

- precision and missed-fire recall;
- false alarms per unit area or time;
- detection delay, where measurable;
- probability calibration;
- performance by sensor, season, event size, and subregion; and
- behaviour when observations are missing or obscured.

### 5. Confidence and explanation require evaluation

A product confidence flag, neural-network score, and calibrated probability are different quantities. Similarly, a visually plausible attention or SHAP plot is not evidence of a stable or faithful explanation.

The project should evaluate calibration with reliability curves, Brier score, and expected calibration error. Explanations should be checked across folds, events, seasons, and regions and compared with known sensor or environmental failure mechanisms.

## Candidate research gaps

### Gap A — Recommended

**Trustworthy multi-source hotspot reliability**

Existing systems provide multi-sensor hotspots, but the reviewed material offers limited evidence of an Australian evaluation that jointly tests calibrated confidence, event/time generalisation, false-alarm mechanisms, missing-observation robustness, and explanation stability.

Possible research question:

> Can a sensor-aware spatiotemporal model improve the reliability of DEA hotspot confidence for an NSW case-study region compared with operational confidence and strong non-neural baselines under held-out-event and future-period evaluation?

### Gap B — Safer fallback

**Rigorous calibration and false-alarm audit**

Compare operational confidence, logistic regression, and tree-based models using event-based and chronological splits. Focus on calibration and an explicit false-alarm taxonomy rather than a complex architecture.

Possible research question:

> How reliable are existing DEA hotspot confidence indicators across sensors, seasons, events, and NSW subregions, and can post-hoc or contextual calibration improve their decision usefulness?

### Gap C — Higher risk

**Label-efficient Australian temporal adaptation**

Use self-supervised learning on unlabelled Australian observations, then test how performance and calibration change when only a limited number of verified events are available.

Possible research question:

> Can self-supervised temporal representations reduce the labelled-event requirement for active-fire detection while retaining calibration and geographic transfer in an Australian case study?

## Recommended direction and minimum viable study

### Working title

**Trustworthy Multi-Source Fire-Hotspot Reliability and Active-Fire Monitoring: An NSW Case Study**

### Minimum viable design

1. Select one NSW subregion after auditing event count and data completeness.
2. Define one detection or monitoring target precisely.
3. Use DEA hotspot records and their sensor, time, confidence, and accuracy metadata.
4. Construct an independently documented event-reference dataset.
5. Establish operational-confidence, logistic, and tree-based baselines.
6. Add only one temporal or event-level advanced model if the data justify it.
7. Hold out complete fire events and a future period.
8. Report detection performance, false-alarm burden, and calibration.
9. Analyse errors by sensor and environmental context.
10. Test explanation stability rather than presenting explanations only.

Graph modelling should remain optional. It should be used only if a defensible graph structure—such as sensor–event relationships, spatial-cell adjacency, or evolving event clusters—adds value beyond simpler temporal and tree-based models.

## Main feasibility risks

| Risk | Why it matters | Early mitigation |
|---|---|---|
| No independent active-fire reference | Product-to-product agreement cannot prove real-fire detection | Ask Dr Arnick about prepared fire-event or Himawari/VIIRS datasets before modelling |
| Fire boundaries lack exact active time | Spatial overlap can create incorrect labels | Use explicit temporal windows and document label uncertainty |
| Too few verified events | Complex models and geographic tests become unreliable | Begin with a data audit and reduce the region or model complexity |
| Prescribed burns and industrial heat | They may be counted incorrectly as errors or fires | Build a transparent event and false-alarm taxonomy |
| Sensor and time mismatch | Cross-sensor fusion can introduce alignment errors | Quantify spatial/temporal tolerances and run sensitivity checks |
| Semester timeline | Data engineering could consume the project | Treat the calibrated reliability audit as the minimum publishable contribution |

## Initial data-feasibility audit

We should investigate the public data ourselves before asking Dr Arnick for a dataset.

| Candidate source | Potential role | Availability found | Suitability issue to test |
|---|---|---|---|
| DEA Hotspots | Primary hotspot observations and operational confidence | Public historical service with sensor, acquisition time, temperature, power, confidence, positional accuracy, state, and algorithm metadata | Confirm bulk-download workflow, historical completeness by sensor, and changing algorithm versions |
| NSW Fire History feature service | Fire-event polygons and complementary labels | Public query/extract service supporting GeoJSON; includes fire ID/name, fire type, ignition/capture/extinguish dates, cause, area, agency, and geometry | Dates or polygons may be incomplete and represent final extent rather than the location of active flame at a given time |
| NPWS Fire History download | Wildfire versus prescribed-burn distinction | Public ZIP, WMS, and WFS; CC Attribution; updated monthly; coverage listed from 1920 | Confirm record completeness outside NPWS estate and attribute completeness in the selected period |
| Historical FESM | Independent fire extent and severity context | Public NSW dataset derived from Sentinel-2/Landsat mapping | It is retrospective and may not supply exact active-fire timestamps |
| NSW RFS Current Incidents Feed | Incident location and current operational status | Public GeoJSON, GeoRSS, and CAP feed updated every 30 minutes | The public page does not establish a queryable historical archive; collection starting now would not cover earlier model periods |
| NASA FIRMS | MODIS/VIIRS source archive and comparator | Public archive and near-real-time products | It is not independent of DEA records derived from the same source products |

### Data-audit decision rule

Before contacting Dr Arnick about data, we should:

1. download a small DEA sample for one NSW fire season;
2. query the NSW Fire History service for the same region and period;
3. measure missingness in event dates and key attributes;
4. attempt spatial–temporal matching for a small set of known fires;
5. quantify how many hotspots can be assigned to wildfires, prescribed burns, or no recorded polygon;
6. inspect unmatched examples rather than treating them automatically as errors; and
7. document the precise evidence gap.

Only then should we ask whether he has a higher-resolution or independently verified event dataset that addresses the identified limitation.

## Questions to confirm with Dr Arnick after the data audit

1. Does the intended meaning of active-fire monitoring include only repeated current detections, or also short-horizon forecasting?
2. Based on our audit, does he consider NSW Fire History/FESM sufficiently independent and temporally precise for validation?
3. If not, does he have access to a prepared or independently verified active-fire event source that addresses the specific missing fields?
4. Is NSW acceptable, and does he recommend a particular subregion or fire season?
5. Would he prefer a methodological model contribution or a rigorous trustworthy-AI evaluation contribution?
6. Is a calibrated reliability audit an acceptable minimum contribution if the independent-label audit makes multi-sensor modelling infeasible?

## Suggested update to Dr Arnick

> Hi Arnick, I’ve started reviewing the operational resources and the main Australian and international active-fire studies. The key issues emerging are the trade-off between spatial resolution and observation frequency, imperfect reference labels, false alarms from non-fire heat sources, and limited evidence of calibration and event-based generalisation. Multi-sensor detection and contextual filtering already exist, so I’m currently considering a narrower NSW study on hotspot reliability—event/time validation, calibrated confidence, false-alarm analysis, and stable explanations. I’m now auditing DEA Hotspots against the public NSW Fire History and FESM sources. Once I have tested their temporal and spatial suitability, I’ll send you the comparison and any specific data limitation that needs your advice.

## Evidence status

- The operational-source statements have been checked against the DEA, MyFireWatch, EFFIS, and FIRMS documentation.
- Eleven accessible PDFs have been collected and technically verified.
- Several comparison entries remain at preliminary or partial full-text extraction level.
- The gap statement must be re-tested after complete extraction of the closest studies and backward/forward citation searching.

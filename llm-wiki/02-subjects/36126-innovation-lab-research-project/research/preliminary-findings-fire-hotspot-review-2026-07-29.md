# Preliminary Findings: Fire-Hotspot Detection and Active-Fire Monitoring

**Superseded:** [supervisor-findings-brief-2026-08-03.md](supervisor-findings-brief-2026-08-03.md) is the canonical document for external communication with Dr Arnick. This file is kept as research history.

## Purpose and status

This brief responds to Dr Arnick Abdollahi's request to identify what has been done, recurring limitations, and feasible research gaps in fire-hotspot detection and active-fire monitoring.

- **Review scope:** Australia and other regions globally
- **Modelling scope:** one Australian state or fire-prone region
- **Excluded task:** fire-spread forecasting
- **Current evidence:** 15 seed records, including 11 peer-reviewed publications, three preprints, and one Australian technical report
- **Status:** preliminary abstract-level screening; key full texts and citation chains still require verification

The findings below are defensible working conclusions, not final systematic-review claims.

## Executive finding

Fire-hotspot detection is already supported by mature contextual algorithms and operational MODIS, VIIRS, and geostationary-satellite products. Recent research has also applied deep segmentation, attention, vision transformers, self-supervised temporal learning, multi-sensor fusion, and explainable event processing.

Therefore, the following would **not** be sufficient originality by themselves:

- applying machine learning to satellite fire imagery;
- using a transformer for fire detection;
- combining multiple satellite products;
- producing SHAP or attention visualisations;
- conducting a single-event NSW case study with a random train/test split.

The strongest feasible research opportunity found so far is:

> **A trustworthy reliability layer for multi-source DEA fire hotspots in an NSW case study, using event-based and temporal validation, calibrated confidence, false-alarm analysis, and stable explanations.**

The contribution should be framed around reliability and decision usefulness under realistic monitoring conditions. The advanced model—temporal transformer, graph model, or another architecture—should be selected only after the data audit and gap verification.

## What has already been done

### 1. Operational contextual detection is mature

MODIS and VIIRS active-fire products are established baselines. The MODIS contextual algorithm improved sensitivity to smaller and cooler fires while reducing persistent false alarms, and Collection 6 provides a long-running global product. VIIRS provides finer 375 m active-fire detection and improved sensitivity to smaller fires. These products already contain quality or confidence indicators, although these are not equivalent to an end-to-end calibrated probability of a true operational fire.

Key evidence:

- [Enhanced MODIS contextual algorithm](https://doi.org/10.1016/S0034-4257%2803%2900184-6)
- [MODIS Collection 6 algorithm and products](https://doi.org/10.1016/j.rse.2016.02.054)
- [VIIRS 375 m active-fire product](https://doi.org/10.1016/j.rse.2013.12.008)
- [NASA FIRMS active-fire archive](https://firms.modaps.eosdis.nasa.gov/active_fire)

### 2. Australia already has operational hotspot monitoring

[Digital Earth Australia Hotspots](https://knowledge.dea.ga.gov.au/data/product/dea-hotspots/) is a national multi-sensor vector data service covering 27 August 2002 to the present. It incorporates MODIS, VIIRS, and Himawari/AHI sources and is updated every 10 minutes. Available attributes include sensor, processing algorithm and version, acquisition and processing time, temperature, power, confidence, positional accuracy, and Australian state.

[MyFireWatch](https://myfirewatch.landgate.wa.gov.au/map.html) is another Australian operational map service. It combines recent hotspots with fire-danger ratings, wind, vegetation, burnt areas, and lightning layers. Its documentation states that hotspot updates depend on satellite availability and are generally refreshed every two to four hours.

Australia has also trialled Himawari-8 hotspot delivery to NSW and Victorian agencies. Consequently, an Australian hotspot map, basic historical dashboard, or elementary multi-sensor integration would reproduce existing capability rather than constitute research novelty.

These systems provide both a potential data foundation and a concrete problem statement: their confidence and location information must be interpreted carefully, false positives and false negatives occur, and neither system is intended to be used alone for safety-of-life decisions.

### 3. Australian machine-learning detection studies exist

Two close studies constrain the novelty claim:

- A 2025 Wolgan Valley, NSW study used Landsat-8 bands, an NDFI index, and SVMs for active-fire and burned-area discrimination: [Singh et al.](https://doi.org/10.1007/s11069-025-07163-w).
- A 2021 study trained a DCPA+HRNetV2 active-fire segmentation framework on Sentinel-2 samples from eastern Australia and the western United States, reporting IoU near 70–72% in the two test areas: [Zhang et al.](https://doi.org/10.3390/rs13234790).

These establish that neither “machine learning in NSW” nor “deep learning on Australian satellite imagery” is new.

### 4. High-frequency and high-resolution sensors have complementary strengths

Polar-orbiting sensors such as VIIRS and Sentinel provide useful spatial detail but observe a location intermittently. Geostationary platforms such as Himawari provide frequent observations at coarser spatial resolution. A 2023 study already combined VIIRS fire products with Himawari-8 for real-time detection in Australia: [Real-Time Wildfire Detection Algorithm Based on VIIRS and Himawari-8](https://doi.org/10.3390/rs15061541).

The research opportunity is therefore not simply to fuse these sensors, but to test whether a specific fusion and reliability design improves detection under event, time, and region shifts.

### 5. Transformers and temporal learning are already represented

- A vision-transformer architecture has been evaluated for multispectral wildfire detection in North America: [Rad, 2024](https://proceedings.mlr.press/v222/rad24a.html).
- Self-supervised multi-temporal hotspot detection has been proposed for European events: [Rapid Wildfire Hotspot Detection](https://arxiv.org/abs/2405.20093).
- TS-SatFire combines active-fire detection, daily monitoring, and next-day prediction in a satellite time-series dataset: [TS-SatFire](https://arxiv.org/abs/2412.11555).

This means the research question must explain why a temporal architecture is appropriate for the monitoring definition and what scientific or operational weakness it addresses.

### 6. Multi-source fusion is an active research area

Recent work integrates several active-fire products. FireCluster combines MODIS, VIIRS, Landsat-8, and Himawari-8 observations for event identification in China. This further raises the novelty threshold for a generic “multi-source fusion” contribution: [FireCluster](https://www.sciencedirect.com/science/article/pii/S2666017226000611).

### 7. Explainability and uncertainty remain uneven

Semantic explanations have been studied for real-time event-stream fire detection: [FADE](https://doi.org/10.1016/j.eswa.2022.117007). Explainability is also common in fire susceptibility and occurrence modelling. However, preliminary screening found fewer active-fire satellite studies that jointly evaluate:

- calibrated probability;
- false-alarm burden;
- uncertainty under cloud, smoke, sensor, event, and geographic shifts;
- stability of explanations across time and regions; and
- whether explanations correspond to operationally meaningful failure modes.

A recent review identifies data-quality management, multimodal learning, spatiotemporal modelling, self-supervision, and interpretable models as continuing directions: [Kondylatos et al., 2024](https://doi.org/10.1016/j.scitotenv.2024.173273).

## Recurring limitations

### L1. Spatial–temporal resolution trade-off

High-frequency geostationary monitoring may miss small or weak fires because of coarse pixels. Finer-resolution polar-orbiting sensors may detect smaller fires but have longer revisit intervals. Cloud, smoke, viewing geometry, saturation, and background temperature further affect detection.

### L2. Labels and reference products are imperfect

Manual labels are expensive and subjective. Using MODIS or VIIRS detections as ground truth can transfer their omissions, commission errors, and resolution limits into a learned model. Evaluation must distinguish “agreement with a satellite product” from “detection of a verified fire.”

### L3. Validation often does not demonstrate deployment generalisation

A detector can perform well when neighbouring pixels, the same fire event, or the same acquisition period appear in both training and testing. Random image or patch splits may overstate performance. Monitoring research needs held-out fire events, future periods, and preferably distinct subregions.

### L4. Accuracy is often disconnected from operational cost

ROC-AUC, accuracy, or IoU alone do not quantify alert fatigue, missed small fires, detection delay, or confidence reliability. False positives from industrial heat, sun glint, hot bare ground, cloud edges, and other thermal anomalies are operationally important.

The two Australian systems make these limitations concrete:

- MyFireWatch notes that hotspots may represent heavy industry, may be missed through cloud or smoke, may omit small or cool fires, and can have location uncertainty of approximately 2 km or as much as 5 km near image edges.
- DEA documents false positives and false negatives, sunrise/sunset reliability issues for geostationary detection, interrupted sensor feeds, a best-case positional accuracy of ±375 m, and missed observations caused by cloud, smoke, canopy, small fire size, cool fires, or satellite revisit timing.

### L5. Confidence is not consistently calibrated

Product confidence flags, neural softmax scores, and model uncertainty are different concepts. Few screened active-detection studies jointly report calibration, reliability diagrams, Brier score, and performance under distribution shift.

### L6. Explanations are rarely validated

Attention maps and feature attribution can appear plausible without being stable or faithful. Explanations should be tested across folds, events, seasons, and regions and connected to sensor physics or known false-alarm mechanisms.

## Candidate research gaps

### Gap A — Recommended: trustworthy multi-sensor monitoring

> Although operational and research systems combine polar-orbiting and geostationary fire observations, the reviewed literature provides limited evidence that learned multi-source active-fire detectors are simultaneously calibrated, explanation-stable, and validated on held-out events and future periods in an Australian operational context.

Possible contribution:

- NSW case study;
- DEA historical hotspots as the multi-sensor foundation;
- MODIS, VIIRS, and Himawari/AHI source and algorithm metadata;
- NSW incident or fire-history records as imperfect complementary references;
- strong contextual and tree-based baselines;
- one sensor-aware temporal or event-level model;
- event-based and chronological holdouts;
- calibration, false-alarm taxonomy, and uncertainty under missing/cloud-affected observations;
- stable regional and temporal explanations.

Main risk: matching hotspot records to independently verified active-fire events and constructing credible negative/false-alarm labels may be substantial.

### Gap B — Safer fallback: reliability audit and calibrated detection

> Existing Australian active-fire detection studies demonstrate classification or segmentation performance, but there is an opportunity for a rigorous reliability audit that compares simple and deep models under event-based splits, calibration analysis, and explicit false-alarm categories.

Possible contribution:

- one NSW subregion and a curated set of fire events;
- Landsat-8/9 or Sentinel-2 multispectral inputs;
- spectral-index, SVM/tree, CNN, and compact attention baseline comparison;
- spatial/event holdouts;
- probability calibration and error analysis;
- explanation stability.

Main limitation: Sentinel/Landsat revisit times make the project detection-focused rather than genuinely continuous monitoring.

### Gap C — Higher-risk: label-efficient temporal adaptation

> Self-supervised temporal detection has been explored internationally, but its transferability to Australian landscapes, sensors, and fire regimes remains underexplored in the screened evidence.

Possible contribution:

- pretrain temporal representations on unlabelled Australian observations;
- fine-tune on limited verified fire events;
- compare label efficiency and geographic transfer;
- quantify calibration as labelled data decrease.

Main risk: implementation and dataset scale may exceed the semester.

## Case-study region recommendation

### Recommended: NSW, with a smaller subregion if necessary

NSW should be the first candidate because it offers the strongest current combination of:

- direct alignment with Dr Arnick's suggestion;
- recent active-fire ML studies in Wolgan Valley and eastern Australia;
- historical fire-boundary data extending back to 1920 and updated monthly through the [NSW NPWS Fire History dataset](https://data.nsw.gov.au/data/dataset/fire-history-wildfires-and-prescribed-burns-1e8b6);
- operational and near-real-time remote-sensing programmes, including [NSW Fire Extent and Severity Mapping](https://www.environment.nsw.gov.au/topics/animals-and-plants/native-vegetation/landcover-science/fire-extent-and-severity-maps);
- evidence from the 2019–20 season, during which 5.52 million hectares burned in NSW according to the [NSW RFS annual report](https://data.nsw.gov.au/data/dataset/8f42856f-21b7-4306-9157-7c846e925745/resource/5aaf942f-64e3-46cf-8182-4516e5c2b87d/download/nsw_rfs_annual_report_2019_20_19105.pdf); and
- manageable options for subregional analysis.

This does not establish that NSW is universally “the most fire-prone” Australian state. It establishes that NSW is currently the most defensible **semester case study** based on relevance, data readiness, prior work, and operational context.

Possible subregions to audit:

- Greater Blue Mountains / Wolgan Valley, enabling direct comparison with prior work;
- South Coast and southeastern NSW, strongly represented in 2019–20 events;
- a bioregional subset selected by event count and data completeness.

## Recommended provisional direction

### Working title

**Trustworthy Multi-Source Fire-Hotspot Reliability and Active-Fire Monitoring: An NSW Case Study**

### Provisional research question

> Can sensor-aware spatiotemporal modelling improve the reliability of DEA active-fire hotspot confidence in an NSW case-study region compared with existing product-confidence and single-sensor baselines under held-out-event and future-period evaluation?

### Supporting questions

1. How much does each sensor or source contribute under normal and missing-observation conditions?
2. How well do existing confidence fields and proposed probabilities correspond to independently recorded fires across events, seasons, and subregions?
3. Which conditions drive false positives and false negatives?
4. Are model explanations stable and consistent with sensor physics and environmental context?
5. Does the advanced model provide enough benefit to justify its complexity?

### Minimum viable experiment

- One NSW subregion
- One clearly defined active-fire target
- DEA hotspot records from selected sensors
- Existing DEA confidence as an operational baseline
- Tree-based or logistic baseline
- One advanced temporal model
- Held-out-event and chronological validation
- Precision, recall, F1, PR-AUC, false alarms per area/time, detection delay where measurable
- Brier score, calibration curve, and expected calibration error
- Explanation and error-stability analysis

Graph modelling should remain optional unless the evidence identifies a defensible graph—such as sensor-event relations, spatial cells, or fire-event connectivity—that adds value beyond a temporal fusion model.

## Questions for Dr Arnick after he reviews the findings

1. Does “active-fire monitoring” in the intended project include detection from repeated satellite observations only, or should it include short-horizon hotspot forecasting?
2. Does he have access to a prepared Himawari, VIIRS, MODIS, or NSW fire-event dataset?
3. Would he prefer a method contribution or a rigorous trustworthy-AI evaluation contribution?
4. Is NSW acceptable as the case-study state, and is there a preferred subregion?
5. Should the project prioritise calibrated confidence and false-alarm reduction over comparing both transformer and graph models?

## Recommended next step

Send this preliminary direction with the evidence matrix to Dr Arnick, clearly labelled as an initial scan. Ask him to confirm the operational definition of monitoring, available data, and preferred NSW subregion before beginning dataset construction.

## Supervisor-provided operational resources

- [MyFireWatch](https://myfirewatch.landgate.wa.gov.au/map.html)
- [Digital Earth Australia Hotspots overview](https://www.ga.gov.au/scientific-topics/dea/dea-data-and-products/dea-hotspots)
- [DEA Hotspots technical product page](https://knowledge.dea.ga.gov.au/data/product/dea-hotspots/)

These resources were provided by Dr Arnick after the initial scope clarification and should be treated as core operational context for the next review iteration.

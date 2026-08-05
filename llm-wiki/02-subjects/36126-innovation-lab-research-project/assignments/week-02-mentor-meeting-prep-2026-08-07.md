# Week 2 Mentor Meeting Prep — Friday 7 August 2026

**Purpose:** Confirm the redirected project scope with Dr Arnick, get his decisions on the open questions below, and leave with a frozen methodology to start building against.

## 1. Recap since the 3 August brief

- Sent the consolidated findings brief (literature position + a public-data feasibility pilot on DEA Hotspots vs NSW fire-boundary references).
- Extended the pilot to a licensed, redistributable reference (NPWS Fire History), and built it into a reproducible, publicly reviewable Kaggle notebook pair (EDA + reliability-matching pilot), now public: [dataset](https://www.kaggle.com/datasets/tuannm3812/nsw-active-fire-pilot-snapshot), [notebook](https://www.kaggle.com/code/tuannm3812/nsw-active-fire-reliability-pilot).
- Key finding from that work: neither a narrow, incident-level fire reference (NSW RFS) nor a broad, whole-of-season complex-level reference (NPWS) currently supports clean point-in-time or event-level reliability testing of satellite hotspots — the narrow one under-covers true fire extent, the broad one over-matches because two mega-complexes (Kerry Ridge, Gospers Mountain) dominate the region and swallow ~98% of matches on their own.

## 2. What Arnick's reply changed

His 5 August reply made clear the reliability-auditing work is groundwork, not the final contribution. Restating the actual target back to him, to confirm we understood correctly:

1. Build a confidence-filtered MODIS FIRMS hotspot time series (2000–2025), validated against NSW fire records, cross-sensor matching (VIIRS/Himawari), and independent burnt-area datasets.
2. Fuse it with auxiliary weather (rainfall, temperature, wind, humidity) and land-cover/vegetation-condition variables.
3. Train a multimodal spatiotemporal transformer with cross-attention fusion across modalities.
4. Predict — one of:
   - **(A)** fire-occurrence probability with uncertainty, explanation, and spatial probability maps, or
   - **(B)** 1–7 day hotspot forecasting/nowcasting with confidence.

**Decision made internally (D-012, pending his confirmation): Option B.** Reasoning to bring to the meeting: it directly extends the hotspot-time-series infrastructure already built this week rather than needing a different data unit; there's a directly comparable existing paper already in the literature matrix (`TS-SatFire`, which combines detection, daily monitoring, and next-day prediction in one time-series dataset) to build from rather than starting blank; its evaluation reuses the same reliability-audited data already being built, rather than needing a separately-defined "did a fire occur here" label with its own leakage risks; and it's closer to the originally supervisor-confirmed "detection and monitoring, not spread" scope from 29 July.

## 3. Proposed methodology outline (for discussion, not yet frozen)

Following the existing `research-execution-plan-2026.md` phase structure:

- **Data foundation:** MODIS FIRMS hotspot archive (2000–2025) for the case-study region → confidence-filter using the reliability-audit method already built (cross-sensor + reference-boundary matching, extended per §4 below) → three-class labels (confirmed event / unresolved / confirmed non-fire), not a forced binary.
- **Auxiliary data:** weather (rainfall, temperature, wind, humidity — candidate source: SILO or BOM), land-cover/vegetation condition (candidate source: DEA Land Cover, already referenced in earlier literature notes).
- **Model:** multimodal spatiotemporal transformer, cross-attention fusion across a hotspot-history branch, a weather branch, and a vegetation/land-cover branch, following the `TS-SatFire` task framing adapted to short-horizon forecasting.
- **Baselines:** logistic regression and tree-based models first, per the existing evaluation-design section of the execution plan, before the transformer.
- **Validation:** chronological splits, spatial/leave-region-out holdouts, and — new lesson from this week's work — split-complex holdouts, so a forecast isn't evaluated on the same mega-complex it was trained near.
- **Evaluation:** PR-AUC alongside ROC-AUC, calibration (Brier score, ECE), and threshold-dependent operational measures (precision/recall/false-alarm burden) — all already specified in the execution plan, unaffected by this pivot.

## 4. Open questions for Arnick

1. **Forecast horizon:** does he want a single fixed horizon (e.g. exactly 3 days) or a multi-horizon output across 1–7 days? Affects the model's output head design.
2. **Case-study region/subregion (G3, still open):** NSW confirmed broadly, but this week's pilot found that within NSW, two events dominate almost all signal in the Blue Mountains area — does he want a specific subregion, or a region deliberately chosen to avoid one or two mega-complexes dominating the training data?
3. **Auxiliary data source preference:** does he have a preferred/prepared weather or vegetation-condition dataset, or should we source SILO/BOM and DEA Land Cover independently?
4. **Burnt-area reference:** he linked the Digital Atlas of Australia's national "Bushfire Historical Extents" dataset (1899–2024, all jurisdictions except NT) — is this meant to replace or supplement the NSW-specific NPWS/RFS layers already in use for confidence validation?
5. **Compute:** any GPU/compute resources available beyond Kaggle's free tier, given a multi-decade, multimodal transformer is a meaningfully bigger training job than the pilot?
6. **Contribution framing (G6):** is the intended contribution the forecasting model itself, the calibrated-uncertainty/explanation layer on top of it, or both — useful to know how much of the semester should go to model iteration vs. trust/explanation analysis (Phase 6 of the execution plan).

## 5. What to show him in the meeting

- The public Kaggle notebook pair (now includes a short note on where this fits in the larger project, added ahead of this meeting).
- The reconciled reliability finding (17.1% vs 97.12%, and why).
- This document's proposed methodology outline, as a discussion starting point, not a finished plan.

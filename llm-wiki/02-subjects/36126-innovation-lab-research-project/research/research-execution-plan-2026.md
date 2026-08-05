# Transparent Fire-Hotspot Detection and Monitoring — Research Execution Plan

## Current working direction

Develop and evaluate a transparent model for fire-hotspot detection and active-fire monitoring using multi-source remote-sensing and environmental data. Fire-spread forecasting is explicitly outside the project scope. The project should produce decision-relevant explanations and calibrated uncertainty, not only detection metrics.

The literature review will be geographically broad and must include both Australian and international studies. The eventual model will use a bounded case-study region, potentially NSW or another demonstrably fire-prone Australian state or region.

## Provisional research question

> Can a transparent spatiotemporal model using multi-source remote-sensing and environmental data improve fire-hotspot detection and active-fire monitoring in a selected Australian case-study region while providing calibrated uncertainty and regionally meaningful explanations?

## Decision gates

| Gate | Decision | Evidence required |
|---|---|---|
| G1 — Task | Fire-hotspot detection and active-fire monitoring; exclude spread | **Resolved by supervisor** |
| G2 — Review scope | Australia plus other global regions | **Resolved by supervisor** |
| G3 — Modelling region | NSW or another fire-prone Australian state/region | Fire-proneness evidence, data coverage, compute cost |
| G4 — Monitoring definition | Near-real-time detection, temporal tracking, or short-horizon monitoring | Literature taxonomy, label design, operational meaning |
| G5 — Model | Transformer, graph model, or justified comparison | Literature gap, baselines, sample size, compute |
| G6 — Contribution | Method, validation, transparency, uncertainty, or combination | Novelty evidence and semester feasibility |

No advanced model should be selected before the modelling region and operational definition of monitoring are resolved.

## First research sprint: 29 July–1 August

### Output for Dr Arnick

A concise gap brief containing:

1. Defined literature-search protocol
2. Evidence matrix of approximately 15–25 relevant papers
3. Taxonomy separating hotspot detection and active-fire monitoring from occurrence prediction, susceptibility, spread, severity, and burned-area tasks
4. Three recurring limitations supported by citations
5. Two or three candidate gaps
6. A recommended direction and fallback direction
7. Questions requiring supervisor decisions

### Acceptance criteria

- Every claimed gap is supported by multiple papers or a recent review.
- “No research exists” is not claimed without a systematic search.
- Prediction-time features are distinguished from information unavailable at inference time.
- Spatial and temporal leakage risks are recorded.
- The proposed scope can be executed with public or supervisor-provided data.
- Ethics and confidentiality risks remain low.

## Week calendar

Weeks run Wednesday–Tuesday, starting from the 29 July topic-scoping meeting. New dated files in this subject use a `week-NN-description-YYYY-MM-DD.md` prefix so files sort and group by week; existing files aren't being retroactively renamed, this applies going forward only.

| Week | Dates | Notable |
|---|---|---|
| 1 | 29 Jul – 4 Aug 2026 | Topic scoping, first research sprint, gap brief |
| 2 | 5 Aug – 11 Aug 2026 | Reliability pilot, NPWS pivot, Kaggle pipeline, Arnick's D-011 direction correction, Friday 7 Aug mentor meeting |
| 3 | 12 Aug – 18 Aug 2026 | Planned: T-032 (Digital Atlas evaluation), start T-033 (FIRMS full-history + weather/land-cover sourcing) |
| 4 | 19 Aug – 25 Aug 2026 | Planned: extend confidence-filtering pipeline across full history, produce versioned analytical dataset (Phase 3 exit artefact) |
| 5 | 26 Aug – 1 Sep 2026 | Planned: Phase 4 baselines (logistic regression, tree-based) before the transformer |
| 6 | 2 Sep – 8 Sep 2026 | |
| 7 | 9 Sep – 15 Sep 2026 | |
| 8 | 16 Sep – 22 Sep 2026 | |
| 9 | 23 Sep – 29 Sep 2026 | |
| 10 | 30 Sep – 6 Oct 2026 | |
| 11 | 7 Oct – 13 Oct 2026 | |
| 12 | 14 Oct – 20 Oct 2026 | |

## Arnick's 5 August direction — requirement breakdown and near-term plan

Source: [`communications/arnick-message-2026-08-05-direction-correction.md`](../communications/arnick-message-2026-08-05-direction-correction.md) (verbatim). This supersedes the "First research sprint" framing above as the operative plan — recorded here as the working breakdown of what he actually asked for, mapped onto concrete next steps.

### What he asked for, broken down

| # | Requirement (his words) | Status | Owning task |
|---|---|---|---|
| 1 | Reliability auditing is groundwork, "not about" the destination | Understood — reframed as Phase 1 data-quality gate | D-011 |
| 2 | Build MODIS FIRMS hotspot time series, 2000–2025 | **Not started** — biggest remaining task | T-033 |
| 3 | Confidence-filter it via NSW fire records, cross-sensor matching (VIIRS/Himawari), or burnt-area datasets (named the Digital Atlas link explicitly) | Method already exists (reliability-audit pipeline, T-004/T-009) but only covers a Jan 2020 pilot window against 2 references — needs extending to full history + the named Digital Atlas reference | T-032 (Digital Atlas), T-033 (full-history extension) |
| 4 | Fuse in auxiliary weather (rainfall, temperature, wind, humidity) and land-cover/vegetation-condition data, per hotspot location/record | Sources not yet chosen (SILO/BOM, DEA Land Cover are candidates) — open question for Friday | T-033 |
| 5 | Multimodal spatiotemporal transformer, cross-attention fusion across MODIS/weather/vegetation branches | Architecture template already worked out from literature (TS-SatFire task framing, FireSenseNet's cross-attention gate design) | T-031 (done, first pass), design section below |
| 6 | Pick **one** prediction target: (A) occurrence probability + explanation + spatial maps, or (B) 1–7 day forecasting/nowcasting | **Resolved — Option B** | D-012 |
| 7 | "check work pipeline... how to add innovation... how each process can be done" | First pass done; full-text verification in progress; formal Scopus/WoS pass still owed | T-031, T-038 |
| 8 | "cannot add more complexity" — explicit scope constraint | Governs every choice below: no extra modalities beyond weather + land cover/vegetation, no pursuing both A and B, no architecture beyond what's needed to fuse three branches | Applies throughout |

### Near-term plan (Weeks 2–5)

Ordered against the [Week calendar](#week-calendar) above, and against `Recommended minimum viable design for Option B` in [the literature scan](week-02-forecasting-literature-scan-2026-08-06.md), which already answers requirement 5 in detail — this section sequences requirements 2–4 (data foundation) and 6–7 (protocol), which the scan doesn't cover.

1. **Week 2 (through 7 Aug):** Friday meeting — resolve the open questions blocking everything below: exact case-study region/subregion (G3), fixed vs. multi-horizon output, weather/vegetation source preference, whether the Digital Atlas layer replaces or supplements NPWS/NSW RFS, compute availability, and contribution framing (G6). Full list in the [meeting-prep doc](../assignments/week-02-mentor-meeting-prep-2026-08-07.md).
2. **Week 3 (12–18 Aug):** T-032 (evaluate the Digital Atlas burnt-area dataset as a confidence-validation reference) and start T-033 (source full FIRMS 2000–2025 history plus weather and land-cover data) for the region confirmed on Friday.
3. **Week 4 (19–25 Aug):** Extend the confidence-filtering pipeline (T-009's method) across the full time range and the confirmed reference set; produce the versioned, three-class-labelled analytical dataset — Phase 3's exit artefact.
4. **Week 5 (26 Aug–1 Sep):** Phase 4 baselines (logistic regression, tree-based) on the frozen protocol, before touching the transformer — per the existing risk control against "deep model adds no value" going untested.
5. **Week 6 onward:** Phase 5 (transformer + cross-attention build) using the design already specified in the literature scan; not detailed further here until Phase 3/4 are actually done — premature to plan further given G3/G4/G5 aren't all frozen yet.

This isn't a new decision — it's D-011/D-012 turned into a sequence, so "what's next" doesn't require re-deriving it from the raw message each time.

## Semester phases

| Phase | Purpose | Exit artefact |
|---|---|---|
| 1. Discovery | Establish task, literature gap, and data feasibility | Gap brief and supervisor-approved direction |
| 2. Protocol | Freeze target, horizon, splits, metrics, and hypotheses | Research protocol |
| 3. Data foundation | Acquire, harmonise, and audit sources | Versioned analytical dataset and data card |
| 4. Baselines | Establish honest reference performance | Logistic regression and tree-based baselines |
| 5. Advanced model | Test one primary modelling contribution | Transformer or graph pipeline |
| 6. Trust analysis | Evaluate explanation stability, calibration, and uncertainty | Reliability and interpretation report |
| 7. Robustness | Test future periods, unseen regions, and ablations | Robustness evidence |
| 8. Writing | Produce the report and face-to-face presentation | Final paper, repository, and slides |

## Proposed evaluation design

- Use chronological splits; never randomly mix future observations into training.
- Add spatial holdouts or leave-region-out evaluation.
- Compare against simple, strong baselines before deep learning.
- Report class imbalance and use PR-AUC alongside ROC-AUC.
- Include calibration metrics such as Brier score and expected calibration error.
- Report threshold-dependent operational measures, including recall, precision, and false-alarm burden.
- Test explanation stability across folds, periods, and regions.
- Add ablations for fire history, weather, climate, vegetation, land use, and spatial context.
- Record compute cost and reproducibility information.

## Risk controls

| Risk | Control |
|---|---|
| Topic becomes too broad | Fix one target, horizon, spatial unit, and advanced model |
| Data engineering consumes semester | Begin with one region or analysis-ready public products |
| Rare-event imbalance | Use suitable sampling, PR metrics, calibrated probabilities, and threshold analysis |
| Spatial/temporal leakage | Define splits before feature construction and audit feature timestamps |
| Deep model adds no value | Treat a rigorous negative result as evidence; retain strong baselines |
| Explanations are superficial | Test stability and connect drivers to domain literature |
| GPU limitations | Prototype locally on samples; train bounded experiments on Kaggle or Colab |
| Unclear originality | Maintain a claim-to-evidence gap table and review it with Dr Arnick |

## Supervision rhythm

- Use a short weekly written update: completed, evidence, blockers, next decisions.
- Schedule approximately one hour per week where possible to satisfy and document the expected 12 contact hours.
- Send artefacts before meetings so supervision time is used for decisions.
- Keep a dated decision log, including changes to scope and research questions.

## Questions to resolve through the findings

1. Which Australian state or region has the strongest combination of fire-proneness, data readiness, and manageable scale?
2. In the closest literature, does “active-fire monitoring” mean contemporaneous satellite detection, temporal tracking, or short-horizon forecasting?
3. What spatial and temporal units are operationally meaningful for the selected case study?
4. Which gap most strongly supports graph structure, temporal modelling, data fusion, or trustworthy detection?
5. Which existing dataset or baseline does Dr Arnick recommend after reviewing the findings?

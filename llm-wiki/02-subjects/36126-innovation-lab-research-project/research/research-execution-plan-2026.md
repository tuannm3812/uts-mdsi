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
| 3 | 12 Aug – 18 Aug 2026 | |
| 4 | 19 Aug – 25 Aug 2026 | |
| 5 | 26 Aug – 1 Sep 2026 | |
| 6 | 2 Sep – 8 Sep 2026 | |
| 7 | 9 Sep – 15 Sep 2026 | |
| 8 | 16 Sep – 22 Sep 2026 | |
| 9 | 23 Sep – 29 Sep 2026 | |
| 10 | 30 Sep – 6 Oct 2026 | |
| 11 | 7 Oct – 13 Oct 2026 | |
| 12 | 14 Oct – 20 Oct 2026 | |

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

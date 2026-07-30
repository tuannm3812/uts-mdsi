# Preliminary Seed Literature — 29 July 2026

This is a discovery list, not yet a completed literature review. Claims and bibliographic metadata must be checked against full texts before inclusion in the gap brief.

## Closest methodological work

1. [Explainable global wildfire prediction model using graph neural networks](https://doi.org/10.1016/j.geoai.2026.100052) — graph-based sequence learning for global burned-area forecasts with a correlation-defined climate-fire graph. This means “graph modelling for wildfire” is not itself a gap.
2. [Causal Graph Neural Networks for robust wildfire forecasting across geographic shifts](https://doi.org/10.1016/j.isprsjprs.2026.03.018) — directly relevant to geographic generalisation, causal structure, and explanations. This is likely a central comparator for any graph proposal.
3. [Time Series Forest Fire Prediction Based on Improved Transformer](https://doi.org/10.3390/f14081596) — transformer-based forest-fire prediction from time-series environmental factors. This means “using a transformer” is not sufficient originality.
4. [Spatio-Temporal Wildfire Prediction using Multi-Modal Data](https://arxiv.org/abs/2207.13250) — separates real-time fire-risk prediction from magnitude prediction sets and uses time-series conformal prediction. Relevant to uncertainty and multi-source data.
5. [XGBoost meets INLA: a two-stage spatio-temporal forecasting of wildfires in Portugal](https://arxiv.org/abs/2508.09896) — probabilistic one-month-ahead fire-count and burned-area forecasting. Relevant as a strong non-neural spatiotemporal comparator.

## Reviews and transparency

6. [A comprehensive survey of the machine learning pipeline for wildfire risk prediction and assessment](https://doi.org/10.1016/j.ecoinf.2025.103325) — recent pipeline-level review highlighting data integration, generalisation, interpretability, and uncertainty.
7. [Recent advances in explainable Machine Learning models for wildfire prediction](https://doi.org/10.1016/j.acags.2025.100266) — combines model optimisation and SHAP on public wildfire datasets. Useful for assessing whether explanation practice goes beyond standard SHAP plots.
8. [Deep fire topology: Understanding the role of landscape spatial patterns in wildfire occurrence using artificial intelligence](https://doi.org/10.1016/j.envsoft.2021.105167) — relevant to landscape topology, occurrence prediction, interpretation, and uncertainty.

## Preliminary observations to test

- The method labels “transformer,” “GNN,” “data fusion,” and “SHAP” are already represented in the literature.
- A stronger contribution may lie in the combination of multi-source active-fire monitoring, rigorous spatiotemporal validation, calibrated uncertainty, and stable regional explanations for an Australian case-study region.
- Task definition matters: active-fire detection, future occurrence, susceptibility, spread, and burned-area forecasting are scientifically different.
- Recent 2026 work raises the novelty threshold for a generic graph-based proposal.

## Supervisor-confirmed scope

- Primary task: fire-hotspot detection and active-fire monitoring
- Excluded task: fire-spread forecasting
- Review geography: Australia plus other regions globally
- Modelling geography: one manageable Australian state or fire-prone region, potentially NSW

These are hypotheses for the systematic scan, not final gap claims.

## Candidate data anchors

- [NASA FIRMS active-fire data](https://firms.modaps.eosdis.nasa.gov/active_fire) provides MODIS and VIIRS products; scientific analysis should use the standard science-quality archive rather than only near-real-time feeds.
- [Digital Earth Australia Land Cover](https://knowledge.dea.ga.gov.au/data/product/dea-land-cover-landsat/) provides nationally consistent annual land-cover information suitable for evaluating land-cover drivers in an Australian study.

# Week 2 Mentor Meeting Prep — Friday 7 August 2026, 12:00pm (Teams)

**Purpose:** Confirm the redirected project scope with Dr Arnick, get his decisions on the open questions below, and leave with a frozen methodology to start building against.

**Time confirmed by Arnick, 2026-08-05** ([verbatim](../communications/from-arnick-2026-08-05-direction-correction.md)): Friday 7 August, 12pm, to discuss "your review and findings as well this one I shared" — i.e. the reliability-audit work below and (likely) the Bushfire Historical Extents dataset in open question 4.

**Backing detail:** [`research/week-02-forecasting-literature-scan-2026-08-06.md`](../research/week-02-forecasting-literature-scan-2026-08-06.md) has the full evidence table and reasoning behind §3's methodology outline — bring it along in case Arnick wants the detail.

**Speaking notes:** [`week-02-meeting-presentation-script-2026-08-07.md`](week-02-meeting-presentation-script-2026-08-07.md) turns this doc into talking points organised by meeting flow, with his own words quoted before each ask. **Live tick-sheet:** [`week-02-decision-checklist-2026-08-07.md`](week-02-decision-checklist-2026-08-07.md) — one page per decision with concrete options to mark as he answers. All materials (this doc, the script, the checklist, the literature scan, the Digital Atlas evaluation, the traceability check, and both Kaggle notebooks) are exported as PDF in the Drive folder `02 Supervision/Dr Arnick/01 Preparation/2026-08-07 Week 2 Meeting/`.

**Traceability check:** [`research/arnick-message-traceability-2026-08-07.md`](../research/arnick-message-traceability-2026-08-07.md) maps every clause of his 5 August message to an action, to make sure nothing got missed. It surfaced one real gap not caught before — see open question 7 below.

**Send the Kaggle notebook before the meeting (T-039), not just live in it.** Arnick has never actually been sent the link — the 3 August brief predates it going public (D-010, 5 Aug) — and the execution plan's own supervision-rhythm guidance says to send artefacts ahead so meeting time goes to decisions, not first reactions. Suggested Teams invite description:

> Discussion of the redirected research direction (reliability audit as Phase 1, multimodal forecasting as the target) and next steps.
>
> Reference material, happy for you to look before Friday if useful, otherwise I'll walk through it live:
> - Public Kaggle dataset: https://www.kaggle.com/datasets/tuannm3812/nsw-active-fire-pilot-snapshot
> - EDA notebook: https://www.kaggle.com/code/tuannm3812/nsw-active-fire-eda
> - Reliability-matching notebook: https://www.kaggle.com/code/tuannm3812/nsw-active-fire-reliability-pilot
>
> Agenda: recap of the reliability-audit finding, confirming the forecasting direction (1–7 day hotspot prediction), and a few open questions on region, data sources, and compute.

## 1. Recap since the 3 August brief

- Sent the consolidated findings brief (literature position + a public-data feasibility pilot on DEA Hotspots vs NSW fire-boundary references).
- Extended the pilot to a licensed, redistributable reference (NPWS Fire History), and built it into a reproducible, publicly reviewable Kaggle pipeline — a dataset plus two separate notebooks: [dataset](https://www.kaggle.com/datasets/tuannm3812/nsw-active-fire-pilot-snapshot), [EDA notebook](https://www.kaggle.com/code/tuannm3812/nsw-active-fire-eda), [reliability-matching notebook](https://www.kaggle.com/code/tuannm3812/nsw-active-fire-reliability-pilot).
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

## 4. Open questions for Arnick — with our recommendation

Each framed as a proposal to confirm or correct, not a blank question — faster to resolve in a 30–45 minute meeting.

1. **Forecast horizon.** *Our recommendation:* multi-horizon output across 1–7 days, not a single fixed day — matches his own framing ("this can change based on final data and possibility of the model"), and the literature scan found aleatoric uncertainty grows measurably with horizon (Uncertainty-Aware DL paper, arXiv 2509.25017), which is worth showing explicitly rather than collapsing to one number.
2. **Case-study region/subregion (G3, still open).** *Our recommendation:* don't restrict to the exact Greater Blue Mountains pilot footprint — two events (Kerry Ridge, Gospers Mountain) dominate ~98% of matches there, too few independent events for split-complex validation. Either widen to all of NSW, or pick a fire-prone NSW subregion with more distinct, comparably-sized fire events. Ask him directly whether he has a preferred subregion or defers to us on this.
3. **Auxiliary data source preference.** *Our recommendation:* SILO (Queensland Government "Long Paddock" gridded daily climate data, free API, coverage from 1889 — matches the FIRMS 2000–2025 window with no gaps) for weather, and DEA Land Cover for vegetation/land-cover — both free, Australian-government-maintained, and DEA is already the operational baseline Arnick pointed to on 29 July. Proceed with these unless he has a preferred/prepared dataset already.
4. **Burnt-area reference — the Digital Atlas "Bushfire Historical Extents" dataset he linked.** *New finding (T-032, done ahead of this meeting):* it's CC BY 4.0 licensed (no blocker), but its NSW-portion lineage traces to New South Wales Parks and Wildlife — the same agency behind NPWS Fire History, already in use. It's very likely the same underlying NSW source re-aggregated nationally, not an independent reference that would fix the mega-complex-dominance problem. *Our recommendation:* treat it as supplementary (useful for cross-jurisdictional coverage if the region ever spans a state border), not a replacement for NPWS/RFS — full detail in [`research/digital-atlas-bushfire-extents-evaluation-2026-08-06.md`](../research/digital-atlas-bushfire-extents-evaluation-2026-08-06.md). Worth confirming with him directly since he raised it, rather than just assuming.
5. **Compute.** *Our recommendation:* default to Kaggle's free tier (P100/T4, ~30 GPU-hours/week) for prototyping and baselines; only escalate if the full 2000–2025 multimodal training run proves infeasible there. Ask whether UTS-provided compute or Colab Pro/GCP credits exist as a fallback, so we know before we hit the wall rather than after.
6. **Contribution framing (G6).** *Our recommendation:* frame it as "reliability-aware forecasting," not just "a forecasting model" — the label-confidence-aware training/uncertainty design (propagating Phase 1's confirmed/unresolved/non-fire pipeline into the model, rather than treating labels as clean ground truth like every UQ paper found does) and the split-complex validation discipline (now backed by three independent literature findings, not just our own pilot) are both genuine, defensible contributions in their own right — not just scaffolding around the transformer. Worth stating this explicitly so semester time isn't allocated as if the model architecture were the only thing that counts.
7. **Cross-sensor matching (his own words: "corss-sesnor matching and validation like with other sensor like VIIRS or Himawari") — found via the traceability check, not previously flagged.** Everything built so far validates hotspots against *fire-boundary references* (NSW RFS, NPWS); it's never checked whether MODIS and VIIRS/Himawari *agree with each other* at the same place and time, which is a genuinely separate confidence signal from boundary-matching. *Our recommendation:* fold this explicitly into the T-033 data-foundation scope as its own step, rather than letting it stay silently unaddressed — worth naming directly so it's a planned task, not an accidental gap.

## 5. What to show him in the meeting

- The public Kaggle notebook pair (now includes a short note on where this fits in the larger project, added ahead of this meeting).
- The reconciled reliability finding (17.1% vs 97.12%, and why).
- This document's proposed methodology outline, as a discussion starting point, not a finished plan.
- The Digital Atlas dataset evaluation (T-032, question 4 above) — a direct answer to something he explicitly asked us to check.
- The evaluation-inflation finding from the literature scan (F1 ranging 36–97% on the identical benchmark dataset across papers) — strengthens the case for treating split-complex validation as a real contribution, not overkill.

## 6. Analysis, workings, and findings behind this plan

Everything above rests on work already done and verifiable, not assumptions:

- **Reliability pipeline (T-004/T-009, D-005–D-007):** built and run twice, against NSW RFS (narrow, incident-level — 17.1% match rate) and NPWS Fire History (broad, complex-level — 97.12%). Root-caused the gap to reference-polygon scale, not sensor performance — both results point the same direction: neither granularity alone supports point-in-time reliability testing.
- **Literature scan (T-031, first pass done; T-038, 3 of 3 previously-blocked full texts now read in full):** 11+ papers, 2022–2026. Closest direct comparator identified (`TS-SatFire`); concrete architecture template found (FireSenseNet's cross-attention gate, 7.1% F1 gain over concatenation); concrete explainability template found (Dubey & Dubey's Mamdani fuzzy rule-based system, fully worked). Full detail in [`research/week-02-forecasting-literature-scan-2026-08-06.md`](../research/week-02-forecasting-literature-scan-2026-08-06.md).
- **Evaluation-inflation risk — independently confirmed three separate ways** in that literature (FireSenseNet's own 44% inflation claim; a 60-point F1 spread across papers on the identical "Next Day Wildfire Spread" benchmark; a specific paper's 92.9% F1 looking inflated against its own cited base method's 64–68%). This isn't a hypothetical risk — it's the same failure mode this project already found empirically (mega-complex dominance), now backed by external evidence.
- **T-032 (Digital Atlas evaluation, done today):** license and lineage checked — CC BY 4.0, but NSW portion likely traces to the same NPWS source already in use. See dedicated finding above.
- **Data-foundation gap (T-033, not started):** the honest state of the actual next step — sourcing the full FIRMS 2000–2025 history plus weather/land-cover data hasn't begun. Flagged explicitly rather than implied as further along than it is; sequencing for this is in [`research/research-execution-plan-2026.md`](../research/research-execution-plan-2026.md)'s "Arnick's 5 August direction" section (Weeks 3–5).

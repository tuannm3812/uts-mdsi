# Speaking Script — Friday 7 August Meeting with Dr Arnick

Talking points, not a script to read verbatim — say it in your own words. Built from [`week-02-mentor-meeting-prep-2026-08-07.md`](week-02-mentor-meeting-prep-2026-08-07.md); full evidence and reasoning are there and in the linked backing docs if he wants to go deeper than these notes.

**His actual words are woven in below** (marked *"His words"*) — reading his own phrasing back to him before each recommendation is a fast, low-friction way to confirm you understood him, and makes it obvious every ask is grounded in something he actually said, not assumed. Full source: [`communications/from-arnick-2026-08-05-direction-correction.md`](../communications/from-arnick-2026-08-05-direction-correction.md) and [`communications/from-arnick-2026-07-29-scope-clarification.md`](../communications/from-arnick-2026-07-29-scope-clarification.md).

**Target length:** 30–45 minutes. Seven decisions needed by the end (Section 4 below) — that's the actual goal of the meeting, everything else is context to get there efficiently. A companion tick-sheet ([`week-02-decision-checklist-2026-08-07.md`](week-02-decision-checklist-2026-08-07.md), exported as PDF) has the options for each decision to mark live during the call.

---

## 0. Open (30 seconds)

> "Thanks for making time. Quick structure for today: I'll recap what's changed since the 3 August brief, confirm I understood your redirect correctly, show you the public notebooks quickly, then I've got seven things I'd like your decision on so I can start building next week. Should take 30–40 minutes."

---

## 1. Recap since 3 August (2 minutes)

> "Since the brief, I extended the reliability pilot to use NPWS Fire History instead of NSW RFS, since RFS's license wasn't actually confirmed for redistribution. That let me publish the whole thing as a reproducible public Kaggle pipeline — I'll show you in a second."

**Key finding to state plainly:**

> "The headline result: neither reference is actually good enough on its own. NSW RFS — narrow, incident-level records — only matched 17.1% of hotspots even with sensor-buffering. NPWS — broad, whole-of-season fire-complex boundaries — matched 97.12%. That jump isn't sensor improvement, it's scale. Two mega-complexes, Kerry Ridge and Gospers Mountain, account for about 98% of every match in NPWS. So the real lesson isn't 'NPWS is better,' it's that reference-data granularity dominates the result more than anything about the sensors themselves."

*(This is the finding likely to prompt the most discussion — give it room, don't rush past it.)*

---

## 2. Confirm the redirect (2 minutes)

**His words (5 Aug):** *"But this project is not about the reliability auditing of those existing platforms and methodology for hotspot monitoring."* ... *"what I was thinking is that, we get hotspot datasets like time series of fire hotspots from sensors like MODIS (FIRMS)... create a dataset of all fire hotspots timeseries from for example 2000-25 for training the model."* ... *"then build multimodal spatiotemporal transformer (time series model) with different modalities coming from MODIS, weather, vegetation/land cover etc and cross-attention for fusion."*

**Say:**
> "I want to make sure I understood your reply correctly before I show you anything else. You said the reliability audit isn't the project — it's groundwork. The actual target, in your words, is a MODIS FIRMS hotspot time series from 2000 to 2025, checked for confidence, fused with weather and land-cover data, feeding a multimodal spatiotemporal transformer with cross-attention. And you wanted one prediction output, not both — either occurrence probability with explanation, or 1-to-7-day forecasting. Is that a fair summary?"

*(Pause for confirmation before moving on — this is the foundation everything else sits on.)*

---

## 3. Show the notebooks (3–5 minutes, screen share)

Open both links (already sent ahead via Teams):
- EDA notebook: https://www.kaggle.com/code/tuannm3812/nsw-active-fire-eda
- Reliability-matching notebook: https://www.kaggle.com/code/tuannm3812/nsw-active-fire-reliability-pilot

**Walk through in this order:**
1. EDA notebook, Section 5 ("Key EDA Takeaways") — the area-skewness table, point at Gospers Mountain/Kerry Ridge dominance.
2. Reliability notebook, Section 3 ("Results") — the 77.25%/97.12% headline numbers.
3. Reliability notebook, Section 4 ("Event Concentration") — the bar chart, ~98% concentration in two events.
4. Reliability notebook, end — "Project Context and Roadmap" note, ties this pilot explicitly to the forecasting direction.

> "Both notebooks are public and reproducible — dataset plus two separate kernels, so either one can be re-run independently on Kaggle's free tier."

---

## 4. The seven decisions (20–25 minutes — the core of the meeting)

Frame each one as "here's what we'd recommend, does that work or would you adjust it" — not an open question. Faster to resolve, and shows the thinking isn't starting from zero. Tick the chosen option on the [decision checklist](week-02-decision-checklist-2026-08-07.md) PDF as he answers each one.

### 4.1 Forecast horizon
**His words (5 Aug):** *"prediction hotspots with showing confidence and uncertainty level based on those time series auxiliary data for next for example 1-7 days ahead (this can change based on final data and possibility of the model)."*

**Say:**
> "You said 1-to-7 days, with room to change based on the data. We'd recommend keeping it as a multi-horizon output across the full range, rather than one fixed day — the literature we found shows uncertainty grows measurably with horizon, worth showing explicitly. Does that work?"

### 4.2 Case-study region
**His words (29 Jul):** *"you can select a specific study region - for example, a state in Australia such as NSW - to build and analyse your model... You could also look at which regions or states in Australia are more fire-prone and use one of those as your case study."*

**Say:**
> "Back on 29 July you said NSW broadly, or a fire-prone subregion within it. This week's pilot found a real reason to be careful about which subregion: if we stay in the exact Blue Mountains pilot footprint, two events dominate everything and we can't validate properly. We'd recommend either widening to all of NSW, or a different fire-prone subregion with more distinct events. Do you have a preference, or should we choose based on where the data actually supports proper validation?"

### 4.3 Auxiliary data sources
**His words (5 Aug):** *"auxiliary data to this with additional variables like weather (rainfall, temperature, wind, humidity, etc), land cover and vegetation condition, etc. for each hotspot location and records."*

**Say:**
> "For weather, we'd use SILO — free, gridded, daily, goes back to 1889, covers the full FIRMS window with no gaps. For land cover, DEA Land Cover — same agency as DEA Hotspots, which you already pointed us to. Unless you've got a preferred or prepared dataset, we'd start there."

*(If asked about wind: SILO doesn't have it — confirmed directly against their variable list. Flag this honestly: "wind will need a different source, BOM or ERA5, we haven't sourced it yet.")*

### 4.4 The Digital Atlas dataset
**His words (5 Aug):** *"or burned datasets like (https://digital.atlas.gov.au/datasets/524e2962bd8b4968b8df9f9774345926/about)."*

**Say:**
> "You linked the Digital Atlas 'Bushfire Historical Extents' dataset — we checked it. CC BY 4.0, no licensing issue. But its NSW records trace back to the same NSW Parks and Wildlife source as NPWS, which we're already using — so it's very likely the same underlying data re-aggregated nationally, not an independent check. We'd treat it as useful mainly if the region ever crosses a state border. Does that match what you had in mind for it?"

### 4.5 Compute
No specific line from him on this — genuinely open, not grounded in a quote.

**Say:**
> "We'll default to Kaggle's free tier for prototyping and baselines. If the full 2000-to-2025 multimodal training run needs more than that, is there UTS compute or cloud credits available as a fallback? Better to know now than mid-semester."

### 4.6 Contribution framing
**His words (5 Aug):** *"check work pipeline and do a bit of search how this looks like and how to add innovation to this and then see how to build methodology, data and models."* ... *"Because of timeframe of the research subject, can not add more complexity to the project."*

**Say:**
> "You asked us to find where the innovation actually is, within a tight timeframe. Our recommendation is 'reliability-aware forecasting' — propagating the label-confidence work from Phase 1 into the model's own uncertainty estimate, plus split-complex validation, now backed by three independent literature findings. We think that's a real contribution in its own right, not just scaffolding around the transformer, and it doesn't add complexity — it reuses what's already built. Does that framing work for how you want the semester allocated?"

### 4.7 Cross-sensor matching — a gap we found going back through your message
**His words (5 Aug):** *"this can be done based on your review through fire records from NSW for exmaple, or corss-sesnor matching and validation like with other sensor like VIIRS or Himawari, or burned datasets like..."*

**Say:**
> "One more thing, going back through your message carefully — you named cross-sensor matching with VIIRS or Himawari as one of three confidence-filtering methods. We've done the other two — NSW fire-record matching and the Digital Atlas check — but cross-sensor agreement itself, checking whether MODIS and VIIRS actually agree with each other at the same place and time, hasn't been done as its own step yet. We'd fold it into the data-foundation work as an explicit task. Wanted to flag it directly rather than let it quietly slip."

---

## 5. Close (1 minute)

> "So to confirm what I'm taking away: [restate his answers to the seven items above]. I'll start on the data-sourcing work next week — full FIRMS history plus weather and land-cover for the confirmed region — and send a short written update once that's underway."

---

## If he asks something not covered above

- **"Why not just use NSW RFS since it's more precise?"** → License was never confirmed for redistribution (D-005) — that's the actual reason for the NPWS switch, not a preference.
- **"How confident are you in the 97.12% number?"** → Verified independently multiple times this session, including re-deriving the event-level breakdown directly from the matching code against the raw data, not just reading it off the notebook.
- **"What's actually done vs. not started?"** → Be direct: Phase 1 (reliability audit) is done and published. Phase 3 (the actual multi-decade data foundation, T-033) has **not** started — flag this honestly rather than implying more progress than exists.

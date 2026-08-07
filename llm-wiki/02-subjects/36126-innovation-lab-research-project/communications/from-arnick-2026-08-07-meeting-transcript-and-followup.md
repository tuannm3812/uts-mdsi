# Dr Arnick — Meeting Transcript (Full) and Post-Meeting Messages, 7 August 2026

**Status:** Full transcript now available (Tuan downloaded `Research Update.vtt`/`.docx` from Teams, 2026-08-07) — supersedes the earlier partial version of this file, which only had the opening (0:00–10:07) and closing (51:38–54:40) with a ~40-minute gap. Two rounds of post-meeting Teams messages also recorded below. This is the source for D-014.

## Transcript — organised by topic (verbatim exchanges, connection/small-talk filler trimmed)

### Opening recap (7:55–11:17)
Tuan recaps the reliability pilot: NSW RFS ~17% match rate, NPWS ~97%, explained by Kerry Ridge/Gospers Mountain dominating ~98% of NPWS matches. Restates his understanding of the 5 August redirect back to Arnick (MODIS FIRMS 2000-25, confidence-filtered, fused with weather/land-cover, multimodal transformer, one prediction output — occurrence probability or 1-7 day forecast).

> Arnick Abdollahi (11:17): "Yeah, but let's, yeah, we'll discuss that. Yeah, that's the first thing that you did that was like a great effort. Amazing. Thank you for that."

### Notebook walkthrough (11:44–22:38)
Arnick reviews the Kaggle notebook live — DEA hotspot schema, NPWS fire-boundary schema (14 entries: fire ID, ignition date, area, perimeter), how the confidence matching was done. Confirms methodology understanding, asks Tuan to add a reference for the matching formula/methodology used.

### The core redirection — why not time series (23:13–37:35)

> Arnick Abdollahi: "If you want to build a... machine learning, because this is for, I think, for like a specific fire, right? Like a 2019 and 20, right? That's 2 years. Not like a time series, right? Is that correct, or?"
>
> Manh Tuan Nguyen: "Yes, we only match the incident... from like 2019 and 20, not the other years."
>
> Arnick Abdollahi: "One thing, because this is for this year only, you can put your focus on this year, because... that this year actually we had like a big fire, right? And then you can build your methodology around... that situation and that kind of scenario, right? For example, what would be your understanding and impact of your research for 2019 and 2020 bushfire? That is like a called Black Summer, right? Instead of just moving to like other fires in different years or something, you can select this as a study because it's like a reference, right? Because it was like a big fire happened for Australia and it's evident. So you can do research on that, right, and build your methodology, whatever we want to do for next step, you can do on these types of fire, and then see what we can actually understand from that fire, or what we can add to that kind of right, what kind of insight we can have..."
>
> Arnick Abdollahi: "You selected here, this is a very good foundation that you actually find this kind of matching and reliability auditing and then you extract that like a hottest spot with this high level of confidence. What is the confidence in here? ... Total hot spot, you have like 15,000... like a sample record, right? This is your final record, right? Then you can actually use these as your data set, like because you have 15,000 record and it's good enough for training the model, isn't it?"
>
> Manh Tuan Nguyen: "Yep, the time series prediction, right? With the horizon."
>
> Arnick Abdollahi: "But the problem here is that you cannot apply that, because you have like a limited time frame, like just two years. For time series prediction, at least you must have like maybe 20, 30 years of data. So imagine that for weather. Weather prediction, so we usually use like maybe 40-50 year data. Long historical data set, we cannot build like a time series model for just one year, two years data, so that's why you have to shift your time series prediction to something else, like the goal of the project change if you want to use this data set. So, but if you want to go to time series data set, then you need to use like another set of data set that has like a time series. For example, different area, maybe 10 years, 20 years of the data you have to have, right? And then do that prediction analysis. So, but both types are OK, are fine, but which one you are most interested to do, and you think?"

Tuan raises the region-concentration concern:

> Manh Tuan Nguyen: "...if we focus only on New South Wales regions, there's only two big [fires]. So they maybe the models will be a bit overfit because that's two big fires. If we choose another regions, do you have any preference? Or any direction for choosing another regions, or do we have any reliable data set right now?"
>
> Arnick Abdollahi: "Yeah, there are like a hottest spot data set, as I mentioned, for example, MODIS had like a time series hottest spot and active fire that you can use for it is global data set. But it need to be checked at how much actually reliable that hot spot are, because that sensor pick up every hot spot, and that does not mean that 100% is fire, right? ... If you want, but it's OK, we can do some kind of stuff there if you want to do time series analysis."

Arnick then walks through what a genuine time-series path would need (a longer-history global hotspot dataset, e.g. via Google Earth Engine, "from 2000 to this current date") and what it would enable (a proper multimodal spatiotemporal transformer with cross-attention) — but immediately contrasts it with the small-data path:

> Arnick Abdollahi: "But for this data, because we don't have that time series... we cannot go to time series models, like transformer or whatever, but still we can have the multimodal. For example, multimodal deep learning model, because you would have like a different modality, for example, weather modality, land cover modality, or I don't know, whatever other you have, and then you can build on top of that to see how they work."

**The decision:**

> Arnick Abdollahi (36:44): "But if we want to move to that time series kind of thing, then the direction a little bit will be shifted... yeah, and then actually it makes sense to shift to that. We can work on this data set and move forward because we have limited time."
>
> Manh Tuan Nguyen: "I think I will try first, and... right now, so I think, okay, about the direction, I think that's fine."

(Tuan briefly floats doing both — "I can do both at the same time" — Arnick doesn't push back on this but doesn't commit resources to it either; the concrete, agreed-on primary path is the small-data multimodal model below.)

### Compute (37:36–38:45)

> Manh Tuan Nguyen: "...when I training models, actually now I still use [K]aggle. They offer 30 hours with GPU. I think that's okay. Should we have in the future if there's I need more GPU, can I use another? Compute Engine from [S]chool or something else. What do you think?"
>
> Arnick Abdollahi: "For this answer, I think it should be fine. Because you have just 15,000 records... maybe you don't need [all of them]... like 1000 or 5000 or something you need based on your region. You can just select those high level confidence of the hottest spot records... and then try to train your model and that should be enough. Even in a normal laptop it works because your region is not too [big/heavy]."

### Innovation / model mechanism (39:00–44:41)

> Manh Tuan Nguyen: "...we have a really tight time frame, so... what the innovation can we do for this project? I still wonder if you have suggested any idea."
>
> Arnick Abdollahi: "You need to put your innovation into the model... that actually developing a new model, for example... maybe when you develop a model, you can add like [a] mechanism within the model that could help to better predict the probability of fire. Know what I mean? Like attention mechanism or... sensor kind of mechanism or like a modality kind of mechanism into the system, into the model."
>
> Manh Tuan Nguyen: "Yeah, I understand. I think this one I will... do some research about that and I would do some experiment."
>
> Arnick Abdollahi: "No, I can suggest you to go with this because you have the data set ready. You just need to add your auxiliary data here, like weather or land cover or whatever, and then build your model and do a bit of analysis to see that how you can actually do the probability of the fire. And then, uh, we can discuss next. For the model, also, I'll search to see what kind of other innovation we can add to the model, and I'll share something new."

### Auxiliary data — sources and feature engineering (35:04–35:59, 45:00–48:52)

> Manh Tuan Nguyen: "...for the auxiliary data source, so actually now I have [SILO] to track the weather data, [it's] free and it can match with the full firms window we have right now... For silo, we don't have wind, and for the [land] cover, we can use the DA's land cover. They have the data set matched to the DA's hotspot."
>
> Arnick Abdollahi: "Yeah, you can use the silo or you can use the [other] data... In DA, if you check, you have land cover and also you have... different data set on fuel, for example, the moisture content — moisture, you can use that as well. I'll share some data set that you can use from there."

Arnick then gives concrete feature-engineering guidance on temporal aggregation of weather data:

> Arnick Abdollahi: "For the data set that you get, for example, for weather data... you need to check that you get [the] data set for the same date at fire, [or] a little bit of time before, for example, maybe three months, two months, three months, or six months back... you need to check the range of these fire dates, right, to see how the interval [is] distributed... maybe monthly data, or 10 days aggregation... see which one actually affects the prediction [most]. That's for the weather. For land cover, we usually don't have [frequent updates], because land cover is not something that is changed [often], and you may have like a just one year [of] data — just feed that to the model, that's okay. But for better, you can do a bit of engineering, like different aggregation, monthly, 10 days, maybe 15 days, and see which one actually affects the prediction [most]."
>
> Arnick Abdollahi: "...you have fired at this month, right? ... you can get the weather data at month [minus] 1, [minus] 3, [minus] 2, [minus] 6 months before, because the fire is not something that happened quickly. The condition of the weather has to be in that situation for a long time — two months, three months — of the hot weather, then it leads to fire. So that's why you need to have that lag."
>
> Arnick Abdollahi: "Wow, this is very cool... you can add this also into your paper."

### The paper/journal framing (48:54–52:26)

> Arnick Abdollahi: "...these are very good findings for the first [stage] that you did, right, and you can add to do your paper as well... For this work, if we actually do very good kind of stuff, I can also try like publishing the work in journal instead of [a lesser venue]... you can just check [a template paper] and see how you can actually format your paper. So, like abstract, then introduction and background, because this is the template... [then] related work — what actually kind of work has been done already and what are the limitation of those work and what actually you will bring as a new contribution, right, and new innovation to address those kind of limitations... and the research gaps that you find, the research problem/questions... the methodology that you have... the results, discussion, and conclusion at the end... this kind of things, so it's really actually a research paper kind of thing that you need to follow. But I believe this work would be good and we can even try journal, see what would be there. Final outcomes. So, I'm good."

### Close (52:34–53:18)

> Arnick Abdollahi: "Okay, you update the access to [the] side of data and then land cover for DA, and also we'll check that what other data set we can use or share the links from DA. You can add to your data set. Also, just remember to do a bit of search on the models, how to add more innovation into the model."
>
> Manh Tuan Nguyen: "Yeah, okay, I understand. I will share you... I will look at the data set and will share you the findings later."

[53:27–54:41: casual conversation — Tuan's location, capstone subject, no research-direction content.]

## Post-meeting message 1 (sent immediately after — full content recorded previously)

Shared his own 2023 paper (Abdollahi & Pradhan, XAI wildfire susceptibility, *Science of the Total Environment* — confirmed via Crossref), AlphaEarth/Satellite Embedding V1, Prithvi-EO-2.0, and the "Awesome-Remote-Sensing-Foundation-Models" GitHub list. Full text preserved in the prior version of this record (git history).

## Post-meeting message 2 (later same day)

> "If you use those embedding datasets with foundation models, this would be good and new. Also, you can do comparisons with some baseline models if needed. That's it. It would be enough for your research! 🙂"
>
> [Image: a 4-panel expected-output mockup — "Occurrence Probability Map", "Driver Attribution Map", "Uncertainty / Confidence Surface", and an "Ablation Comparison Table" button]
>
> "outputs can be like this (image) These datasets also good to add to the analysis
>
> DEA Fuel Moisture Content: https://www.ga.gov.au/scientific-topics/dea/dea-data-and-products/dea-fuel-moisture-content
>
> DEA Fractional Cover: https://www.ga.gov.au/scientific-topics/dea/dea-data-and-products/dea-fractional-cover"

## What this confirms, superseding the earlier partial-transcript reading

- **Option A confirmed, and more specifically than assumed:** not just "occurrence probability," but explicitly a **non-time-series, multimodal ML/DL model** — ruled out a spatiotemporal transformer for the current data on the grounds that 2 years (2019-20) is nowhere near enough for time-series modelling (Arnick's own benchmark: weather prediction typically uses 40-50 years of data).
- **Data: confirmed to reuse the existing ~15,000-record reliability-audited 2019-20 pilot data.** T-033 (full FIRMS 2000-2025 history) is **not needed for the primary, agreed path** — only relevant if pursuing the optional/unfunded "stretch" time-series track, which was discussed but not committed to given "limited time."
- **Region: reversed from the pre-meeting recommendation.** Arnick explicitly wants to **keep the NSW Black Summer 2019-20 event as the defining case study**, not widen to all of NSW or pick a different subregion — framing the mega-complex concentration not as a flaw to route around but as the actual reference event the whole paper should be built around ("it was like a big fire happened for Australia and it's evident").
- **Compute confirmed sufficient:** Kaggle free tier, no need to escalate — the dataset is small enough (Arnick even suggested subsampling to 1,000-5,000 records if useful).
- **Innovation direction confirmed and made concrete:** add a genuine architectural mechanism to the model itself — attention, or a "sensor kind of mechanism" / "modality kind of mechanism" for fusing weather/land-cover/other modalities — not just picking an existing architecture off the shelf. The post-meeting messages extend this to fine-tuning an existing geospatial foundation model (AlphaEarth, Prithvi-EO-2.0) plus baseline-model comparisons.
- **New auxiliary datasets confirmed:** DEA Fuel Moisture Content (named live in the transcript, "moisture content... I'll share some data set"), DEA Fractional Cover (in the follow-up message).
- **New concrete feature-engineering guidance:** weather variables need a lag/aggregation window before each fire date (not same-day) — test multiple aggregation windows (10-day, 15-day, monthly) over a multi-month lookback (2-6 months) and see which correlates best with fire occurrence.
- **The whole project (Phase 1 audit + Phase 2 occurrence model) is explicitly framed as heading toward an actual paper, potentially journal submission** — Arnick walked through a full paper structure (abstract → intro/background → related work/gaps → methodology → results/discussion → conclusion → references).
- **Not addressed at all in the full transcript:** cross-sensor matching (VIIRS/Himawari agreement) — the gap found in the earlier traceability check (T-046) remains genuinely open; it just never came up in this meeting.

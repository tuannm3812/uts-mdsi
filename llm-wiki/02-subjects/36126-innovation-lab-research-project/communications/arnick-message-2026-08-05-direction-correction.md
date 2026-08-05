# Dr Arnick — Direction Correction and Meeting Request, 5 August 2026

**Status:** Received from Dr Arnick via Microsoft Teams, 5 August 2026 (reply to the 3 August findings brief), as two consecutive messages. Recorded verbatim below. This is the source text behind [D-011](../research/decision-log.md), [D-012](../research/decision-log.md) (both previously logged as paraphrase only), [T-008](../research/task-tracker.md), and [T-039](../research/task-tracker.md).

## Message 1 — direction correction

> Hello Tuan, this a very nice information and review you have done. nice job putting all information in the word file summarising details.
>
> But this project is not about the reliability auditing of those existing platforms and methodology for hotspot monitoring.
>
> what I was thinking is that, we get hotspot datasets like time series of fire hotspots from sensors like MODIS (FIRMS: Fire Information for Resource Management System), create a dataset of all fire hotspots timeseries from for example 2000-25 for training the model. But before using this data directly for training, we need to check its reliability and confidence level for those hotspots detected through MODIS algorithms to make sure that the final dataset is in high confidence of fire hotspots. this can be done based on your review through fire records from NSW for exmaple, or corss-sesnor matching and validation like with other sensor like VIIRS or Himawari, or burned datasets like (https://digital.atlas.gov.au/datasets/524e2962bd8b4968b8df9f9774345926/about).
>
> Once final dataset created with confidence, then you can auxiliary data to this with additional variables like weather (rainfall, temperature, wind, humidity, etc), land cover and vegetation condition, etc. for each hotspot location and records. then build multimodal spatiotemporal transformer (time series model) with different modalities coming from MODIS, weather, vegetation/land cover etc and cross-attention for fusion, and then do prediction. This prediction can be different options, for example 1. fire occurrence probability predation with uncertainty and confidence understanding. Like saying that based on whatever model learned from hotspots and auxiliary time series dataset, the probability of fire occurrence is this much and then provides reasoning why with transparent explanation of factors. You can create spatial maps to show probability map for the region you selected as case study.
>
> Also, option 2. prediction hotspots with showing confidence and uncertainty level based on those time series auxiliary data for next for example 1-7 days ahead (this can change based on final data and possibility of the model). This would be forecasting of future what we would expect would be the status of fire hotspot as nowcast.
>
> check work pipeline and do a bit of search how this looks like and how to add innovation to this and then see how to build methodology, data and models. Any of those prediction options would be fine to work. check how each process can be done.
>
> Because of timeframe of the research subject, can not add more complexity to the project.
> thanks

## Message 2 — meeting request (sent immediately after)

> If you want to discuss about your review and findings as well this one I shared, please send me a teams invite for Friday 7 August, 12pm to talk the concerns and steps.

## Notes

- An earlier version of this record included a stray paragraph ("The Earth Engine version of the Fire Information for Resource Management System (FIRMS) dataset contains the LANCE fire detection product...") between "thanks" and the meeting-request message. Tuan confirmed (2026-08-06) that was a clipboard artifact from copy-pasting the message — not something Arnick wrote — and it's removed here.
- "This one I shared" in message 2 most plausibly refers to the Digital Atlas of Australia burnt-area link in message 1 (`digital.atlas.gov.au/datasets/524e2962...`) — confirmed at the meeting, not assumed.
- Confirms the Friday 7 August meeting time: **12:00pm**.
- Maps directly onto D-011 (reliability audit reframed as Phase 1 data-quality gate, not the destination) and D-012 (Option B — 1–7 day forecasting — confirmed over Option A — occurrence probability).

## Action needed (Tuan, not automatable from here)

Send a Microsoft Teams calendar invite to Dr Arnick for **Friday 7 August 2026, 12:00pm**. No Teams/Outlook access from this session — has to go out from Tuan's own calendar. Tracked as T-039.

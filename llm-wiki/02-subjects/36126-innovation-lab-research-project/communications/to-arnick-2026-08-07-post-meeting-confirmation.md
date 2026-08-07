# Teams Message to Dr Arnick — Post-Meeting Confirmation, 7 August 2026

**Status:** Drafted, not yet sent. Confirms the direction from today's meeting plus the two follow-up messages, so it's on record that both sides understood the same thing before Tuan starts building.

Hi Arnick, thank you for the meeting and for sharing your paper and the model/dataset links — really helpful.

To confirm what I'm taking away: I'll build a multimodal ML/DL model — not time series, since we only have 2 years of audited data — on the existing ~15,000 reliability-audited hotspots from the 2019-20 Black Summer pilot, keeping NSW as the case study. I'll fuse in weather (SILO), DEA land cover, fuel moisture, and fractional cover, with a lagged/aggregated window before each fire date rather than same-day values. For the model, I'll look at fine-tuning a foundation model like AlphaEarth or Prithvi-EO-2.0 with an attention/modality mechanism, and compare against baseline models.

This week I'll read through your paper and the foundation model resources, source the two new DEA datasets, and start the feature engineering. Will share findings as I go.

Thanks again!
Tuan

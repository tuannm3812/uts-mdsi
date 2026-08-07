# Dr Arnick — Meeting Transcript Excerpt and Post-Meeting Message, 7 August 2026

**Status:** Received from Tuan, 7 August 2026 (Teams meeting transcript excerpt, pasted by Tuan) plus Arnick's post-meeting Teams message (sent immediately after the call, includes a paper reference and links). Recorded verbatim below.

**Important caveat:** the transcript excerpt Tuan pasted covers roughly **0:00–10:07** (Tuan's opening recap) and then jumps to **51:38–54:40** (closing exchange). **The ~40 minutes in between — where the actual walkthrough of the 7 prepared decisions most likely happened — is not included in what was pasted.** Do not assume any of the 7 decisions were resolved as planned based on this excerpt alone; only what's explicitly visible below and in the post-meeting message is confirmed.

## Transcript — opening (0:07:55–0:10:07)

> Manh Tuan Nguyen (7:55): So I think, yeah, so actually I still have some questions for you based on what I have done for this week and also about your feedback. So.
>
> Manh Tuan Nguyen (8:10): Yes, so actually I have pushed my findings into the Kaggle notebook and also...
>
> Manh Tuan Nguyen (8:22): Ohh, wait me a second, I will check my...
>
> Manh Tuan Nguyen (8:25): My point, okay, yes, so...
>
> Manh Tuan Nguyen (8:29): Yeah, so I have some some question for you to to seek for your decisions, so I can start doing next week, and yes, for for those for the kernel loop, I can share my my screen right now, but...
>
> Manh Tuan Nguyen (8:49): For the findings, actually, right now I use the...
>
> Manh Tuan Nguyen (8:55): I have do the two data set from the New South Wales IRS [RFS] and also the NPWS, so all of so we have so.
>
> Manh Tuan Nguyen (9:12): So, we have so far the and and and SFWRFS, we only match around 17% of the hotspot with the sensor bufferings, but for the NPWS, those the areas are more broader, so we match.
>
> Manh Tuan Nguyen (9:32): 97%. So, for this one, there's not a real jumps between the sensor improvement for the for between the both data set.
>
> Manh Tuan Nguyen (9:44): is mostly because there are two mega complex in Kerry Ridge and Gospel Mountains that account for 98% of every match in the NPWS. So I think there's no problem with the data set right now.
>
> Manh Tuan Nguyen (10:07): So, so right now, so you, I want to make sure that I understood your replies correctly before I I move to anything else. So, you you said that the the right the reliability audit?

**[~40 minutes not captured in what was pasted]**

## Transcript — closing (0:51:38–0:54:40)

> Arnick Abdollahi (51:38): The results discussion.
>
> Arnick Abdollahi (51:46): And conclusion at the end, I think something reference.
>
> Arnick Abdollahi (51:54): This kind of things, so it's really actually a...
>
> Arnick Abdollahi (52:02): Research paper kind of things that you need to follow.
>
> Arnick Abdollahi (52:09): But I believe this work would be good and we can even try journal, see what would be there.
>
> Manh Tuan Nguyen (52:14): Yeah.
>
> Arnick Abdollahi (52:17): Final outcomes.
>
> Arnick Abdollahi (52:24): So, I'm good.
>
> Manh Tuan Nguyen (52:27): Yeah, I think good, I think.
>
> Manh Tuan Nguyen (52:30): Yeah.
>
> Arnick Abdollahi (52:34): Okay, you update the access to side of data and then land cover for DA, and also we'll check that what other data set we can use or share the links from DA. You can add to your data set.
>
> Manh Tuan Nguyen (52:45): Yeah, yeah.
>
> Arnick Abdollahi (52:50): Also, just remember to do a bit of search on the models, how to add more innovation into the model.
>
> Manh Tuan Nguyen (53:01): Yeah, okay, I understand. I will share you. Yeah, I will look at the data set and will share you the findings later.
>
> Arnick Abdollahi (53:10): Always.
>
> Arnick Abdollahi (53:14): If you have any question or something, just, yeah.
>
> Manh Tuan Nguyen (53:18): I think that's good for me now.
>
> Manh Tuan Nguyen (53:21): Okay.
>
> Manh Tuan Nguyen (53:23): Okay, thank you. Yeah, thank you so much.
>
> Arnick Abdollahi (53:25): Got it.
>
> Manh Tuan Nguyen (53:26): Okay, thank you. Have a good day.
>
> [53:27–54:40: casual conversation — Tuan's location, capstone subject (36127, custom agent harness project), no research-direction content]
>
> Arnick Abdollahi (54:39): Yeah, bye, bye.
>
> Manh Tuan Nguyen (54:40): Bye bye.

## Post-meeting Teams message (sent immediately after)

> This is one of my paper (long time ago) on similar thing I discussed for the first methodology on fire occurrence probability prediction if you want to work on it based your 2019-20 hotspot records you found at initial reliability auditing. But you need to put more innovation into your models and develop new ML/DL architecture.
>
> If we would have good results and methodology, you can write also the similar paper for a good journal.
>
> https://doi.org/10.1016/j.scitotenv.2023.163004 you can also add this Embedding dataset a unified data representation to your dataset as auxiliary data.
>
> AlphaEarth Foundations helps map our planet in unprecedented detail
>
> Satellite Embedding V1 For model, you can work on Fondation models, it would be very interesting to pitch and fine-tune these models to the fire applicaitin and occurecne predction, and see how they will work.
>
> GitHub - Jack-bo1220/Awesome-Remote-Sensing-Foundation-Models
> Prithvi-EO-2.0: A Versatile Multi-Temporal Foundation Model for...
> https://arxiv.org/html/2602.23678v1
>
> Lost of models in GitHub, which you can choose those most well known for time series embeddings and earth observation applications, then see how we can bring it to fire research.

## Notes

- **Not yet reconciled against the 7 prepared decisions** — the visible transcript doesn't confirm or deny most of them (horizon, region, compute, cross-sensor matching). Only two get any visible signal: land cover (confirmed to add) and the Digital Atlas dataset (Arnick says he'll share specific links from DA himself, not settled as "supplementary only").
- **Possible major redirection, not yet confirmed:** "fire occurrence probability prediction... based [on] your 2019-20 hotspot records you found at initial reliability auditing" reads as Option A (occurrence probability), built on the *existing* reliability-audited pilot data — not necessarily requiring the full 2000–2025 FIRMS history (T-033) as an immediate prerequisite, and not explicitly Option B (1–7 day forecasting, D-012's internal pick). This needs direct clarification with Tuan before treating D-012 as still current.
- **Model direction shifted toward foundation models**, not necessarily a from-scratch multimodal transformer: AlphaEarth/Satellite Embedding V1, Prithvi-EO-2.0, and a general pointer to "Awesome-Remote-Sensing-Foundation-Models" — fine-tuning an existing pretrained model rather than building cross-attention fusion from scratch.
- **The referenced paper is confirmed to be Arnick's own prior work** (checked via Crossref): Abdollahi, A. & Pradhan, B. (2023), "Explainable artificial intelligence (XAI) for interpreting the contributing factors feed into the wildfire susceptibility prediction model," *Science of the Total Environment*. It's a wildfire susceptibility/occurrence paper using **explainable AI** — this matches Option A's original description ("transparent explanation of factors") far more closely than Option B. Strong signal, not yet confirmed with Tuan, that this points at Option A rather than the internally-chosen Option B (D-012).
- **Google's Satellite Embedding V1 (AlphaEarth Foundations)** — confirmed via web search: a Google/DeepMind model producing a 64-channel embedding per 10m pixel, integrating optical, radar, elevation, and climate data into one unified representation, annual coverage 2018–2024. Could substantially simplify the auxiliary-data-fusion problem (partially overlaps with the separately-planned weather/land-cover sourcing).
- **Prithvi-EO-2.0** — confirmed real (arXiv 2412.02732, NASA/IBM), a 300M/600M-parameter multi-temporal geospatial foundation model trained on Landsat/Sentinel-2, outperforms 6 other geospatial foundation models on benchmark tasks.
- **The second arXiv link Arnick pasted under the "Prithvi-EO-2.0" heading doesn't actually match** — `arxiv.org/abs/2602.23678` is a different, genuine, more recent (Feb 2026) paper, "Any Model, Any Place, Any Time: Get Remote Sensing Foundation Model Embeddings On Demand" (a tool for retrieving embeddings from multiple remote-sensing foundation models on demand) — still relevant, but not actually Prithvi-EO-2.0 itself. Likely a copy-paste mismatch on his end (same pattern as the stray paragraph found in his 5 August message) — not urgent to correct with him, both links are genuinely useful regardless.
- **Reliability audit may itself be journal-worthy** — "I believe this work would be good and we can even try journal" — a possible parallel/independent publication track for the Phase 1 work, separate from the forecasting model.

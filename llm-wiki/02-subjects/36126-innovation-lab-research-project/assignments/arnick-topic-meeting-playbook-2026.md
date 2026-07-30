# Dr Arnick Topic Meeting Playbook — 29 July 2026

## Desired outcome

Leave the meeting with:

1. A preferred topic
2. A provisional research question
3. A clear understanding of the data
4. A feasible semester scope
5. A concrete first task and deadline
6. Confirmation of supervision or the next approval step

You do not need to finalise the model architecture during this meeting.

## Suggested 30-minute structure

| Time | Purpose |
|---:|---|
| 0–3 minutes | Introductions, goals, and background |
| 3–10 minutes | Dr Arnick explains available topics |
| 10–20 minutes | Compare the strongest options |
| 20–26 minutes | Agree on scope, data, and expected contribution |
| 26–30 minutes | Confirm supervision, first tasks, and next meeting |

## Opening

> Thank you for meeting with me. I’m looking for a Research Project that will help me develop rigorous research skills while building on my applied machine-learning experience. My longer-term goal is to work as an AI/ML engineer, and I may consider a PhD later.
>
> My current strengths are Python, machine learning, deep learning, time-series forecasting, data engineering, model evaluation, and building reproducible AI applications. Remote sensing, GIS, and environmental modelling would be new areas for me, but I’m willing to learn them.
>
> I’d like to understand the topics and datasets currently available, then identify an option that has a clear research contribution and is feasible within the subject timeline.

## Full demo conversation

This is a model conversation, not a script that must be followed word for word. Listen to Dr Arnick’s answer before moving to the next question.

### Opening and available topics

**Tuan:**

> Thank you for meeting with me. I’m interested in developing rigorous research skills while building on my machine-learning and data-engineering experience. I may also consider a PhD later.
>
> Could you first explain which environmental or climate-hazard topics and datasets are currently available for a student to begin this semester?

**Possible answer from Dr Arnick:**

> The two main options are bushfire occurrence prediction and agentic AI for weather extremes. I may also have a related topic depending on your interests.

**Tuan:**

> Thank you. Before choosing, could you explain the main research question, available data, and expected contribution for each option? I would like to compare them based on feasibility and research value, not only the application title.

### If he explains the bushfire project

**Possible answer from Dr Arnick:**

> The bushfire project uses satellite, climate, and historical fire data to predict where fire occurrence is likely. Explainability is important because we want to understand the environmental drivers.

**Tuan:**

> That direction interests me because it combines predictive modelling, time-dependent data, explainability, and an important Australian application.
>
> What would the model predict exactly: fire occurrence, susceptibility, or a risk category? What geographic unit and prediction horizon would we use?

**Possible answer:**

> We may predict fire occurrence across regional grid cells using monthly environmental variables.

**Tuan:**

> Is that dataset already prepared and aligned, or would acquiring and integrating the satellite, climate, and fire records be a major part of my work?

**Possible answer:**

> We have some processed data, but you may need to perform further cleaning and feature engineering.

**Tuan:**

> That sounds manageable. Could we identify what is already available and define a minimum dataset for the first modelling baseline? I want to preserve enough time for leakage-safe validation, explainability, and writing.

### Clarifying the research contribution

**Tuan:**

> What would make this a research contribution rather than only applying standard models to an environmental dataset?

**Possible answer:**

> You could compare models across bioregions, study how risk drivers vary spatially, or improve the validation and explainability framework.

**Tuan:**

> Of those directions, which one addresses the clearest gap in the existing research and is realistic within the remaining semester?

**Possible answer:**

> Region-specific explainability and robust spatial validation would be useful.

**Tuan:**

> Would a suitable provisional question be: “Can region-specific explainable machine-learning models improve bushfire occurrence prediction and reveal how environmental risk drivers vary across regions compared with a single national model?”
>
> I understand that we would refine the wording after reviewing the data and literature.

### If he recommends the agentic weather project

**Possible answer from Dr Arnick:**

> Your AI-agent experience may make the agentic weather-extremes project a better technical fit.

**Tuan:**

> I’m open to that direction. What measurable problem would the agents solve better than a conventional anomaly-detection or forecasting pipeline?

**Possible answer:**

> The agents would combine several sources, detect unusual conditions, and generate an interpretable assessment.

**Tuan:**

> What objective baselines and metrics would we use to evaluate earlier detection, false alarms, evidence grounding, and reliability? I would want the project to test a scientific hypothesis rather than only demonstrate a multi-agent application.

### If he proposes another topic

**Possible answer from Dr Arnick:**

> I also have another project involving drought, vegetation, or climate-risk prediction.

**Tuan:**

> I would be interested in considering it. Could we define its prediction target, available dataset, research gap, minimum experiment, and new skills required? That would help me compare it fairly with the two listed topics.

### Discussing your background

**Possible question from Dr Arnick:**

> What experience can you bring to the project?

**Tuan:**

> I can contribute Python, data preparation and pipelines, machine learning, deep learning, time-series forecasting, reproducible evaluation, APIs, dashboards, and technical documentation. My main learning areas would be remote sensing, GIS operations, spatial validation, and environmental interpretation.
>
> I’m willing to learn those areas, but I would like to begin with a focused scope and data that lets me establish a reliable baseline early.

### Discussing computing

**Tuan:**

> I don’t currently have a dedicated local GPU. Do you expect the project to require substantial GPU training, and are university computing resources available? If appropriate, I can use Kaggle, Colab, or another cloud environment for experiments.

**Possible answer:**

> Classical models may be sufficient initially, and we can discuss cloud resources if deep learning is required.

**Tuan:**

> That approach suits me. I would prefer to establish strong interpretable baselines first and only add a complex model if it addresses a demonstrated limitation.

### Discussing publication without overpromising

**Tuan:**

> I saw the recent MDSI drought-prediction preprint and was encouraged by the research outcome. If my results are strong, could this project potentially be developed into a preprint or publication?

**Possible answer:**

> It may be possible, but it depends on the novelty and quality of the results.

**Tuan:**

> Understood. My priority is to complete a rigorous and reproducible subject project. I would be willing to continue after the semester if the results justify a manuscript and we agree on the additional work.

### Selecting the topic

**Tuan:**

> Based on what we have discussed, which option would you recommend for my background, the available data, and the limited timeline?

**Possible answer:**

> I recommend the bushfire project because the data and research direction are clearer.

**Tuan:**

> I’m happy to proceed with that recommendation. Could we record a provisional title and research question now, even if we refine them after the initial literature and data review?

### Confirming the first task

**Tuan:**

> What should I complete during the first week? For example, should I begin with a focused literature review, inspect a provided dataset, reproduce an existing baseline, or prepare a short proposal?

**Possible answer:**

> Read these papers, review the data dictionary, and prepare an initial problem statement.

**Tuan:**

> Thank you. When should I send those materials to you, and when would you like our next supervision meeting?

### Closing

**Tuan:**

> Let me confirm my understanding. The provisional direction is **[topic]**, the initial research question is **[question]**, and the main data will be **[dataset]**. My first tasks are **[tasks]** by **[date]**.
>
> I’ll send you a short written summary today so you can correct anything I misunderstood. What administrative confirmation should we send to the subject coordinator to formalise the topic and supervision?

## Short demo for a rushed meeting

If only five minutes remain, use:

> Of the topics and datasets currently available, which one would you recommend for my background and the remaining timeline?
>
> What exact research question would I investigate?
>
> Is the data ready for me to begin?
>
> What should I complete during the first week?
>
> What must we send to the coordinator to confirm the supervision?

## First questions: understand the available choices

Ask these before selecting a topic:

1. What specific research topics are currently available for me to begin this semester?
2. Are the two published topics—the bushfire project and agentic weather-extremes project—the main options, or are there related alternatives?
3. For each option, what is the core research question rather than only the application area?
4. Which topic do you think best matches my current skills and limited geospatial experience?
5. Which project has data and a clear starting point available now?
6. Which option is most likely to produce a meaningful research contribution within the semester?

## Questions for each serious topic

### Research problem

- What exactly would the model predict, detect, explain, or optimise?
- What decision or user would the result support?
- What limitation in existing research would the project address?
- What would make my work different from simply applying an existing model?
- What result would count as a successful research outcome?

### Scope

- What is the geographic region?
- What spatial unit should be used?
- What time period and prediction horizon are expected?
- Is the study retrospective, forecasting-oriented, or both?
- What is the minimum viable scope?
- Which extensions should only be attempted if time permits?

### Data

- What datasets are already available?
- Are they cleaned and aligned, or must I build the dataset?
- What are the target labels?
- How large are the raster/tabular datasets?
- Are there data-access, licensing, storage, or confidentiality restrictions?
- Is there existing preprocessing code from the research team?
- Who can help interpret the environmental variables?

### Methods

- Which baseline models must be included?
- Is there an expected advanced modelling family?
- Is explainability a central research component?
- Should the project include uncertainty estimation or probability calibration?
- How should spatial and temporal leakage be prevented?
- What evaluation design would be scientifically convincing?
- Which metrics matter to the domain, beyond generic ML accuracy?

### Resources and supervision

- What software should I learn first?
- Are Google Earth Engine, QGIS, GeoPandas, Rasterio, or Xarray likely to be required?
- Can the experiments run on Kaggle or Colab?
- Are university compute or cloud resources available?
- Will I work only with you, or with another researcher or domain expert?
- How frequently will we meet?
- What should I bring to each supervision meeting?

### Deliverables and publication

- What outputs are expected: paper, code, maps, model, dashboard, or dataset?
- What level of reproducibility is expected?
- If the results are strong, could the work be developed into a preprint or journal submission?
- Would publication require additional work after the subject?
- How would authorship and responsibilities be discussed?

## Scenario A: bushfire project is available with prepared data

### What to clarify

- Exact target: occurrence, susceptibility, risk, severity, or recovery
- Spatial unit and forecast horizon
- Dataset contents and readiness
- Required baseline and advanced models
- Expected XAI and validation design

### Response

> This sounds strongly aligned with my interests, especially the combination of predictive modelling, explainability, and actionable risk information. The prepared data also makes the semester scope more realistic.
>
> Before confirming, could we define the provisional research question and the first task I should complete this week?

### Do not leave without

- Dataset access method
- One initial paper or reading list
- Provisional research question
- First task and expected completion date

## Scenario B: bushfire project is available, but data engineering is substantial

### Risks

- Most of the semester may be consumed by downloading and aligning satellite data
- Limited time may remain for modelling, evaluation, and writing
- Storage and compute may become a bottleneck

### Questions

- Is dataset construction itself part of the intended contribution?
- Can the geographic or temporal scope be reduced?
- Is there an existing subset or processed dataset?
- Can I begin with tabular regional aggregates before raster modelling?
- What minimum modelling result is expected if data preparation takes longer than planned?

### Response

> I’m comfortable with data engineering, but I want to ensure there is enough time for rigorous modelling and evaluation. Would it be sensible to begin with an existing regional or processed subset and treat broader satellite integration as an extension?

## Scenario C: he recommends agentic AI for weather extremes

### What to investigate

- Whether “agentic” is essential to the research question or only the system architecture
- Available weather feeds and historical extreme-event labels
- How agent performance would be evaluated objectively
- Whether the project risks becoming a demonstration without a strong scientific comparison

### Questions

- What failure in conventional forecasting or monitoring is the agent system intended to address?
- What does each agent do?
- What are the baselines: anomaly detection, conventional ML, or a single LLM workflow?
- How will early detection, false alarms, reasoning quality, and reliability be measured?
- Is LLM reasoning grounded in deterministic weather analysis?

### Response if interested

> This is close to my existing AI-agent experience. To ensure it has sufficient research depth, I would like to understand the measurable hypothesis and comparison baselines. Would the contribution focus on earlier anomaly detection, better evidence integration, or more interpretable risk assessment?

### Decision warning

Prefer this topic only if:

- Data and labels are available
- There is a measurable hypothesis
- The evaluation goes beyond subjective LLM output quality
- The scope does not require building a large multi-agent platform before research begins

## Scenario D: he proposes a new related topic

Do not accept immediately just because it sounds innovative.

### Ask

- What is the one-sentence research question?
- Why is this problem currently unresolved?
- What data is immediately available?
- What is the minimum feasible experiment?
- What skills must I learn in the first two weeks?
- Is this topic formally acceptable for the subject?

### Response

> The direction sounds interesting. Could we write down a provisional title, research question, dataset, expected contribution, and minimum deliverable? That would help me compare it fairly with the listed topics and start without ambiguity.

## Scenario E: he asks you to choose immediately

Use this decision order:

1. Data readiness
2. Clear research question
3. Feasibility in the remaining semester
4. Quality of evaluation opportunity
5. Fit with your skills and career goals
6. Publication potential
7. Novelty or trendiness

Say:

> Based on our discussion, my current preference is **[topic]** because it has **[ready data / clear research gap / feasible evaluation]**. Before I confirm, could we agree on the provisional research question and first milestone?

## Scenario F: he says your geospatial background is insufficient

Do not become defensive.

### Ask

- Which specific prerequisite is missing?
- Can it be learned during the first one or two weeks?
- Is there a smaller geographic or tabular version of the problem?
- Is another available topic a better fit?

### Response

> Thank you for being direct. I’m willing to learn the required tools, but I also want to choose a realistic scope. Which skills would I need immediately, and would a smaller regional or tabular formulation make the project feasible?

## Scenario G: compute requirements are high

### Ask

- Is GPU training genuinely necessary?
- Are precomputed satellite features available?
- Can classical ML or smaller models answer the research question?
- Are cloud credits, university compute, Colab, Kaggle, or Google Earth Engine available?
- What storage and memory are required?

### Response

> I don’t currently have a dedicated local GPU, so I would plan to use cloud or hosted resources. I’m comfortable designing the workflow around Kaggle, Colab, or university compute, but I’d like to confirm the expected cost and access before finalising the scope.

## Scenario H: publication is possible

Ask carefully:

- What additional standard would publication require?
- Is there a target venue or only a general possibility?
- Would work continue after the subject deadline?
- Who would be involved in interpreting results and writing?

### Response

> Publication potential is attractive because I may consider a PhD, but my priority is to complete a rigorous subject project first. I would be willing to continue afterward if the results justify it and expectations are agreed clearly.

Do not treat publication as guaranteed.

## Scenario I: he has no supervision capacity

### Ask

- Does he recommend another supervisor?
- Can he suggest which listed topic best fits your background?
- Is Dr Tony Huang’s graph-design assistant a sensible alternative?
- May you mention Dr Arnick’s recommendation when making contact?

### Response

> Thank you for letting me know. I’m also considering Dr Tony Huang’s intelligent graph-design assistant topic because it combines LLMs, RAG, graph analytics, and controlled evaluation. Do you think that would suit my background, and would you recommend that I contact him directly?

## Scenario J: he asks about your preferred topic

Use:

> My initial preference is the bushfire occurrence and risk-intelligence project because it combines time-series and predictive modelling with explainability and a meaningful Australian application. However, I would like to hear which topics have the clearest data, research gap, and feasible scope before making the final decision.

## Scenario K: he asks what methods you want to use

Do not lead with graph ML or deep learning.

Use:

> I would begin with the research question and data structure. My initial plan would be to establish interpretable statistical and tree-based baselines, design leakage-safe spatial and temporal validation, and then investigate a more advanced model only if it addresses a clear limitation. I’m interested in explainability, calibration, and potentially spatiotemporal or graph methods, but I would not want to force them into the project without evidence that they are appropriate.

## Scenario L: he asks what you can contribute

> I can contribute strong Python development, data preparation and pipelines, conventional machine learning, deep learning, time-series forecasting, evaluation, reproducibility, APIs, dashboards, and technical documentation. My main learning areas would be remote-sensing data, GIS operations, spatial validation, and environmental interpretation.

## Closing script

> Thank you. To confirm my understanding, the selected direction is **[topic]**, with a provisional question of **[question]**, using **[data]**. My first task is **[task]** by **[date]**, and our next step for formal confirmation is **[administrative step]**.
>
> I’ll send a short written summary after the meeting so you can correct anything I misunderstood. When would you like our next supervision meeting?

## Notes to capture live

| Item | Notes |
|---|---|
| Available topics |  |
| Recommended topic |  |
| Provisional title |  |
| Research question |  |
| Research gap |  |
| Prediction target |  |
| Geographic scope |  |
| Time horizon |  |
| Available data |  |
| Required data work |  |
| Baseline methods |  |
| Advanced methods |  |
| XAI / uncertainty |  |
| Validation approach |  |
| Compute resources |  |
| Expected deliverables |  |
| Publication possibility |  |
| First task |  |
| First-task deadline |  |
| Next meeting |  |
| Administrative action |  |

## Final decision check

Before agreeing, you should be able to complete this sentence:

> I will investigate whether **[method or information]** improves **[measurable outcome]** for **[defined prediction/decision task]** using **[named data and scope]**, compared with **[baseline]**.

If this sentence cannot be completed, the topic is not yet sufficiently defined.

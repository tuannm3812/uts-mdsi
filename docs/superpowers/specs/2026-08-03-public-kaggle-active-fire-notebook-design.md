# Public Kaggle Active-Fire Pilot Notebook Design

**Date:** 3 August 2026  
**Owner:** Tuan Nguyen  
**Implementer:** Codex  
**Reviewer:** Claude, through the shared 36126 agent collaboration log  
**Publication state:** Private Kaggle draft first; public release requires Tuan's later approval

## Objective

Create a polished, reproducible Kaggle notebook that explains the NSW public-data fire-hotspot feasibility pilot to a general technical audience. The notebook must demonstrate how the findings were produced without exposing supervision discussions, internal planning, credentials, personal contact details, or local filesystem information.

The notebook is an evidence presentation and reproducibility artifact. It is not a claim of operational fire-detector accuracy and not yet a machine-learning model demonstration.

## Audience and success criteria

The initial audience is Tuan and reviewers of the private Kaggle draft. The eventual audience is data-science practitioners, researchers, and interested public Kaggle users.

The notebook succeeds when:

- a reader can understand the research problem, pilot design, main findings, and limitations without opening repository files;
- every displayed headline count and percentage is generated from the included snapshot rather than typed as an unsupported result;
- the saved notebook opens with complete outputs even when external public services are unavailable;
- an optional refresh path can retrieve public data and rerun the analysis when Kaggle internet access is enabled;
- the notebook clearly distinguishes confirmed matches, unresolved observations, and false-alarm claims that the data cannot support;
- no internal or sensitive content appears in notebook source, outputs, metadata, dataset files, logs, or upload configuration; and
- the private Kaggle draft executes successfully before Tuan considers public publication.

## Privacy boundary

### Allowed public content

- Public DEA Hotspots and NSW Fire History source descriptions and URLs
- Public study configuration, code, provenance, checksums, and derived results
- Scientific interpretation, uncertainty, limitations, and general future work
- Repository-neutral reproduction instructions

### Local-only content

- Dr Arnick Abdollahi's name, messages, advice, meeting notes, or supervision questions
- Internal subject administration and assessment planning
- Draft outreach messages and supervisor findings briefs
- Kaggle API credentials, email addresses, phone numbers, usernames used as secrets, or authentication paths
- Local absolute paths and private Google Drive locations
- Agent collaboration discussion that is not required to reproduce the pilot

The public notebook may describe the work as an independent feasibility pilot. It must not mention or imply supervisor endorsement.

## Delivery architecture

The Kaggle deliverable consists of two private artifacts during review:

1. **Snapshot dataset:** immutable pilot inputs and outputs, configuration, provenance, checksums, licence/source notes, and reusable analysis modules.
2. **Presentation notebook:** a readable `.ipynb` that uses the attached snapshot by default and optionally refreshes from the public source services.

This separation keeps the notebook readable, makes saved results reliable, and avoids embedding large raw payloads in notebook JSON.

### Execution modes

- `snapshot` is the default mode. It reads the attached Kaggle dataset and must work without network access.
- `live_refresh` is opt-in. It retrieves the same bounded public-source queries, records new provenance and checksums, and reruns the analysis. It must never silently replace the reviewed snapshot.
- A compact comparison reports whether refreshed headline results match the reviewed snapshot. Differences are flagged as source evolution, not automatically treated as code failures.

GPU acceleration is disabled by default because the pilot is data retrieval, geometry, aggregation, and visualisation. GPU use belongs to a later modelling notebook if the research design justifies it.

## Public notebook structure

The narrative is grouped into six major sections.

### 1. Project overview

- Plain-language problem statement
- Scope: hotspot detection and active-fire monitoring; no fire-spread prediction
- Bounded NSW region and January 2020 pilot period
- Headline finding cards generated from data
- Interpretation warning: unmatched observations are unresolved, not proven false alarms

### 2. Data and methodology

- DEA Hotspots and NSW Fire History source roles
- Snapshot/live-mode control and provenance
- Study bounding box and temporal windows
- Exact spatial-temporal match definition
- Sensor-position-buffer sensitivity definition
- Reproducible pipeline diagram or compact process explanation

### 3. Results

- Sensor composition table and chart
- Map of hotspot observations and fire-event boundaries, using sampling or aggregation if needed for readability
- Exact versus buffered match counts and rates
- Match rate by sensor with denominators shown
- Confidence distributions separated by sensor and processing algorithm
- Accessible colour palette, informative titles, captions, and source/sample notes

### 4. Reliability analysis

- Event concentration and the dominance of `Stockyard Creek; Little`
- Why random hotspot-row splitting leaks events
- Effect of sensor-position buffers
- Why confidence fields are not one common probability scale
- Transparent explanation of unresolved observations and reference-data limitations

### 5. Research implications

- Three-class evidence design: confirmed event, unresolved, confirmed non-fire
- Held-out-event and future-period evaluation recommendation
- Event aggregation and sensor-aware calibration as defensible next experiments
- Advanced temporal or graph models positioned as conditional future work, not assumed novelty
- No supervisor-specific question or internal decision request

### 6. Reproducibility

- Software and data requirements
- Source URLs, retrieval timestamps, query configuration, checksums, and record counts
- Instructions for snapshot and live-refresh execution
- Known limitations and ethical/safety interpretation boundary
- Public-source acknowledgements and licence notes

## Visual and editorial standards

- Use concise Markdown and progressive disclosure; explanatory prose precedes complex code.
- Keep setup and helper code collapsed where Kaggle supports it, while leaving the core matching and calculation logic inspectable.
- Use a colour-blind-safe palette with sufficient contrast and avoid red/green-only encoding.
- Every chart must state its population or sample size and distinguish counts from rates.
- Maps must avoid misleading precision and explain that final fire polygons are not point-in-time flame boundaries.
- Avoid decorative visualisations that do not answer a stated question.
- Use Australian English and define technical terms on first use.
- Do not include claims that exceed the evidence in the completed pilot.

## Data flow

1. Resolve Kaggle snapshot paths or explicitly enter live-refresh mode.
2. Validate expected files, schemas, query configuration, record counts, and hashes.
3. Normalise hotspot and fire-event records using the existing tested pilot logic.
4. Produce exact and sensor-buffered observation-level classifications.
5. Derive all summaries and chart frames from those classifications.
6. Assert the reviewed snapshot invariants: 19,849 hotspots, 14 overlapping events, 2,878 exact matches, 3,385 buffered matches, and 16,461 unresolved buffered observations.
7. Render tables, maps, charts, interpretations, and provenance.
8. In live mode, compare refreshed results with the reviewed snapshot and explain any drift.

## Error handling

- Missing snapshot files stop execution with a clear instruction to attach the required Kaggle dataset.
- Schema drift identifies the missing or changed fields and stops before producing misleading results.
- Live-source network failures fall back only when the user explicitly accepts the reviewed snapshot; they must not masquerade as a successful refresh.
- Hash mismatches produce a visible warning and prevent reviewed-snapshot claims.
- Empty filters or zero-event queries stop with the active region and date configuration shown.
- Visualisation sampling affects display only; numerical calculations always use the full dataset.

## Verification strategy

Before upload, Codex will:

1. Run the existing pilot unit tests.
2. Execute the notebook from a clean state against the packaged snapshot.
3. Assert the headline counts and percentages against the reviewed pilot report.
4. Confirm charts and maps use the intended full-data summaries or clearly labelled display samples.
5. Validate notebook JSON and confirm no cell has an unintended exception.
6. Scan notebook source, outputs, metadata, snapshot files, and Kaggle metadata for secrets, private paths, contact details, and internal-only names.
7. render the executed notebook to HTML or an equivalent visual form and inspect every section for clipping, unreadable colours, misleading labels, and excessive output;
8. upload both artifacts privately; and
9. confirm their Kaggle privacy state and successful private execution.

Claude's review should challenge privacy leakage, scientific overclaiming, result reproducibility, visual clarity, and whether the six-section structure is understandable to a public reader. Any review finding will be evaluated and resolved before implementation or publication, rather than accepted without technical verification.

## Publication workflow

1. Codex writes the implementation plan after Tuan and Claude approve this design.
2. Codex builds and validates the snapshot dataset and notebook locally.
3. Codex uploads both artifacts privately to Tuan's Kaggle account.
4. Tuan reviews the private Kaggle presentation and outputs.
5. Claude reviews the private-ready artifact or exported notebook evidence.
6. Codex addresses verified findings and reruns validation.
7. Public publication occurs only after Tuan explicitly authorises it.

## Out of scope

- Training a deep-learning, graph, or temporal prediction model
- Fire-spread forecasting
- Claiming unmatched hotspots are false positives
- Publishing the notebook or dataset publicly during initial implementation
- Uploading supervisor correspondence, internal literature notes, or unfinished citation claims
- Requesting or using non-public incident data

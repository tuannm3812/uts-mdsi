# Fire-Hotspot Detection and Monitoring Literature Search Protocol

## Review objective

Map existing fire-hotspot detection and active-fire-monitoring methods and identify a feasible gap involving transparent modelling, data fusion, graph or transformer methods, uncertainty, and robust geographic/temporal validation. The review must include Australian studies and geographically diverse international studies.

## Scope taxonomy

Record each paper under exactly one primary task:

1. Fire-hotspot or active-fire detection — primary scope
2. Active-fire monitoring or temporal tracking — primary scope
3. Future ignition or hotspot occurrence prediction — adjacent scope
4. Fire susceptibility or long-term risk mapping — adjacent scope
5. Fire spread or perimeter forecasting — excluded from synthesis except to distinguish tasks
6. Burned-area or severity forecasting — adjacent scope
7. Decision support or response optimisation — supporting scope

Do not combine performance results across these tasks.

## Databases

- Scopus
- Web of Science
- Google Scholar
- IEEE Xplore
- ACM Digital Library
- ScienceDirect
- SpringerLink
- arXiv for recent work, marked as non-peer-reviewed where applicable

## Search blocks

### Hazard and task

`wildfire OR bushfire OR "forest fire" OR "fire hotspot" OR "active fire"`

AND

`detection OR monitoring OR tracking OR identification`

### Methods

Use one or more:

- `transformer OR "temporal fusion transformer" OR attention`
- `"graph neural network" OR GNN OR graph-based`
- `"spatiotemporal model" OR "time series"`
- `"data fusion" OR multimodal OR multisource`
- `explainable OR interpretable OR SHAP`
- `uncertainty OR calibration OR conformal OR probabilistic`
- `"spatial validation" OR "temporal validation" OR generalisation`

## Inclusion criteria

- Predictive or explanatory modelling of a wildfire-related task
- Uses environmental, remote-sensing, meteorological, spatial, temporal, or human-driver data
- Provides enough methodological detail to extract task, target, validation, and metrics
- Peer-reviewed work, plus clearly marked influential or very recent preprints
- English-language publication

## Exclusion criteria

- Fire-spread or perimeter-forecasting studies with no hotspot-detection or active-monitoring component
- Purely physical fire simulation without a relevant ML or uncertainty comparison
- Commentary without empirical or review evidence
- Duplicate or superseded versions
- Papers where full text or essential methodological information cannot be verified

## Screening procedure

1. Deduplicate by DOI and title.
2. Screen title and abstract.
3. Assign primary task taxonomy.
4. Read full text for included studies.
5. Extract evidence into the matrix.
6. Conduct backward and forward citation chaining for key reviews and closest methods.
7. Record the exact search date, database, query, and result count.

## Geographic coverage rule

- Tag every included paper by country, region, and biome where available.
- Maintain an explicit Australian subgroup.
- Include studies from several non-Australian regions rather than treating one international dataset as globally representative.
- Use global evidence to identify methods and gaps; use Australian evidence to assess case-study relevance and data feasibility.

## Quality checks

- Was validation random, temporal, spatial, or spatiotemporal?
- Could any feature contain future information?
- Are non-fire samples and class imbalance handled credibly?
- Are baselines competitive?
- Is uncertainty quantified or merely mentioned?
- Are explanations local/global, stable, and scientifically interpreted?
- Is code or data available?
- Does the claimed operational value match the prediction horizon?

## Gap-evidence rule

A candidate gap must be expressed as:

> Although studies A–C address **X**, they are limited by **Y** under **Z** conditions. This project will test **proposed contribution** using **evaluation capable of falsifying the claim**.

Use “underexplored in the reviewed literature” instead of “never studied” unless the search supports the stronger statement.

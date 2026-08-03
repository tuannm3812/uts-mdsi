# Public Kaggle Active-Fire Pilot Notebook Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build, validate, and privately upload a public-ready Kaggle notebook that reproduces and explains a licensed NSW fire-hotspot reliability pilot without exposing supervision or private content.

**Architecture:** Keep the existing internal pilot unchanged. Add a separate public-Kaggle package with an enforceable source-licence manifest, deterministic analysis/visualisation helpers, a generated six-section notebook, and private-upload metadata. Package a snapshot only after the licence gate passes; otherwise switch to the explicitly licensed NPWS Fire History source and regenerate all public results.

**Tech Stack:** Python 3.9+, standard library, pandas, matplotlib, seaborn, nbformat, nbclient, pytest, Kaggle API/CLI, GeoJSON, JSON, Markdown

## Global Constraints

- The notebook contains no Dr Arnick/supervision content, internal subject administration, contact details, credentials, local absolute paths, Google Drive paths, or agent discussion.
- Upload privately first; do not make the dataset or notebook public without a later explicit instruction from Tuan.
- Do not upload NSW RFS `NSWFireHistory/FeatureServer/0` records, geometry, or record-level derivatives unless an authoritative exact licence and attribution statement is recorded.
- If NPWS Fire History replaces the NSW RFS service, rerun the complete pilot and regenerate every public number, table, map, invariant, and interpretation.
- Snapshot mode is the default; live refresh is opt-in and never overwrites the reviewed snapshot.
- Hard result assertions apply only to the reviewed snapshot; live-source drift is reported without being mislabelled as code failure.
- Unmatched observations are called `unresolved`, never assumed to be false alarms or false positives.
- Visual samples use a fixed seed or deterministic thinning rule stated in their captions.
- GPU is disabled for this pilot notebook.
- No collaborator is invited to the private Kaggle artifacts unless Tuan names that person explicitly.
- Claude reviews the plan and private-ready artifact through `agent-collaboration-log.md`; Codex evaluates each finding before implementation or upload continues.

## File map

- Create `llm-wiki/02-subjects/36126-innovation-lab-research-project/notebooks/active-fire-kaggle/README.md` — local build, validation, and private-upload instructions.
- Create `.../active-fire-kaggle/licence-manifest.json` — machine-readable redistribution status and attribution for each source.
- Create `.../active-fire-kaggle/package_snapshot.py` — fail-closed snapshot packager.
- Create `.../active-fire-kaggle/public_analysis.py` — public-safe aggregation, invariant, drift, and deterministic-sampling functions.
- Create `.../active-fire-kaggle/public_visuals.py` — accessible charts and map rendering.
- Create `.../active-fire-kaggle/build_notebook.py` — deterministic six-section notebook generator.
- Create `.../active-fire-kaggle/audit_public_artifact.py` — privacy, claim-language, metadata, and output audit.
- Create `.../active-fire-kaggle/requirements-public.txt` — direct dependency versions used for local execution.
- Create `.../active-fire-kaggle/kaggle/dataset-metadata.json` — private snapshot dataset metadata.
- Create `.../active-fire-kaggle/kaggle/kernel-metadata.json` — private CPU notebook metadata with internet disabled by default.
- Create `.../active-fire-kaggle/upload_private.py` — credential-safe private Kaggle upload and status verification.
- Generate `.../active-fire-kaggle/nsw-active-fire-reliability-pilot.ipynb` — tracked notebook source with saved outputs only after clean execution.
- Create `.../active-fire-kaggle/tests/` — focused tests for licensing, analysis, notebook structure, audits, and upload metadata.
- Create `llm-wiki/02-subjects/36126-innovation-lab-research-project/sources/data/nsw-fire-history-licence-decision.md` — authoritative source evidence and selected public-source decision.
- Modify `llm-wiki/02-subjects/36126-innovation-lab-research-project/README.md` — link the private-ready notebook package after local verification.
- Append `llm-wiki/02-subjects/36126-innovation-lab-research-project/agent-collaboration-log.md` — Codex decisions and Claude review handoffs.
- Use ignored/generated `output/kaggle/active-fire-pilot/` for packaged snapshot and Kaggle staging; never commit credentials or raw data without an explicit licence decision.

---

### Task 1: Enforce the source-licence gate

**Files:**
- Create: `llm-wiki/02-subjects/36126-innovation-lab-research-project/notebooks/active-fire-kaggle/licence-manifest.json`
- Create: `llm-wiki/02-subjects/36126-innovation-lab-research-project/notebooks/active-fire-kaggle/package_snapshot.py`
- Create: `llm-wiki/02-subjects/36126-innovation-lab-research-project/notebooks/active-fire-kaggle/tests/test_package_snapshot.py`
- Create: `llm-wiki/02-subjects/36126-innovation-lab-research-project/sources/data/nsw-fire-history-licence-decision.md`

**Interfaces:**
- Consumes: source files, manifest entries with `source_id`, `licence_status`, `licence_name`, `kaggle_license_name`, `attribution`, `reviewed_sha256`, and `allowed_files`.
- Produces: `validate_manifest(manifest: dict) -> None` and `package_snapshot(manifest_path: Path, source_dir: Path, output_dir: Path) -> list[Path]`.

- [ ] **Step 1: Write the failing licence-gate tests**

```python
def test_unconfirmed_source_cannot_be_packaged(tmp_path):
    manifest = {
        "sources": [{
            "source_id": "nsw-rfs-fire-history",
            "licence_status": "unconfirmed",
            "allowed_files": ["nsw_fire_history.geojson"],
        }]
    }
    with pytest.raises(ValueError, match="unconfirmed"):
        validate_manifest(manifest)


def test_confirmed_source_requires_attribution():
    manifest = {
        "sources": [{
            "source_id": "npws-fire-history",
            "licence_status": "confirmed",
            "licence_name": "Creative Commons Attribution",
            "attribution": "",
            "allowed_files": ["npws_fire_history.geojson"],
        }]
    }
    with pytest.raises(ValueError, match="attribution"):
        validate_manifest(manifest)


def test_packager_writes_checksums_for_every_file(tmp_path):
    packaged = package_confirmed_fixture(tmp_path)
    snapshot_manifest = json.loads((packaged / "snapshot-manifest.json").read_text())
    assert set(snapshot_manifest["sha256"]) == {
        "dea_hotspots.geojson",
        "fire_history.geojson",
        "source-config.json",
    }


def test_packager_rejects_file_that_differs_from_reviewed_provenance(tmp_path):
    source_dir, manifest_path = confirmed_fixture_with_reviewed_hashes(tmp_path)
    (source_dir / "dea_hotspots.geojson").write_text("modified", encoding="utf-8")
    with pytest.raises(ValueError, match="reviewed provenance"):
        package_snapshot(manifest_path, source_dir, tmp_path / "package")
```

- [ ] **Step 2: Run the focused test and verify failure**

Run: `python3 -m pytest llm-wiki/02-subjects/36126-innovation-lab-research-project/notebooks/active-fire-kaggle/tests/test_package_snapshot.py -q`

Expected: FAIL because `package_snapshot.py` does not exist.

- [ ] **Step 3: Implement the fail-closed manifest validator and packager**

```python
def validate_manifest(manifest: dict) -> None:
    for source in manifest.get("sources", []):
        if source.get("licence_status") != "confirmed":
            raise ValueError(f"Source licence is unconfirmed: {source.get('source_id')}")
        for field in ("licence_name", "kaggle_license_name", "attribution", "reviewed_sha256", "allowed_files"):
            if not source.get(field):
                raise ValueError(f"Confirmed source is missing {field}: {source.get('source_id')}")


def package_snapshot(manifest_path: Path, source_dir: Path, output_dir: Path) -> list[Path]:
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    validate_manifest(manifest)
    output_dir.mkdir(parents=True, exist_ok=True)
    packaged = []
    for source in manifest["sources"]:
        for name in source["allowed_files"]:
            src = source_dir / name
            if not src.is_file():
                raise FileNotFoundError(src)
            expected = source["reviewed_sha256"].get(name)
            actual = hashlib.sha256(src.read_bytes()).hexdigest()
            if expected != actual:
                raise ValueError(f"File differs from reviewed provenance: {name}")
            dst = output_dir / name
            shutil.copy2(src, dst)
            packaged.append(dst)
    checksums = {
        path.relative_to(output_dir).as_posix(): hashlib.sha256(path.read_bytes()).hexdigest()
        for path in packaged
    }
    (output_dir / "snapshot-manifest.json").write_text(
        json.dumps({"sources": manifest["sources"], "sha256": checksums}, indent=2) + "\n",
        encoding="utf-8",
    )
    return packaged
```

- [ ] **Step 4: Record the authoritative licence evidence and select the source path**

The decision document must record:

- NSW ArcGIS item ID `99b11f8af9444737b3f484dd7334d671`;
- the exact official URL checked and retrieval date;
- `Terms and Conditions: Creative Common`, empty `licenseInfo`, and absent licence version;
- the Data.NSW NPWS page and its stated Creative Commons Attribution licence;
- decision `A`: exact NSW RFS licence confirmed with attribution, or decision `B`: NPWS replacement and full rerun required.

Do not set `licence_status` to `confirmed` from the ambiguous phrase alone. If no authoritative exact NSW RFS licence is already available when Task 1 executes, select decision `B` immediately and rerun with NPWS. Do not contact a data custodian or other external party unless Tuan separately authorises that outreach.

Task 1 must finish, including any NPWS rerun and its new reviewed hashes/invariants, before Tasks 2-4 begin. This prevents public analysis or notebook copy from being built around a source that cannot be packaged.

- [ ] **Step 5: Run licence tests**

Run: `python3 -m pytest llm-wiki/02-subjects/36126-innovation-lab-research-project/notebooks/active-fire-kaggle/tests/test_package_snapshot.py -q`

Expected: PASS.

- [ ] **Step 6: Commit the licence gate**

```bash
git add llm-wiki/02-subjects/36126-innovation-lab-research-project/notebooks/active-fire-kaggle/package_snapshot.py llm-wiki/02-subjects/36126-innovation-lab-research-project/notebooks/active-fire-kaggle/licence-manifest.json llm-wiki/02-subjects/36126-innovation-lab-research-project/notebooks/active-fire-kaggle/tests/test_package_snapshot.py llm-wiki/02-subjects/36126-innovation-lab-research-project/sources/data/nsw-fire-history-licence-decision.md
git commit -m "feat(research): enforce public data licence gate"
```

---

### Task 2: Build deterministic public analysis helpers

**Files:**
- Create: `llm-wiki/02-subjects/36126-innovation-lab-research-project/notebooks/active-fire-kaggle/public_analysis.py`
- Create: `llm-wiki/02-subjects/36126-innovation-lab-research-project/notebooks/active-fire-kaggle/tests/test_public_analysis.py`
- Reuse: `llm-wiki/02-subjects/36126-innovation-lab-research-project/notebooks/active-fire-pilot/run_pilot.py`

**Interfaces:**
- Consumes: exact and buffered `matched_hotspots.csv` tables and reviewed invariant JSON.
- Produces: `headline_summary(exact: DataFrame, buffered: DataFrame) -> dict`, `sensor_summary(matches: DataFrame) -> DataFrame`, `event_concentration(matches: DataFrame) -> DataFrame`, `deterministic_display_sample(frame: DataFrame, size: int, seed: int = 36126) -> DataFrame`, and `compare_refresh(reviewed: dict, refreshed: dict) -> DataFrame`.

- [ ] **Step 1: Write failing analysis tests**

```python
def test_headline_summary_uses_unresolved_language():
    result = headline_summary(exact_fixture(), buffered_fixture())
    assert result["buffered_unresolved"] == 3
    assert "false_positive" not in result


def test_display_sample_is_deterministic():
    frame = pd.DataFrame({"id": range(100)})
    first = deterministic_display_sample(frame, 10, seed=36126)
    second = deterministic_display_sample(frame, 10, seed=36126)
    pd.testing.assert_frame_equal(first, second)


def test_refresh_comparison_flags_drift_without_raising():
    comparison = compare_refresh({"total_hotspots": 10}, {"total_hotspots": 11})
    assert comparison.loc[0, "status"] == "changed"
```

- [ ] **Step 2: Verify tests fail**

Run: `python3 -m pytest llm-wiki/02-subjects/36126-innovation-lab-research-project/notebooks/active-fire-kaggle/tests/test_public_analysis.py -q`

Expected: FAIL because the analysis module does not exist.

- [ ] **Step 3: Implement minimal analysis functions**

Use full-data calculations for all metrics. Restrict sampling to display frames. Compute rates as `matched / sensor_total`, preserve `spatial_only` separately, and never rename `unmatched` to a negative class.

- [ ] **Step 4: Add reviewed-snapshot invariant checking**

```python
REVIEWED_RFS_INVARIANTS = {
    "total_hotspots": 19849,
    "fire_event_count": 14,
    "exact_matches": 2878,
    "buffered_matches": 3385,
    "buffered_unresolved": 16461,
}


def assert_snapshot_invariants(actual: dict, expected: dict) -> None:
    differences = {key: (expected[key], actual.get(key)) for key in expected if actual.get(key) != expected[key]}
    if differences:
        raise AssertionError(f"Snapshot invariants changed: {differences}")
```

Store a new invariant file if Task 1 selects NPWS. Do not reuse `REVIEWED_RFS_INVARIANTS` with NPWS data.

- [ ] **Step 5: Run existing and new analysis tests**

Run: `python3 -m pytest llm-wiki/02-subjects/36126-innovation-lab-research-project/notebooks/active-fire-pilot/tests llm-wiki/02-subjects/36126-innovation-lab-research-project/notebooks/active-fire-kaggle/tests/test_public_analysis.py -q`

Expected: PASS.

- [ ] **Step 6: Commit deterministic analysis**

```bash
git add llm-wiki/02-subjects/36126-innovation-lab-research-project/notebooks/active-fire-kaggle/public_analysis.py llm-wiki/02-subjects/36126-innovation-lab-research-project/notebooks/active-fire-kaggle/tests/test_public_analysis.py
git commit -m "feat(research): add public pilot analysis helpers"
```

---

### Task 3: Add accessible, reproducible visualisations

**Files:**
- Create: `llm-wiki/02-subjects/36126-innovation-lab-research-project/notebooks/active-fire-kaggle/public_visuals.py`
- Create: `llm-wiki/02-subjects/36126-innovation-lab-research-project/notebooks/active-fire-kaggle/tests/test_public_visuals.py`

**Interfaces:**
- Consumes: pandas summary frames and deterministic map-display frames from Task 2.
- Produces: `plot_sensor_composition(frame: DataFrame) -> Figure`, `plot_match_rates(frame: DataFrame) -> Figure`, `plot_confidence_by_algorithm(frame: DataFrame) -> Figure`, `plot_event_concentration(frame: DataFrame) -> Figure`, and `plot_pilot_map(hotspots: DataFrame, polygons: list[dict], displayed_n: int) -> Figure`.

- [ ] **Step 1: Write failing visual-contract tests**

```python
def test_match_rate_chart_labels_denominators():
    figure = plot_match_rates(sensor_fixture())
    labels = [text.get_text() for text in figure.axes[0].texts]
    assert any("n=" in label for label in labels)


def test_map_caption_discloses_display_sample():
    figure = plot_pilot_map(hotspot_fixture(), polygon_fixture(), displayed_n=2500)
    assert "2,500" in figure.axes[0].get_title()
```

- [ ] **Step 2: Verify visual tests fail**

Run: `MPLBACKEND=Agg python3 -m pytest llm-wiki/02-subjects/36126-innovation-lab-research-project/notebooks/active-fire-kaggle/tests/test_public_visuals.py -q`

Expected: FAIL because `public_visuals.py` does not exist.

- [ ] **Step 3: Implement the five figures**

Use the Okabe-Ito categorical colours `#0072B2`, `#E69F00`, `#CC79A7`, and `#999999`, white chart backgrounds, dark text, explicit denominators, and `tight_layout()`. Use deterministic display sampling only for the map; calculate all plotted summaries from full data. Add a test using `colorspacious` to simulate 100% protanomaly and deuteranomaly and require a minimum pairwise CIE Lab colour distance of 10 for the selected series colours.

- [ ] **Step 4: Save test renders and inspect them**

Run: `MPLBACKEND=Agg python3 -m pytest llm-wiki/02-subjects/36126-innovation-lab-research-project/notebooks/active-fire-kaggle/tests/test_public_visuals.py -q`

Expected: PASS and test figures saved under `tmp/active-fire-kaggle-figures/` for visual review.

- [ ] **Step 5: Commit visualisations**

```bash
git add llm-wiki/02-subjects/36126-innovation-lab-research-project/notebooks/active-fire-kaggle/public_visuals.py llm-wiki/02-subjects/36126-innovation-lab-research-project/notebooks/active-fire-kaggle/tests/test_public_visuals.py
git commit -m "feat(research): add public pilot visualisations"
```

---

### Task 4: Generate the six-section public notebook

**Files:**
- Create: `llm-wiki/02-subjects/36126-innovation-lab-research-project/notebooks/active-fire-kaggle/build_notebook.py`
- Create: `llm-wiki/02-subjects/36126-innovation-lab-research-project/notebooks/active-fire-kaggle/requirements-public.txt`
- Create: `llm-wiki/02-subjects/36126-innovation-lab-research-project/notebooks/active-fire-kaggle/tests/test_notebook_contract.py`
- Generate and later execute in place: `llm-wiki/02-subjects/36126-innovation-lab-research-project/notebooks/active-fire-kaggle/nsw-active-fire-reliability-pilot.ipynb`

**Interfaces:**
- Consumes: Task 1 snapshot contract and Task 2/3 public helpers.
- Produces: `build_notebook(output_path: Path, snapshot_slug: str) -> Path` and a valid notebook with exactly six H2 narrative sections.

- [ ] **Step 1: Write failing notebook-contract tests**

```python
EXPECTED_SECTIONS = [
    "1. Project overview",
    "2. Data and methodology",
    "3. Results",
    "4. Reliability analysis",
    "5. Research implications",
    "6. Reproducibility",
]


def test_notebook_has_six_public_sections(tmp_path):
    path = build_notebook(tmp_path / "pilot.ipynb", "tuannm3812/nsw-active-fire-pilot-snapshot")
    notebook = nbformat.read(path, as_version=4)
    headings = [cell.source.removeprefix("## ") for cell in notebook.cells if cell.cell_type == "markdown" and cell.source.startswith("## ")]
    assert headings == EXPECTED_SECTIONS


def test_notebook_defaults_to_snapshot_cpu_mode(tmp_path):
    path = build_notebook(tmp_path / "pilot.ipynb", "tuannm3812/nsw-active-fire-pilot-snapshot")
    source = "\n".join(cell.source for cell in nbformat.read(path, as_version=4).cells)
    assert 'EXECUTION_MODE = "snapshot"' in source
    assert "enable_gpu" not in source
```

- [ ] **Step 2: Verify notebook-contract tests fail**

Run: `python3 -m pytest llm-wiki/02-subjects/36126-innovation-lab-research-project/notebooks/active-fire-kaggle/tests/test_notebook_contract.py -q`

Expected: FAIL because the builder does not exist.

- [ ] **Step 3: Implement the notebook builder**

Build cells in this order:

1. Title, scope, safety/interpretation callout
2. Imports and `EXECUTION_MODE = "snapshot"`
3. Six H2 sections from the approved design
4. Data validation and snapshot invariant cell
5. Tables and five figures using Task 2/3 helpers
6. Live-refresh cell guarded by `if EXECUTION_MODE == "live_refresh"`
7. Environment/provenance table and public-source attribution

Do not mention a supervisor, university assessment, private repository, or local path.

- [ ] **Step 4: Generate and structurally validate the notebook**

Run:

```bash
python3 llm-wiki/02-subjects/36126-innovation-lab-research-project/notebooks/active-fire-kaggle/build_notebook.py
python3 -m pytest llm-wiki/02-subjects/36126-innovation-lab-research-project/notebooks/active-fire-kaggle/tests/test_notebook_contract.py -q
```

Expected: generated notebook parses as nbformat v4 and tests PASS.

- [ ] **Step 5: Commit notebook source and dependency manifest**

```bash
git add llm-wiki/02-subjects/36126-innovation-lab-research-project/notebooks/active-fire-kaggle/build_notebook.py llm-wiki/02-subjects/36126-innovation-lab-research-project/notebooks/active-fire-kaggle/requirements-public.txt llm-wiki/02-subjects/36126-innovation-lab-research-project/notebooks/active-fire-kaggle/tests/test_notebook_contract.py llm-wiki/02-subjects/36126-innovation-lab-research-project/notebooks/active-fire-kaggle/nsw-active-fire-reliability-pilot.ipynb
git commit -m "feat(research): build public Kaggle pilot notebook"
```

---

### Task 5: Execute and audit the complete local artifact

**Files:**
- Create: `llm-wiki/02-subjects/36126-innovation-lab-research-project/notebooks/active-fire-kaggle/audit_public_artifact.py`
- Create: `llm-wiki/02-subjects/36126-innovation-lab-research-project/notebooks/active-fire-kaggle/tests/test_public_audit.py`
- Create: `llm-wiki/02-subjects/36126-innovation-lab-research-project/notebooks/active-fire-kaggle/README.md`
- Modify: `llm-wiki/02-subjects/36126-innovation-lab-research-project/README.md`

**Interfaces:**
- Consumes: executed notebook, packaged snapshot, Kaggle metadata, and forbidden-pattern configuration.
- Produces: `audit_artifact(paths: list[Path]) -> list[str]`, returning an empty list only when privacy and claim-language checks pass.

- [ ] **Step 1: Write failing audit tests**

```python
def test_audit_rejects_private_content(tmp_path):
    artifact = tmp_path / "bad.ipynb"
    artifact.write_text('{"note": "Dr Arnick /Users/example"}', encoding="utf-8")
    findings = audit_artifact([artifact])
    assert any("internal name" in finding for finding in findings)
    assert any("absolute path" in finding for finding in findings)


def test_claim_audit_rejects_unscoped_accuracy(tmp_path):
    artifact = tmp_path / "bad.md"
    artifact.write_text("The detector accuracy is 17.1%.", encoding="utf-8")
    assert any("accuracy" in finding for finding in audit_artifact([artifact]))
```

- [ ] **Step 2: Verify audit tests fail**

Run: `python3 -m pytest llm-wiki/02-subjects/36126-innovation-lab-research-project/notebooks/active-fire-kaggle/tests/test_public_audit.py -q`

Expected: FAIL because the audit module does not exist.

- [ ] **Step 3: Implement privacy and claim-language auditing**

Scan text extracted from notebook cells and outputs plus JSON/Markdown/CSV metadata. Reject credential keys, emails, phone numbers, `/Users/`, Google Drive paths, internal names, and unreviewed uses of `accuracy`, `false alarm`, `false positive`, `detection rate`, `miss rate`, or `ground truth`. Maintain a small allowlist only for reviewed phrases such as `positional accuracy` and `not a detector-accuracy evaluation`.

- [ ] **Step 4: Execute the snapshot notebook from a clean state**

Run:

```bash
python3 -m jupyter nbconvert --to notebook --execute --inplace --ExecutePreprocessor.timeout=600 llm-wiki/02-subjects/36126-innovation-lab-research-project/notebooks/active-fire-kaggle/nsw-active-fire-reliability-pilot.ipynb
python3 -m jupyter nbconvert --to html llm-wiki/02-subjects/36126-innovation-lab-research-project/notebooks/active-fire-kaggle/nsw-active-fire-reliability-pilot.ipynb --output-dir output/kaggle/active-fire-pilot/review
```

Expected: every cell completes and HTML is created.

- [ ] **Step 5: Run all tests and audits**

Run:

```bash
python3 -m pytest llm-wiki/02-subjects/36126-innovation-lab-research-project/notebooks/active-fire-pilot/tests llm-wiki/02-subjects/36126-innovation-lab-research-project/notebooks/active-fire-kaggle/tests -q
python3 llm-wiki/02-subjects/36126-innovation-lab-research-project/notebooks/active-fire-kaggle/audit_public_artifact.py llm-wiki/02-subjects/36126-innovation-lab-research-project/notebooks/active-fire-kaggle/nsw-active-fire-reliability-pilot.ipynb output/kaggle/active-fire-pilot
```

Expected: tests PASS and audit reports zero findings.

- [ ] **Step 6: Visually inspect the complete rendered HTML**

Check all six sections, table contrast, chart captions and denominators, deterministic map caption, source attributions, absence of internal material, and the interpretation of 17.1%. Record the inspection result in the collaboration log.

- [ ] **Step 7: Document usage and commit the locally verified artifact**

```bash
git add llm-wiki/02-subjects/36126-innovation-lab-research-project/notebooks/active-fire-kaggle llm-wiki/02-subjects/36126-innovation-lab-research-project/README.md
git commit -m "docs(research): document public pilot notebook workflow"
```

---

### Task 6: Prepare private Kaggle metadata and credential-safe upload

**Files:**
- Create: `llm-wiki/02-subjects/36126-innovation-lab-research-project/notebooks/active-fire-kaggle/kaggle/dataset-metadata.json`
- Create: `llm-wiki/02-subjects/36126-innovation-lab-research-project/notebooks/active-fire-kaggle/kaggle/kernel-metadata.json`
- Create: `llm-wiki/02-subjects/36126-innovation-lab-research-project/notebooks/active-fire-kaggle/upload_private.py`
- Create: `llm-wiki/02-subjects/36126-innovation-lab-research-project/notebooks/active-fire-kaggle/tests/test_kaggle_metadata.py`

**Interfaces:**
- Consumes: packaged snapshot, executed notebook, metadata templates, and a credential path supplied only at runtime.
- Produces: `validate_private_metadata(dataset: dict, kernel: dict) -> None` and `upload_private(credentials_path: Path, staging_dir: Path) -> dict`.

- [ ] **Step 1: Write failing private-metadata tests**

```python
def test_kernel_is_private_cpu_and_snapshot_first():
    metadata = json.loads(KERNEL_METADATA.read_text())
    assert metadata["enable_gpu"] is False
    assert metadata["enable_internet"] is False
    assert metadata["is_private"] is True


def test_dataset_is_private_and_has_no_collaborators():
    metadata = json.loads(DATASET_METADATA.read_text())
    assert metadata["isPrivate"] is True
    assert metadata.get("collaborators", []) == []


def test_dataset_licence_matches_confirmed_manifest():
    dataset = json.loads(DATASET_METADATA.read_text())
    manifest = json.loads(LICENCE_MANIFEST.read_text())
    confirmed = {source["kaggle_license_name"] for source in manifest["sources"]}
    assert dataset["licenses"][0]["name"] in confirmed
```

- [ ] **Step 2: Verify metadata tests fail**

Run: `python3 -m pytest llm-wiki/02-subjects/36126-innovation-lab-research-project/notebooks/active-fire-kaggle/tests/test_kaggle_metadata.py -q`

Expected: FAIL because metadata files do not exist.

- [ ] **Step 3: Implement metadata and safe credential handling**

The upload script must:

- accept `--credentials` and never print its content;
- load JSON only to validate the expected username;
- create a `TemporaryDirectory`, write a mode-`0600` temporary `kaggle.json`, and set `KAGGLE_CONFIG_DIR` only for child commands;
- invoke dataset creation/version with private metadata;
- invoke kernel push with `is_private: true`, `enable_gpu: false`, and `enable_internet: false`;
- delete the temporary directory automatically; and
- return artifact references and statuses without returning the key.

- [ ] **Step 4: Test with a fake credential and mocked subprocess**

Assert that command arguments and captured output never contain the fake key and that the temporary credential path no longer exists after completion.

- [ ] **Step 5: Run metadata and upload-unit tests**

Run: `python3 -m pytest llm-wiki/02-subjects/36126-innovation-lab-research-project/notebooks/active-fire-kaggle/tests/test_kaggle_metadata.py -q`

Expected: PASS.

- [ ] **Step 6: Commit private-upload tooling**

```bash
git add llm-wiki/02-subjects/36126-innovation-lab-research-project/notebooks/active-fire-kaggle/kaggle llm-wiki/02-subjects/36126-innovation-lab-research-project/notebooks/active-fire-kaggle/upload_private.py llm-wiki/02-subjects/36126-innovation-lab-research-project/notebooks/active-fire-kaggle/tests/test_kaggle_metadata.py
git commit -m "feat(research): add private Kaggle upload workflow"
```

---

### Task 7: Claude review gate and private Kaggle deployment

**Files:**
- Append: `llm-wiki/02-subjects/36126-innovation-lab-research-project/agent-collaboration-log.md`
- Use generated: `output/kaggle/active-fire-pilot/`

**Interfaces:**
- Consumes: zero-finding audit report, passing tests, rendered notebook review, Claude findings, and Tuan's credential file supplied at runtime.
- Produces: a private Kaggle dataset, a private Kaggle notebook version, verified private status, and a review handoff URL/reference.

- [ ] **Step 1: Request Claude's private-ready artifact review**

Append the exact local notebook, rendered HTML, audit result, test result, licence decision, and the five requested review dimensions to the collaboration log. Pause deployment until Claude records findings or `no blocking findings`.

- [ ] **Step 2: Evaluate and resolve Claude's findings**

For each finding, record `accepted`, `partially accepted`, or `rejected`, with evidence. Rerun the affected tests, notebook execution, audit, and visual inspection after accepted changes.

- [ ] **Step 3: Run the final pre-upload gate**

Run:

```bash
python3 -m pytest llm-wiki/02-subjects/36126-innovation-lab-research-project/notebooks/active-fire-pilot/tests llm-wiki/02-subjects/36126-innovation-lab-research-project/notebooks/active-fire-kaggle/tests -q
python3 llm-wiki/02-subjects/36126-innovation-lab-research-project/notebooks/active-fire-kaggle/audit_public_artifact.py output/kaggle/active-fire-pilot
```

Expected: all tests PASS, zero audit findings, exact licence gate PASS.

- [ ] **Step 4: Upload privately using the account-specific credential**

Run the upload script with the account-specific credential file supplied as the runtime `--credentials` argument. The credential must remain outside this repository, and neither its path nor content may appear in a staged or uploaded artifact, checked-in document, notebook cell, output, or log.

- [ ] **Step 5: Verify remote state**

Use the Kaggle API/CLI to confirm:

- dataset owner is `tuannm3812`;
- dataset visibility is private;
- kernel owner is `tuannm3812`;
- kernel visibility is private;
- GPU and internet are disabled;
- kernel execution completed successfully; and
- no collaborators are present.

- [ ] **Step 6: Record deployment without publishing**

Append artifact references, version numbers, execution status, and privacy verification to the collaboration log. Do not change visibility to public.

- [ ] **Step 7: Commit the deployment record**

```bash
git add llm-wiki/02-subjects/36126-innovation-lab-research-project/agent-collaboration-log.md
git commit -m "docs(research): record private Kaggle pilot review"
```

---

## Final verification checklist

- [ ] The exact source licence and attribution are recorded for every uploaded input or derivative.
- [ ] Existing pilot tests and all new Kaggle-package tests pass.
- [ ] Snapshot results are generated from data and match the selected reviewed invariant set.
- [ ] Live refresh is opt-in and handles source drift without snapshot assertion failure.
- [ ] The notebook contains exactly six major public sections.
- [ ] The map and any sampled displays are deterministic and disclose displayed sample sizes.
- [ ] Every chart shows counts or denominators and uses accessible contrast.
- [ ] The claim-language audit finds no unscoped detector-performance statement.
- [ ] The privacy audit finds no internal names, contact details, credentials, local paths, or supervision content.
- [ ] Direct dependency versions and source provenance are visible.
- [ ] Claude has no unresolved blocking review finding.
- [ ] Kaggle dataset and notebook are private, CPU-only, internet-off by default, and owner-only.
- [ ] No public visibility change has been made.

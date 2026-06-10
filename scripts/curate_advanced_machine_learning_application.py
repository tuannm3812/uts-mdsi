from __future__ import annotations

import contextlib
import csv
import io
import re
import warnings
import zipfile
from collections import Counter, defaultdict
from pathlib import Path
from xml.etree import ElementTree

import nbformat
from pypdf import PdfReader


REPO_ROOT = Path(__file__).resolve().parents[1]
SUBJECT = REPO_ROOT / "llm-wiki" / "02-subjects" / "36120-advanced-machine-learning-application"
MANIFEST = REPO_ROOT / "llm-wiki" / "00-admin" / "drive-import-manifest.csv"
LECTURE_RAW = SUBJECT / "lectures" / "raw" / "advml_slides_25sp"
NOTEBOOK_RAW = SUBJECT / "notebooks" / "raw" / "advmla_notebooks"
ASSIGNMENT_RAW = SUBJECT / "assignments" / "raw" / "advml_assignments"
SOURCE_RAW = SUBJECT / "sources" / "raw"


SESSION_TOPICS = {
    1: "Problem Framing and Advanced ML Workflow",
    2: "Classical Learners, Baselines, and Feature Design",
    3: "Model Selection, Tuning, and Evaluation Strategy",
    4: "Binary Classification and Imbalance-Sensitive Methods",
    5: "Time-Series and Weather Data Preparation",
    6: "Ensemble, Calibration, and Performance Diagnostics",
    7: "Robust Modelling Patterns and Interpretation",
    8: "Assessment-Linked Integration and Deployment Notes",
}

SESSION_OBJECTIVES = {
    1: [
        "Define the assessment-relevant modelling problem and output type.",
        "Set up a reproducible baseline and identify major uncertainty sources.",
    ],
    2: [
        "Compare preprocessing strategies for structured tabular modelling.",
        "Identify why feature representation can dominate model choice and tuning.",
    ],
    3: [
        "Explain cross-validation and holdout design for fair model comparison.",
        "Interpret precision, recall, and threshold effects for decision tasks.",
    ],
    4: [
        "Analyse class imbalance and threshold adjustments in binary outputs.",
        "Translate model scores into decision-ready recommendations.",
    ],
    5: [
        "Inspect weather-style temporal features and leakage risks.",
        "Map stationarity and time ordering constraints into model design.",
    ],
    6: [
        "Compare ensemble methods for variance and bias control.",
        "Use calibration and probability checks before interpretation.",
    ],
    7: [
        "Evaluate model outputs against assumptions, feature drift, and failure modes.",
        "Connect notebooks to reproducible experiment reporting.",
    ],
    8: [
        "Prepare an assessment-ready evidence map from assignments and sessions.",
        "Summarise trade-offs and practical risks for final submission.",
    ],
}

CONCEPTS = {
    "feature engineering": ["feature", "engineer", "encoding", "scaling", "normalization", "normalise", "normalization"],
    "model evaluation": ["accuracy", "precision", "recall", "f1", "roc", "auc", "metrics", "baseline", "validation", "cross-validation", "confusion"],
    "overfitting": ["overfitting", "underfitting", "variance", "bias", "generalization", "train", "test", "leakage"],
    "hyperparameter tuning": ["hyperparameter", "grid", "search", "tune", "max_depth", "learning_rate", "n_estimators", "cv"],
    "ensemble": ["ensemble", "random_forest", "xgboost", "gradient", "boost", "bagging", "stacking"],
    "probability calibration": ["calibration", "sigmoid", "isotonic", "predict_proba", "threshold", "decision threshold"],
    "class imbalance": ["imbalance", "class weight", "roc", "precision", "recall", "pr curve", "smote"],
    "data leakage": ["leakage", "leaked", "future", "target", "split", "chronological", "time"],
    "reproducibility": ["seed", "random", "reproducible", "pipeline", "shuffle", "fold", "repeat"],
    "time-series": ["time", "lag", "rolling", "seasonal", "temporal", "timestamp", "series", "trend"],
    "experiment tracking": ["experiment", "run", "baseline", "tracking", "artifact", "model", "metrics"],
    "evaluation protocol": ["validation set", "holdout", "cross validation", "k-fold", "train-test split"],
}

DEFINITIONS = {
    "feature engineering": "Transforming raw inputs into forms that improve model signal and stability.",
    "model evaluation": "Measuring model quality using metrics aligned to a defined objective and failure cost.",
    "overfitting": "A pattern where a model performs well on training data but poorly generalizes.",
    "hyperparameter tuning": "Systematic selection of algorithm settings that are not learned directly from gradients.",
    "ensemble": "Combining multiple models to improve robustness and reduce variance.",
    "probability calibration": "Adjusting predicted probabilities to better reflect true outcome frequencies.",
    "class imbalance": "When target classes are not equally represented and metrics can mislead.",
    "data leakage": "Including information unavailable at prediction time, producing inflated validation scores.",
    "reproducibility": "Ability to re-run an experiment and obtain consistent outcomes.",
    "time-series": "Data indexed by time where ordering and dependencies constrain validation strategy.",
    "experiment tracking": "Systematic logging of setup, code, and outputs for review and audit.",
    "evaluation protocol": "Consistent strategy for splits, folds, and metric reporting.",
}


def clean(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def read_manifest_counts() -> Counter:
    counts = Counter()
    if not MANIFEST.exists():
        return counts
    with MANIFEST.open(newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            if row.get("repo_subject") != SUBJECT.name:
                continue
            counts[row["target_bucket"]] += 1
    return counts


def xml_text(xml: bytes) -> str:
    root = ElementTree.fromstring(xml)
    return " ".join(node.text for node in root.iter() if node.text)


def extract_docx(path: Path, max_chars: int = 12000) -> str:
    try:
        chunks = []
        with zipfile.ZipFile(path) as archive:
            for name in sorted(archive.namelist()):
                if name.startswith("word/") and name.endswith(".xml"):
                    chunks.append(xml_text(archive.read(name)))
        return clean("\n".join(chunks))[:max_chars]
    except Exception as exc:
        return f"[DOCX extraction failed: {exc}]"


def extract_pdf(path: Path, max_chars: int = 12000) -> str:
    try:
        stderr = io.StringIO()
        with contextlib.redirect_stderr(stderr), warnings.catch_warnings():
            warnings.simplefilter("ignore")
            reader = PdfReader(str(path))
            return clean("\n".join((page.extract_text() or "") for page in reader.pages[:14]))[:max_chars]
    except Exception as exc:
        return f"[PDF extraction failed: {exc}]"


def extract_notebook(path: Path, max_chars: int = 12000) -> str:
    try:
        nb = nbformat.read(path, as_version=4)
        chunks = []
        for cell in nb.cells:
            source = str(cell.source)
            if cell.cell_type == "markdown":
                chunks.append(source)
            elif cell.cell_type == "code":
                imports = "\n".join(line for line in source.splitlines() if line.startswith(("import ", "from ")))
                comments = "\n".join(line.strip("# ") for line in source.splitlines() if line.strip().startswith("#"))
                calls = "\n".join(
                    line.strip()
                    for line in source.splitlines()
                    if any(term in line.lower() for term in ["fit(", "predict(", "score(", "train_test_split", "pipeline", "GridSearch", "cross_val"])
                )
                if imports:
                    chunks.append("Code imports:\n" + imports)
                if comments:
                    chunks.append(comments)
                if calls:
                    chunks.append("Code signals:\n" + calls)
        return clean("\n".join(chunks))[:max_chars]
    except Exception as exc:
        return f"[Notebook extraction failed: {exc}]"


def extract_text(path: Path, max_chars: int = 12000) -> str:
    suffix = path.suffix.lower()
    if suffix == ".pdf":
        return extract_pdf(path, max_chars=max_chars)
    if suffix == ".ipynb":
        return extract_notebook(path, max_chars=max_chars)
    if suffix == ".docx":
        return extract_docx(path, max_chars=max_chars)
    if suffix in {".md", ".txt", ".py"}:
        return clean(path.read_text(encoding="utf-8", errors="ignore"))[:max_chars]
    return ""


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def bullet(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items)


def parse_session_from_filename(name: str) -> int | None:
    match = re.search(r"(?:lecture|lec)[-_\\s]*0*([0-9]+)", name, flags=re.I)
    if not match:
        return None
    session = int(match.group(1))
    return session if 1 <= session <= 12 else None


def parse_lab_and_exercise(name: str) -> tuple[int, int, str]:
    normalized = name.lower().replace("-", "_")
    match = re.search(r"lab0*([0-9]+).*ex0*([0-9]+)", normalized)
    if match:
        return int(match.group(1)), int(match.group(2)), normalized
    if "lab" in normalized:
        m = re.search(r"lab0*([0-9]+)", normalized)
        return (int(m.group(1)), 0, normalized) if m else (0, 0, normalized)
    return 0, 0, normalized


def detect_assessment(path: Path) -> str | None:
    lower = str(path).lower()
    if "advmla_at1" in lower:
        return "01"
    if "advmla_at2" in lower:
        return "02"
    if "advmla_at3" in lower:
        return "03"
    return None


def score_terms(text: str) -> Counter:
    lowered = text.lower()
    scores = Counter()
    for concept, terms in CONCEPTS.items():
        for term in terms:
            scores[concept] += lowered.count(term)
    return scores


def keywords(text: str, n: int = 12) -> list[str]:
    words = re.findall(r"[A-Za-z][A-Za-z0-9_+-]{3,}", text.lower())
    stop = {
        "this", "that", "with", "from", "model", "session", "lecture", "learning",
        "file", "files", "source", "data", "using", "used", "result", "results",
        "code", "class", "model", "student", "group", "train", "test",
    }
    return [word for word, _ in Counter(w for w in words if w not in stop).most_common(n)]


def collect_lecture_sources() -> dict[int, list[dict[str, str]]]:
    by_session: dict[int, list[dict[str, str]]] = defaultdict(list)
    for path in sorted(LECTURE_RAW.rglob("*.pdf")):
        session = parse_session_from_filename(path.name)
        if session is None:
            continue
        by_session[session].append(
            {
                "type": "pdf",
                "path": str(path.relative_to(SUBJECT)),
                "text": extract_pdf(path),
            }
        )
    return by_session


def collect_notebook_sources() -> dict[int, list[dict[str, str]]]:
    by_lab: dict[int, list[dict[str, str]]] = defaultdict(list)
    for path in sorted(NOTEBOOK_RAW.rglob("*.ipynb")):
        lab, exercise, normalized = parse_lab_and_exercise(path.name)
        if lab == 0:
            lab = 99
        source_key = f"Lab {lab:02d} Exercise {exercise:02d}" if exercise else f"Lab {lab:02d}"
        by_lab[lab].append(
            {
                "type": "ipynb",
                "path": str(path.relative_to(SUBJECT)),
                "text": extract_notebook(path),
                "order": source_key + "-" + normalized,
            }
        )
    return by_lab


def collect_assignments() -> dict[str, list[dict[str, str]]]:
    payloads: dict[str, list[dict[str, str]]] = defaultdict(list)
    for path in sorted(ASSIGNMENT_RAW.rglob("*")):
        if not path.is_file():
            continue
        at = detect_assessment(path)
        if not at:
            continue
        payloads[at].append(
            {
                "path": str(path.relative_to(SUBJECT)),
                "name": path.name,
                "ext": path.suffix.lower(),
                "text": extract_text(path, max_chars=2500),
            }
        )
    return payloads


def top_task_sources(payload: list[dict[str, str]]) -> list[str]:
    priority_exts = {".docx", ".gdoc", ".pdf", ".ipynb", ".md"}
    priorities = []
    for item in payload:
        path = item["path"]
        ext = item["ext"]
        if ext in priority_exts:
            priorities.append(path)
    return sorted(priorities)


def write_session_notes(by_session: dict[int, list[dict[str, str]]]) -> None:
    for session in sorted(by_session):
        sources = by_session[session]
        all_text = "\n".join(item["text"] for item in sources)
        concepts = [
            f"- {concept}: {DEFINITIONS.get(concept, 'Verify definition from source material.')}"
            for concept, count in score_terms(all_text).most_common()
            if count > 0
        ]
        source_lines = "\n".join(f"- `{item['path']}` ({item['type']})" for item in sources) or "- No matching lecture files detected."
        write(
            SUBJECT / "lectures" / f"session-{session:02d}.md",
            f"""---
type: lecture-note
subject: 36120-advanced-machine-learning-application
session: {session}
status: draft
---

# Session {session:02d} - {SESSION_TOPICS.get(session, f'Advanced ML Topic {session:02d}')}

## Source Files

{source_lines}

## Working Summary

This is a first-pass curated note generated from copied lecture PDFs and notebook-linked teaching materials. Verify all details against source files before using this for assessment.

## Study Objectives

{bullet(SESSION_OBJECTIVES.get(session, [f'Review session {session:02d} source files and validate modelling workflow.']))}

## Likely Concepts

{chr(10).join(concepts[:10]) if concepts else '- To be confirmed from source review.'}

## Extracted Keywords

{bullet(keywords(all_text))}

## What To Understand

- Which target variable and task type this lesson is designed for.
- The assumptions behind each model and split strategy.
- How metrics map to practical decisions.
- What risks could invalidate the reported results.

## Assessment Relevance

- Link this session to AT1/AT2/AT3 evidence using [the assignment evidence map](../assignments/evidence-map.md).
- Turn each high-signal slide section into a concise claim with source evidence.

## Revision Questions

- What is the modelling objective and what data constraints are explicit?
- Which evaluation metric is most honest for this task and why?
- What is a likely leakage source, and how would you prevent it?
- Which model choice is justified by this session’s assumptions?

## LLM Follow-Up Prompt

Using the source files listed above, expand this first-pass note into a precise study note with task examples, metric trade-offs, and assessment-relevant implications.
""",
        )


def write_glossary(by_session: dict[int, list[dict[str, str]]], by_lab: dict[int, list[dict[str, str]]]) -> None:
    text = "\n".join(item["text"] for sources in by_session.values() for item in sources)
    text += "\n" + "\n".join(item["text"] for sources in by_lab.values() for item in sources)
    rows = []
    for concept, score in score_terms(text).most_common():
        if score > 0:
            rows.append(f"| {concept} | {score} | {DEFINITIONS.get(concept, 'Add verified definition from source material.')} |")
    write(
        SUBJECT / "glossary.md",
        f"""---
type: glossary
subject: 36120-advanced-machine-learning-application
status: draft
---

# 36120 Advanced Machine Learning Application - Glossary

| Term | Evidence Count | Working Definition |
|---|---:|---|
{chr(10).join(rows)}

## Maintenance

- Replace working definitions with precise formulas, thresholds, and examples from slides and notebooks.
- Link durable terms to [Machine Learning](../../03-shared-concepts/machine-learning.md), [Python](../../03-shared-concepts/python.md), and [Statistics](../../03-shared-concepts/statistics.md).
""",
    )


def write_notebook_catalog(by_lab: dict[int, list[dict[str, str]]]) -> None:
    def lab_sort_key(item: tuple[int, list[dict[str, str]]]) -> tuple[int, str]:
        lab, entries = item
        return lab, entries[0].get("order", f"{lab:02d}")

    rows = []
    for lab, entries in sorted(by_lab.items(), key=lab_sort_key):
        key = "Unmapped Lab" if lab == 99 else f"Lab {lab:02d}"
        items = sorted(entries, key=lambda i: i.get("order", ""))
        source_lines = "\n".join(f"  - `{item['path']}` ({item['type']})" for item in items)
        rows.append(f"### {key}\n\n{source_lines}")

    write(
        SUBJECT / "notebooks" / "lab-notes.md",
        f"""---
type: notebook-catalog
subject: 36120-advanced-machine-learning-application
status: draft
---

# 36120 Advanced Machine Learning Application - Notebook Notes

## Scope

This index links notebook files copied into `notebooks/raw` to the lab sequence used in this subject.

{chr(10).join(rows) if rows else "- No notebook sources were detected."}

## Maintenance

- Add a short hand-crafted note for each lab where you keep key implementation learnings.
- Keep source mappings and key output checks next to each lab block.
""",
    )

    notebooks_readme = SUBJECT / "notebooks" / "README.md"
    text = notebooks_readme.read_text(encoding="utf-8")
    if "## Curated Notebook Notes" in text:
        text = text.split("## Curated Notebook Notes", 1)[0].rstrip()
    write(notebooks_readme, text.rstrip() + "\n\n## Curated Notebook Notes\n\n- [Lab Notes](lab-notes.md)\n")


def write_assignment_pages(payloads: dict[str, list[dict[str, str]]]) -> None:
    at_profiles = {
        "01": {
            "title": "AT1",
            "description": "AT1 appears to be the first applied assignment with baseline modelling and experimentation workflow.",
            "sessions": "Sessions 1-4",
        },
        "02": {
            "title": "AT2",
            "description": "AT2 appears to focus on model comparison and forecasting style modelling workflow.",
            "sessions": "Sessions 4-7",
        },
        "03": {
            "title": "AT3",
            "description": "AT3 appears to be project-integration style reporting where all evidence is synthesised.",
            "sessions": "Sessions 5-8",
        },
    }
    for at in ["01", "02", "03"]:
        profile = at_profiles[at]
        sources = sorted(payloads.get(at, []), key=lambda item: item["path"])
        if sources:
            task_docs = top_task_sources(sources)
            top_items = "\n".join(f"- `{item['path']}` ({item['ext'] or 'file'})" for item in sources[:80])
            task_hint = task_docs[0] if task_docs else sources[0]["path"]
        else:
            task_hint = "No source files were detected automatically for this assessment."
            top_items = "- No copied source files were detected for this assessment."

        write(
            SUBJECT / "assignments" / f"at{int(at)}.md",
            f"""---
type: assessment
subject: 36120-advanced-machine-learning-application
code: 36120
status: planning
---

# 36120 AT{int(at)}

## Official Task

- Source task file: `{task_hint}`
- Related sessions: {profile['sessions']}
- Suggested focus: {profile['description']}

## Evidence Sources

{top_items}

## Assignment Checklist

- [ ] Confirm task requirements and required deliverables are captured from official files.
- [ ] Link each task section to at least one source file and one session note.
- [ ] Verify evaluation setup and split strategy assumptions.
- [ ] Record key hyperparameters, metrics, and interpretation notes.
- [ ] Ensure all claims are tied to reproducible outputs.

## Working Plan

| Step | Output | Status |
|---|---|---|
| Read official task and constraints | Brief summary | Not started |
| Map required evidence | Source mapping table | Not started |
| Build draft response/analysis | Working draft | Not started |
| Validate with rubric and metrics | Evidence check | Not started |
| Final review | Submission-ready version | Not started |

## LLM Review Notes

- Ask for strict rubric checks against each checklist item.
- Request metric sanity checks for any improvement claim.
- Keep non-reproducible claims clearly marked.

## Final Verification

- [ ] Task requirements are fully interpreted and met.
- [ ] Source files are mapped to evidence claims.
- [ ] Data splits, random seeds, and model settings are stated.
- [ ] Results are interpreted with limitations and risk notes.
- [ ] Submission format aligns with the official brief.
""",
        )


def write_evidence_map(by_session: dict[int, list[dict[str, str]]], payloads: dict[str, list[dict[str, str]]]) -> None:
    session_rows = "\n".join(
        f"| Session {session:02d} | {SESSION_TOPICS.get(session, '')} | {len(sources)} | [note](../lectures/session-{session:02d}.md) |"
        for session, sources in sorted(by_session.items())
    )
    assignment_rows = "\n".join(
        f"| AT{at} | {len(payloads.get(at, []))} source files | [AT{at}](at{int(at)}.md) |"
        for at in ["01", "02", "03"]
    )
    write(
        SUBJECT / "assignments" / "evidence-map.md",
        f"""---
type: evidence-map
subject: 36120-advanced-machine-learning-application
status: draft
---

# 36120 Advanced Machine Learning Application - Evidence Map

## Session Evidence

| Session | Topic | Source Count | Curated Note |
|---|---|---:|---|
{session_rows}

## Assessment Evidence

| Assessment | Source File Count | Curated Task Note |
|---|---:|---|
{assignment_rows}

## Notes

- Prefer using source files listed in each AT page and map each claim to a session note for traceability.
- Keep notebook outputs and metrics as supporting artefacts where applicable.
""",
    )


def write_questions() -> None:
    concepts = [
        "- What is the difference between precision and recall, and when does each matter most?",
        "- How does class imbalance affect model selection and interpretation?",
        "- What is data leakage and how can it happen in time-based forecasting tasks?",
        "- How should you choose between precision-oriented and recall-oriented models in AT-like tasks?",
        "- What are practical checks for model reproducibility across reruns?",
        "- Why does an ensemble help and what are its failure modes?",
        "- How can session notes and notebook evidence be linked into AT reports?",
    ]
    concept_text = "\n".join(concepts)
    write(
        SUBJECT / "questions" / "revision-questions.md",
        "\n".join(
            [
                "---",
                "type: question-bank",
                "subject: 36120-advanced-machine-learning-application",
                "code: 36120",
                "status: draft",
                "---",
                "",
                "# 36120 Advanced Machine Learning Application - Revision Questions",
                "",
                "## Conceptual Questions",
                "",
                concept_text,
                "",
                "## Applied Questions",
                "",
                "- Build a reproducible training/evaluation loop for AT2 using only source materials.",
                "- Compare two models from the same session and justify the final choice using metrics.",
                "- Create a checklist for spotting leakage and invalid evaluation claims.",
                "- Design a short LLM prompt to inspect this assignment’s outputs for risk and bias.",
                "",
                "## Technical Questions",
                "",
                "- What preprocessing choices in the notebooks affect feature scale and model fairness?",
                "- How do you validate that metrics are computed on the correct split?",
                "- What notebook lines are most useful for reproducibility evidence?",
                "",
                "## LLM Drill Prompt",
                "",
                "Using the session notes, glossary, and evidence map, generate:",
                "- a 20-question exam set,",
                "- a model answer key with concise grading guidance,",
                "- and a checklist of common failure patterns for this subject.",
            ]
        ),
    )


def update_learning_map(by_session: dict[int, list[dict[str, str]]], payloads: dict[str, list[dict[str, str]]]) -> None:
    bucket_counts = read_manifest_counts()
    lecture_files = [p.name for p in sorted(LECTURE_RAW.glob("*.pdf"))]
    notebook_files = [p.name for p in sorted(NOTEBOOK_RAW.rglob("*.ipynb"))]
    source_files = [p.name for p in sorted(SOURCE_RAW.rglob("*.pdf"))] if SOURCE_RAW.exists() else []
    assignment_files = [
        item["path"]
        for at in ["01", "02", "03"]
        for item in sorted(payloads.get(at, []), key=lambda item: item["path"])
        if Path(item["path"]).suffix.lower() in {".pdf", ".docx", ".ipynb", ".md", ".txt", ".gdoc"}
    ]

    lines = [
        "---",
        "type: learning-map",
        "subject: 36120-advanced-machine-learning-application",
        "code: 36120",
        "semester: Sem2 2025 Spring",
        "status: active",
        "---",
        "",
        "# 36120 Advanced Machine Learning Application - Learning Map",
        "",
        "## Purpose",
        "",
        "Use this page as the curated entry point for the subject. Raw copied files are useful evidence, but this page should become the LLM-friendly map of what matters.",
        "",
        "## Core Focus",
        "",
        "- Advanced machine learning workflows and model selection",
        "- Reproducible experimentation and fair evaluation",
        "- Time-series and imbalance-aware modelling",
        "- Assessment evidence mapping and report quality",
        "",
        "## Connected Concepts",
        "",
        "- [Machine Learning](../../03-shared-concepts/machine-learning.md)",
        "- [Deep Learning](../../03-shared-concepts/deep-learning.md)",
        "- [Statistics](../../03-shared-concepts/statistics.md)",
        "",
        "## Study Workflow",
        "",
        "1. Review the lecture notes in [lectures](lectures/README.md).",
        "2. Convert session source material into concise notes and concept summaries.",
        "3. Link durable ideas to shared concepts and assessment requirements.",
        "4. Track AT evidence in [assignments](assignments/README.md) and [evidence map](assignments/evidence-map.md).",
        "5. Use [notebook notes](notebooks/lab-notes.md) for reproducibility and implementation details.",
        "6. Use [revision questions](questions/revision-questions.md) for retrieval and testing.",
        "",
        "## Imported Source Profile",
        "",
        "| Bucket | Source Count |",
        "|---|---:|",
        f"| Lectures | {bucket_counts.get('lectures', len(lecture_files))} |",
        f"| Assignments | {bucket_counts.get('assignments', 0)} |",
        f"| Notebooks | {bucket_counts.get('notebooks', 0)} |",
        f"| Sources | {bucket_counts.get('sources', len(source_files))} |",
        "",
        "## Key Raw Files To Triage",
        "",
        "### Lectures",
        "",
    ]
    lines.extend(f"- {name}" for name in lecture_files)
    lines.extend(["", "### Assignments", ""])
    if assignment_files:
        lines.extend(f"- {name.rsplit('/', 1)[-1]}" for name in assignment_files)
    else:
        lines.append("- No copied assignment files detected.")

    lines.extend(["", "### Notebooks", ""])
    if notebook_files:
        lines.extend(f"- {name}" for name in notebook_files[:24])
    else:
        lines.append("- No copied notebook files detected.")

    lines.extend(
        [
            "",
            "## Assessment Links",
            "",
            "- [AT1](assignments/at1.md)",
            "- [AT2](assignments/at2.md)",
            "- [AT3](assignments/at3.md)",
            "- [Evidence Map](assignments/evidence-map.md)",
            "",
            "## LLM Study Prompts",
            "",
            "- Summarise session notes with assumptions, risks, and reproducibility implications.",
            "- Build a compact exam set from the session and notebook evidence.",
            "- Identify the highest-value AT evidence and map it to grading criteria.",
            "- Compare model trade-offs per session and validate interpretation consistency.",
            "",
            "## Maintenance Checklist",
            "",
            f"- [x] Session notes created ({len(by_session)} sessions)",
            "- [x] Notebook catalog created",
            "- [x] Assignment pages created",
            "- [x] Evidence map created",
            "- [x] Revision questions created",
            "- [ ] Finalise assignment-specific evidence links and citations",
        ]
    )
    write(SUBJECT / "learning-map.md", "\n".join(lines) + "\n")


def update_lecture_readme(by_session: dict[int, list[dict[str, str]]]) -> None:
    lecture_readme = SUBJECT / "lectures" / "README.md"
    text = lecture_readme.read_text(encoding="utf-8")
    links = "\n".join(
        f"- [Session {session:02d} - {SESSION_TOPICS.get(session, f'Advanced ML Session {session:02d}')}](session-{session:02d}.md)"
        for session in sorted(by_session)
    )
    if "## Curated Session Notes" in text:
        text = text.split("## Curated Session Notes", 1)[0].rstrip()
    write(lecture_readme, text.rstrip() + "\n\n## Curated Session Notes\n\n" + links + "\n")


def update_subject_links() -> None:
    subject_readme = SUBJECT / "README.md"
    text = subject_readme.read_text(encoding="utf-8")
    if "notebooks/lab-notes.md" not in text:
        text = text.replace(
            "- [Assignment Dashboard](assignments/README.md)",
            "- [Assignment Dashboard](assignments/README.md)\n- [Notebook Notes](notebooks/lab-notes.md)",
        )
    write(subject_readme, text)


def main() -> None:
    by_session = collect_lecture_sources()
    by_lab = collect_notebook_sources()
    payloads = collect_assignments()

    write_session_notes(by_session)
    write_glossary(by_session, by_lab)
    write_notebook_catalog(by_lab)
    write_assignment_pages(payloads)
    write_evidence_map(by_session, payloads)
    write_questions()
    update_learning_map(by_session, payloads)
    update_lecture_readme(by_session)
    update_subject_links()
    print(f"Generated 36120 Advanced ML Application notes for {len(by_session)} sessions and {sum(len(v) for v in by_lab.values())} notebooks.")


if __name__ == "__main__":
    main()

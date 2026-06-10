from __future__ import annotations

import contextlib
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
SUBJECT = REPO_ROOT / "llm-wiki" / "02-subjects" / "36106-machine-learning-algorithms-and-applications"
RAW_ROOT = SUBJECT / "sources" / "raw"


SESSION_TOPICS = {
    1: "Exploratory Data Analysis and Problem Framing",
    2: "Multivariate Linear Regression",
    3: "ElasticNet, Ridge, Lasso, and Regularisation",
    4: "K-Nearest Neighbours Regression",
    5: "Classification Baselines and Metrics",
    6: "SVM and Decision Tree Classification",
    7: "Clustering and Unsupervised Learning",
    8: "Dimensionality Reduction and Anomaly Detection",
    9: "MLAA Recap and Assessment Integration",
}

SESSION_OBJECTIVES = {
    1: [
        "Use EDA to identify missing values, feature relationships, and target behaviour.",
        "Frame a machine learning problem from data, target, features, and evaluation constraints.",
    ],
    2: [
        "Explain multivariate linear regression workflows and baseline model expectations.",
        "Understand intercept handling, train/test splits, and metrics for continuous targets.",
    ],
    3: [
        "Compare Ridge, Lasso, and ElasticNet regularisation.",
        "Explain how alpha and l1_ratio affect coefficients and overfitting.",
    ],
    4: [
        "Explain KNN regression using distance-based neighbours.",
        "Recognise why scaling and feature choice affect KNN predictions.",
    ],
    5: [
        "Set classification baselines for AT2-style tasks.",
        "Use precision, recall, accuracy, and class-balance reasoning appropriately.",
    ],
    6: [
        "Compare SVM and decision tree classification workflows.",
        "Inspect classification reports, decision boundaries, and practical model tradeoffs.",
    ],
    7: [
        "Explain clustering as an unsupervised workflow without ground-truth labels.",
        "Evaluate whether discovered structure is meaningful for the problem.",
    ],
    8: [
        "Explain PCA as dimensionality reduction based on high-variance directions.",
        "Connect anomaly detection to unusual usage or behaviour patterns.",
    ],
    9: [
        "Synthesize model evidence into an assessment-ready narrative.",
        "Communicate limitations, assumptions, and practical recommendations.",
    ],
}

CONCEPTS = {
    "supervised learning": ["supervised", "label", "target", "train", "test"],
    "regression": ["regression", "linear regression", "rmse", "mae", "r2"],
    "classification": ["classification", "classifier", "accuracy", "precision", "recall", "f1"],
    "train-test split": ["train test", "train_test_split", "holdout", "test set", "training set"],
    "cross-validation": ["cross-validation", "cross validation", "kfold", "validation"],
    "feature engineering": ["feature", "encoding", "scaling", "preprocess", "pipeline"],
    "data leakage": ["leakage", "data leakage", "target leakage"],
    "decision tree": ["decision tree", "tree", "random forest", "forest"],
    "ensemble learning": ["ensemble", "random forest", "boost", "bagging", "xgboost"],
    "clustering": ["cluster", "clustering", "kmeans", "k-means"],
    "dimensionality reduction": ["pca", "dimension", "dimensionality", "component"],
    "model evaluation": ["evaluation", "metric", "confusion matrix", "roc", "auc"],
    "hyperparameter tuning": ["hyperparameter", "gridsearch", "randomizedsearch", "tuning"],
    "anomaly detection": ["anomaly", "outlier", "isolation", "fraud"],
    "model interpretation": ["interpret", "importance", "explain", "shap"],
}

DEFINITIONS = {
    "supervised learning": "Learning a mapping from input features to known target labels or values.",
    "regression": "A supervised learning task where the model predicts a continuous target.",
    "classification": "A supervised learning task where the model predicts a discrete class or class probability.",
    "train-test split": "A separation of data used to estimate performance on examples not used for fitting.",
    "cross-validation": "A validation strategy that repeatedly trains and evaluates models across different folds.",
    "feature engineering": "Creating, transforming, encoding, or selecting variables to improve model learning.",
    "data leakage": "Using information during training that would not be available at prediction time.",
    "decision tree": "A model that predicts by recursively splitting feature space into decision regions.",
    "ensemble learning": "Combining multiple models to improve predictive performance or robustness.",
    "clustering": "Unsupervised grouping of examples based on similarity or distance structure.",
    "dimensionality reduction": "Transforming data into fewer variables while retaining important structure.",
    "model evaluation": "Measuring model performance with metrics aligned to the problem and consequences.",
    "hyperparameter tuning": "Choosing model settings that are not directly learned from the training algorithm.",
    "anomaly detection": "Identifying observations that are unusual relative to expected patterns.",
    "model interpretation": "Explaining what a model learned, which features matter, and where predictions may fail.",
}


def clean(text: str) -> str:
    return re.sub(r"\s+", " ", text).strip()


def xml_text(xml: bytes) -> str:
    root = ElementTree.fromstring(xml)
    return " ".join(node.text for node in root.iter() if node.text)


def extract_zip_xml(path: Path, prefixes: tuple[str, ...], max_chars: int = 12000) -> str:
    try:
        chunks = []
        with zipfile.ZipFile(path) as archive:
            for name in sorted(archive.namelist()):
                if name.startswith(prefixes) and name.endswith(".xml"):
                    chunks.append(xml_text(archive.read(name)))
        return clean("\n".join(chunks))[:max_chars]
    except Exception as exc:
        return f"[Office extraction failed: {exc}]"


def extract_pdf(path: Path, max_chars: int = 12000) -> str:
    try:
        stderr = io.StringIO()
        with warnings.catch_warnings(), contextlib.redirect_stderr(stderr):
            warnings.simplefilter("ignore")
            reader = PdfReader(str(path))
            return clean("\n".join((page.extract_text() or "") for page in reader.pages[:12]))[:max_chars]
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
                    if any(term in line.lower() for term in ["fit(", "predict(", "score(", "train_test_split", "pipeline", "gridsearch"])
                )
                if imports:
                    chunks.append("Code imports:\n" + imports)
                if comments:
                    chunks.append(comments)
                if calls:
                    chunks.append("Model code signals:\n" + calls)
        return clean("\n".join(chunks))[:max_chars]
    except Exception as exc:
        return f"[Notebook extraction failed: {exc}]"


def extract_text(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix == ".pptx":
        return extract_zip_xml(path, ("ppt/slides/", "ppt/notesSlides/"))
    if suffix == ".docx":
        return extract_zip_xml(path, ("word/",))
    if suffix == ".pdf":
        return extract_pdf(path)
    if suffix == ".ipynb":
        return extract_notebook(path)
    if suffix in {".md", ".txt", ".py"}:
        return clean(path.read_text(encoding="utf-8", errors="ignore"))[:12000]
    return ""


def session_from_path(path: Path) -> int | None:
    match = re.search(r"session[_\s-]*(\d+)", path.name, flags=re.I)
    if not match:
        match = re.search(r"Session\s+(\d+)", str(path), flags=re.I)
    if match:
        value = int(match.group(1))
        if 1 <= value <= 9:
            return value
    return None


def collect() -> tuple[dict[int, list[dict[str, str]]], list[dict[str, str]]]:
    by_session: dict[int, list[dict[str, str]]] = defaultdict(list)
    assessment_sources = []
    for path in sorted(RAW_ROOT.rglob("*")):
        if not path.is_file():
            continue
        rel = str(path.relative_to(SUBJECT))
        suffix = path.suffix.lower()
        if suffix in {".png", ".jpg", ".jpeg", ".svg"}:
            continue
        item = {"type": suffix.lstrip(".") or "file", "path": rel, "text": extract_text(path)}
        session = session_from_path(path)
        if session is not None:
            by_session[session].append(item)
        elif "AT3" in str(path) or "project" in path.name.lower() or "anomaly" in path.name.lower():
            assessment_sources.append(item)
    return by_session, assessment_sources


def score(text: str) -> Counter:
    lower = text.lower()
    counts = Counter()
    for concept, terms in CONCEPTS.items():
        for term in terms:
            counts[concept] += lower.count(term)
    return counts


def keywords(text: str, n: int = 12) -> list[str]:
    words = re.findall(r"[A-Za-z][A-Za-z0-9_+-]{3,}", text.lower())
    stop = {
        "this",
        "that",
        "with",
        "from",
        "session",
        "machine",
        "learning",
        "model",
        "data",
        "slides",
        "activity",
        "assessment",
        "group",
    }
    return [word for word, _ in Counter(w for w in words if w not in stop).most_common(n)]


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def bullet(items: list[str]) -> str:
    return "\n".join(f"- {item}" for item in items)


def write_session(session: int, sources: list[dict[str, str]]) -> None:
    all_text = "\n".join(item["text"] for item in sources)
    concepts = [
        f"- {concept}: {DEFINITIONS.get(concept, 'Verify definition from source material.')}"
        for concept, count in score(all_text).most_common()
        if count > 0
    ]
    source_lines = "\n".join(f"- `{item['path']}` ({item['type']})" for item in sources)
    write(
        SUBJECT / "lectures" / f"session-{session:02d}.md",
        f"""---
type: lecture-note
subject: 36106-machine-learning-algorithms-and-applications
session: {session}
status: draft
---

# Session {session:02d} - {SESSION_TOPICS.get(session, 'Machine Learning Topic')}

## Source Files

{source_lines}

## Working Summary

This is a first-pass curated note generated from copied UPASS decks, notebooks, and assessment-adjacent materials. Verify details against source files before using it for assessment.

## Study Objectives

{bullet(SESSION_OBJECTIVES.get(session, ['Review source files and identify the main machine learning workflow.']))}

## Likely Concepts

{chr(10).join(concepts[:10]) or '- To be confirmed from source review.'}

## Extracted Keywords

{bullet(keywords(all_text))}

## What To Understand

- What prediction or analysis task is being solved.
- Which features, target, split strategy, model, and metrics are being used.
- Whether preprocessing is fitted only on training data.
- How the model is evaluated against a baseline.
- What practical limitation, risk, or interpretation issue should be reported.

## Assessment Relevance

- Use this session to justify modelling choices, evaluation metrics, and workflow decisions.
- Cross-check any notebook implementation against leakage, weak baselines, and metric mismatch.

## Revision Questions

- What is the supervised or unsupervised learning task?
- Which metric matches the practical objective?
- Where could leakage or overfitting enter the workflow?
- How would you explain the model result to a non-technical stakeholder?

## LLM Follow-Up Prompt

Using the source files listed above, expand this draft into a precise study note with definitions, modelling steps, metric guidance, notebook implementation details, and assessment relevance. Keep claims traceable to source files.
""",
    )


def write_glossary(by_session: dict[int, list[dict[str, str]]], assessment_sources: list[dict[str, str]]) -> None:
    text = "\n".join(item["text"] for sources in by_session.values() for item in sources)
    text += "\n" + "\n".join(item["text"] for item in assessment_sources)
    rows = []
    for concept, count in score(text).most_common():
        if count > 0:
            rows.append(f"| {concept} | {count} | {DEFINITIONS.get(concept, 'Add verified definition from source material.')} |")
    write(
        SUBJECT / "glossary.md",
        f"""---
type: glossary
subject: 36106-machine-learning-algorithms-and-applications
status: draft
---

# 36106 Machine Learning Algorithms and Applications - Glossary

| Term | Evidence Count | Working Definition |
|---|---:|---|
{chr(10).join(rows)}

## Maintenance

- Replace working definitions with precise formulas, examples, and metric notes from source materials.
- Link durable terms to [Machine Learning](../../03-shared-concepts/machine-learning.md), [Statistics](../../03-shared-concepts/statistics.md), and [Python](../../03-shared-concepts/python.md).
""",
    )


def write_evidence_map(by_session: dict[int, list[dict[str, str]]], assessment_sources: list[dict[str, str]]) -> None:
    rows = "\n".join(
        f"| Session {session:02d} | {SESSION_TOPICS.get(session, '')} | {len(sources)} | [note](../lectures/session-{session:02d}.md) |"
        for session, sources in sorted(by_session.items())
    )
    assessment_rows = "\n".join(f"- `{item['path']}` ({item['type']})" for item in assessment_sources) or "- No assessment-specific source files detected."
    write(
        SUBJECT / "assignments" / "evidence-map.md",
        f"""---
type: evidence-map
subject: 36106-machine-learning-algorithms-and-applications
status: draft
---

# 36106 Machine Learning Algorithms and Applications - Assessment Evidence Map

## Session Evidence

| Session | Topic | Source Count | Curated Note |
|---|---|---:|---|
{rows}

## Assessment-Specific Sources

{assessment_rows}

## Assessment Evidence Strategy

- Use Sessions 1-4 for problem framing, preprocessing, splits, and leakage checks.
- Use Sessions 5-8 for model families, tuning, and implementation details.
- Use Session 9 and AT3 sources for reporting structure, interpretation, limitations, and recommendations.
- Link each modelling claim to a session note, notebook, metric, or assessment source.
""",
    )


def update_indexes(by_session: dict[int, list[dict[str, str]]]) -> None:
    links = "\n".join(
        f"- [Session {session:02d} - {SESSION_TOPICS.get(session, 'ML Topic')}](session-{session:02d}.md)"
        for session in sorted(by_session)
    )
    lectures_readme = SUBJECT / "lectures" / "README.md"
    text = lectures_readme.read_text(encoding="utf-8")
    if "## Curated Session Notes" in text:
        text = text.split("## Curated Session Notes", 1)[0].rstrip()
    write(lectures_readme, text.rstrip() + f"\n\n## Curated Session Notes\n\n{links}\n")

    subject_readme = SUBJECT / "README.md"
    text = subject_readme.read_text(encoding="utf-8")
    if "[Glossary](glossary.md)" not in text and "## Curated Study Layer" in text:
        text = text.replace(
            "- [Revision Questions](questions/revision-questions.md)",
            "- [Revision Questions](questions/revision-questions.md)\n- [Glossary](glossary.md)\n- [Assessment Evidence Map](assignments/evidence-map.md)",
        )
    write(subject_readme, text)


def main() -> None:
    by_session, assessment_sources = collect()
    for session, sources in sorted(by_session.items()):
        write_session(session, sources)
    write_glossary(by_session, assessment_sources)
    write_evidence_map(by_session, assessment_sources)
    update_indexes(by_session)
    print(f"Generated {len(by_session)} session notes for 36106 Machine Learning Algorithms and Applications")


if __name__ == "__main__":
    main()

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path

import nbformat
from pypdf import PdfReader


REPO_ROOT = Path(__file__).resolve().parents[1]
SUBJECT = REPO_ROOT / "llm-wiki" / "02-subjects" / "94691-deep-learning"
LECTURES_RAW = SUBJECT / "lectures" / "raw"
NOTEBOOKS_RAW = SUBJECT / "notebooks" / "raw"
ASSIGNMENTS_RAW = SUBJECT / "assignments" / "raw"


CONCEPTS = {
    "neural network": ["neural network", "neural networks", "multilayer perceptron", "mlp"],
    "backpropagation": ["backpropagation", "back-propagation", "gradient descent"],
    "activation function": ["activation", "relu", "sigmoid", "softmax", "tanh"],
    "loss function": ["loss function", "cross entropy", "mse", "objective function"],
    "optimisation": ["optimizer", "optimisation", "optimization", "adam", "sgd", "learning rate"],
    "regularisation": ["regularization", "regularisation", "dropout", "weight decay", "batch normalization", "batch normalisation"],
    "convolutional neural network": ["convolution", "cnn", "convolutional neural network", "convnet"],
    "transfer learning": ["transfer learning", "fine tuning", "fine-tuning", "pretrained", "pre-trained"],
    "resnet": ["resnet", "residual"],
    "inception": ["inception", "googlenet"],
    "object detection": ["object detection", "yolo", "faster r-cnn", "ssd", "bounding box"],
    "computer vision": ["image", "opencv", "vision", "feature extraction"],
    "pytorch": ["pytorch", "torch", "torchvision"],
    "evaluation": ["accuracy", "precision", "recall", "f1", "confusion matrix", "bleu"],
    "image captioning": ["caption", "encoder", "decoder", "attention", "flickr"],
}


WEEK_TOPICS = {
    1: "Python, OpenCV, and Deep Learning Foundations",
    2: "Image Processing, Edge Detection, and Machine Learning Review",
    3: "Feature Extraction and Logistic Regression Foundations",
    4: "Neural Networks and Multilayer Models",
    5: "Convolutional Neural Networks",
    6: "Regularisation and Overfitting Control",
    7: "Transfer Learning, ResNet, and Inception",
    8: "Object Detection with Faster R-CNN and SSD",
    9: "Object Detection with YOLO and RF-DETR",
}

WEEK_OBJECTIVES = {
    1: [
        "Set up the Python/OpenCV workflow used by later computer vision notebooks.",
        "Understand image arrays, channels, transformations, and display pipelines.",
        "Connect low-level image operations to later neural network inputs.",
    ],
    2: [
        "Explain edge detection and classical image-processing operations.",
        "Review the machine learning pipeline before introducing deep models.",
        "Identify where hand-crafted features stop scaling well.",
    ],
    3: [
        "Compare hand-crafted feature extraction with learned representations.",
        "Understand logistic regression as a bridge into neural classifiers.",
        "Recognise how feature quality affects downstream classification.",
    ],
    4: [
        "Explain multilayer neural networks, activations, loss functions, and backpropagation.",
        "Track tensor shapes through dense layers.",
        "Diagnose training behaviour using loss and validation metrics.",
    ],
    5: [
        "Explain why convolution is effective for image data.",
        "Track feature maps through convolution, pooling, and classifier layers.",
        "Implement and evaluate CNN models in PyTorch.",
    ],
    6: [
        "Identify overfitting from train/validation behaviour.",
        "Apply regularisation strategies such as dropout, weight decay, and augmentation.",
        "Explain the tradeoff between model capacity and generalisation.",
    ],
    7: [
        "Use pretrained CNNs through transfer learning and fine-tuning.",
        "Explain residual connections and why they help deep networks train.",
        "Compare ResNet and Inception-style architectures at a high level.",
    ],
    8: [
        "Explain object detection as classification plus localisation.",
        "Compare two-stage and one-stage detection framing.",
        "Understand bounding boxes, confidence scores, and detection metrics.",
    ],
    9: [
        "Use modern object detection workflows such as YOLO-style models.",
        "Evaluate detection outputs and common failure modes.",
        "Connect object detection notebooks to practical computer vision tasks.",
    ],
}

WEEK_ASSESSMENT_RELEVANCE = {
    1: "Supports notebook hygiene, image loading, preprocessing, and reproducible coding expected across all assignments.",
    2: "Supports Assignment 1 foundations where image representations and classical feature processing matter.",
    3: "Supports Assignment 1 by connecting feature extraction to classification baselines.",
    4: "Supports Assignment 1 and exam revision on neural network training fundamentals.",
    5: "Supports Assignment 1 and Assignment 2 where CNN design, training, and diagnostics are central.",
    6: "Supports Assignment 2 through overfitting control, validation reasoning, and model improvement.",
    7: "Supports Assignment 2 through transfer learning, pretrained models, ResNet/Inception, and fine-tuning decisions.",
    8: "Supports later computer vision tasks and object detection revision.",
    9: "Supports object detection extension work and practical model evaluation.",
}

CONCEPT_DEFINITIONS = {
    "neural network": "A model made of layers of learned parameters that transform inputs into predictions through nonlinear functions.",
    "backpropagation": "The algorithm used to compute gradients of a loss with respect to model parameters so the optimiser can update weights.",
    "activation function": "A nonlinear function such as ReLU, sigmoid, tanh, or softmax that lets neural networks model non-linear relationships.",
    "loss function": "The objective being minimised during training, such as cross-entropy for classification or mean squared error for regression.",
    "optimisation": "The process of updating model parameters, often with SGD or Adam, to reduce the loss function.",
    "regularisation": "Techniques that reduce overfitting, including dropout, weight decay, data augmentation, and early stopping.",
    "convolutional neural network": "A neural architecture that uses convolutional filters to learn spatial features from image-like inputs.",
    "transfer learning": "Reusing a pretrained model or representation for a new task, often by freezing or fine-tuning selected layers.",
    "resnet": "A CNN architecture family that uses residual connections to make deeper networks easier to train.",
    "inception": "A CNN architecture pattern that combines multiple convolutional filter sizes to capture features at different scales.",
    "object detection": "A computer vision task that predicts both object classes and object locations, usually via bounding boxes.",
    "computer vision": "Methods for representing, analysing, and modelling images or visual data.",
    "pytorch": "A Python deep learning framework used to define tensors, neural network modules, losses, optimisers, and training loops.",
    "evaluation": "The process of judging model performance with metrics, validation data, error analysis, and task-specific criteria.",
    "image captioning": "A multimodal task that generates text descriptions for images, often using an image encoder and text decoder.",
}


def clean_text(text: str) -> str:
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def extract_pdf_text(path: Path, max_chars: int = 12000) -> str:
    try:
        reader = PdfReader(str(path))
        chunks = []
        for page in reader.pages[:12]:
            chunks.append(page.extract_text() or "")
        return clean_text("\n".join(chunks))[:max_chars]
    except Exception as exc:
        return f"[PDF extraction failed: {exc}]"


def extract_notebook_text(path: Path, max_chars: int = 12000) -> str:
    try:
        nb = nbformat.read(path, as_version=4)
        chunks = []
        for cell in nb.cells:
            if cell.cell_type == "markdown":
                chunks.append(str(cell.source))
            elif cell.cell_type == "code":
                source = str(cell.source)
                imports = "\n".join(line for line in source.splitlines() if line.startswith(("import ", "from ")))
                if imports:
                    chunks.append("Code imports:\n" + imports)
                for line in source.splitlines():
                    if line.strip().startswith("#"):
                        chunks.append(line.strip("# "))
        return clean_text("\n".join(chunks))[:max_chars]
    except Exception as exc:
        return f"[Notebook extraction failed: {exc}]"


def week_from_name(path: Path) -> int | None:
    text = str(path)
    patterns = [
        r"week[_\s-]*(\d+)",
        r"lecture[_\s-]*(\d+)",
        r"module[_\s-]*(\d+)",
        r"lab[_\s-]*(\d+)",
    ]
    for pattern in patterns:
        match = re.search(pattern, text, flags=re.I)
        if match:
            week = int(match.group(1))
            if 1 <= week <= 12:
                return week
    return None


def score_concepts(text: str) -> Counter:
    lowered = text.lower()
    scores = Counter()
    for concept, terms in CONCEPTS.items():
        for term in terms:
            scores[concept] += lowered.count(term)
    return scores


def collect_sources() -> dict[int, list[dict[str, str]]]:
    by_week: dict[int, list[dict[str, str]]] = defaultdict(list)
    for path in sorted(LECTURES_RAW.rglob("*.pdf")):
        week = week_from_name(path)
        if not week:
            continue
        text = extract_pdf_text(path)
        by_week[week].append({"type": "lecture", "path": str(path.relative_to(SUBJECT)), "text": text})
    for path in sorted(NOTEBOOKS_RAW.rglob("*.ipynb")):
        week = week_from_name(path)
        if not week:
            continue
        text = extract_notebook_text(path)
        by_week[week].append({"type": "notebook", "path": str(path.relative_to(SUBJECT)), "text": text})
    return by_week


def top_terms(text: str, n: int = 12) -> list[str]:
    words = re.findall(r"[A-Za-z][A-Za-z0-9+-]{3,}", text.lower())
    stop = {
        "this", "that", "with", "from", "have", "your", "will", "using", "data", "model",
        "learning", "deep", "lecture", "week", "part", "solution", "exercise", "image",
    }
    counts = Counter(w for w in words if w not in stop)
    return [word for word, _ in counts.most_common(n)]


def write_week_note(week: int, sources: list[dict[str, str]]) -> None:
    all_text = "\n".join(item["text"] for item in sources)
    concepts = [name for name, score in score_concepts(all_text).most_common() if score > 0][:8]
    keywords = top_terms(all_text)
    source_lines = "\n".join(f"- `{item['path']}` ({item['type']})" for item in sources)
    concept_lines = "\n".join(f"- {concept}: {CONCEPT_DEFINITIONS.get(concept, 'Verify definition from source material.')}" for concept in concepts) or "- To be confirmed from lecture review"
    keyword_lines = "\n".join(f"- {kw}" for kw in keywords) or "- To be confirmed"
    objective_lines = "\n".join(f"- {item}" for item in WEEK_OBJECTIVES.get(week, []))

    note = f"""---
type: lecture-note
subject: 94691-deep-learning
week: {week}
status: draft
---

# Week {week:02d} - {WEEK_TOPICS.get(week, 'Deep Learning Topic')}

## Source Files

{source_lines}

## Working Summary

This note was generated from copied lecture PDFs and notebooks. Treat it as a first-pass study map: verify details against the source files before using it for assessment.

## Study Objectives

{objective_lines}

## Likely Concepts

{concept_lines}

## Extracted Keywords

{keyword_lines}

## What To Understand

- What problem this week's models or methods solve.
- What assumptions the method makes about data, labels, architecture, or training.
- How the method is implemented in PyTorch or notebook code.
- How performance should be evaluated and diagnosed.

## Assessment Relevance

- {WEEK_ASSESSMENT_RELEVANCE.get(week, 'Identify whether this week supports Assignment 1, Assignment 2, Assignment 3, or exam revision.')}
- Link useful source files to the relevant assessment page.

## Revision Questions

- Explain the main model or method from this week in plain language.
- What are the key hyperparameters or design choices?
- What failure modes should be checked?
- How would you evaluate whether the model is working?

## LLM Follow-Up Prompt

Using the source files listed above, expand this draft into a precise study note with definitions, formulas, PyTorch implementation details, examples, and likely assessment relevance. Keep all claims traceable to source files.
"""
    write(SUBJECT / "lectures" / f"week-{week:02d}.md", note)


def write(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def write_glossary(by_week: dict[int, list[dict[str, str]]]) -> None:
    combined = "\n".join(item["text"] for sources in by_week.values() for item in sources)
    scores = score_concepts(combined)
    rows = []
    for concept, score in scores.most_common():
        if score <= 0:
            continue
        definition = CONCEPT_DEFINITIONS.get(concept, "Add verified definition from lectures and notebooks.")
        rows.append(f"| {concept} | {score} | {definition} |")
    body = "\n".join(rows)
    write(
        SUBJECT / "glossary.md",
        f"""---
type: glossary
subject: 94691-deep-learning
status: draft
---

# 94691 Deep Learning - Glossary

| Term | Evidence Count | Working Definition |
|---|---:|---|
{body}

## Maintenance

- Replace working definitions with verified definitions from lectures and notebooks.
- Link repeated terms to [Deep Learning](../../03-shared-concepts/deep-learning.md), [Machine Learning](../../03-shared-concepts/machine-learning.md), and [Python](../../03-shared-concepts/python.md).
""",
    )


def write_evidence_map(by_week: dict[int, list[dict[str, str]]]) -> None:
    assignment_files = sorted(str(p.relative_to(SUBJECT)) for p in ASSIGNMENTS_RAW.rglob("*") if p.is_file())
    weekly_rows = []
    for week, sources in sorted(by_week.items()):
        weekly_rows.append(f"| Week {week:02d} | {WEEK_TOPICS.get(week, '')} | {len(sources)} | [note](../lectures/week-{week:02d}.md) |")
    assignment_lines = "\n".join(f"- `{path}`" for path in assignment_files[:40])
    write(
        SUBJECT / "assignments" / "evidence-map.md",
        f"""---
type: evidence-map
subject: 94691-deep-learning
status: draft
---

# 94691 Deep Learning - Assessment Evidence Map

## Weekly Evidence

| Week | Topic | Source Count | Curated Note |
|---|---|---:|---|
{chr(10).join(weekly_rows)}

## Assignment Source Files

{assignment_lines}

## Assessment-To-Week Map

| Assessment | Most Relevant Weeks | Evidence Focus |
|---|---|---|
| Assignment 1 | Weeks 1-5 | Image preprocessing, feature extraction, neural network fundamentals, CNN classification. |
| Assignment 2 | Weeks 5-7 | CNN training, overfitting control, transfer learning, pretrained architectures, model diagnostics. |
| Assignment 3 | Weeks 7-9 | Advanced computer vision, encoder/decoder thinking, object detection or image captioning workflows. |

## How To Use This Map

- Link each assignment page to the weekly notes that support it.
- Add source-specific evidence under the relevant assignment page.
- Keep model weights and large data referenced rather than embedded in notes.
""",
    )


def update_indexes(by_week: dict[int, list[dict[str, str]]]) -> None:
    links = "\n".join(f"- [Week {week:02d} - {WEEK_TOPICS.get(week, 'Deep Learning Topic')}](week-{week:02d}.md)" for week in sorted(by_week))
    readme = SUBJECT / "lectures" / "README.md"
    text = readme.read_text(encoding="utf-8")
    section = f"\n## Curated Weekly Notes\n\n{links}\n"
    if "## Curated Weekly Notes" in text:
        text = text.split("## Curated Weekly Notes", 1)[0].rstrip()
    write(readme, text.rstrip() + "\n" + section)

    subject_readme = SUBJECT / "README.md"
    text = subject_readme.read_text(encoding="utf-8")
    additions = [
        "- [Glossary](glossary.md)",
        "- [Assessment Evidence Map](assignments/evidence-map.md)",
    ]
    if "[Glossary](glossary.md)" not in text and "## Curated Study Layer" in text:
        text = text.replace(
            "- [Revision Questions](questions/revision-questions.md)",
            "- [Revision Questions](questions/revision-questions.md)\n" + "\n".join(additions),
        )
    write(subject_readme, text)


def main() -> None:
    by_week = collect_sources()
    for week, sources in sorted(by_week.items()):
        write_week_note(week, sources)
    write_glossary(by_week)
    write_evidence_map(by_week)
    update_indexes(by_week)
    print(f"Generated {len(by_week)} weekly notes for 94691 Deep Learning")


if __name__ == "__main__":
    main()

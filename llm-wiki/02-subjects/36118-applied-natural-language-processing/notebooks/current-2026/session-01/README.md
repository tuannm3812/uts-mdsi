# Session 1 Notebooks — Spring 2026

These are the current-semester versions. The inherited notebooks in `notebooks/raw/` remain reference material only.

## Files

- `ANLP_Session_1_NLP_Basics_Part_1.ipynb`: Python, web text extraction, regular expressions, NLTK, spaCy, tagging, and parsing.
- `ANLP_Session_1_NLP_Basics_Part_2.ipynb`: exploratory text analysis with pandas, seaborn, NLTK, matplotlib, and word clouds.
- `ANLP_Session_1_HW.ipynb`: Session 1 exercises.
- `ANLP_Session_1_HW_Worked.ipynb`: worked learning copy with explanations and
  defensive implementations for all six exercises.

See the [notebook guide](../../notebook-guide.md) for concept summaries and the
relationship between current and archived notebooks.

## Recommended Local Setup

Local Jupyter is the most reliable setup for both the lecture notebooks and later PDF export for AT1.

```bash
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements-week-01.txt
python -m spacy download en_core_web_sm
python -m ipykernel install --user \
  --name python311-nlp \
  --display-name "Python 3.11 (NLP)"
python -m jupyter lab
```

Python **3.11** is recommended. The latest spaCy release may fail to resolve
against Apple’s system Python 3.9. If Python 3.9 is unavoidable, use
`python -m pip install "spacy==3.7.5"`; otherwise, do not pin spaCy.

The requirements file covers all imports used across Part 1, Part 2, and the
worked homework. The `en_core_web_sm` model is installed separately because it
is a spaCy model package rather than a normal project dependency.

Run this once in Python to install the resources used by the current notebooks:

```python
import nltk

for resource in [
    "punkt",
    "punkt_tab",
    "averaged_perceptron_tagger_eng",
    "tagsets_json",
    "maxent_ne_chunker_tab",
    "words",
    "stopwords",
]:
    nltk.download(resource)
```

## Part 2 Dataset

The CNN articles CSV referenced by Part 2 was not included with the new downloads. The notebook includes an online source as an alternative to its Google Drive path. Use that URL cell, or place the CSV at:

```text
My Drive/Colab Notebooks/ANLP Colab Notebooks/ANLP Datasets/Session1_CNN_Articles_2021-2023.csv
```

If working locally, download the CSV beside the notebook and replace the path with:

```python
from pathlib import Path

data_path = Path("Session1_CNN_Articles_2021-2023.csv")
```

## Current-Version Notes

Part 1 now requests newer NLTK resource names such as **`punkt_tab`**, **`averaged_perceptron_tagger_eng`**, **`tagsets_json`**, and **`maxent_ne_chunker_tab`**. Use these current names if an older notebook or tutorial produces a resource lookup error.

## Worked-Homework Troubleshooting

- `ModuleNotFoundError: No module named 'spacy'`: activate the environment and
  install the packages above.
- `LookupError: Resource punkt... not found`: run the NLTK download cell; the
  worked notebook downloads both `punkt` and `punkt_tab` for compatibility.
- `OSError: Can't find model 'en_core_web_sm'`: run
  `python -m spacy download en_core_web_sm`. The worked notebook falls back to
  a blank English tokenizer, but POS tags and named entities require the model.
- UTS scraping errors usually indicate a network restriction or page redesign.
  The scraper uses table structure rather than presentation-specific CSS and
  was verified against the live UTS page on 28 July 2026.

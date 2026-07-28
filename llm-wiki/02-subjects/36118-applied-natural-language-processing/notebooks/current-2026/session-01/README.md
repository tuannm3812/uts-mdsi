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
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install jupyterlab pandas matplotlib seaborn nltk spacy beautifulsoup4 requests regex svgling wordcloud pypdf
python -m spacy download en_core_web_sm
python -m jupyter lab
```

Run this once in Python to install the resources used by the current notebooks:

```python
import nltk

for resource in [
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

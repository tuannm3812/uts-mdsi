---
type: notebook-guide
subject: 36118-applied-natural-language-processing
semester: 2026-spring
status: active
---

# NLP Notebook Guide

## How to Use This Collection

Use `current-2026/` for this semester’s classes and homework. Use
`raw/archive-2025/` only for preview, comparison, and extra practice because
topics, APIs, datasets, and assessment instructions may have changed.

The recommended sequence is:

1. Read the current lecture note.
2. Run the current Part 1 notebook from top to bottom.
3. Run Part 2 and explain what each cleaning or visualisation choice changes.
4. Attempt the original homework independently.
5. Compare your approach with the worked learning copy.

## Spring 2026 — Session 1

### NLP Basics, Part 1

`current-2026/session-01/ANLP_Session_1_NLP_Basics_Part_1.ipynb`

This notebook introduces the first applied NLP workflow:

- collecting text through input or **web scraping**;
- representing text as Python strings and encoded characters;
- **sentence tokenisation** and **word tokenisation** with NLTK;
- **stopwords**, **stemming**, and **lemmatisation**;
- **part-of-speech tagging** and named-entity chunking;
- dependency analysis and visualisation with **spaCy**;
- regular expressions for structured patterns such as dates and email
  addresses.

The current version uses newer NLTK resource identifiers, including
`punkt_tab`, `averaged_perceptron_tagger_eng`, `tagsets_json`, and
`maxent_ne_chunker_tab`.

### NLP Basics, Part 2

`current-2026/session-01/ANLP_Session_1_NLP_Basics_Part_2.ipynb`

Part 2 moves from individual strings to a tabular text corpus:

- loading a CSV with **pandas**, either from Google Drive or a URL;
- inspecting shape, columns, missing values, and descriptive statistics;
- normalising case and removing punctuation or stopwords;
- computing unigram and n-gram frequency distributions;
- plotting counts with **matplotlib** and **seaborn**;
- creating and interpreting a **word cloud**.

A frequency plot is descriptive evidence, not a conclusion. Interpretation
should explain what the preprocessing removed, what the remaining terms mean
in context, and what the chart cannot establish.

### Session 1 Homework

- `current-2026/session-01/ANLP_Session_1_HW.ipynb` — untouched exercise.
- `current-2026/session-01/ANLP_Session_1_HW_Worked.ipynb` — worked learning
  copy with input handling, spaCy analysis, a custom tokenizer, citation and
  URL regular expressions, word-frequency comparisons, and robust extraction
  of UTS core-subject rows.

The worked notebook intentionally keeps explanations beside the code. Change
the sample text and inspect the output before writing your own observations.

## Archived 2025 Course Sequence

The archived course notebooks live in
`raw/archive-2025/course-notebooks/`.

| Session | Main topics | Typical libraries |
|---|---|---|
| 1 | NLP basics, tokenisation, regex, corpus frequencies, scraping | NLTK, spaCy, Beautiful Soup |
| 2 | preprocessing pipeline, visualisation, LDA topic modelling, K-means clustering | pandas, Gensim, scikit-learn, pyLDAvis, UMAP |
| 3 | TextRank summarisation, classical text classification, sentiment analysis | NetworkX, scikit-learn, TextBlob |
| 4 | Word2Vec and neural sentiment models | Gensim, TensorFlow/Keras |
| 5 | BERT inference and fine-tuning, Hugging Face pipelines, Gradio | Transformers, PyTorch, Datasets |
| 6 | LLM prompting and API workflows | OpenAI SDK, tiktoken, LangChain |

### Important Archive Caveats

- Two archived notebooks are extensionless but contain notebook JSON:
  `ANLP Session 2_Part 1_Text Analysis` and
  `ANLP_Session 4_Part 2_Deep Learning models`.
- Older notebooks may use retired NLTK download names, outdated model APIs, or
  Google Colab paths that do not exist locally.
- The Session 6 notebooks may require an API key. Never store a key in a
  notebook or commit it to Git.
- Archived assessment work is reference material, not a template for a 2026
  submission.

## Supplementary Archive

`raw/archive-2025/supplementary/google-skill-boost/` contains optional examples
covering text classification, embeddings, recurrent neural networks, BERT,
text generation, similarity, image captioning, and AutoML. These notebooks
are useful when the current subject reaches the corresponding topic, but they
are not part of the authoritative 2026 weekly sequence.

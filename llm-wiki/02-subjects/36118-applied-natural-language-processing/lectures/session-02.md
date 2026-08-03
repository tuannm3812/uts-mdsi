---
type: lecture-note
subject: 36118-applied-natural-language-processing
session: 2
status: current-source-backed
---

# Session 02 - Text Analysis, Topic Modelling, and Clustering

## Source Files

- `current-2026/ANLP Session2_Week2-5.pdf` (authoritative current lecture)
- `../notebooks/current-2026/session-02/` (three practical notebooks and homework)
- `raw/archive-2025/ANLP Session2_Week2_After Session-1.pdf` (comparison only)

## Working Summary

The comprehensive current-semester note is maintained in
`session-02-preparation-2026.md` and rendered as
`handouts/session-02-comprehensive-notes.pdf`. It integrates the updated 2026
slides with all four Session 2 notebooks and records the LDA notebook’s saved
execution-order issue.

## Study Objectives

- Compare exploratory text analysis, topic modelling, and clustering.
- Explain how document representations affect unsupervised text results.
- Evaluate whether discovered topics or clusters are meaningful for a task.

## Core Concepts

- clustering: Grouping documents or text units by representation similarity without using labelled classes.
- topic modelling: Unsupervised methods for discovering recurring themes or latent topics in a document collection.
- text preprocessing: Cleaning and transforming text before analysis, including normalisation, stopword handling, stemming, lemmatisation, and filtering.
- bag of words: A sparse representation that counts words or weighted word occurrences without modelling word order.
- tokenisation: Splitting raw text into units such as words, subwords, or tokens that downstream NLP models can process.
- word association and collocation: complementary methods for finding repeated lexical relationships using frequency, PMI, likelihood ratio, or chi-square evidence.
- evaluation: elbow, silhouette, stability, representative-document inspection, and interpretability checks for unsupervised outputs.

## Extracted Keywords

- words
- code
- imports
- function
- learning
- gensim
- clusters
- love
- create
- sklearn
- word
- topic

## What To Understand

- What NLP task is being solved.
- How raw text becomes features, embeddings, prompts, or model inputs.
- Which model or method is appropriate for the task.
- How output quality should be evaluated.
- What responsible AI or data limitations apply.

## Assessment Relevance

- Link this session to AT1, AT2, AT3, or project evidence where relevant.
- Record which raw files support the assignment task, method, or evaluation.

## Revision Questions

- What is the main NLP workflow from this session?
- What representation of text is used?
- Which evaluation metric or qualitative check is appropriate?
- What could go wrong with this method in a real applied setting?

## Current Outputs

- Comprehensive Markdown: `session-02-preparation-2026.md`
- Printable PDF: `handouts/session-02-comprehensive-notes.pdf`
- Notebook setup and summaries: `../notebooks/current-2026/session-02/README.md`

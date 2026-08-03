# Session 2 Notebooks - Spring 2026

These notebooks accompany the current Session 2 lecture deck. Work through
them in teaching order:

1. ANLP_Session_2_Part1_Text_Analysis.ipynb
2. ANLP_Session2_Part2_Topic_Modeling.ipynb
3. ANLP_Session2_Part3_TextClustering.ipynb
4. ANLP_Session_2_HW.ipynb

## Notebook Summaries

### Part 1 - Text Analysis

Continues the Session 1 news-text workflow with **n-grams**, word
associations, statistically ranked **collocations**, concordances, and a
reproducible preprocessing pipeline. It compares frequencies before and after
cleaning, then visualises results with word clouds, bar charts, and a bigram
network.

### Part 2 - Topic Modelling

Uses the scikit-learn 20 Newsgroups corpus to build **Latent Dirichlet
Allocation (LDA)** models with Gensim. The workflow cleans text, creates
bigrams and trigrams, removes stopwords, lemmatises with spaCy, constructs a
dictionary and corpus, and explores topic-word distributions with pyLDAvis. It
also compares count-based input with TF-IDF.

The downloaded notebook contains a saved NameError output for LdaModel. Treat
that output as stale execution state: restart the kernel and run cells in order
so the LdaModel import executes before model creation.

### Part 3 - Text Clustering

Introduces hierarchical clustering and **k-means** for text. It represents
documents with TF-IDF, compares distance-based groupings, examines elbow and
silhouette methods for selecting k, inspects cluster terms, and uses UMAP for
two-dimensional visualisation.

### Homework

Applies the session methods to an open or AT1 dataset:

1. Compare word-association measures such as PMI and chi-square.
2. Compare stemming with lemmatisation.
3. Add digit removal to the preprocessing pipeline.
4. Try another topic-modelling implementation or algorithm, such as LSA, LDA,
   or NMF in scikit-learn.
5. Rebuild text clustering on a different dataset and re-evaluate the number
   of clusters.

## Environment Notes

The notebooks declare a Python 3 kernel and use:

- pandas, NumPy, Matplotlib, seaborn, and NetworkX;
- NLTK and its tokeniser, stopword, stemmer, collocation, and text tools;
- spaCy with en_core_web_sm;
- Gensim and pyLDAvis;
- scikit-learn, SciPy, wordcloud, tqdm, and umap-learn.

Install packages in the same Python environment used by the notebook, then
restart the kernel before running all cells. Dataset downloads and interactive
visualisations require network access.

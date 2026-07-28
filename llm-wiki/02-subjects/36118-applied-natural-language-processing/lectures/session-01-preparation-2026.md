---
type: lesson-preparation
subject: 36118-applied-natural-language-processing
session: 1
date: 2026-07-27
status: ready-for-class
source_scope: previous-semester-reference
---

# Session 01 Preparation - 27 July 2026

## Before Class

Spend 45-60 minutes on this preparation:

1. Read the pipeline and concepts below.
2. Open `ANLP Session 1_NLP_Basics - Part 1.ipynb` and skim the markdown and code sequence.
3. Open Part 2 and identify each text-cleaning decision.
4. Write down the five questions at the end to check during today's class.

The archived files came from a previous delivery of the subject. Use them to learn the concepts, but use the current Canvas materials for dates, assessments, required software, and the exact weekly sequence.

## The Core NLP Pipeline

`problem -> collect text -> inspect/clean -> tokenise -> represent -> model -> evaluate -> communicate`

- **Problem:** Define the decision or insight the text analysis must support.
- **Corpus:** Decide what documents belong in the dataset and whether they are representative.
- **Preprocessing:** Clean only what the task requires. Removing punctuation, case, stopwords, or emojis can also remove useful meaning.
- **Tokenisation:** Split text into words, sentences, or subword tokens.
- **Representation:** Convert language into numbers, such as counts, TF-IDF values, or embeddings.
- **Model:** Apply an exploratory, predictive, or generative method.
- **Evaluation:** Use task-appropriate metrics plus error analysis.
- **Communication:** Explain results, uncertainty, limitations, and ethical risks.

## Concepts To Know Today

| Concept | Plain-language meaning | Important caution |
|---|---|---|
| Corpus | The collection of documents being analysed | Sampling choices can bias every later result |
| Token | A unit processed by an NLP system | A token is not always a complete word |
| Normalisation | Making text more consistent, such as lowercasing | Consistency may remove meaningful distinctions |
| Stopword removal | Removing frequent function words | Words such as “not” may be crucial |
| Stemming | Heuristically reducing words to a root-like form | The result may not be a real word |
| Lemmatisation | Reducing a word to its dictionary base form | Usually needs linguistic context and is slower |
| Bag of words | Representing a document by word counts | It largely ignores order and context |
| TF-IDF | Upweighting words distinctive to a document | It is still sparse and context-poor |
| Embedding | A dense vector representing semantic information | Similarity can reproduce training-data bias |

## Small Worked Example

Text: `I did not enjoy the movie, but the acting was excellent.`

- Lowercasing is probably safe here.
- Removing punctuation may be acceptable for a simple bag-of-words model.
- Removing the stopword `not` would reverse important sentiment information.
- A bag-of-words representation captures word occurrence but weakly represents the contrast between the movie and the acting.
- Evaluation should inspect errors, not only report one aggregate accuracy score.

## Code Knowledge To Refresh

Be able to explain the purpose of:

```python
import re
import pandas as pd

text = "NLP is useful, but preprocessing choices matter!"
clean = re.sub(r"[^a-zA-Z\s]", "", text.lower())
tokens = clean.split()
```

Questions to ask about this code:

- What information does the regular expression remove?
- Is that information irrelevant to the actual task?
- How would this behave with contractions, emojis, URLs, names, or non-English text?
- Would a library tokenizer be more appropriate?

## Questions To Verify In Today's Class

1. Is the current weekly sequence the same as the archived Session 1-8 sequence?
2. Which Python environment and NLP libraries are required this semester?
3. Are the current assessments still AT1, AT2, and AT3, and what are their weights and due dates?
4. Which current-semester Canvas files replace the archived slides and notebooks?
5. What are the rules for using generative AI in learning activities and assessments?

## After Class - 15 Minute Update

- Add the current slides, notebook, subject outline, and assessment overview to the current-material tracker.
- Record anything that changed from the archived material.
- Replace this provisional preparation note with a source-backed Session 1 summary.
- Add unclear points to the tutor-question list while the lesson is still fresh.

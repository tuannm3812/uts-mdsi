---
type: assessment
subject: 36118-applied-natural-language-processing
code: 36118
semester: 2026-spring
status: in-progress
---

# 36118 AT1 — Text Analysis

## Official 2026 Task

- **Due:** Wednesday, 19 August 2026
- **Weight:** 30%
- **Mode:** individual
- **Corpus:** public submissions to the parliamentary inquiry into the value
  of skilled migration to Australia
- **Deliverables:** submit the `.ipynb` notebook and `.pdf` report separately
- **Current sources:** [brief, FAQ, sample notebook, data setup, and checks](current-2026/at1/README.md)

The work must combine reproducible Python, suitable statistics and
visualisations, and interpretation that answers a focused question. The rubric
places more weight on communication than on technical breadth:

1. Technical proficiency and justification: **35%**
2. Explanations and visualisations: **40%**
3. Readability, structure, and originality: **25%**

## Should We Follow the Previous Reports?

**Use them as examples of report organisation, not as templates to reproduce.**
They address different corpora and older task requirements. Following their
analyses or visual style too closely would weaken originality and may introduce
methods that do not help answer the 2026 question.

### 2023 Redacted Sample

The 40-page sample progresses from setup and cleaning through word frequency,
NER, n-grams, dependency trees, similarity, clustering, BERT topic modelling,
and references.

Useful features:

- commentary is placed beside code and output;
- several methods are compared rather than presented without explanation;
- charts are followed by interpretation;
- limitations of cleaning and modelling are sometimes discussed.

Features not to copy:

- its scope is much too broad for a focused 2026 story;
- numerous advanced methods compete for attention;
- many large code outputs make the report harder to scan;
- dark charts and dense notebook pages are not consistently print-friendly.

### 2024 Redacted Sample

The 46-page sample has a clearer report structure: project overview, data
understanding, preprocessing, EDA, text analysis, clustering, topic modelling,
conclusion, and references. It compares Australian radio transcripts by
station type and region.

Useful features:

- an explicit table of contents and numbered analytical sections;
- dataset context before modelling;
- preprocessing choices are explained;
- group comparisons are tied to defined metadata;
- the report closes with findings, limitations, future work, and references.

Features not to copy:

- 46 pages is longer than necessary for this AT1;
- repeated tables and charts could be condensed;
- some frequency views show common conversational words rather than evidence
  tightly aligned with the research question;
- methods should not be included merely because they appeared in a previous
  high-quality submission.

### Recommended 2026 Structure

Adopt the **narrative discipline** of the 2024 sample and the **method
explanations** of the 2023 sample, but use the official 2026 sample notebook as
the structural starting point:

1. Question and motivation
2. Corpus provenance and metadata
3. PDF extraction and quality audit
4. Preprocessing decisions
5. Focused exploratory evidence
6. One main comparative or thematic analysis
7. Interpretation and limitations
8. Conclusion
9. References

Aim for the shortest report that fully supports the argument. A compact,
well-explained analysis is better aligned with the rubric than a catalogue of
NLP techniques.

## Recommended Analytical Direction

A defensible corpus-wide baseline question is:

> **Which expected-benefit, risk, and policy-condition themes recur across the
> supplied submissions, and how consistently do those themes co-occur?**

This version is answerable with the supplied files and avoids inventing
submitter metadata. Once a reliable mapping is available, it can be extended
to compare submitter categories such as individual, industry/employer,
professional body, union/worker representative, government/public body, and
research/community organisation.

Possible evidence:

- document count and length by submitter category;
- relative term or phrase frequencies, not only raw counts;
- distinctive bigrams or TF-IDF terms by category;
- a small, interpretable set of themes such as skills shortages, productivity,
  exploitation, wages, recognition of qualifications, regional needs, housing,
  and pathways to permanence;
- representative excerpts verified against the original PDFs;
- sensitivity checks showing how cleaning or category definitions affect the
  result.

Do not infer support or opposition from isolated keywords. If stance becomes
part of the analysis, define an annotation rule, manually validate a sample,
and report ambiguity.

## Work Plan

| Phase | Output | Quality gate |
|---|---|---|
| 1. Inventory | One row per supplied PDF | 143 files accounted for; variants and numbering gaps preserved |
| 2. Extract | Raw text, page count, extraction status | Failures and low-text scans listed; OCR decisions recorded |
| 3. Enrich metadata | Submitter name and category | Mapping checked against the official inquiry page |
| 4. Define question | One question and expected comparison | Answerable with available text and metadata |
| 5. Preprocess | Original and cleaned text columns | Each transformation justified; negation and domain terms reviewed |
| 6. Baseline EDA | Length, missingness, category balance | Raw and relative quantities clearly distinguished |
| 7. Main analysis | A small set of tables and charts | Every output contributes to the question |
| 8. Validate | Manual review of documents and excerpts | Claims traceable to source submissions |
| 9. Write | Connected notebook narrative | Results interpreted, not merely described |
| 10. Reproduce | Clean restart and PDF export | All cells run in order; paths relative; PDF readable |

## Immediate Next Actions

1. Create `metadata.csv` only if submitter identity and category can be mapped
   reliably to every supplied file.
2. Export the trusted clean run to PDF and inspect the report page by page.

## Academic-Integrity Boundary

The archived reports can inform expectations about readability and
explanation. Do not reuse their wording, code, hypotheses, charts, taxonomies,
or conclusions. The 2026 corpus, research question, implementation, validation,
and interpretive argument must be independently developed.

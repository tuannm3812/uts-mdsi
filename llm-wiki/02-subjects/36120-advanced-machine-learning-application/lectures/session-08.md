---
type: lecture-note
subject: 36120-advanced-machine-learning-application
session: 8
status: draft
---

# Session 08 - Assessment-Linked Integration and Deployment Notes

## Source Files

- `lectures/raw/advml_slides_25sp/36120-25SP-Advanced ML Application-Lecture08.pdf` (pdf)

## Working Summary

This is a first-pass curated note generated from copied lecture PDFs and notebook-linked teaching materials. Verify all details against source files before using this for assessment.

## Study Objectives

- Prepare an assessment-ready evidence map from assignments and sessions.
- Summarise trade-offs and practical risks for final submission.

## Likely Concepts

- experiment tracking: Systematic logging of setup, code, and outputs for review and audit.
- overfitting: A pattern where a model performs well on training data but poorly generalizes.
- feature engineering: Transforming raw inputs into forms that improve model signal and stability.
- model evaluation: Measuring model quality using metrics aligned to a defined objective and failure cost.
- data leakage: Including information unavailable at prediction time, producing inflated validation scores.
- reproducibility: Ability to re-run an experiment and obtain consistent outcomes.
- time-series: Data indexed by time where ordering and dependencies constrain validation strategy.
- class imbalance: When target classes are not equally represented and metrics can mislead.

## Extracted Keywords

- mlops
- deployment
- machine
- models
- work
- scientists
- version
- collaboration
- control
- reproducibility
- cient
- development

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

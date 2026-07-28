# AT1 Text Analysis — Spring 2026

## Requirements at a Glance

- **Individual assessment**
- **Weight:** 30%
- **Due:** Wednesday, 19 August 2026
- Analyse the public submissions to the parliamentary inquiry into the value of skilled migration to Australia.
- Submit the notebook and rendered report as **two separate files**: `.ipynb` and `.pdf`. The FAQ permits HTML if PDF export cannot be completed.
- Combine reproducible code, statistics and visualisations with interpretation and a coherent data story.

The rubric weights are:

1. Technical proficiency and justification of code: **35%**
2. Communication through explanations and visualisations: **40%**
3. Readability, structure, and originality: **25%**

## Included Material

- `ANLP_AT1_Template_Sample.ipynb`
- `36118_Spring_2026_AT1_Detailed_Description.pdf`
- `36118_Spring_2026_AT1_FAQ.pdf`
- `notebooks/1_skilled_migration_text_analysis.ipynb`: reproducible AT1
  baseline using the complete supplied corpus
- `docs/0_coding_standards.md`: AT1-specific adaptation of the repository's
  master coding standard
- `docs/1_validation_log.md`: extraction diagnosis and an 18-submission
  theme-validation audit
- `requirements-at1.txt`: Python 3.11 dependency ranges
- `requirements-ocr.txt` and `scripts/ocr_low_text_pdfs.py`: optional local
  OCR workflow for image-based submissions
- `validation/`: the tracked 18-submission audit, source-verified thematic and
  group-contrast excerpts, curated submitter metadata, and the 20-sentence
  stance audit displayed by the notebook
- `data/submissions-skilled-migration/submissions_Skilledmigration/`: **143 PDFs**, extracted from the supplied archive

The official inquiry page is the authoritative public submissions register:

<https://www.aph.gov.au/Parliamentary_Business/Committees/Joint/Migration/Skilledmigration/Submissions>

> **Dataset check:** the supplied archive contains 143 PDF files, while the inquiry page may show a different total. Filenames include variants such as `Sub006.1` and gaps in the numbering. Preserve these source identifiers and verify any webpage-to-file mapping rather than renumbering files.

## Start the Analysis

Use the dedicated Python 3.11 environment and open the numbered working
notebook:

```bash
/opt/homebrew/bin/python3.11 -m pip install -r requirements-at1.txt
jupyter lab notebooks/1_skilled_migration_text_analysis.ipynb
```

The baseline accounts for all 143 PDFs, records extraction failures, and flags
documents with fewer than 500 extracted characters. Its current question
examines benefit, risk, and policy-condition themes without claiming that a
keyword match reveals stance. It also profiles the corpus using curated
submitter metadata and compares document-level theme prevalence across
submitter types.

The notebook also audits metadata readiness: the 143 files represent 139 main
submission numbers and four supplements. Numbers 49, 121, 124, 125, 126, and
144 are absent from the supplied archive, so preserve official identifiers and
do not treat file order as a submitter index. Four unsigned submissions retain
the label `Name not publicly stated`; `Sub079` remains unclassified because its
PDF begins mid-submission. `Sub140.pdf` is not silently renamed even though its
internal page footers say `Submission 121`; the discrepancy is recorded in
`validation/submitter_metadata.csv`.

The four image-based submissions have been recovered into ignored OCR
sidecars. To reproduce that preprocessing:

```bash
/opt/homebrew/bin/python3.11 -m pip install -r requirements-ocr.txt
/opt/homebrew/bin/python3.11 scripts/ocr_low_text_pdfs.py
```

## Suggested Notebook Structure

1. Research question or exploratory aim
2. Dataset provenance and limitations
3. Extraction and data-quality checks
4. Text cleaning, with justification for each choice
5. Exploratory analysis and visualisations
6. Focused findings tied to the research question
7. Limitations and interpretation
8. Conclusion

There is no fixed word count in the FAQ. Prioritise a clear argument, interpretable figures, and explanations in your own words. Reusing tutorial techniques is acceptable, but the question, implementation, analysis, and commentary must be your own.

## Export Check

Before submission:

1. Restart the kernel and run all cells from top to bottom.
2. Confirm that paths are relative and no private credentials appear.
3. Check that every chart has a title, readable labels, and an explanation.
4. Export to PDF and inspect every page for clipped code or figures.
5. Submit the `.ipynb` and `.pdf` separately.

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
- `data/submissions-skilled-migration/submissions_Skilledmigration/`: **143 PDFs**, extracted from the supplied archive

The official inquiry page lists submissions and can be used to build submitter metadata:

<https://www.aph.gov.au/Parliamentary_Business/Committees/Joint/Migration/Skilledmigration/Submissions>

> **Dataset check:** the supplied archive contains 143 PDF files, while the inquiry page may show a different total. Filenames include variants such as `Sub006.1` and gaps in the numbering. Preserve these source identifiers and verify any webpage-to-file mapping rather than renumbering files.

## Start the Analysis

Open `ANLP_AT1_Template_Sample.ipynb` from this directory. The following setup finds every PDF without depending on the current working directory:

```python
from pathlib import Path

data_dir = Path("data/submissions-skilled-migration/submissions_Skilledmigration")
pdf_paths = sorted(data_dir.glob("*.pdf"))

print(f"PDF files found: {len(pdf_paths)}")
assert len(pdf_paths) == 143, "Unexpected dataset size—check extraction and path."
```

Extract text with `pypdf`, while recording failures instead of stopping the whole run:

```python
from pypdf import PdfReader

documents = []
errors = []

for pdf_path in pdf_paths:
    try:
        reader = PdfReader(pdf_path)
        text = "\n".join(page.extract_text() or "" for page in reader.pages)
        documents.append(
            {
                "submission_id": pdf_path.stem,
                "filename": pdf_path.name,
                "page_count": len(reader.pages),
                "text": text,
            }
        )
    except Exception as exc:
        errors.append({"filename": pdf_path.name, "error": str(exc)})
```

Then create a dataframe and inspect data quality before analysis:

```python
import pandas as pd

df = pd.DataFrame(documents)
df["character_count"] = df["text"].str.len()
df["word_count"] = df["text"].str.split().str.len()

display(df[["submission_id", "page_count", "word_count"]].describe())
display(df.nsmallest(10, "character_count"))
print(f"Extraction errors: {len(errors)}")
```

Some PDFs may contain scanned pages. A very low character count is a signal to inspect the document and, if necessary, use OCR. Record OCR and cleaning choices because they affect reproducibility.

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

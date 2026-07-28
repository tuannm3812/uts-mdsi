"""Create local OCR sidecars for image-based AT1 submissions.

The generated text belongs beside the supplied raw data and is ignored by Git.
Run this script only when the notebook's quality audit identifies low-text
PDFs. The primary notebook will use a matching sidecar when one is available.
"""

import logging
import re
from pathlib import Path

import fitz
from pypdf import PdfReader
from rapidocr_onnxruntime import RapidOCR

MIN_EXTRACTED_CHARACTERS = 500
RENDER_SCALE = 3.0
MIN_OCR_CONFIDENCE = 0.50
DATA_RELATIVE_PATH = Path(
    "data/submissions-skilled-migration/submissions_Skilledmigration"
)
OCR_RELATIVE_PATH = Path("data/ocr_text")

logging.getLogger("pypdf").setLevel(logging.ERROR)


def find_project_root(start: Path) -> Path:
    """Find the AT1 directory from a child working directory."""
    for candidate in (start.resolve(), *start.resolve().parents):
        if (candidate / DATA_RELATIVE_PATH).is_dir():
            return candidate
    raise FileNotFoundError(f"Could not locate {DATA_RELATIVE_PATH}")


def extracted_character_count(path: Path) -> int:
    """Return the number of characters available without OCR."""
    reader = PdfReader(path)
    return len("\n".join(page.extract_text() or "" for page in reader.pages))


def ocr_pdf(path: Path, engine: RapidOCR) -> str:
    """Recognise text from every rendered page in one PDF."""
    document = fitz.open(path)
    pages: list[str] = []
    matrix = fitz.Matrix(RENDER_SCALE, RENDER_SCALE)

    for page_number, page in enumerate(document, start=1):
        pixmap = page.get_pixmap(matrix=matrix, alpha=False)
        results, _ = engine(pixmap.tobytes("png"))
        lines = [
            item[1]
            for item in (results or [])
            if len(item) >= 3 and float(item[2]) >= MIN_OCR_CONFIDENCE
        ]
        pages.append(f"--- PAGE {page_number} ---\n" + "\n".join(lines))

    return "\n\n".join(pages)


def main() -> None:
    """OCR every low-text PDF and write an ignored UTF-8 sidecar."""
    project_root = find_project_root(Path.cwd())
    data_dir = project_root / DATA_RELATIVE_PATH
    output_dir = project_root / OCR_RELATIVE_PATH
    output_dir.mkdir(parents=True, exist_ok=True)

    low_text_paths = [
        path
        for path in sorted(data_dir.glob("*.pdf"))
        if extracted_character_count(path) < MIN_EXTRACTED_CHARACTERS
    ]
    engine = RapidOCR()

    for path in low_text_paths:
        text = ocr_pdf(path, engine)
        output_path = output_dir / f"{path.stem}.txt"
        output_path.write_text(text, encoding="utf-8")
        word_count = len(re.findall(r"[A-Za-z]+", text))
        print(
            f"{path.name}: {len(text):,} OCR characters, "
            f"{word_count:,} alphabetic sequences -> {output_path}"
        )


if __name__ == "__main__":
    main()

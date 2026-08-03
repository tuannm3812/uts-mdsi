from pathlib import Path

import pytest

from scripts.create_nlp_comprehensive_notes import (
    clean_markdown,
    default_output_for,
    infer_session_label,
    pdf_metadata,
)


def test_infer_session_label_from_curated_note():
    path = Path("lectures/session-02-preparation-2026.md")

    assert infer_session_label(path) == "Session 02"


def test_infer_session_label_normalises_single_digit():
    path = Path("lectures/session-2-preparation.md")

    assert infer_session_label(path) == "Session 02"


def test_infer_session_label_rejects_unlabelled_input():
    with pytest.raises(ValueError, match="Cannot infer session number"):
        infer_session_label(Path("lecture-notes.md"))


def test_default_output_uses_session_number():
    path = Path("lectures/session-02-preparation-2026.md")

    assert default_output_for(path).name == "session-02-comprehensive-notes.pdf"
    assert default_output_for(path).parent == path.parent / "handouts"


def test_clean_markdown_strips_blockquote_markers():
    sections = clean_markdown("### Deep Dive — Check\n>\n> **PMI** needs a frequency filter.\n")

    assert sections == [
        ("Deep Dive — Check", ["¶**PMI** needs a frequency filter."])
    ]


def test_pdf_metadata_omits_volatile_timestamps():
    metadata = pdf_metadata("Session 02")

    assert metadata["CreationDate"] is None
    assert metadata["ModDate"] is None

"""Regression tests for the Project 15 literature-review PDF renderer."""

from __future__ import annotations

import importlib.util
import tempfile
import unittest
from pathlib import Path

import fitz
from reportlab.lib import colors
from reportlab.platypus import PageBreak


ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = ROOT / "scripts/render_project15_literature_pdf.py"
SPEC = importlib.util.spec_from_file_location("project15_pdf_renderer", MODULE_PATH)
assert SPEC and SPEC.loader
renderer = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(renderer)


class Project15PdfRendererTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        renderer.register_google_sans(
            Path("/Applications/Google Drive.app/Contents/Resources/GoogleSans-Regular.ttf"),
            Path("/Applications/Google Drive.app/Contents/Resources/GoogleSans-Medium.ttf"),
        )

    def test_google_sans_regular_is_used_for_body_and_medium_for_headings(self) -> None:
        styles = renderer.build_styles()

        self.assertEqual(styles["body"].fontName, "GoogleSans")
        self.assertEqual(styles["list"].fontName, "GoogleSans")
        self.assertEqual(styles["h1"].fontName, "GoogleSansMedium")
        self.assertEqual(styles["h2"].fontName, "GoogleSansMedium")
        self.assertEqual(styles["h3"].fontName, "GoogleSansMedium")

    def test_heading_levels_have_distinct_approved_colours(self) -> None:
        styles = renderer.build_styles()

        self.assertEqual(styles["h1"].textColor, colors.HexColor("#0B57D0"))
        self.assertEqual(styles["h2"].textColor, colors.HexColor("#137F8B"))
        self.assertEqual(styles["h3"].textColor, colors.HexColor("#6554C0"))

    def test_rendered_list_markers_and_text_use_body_aligned_hanging_indent(self) -> None:
        with tempfile.TemporaryDirectory() as temp_dir:
            source = Path(temp_dir) / "source.md"
            output = Path(temp_dir) / "output.pdf"
            source.write_text(
                "# Test\n\nParagraph alignment.\n\n"
                "- A bullet item that wraps across multiple lines because it contains "
                "enough words to exceed a deliberately narrow line width in the PDF.\n\n"
                "1. A numbered item.\n",
                encoding="utf-8",
            )
            renderer.build_pdf(
                source,
                output,
                Path("/Applications/Google Drive.app/Contents/Resources/GoogleSans-Regular.ttf"),
                Path("/Applications/Google Drive.app/Contents/Resources/GoogleSans-Medium.ttf"),
            )
            page = fitz.open(output)[0]
            spans = [
                span
                for block in page.get_text("dict")["blocks"]
                for line in block.get("lines", [])
                for span in line["spans"]
            ]

        paragraph = next(span for span in spans if span["text"] == "Paragraph alignment.")
        bullet = next(span for span in spans if span["text"] == "\u2022")
        bullet_text = next(span for span in spans if span["text"].startswith("A bullet item"))
        number = next(span for span in spans if span["text"] == "1")
        number_text = next(span for span in spans if span["text"] == "A numbered item.")
        self.assertAlmostEqual(bullet["bbox"][0], paragraph["bbox"][0], places=2)
        self.assertAlmostEqual(number["bbox"][0], paragraph["bbox"][0], places=2)
        self.assertGreaterEqual(bullet_text["bbox"][0], paragraph["bbox"][0] + 11.5)
        self.assertGreaterEqual(number_text["bbox"][0], paragraph["bbox"][0] + 11.5)

    def test_only_approved_major_sections_receive_page_breaks(self) -> None:
        source = (
            "# Review\n\n## Project context\nIntro.\n\n"
            "## Paper 1: Terminal-Bench\nPaper.\n\n### Research problem\nDetail.\n\n"
            "## Experimental variables\nVariables.\n\n## References\nSources.\n"
        )
        story = renderer.parse_markdown(source, renderer.build_styles(), 400)
        breaks = [flowable for flowable in story if isinstance(flowable, PageBreak)]

        self.assertEqual(len(breaks), 2)
        self.assertIn(
            "Project significance and real-world analysis",
            renderer.PAGE_BREAK_H2,
        )

    def test_markdown_bold_maps_to_registered_medium_font(self) -> None:
        marked_up = renderer.inline_markup("Use **Terminal-Bench**, **Harbor**, and `JSONL`.")

        self.assertIn("<font name='GoogleSansMedium'>Terminal-Bench</font>", marked_up)
        self.assertIn("<font name='GoogleSansMedium'>Harbor</font>", marked_up)
        self.assertIn("<font name='Courier'>JSONL</font>", marked_up)


if __name__ == "__main__":
    unittest.main()

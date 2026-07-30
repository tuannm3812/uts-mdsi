"""Regression tests for the Project 15 literature-review PDF renderer."""

from __future__ import annotations

import importlib.util
import unittest
from pathlib import Path

from reportlab.lib import colors


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

    def test_lists_use_one_safe_hanging_indent(self) -> None:
        flowable = renderer.build_list(["first item"], False, renderer.build_styles())

        self.assertEqual(flowable._leftIndent, 14)
        self.assertEqual(flowable._bulletDedent, 6)
        self.assertEqual(flowable._flowables[0]._params["leftIndent"], 0)

    def test_markdown_bold_maps_to_registered_medium_font(self) -> None:
        marked_up = renderer.inline_markup("Use **Terminal-Bench**, **Harbor**, and `JSONL`.")

        self.assertIn("<font name='GoogleSansMedium'>Terminal-Bench</font>", marked_up)
        self.assertIn("<font name='GoogleSansMedium'>Harbor</font>", marked_up)
        self.assertIn("<font name='Courier'>JSONL</font>", marked_up)


if __name__ == "__main__":
    unittest.main()

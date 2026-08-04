#!/usr/bin/env python3
"""Render the 36126 supervisor findings brief as a styled A4 PDF."""

from __future__ import annotations

import argparse
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import BaseDocTemplate, Frame, PageTemplate

from render_project15_literature_pdf import (
    GOOGLE_BORDER,
    GOOGLE_MUTED,
    build_styles,
    parse_markdown,
    register_google_sans,
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--font", type=Path, required=True)
    return parser.parse_args()


def add_page_chrome(canvas: Canvas, document: BaseDocTemplate) -> None:
    canvas.saveState()
    width, _ = A4
    canvas.setStrokeColor(GOOGLE_BORDER)
    canvas.setLineWidth(0.35)
    canvas.line(18 * mm, 15.5 * mm, width - 18 * mm, 15.5 * mm)
    canvas.setFont("GoogleSans", 7.2)
    canvas.setFillColor(GOOGLE_MUTED)
    canvas.drawString(18 * mm, 10.5 * mm, "36126 Innovation Lab: Research Project")
    canvas.drawRightString(
        width - 18 * mm,
        10.5 * mm,
        f"Supervisor findings brief  |  {canvas.getPageNumber()}",
    )
    canvas.restoreState()


class SupervisorBriefTemplate(BaseDocTemplate):
    def __init__(self, filename: str) -> None:
        super().__init__(
            filename,
            pagesize=A4,
            leftMargin=18 * mm,
            rightMargin=18 * mm,
            topMargin=17 * mm,
            bottomMargin=21 * mm,
            title="Supervisor Findings Brief: Fire-Hotspot Reliability in NSW",
            author="Tuan Nguyen",
            subject="36126 Innovation Lab Research Project",
        )
        frame = Frame(
            self.leftMargin,
            self.bottomMargin,
            self.width,
            self.height,
            id="content",
        )
        self.addPageTemplates(
            PageTemplate(id="supervisor-brief", frames=[frame], onPage=add_page_chrome)
        )


def main() -> None:
    args = parse_args()
    if not args.input.is_file():
        raise FileNotFoundError(f"Markdown input not found: {args.input}")
    register_google_sans(args.font, args.font)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    styles = build_styles()
    document = SupervisorBriefTemplate(str(args.output))
    story = parse_markdown(args.input.read_text(encoding="utf-8"), styles, document.width)
    document.build(story)


if __name__ == "__main__":
    main()

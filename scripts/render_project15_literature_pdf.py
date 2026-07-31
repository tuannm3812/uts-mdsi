#!/usr/bin/env python3
"""Render the Project 15 Markdown literature review as a styled A4 PDF."""

from __future__ import annotations

import argparse
import html
import re
import sys
from pathlib import Path
from typing import Iterable

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.pdfmetrics import registerFontFamily
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import (
    BaseDocTemplate,
    Flowable,
    HRFlowable,
    KeepTogether,
    ListFlowable,
    ListItem,
    PageBreak,
    PageTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle,
)
from reportlab.platypus.frames import Frame


GOOGLE_BLUE = colors.HexColor("#0B57D0")
GOOGLE_TEAL = colors.HexColor("#137F8B")
GOOGLE_VIOLET = colors.HexColor("#6554C0")
GOOGLE_DARK = colors.HexColor("#202124")
GOOGLE_TEXT = colors.HexColor("#3C4043")
GOOGLE_MUTED = colors.HexColor("#5F6368")
GOOGLE_LIGHT = colors.HexColor("#E8F0FE")
GOOGLE_BORDER = colors.HexColor("#DADCE0")
GOOGLE_SURFACE = colors.HexColor("#F8F9FA")

PAGE_BREAK_H2 = {
    "Paper 1: Terminal-Bench",
    "Project significance and real-world analysis",
    "Paper 2: SWE-agent",
    "Paper 3: OpenHands",
    "Paper 4: Agentless",
    "Paper 5: OpenHands Software Agent SDK",
    "Cross-paper synthesis",
    "Implications for our custom harness",
    "Evaluation framework",
    "Reproducibility, cost, and validity",
    "Research questions and hypotheses",
    "Six-member reading allocation",
    "References",
    "Ý nghĩa dự án và phân tích thực tế",
    "Bài báo 1: Terminal-Bench",
    "Bài báo 2: SWE-agent",
    "Bài báo 3: OpenHands",
    "Bài báo 4: Agentless",
    "Bài báo 5: OpenHands Software Agent SDK",
    "Tổng hợp liên bài báo",
    "Hàm ý đối với harness tùy chỉnh của nhóm",
    "Khung đánh giá",
    "Khả năng tái tạo, chi phí và hiệu lực",
    "Câu hỏi nghiên cứu và giả thuyết",
    "Phân bổ đọc sáu thành viên",
    "Tài liệu tham khảo",
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input", type=Path, required=True, help="Source Markdown file")
    parser.add_argument("--output", type=Path, required=True, help="Destination PDF file")
    parser.add_argument(
        "--font-regular", type=Path, required=True, help="Google Sans Regular TTF file"
    )
    parser.add_argument(
        "--font-medium", type=Path, required=True, help="Google Sans Medium TTF file"
    )
    parser.add_argument(
        "--language",
        choices=("en", "vi"),
        default="en",
        help="Language used for PDF metadata, header, and footer text",
    )
    return parser.parse_args()


def register_google_sans(regular_path: Path, medium_path: Path) -> None:
    for font_path in (regular_path, medium_path):
        if not font_path.is_file():
            raise FileNotFoundError(f"Google Sans font not found: {font_path}")
    pdfmetrics.registerFont(TTFont("GoogleSans", str(regular_path)))
    pdfmetrics.registerFont(TTFont("GoogleSansMedium", str(medium_path)))
    registerFontFamily(
        "GoogleSans",
        normal="GoogleSans",
        bold="GoogleSansMedium",
        italic="GoogleSans",
        boldItalic="GoogleSansMedium",
    )


def build_styles() -> dict[str, ParagraphStyle]:
    sample = getSampleStyleSheet()
    return {
        "title": ParagraphStyle(
            "Title",
            parent=sample["Title"],
            fontName="GoogleSansMedium",
            fontSize=25,
            leading=30,
            textColor=GOOGLE_DARK,
            alignment=TA_LEFT,
            spaceAfter=10,
        ),
        "subtitle": ParagraphStyle(
            "Subtitle",
            parent=sample["Normal"],
            fontName="GoogleSans",
            fontSize=11,
            leading=16,
            textColor=GOOGLE_MUTED,
            spaceAfter=5,
        ),
        "h1": ParagraphStyle(
            "Heading1",
            parent=sample["Heading1"],
            fontName="GoogleSansMedium",
            fontSize=17,
            leading=21,
            textColor=GOOGLE_BLUE,
            spaceBefore=13,
            spaceAfter=7,
            keepWithNext=True,
        ),
        "h2": ParagraphStyle(
            "Heading2",
            parent=sample["Heading2"],
            fontName="GoogleSansMedium",
            fontSize=13,
            leading=17,
            textColor=GOOGLE_TEAL,
            spaceBefore=10,
            spaceAfter=5,
            keepWithNext=True,
        ),
        "h3": ParagraphStyle(
            "Heading3",
            parent=sample["Heading3"],
            fontName="GoogleSansMedium",
            fontSize=11,
            leading=15,
            textColor=GOOGLE_VIOLET,
            spaceBefore=8,
            spaceAfter=4,
            keepWithNext=True,
        ),
        "body": ParagraphStyle(
            "Body",
            parent=sample["BodyText"],
            fontName="GoogleSans",
            fontSize=9.2,
            leading=13.3,
            textColor=GOOGLE_TEXT,
            spaceAfter=5.5,
            allowWidows=0,
            allowOrphans=0,
        ),
        "quote": ParagraphStyle(
            "Quote",
            parent=sample["BodyText"],
            fontName="GoogleSans",
            fontSize=9.2,
            leading=13.3,
            textColor=GOOGLE_DARK,
            backColor=GOOGLE_LIGHT,
            borderColor=GOOGLE_BLUE,
            borderWidth=0,
            borderPadding=(7, 9, 7, 11),
            leftIndent=4,
            spaceBefore=4,
            spaceAfter=8,
        ),
        "code": ParagraphStyle(
            "Code",
            parent=sample["Code"],
            fontName="Courier",
            fontSize=7.6,
            leading=10.2,
            textColor=GOOGLE_DARK,
            backColor=GOOGLE_SURFACE,
            borderColor=GOOGLE_BORDER,
            borderWidth=0.5,
            borderPadding=7,
            leftIndent=4,
            rightIndent=4,
            spaceBefore=4,
            spaceAfter=7,
        ),
        "list": ParagraphStyle(
            "List",
            parent=sample["BodyText"],
            fontName="GoogleSans",
            fontSize=9.1,
            leading=12.8,
            textColor=GOOGLE_TEXT,
            leftIndent=12,
        ),
        "table_header": ParagraphStyle(
            "TableHeader",
            parent=sample["BodyText"],
            fontName="GoogleSansMedium",
            fontSize=7.6,
            leading=9.5,
            textColor=colors.white,
            alignment=TA_LEFT,
        ),
        "table_body": ParagraphStyle(
            "TableBody",
            parent=sample["BodyText"],
            fontName="GoogleSans",
            fontSize=7.3,
            leading=9.4,
            textColor=GOOGLE_TEXT,
            alignment=TA_LEFT,
        ),
        "footer": ParagraphStyle(
            "Footer",
            parent=sample["Normal"],
            fontName="GoogleSans",
            fontSize=7.3,
            leading=9,
            textColor=GOOGLE_MUTED,
        ),
    }


def inline_markup(value: str) -> str:
    """Escape Markdown text and retain a small, safe inline subset."""
    escaped = html.escape(value.strip())
    escaped = re.sub(r"`([^`]+)`", r"<font name='Courier'>\1</font>", escaped)
    escaped = re.sub(
        r"\*\*([^*]+)\*\*",
        r"<font name='GoogleSansMedium'>\1</font>",
        escaped,
    )
    escaped = re.sub(r"\*([^*]+)\*", r"<i>\1</i>", escaped)
    escaped = re.sub(
        r"(https?://[^\s<]+)",
        r"<link href='\1' color='#0B57D0'>\1</link>",
        escaped,
    )
    return escaped


def split_table_row(line: str) -> list[str]:
    return [part.strip() for part in line.strip().strip("|").split("|")]


def is_table_separator(line: str) -> bool:
    cells = split_table_row(line)
    return bool(cells) and all(re.fullmatch(r":?-{3,}:?", cell) for cell in cells)


def table_widths(column_count: int, available: float) -> list[float]:
    if column_count == 2:
        return [available * 0.27, available * 0.73]
    if column_count == 3:
        return [available * 0.18, available * 0.42, available * 0.40]
    if column_count == 4:
        return [available * 0.17, available * 0.29, available * 0.27, available * 0.27]
    if column_count == 5:
        return [available * 0.14, available * 0.21, available * 0.21, available * 0.22, available * 0.22]
    if column_count == 6:
        return [available / 6] * 6
    return [available / column_count] * column_count


def build_table(
    rows: list[list[str]],
    styles: dict[str, ParagraphStyle],
    available_width: float,
) -> Table:
    column_count = max(len(row) for row in rows)
    normalised = [row + [""] * (column_count - len(row)) for row in rows]
    data: list[list[Paragraph]] = []
    for row_index, row in enumerate(normalised):
        style = styles["table_header"] if row_index == 0 else styles["table_body"]
        data.append([Paragraph(inline_markup(cell), style) for cell in row])
    table = Table(
        data,
        colWidths=table_widths(column_count, available_width),
        repeatRows=1,
        hAlign="LEFT",
        splitByRow=1,
    )
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), GOOGLE_BLUE),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 5),
                ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                ("TOPPADDING", (0, 0), (-1, -1), 4),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                ("LINEBELOW", (0, 0), (-1, 0), 0.7, GOOGLE_BLUE),
                ("LINEBELOW", (0, 1), (-1, -2), 0.25, GOOGLE_BORDER),
                ("BACKGROUND", (0, 1), (-1, -1), colors.white),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, GOOGLE_SURFACE]),
            ]
        )
    )
    return table


def build_list(
    items: Iterable[str],
    ordered: bool,
    styles: dict[str, ParagraphStyle],
) -> ListFlowable:
    list_items = [
        ListItem(Paragraph(inline_markup(item), styles["list"]), leftIndent=0)
        for item in items
    ]
    return ListFlowable(
        list_items,
        bulletType="1" if ordered else "bullet",
        start="1" if ordered else "\u2022",
        leftIndent=14,
        bulletDedent=0,
        bulletFontName="GoogleSans",
        bulletFontSize=8,
        bulletColor=GOOGLE_BLUE,
        spaceAfter=6,
    )


def parse_markdown(
    source: str,
    styles: dict[str, ParagraphStyle],
    available_width: float,
) -> list[Flowable]:
    lines = source.splitlines()
    story: list[Flowable] = []
    paragraph_lines: list[str] = []
    list_items: list[str] = []
    list_ordered = False
    code_lines: list[str] = []
    in_code = False
    table_rows: list[list[str]] = []
    first_heading = True

    def flush_paragraph() -> None:
        if paragraph_lines:
            text = " ".join(part.strip() for part in paragraph_lines)
            story.append(Paragraph(inline_markup(text), styles["body"]))
            paragraph_lines.clear()

    def flush_list() -> None:
        nonlocal list_ordered
        if list_items:
            story.append(build_list(list_items, list_ordered, styles))
            list_items.clear()
            list_ordered = False

    def flush_table() -> None:
        if table_rows:
            story.append(Spacer(1, 2))
            story.append(build_table(table_rows, styles, available_width))
            story.append(Spacer(1, 6))
            table_rows.clear()

    for index, raw_line in enumerate(lines):
        line = raw_line.rstrip()

        if line.startswith("```"):
            flush_paragraph()
            flush_list()
            flush_table()
            if in_code:
                story.append(
                    Paragraph(
                        "<br/>".join(html.escape(value) or " " for value in code_lines),
                        styles["code"],
                    )
                )
                code_lines.clear()
            in_code = not in_code
            continue

        if in_code:
            code_lines.append(line)
            continue

        if line.startswith("|") and line.endswith("|"):
            flush_paragraph()
            flush_list()
            if index + 1 < len(lines) and is_table_separator(lines[index + 1]):
                table_rows.append(split_table_row(line))
            elif is_table_separator(line):
                continue
            elif table_rows:
                table_rows.append(split_table_row(line))
            else:
                paragraph_lines.append(line)
            continue
        flush_table()

        if not line.strip():
            flush_paragraph()
            flush_list()
            continue

        heading_match = re.match(r"^(#{1,3})\s+(.+)$", line)
        if heading_match:
            flush_paragraph()
            flush_list()
            level = len(heading_match.group(1))
            text = heading_match.group(2).strip()
            if level == 1 and first_heading:
                story.extend(
                    [
                        Spacer(1, 28 * mm),
                        HRFlowable(
                            width=24 * mm,
                            thickness=3,
                            color=GOOGLE_BLUE,
                            hAlign="LEFT",
                            spaceAfter=9,
                        ),
                        Paragraph(inline_markup(text), styles["title"]),
                    ]
                )
                first_heading = False
            else:
                if level == 2 and text in PAGE_BREAK_H2:
                    story.append(PageBreak())
                story.append(Paragraph(inline_markup(text), styles[f"h{level}"]))
            continue

        if line.startswith("> "):
            flush_paragraph()
            flush_list()
            story.append(Paragraph(inline_markup(line[2:]), styles["quote"]))
            continue

        unordered = re.match(r"^[-*]\s+(.+)$", line)
        ordered = re.match(r"^\d+\.\s+(.+)$", line)
        if unordered or ordered:
            flush_paragraph()
            this_ordered = bool(ordered)
            if list_items and this_ordered != list_ordered:
                flush_list()
            list_ordered = this_ordered
            list_items.append((ordered or unordered).group(1))
            continue

        if re.match(r"^\*\*[^*]+:\*\*", line):
            flush_paragraph()
            paragraph_lines.append(line)
            continue

        paragraph_lines.append(line)

    flush_paragraph()
    flush_list()
    flush_table()
    if code_lines:
        story.append(
            Paragraph(
                "<br/>".join(html.escape(value) or " " for value in code_lines),
                styles["code"],
            )
        )
    return story


def add_page_chrome(canvas: Canvas, document: BaseDocTemplate) -> None:
    canvas.saveState()
    width, height = A4
    canvas.setStrokeColor(GOOGLE_BORDER)
    canvas.setLineWidth(0.35)
    canvas.line(18 * mm, 15.5 * mm, width - 18 * mm, 15.5 * mm)
    canvas.setFont("GoogleSans", 7.2)
    canvas.setFillColor(GOOGLE_MUTED)
    language = getattr(document, "language", "en")
    canvas.drawString(
        18 * mm,
        10.5 * mm,
        "36127 Capstone - Project 15",
    )
    canvas.drawRightString(
        width - 18 * mm,
        10.5 * mm,
        (
            f"Tổng quan tài liệu  |  {canvas.getPageNumber()}"
            if language == "vi"
            else f"Literature review  |  {canvas.getPageNumber()}"
        ),
    )
    canvas.restoreState()


class LiteratureDocTemplate(BaseDocTemplate):
    def __init__(self, filename: str, language: str = "en") -> None:
        self.language = language
        super().__init__(
            filename,
            pagesize=A4,
            leftMargin=18 * mm,
            rightMargin=18 * mm,
            topMargin=17 * mm,
            bottomMargin=21 * mm,
            title=(
                "Tổng quan tài liệu Project 15 Terminal-Bench"
                if language == "vi"
                else "Project 15 Terminal-Bench Literature Review"
            ),
            author="Tuan Nguyen and Project 15 Team",
            subject="36127 Innovation Lab Capstone Project",
        )
        frame = Frame(
            self.leftMargin,
            self.bottomMargin,
            self.width,
            self.height,
            id="content",
        )
        self.addPageTemplates(
            PageTemplate(id="literature", frames=[frame], onPage=add_page_chrome)
        )


def build_pdf(
    input_path: Path,
    output_path: Path,
    regular_font_path: Path,
    medium_font_path: Path,
    language: str = "en",
) -> None:
    if not input_path.is_file():
        raise FileNotFoundError(f"Markdown input not found: {input_path}")
    register_google_sans(regular_font_path, medium_font_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    styles = build_styles()
    source = input_path.read_text(encoding="utf-8")
    doc = LiteratureDocTemplate(str(output_path), language=language)
    story = parse_markdown(source, styles, doc.width)
    doc.build(story)


def main() -> int:
    args = parse_args()
    try:
        build_pdf(
            args.input,
            args.output,
            args.font_regular,
            args.font_medium,
            language=args.language,
        )
    except (FileNotFoundError, OSError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

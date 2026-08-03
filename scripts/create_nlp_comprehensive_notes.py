#!/usr/bin/env python3
"""Render a NotebookLM text export as comprehensive Google Sans lecture notes."""

from __future__ import annotations

import argparse
import os
import re
import tempfile
from pathlib import Path
from textwrap import wrap

os.environ.setdefault("MPLCONFIGDIR", str(Path(tempfile.gettempdir()) / "uts-mdsi-matplotlib"))

import matplotlib

matplotlib.use("pdf")
import matplotlib.font_manager as fm
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.textpath import TextToPath


ROOT = Path(__file__).resolve().parents[1]
FONT_DIR = Path("/Applications/Google Drive.app/Contents/Resources")
REGULAR = FONT_DIR / "GoogleSans-Regular.ttf"
MEDIUM = FONT_DIR / "GoogleSans-Medium.ttf"

BLUE = "#3066BE"
INK = "#17243A"
MUTED = "#5A6577"
PALE = "#EAF1FB"
RULE = "#D5DCE7"
# Conventional light-theme syntax colours (aligned with common editor palettes).
CODE_KEYWORD = "#0000FF"
CODE_STRING = "#A31515"
CODE_NUMBER = "#098658"
CODE_MODULE = "#267F99"
CODE_FUNCTION = "#795E26"
CODE_COMMENT = "#008000"

SECTION_TITLES = {
    "Introduction to Applied Natural Language Processing (NLP)",
    "Core Text Processing and Feature Extraction",
    "Deep Dive: N-Grams, Relationships, and Word Associations",
    "Visualisation and Storytelling for Text Data",
    "Machine Learning Approaches in NLP",
    "Deep Learning, Language Models, and LLMs",
    "Ethics, Fairness, and Sustainability in NLP",
    "Subject Learning Objectives (SLOs)",
}

EQUATIONS = {
    "Deep Dive: N-Grams, Relationships, and Word Associations": [
        (r"$\mathrm{PMI}(x,y)=\log_{2}\!\left(\frac{P(x,y)}{P(x)P(y)}\right)$",
         "Positive PMI indicates co-occurrence above the independence baseline."),
    ],
    "Machine Learning Approaches in NLP": [
        (r"$d_{\mathrm{Euclidean}}(\mathbf{x},\mathbf{a})="
         r"\sqrt{\sum_{i=1}^{n}(x_i-a_i)^2}$",
         "Straight-line distance; scale-sensitive."),
        (r"$d_{\mathrm{Manhattan}}(\mathbf{x},\mathbf{a})="
         r"\sum_{i=1}^{n}|x_i-a_i|$",
         "Axis-aligned distance."),
        (r"$d_{\mathrm{cosine}}(\mathbf{x},\mathbf{a})="
         r"1-\frac{\mathbf{x}\cdot\mathbf{a}}{\|\mathbf{x}\|_2\|\mathbf{a}\|_2}$",
         "Compares direction rather than vector magnitude."),
    ],
    "Deep Learning, Language Models, and LLMs": [
        (r"$\mathbf{h}_{i}=\mathbf{e}_{i}+\mathbf{p}_{i}$",
         "A token embedding plus positional encoding gives a position-aware representation."),
        (r"$\mathrm{Attention}(Q,K,V)="
         r"\mathrm{softmax}\!\left(\frac{QK^{\mathsf{T}}}{\sqrt{d_k}}\right)V$",
         "Scaled dot-product attention; supplementary context for the slide’s Q, K, and V discussion."),
    ],
    "Deep Dive — From Counts to Comparable Measures": [
        (r"$N_d=\sum_{i=1}^{|d|}1=|d|$",
         "Document length: the number of tokens in document d."),
        (r"$\mathrm{TF}(t,d)=f_{t,d}$",
         "Absolute term frequency: the number of occurrences of term t in document d."),
        (r"$\mathrm{RelativeTF}(t,d)=\frac{f_{t,d}}{\sum_{t' \in d}f_{t',d}}$",
         "Relative frequency controls for documents with different lengths."),
        (r"$\mathrm{TTR}(d)=\frac{|V_d|}{N_d}$",
         "Type–token ratio: unique token types divided by all tokens; it is length-sensitive."),
    ],
    "2.3 Word Association and Pointwise Mutual Information": [
        (r"$\mathrm{PMI}(x,y)=\log_{2}\!\left(\frac{P(x,y)}{P(x)P(y)}\right)$",
         "Association relative to independence; the log base controls the unit."),
    ],
    "4.2 Term Frequency–Inverse Document Frequency": [
        (r"$\mathrm{TF}(t,d)=\frac{f_{t,d}}{\sum_{t'\in d}f_{t',d}}$",
         "One common normalised term-frequency definition."),
        (r"$\mathrm{IDF}(t)=\log\!\left(\frac{N}{\mathrm{df}(t)}\right)$",
         "N is corpus size; df(t) is the number of documents containing t."),
        (r"$\mathrm{TFIDF}(t,d)=\mathrm{TF}(t,d)\times\mathrm{IDF}(t)$",
         "Distinctive-in-document weighting; implementations may smooth or normalise."),
    ],
    "7.2 Similarity and Distance in Text Space": [
        (r"$d_{2}(\mathbf{x},\mathbf{y})=\sqrt{\sum_i(x_i-y_i)^2}$",
         "Euclidean distance: straight-line separation in feature space."),
        (r"$d_{1}(\mathbf{x},\mathbf{y})=\sum_i|x_i-y_i|$",
         "Manhattan distance: coordinate-wise absolute separation."),
        (r"$d_{\cos}(\mathbf{x},\mathbf{y})=1-\frac{\mathbf{x}\cdot\mathbf{y}}{\|\mathbf{x}\|_2\|\mathbf{y}\|_2}$",
         "Cosine distance compares direction and reduces magnitude effects."),
    ],
    "9.2 Elbow and Silhouette Methods": [
        (r"$s(i)=\frac{b(i)-a(i)}{\max\{a(i),b(i)\}}$",
         "Silhouette ranges from -1 to 1; larger values indicate clearer separation."),
    ],
}


def infer_session_label(path: Path) -> str:
    """Return a zero-padded session label inferred from a source filename."""
    match = re.search(r"session[-_ ](\d+)", path.stem, flags=re.IGNORECASE)
    if not match:
        raise ValueError(f"Cannot infer session number from: {path.name}")
    return f"Session {int(match.group(1)):02d}"


def default_output_for(path: Path) -> Path:
    """Return the standard handout output path for a curated session note."""
    session = infer_session_label(path).lower().replace(" ", "-")
    return path.parent / "handouts" / f"{session}-comprehensive-notes.pdf"


def pdf_metadata(session_label: str) -> dict[str, str | None]:
    """Return stable PDF metadata so identical notes render reproducibly."""
    return {
        "Title": f"36118 ANLP {session_label} Comprehensive Notes",
        "Author": "36118 Applied Natural Language Processing",
        "Subject": "Study-ready lecture notes",
        "CreationDate": None,
        "ModDate": None,
    }


def register_fonts() -> tuple[fm.FontProperties, fm.FontProperties]:
    for path in (REGULAR, MEDIUM):
        if not path.exists():
            raise FileNotFoundError(f"Required Google Sans font not found: {path}")
        fm.fontManager.addfont(str(path))
    regular = fm.FontProperties(fname=str(REGULAR))
    medium = fm.FontProperties(fname=str(MEDIUM))
    plt.rcParams.update({
        "font.family": regular.get_name(),
        "mathtext.fontset": "stix",
        "pdf.fonttype": 42,
    })
    return regular, medium


def clean_export(text: str) -> list[tuple[str, list[str]]]:
    text = text.replace("\r\n", "\n")
    text = text.replace("∣", "|")
    text = re.sub(r"\n-{20,}\n", "\n§SECTION§\n", text)
    text = re.sub(
        r"PMI Formula:.*?PMI > 0:",
        "PMI > 0:",
        text,
        flags=re.S,
    )
    text = re.sub(
        r"Euclidean Distance:.*?\n\\.",
        "Euclidean Distance: See the correctly typeset equation below.",
        text,
        count=1,
        flags=re.S,
    )
    text = re.sub(
        r"Manhattan Distance:.*?\n\\.",
        "Manhattan Distance: See the correctly typeset equation below.",
        text,
        count=1,
        flags=re.S,
    )
    text = re.sub(
        r"Cosine Distance:.*?\n\\.",
        "Cosine Distance: See the correctly typeset equation below.",
        text,
        count=1,
        flags=re.S,
    )

    sections: list[tuple[str, list[str]]] = []
    for block in text.split("§SECTION§"):
        lines = [line.strip() for line in block.splitlines()]
        lines = [line for line in lines if line and line != "."]
        if not lines:
            continue
        title = lines.pop(0)
        if title not in SECTION_TITLES:
            title = title.rstrip()
        merged: list[str] = []
        for line in lines:
            if len(line) <= 2:
                continue
            if merged and merged[-1].endswith((",", "—", "–")):
                merged[-1] += " " + line
            else:
                merged.append(line)
        sections.append((title, merged))
    return sections


def clean_markdown(text: str) -> list[tuple[str, list[str]]]:
    """Turn the curated Session 1 Markdown into printable sections."""
    text = re.sub(r"^---.*?---\s*", "", text, count=1, flags=re.S)
    sections: list[tuple[str, list[str]]] = []
    title = ""
    items: list[str] = []
    paragraph: list[str] = []
    bullet: list[str] = []
    code_lines: list[str] = []
    in_code = False

    def plain(value: str) -> str:
        return value.replace("`", "")

    def flush_bullet() -> None:
        nonlocal bullet
        if bullet:
            items.append(plain(" ".join(bullet)))
            bullet = []

    def flush_paragraph() -> None:
        nonlocal paragraph
        if paragraph:
            items.append("¶" + plain(" ".join(paragraph)))
            paragraph = []

    def flush_section() -> None:
        nonlocal items
        flush_paragraph()
        if title:
            sections.append((title, items))
        items = []

    for raw in text.splitlines():
        line = raw.strip()
        if line == ">":
            line = ""
        elif line.startswith("> "):
            line = line[2:].strip()
        if line.startswith("```"):
            flush_bullet()
            flush_paragraph()
            if in_code and code_lines:
                items.append("⌘" + "\n".join(code_lines))
                code_lines = []
            in_code = not in_code
            continue
        if in_code:
            if line:
                code_lines.append(plain(line))
            continue
        if line.startswith("# "):
            continue
        if line.startswith(("## ", "### ")):
            flush_bullet()
            flush_section()
            title = line.lstrip("#").strip()
            continue
        if not line:
            flush_bullet()
            flush_paragraph()
        elif re.match(r"^[-*]\s+", line):
            flush_bullet()
            flush_paragraph()
            bullet = [re.sub(r"^[-*]\s+", "", line)]
        elif re.match(r"^\d+\.\s+", line):
            flush_bullet()
            flush_paragraph()
            bullet = ["№" + line]
        elif bullet:
            bullet.append(line)
        else:
            paragraph.append(line)
    flush_bullet()
    flush_section()
    return sections


class NotesWriter:
    def __init__(
        self,
        pdf: PdfPages,
        regular: fm.FontProperties,
        medium: fm.FontProperties,
        session_label: str,
    ):
        self.pdf = pdf
        self.regular = regular
        self.medium = medium
        self.session_label = session_label
        self.code = fm.FontProperties(fname="/System/Library/Fonts/Menlo.ttc")
        self.page_no = 0
        self.fig = None
        self.ax = None
        self.y = 0.0

    def new_page(self, section: str = "") -> None:
        if self.fig is not None:
            self.finish_page()
        self.page_no += 1
        self.fig = plt.figure(figsize=(8.27, 11.69), facecolor="white")
        self.ax = self.fig.add_axes([0, 0, 1, 1])
        self.ax.set_xlim(0, 1)
        self.ax.set_ylim(0, 1)
        self.ax.set_axis_off()
        self.ax.add_patch(plt.Rectangle((0, 0), 0.018, 1, color=BLUE, transform=self.ax.transAxes))
        self.ax.text(0.065, 0.965, "36118  |  APPLIED NATURAL LANGUAGE PROCESSING",
                     fontsize=8.5, color=BLUE, fontproperties=self.medium, va="top")
        if section:
            self.ax.text(0.935, 0.965, section.upper(), fontsize=7.5, color=MUTED,
                         fontproperties=self.regular, ha="right", va="top")
        self.ax.plot([0.065, 0.935], [0.938, 0.938], color=RULE, lw=0.8)
        self.y = 0.90

    def finish_page(self) -> None:
        self.ax.text(0.065, 0.035, f"{self.session_label} • Study-ready lecture notes",
                     fontsize=7.5, color=MUTED, fontproperties=self.regular)
        self.ax.text(0.935, 0.035, f"{self.page_no:02d}", fontsize=7.5, color=MUTED,
                     fontproperties=self.regular, ha="right")
        self.pdf.savefig(self.fig, bbox_inches=None)
        plt.close(self.fig)
        self.fig = None

    def need(self, height: float, section: str) -> None:
        if self.fig is None or self.y - height < 0.075:
            self.new_page(section)

    def section_title(self, title: str, attach_next: bool = False,
                      suppress_before: bool = False) -> None:
        deep_dive = "Deep Dive" in title
        subsection = bool(re.match(r"^\d+\.\d+\s", title))
        required = 0.145 if deep_dive else (0.155 if subsection else 0.175)
        self.need(required, title)
        if self.y < 0.895 and not suppress_before:
            self.y -= 0.015
        size = 12 if deep_dive else (13.5 if subsection else 17)
        color = BLUE if deep_dive or subsection else INK
        if deep_dive:
            self.ax.add_patch(plt.Rectangle((0.065, self.y - 0.031), 0.006, 0.040,
                                           color=BLUE, transform=self.ax.transAxes))
            x = 0.080
        else:
            x = 0.065
        self.ax.text(x, self.y, title, fontsize=size, color=color,
                     fontproperties=self.medium, va="top")
        if attach_next:
            self.y -= 0.038
        else:
            self.y -= 0.040 if deep_dive else (0.038 if subsection else 0.045)
    def text_width(self, value: str, prop: fm.FontProperties, size: float) -> float:
        if not value:
            return 0.0
        sized = prop.copy()
        sized.set_size(size)
        width, _, _ = TextToPath().get_text_width_height_descent(value, sized, ismath=False)
        return width / (8.27 * 72)

    def rich_lines(self, value: str, max_width: float, size: float = 11):
        parts = re.split(r"(\*\*.*?\*\*)", value)
        words: list[tuple[str, bool]] = []
        for part in parts:
            if not part:
                continue
            bold = part.startswith("**") and part.endswith("**")
            content = part[2:-2] if bold else part
            words.extend((word, bold) for word in content.split())
        lines: list[list[tuple[str, bool]]] = [[]]
        width = 0.0
        space = self.text_width(" ", self.regular, size)
        for word, bold in words:
            prop = self.medium if bold else self.regular
            word_width = self.text_width(word, prop, size)
            extra = word_width + (space if lines[-1] else 0)
            if lines[-1] and width + extra > max_width:
                lines.append([])
                width = 0.0
                extra = word_width
            lines[-1].append((word, bold))
            width += extra
        return lines, space

    def code_segments(self, line: str):
        keywords = {
            "and", "as", "break", "class", "continue", "def", "elif", "else",
            "except", "False", "for", "from", "if", "import", "in", "is",
            "lambda", "None", "not", "or", "pass", "raise", "return", "True",
            "try", "while", "with", "yield",
        }
        libraries = {
            "nltk", "re", "regex", "spacy", "pandas", "pd",
        }
        functions = {
            "BeautifulSoup", "sent_tokenize", "word_tokenize", "pos_tag",
            "findall", "FreqDist",
        }
        pattern = re.compile(
            r"(#.*$|\"(?:\\.|[^\"\\])*\"|'(?:\\.|[^'\\])*'|"
            r"\b\d+(?:\.\d+)?\b|\b[A-Za-z_]\w*\b)"
        )
        segments = []
        last = 0
        for match in pattern.finditer(line):
            if match.start() > last:
                segments.append((line[last:match.start()], INK))
            token = match.group(0)
            if token.startswith("#"):
                color = CODE_COMMENT
            elif token.startswith(("'", '"')):
                color = CODE_STRING
            elif token in keywords:
                color = CODE_KEYWORD
            elif token in libraries:
                color = CODE_MODULE
            elif token in functions:
                color = CODE_FUNCTION
            elif token[0].isdigit():
                color = CODE_NUMBER
            else:
                color = INK
            segments.append((token, color))
            last = match.end()
        if last < len(line):
            segments.append((line[last:], INK))
        return segments

    def item(self, text: str, section: str) -> None:
        paragraph = text.startswith("¶")
        numbered = text.startswith("№")
        code = text.startswith("⌘")
        body = text[1:] if paragraph or numbered or code else text
        deep_dive = "Deep Dive" in section
        if code:
            lines = body.splitlines() or [""]
            code_size = 9.5
            line_height = 0.016
            height = line_height * len(lines) + 0.012
            self.need(height, section)
            self.ax.add_patch(plt.Rectangle((0.065, self.y - height + 0.003), 0.87, height + 0.006,
                                           color="#F3F5F8", transform=self.ax.transAxes, zorder=0))
            for i, line in enumerate(lines):
                cursor = 0.082
                for segment, color in self.code_segments(line):
                    self.ax.text(cursor, self.y - i * line_height, segment, fontsize=code_size, color=color,
                                 fontproperties=self.code, va="top", zorder=2)
                    cursor += self.text_width(segment, self.code, code_size)
            self.y -= height
            return
        x = 0.080 if deep_dive else (0.065 if paragraph or numbered else 0.088)
        max_x = 0.920 if deep_dive else 0.935
        lines, space = self.rich_lines(body, max_x - x)
        body_size = 11
        line_height = 0.014
        gap = 0.008 if paragraph else 0.003
        height = line_height * max(1, len(lines)) + gap
        self.need(height, section)
        if deep_dive:
            self.ax.add_patch(plt.Rectangle((0.065, self.y - height + 0.003), 0.87, height + 0.008,
                                           color=PALE, transform=self.ax.transAxes, zorder=0))
            self.ax.add_patch(plt.Rectangle((0.065, self.y - height + 0.003), 0.006, height + 0.008,
                                           color=BLUE, transform=self.ax.transAxes, zorder=1))
        elif not paragraph and not numbered:
            self.ax.text(0.069, self.y, "•", fontsize=8.5, color=BLUE, va="top")
        for i, line in enumerate(lines):
            cursor = x
            for j, (word, bold) in enumerate(line):
                if j:
                    cursor += space
                prop = self.medium if bold else self.regular
                self.ax.text(cursor, self.y - i * line_height, word, fontsize=body_size, color=INK,
                             fontproperties=prop, va="top", zorder=2)
                cursor += self.text_width(word, prop, body_size)
        self.y -= height

    def equation(self, equation: str, note: str, section: str) -> None:
        self.need(0.105, section)
        self.ax.add_patch(plt.Rectangle((0.075, self.y - 0.076), 0.85, 0.086,
                                       color=PALE, transform=self.ax.transAxes))
        self.ax.text(0.095, self.y - 0.019, equation, fontsize=13.5, color=INK, va="top")
        self.ax.text(0.095, self.y - 0.057, note, fontsize=8.0, color=MUTED,
                     fontproperties=self.regular, va="top")
        self.y -= 0.105


def render(input_path: Path, output_path: Path) -> None:
    regular, medium = register_fonts()
    session_label = infer_session_label(input_path)
    source = input_path.read_text(encoding="utf-8")
    sections = clean_markdown(source) if input_path.suffix.lower() == ".md" else clean_export(source)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with PdfPages(output_path, metadata=pdf_metadata(session_label)) as pdf:
        writer = NotesWriter(pdf, regular, medium, session_label)
        suppress_before = False
        for index, (title, items) in enumerate(sections):
            next_is_subsection = (
                index + 1 < len(sections)
                and bool(re.match(r"^\d+\.\d+\s", sections[index + 1][0]))
            )
            attach_next = not items and bool(re.match(r"^\d+\.\s", title)) and next_is_subsection
            if attach_next:
                writer.need(0.245, title)
            writer.section_title(title, attach_next=attach_next,
                                 suppress_before=suppress_before)
            suppress_before = attach_next
            for item in items:
                writer.item(item, title)
            for equation, note in EQUATIONS.get(title, []):
                writer.equation(equation, note, title)
        if writer.fig is not None:
            writer.finish_page()


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path, help="NotebookLM plain-text export")
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    output = args.output or default_output_for(args.input)
    render(args.input, output)
    print(output.resolve())


if __name__ == "__main__":
    main()

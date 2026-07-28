#!/usr/bin/env python3
"""Create an A4, handwriting-friendly Session 1 NLP lecture handout."""

from pathlib import Path
from textwrap import wrap

from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = (
    ROOT
    / "llm-wiki/02-subjects/36118-applied-natural-language-processing"
    / "lectures/handouts/session-01-note-taking-handout.pdf"
)

W, H = 1240, 1754
INK = "#17243a"
MUTED = "#546176"
BLUE = "#3066be"
PALE = "#eaf1fb"
LINE = "#cbd5e1"
WHITE = "#ffffff"

GOOGLE_FONT_DIR = Path("/Applications/Google Drive.app/Contents/Resources")
FONT = GOOGLE_FONT_DIR / "GoogleSans-Regular.ttf"
FONT_BOLD = GOOGLE_FONT_DIR / "GoogleSans-Medium.ttf"


def font(size: int, bold: bool = False) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(FONT_BOLD if bold else FONT), size=size)


F_TITLE = font(54, bold=True)
F_H1 = font(34, bold=True)
F_H2 = font(25, bold=True)
F_BODY = font(21)
F_SMALL = font(17)
F_LABEL = font(18, bold=True)


def page(title: str, subtitle: str, number: int) -> tuple[Image.Image, ImageDraw.ImageDraw]:
    image = Image.new("RGB", (W, H), WHITE)
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, 24, H), fill=BLUE)
    draw.text((76, 64), "36118  |  APPLIED NATURAL LANGUAGE PROCESSING", font=F_LABEL, fill=BLUE)
    draw.text((76, 112), title, font=F_H1, fill=INK)
    draw.text((76, 164), subtitle, font=F_BODY, fill=MUTED)
    draw.line((76, 215, W - 76, 215), fill=LINE, width=2)
    draw.text((76, H - 62), "Session 01  •  27 July 2026", font=F_SMALL, fill=MUTED)
    draw.text((W - 112, H - 62), f"{number:02d}", font=F_SMALL, fill=MUTED)
    return image, draw


def wrapped(draw: ImageDraw.ImageDraw, text: str, xy: tuple[int, int], width: int = 82,
            fill: str = INK, spacing: int = 9, bullet: bool = False) -> int:
    x, y = xy
    prefix = "• " if bullet else ""
    subsequent = "  " if bullet else ""
    lines = wrap(prefix + text, width=width, subsequent_indent=subsequent)
    for line in lines:
        draw.text((x, y), line, font=F_BODY, fill=fill)
        y += 34
    return y + spacing


def heading(draw: ImageDraw.ImageDraw, text: str, y: int) -> int:
    draw.text((76, y), text, font=F_H2, fill=BLUE)
    return y + 46


def ruled(draw: ImageDraw.ImageDraw, y: int, lines: int, label: str = "MY NOTES") -> int:
    draw.text((76, y), label, font=F_LABEL, fill=BLUE)
    y += 37
    for _ in range(lines):
        draw.line((76, y, W - 76, y), fill=LINE, width=2)
        y += 48
    return y


def checkbox(draw: ImageDraw.ImageDraw, text: str, y: int) -> int:
    draw.rounded_rectangle((78, y + 2, 102, y + 26), radius=3, outline=BLUE, width=2)
    return wrapped(draw, text, (120, y), width=76)


pages: list[Image.Image] = []

# Cover
im = Image.new("RGB", (W, H), WHITE)
d = ImageDraw.Draw(im)
d.rectangle((0, 0, 34, H), fill=BLUE)
d.rounded_rectangle((76, 105, W - 76, 510), radius=30, fill=PALE)
d.text((112, 150), "36118", font=F_H2, fill=BLUE)
d.text((112, 210), "Applied Natural", font=F_TITLE, fill=INK)
d.text((112, 282), "Language Processing", font=F_TITLE, fill=INK)
d.text((112, 385), "SESSION 01  •  NOTE-TAKING HANDOUT", font=F_LABEL, fill=BLUE)
d.text((112, 435), "NLP foundations, linguistics & basic text analysis", font=F_BODY, fill=MUTED)
d.text((76, 610), "Student", font=F_LABEL, fill=MUTED)
d.line((178, 635, 720, 635), fill=LINE, width=2)
d.text((760, 610), "Date", font=F_LABEL, fill=MUTED)
d.line((822, 635, W - 76, 635), fill=LINE, width=2)
y = 740
y = heading(d, "How to use this handout", y)
for item in (
    "Before class: skim the key ideas and write one prediction or question.",
    "During class: capture examples, lecturer emphasis, and changes from the archived material.",
    "After class: complete the retrieval questions without looking at the notes.",
):
    y = wrapped(d, item, (76, y), bullet=True)
ruled(d, 1050, 10, "FIRST THOUGHTS / QUESTIONS")
# Cover intentionally omitted so the handout starts with substantive content.

# Learning map
im, d = page("Learning map", "See the whole workflow before studying the pieces.", 1)
y = 265
steps = ["Why NLP?", "Language levels", "Tokenise", "Syntax & POS", "NER", "Meaning", "Regex", "Text analysis"]
box_w, gap = 245, 26
for i, step in enumerate(steps):
    row, col = divmod(i, 4)
    x = 76 + col * (box_w + gap)
    yy = y + row * 126
    d.rounded_rectangle((x, yy, x + box_w, yy + 74), radius=14, fill=PALE, outline=BLUE, width=2)
    d.text((x + 16, yy + 22), f"{i + 1}. {step}", font=F_LABEL, fill=INK)
    if col < 3:
        d.line((x + box_w + 4, yy + 37, x + box_w + gap - 4, yy + 37), fill=BLUE, width=3)
y = 550
y = heading(d, "The key principle", y)
y = wrapped(d, "Computers receive strings and symbols, but useful NLP depends on linguistic structure and context. Session 1 moves from raw text to tokens, grammatical labels, entities, patterns, counts, and interpretable observations.", (76, y), width=88)
y = heading(d, "Listen for these distinctions", y + 18)
for item in (
    "human meaning vs machine representation",
    "word, character, subword, and sentence tokens",
    "syntax, semantics, discourse, and pragmatics",
    "POS tags, named entities, and co-reference",
    "raw frequencies vs cleaned frequencies",
):
    y = checkbox(d, item, y)
ruled(d, 1060, 10, "LECTURER EXAMPLES")
pages.append(im)

# Concepts
im, d = page("Core vocabulary", "Write the lecturer’s example beside each definition.", 2)
y = 260
concepts = [
    ("Corpus", "The collection of documents selected for analysis."),
    ("Token", "A unit processed by a system; it is not always a whole word."),
    ("Syntax & POS", "Syntax describes grammatical structure; POS tagging labels each token’s word class."),
    ("Named entity", "A person, organisation, location, time, quantity, or other categorised mention."),
    ("Semantics", "The meaning of words or texts; context helps distinguish senses such as two meanings of “bark”."),
    ("Discourse", "Meaning created across connected sentences rather than within one sentence alone."),
]
for term, definition in concepts:
    d.rounded_rectangle((76, y, W - 76, y + 150), radius=14, outline=LINE, width=2)
    d.text((98, y + 18), term, font=F_H2, fill=BLUE)
    wrapped(d, definition, (98, y + 58), width=82, fill=INK)
    d.line((98, y + 125, W - 98, y + 125), fill=LINE, width=2)
    y += 174
pages.append(im)

# Worked example
im, d = page("Tokenisation is a design decision", "The correct token boundaries depend on the task.", 3)
y = 270
d.rounded_rectangle((76, y, W - 76, y + 130), radius=18, fill=PALE)
d.text((104, y + 22), "RAW TEXT", font=F_LABEL, fill=BLUE)
wrapped(d, "I can't believe it's not butter. Visit https://example.com!", (104, y + 62), width=78)
y += 180
for prompt in (
    "Should “can't” become one token, “can” + “not”, or “ca” + “n't”?",
    "Should punctuation be kept as separate tokens for this task?",
    "How should a tokenizer preserve the URL as one meaningful unit?",
    "Compare a custom regular-expression tokenizer with NLTK word_tokenize.",
):
    y = heading(d, prompt, y)
    for _ in range(3):
        d.line((76, y, W - 76, y), fill=LINE, width=2)
        y += 46
    y += 20
pages.append(im)

# Code
im, d = page("Code reading", "Explain each transformation before running it.", 4)
y = 265
d.rounded_rectangle((76, y, W - 76, y + 260), radius=16, fill="#152033")
code = [
    'from nltk.tokenize import sent_tokenize, word_tokenize',
    'sentences = sent_tokenize(mytext)',
    'tokens = word_tokenize(mytext)',
    'tags = nltk.pos_tag(tokens)',
]
for i, line in enumerate(code):
    d.text((106, y + 34 + i * 50), line, font=F_BODY, fill="#e7edf7")
y += 315
for prompt in (
    "How are sentence tokens different from word tokens?",
    "Why does NLTK return punctuation as tokens?",
    "How can POS tags support NER, lemmatisation, parsing, or word-sense disambiguation?",
):
    y = heading(d, prompt, y)
    for _ in range(3):
        d.line((76, y, W - 76, y), fill=LINE, width=2)
        y += 46
    y += 16
pages.append(im)

# Comparison page
im, d = page("Session 1 notebook workflow", "Follow the actual order used in the practical notebooks.", 5)
y = 270
items = [
    ("1. Collect text", "Python variable, web page, or CSV", "Inspect source structure and access assumptions"),
    ("2. Analyse language", "Sentence/word tokens, POS, NER, dependency tree, regex", "Outputs depend on tokenisation and pretrained rules"),
    ("3. Explore a corpus", "Word counts, frequencies, plots, and word clouds", "Frequent terms may be stopwords or punctuation"),
]
for name, strength, caution in items:
    d.rounded_rectangle((76, y, W - 76, y + 210), radius=16, outline=LINE, width=2)
    d.text((100, y + 22), name, font=F_H2, fill=BLUE)
    d.text((100, y + 72), "CAPTURES", font=F_SMALL, fill=MUTED)
    d.text((260, y + 68), strength, font=F_BODY, fill=INK)
    d.text((100, y + 116), "LIMITATION", font=F_SMALL, fill=MUTED)
    wrapped(d, caution, (260, y + 112), width=63)
    d.line((100, y + 184, W - 100, y + 184), fill=LINE, width=2)
    y += 238
ruled(d, 1040, 10, "EXAMPLES / DIAGRAMS FROM CLASS")
pages.append(im)

# Current-semester verification
im, d = page("Cleaning and interpretation", "Compare results before and after each preprocessing decision.", 6)
y = 270
for item in (
    "Inspect the dataset with info(), describe(), head(), and sample()",
    "Measure text length and ask a question that makes the count meaningful",
    "Tokenise the corpus and inspect the raw frequency distribution",
    "Lowercase and remove task-irrelevant stopwords and punctuation",
    "Recalculate frequencies and explain what changed—and what may have been lost",
):
    y = checkbox(d, item, y)
    d.line((120, y + 10, W - 76, y + 10), fill=LINE, width=2)
    d.line((120, y + 58, W - 76, y + 58), fill=LINE, width=2)
    y += 88
y = heading(d, "Evidence and interpretation from the notebook", y + 10)
for _ in range(8):
    d.line((76, y, W - 76, y), fill=LINE, width=2)
    y += 48
pages.append(im)

# Retrieval
im, d = page("After-class retrieval", "Answer from memory, then check and correct in another colour.", 7)
y = 260
questions = [
    "Why is machine understanding of language difficult? Give two slide examples.",
    "Compare word, character, subword, and sentence tokenisation.",
    "Explain the difference between syntax, semantics, discourse, and pragmatics.",
    "How do POS tagging, NER, and co-reference add structure to raw text?",
    "Why should word frequencies be compared before and after cleaning?",
]
for i, question in enumerate(questions, 1):
    d.text((76, y), f"{i}.", font=F_H2, fill=BLUE)
    y = wrapped(d, question, (118, y), width=76)
    for _ in range(3):
        d.line((118, y, W - 76, y), fill=LINE, width=2)
        y += 43
    y += 18
d.rounded_rectangle((76, 1470, W - 76, 1625), radius=16, fill=PALE)
d.text((102, 1492), "ONE-SENTENCE SUMMARY", font=F_LABEL, fill=BLUE)
d.line((102, 1564, W - 102, 1564), fill=LINE, width=2)
d.line((102, 1604, W - 102, 1604), fill=LINE, width=2)
pages.append(im)

OUTPUT.parent.mkdir(parents=True, exist_ok=True)
pages[0].save(OUTPUT, "PDF", resolution=150.0, save_all=True, append_images=pages[1:])
print(OUTPUT)

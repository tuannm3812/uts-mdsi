# 36118 NLP Lecture Notes Supplement

Universal standard:
[Universal Lecture Notes Specification](../../../../07-templates/lecture-note-style-guide.md)

Apply the universal specification first. This file retains NLP-specific source
and regeneration details for 36118.

## 1. Source Requirements

Use the materials for the target session as the primary sources:

1. Lecture slide deck
2. In-class practical notebooks
3. Homework or exercise notebooks
4. Current Canvas instructions, when available

Keep content in the same conceptual sequence as the lecture and notebooks.
Do not introduce topics from later sessions merely because they are generally
related to NLP. Mark dates, assessment details, and policies from older
semesters as archival until checked against current Canvas material.

## 2. Writing Prompt

> You are an expert academic assistant and technical writer. Convert the
> supplied lecture slides and notebooks into connected, comprehensive,
> study-ready notes. Preserve technical details, examples, code workflows, and
> important cautions. Follow the teaching sequence in the source material.
> Turn slide fragments into coherent explanations without changing their
> meaning. Add brief Deep Dives only when they clarify a concept introduced in
> the session. Do not import material from later sessions. End with specific,
> source-grounded learning objectives.

## 3. Content Structure

- Begin directly with content; do not create a cover page.
- Use numbered Level 1 headings: `1.`, `2.`, `3.`, and so on.
- Use numbered Level 2 headings: `1.1`, `1.2`, `2.1`, and so on.
- Do not number Deep Dive headings.
- Use true numbered lists without an additional bullet.
- Use bullets only for genuinely parallel items.
- Keep paragraphs connected; do not turn every sentence into a bullet.
- Prevent headings from appearing alone at the bottom of a page.
- Keep a parent heading visually connected to its first subsection.

## 4. Technical Emphasis

Bold important terms directly in the passage rather than placing them in a
separate key-terms table.

Bold selectively:

- the first meaningful use of a technical term;
- important contrasts, such as **syntax** versus **semantics**;
- named methods, libraries, models, metrics, and data structures;
- terms the lecturer explicitly defines or emphasises;
- important warnings such as **task-dependent** or **information loss**.

Avoid bolding entire sentences or repeatedly bolding the same term in every
paragraph.

## 5. Deep Dives

- Use the heading `Deep Dive — Descriptive Title`.
- Do not number Deep Dives.
- Render them as compact block quotes with a pale background and coloured
  left border.
- Keep each Deep Dive brief and directly relevant to the session.
- Clearly distinguish supplementary context from source claims.

## 6. Formulas

- Include formulas only when they clarify concepts taught or used in the
  session.
- Typeset mathematics with STIX Two Math.
- Define every symbol and explain how to interpret the result.
- Do not add advanced equations from later sessions merely to make the notes
  appear more technical.

## 7. Code Blocks

- Render fenced Python or text snippets as real code blocks.
- Preserve indentation and line breaks.
- Use a monospaced font and a light neutral background.
- Do not add bullets or `Code:` prefixes.
- Use conventional light-theme syntax colours:

| Element | Colour |
|---|---|
| Python keywords | Blue |
| Strings | Red |
| Comments | Green |
| Numbers | Dark green |
| Imported modules | Teal |
| Functions and NLP utilities | Brown |
| Variables and operators | Dark navy |

## 8. PDF Typography and Spacing

- Body font: **Google Sans, 11 pt**
- Body line spacing: **single**
- Paragraph spacing: small, consistent space after each paragraph
- Level 1 headings: larger, dark navy
- Level 2 headings: medium-sized, blue
- Deep Dive headings: smaller blue headings
- Code: monospaced, approximately 9.5 pt
- No decorative rule beneath each content heading
- Retain only minimal page-header and footer furniture

## 9. Quality Checklist

- [ ] Every section is traceable to the target session’s sources.
- [ ] Slide fragments have been rewritten as connected prose.
- [ ] No unrelated later-session material has been introduced.
- [ ] Main sections and subsections are correctly numbered.
- [ ] Deep Dives are unnumbered and rendered as block quotes.
- [ ] Important technical terms are bolded in context.
- [ ] Numbered lists do not also have bullets.
- [ ] Code appears in syntax-highlighted code blocks.
- [ ] Formulas are relevant, correct, and explained.
- [ ] Body text is Google Sans 11 pt with single spacing.
- [ ] Headings are not orphaned or stuck to preceding paragraphs.
- [ ] The final PDF has been visually inspected.

## 10. Regeneration

From the repository root:

```bash
python3 scripts/create_nlp_comprehensive_notes.py \
  llm-wiki/02-subjects/36118-applied-natural-language-processing/lectures/session-01.md
```

For a future session, create a source-grounded Markdown note with the same
structure, then pass that file to the generator. Use a session-specific output
path until the generator supports automatic session naming.

# Universal Lecture Notes Specification

Apply this standard whenever the user requests comprehensive lecture notes,
study notes, or a lecture-note PDF for any subject, unless the user gives
different formatting instructions.

## Purpose

Convert the target session’s slides, notebooks, readings, exercises, and
current teaching instructions into connected, detailed, source-grounded notes.
The result should support study and annotation rather than merely reproduce
slide fragments.

## Source Priority

Use sources in this order:

1. Current-semester lecture slides and instructor instructions
2. Current practical, tutorial, or laboratory notebooks
3. Current exercises, readings, and assessment guidance
4. Previous-semester material, clearly labelled as archival
5. General knowledge, only for concise and relevant Deep Dives

Follow the conceptual sequence of the target lecture. Do not introduce topics
from later sessions merely because they are related. Distinguish supplementary
explanation from claims made by the source material.

## Reusable Writing Prompt

> You are an expert academic assistant and technical writer. Convert the
> supplied lecture slides, notebooks, readings, and exercises into connected,
> comprehensive, study-ready notes. Preserve technical details, examples,
> formulas, code workflows, qualifications, and important warnings. Follow the
> teaching sequence in the source material. Turn slide fragments into coherent
> explanations without changing their meaning. Add brief Deep Dives only when
> they clarify a concept introduced in the session. Do not import unrelated
> material from later sessions. End with specific, source-grounded learning
> objectives.

## Document Structure

- Begin directly with substantive content; do not add a cover page.
- Number Level 1 sections: `1.`, `2.`, `3.`, and so on.
- Number Level 2 subsections: `1.1`, `1.2`, `2.1`, and so on.
- Do not number Deep Dive headings.
- Use true numbered lists without an additional bullet.
- Use bullets only for genuinely parallel items.
- Keep explanations as connected paragraphs.
- Prevent headings from appearing alone at the bottom of a page.
- Keep a parent heading visually connected to its first subsection.

## Technical Emphasis

Bold important terms directly in the passage. Do not add a separate key-terms
table beneath every heading.

Bold selectively:

- the first meaningful occurrence of a technical term;
- important conceptual contrasts;
- named methods, theories, models, algorithms, libraries, metrics, and data
  structures;
- formulas or notation being introduced;
- warnings, assumptions, limitations, and task-dependent decisions;
- concepts explicitly defined or emphasised by the lecturer.

Avoid bolding entire sentences or repeatedly bolding the same term.

## Deep Dives

- Use `Deep Dive — Descriptive Title`.
- Do not number Deep Dives.
- Render each as a compact block quote with a pale background and coloured
  left border.
- Keep it brief and directly relevant to the session.
- Use it to clarify intuition, assumptions, limitations, practical
  implications, or necessary background.

## Formulas

- Include formulas when they occur in the source or materially clarify a
  concept taught in the session.
- Use a suitable mathematical font such as STIX Two Math.
- Define every variable and symbol.
- Explain the intuition and interpretation.
- Include units, assumptions, and boundary cases where relevant.
- Keep equations with their explanations.

## Code Blocks

- Render fenced code or commands as real code blocks.
- Preserve indentation and line breaks.
- Use a monospaced font on a light neutral background.
- Do not add bullets or `Code:` prefixes.
- Apply language-appropriate syntax highlighting.

For Python:

| Element | Colour |
|---|---|
| Keywords | Blue |
| Strings | Red |
| Comments | Green |
| Numbers | Dark green |
| Imported modules | Teal |
| Functions and utilities | Brown |
| Variables and operators | Dark navy |

For R, SQL, Java, shell, or other languages, use their conventional syntax
categories rather than forcing Python-specific colouring.

## Typography and Spacing

- Body font: **Google Sans, 11 pt**
- Body line spacing: **single**
- Paragraph spacing: small, consistent space after each paragraph
- Level 1 headings: larger and dark navy
- Level 2 headings: medium-sized and blue
- Deep Dive headings: smaller and blue
- Code: monospaced, approximately 9.5 pt
- No decorative rule beneath content headings
- Minimal page header and footer furniture
- Maintain space before headings while keeping parent headings compactly
  connected to their first subsections

## Subject-Specific Adaptation

- Mathematics and statistics: preserve derivations, notation, assumptions, and
  worked examples.
- Programming and data engineering: preserve executable code, commands,
  schemas, architecture, and failure modes.
- Machine learning and AI: explain the pipeline, objective, representation,
  model, evaluation, assumptions, and responsible-use implications.
- Visualisation: preserve design principles, encodings, chart interpretation,
  and narrative purpose.
- Research and innovation: emphasise argument structure, methodology,
  evidence, decisions, and reflective prompts.

Do not force formulas, code, or Deep Dives into a lecture that does not benefit
from them.

## Quality Checklist

- [ ] Content is traceable to the target session’s sources.
- [ ] Current material takes priority over archival material.
- [ ] Slide fragments have been converted into connected prose.
- [ ] No unrelated later-session content has been introduced.
- [ ] Sections and subsections are correctly numbered.
- [ ] Deep Dives are relevant, unnumbered, and formatted as block quotes.
- [ ] Technical terms are selectively bolded in context.
- [ ] Numbered lists do not also have bullets.
- [ ] Code uses proper blocks and suitable syntax colours.
- [ ] Formulas are relevant, correct, defined, and interpreted.
- [ ] Body text is Google Sans 11 pt with single spacing.
- [ ] Paragraph-after spacing is consistent.
- [ ] Parent and subsection headings are visually connected.
- [ ] Headings are not orphaned or attached to preceding paragraphs.
- [ ] The PDF has been validated and visually inspected.

## Workflow

1. Inventory the target lecture’s files.
2. Identify the authoritative current sources.
3. Extract slide text and notebook structure.
4. Build source-grounded Markdown notes.
5. Add only relevant Deep Dives, formulas, or code explanations.
6. Render the PDF using this standard.
7. Inspect page breaks, headings, bold terms, formulas, and code colours.
8. Save the Markdown, PDF, and regeneration instructions in the subject folder.

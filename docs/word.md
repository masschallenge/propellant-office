# Word

This guide covers memos, reports, proposals, letters and one pagers in Microsoft Word. Read the
[foundations](foundations.md) first: they set the colors, fonts and voice this guide applies.

## Start from the template

1. Install [`propellant-document.dotx`](../templates/word/propellant-document.dotx) as described in
   [installing the templates](templates.md).
2. In Word, choose **File**, then **New**, then **Personal** (or **Shared** if your organization
   publishes it), and pick **Propellant document**.
3. Replace the sample text. Keep the styles.

The template sets a US Letter page with one inch margins, the logo in the header, page numbers in
the footer, and every style below. It also opens with the same skeleton our documents use: a
title, an italic status line, the author, and an Overview section.

Already have a document? Open it and choose **Design**, then **Themes**, then **Browse for
Themes**, and pick [`Propellant.thmx`](../templates/powerpoint/Propellant.thmx). That switches
the colors and theme fonts. You still need to apply the Propellant styles below.

## Structure

Every document follows the same order so readers always know where to look:

1. **Title** in the Title style, in capitals. Keep it short: what the document is.
2. **Subtitle**, optional: the program, period or audience.
3. **Status line** in italics, such as Status: Draft, and **Author** on the line below.
4. **Overview** as Heading 1: one or two paragraphs with the point, the ask or the decision.
5. **Sections** as Heading 1, with Heading 2 for the parts inside them.

Keep documents short. Most should fit on four pages. If it runs longer, move detail to an
appendix at the end.

## Styles

Use the Styles gallery on the **Home** tab. Never make text look like a heading by making it bold
and big: it will not show in the navigation pane, the table of contents or a screen reader.

| Style | What it looks like | Use it for |
| --- | --- | --- |
| Title | Oswald, 32 pt, Deep teal, capitals | The document title, once |
| Subtitle | Lato, 14 pt, Slate | A short line under the title |
| Heading 1 | Lato Bold, 20 pt, Ink | Sections, including Overview |
| Heading 2 | Lato Bold, 15 pt, Ink | Parts of a section |
| Heading 3 | Lato Bold, 12.5 pt, Ink | Use sparingly |
| Normal | Lato, 11 pt, Ink, line spacing 1.4 | All body text |
| List Bullet, List Number | Lato, 11 pt | Lists |

Headings are in sentence case. Only the Title is in capitals, and the style does that for you, so
type the title normally.

## Lists

- Use the **Bullets** or **Numbering** buttons, never typed dashes.
- Use numbers only when the order matters, such as steps.
- Keep each item to one idea and start it with a capital letter.

## Tables

The sample table in the template shows the style: a Deep teal header row with White bold text,
thin Line `#DBE1E3` rules between rows and Mist on every other row.

- Put the header in the first row and set it to repeat: select the row, choose **Table Layout**,
  then **Repeat Header Rows**.
- Left align text and right align numbers. Give every column the same number of decimals.
- Do not merge cells or leave empty rows for spacing. Screen readers read tables cell by cell.
- If a table runs past half a page, consider putting it in an appendix or an Excel file.

## Callouts

For the one thing a reader must not miss, use a callout: a paragraph with a Pale teal `#D9F6FA`
fill and a Teal left border, as in the template. Copy it from the sample. Use one per page at most.

## Photos and images

- Insert photos with **Insert**, then **Pictures**. Choose **In Line with Text** from **Layout
  Options** so they move with the text.
- Size photos to the full text width or half of it. Do not let text wrap around small photos.
- Add alt text: right click the photo and choose **View Alt Text**.
- Add a caption below with **References**, then **Insert Caption** when the photo needs context.
- Follow the [photography guide](photography.md) for choosing photos.

## Headers and footers

The template puts the full color logo at the top left of every page and "MassChallenge | Page"
with the page number at the bottom right. Do not add more to the header. For a confidential
document, add the word Confidential to the footer, never a watermark across the page.

## Before you share

1. Run **Review**, then **Check Accessibility**, and fix every error.
2. Check that the headings show in **View**, then **Navigation Pane**.
3. Fill in **File**, then **Info**, then **Properties**: a title, so screen readers announce it.
4. Send a PDF (**File**, **Save As**, **PDF**) to people who only need to read it. If someone
   outside MassChallenge needs to edit it, [embed the fonts](foundations.md#sending-files-outside-masschallenge).

## Things to avoid

- Text in Teal, except links.
- Oswald in body text, lists or tables.
- More than one font size per style, or text formatted by hand instead of with styles.
- Word art, shadows, outlines, gradients and 3D effects.
- Clip art and low resolution logos copied from the web.

# Google Docs

This guide covers memos, reports and proposals in Google Docs. Read the
[foundations](foundations.md) first, and the [Word guide](word.md) for structure, lists and tables:
the same rules apply, and this page covers what is different in Google Docs.

## Start from the template

Google Docs has no template file of its own to download, so the Propellant template comes as a
Word file that Docs converts.

1. Download [`propellant-document.docx`](../templates/word/propellant-document.docx).
2. In Google Drive, choose **New**, then **File upload**, and pick it.
3. Open it, choose **File**, then **Save as Google Docs**. Work in the Google Docs copy.

If your organization has added Propellant to the Docs template gallery, choose **File**, then
**New**, then **From template gallery** instead. [Installing the templates](templates.md) explains
how an administrator sets that up, and how to share a "make a copy" link.

Google does not publish a list of what changes when a Word file is converted, so check the result.
The styles, colors, logo and table come across; review the header, footer and page numbers once.
The footer should read "© MassChallenge 2026 | contact@masschallenge.org | Page" and the page
number.

Documents that go outside MassChallenge end with an About MassChallenge section, as the
[Word guide](word.md#structure) explains, quoting the
[boilerplate](foundations.md#about-masschallenge) exactly.

## Fonts

Lato and Oswald are both available in Google Docs. If they are not in your font menu yet, open the
font menu, choose **More fonts**, search for each one and select it. They then stay in your menu.

## Styles

Google Docs calls styles "paragraph styles". The converted template already has them set. Pick
them from the style menu on the toolbar, which shows **Normal text** by default.

| Google Docs style | Propellant style |
| --- | --- |
| Title | Oswald SemiBold, 32 pt, Black, capitals, line spacing 1.0 |
| Subtitle | Lato, 14 pt, Slate |
| Heading 1 | Oswald SemiBold, 18 pt, Teal, capitals, line spacing 1.0 |
| Heading 2 | Oswald SemiBold, 14 pt, Black, capitals, line spacing 1.0 |
| Heading 3 | Lato Bold, 12 pt, Black |
| Normal text | Lato, 11 pt, Black, line spacing 1.5 |

If a style looks wrong in a document that did not start from the template, fix one example by
hand, select it, and choose **Update "Heading 1" to match** from the style menu. To make the
Propellant styles your default for every new document, open the style menu, choose **Options**,
then **Save as my default styles**.

Google Docs cannot make text capitals with a style setting, so type the Title, Heading 1 and
Heading 2 in capitals.

After converting, check that the Title and headings are in Oswald SemiBold. If they show another
font, select one, choose Oswald and its SemiBold weight from the font menu, and update the style
to match as above.

## Page setup

- Choose **File**, then **Page setup**: Letter, one inch margins, and **Pages** rather than
  **Pageless** for anything that will be printed or shared as a PDF.
- Use **Pageless** for working documents that stay in Docs, such as meeting notes.

## Tables and callouts

- Insert tables with **Insert**, then **Table**. Set the header row background to Navy
  `#10263F` with White bold text, add Warm White `#F8F8F5` to alternate rows if the table is long,
  and use Gray 100 `#DBE1E3` for the lines between rows.
- To pin the header row when a table crosses pages, right click it, choose **Table properties**,
  then **Pin header rows**.
- For a callout, insert a one cell table with a Warm White `#F8F8F5` background and a Teal
  `#00708E` left border, or copy the callout from the template.

Add custom colors once with **Custom** in any color menu; Docs remembers them under **Custom**.

## Photos

- Insert photos with **Insert**, then **Image**, and choose **In line** so they move with the
  text.
- Add alt text: right click the image and choose **Alt text**.
- Use Google's own image search only for ideas. Use photos from our libraries, as the
  [photography guide](photography.md) explains.

## Before you share

Google Docs has no built-in accessibility checker. Check by hand:

1. Open **View**, then **Show outline**. Every section should appear, in order.
2. Make sure every image has alt text and every link says where it goes.
3. Share with **Viewer** or **Commenter** access unless someone needs to edit.
4. For people outside MassChallenge, send a PDF with **File**, then **Download**, then **PDF
   document**.

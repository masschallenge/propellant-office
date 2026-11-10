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

## Fonts

Lato and Oswald are both available in Google Docs. If they are not in your font menu yet, open the
font menu, choose **More fonts**, search for each one and select it. They then stay in your menu.

## Styles

Google Docs calls styles "paragraph styles". The converted template already has them set. Pick
them from the style menu on the toolbar, which shows **Normal text** by default.

| Google Docs style | Propellant style |
| --- | --- |
| Title | Oswald, 32 pt, Deep teal, capitals |
| Subtitle | Lato, 14 pt, Slate |
| Heading 1 | Lato Bold, 20 pt, Ink |
| Heading 2 | Lato Bold, 15 pt, Ink |
| Heading 3 | Lato Bold, 12.5 pt, Ink |
| Normal text | Lato, 11 pt, Ink, line spacing 1.4 |

If a style looks wrong in a document that did not start from the template, fix one example by
hand, select it, and choose **Update "Heading 1" to match** from the style menu. To make the
Propellant styles your default for every new document, open the style menu, choose **Options**,
then **Save as my default styles**.

Google Docs cannot make text capitals with a style setting, so type the Title in capitals.

## Page setup

- Choose **File**, then **Page setup**: Letter, one inch margins, and **Pages** rather than
  **Pageless** for anything that will be printed or shared as a PDF.
- Use **Pageless** for working documents that stay in Docs, such as meeting notes.

## Tables and callouts

- Insert tables with **Insert**, then **Table**. Set the header row background to Deep teal
  `#044451` with White bold text, and add Mist `#F3F6F7` to alternate rows if the table is long.
- To pin the header row when a table crosses pages, right click it, choose **Table properties**,
  then **Pin header rows**.
- For a callout, insert a one cell table with a Pale teal `#D9F6FA` background and no border, or
  copy the callout from the template.

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

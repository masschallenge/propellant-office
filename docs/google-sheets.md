# Google Sheets

This guide covers trackers, budgets and shared data in Google Sheets. Read the
[foundations](foundations.md) first, and the [Excel guide](excel.md) for sheets, numbers and
charts: the same rules apply, and this page covers what is different in Google Sheets.

## Start from the template

1. Download [`propellant-workbook.xlsx`](../templates/excel/propellant-workbook.xlsx).
2. In Google Drive, choose **New**, then **File upload**, and pick it.
3. Open it and choose **File**, then **Save as Google Sheets**. Work in the Google Sheets copy.

The header row and Mist stripes are set as cell formatting, so they come across as they are. Check
the chart once after converting.

If your organization has added Propellant to the Sheets template gallery, choose it from
**Template gallery** on the Sheets home page instead. See [installing the templates](templates.md).

## Theme

Google Sheets has its own theme for fonts and chart colors.

1. Choose **Format**, then **Theme**.
2. Choose **Customize** and set the font to **Lato**, the text color to Ink `#1E282B`, and the
   accents in the Propellant order: Teal `#065E6F`, Yellow `#FFC801`, Slate `#4B575B`, Bright
   teal `#0FACBD`, Deep teal `#044451` and Gray `#848F92`. Set links to Teal `#065E6F`.

Charts and new tables then pick up the brand colors. If Lato is not in the font list, add it from
**More fonts** in the toolbar's font menu first.

## Titles and headers

| Element | Style |
| --- | --- |
| Sheet title | Oswald, 24 pt, Deep teal, typed in capitals |
| Header row | Lato Bold, 11 pt, White on Deep teal `#044451` |
| Cells | Lato, 11 pt, Ink |
| Alternate rows | Mist `#F3F6F7` |

To get banded rows on new data, select it and choose **Format**, then **Alternating colors**, then
set the header to Deep teal and the second color to Mist. You can also use **Format**, then
**Convert to table**, which adds filters and column types.

Freeze the header row with **View**, then **Freeze**, then **1 row**.

## Status

Use a dropdown for status (**Insert**, then **Dropdown**) with words such as On track, At risk and
Late. You can color the dropdown chips, but keep the word: never show status by color alone.

## Charts

- Insert charts with **Insert**, then **Chart**. With the theme set, they use the brand colors.
- In the chart editor's **Customize** tab, turn on data labels when there is more than one series,
  set the chart and axis titles, and remove the chart border.
- Follow the chart rules in the [foundations](foundations.md#charts).
- Add alt text: select the chart, open the three dot menu, and choose **Alt text**.

## Sharing

- Share with **Viewer** access by default. Protect ranges people should not edit with **Data**,
  then **Protect sheets and ranges**.
- Google Sheets has no built-in accessibility checker. Check that headers are in the first row,
  there are no merged cells in tables, and status is written as words.
- For people outside MassChallenge, download a PDF or an Excel file from **File**, then
  **Download**.

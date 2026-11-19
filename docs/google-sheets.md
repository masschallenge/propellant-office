# Google Sheets

This guide covers trackers, budgets and shared data in Google Sheets. Read the
[foundations](foundations.md) first, and the [Excel guide](excel.md) for sheets, numbers and
charts: the same rules apply, and this page covers what is different in Google Sheets.

## Start from the template

1. Download [`propellant-workbook.xlsx`](../templates/excel/propellant-workbook.xlsx).
2. In Google Drive, choose **New**, then **File upload**, and pick it.
3. Open it and choose **File**, then **Save as Google Sheets**. Work in the Google Sheets copy.

The header row and Warm White stripes are set as cell formatting, so they come across as they are. Check
the chart once after converting.

If your organization has added Propellant to the Sheets template gallery, choose it from
**Template gallery** on the Sheets home page instead. See [installing the templates](templates.md).

## Theme

Google Sheets has its own theme for fonts and chart colors.

1. Choose **Format**, then **Theme**.
2. Choose **Customize** and set the font to **Lato**, the text color to Black `#222222`, and the
   accents in the Propellant order: Teal `#00708E`, Yellow `#FFC801`, Navy `#10263F`, MC Blue
   `#0EABBC`, Deep Teal `#004F73` and Gray 300 `#848F92`. Set links to Teal `#00708E`.

Charts and new tables then pick up the brand colors. If Lato is not in the font list, add it from
**More fonts** in the toolbar's font menu first.

## Titles and headers

| Element | Style |
| --- | --- |
| Sheet title | Oswald SemiBold, 24 pt, Black, typed in capitals |
| Header row | Lato Bold, 11 pt, White on Navy `#10263F` |
| Cells | Lato, 11 pt, Black |
| Alternate rows | Warm White `#F8F8F5` |

To get banded rows on new data, select it and choose **Format**, then **Alternating colors**, then
set the header to Navy and the second color to Warm White. You can also use **Format**, then
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

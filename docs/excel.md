# Excel

This guide covers budgets, trackers, program data and reports in Microsoft Excel. Read the
[foundations](foundations.md) first: they set the colors, fonts and voice this guide applies.

## Start from the template

1. Install [`propellant-workbook.xltx`](../templates/excel/propellant-workbook.xltx) as described
   in [installing the templates](templates.md).
2. In Excel, choose **File**, then **New**, then **Personal** (or **Shared**), and pick
   **Propellant workbook**.
3. The template has two sheets: **Start here**, with the logo, a title and how to use the
   template, and **Example data**, with a styled table and a chart. Replace the example rows with
   your own data.

To bring an existing workbook onto the brand, choose **Page Layout**, then **Themes**, then
**Browse for Themes**, and pick [`Propellant.thmx`](../templates/powerpoint/Propellant.thmx).
Charts and cell colors chosen from the theme switch over at once.

## Sheets

- Start every workbook with a **Start here** sheet: what the workbook answers, who it is for,
  where the data comes from, and when it was last updated.
- Name every sheet for what it holds, such as Budget 2026 or Applications, never Sheet1.
- Keep one table per sheet, starting near the top left, with no blank rows or columns inside it.
- Turn off gridlines on summary and presentation sheets with **View**, then uncheck
  **Gridlines**. Keep them on sheets where people enter data.

## Titles and headers

| Element | Style |
| --- | --- |
| Sheet title | Oswald SemiBold, 24 pt, Black, typed in capitals, in the first rows |
| Description under the title | Lato, 11 or 12 pt, Slate |
| Table header row | Lato Bold, 11 pt, White on Navy `#10263F` |
| Cells | Lato, 11 pt, Black |
| Alternate rows | Warm White `#F8F8F5` fill, or none |

Header text is in sentence case and includes the unit, such as Budget (USD) or Duration (days).

Excel cannot make text capitals with a style, so type the sheet title in capitals. If Oswald or
Lato is missing, the brand guide's [fallback](foundations.md#when-oswald-or-lato-is-not-there) is
Aptos Narrow Bold in capitals for the title and Aptos for everything else. Never Arial.

## Numbers

- Right align numbers and left align text.
- Use the same number of decimals down a column. Use a thousands separator: 12,400, not 12400.
- Show negative numbers with a minus sign or in brackets, never in red alone.
- Use real dates, not text that looks like a date, so they sort and filter.
- Freeze the header row with **View**, then **Freeze Panes**, then **Freeze Top Row**.
- Write formulas so others can follow them: name important cells or ranges, and avoid typing a
  number into a formula when it belongs in its own labeled cell.

## Tables and filters

The header row and Warm White stripes in the template are applied directly, so they look the same in
Excel and in Google Sheets. To add filters and sorting, select the data and choose **Insert**,
then **Table**. When you do, pick a table style from the light row so it does not fight the
header colors, or keep the template formatting and turn off banded rows.

## Status and conditional formatting

- Show status with a word in its own column, such as On track, At risk or Late. Color can support
  the word, but never replace it.
- For conditional formatting, use the Light tint `#F3FAFC` fill for highlights. For things that
  are wrong, use Propellant's error color, magenta `#BF0261`, with the word beside it. Never use
  Raspberry, Orange or Lime to show status: they are decorative brand accents.
- Avoid data bars and icon sets in shared workbooks: they are hard to read and do not survive
  every export.

## Charts

- Insert charts with **Insert**, then **Recommended Charts**. They take their colors from the
  theme.
- Follow the chart rules in the [foundations](foundations.md#charts): one series in Teal, labels
  on the chart when there are more, four series at most, one axis.
- Give the chart a title that states the takeaway, and label the axes with units.
- Prefer bar and line charts. Avoid pie charts with more than three slices, 3D charts and
  secondary axes.
- Add alt text: right click the chart and choose **View Alt Text**.

## Printing and sharing

- Set printing up front with **Page Layout**: landscape for wide tables, **Fit All Columns on One
  Page**, and the header row repeated with **Print Titles**.
- Check accessibility with **Review**, then **Check Accessibility**.
- For a workbook that goes outside MassChallenge, add © MassChallenge 2026 and
  contact@masschallenge.org to the page footer with **Page Layout**, then **Print Titles**, then
  **Header/Footer**.
- Excel cannot embed fonts. People without Lato see a different font, so share a PDF when the
  look matters.

## Things to avoid

- Merged cells inside tables. They break sorting, filtering and screen readers.
- Colors picked from **More Colors** instead of the theme row.
- Hidden rows or sheets with data others depend on.
- Oswald anywhere but the sheet title.
- The full color logo on anything but White or Warm White.

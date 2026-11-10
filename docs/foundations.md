# Designing documents, decks and spreadsheets

Everything MassChallenge sends out, from a one page memo to a pitch deck to a budget, should look
like it came from the same team that built our website. This page sets the shared rules. The
guides for each app show you where to find the settings, and the templates have everything set up
already.

The rules come straight from Propellant, so a document and the website use the same colors, fonts
and voice.

## Start from a template

The fastest way to get every rule right is to start from a Propellant template. They have the
colors, fonts, styles, logo and page setup built in.

| App | Template | Guide |
| --- | --- | --- |
| Word | [`propellant-document.dotx`](../templates/word/propellant-document.dotx) | [Word](word.md) |
| PowerPoint | [`propellant-presentation.potx`](../templates/powerpoint/propellant-presentation.potx) | [PowerPoint](powerpoint.md) |
| Excel | [`propellant-workbook.xltx`](../templates/excel/propellant-workbook.xltx) | [Excel](excel.md) |
| Google Docs | [`propellant-document.docx`](../templates/word/propellant-document.docx) | [Google Docs](google-docs.md) |
| Google Slides | [`propellant-presentation.pptx`](../templates/powerpoint/propellant-presentation.pptx) | [Google Slides](google-slides.md) |
| Google Sheets | [`propellant-workbook.xlsx`](../templates/excel/propellant-workbook.xlsx) | [Google Sheets](google-sheets.md) |

[Installing the templates](templates.md) explains how to add them to each app, and how an
administrator can share them with everyone.

## Fonts

| Font | Use it for |
| --- | --- |
| Lato | Everything: body text, headings, tables, labels and captions. |
| Oswald | Only the big headline: a document title, a slide title or a sheet title. Always in capitals. |

Oswald is a narrow, condensed font. It is made for short, large headlines and is hard to read in
long text, so never use it for paragraphs, bullets or table text.

### Getting the fonts

Both fonts are free, open source fonts from [Google Fonts](https://fonts.google.com).

- **Google Docs, Sheets and Slides** can use both. Open the font menu, choose **More fonts** and
  search for Lato and Oswald.
- **Microsoft Word, PowerPoint and Excel** do not include them. Lato and Oswald are not among
  Microsoft 365's [cloud fonts](https://support.microsoft.com/en-us/office/cloud-fonts-in-office-f7b009fe-037f-45ed-a556-b5fe6ede6adb),
  so each computer needs them installed. Ask IT to install them for you, or download them from
  [Lato](https://fonts.google.com/specimen/Lato) and [Oswald](https://fonts.google.com/specimen/Oswald)
  and install them yourself. A Microsoft 365 administrator can also
  [publish them as organization fonts](https://learn.microsoft.com/en-us/sharepoint/support-for-organization-fonts-in-powerpoint-for-the-web)
  so they work in Office on the web.

If a computer does not have the fonts, Office swaps in another font and the layout can shift.

### Sending files outside MassChallenge

People outside MassChallenge may not have Lato and Oswald. Before you send a Word or PowerPoint
file that someone else will open:

- **Send a PDF** when they only need to read it. A PDF keeps the fonts exactly.
- **Embed the fonts** when they need to edit it. In Word or PowerPoint on Windows, choose
  **File**, **Options**, **Save**, then **Embed fonts in the file**, and leave "Embed only the
  characters used" off. Recent Word and PowerPoint for Mac support this too.
  [Microsoft explains embedding](https://support.microsoft.com/en-us/office/benefits-of-embedding-custom-fonts-cb3982aa-ea76-4323-b008-86670f222dbc).
  Embedded fonts do not show in Office on the web, and Excel cannot embed fonts.

## Color

Every template uses the Propellant theme. A theme is the set of twelve named colors and two fonts
that Office and Google offer at the top of every color and font menu. Pick colors from the theme
row, never from "More colors", and your file stays on brand even if the theme is updated later.

| Theme slot | Name | Hex | Use it for |
| --- | --- | --- | --- |
| Dark 1 (text) | Ink | `#1E282B` | Body text and headings |
| Light 1 (background) | White | `#FFFFFF` | Page and slide backgrounds |
| Dark 2 | Deep teal | `#044451` | Title slides, section slides, table headers, cover pages |
| Light 2 | Mist | `#F3F6F7` | Alternate rows and quiet panels |
| Accent 1 | Teal | `#065E6F` | Links and the first chart series |
| Accent 2 | Yellow | `#FFC801` | Highlights, always with Ink text, and the second chart series |
| Accent 3 | Slate | `#4B575B` | Secondary text and the third chart series |
| Accent 4 | Bright teal | `#0FACBD` | Accents on Deep teal and the fourth chart series |
| Accent 5 | Deep teal | `#044451` | The fifth chart series |
| Accent 6 | Gray | `#848F92` | Comparison data, such as last year |
| Hyperlink | Teal | `#065E6F` | Links |
| Followed hyperlink | Deep teal | `#044451` | Visited links |

Two more brand colors sit outside the theme on purpose:

- **Pale teal `#D9F6FA`** tints a callout box or a highlighted row.
- **Mid teal `#068DA4`** is a supporting accent for shapes and icons.
- **Magenta `#A30253`** means something is wrong or late. It is not in the theme so it never ends
  up in a chart or a decoration by accident.

### Using color

- Most of the page is White, with Ink text. Color is an accent, not a background for everything.
- Use Deep teal for big brand moments: a title slide, a section divider, a cover. On Deep teal use
  White text and Bright teal accents, never Teal text.
- Keep headings in Ink. Teal is for links and things people can click.
- Never show meaning with color alone. Pair every status color with a word, such as On track or
  Late.
- Keep text readable: a contrast ratio of at least 4.5:1 with its background, as the
  [WCAG guidelines](https://www.w3.org/TR/WCAG21/#contrast-minimum) require. These pairings pass:

  | Text | Background | Contrast |
  | --- | --- | --- |
  | Ink | White, Mist or Pale teal | 13.3:1 or more |
  | Ink | Yellow | 9.7:1 |
  | Slate | White or Mist | 6.9:1 or more |
  | Teal | White | 7.4:1 |
  | White | Deep teal | 10.8:1 |
  | White | Teal | 7.4:1 |
  | Bright teal | Deep teal | 3.9:1, so only for text 18 pt or larger |

  Bright teal, Mid teal, Yellow and Gray are too light for text on White.

### Charts

- A chart with one series uses Teal. Most charts need only one.
- Charts take their colors from the theme in the order above, so do not recolor series by hand.
- With two or more series, show the values or series names on the chart itself, not only in a
  legend. Yellow, Bright teal and Gray are light against White, so labels are what make them
  readable, and they help anyone who cannot tell the colors apart.
- Keep to four series or fewer. Fold the rest into Other, or split the chart.
- Use one value axis. Two measures on different scales belong in two charts.
- Never use Magenta for a series: it means something is wrong.

## Type styles

Use the built-in styles in the templates instead of formatting text by hand. Styles keep a long
document consistent, build the table of contents and tell screen readers how the document is
organized.

### Documents (Word and Google Docs)

| Style | Font | Size | Color | Notes |
| --- | --- | --- | --- | --- |
| Title | Oswald | 32 pt | Deep teal | Capitals, once per document |
| Subtitle | Lato | 14 pt | Slate | |
| Heading 1 | Lato Bold | 20 pt | Ink | Sections |
| Heading 2 | Lato Bold | 15 pt | Ink | Parts of a section |
| Heading 3 | Lato Bold | 12.5 pt | Ink | Rarely needed |
| Normal | Lato | 11 pt | Ink | Line spacing 1.4, 8 pt after each paragraph |

### Slides (PowerPoint and Google Slides)

| Style | Font | Size | Color |
| --- | --- | --- | --- |
| Title on a white slide | Oswald, capitals | 40 pt | Ink |
| Title on a Deep teal slide | Oswald, capitals | 54 pt | White |
| Body, first level | Lato | 24 pt | Ink |
| Body, second level | Lato | 20 pt | Slate |
| Smallest text, such as a source | Lato | 18 pt | Slate |

Microsoft [recommends 18 pt or larger](https://support.microsoft.com/en-us/accessibility/powerpoint/make-your-powerpoint-presentations-accessible-to-people-with-disabilities)
for slide text. Never go smaller.

### Spreadsheets (Excel and Google Sheets)

| Style | Font | Size | Color |
| --- | --- | --- | --- |
| Sheet title | Oswald, capitals | 24 pt | Deep teal |
| Header row | Lato Bold | 11 pt | White on Deep teal |
| Cells | Lato | 11 pt | Ink, with Mist stripes |

### Case

Only Oswald titles are in capitals. Everything else, headings and table headers included, is in
sentence case: a capital first letter and lower case after it, except for names.

## The logo

Use the logo files in [`assets/logos`](../assets/logos), never a copy from a website or an old
file.

| Background | Logo |
| --- | --- |
| White or a light color | Full color: `masschallenge-logo-horizontal-color.png` |
| Deep teal, a dark color or a dark photo | White: `masschallenge-logo-horizontal-white.png` |
| One color printing | Black: `masschallenge-logo-horizontal-black.png` |

- Put the logo once per page or slide, in a corner. The templates place it for you.
- Leave clear space around it equal to half its height.
- Never stretch, recolor, outline or redraw it, and never put the full color logo on Deep teal.
- In a document, keep the horizontal logo at least a third of an inch (8 mm) tall so the wordmark
  stays readable. Use the MC monogram alone only where MassChallenge is already named.

The [brand guidelines](https://github.com/masschallenge/propellant-web/blob/main/docs/brand.md)
have the full logo rules.

## Layout

- **Leave space.** White space makes a page easier to read. Do not fill every corner.
- **Align to the margins.** Line up text, images and charts on the same left edge.
- **One idea per slide, one table per sheet, one purpose per document.**
- **Round the corners of photos and panels** slightly, about 0.12 inch (3 mm), as the website does
  with 12 pixels. Logos and charts stay square.
- **Use real lists.** Use the bullet and numbering buttons, never typed dashes or asterisks.

## Writing

Documents sound like the rest of MassChallenge: bold and human, direct and plain spoken.

- Put the point first: the decision, the ask or the takeaway.
- Use short sentences and everyday words. Write "we" for MassChallenge and "you" for the reader.
- Make a slide title say the takeaway, not the topic: "Applications grew in every program", not
  "Applications".
- Skip buzzwords such as leverage, seamless and robust, and skip exclamation marks.
- Use commas, colons and periods. Do not use em dashes or en dashes.

## Accessibility

Everything we send should work for people who use screen readers, magnifiers or high contrast
settings.

- Use the built-in title, heading and list styles so the structure is real, not just visual.
- Give every photo, chart and diagram alt text that says what it shows. Mark purely decorative
  images as decorative.
- Give every slide a unique title, even if you hide it.
- Run the checker before you share: in Word, PowerPoint and Excel choose **Review**, then
  [**Check Accessibility**](https://support.microsoft.com/en-us/office/improve-accessibility-with-the-accessibility-checker-a16f6de0-2f39-4a2b-8bd8-5ad801426c7f).
  Google Docs, Sheets and Slides have no built-in checker, so check headings, alt text and slide
  titles by hand.
- Use link text that says where it goes, such as "the application guide", never "click here".

## Photography and video

People are at the heart of how MassChallenge looks. The
[photography and video guide](photography.md) covers choosing, treating and placing photos and
videos, from your own event photos to licensed stock.

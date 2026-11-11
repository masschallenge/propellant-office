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

| Font | Use it for | Where |
| --- | --- | --- |
| Lato | All text: body text, headings, tables, labels and captions. On the web and in our products it is called Propellant Sans. | Documents, slides, sheets, email and product screens |
| Oswald | Display headlines only: a document title, a slide title or a sheet title. Always in capitals. | Documents, slides, social graphics and public web pages. Never inside signed in product screens |

Oswald is a narrow, condensed font. It is made for short, large headlines and is hard to read in
long text, so never use it for paragraphs, bullets or table text.

In email, Lato falls back to Arial, Helvetica, sans-serif for anyone who does not have it.

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

The Propellant palette is the same everywhere: on the web, in Office and Google files, and in
print.

### The palette

| Name | Hex | RGB | Print CMYK | Use it for |
| --- | --- | --- | --- | --- |
| Deep teal | `#044451` | 4 68 81 | 100 64 53 50 | Title slides, section slides, table headers, cover pages |
| Teal | `#065E6F` | 6 94 111 | 100 55 45 24 | Links, actions and the first chart series |
| Mid teal | `#068DA4` | 6 141 164 | 87 31 31 2 | A supporting accent for shapes and icons |
| Bright teal | `#0FACBD` | 15 172 189 | 78 11 26 0 | Accents and large text on Deep teal |
| Pale teal | `#D9F6FA` | 217 246 250 | 13 0 2 0 | Callout boxes and highlighted rows |
| Mist | `#F3FBFC` | 243 251 252 | 3 0 1 0 | Alternate rows and quiet panels |
| Magenta | `#BF0261` | 191 2 97 | 21 100 42 5 | Things that are wrong or late, used sparingly |
| Yellow | `#FFC801` | 255 200 1 | 0 22 100 0 | Highlights, always with Ink text |
| Ink | `#1E282B` | 30 40 43 | 81 66 63 83 | Body text and headings |
| Slate | `#4B575B` | 75 87 91 | 73 57 55 35 | Secondary text |
| White | `#FFFFFF` | 255 255 255 | 0 0 0 0 | Page and slide backgrounds |

### Supporting neutrals

Two grays from Propellant support the palette in lines and charts.

| Name | Hex | RGB | Print CMYK | Use it for |
| --- | --- | --- | --- | --- |
| Gray 100 | `#DBE1E3` | 219 225 227 | 13 7 8 0 | Rules and table lines |
| Gray 300 | `#848F92` | 132 143 146 | 53 38 39 4 | The sixth chart color, such as comparison data |

The logo artwork has two colors of its own, Logo gray `#828486` (CMYK 53 44 43 7) and Logo teal
`#17ACBC` (CMYK 77 11 27 0). Use them only in the logo, never for text, shapes or charts.

### Printing

The CMYK values are calculated from the sRGB values with the Artifex CMYK SWOP profile (US web
coated), relative colorimetric intent, rounded to whole percent. Check a printed proof before a
large run.

### The theme

Every template uses the Propellant theme. A theme is the set of twelve named colors and two fonts
that Office and Google offer at the top of every color and font menu. Pick colors from the theme
row, never from "More colors", and your file stays on brand even if the theme is updated later.

| Theme slot | Name | Hex |
| --- | --- | --- |
| Dark 1 (text) | Ink | `#1E282B` |
| Light 1 (background) | White | `#FFFFFF` |
| Dark 2 | Deep teal | `#044451` |
| Light 2 | Mist | `#F3FBFC` |
| Accent 1 | Teal | `#065E6F` |
| Accent 2 | Yellow | `#FFC801` |
| Accent 3 | Slate | `#4B575B` |
| Accent 4 | Bright teal | `#0FACBD` |
| Accent 5 | Deep teal | `#044451` |
| Accent 6 | Gray 300 | `#848F92` |
| Hyperlink | Teal | `#065E6F` |
| Followed hyperlink | Deep teal | `#044451` |

Pale teal, Mid teal, Magenta and Gray 100 sit outside the theme on purpose. Magenta stays out so
it never ends up in a chart or a decoration by accident.

### Using color

- Most of the page is White and the neutrals, with Ink text. Teals are for brand surfaces and
  actions, and Magenta and Yellow are used only a little.
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
  | Slate | White or Mist | 7.1:1 or more |
  | Teal | White or Mist | 7.0:1 or more |
  | Magenta | White or Mist | 5.9:1 or more |
  | White | Deep teal | 10.8:1 |
  | White | Teal | 7.4:1 |
  | Bright teal | Deep teal | 3.9:1, so only for text 18 pt or larger |

  Bright teal, Mid teal, Yellow and Gray 300 are too light for text on White.

### Charts

- A chart with one series uses Teal. Most charts need only one.
- Charts take their colors from the theme in this order: Teal, Yellow, Slate, Bright teal, Deep
  teal, Gray 300. Do not recolor series by hand.
- Label the series directly on the chart, not only in a legend. Yellow, Bright teal and Gray 300
  are light against White, so labels are what make them readable, and they help anyone who
  cannot tell the colors apart.
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
- **Round the corners of photos and panels** slightly, about 0.12 inch (3 mm), the same as the 12
  pixel corners on screen. Logos and charts stay square.
- **Use real lists.** Use the bullet and numbering buttons, never typed dashes or asterisks.

## Writing

Documents sound like the rest of MassChallenge: bold and human, direct and plain spoken.

- Put the point first: the decision, the ask or the takeaway.
- Use short sentences and everyday words. Write "we" for MassChallenge and "you" for the reader.
- Make a slide title say the takeaway, not the topic: "Applications grew in every program", not
  "Applications".
- Skip buzzwords such as leverage, seamless and robust, and skip exclamation marks.
- Use commas, colons and periods. Do not use em dashes or en dashes.

## About MassChallenge

Anything that goes outside MassChallenge, such as a proposal, a report or a pitch deck, ends with
a short About MassChallenge paragraph or slide. Quote one of these versions exactly. Use the short
version on a slide and the medium or long version in a document.

**Short**

> Born in Massachusetts and built for the world, MassChallenge backs the rare humans with the grit to solve the world's hardest challenges.

**Medium**

> Born in Massachusetts and built for the world, MassChallenge backs the rare humans with the grit to solve the world's hardest challenges. What began in New England's innovation corridor is now a global network connecting startups, experts, and partners across industries and continents, all working to turn bold ideas into outcomes that matter.

**Long**

> Born in Massachusetts and built for the world, MassChallenge backs the rare humans with the grit to solve the world's hardest challenges. What began in New England's innovation corridor is now a global network connecting startups, experts, and partners across industries and continents, all working to turn bold ideas into outcomes that matter. We are the earliest believer in founders tackling complex, regulated, and high-stakes problems, providing the infrastructure, access, and catalytic capital to move from proof to scale. Since 2009, MassChallenge has supported more than 5,000 startups across five Challenge Areas, helping them raise $16B+ in funding, create 90K jobs, and collaborate with more than 500 partners worldwide.

The figures in the long version are as of November 2026. Show that date whenever you use a
figure.

Our primary line is "We back the rare humans with the grit to solve
the toughest challenges." "It takes a community to raise a startup" is a founder's testimonial,
not a MassChallenge line, so never use it as a tagline.

## Contact and legal lines

Use these lines in footers and on closing slides. The templates already carry them.

- **Email:** contact@masschallenge.org
- **Copyright:** © MassChallenge 2026, with the current year.
- **No trademark symbol** on the MassChallenge name or logo.

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

# PowerPoint

This guide covers pitch decks, program updates, workshop slides and event presentations in
Microsoft PowerPoint. Read the [foundations](foundations.md) first: they set the colors, fonts and
voice this guide applies.

## Start from the template

1. Install [`propellant-presentation.potx`](../templates/powerpoint/propellant-presentation.potx)
   as described in [installing the templates](templates.md).
2. In PowerPoint, choose **File**, then **New**, then **Personal** (or **Shared**), and pick
   **Propellant presentation**.
3. The template opens with eight sample slides that show every layout. Keep the ones you need,
   delete the rest, and add new slides with **Home**, then **New Slide**.

Moving an existing deck to Propellant? Choose **Design**, then the arrow beside the themes, then
**Browse for Themes**, and pick [`Propellant.thmx`](../templates/powerpoint/Propellant.thmx). That
switches the colors and fonts. Then reapply each slide's layout from **Home**, then **Layout**.

## Slide size

Slides are widescreen 16:9, 13.333 by 7.5 inches, PowerPoint's default. Keep it: it fits every
screen and video call. Do not switch to 4:3.

## Layouts

Always pick a layout instead of drawing your own text boxes. Layouts keep titles in the same
place on every slide, and screen readers use the title placeholder to name each slide.

| Layout | Use it for |
| --- | --- |
| Title Slide | The first slide. Navy, white logo, title in Oswald SemiBold capitals, subtitle in Cyan. |
| Title and Content | Most slides: a title and up to five bullets, a chart, a table or a photo. |
| Section Header | Dividing a long deck into parts. Deep Teal, with the white logo and a Cyan subtitle. Also the closing slide. |
| Two Content | Before and after, or two options side by side. |
| Comparison | Two options, each with a short heading. |
| Title Only | A big number, a quote or a diagram you place yourself. |
| Picture with Caption | One photo filling the left half, with a title and caption on the right. |
| Blank | A full bleed photo or video. It has no logo, so nothing sits on the photo by accident. |

Use the dark slides (Navy and Deep Teal) only for the title, section breaks and the closing slide.
Everything in between is White, so the dark moments stand out. On a dark slide, text is White and
accents are Cyan; on a white slide, colored text is Teal.

## The closing slide

The last sample slide closes the deck on Deep Teal. It carries the presenter's name, email and
next step, the short [About MassChallenge](foundations.md#about-masschallenge) line, and the
contact and copyright lines: contact@masschallenge.org and © MassChallenge 2026. Keep the About
line word for word, update the year when it changes, and never add a trademark symbol. A deck
that goes outside MassChallenge ends with this slide.

## Titles

- Make every title say the takeaway: "Applications grew in every program", not "Applications".
- Keep titles to one line, about 40 characters. The template sets them in Oswald SemiBold
  capitals with a line spacing of 1.0; type them in sentence case and the style does the rest.
- For a two tone title, set the lead phrase in Black (White on a dark slide) and the payoff in
  Teal (Cyan on a dark slide).
- Give every slide a different title, even if you then hide it. PowerPoint's accessibility
  checker flags a missing title as an error.

## Text

- One idea per slide. If you need more than five bullets, split the slide.
- Body text is Lato with a line spacing of 1.5. Never set bullets in Oswald or in capitals.
- Keep bullets short, without full stops on single lines, and one level deep where you can.
- Never shrink text below 18 pt to make it fit. Microsoft
  [recommends 18 pt or larger](https://support.microsoft.com/en-us/accessibility/powerpoint/make-your-powerpoint-presentations-accessible-to-people-with-disabilities).
  Cut words instead.
- Put detail in the speaker notes, not on the slide.

## Big numbers and quotes

The two Title Only samples show how:

- **A big number:** the number in Oswald Bold at about 120 pt in Teal (Cyan on a dark slide), with
  one line underneath saying what it means and where it comes from. Always give the source.
  Oswald Bold is only for numbers like this. A single short Yellow rule can sit with the number as
  the deck's one warm accent; never color a number Raspberry.
- **A quote:** the quote in Lato at about 36 pt with real curly quote marks, and the person's
  name, role and company below in Slate. Only quote people who agreed to be quoted.

## Charts

- Insert charts with **Insert**, then **Chart**, so they take their colors from the theme.
- Use the chart rules in the [foundations](foundations.md#charts): one series in Teal, labels on
  the chart when there are more, four series at most, one axis.
- Remove what does not help: gridlines down to a few light ones, no 3D, no shadows, no chart
  border.
- Put the takeaway in the slide title and the source in small text below the chart.

## Photos and video

- Use photos that fill the frame: the Picture with Caption layout, or a full bleed photo on a
  Blank slide.
- When you crop, crop on purpose: keep faces and heads whole and leave the people looking into
  the slide. Use **Picture Format**, then **Crop**, then **Fill**, and drag the photo to place it.
- Put text on a photo only over a calm, high contrast area. Otherwise move it, add the hero
  overlay, or set it on a solid Navy, Black or Deep Teal block, as the
  [photography guide](photography.md#color-treatment) explains. Use the white logo on dark photos.
- For video, insert the file or a link with **Insert**, then **Video**, add captions, and set it
  to start when clicked, not automatically.
- Follow the [photography guide](photography.md), including alt text for every photo.

## The logo

The template places the logo for you: the white logo at the top left of the Navy and Deep Teal
slides and the full color logo at the bottom right of white slides, each with clear space equal to
the height of the "M" in the wordmark. Do not add another logo, and do not move it into the
content area.

- The full color logo goes only on White or Warm White. The white logo goes on Navy, Black, Deep
  Teal, Teal, MC Blue or a photo with enough contrast, never on Cyan, Yellow or Lime.
- The Blank layout has no logo. On a full bleed photo, place the white logo from
  [`assets/logos`](../assets/logos) in a calm, dark corner, adding the hero overlay or a solid
  Navy block behind it if the photo is busy.
- On a sponsor slide or a banner, keep the horizontal logo at least 160 px wide on screen, and
  align it to a corner or the top edge.
- Never recolor, stretch, rotate or add effects to the logo, and never build a lockup with a
  partner's logo. Ask MassChallenge Marketing for partner lockups.

## Presenting and sharing

1. Run **Review**, then **Check Accessibility**, and fix every error and warning.
2. Check the reading order of busy slides in the **Reading Order** pane.
3. To send the deck to someone outside MassChallenge, send a PDF, or
   [embed the fonts](foundations.md#sending-files-outside-masschallenge) if they need to edit it.
   The template has **Embed fonts in the file** turned on already; check it once in **File**,
   **Options**, **Save** before you send a deck that did not start from the template.
4. Before presenting on someone else's computer, check that Lato and Oswald are installed there,
   or bring a PDF.

## Things to avoid

- Animations other than a simple Appear or Fade, and slide transitions other than Fade.
- Teal text on Navy, MC Blue text anywhere, and Cyan text on a white slide.
- More than one warm accent in a deck, or a warm accent as a large background.
- Logos, icons or photos copied from a web search.
- Busy backgrounds, shadows and outlines on text. The only gradient is the MC Gradient, from Navy
  to Ocean.
- Slides read word for word. If the slide says it all, the presenter has nothing to add.

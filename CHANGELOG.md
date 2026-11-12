# Changelog

All notable changes to Propellant for Office are recorded here. The project follows semantic
versioning.

## Unreleased

### Changed: MassChallenge Brand Guidelines 2026

Propellant for Office now applies the MassChallenge brand guidelines from MassChallenge Marketing
instead of setting brand standards of its own. Messaging, voice, the About MassChallenge lines and
the approved figures are unchanged.

- The palette is the brand palette: the core colors MC Blue, MC Gray, Navy, Black and Warm White,
  the supporting blues Deep Teal, Teal, Cyan and Ocean, and the warm accents Yellow, Orange,
  Raspberry and Lime, with hex, RGB, approximate CMYK and print substitutes. The old Propellant
  brand names Deep teal, Teal, Mid teal, Bright teal, Pale teal, Mist, Ink, Magenta, Logo teal
  and Logo gray are retired from the templates and guides.
- The theme maps Black to Dark 1, White to Light 1, Navy to Dark 2 and Warm White to Light 2, the
  accents follow the new chart order (Teal, Yellow, Navy, MC Blue, Deep Teal, Gray 300), and links
  are Teal.
- Titles and main headings are Oswald SemiBold capitals with a line spacing of 1.0, body text is
  Lato with a line spacing of 1.5, and the big number is Oswald Bold in Teal. Document headings 1
  and 2 move from Lato Bold to Oswald SemiBold capitals.
- The fallback when Oswald or Lato will not load is Aptos Narrow Bold capitals for headers and
  Aptos for body text, never Arial.
- The title slide is Navy and the section and closing slides are Deep Teal, with White titles and
  Cyan subtitles. Table headers are Navy, and table stripes and callouts are Warm White.
- The presentation template has Embed fonts in the file turned on, without subsetting, and its
  bullets use Lato.
- The generator picks the logo for each background by the brand rules (full color only on White or
  Warm White, white on Navy, Black, Deep Teal, Teal or MC Blue), keeps clear space equal to the
  height of the wordmark's M, and checks the print and screen minimum sizes. The Blank layout no
  longer shows the logo, so it never lands on a full bleed photo.
- The logo rules cover the vertical, horizontal, MC mark and local versions, the backgrounds,
  clear space and minimum sizes. Vertical and local logo files come from MassChallenge Marketing.
  The shipped logo files are unchanged and will be replaced when MassChallenge Marketing supplies
  updated official artwork in MC Blue and MC Gray.
- The photography guide adopts the brand guide's imagery and video direction: the overlay, full
  color and accent rescue treatments, the hero overlay, warmth in every image, what to avoid,
  licensed stock that MassChallenge holds a license for, the standard slates and lower thirds.
  The teal duotone is retired.
- The CMYK values are approximate until confirmed with a printer's proof.

### Added

- PNG previews of the first page or slide of the document, presentation and workbook templates in
  `templates/previews`, rendered by the build with LibreOffice.
- The short About MassChallenge line, contact@masschallenge.org and the © MassChallenge copyright
  line on the presentation's closing slide, and the copyright and email in the document footer.
- The standard palette in the foundations, with hex, RGB and print CMYK values, how the CMYK
  values were calculated, the supporting neutrals Gray 100 and Gray 300, and the logo colors.
- The About MassChallenge boilerplate in short, medium and long versions, with the as-of date for
  its figures, and the contact and legal lines.
- The photo library, the teal duotone and the hexagon network frame in the photography guide.

### Changed

- Magenta is now `#BF0261` and Mist is now `#F3FBFC` everywhere. The gray
  `#F3F6F7` that the templates called Mist is replaced by Mist, so the theme's Light 2 and the
  table stripes are now Mist.
- The sixth theme accent is named Gray 300 and table lines Gray 100, after their Propellant tokens.
- The foundations say where each font applies, including product screens and email.
- The teal duotone runs from Deep teal to Bright teal, instead of Deep teal to Pale teal.

## 1.0.0 (2026-11-10)

The first release.

### Added

- Guides for designing documents, presentations and spreadsheets in Word, PowerPoint, Excel,
  Google Docs, Google Slides and Google Sheets, with shared foundations for color, type, the logo,
  layout, writing and accessibility.
- A photography and video guide covering our own photos and videos, licensed stock, permission,
  color treatment, cropping, captions and alt text.
- Templates for Word (`.dotx` and `.docx`), PowerPoint (`.potx` and `.pptx`) and Excel (`.xltx`
  and `.xlsx`), and a `Propellant.thmx` theme for existing files, all generated from the Propellant
  colors, fonts and logos.
- Instructions for installing the templates personally and for everyone through Microsoft 365 and
  Google Workspace.

# Changelog

All notable changes to Propellant for Office are recorded here. The project follows semantic
versioning.

## Unreleased

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

- Magenta is now `#BF0261` and Mist is now `#F3FBFC`, the website's values, everywhere. The gray
  `#F3F6F7` that the templates called Mist is replaced by Mist, so the theme's Light 2 and the
  table stripes are now Mist.
- The sixth theme accent is named Gray 300 and table lines Gray 100, after their Propellant tokens.
- The foundations say where each font applies, including product screens and email.
- The teal duotone runs from Deep teal to Bright teal, as on the website, instead of Deep teal to
  Pale teal.

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

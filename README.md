<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/brand/propellant-lockup-white.svg" />
  <img src="assets/brand/propellant-lockup-color.svg" alt="Propellant" height="64" />
</picture>

# Propellant for Office

Propellant is how MassChallenge looks, sounds and works. This repository brings it to the files we
make every day: documents, presentations and spreadsheets in Microsoft Word, PowerPoint and Excel,
and in Google Docs, Slides and Sheets. It has the guides for designing each one, templates you can
import, and the rules for photography and video.

It follows the same brand, colors, fonts and voice as [Propellant for the web](https://github.com/masschallenge/propellant-web),
and its guides are published at [propellant.masschallenge.org](https://propellant.masschallenge.org).

## Start here

1. Read [designing documents, decks and spreadsheets](docs/foundations.md): the colors, fonts,
   logo, layout, writing and accessibility rules every file follows.
2. [Install the templates](docs/templates.md) for the apps you use.
3. Open the guide for your app.

## Guides

- [Word](docs/word.md)
- [PowerPoint](docs/powerpoint.md)
- [Excel](docs/excel.md)
- [Google Docs](docs/google-docs.md)
- [Google Slides](docs/google-slides.md)
- [Google Sheets](docs/google-sheets.md)
- [Photography and video](docs/photography.md): our own photos and videos, stock, color treatment,
  cropping, captions and alt text
- [Installing the templates](docs/templates.md): for yourself, and for everyone through Microsoft
  365 and Google Workspace

## Templates

| Template | Microsoft Office | Google Workspace |
| --- | --- | --- |
| Document | [`propellant-document.dotx`](templates/word/propellant-document.dotx) | [`propellant-document.docx`](templates/word/propellant-document.docx) |
| Presentation | [`propellant-presentation.potx`](templates/powerpoint/propellant-presentation.potx) | [`propellant-presentation.pptx`](templates/powerpoint/propellant-presentation.pptx) |
| Workbook | [`propellant-workbook.xltx`](templates/excel/propellant-workbook.xltx) | [`propellant-workbook.xlsx`](templates/excel/propellant-workbook.xlsx) |
| Theme | [`Propellant.thmx`](templates/powerpoint/Propellant.thmx): colors and fonts for any existing Office file | |

Every template uses Lato and Oswald, free fonts from Google Fonts. Google Workspace has both;
Office computers need them installed. [Foundations](docs/foundations.md#fonts) explains how.

## Building the templates

The templates are generated from the Propellant colors, fonts and logos, so they always agree with
each other and with the web. To rebuild them:

```bash
python3 -m pip install -r requirements.txt
python3 scripts/build_templates.py
python3 -m unittest discover -s tests
```

The build is reproducible: the same source always makes the same files, and the checks fail if the
committed templates are out of date.

## Contributing and security

See [CONTRIBUTING.md](CONTRIBUTING.md) and [SECURITY.md](SECURITY.md).

## License

The guides and scripts are MIT licensed. The MassChallenge and Propellant names and logos are not;
see [LICENSE](LICENSE).

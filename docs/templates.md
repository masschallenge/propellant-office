# Installing the templates

The templates are in the [`templates`](../templates) folder. Each comes in two forms: a template
file for Microsoft Office (`.dotx`, `.potx`, `.xltx`) that opens a fresh copy every time, and a
regular file (`.docx`, `.pptx`, `.xlsx`) for Google Workspace and for opening directly.

| Template | Office | Google Workspace |
| --- | --- | --- |
| Document | `word/propellant-document.dotx` | `word/propellant-document.docx` |
| Presentation | `powerpoint/propellant-presentation.potx` | `powerpoint/propellant-presentation.pptx` |
| Workbook | `excel/propellant-workbook.xltx` | `excel/propellant-workbook.xlsx` |
| Theme only | `powerpoint/Propellant.thmx` | Not needed |

Install [Lato and Oswald](foundations.md#getting-the-fonts) first, or Office will show other
fonts.

## What the templates carry

- **Colors:** the Propellant theme, built from the [standard palette](foundations.md#the-palette),
  with Mist `#F3FBFC` as Light 2 and the chart colors in the standard order: Teal, Yellow, Slate,
  Bright teal, Deep teal, Gray 300. Table stripes are Mist and table lines are Gray 100 `#DBE1E3`.
- **Fonts:** Lato for all text and Oswald capitals for titles, as
  [the foundations](foundations.md#fonts) set out.
- **Contact and legal lines:** the document footer reads "© MassChallenge 2026 |
  contact@masschallenge.org | Page", and the closing slide of the presentation carries the same
  email and copyright line under the short [About MassChallenge](foundations.md#about-masschallenge)
  line. Neither uses a trademark symbol. The year comes from the build date in
  `scripts/propellant_office/brand.py`, so update that date and rebuild when the year changes.

## For yourself

### Microsoft Office on Windows

1. Download the `.dotx`, `.potx` and `.xltx` files.
2. Save them to your personal templates folder: type `%appdata%\Microsoft\Templates` into the
   File Explorer address bar.
3. In Word, PowerPoint and Excel, choose **File**, then **Options**, then **Save**, and paste the
   same folder into **Default personal templates location**.
4. Choose **File**, then **New**, then **Personal** to find the templates.

Microsoft's page [Where are my custom templates](https://support.microsoft.com/en-us/office/foundations-experiences/where-are-my-custom-templates)
has the details.

### Microsoft Office on Mac

1. Download the template files.
2. Save them to `~/Library/Group Containers/UBF8T346G9.Office/User Content/Templates`. In Finder,
   choose **Go**, then **Go to Folder**, and paste that path.
3. Choose **File**, then **New from Template** to find them.

### Microsoft Office on the web

Office on the web cannot open personal templates. Save the `.docx`, `.pptx` or `.xlsx` to
OneDrive, open it, and use **File**, then **Save a copy** before you start, so the original stays
clean.

### Google Workspace

Upload the `.docx`, `.pptx` or `.xlsx` to Drive and choose **File**, then **Save as Google Docs**
(or Slides, or Sheets). Keep that copy as your master and make a copy of it for each new
document. The guides for [Google Docs](google-docs.md), [Google Slides](google-slides.md) and
[Google Sheets](google-sheets.md) cover the details.

## For everyone at MassChallenge

These steps need an administrator.

### Microsoft 365

- **Templates:** a SharePoint administrator can create an
  [organization assets library](https://learn.microsoft.com/en-us/sharepoint/organization-assets-library)
  for templates and upload the `.dotx`, `.potx` and `.xltx` files. They then appear for everyone
  in Word, PowerPoint and Excel on Windows and Mac, and in PowerPoint on the web, under the
  organization's name. Word and Excel on the web do not show them.
- **Fonts:** the same administrator can
  [publish Lato and Oswald as organization fonts](https://learn.microsoft.com/en-us/sharepoint/support-for-organization-fonts-in-powerpoint-for-the-web)
  so they work in PowerPoint and Word on every platform, including the web, without anyone
  installing them. Both fonts are free under the SIL Open Font License, which allows installing,
  using and hosting them for any work. Allow up to a day for both to appear.
- **Installing the fonts:** IT can also install Lato and Oswald on every managed computer.

### Google Workspace

- **Template gallery:** an administrator can
  [turn on custom templates](https://knowledge.workspace.google.com/admin/drive/turn-custom-drive-templates-on-or-off-for-users)
  in the Admin console under **Apps**, then **Google Workspace**, then **Drive and Docs**, then
  **Templates**. Then submit the converted Google Docs, Slides and Sheets templates to the
  MassChallenge section of the gallery.
- **Default theme:** with organization branding turned on, an administrator can
  [set a default Slides theme](https://knowledge.workspace.google.com/admin/drive/what-are-default-templates-and-themes)
  so every new presentation starts with Propellant.
- **Copy links:** for anyone else, share a Google copy of each template and change the end of its
  link from `/edit` to `/copy`. Opening that link makes the person their own copy.

## Updating the templates

The templates are generated by `scripts/build_templates.py` from the Propellant colors, fonts and
logos, so they never drift apart. When the brand changes, the templates are rebuilt and released
together. Replace your installed copies with the files from the latest release.

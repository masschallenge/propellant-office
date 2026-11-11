import re
import sys
import tempfile
import unittest
import zipfile
from unittest import mock
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from propellant_office.brand import BODY_FONT, HEADLINE_FONT, THEME_COLORS  # noqa: E402
from propellant_office.excel import build_excel_template  # noqa: E402
from propellant_office.powerpoint import build_powerpoint_template  # noqa: E402
from propellant_office import previews  # noqa: E402
from propellant_office.theme import brand_theme_xml, color_scheme_xml  # noqa: E402
from propellant_office.word import build_word_template  # noqa: E402

LOGOS = ROOT / "assets" / "logos"

TEMPLATE_TYPES = {
    "propellant-document.dotx": "wordprocessingml.template.main+xml",
    "propellant-presentation.potx": "presentationml.template.main+xml",
    "propellant-workbook.xltx": "spreadsheetml.template.main+xml",
}


def read_entry(path, pattern):
    with zipfile.ZipFile(path) as package:
        names = [name for name in package.namelist() if re.search(pattern, name)]
        return [package.read(name).decode("utf-8") for name in names]


class BuiltTemplates(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.output = Path(tempfile.mkdtemp())
        build_word_template(cls.output, LOGOS)
        build_powerpoint_template(cls.output, LOGOS)
        build_excel_template(cls.output, LOGOS)
        cls.files = sorted(path for path in cls.output.iterdir())

    def test_builds_every_document_template_and_theme(self):
        names = {path.name for path in self.files}
        self.assertEqual(
            names,
            {
                "propellant-document.docx",
                "propellant-document.dotx",
                "propellant-presentation.pptx",
                "propellant-presentation.potx",
                "propellant-workbook.xlsx",
                "propellant-workbook.xltx",
                "Propellant.thmx",
            },
        )

    def test_every_file_carries_the_propellant_theme(self):
        for path in self.files:
            themes = read_entry(path, r"theme/theme\d*\.xml$")
            self.assertTrue(themes, f"{path.name} has no theme")
            for theme in themes:
                for slot, color in THEME_COLORS.items():
                    self.assertRegex(theme, rf'<a:{slot}><a:srgbClr val="{color}"/>', f"{path.name} {slot}")
                self.assertIn(f'<a:majorFont><a:latin typeface="{HEADLINE_FONT}"/>', theme)
                self.assertIn(f'<a:minorFont><a:latin typeface="{BODY_FONT}"/>', theme)

    def test_template_files_declare_template_content_types(self):
        for name, content_type in TEMPLATE_TYPES.items():
            [types] = read_entry(self.output / name, r"^\[Content_Types\]\.xml$")
            self.assertIn(content_type, types, name)

    def test_presentation_is_widescreen_with_logos_on_master_and_dark_layouts(self):
        [presentation] = read_entry(self.output / "propellant-presentation.pptx", r"^ppt/presentation\.xml$")
        self.assertIn('<p:sldSz cx="12191695" cy="6858000"', presentation)
        [master_relationships] = read_entry(
            self.output / "propellant-presentation.pptx", r"slideMasters/_rels/slideMaster1\.xml\.rels$"
        )
        self.assertIn("relationships/image", master_relationships)
        [title_layout] = read_entry(self.output / "propellant-presentation.pptx", r"slideLayouts/slideLayout1\.xml$")
        self.assertIn('<a:srgbClr val="044451"/>', title_layout)
        self.assertIn('showMasterSp="0"', title_layout)

    def test_presentation_titles_are_capitals_in_the_headline_font(self):
        [master] = read_entry(self.output / "propellant-presentation.pptx", r"slideMasters/slideMaster1\.xml$")
        title_style = re.search(r"<p:titleStyle>.*?</p:titleStyle>", master, re.S).group(0)
        self.assertIn('cap="all"', title_style)
        self.assertIn('typeface="+mj-lt"', title_style)

    def test_document_headings_use_the_body_font_not_the_theme_heading_font(self):
        [styles] = read_entry(self.output / "propellant-document.docx", r"^word/styles\.xml$")
        heading = re.search(r'<w:style [^>]*w:styleId="Heading1".*?</w:style>', styles, re.S).group(0)
        self.assertIn(f'w:ascii="{BODY_FONT}"', heading)
        self.assertNotIn("asciiTheme", heading)
        title = re.search(r'<w:style [^>]*w:styleId="Title".*?</w:style>', styles, re.S).group(0)
        self.assertIn(f'w:ascii="{HEADLINE_FONT}"', title)
        self.assertIn("<w:caps/>", title)

    def test_workbook_default_font_is_the_body_font(self):
        [styles] = read_entry(self.output / "propellant-workbook.xlsx", r"^xl/styles\.xml$")
        first_font = re.search(r"<font>.*?</font>", styles, re.S).group(0)
        self.assertIn(f'val="{BODY_FONT}"', first_font)


class ThemeRewriting(unittest.TestCase):
    def test_replaces_colors_fonts_and_name(self):
        original = (
            '<a:theme xmlns:a="x" name="Office Theme"><a:themeElements>'
            '<a:clrScheme name="Office"><a:dk1><a:sysClr val="windowText"/></a:dk1></a:clrScheme>'
            '<a:fontScheme name="Office"><a:majorFont/></a:fontScheme>'
            "</a:themeElements></a:theme>"
        )
        branded = brand_theme_xml(original)
        self.assertIn('name="Propellant"', branded)
        self.assertIn(color_scheme_xml(), branded)
        self.assertNotIn("windowText", branded)


class TemplatePreviews(unittest.TestCase):
    def test_names_each_preview_after_its_template(self):
        self.assertEqual(previews.preview_name("word/propellant-document.docx"), "propellant-document.png")
        names = {previews.preview_name(source) for source in previews.PREVIEW_SOURCES}
        self.assertEqual(
            names,
            {"propellant-document.png", "propellant-presentation.png", "propellant-workbook.png"},
        )

    def test_previews_every_editable_template_that_is_committed(self):
        for source in previews.PREVIEW_SOURCES:
            self.assertTrue((ROOT / "templates" / source).exists(), source)

    def test_converts_headlessly_with_a_private_profile(self):
        arguments = previews.conversion_arguments("soffice", "in.docx", "out", "/tmp/profile")
        self.assertEqual(arguments[0], "soffice")
        self.assertIn("--headless", arguments)
        self.assertIn("-env:UserInstallation=file:///tmp/profile", arguments)
        self.assertEqual(arguments[-4:], ["png", "--outdir", "out", "in.docx"])

    def test_skips_quietly_without_libreoffice(self):
        with mock.patch.object(previews, "office_command", return_value=None):
            self.assertEqual(previews.render_previews(Path(tempfile.mkdtemp())), [])

    @unittest.skipUnless(previews.office_command(), "LibreOffice is not installed")
    def test_renders_the_same_png_every_time(self):
        source = ROOT / "templates" / previews.PREVIEW_SOURCES[1]
        output = Path(tempfile.mkdtemp())
        previews.render_preview(previews.office_command(), source, output / "first.png")
        previews.render_preview(previews.office_command(), source, output / "second.png")
        first = (output / "first.png").read_bytes()
        self.assertTrue(first.startswith(b"\x89PNG\r\n\x1a\n"))
        self.assertNotIn(b"tIME", first)
        self.assertEqual(first, (output / "second.png").read_bytes())


if __name__ == "__main__":
    unittest.main()

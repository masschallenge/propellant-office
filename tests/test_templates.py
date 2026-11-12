import re
import sys
import tempfile
import unittest
import zipfile
from unittest import mock
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from propellant_office.brand import (  # noqa: E402
    BLACK,
    BODY_FONT,
    BUILD_DATE,
    CHART_ORDER,
    CONTACT_EMAIL,
    COPYRIGHT_LINE,
    CYAN,
    DEEP_TEAL,
    FALLBACK_BODY_FONT,
    FALLBACK_HEADLINE_FONT,
    HEADLINE_FONT,
    HEADLINE_SEMIBOLD_FONT,
    HORIZONTAL_LOGO_PIXELS,
    LIME,
    LOGO_FILES,
    MC_BLUE,
    MC_GRAY,
    MINIMUM_PRINT_WIDTH_MM,
    MINIMUM_SCREEN_WIDTH_PIXELS,
    NAVY,
    ORANGE,
    PALETTE,
    RASPBERRY,
    RETIRED_FONTS,
    SHORT_BOILERPLATE,
    SUPPORTING_NEUTRALS,
    TEAL,
    THEME_COLORS,
    WARM_WHITE,
    WHITE,
    WORDMARK_M_HEIGHT_PIXELS,
    YELLOW,
    logo_clear_space,
    logo_for_background,
    logo_width_for_height,
)
from propellant_office.excel import build_excel_template  # noqa: E402
from propellant_office.powerpoint import build_powerpoint_template  # noqa: E402
from propellant_office import previews  # noqa: E402
from propellant_office.theme import brand_theme_xml, color_scheme_xml  # noqa: E402
from propellant_office.word import HEADER_LOGO_HEIGHT_INCHES, build_word_template, footer_text  # noqa: E402
from PIL import Image  # noqa: E402
from pptx import Presentation  # noqa: E402
from pptx.util import Emu  # noqa: E402

LOGOS = ROOT / "assets" / "logos"
DOCS = ROOT / "docs"

RETIRED_COLORS = (
    "A30253",
    "F3F6F7",
    "044451",
    "065E6F",
    "068DA4",
    "0FACBD",
    "D9F6FA",
    "F3FBFC",
    "1E282B",
    "C7F2EF",
    "003349",
)

EMU_PER_INCH = 914400
MILLIMETERS_PER_INCH = 25.4
SCREEN_PIXELS_PER_INCH = 96

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
        self.assertIn(f'<p:bg><p:bgPr><a:solidFill><a:srgbClr val="{NAVY}"/>', title_layout)
        self.assertIn('showMasterSp="0"', title_layout)
        [section_layout] = read_entry(self.output / "propellant-presentation.pptx", r"slideLayouts/slideLayout3\.xml$")
        self.assertIn(f'<p:bg><p:bgPr><a:solidFill><a:srgbClr val="{DEEP_TEAL}"/>', section_layout)
        self.assertIn(f'<a:srgbClr val="{CYAN}"/>', section_layout)

    def test_presentation_titles_are_semibold_capitals_set_solid(self):
        [master] = read_entry(self.output / "propellant-presentation.pptx", r"slideMasters/slideMaster1\.xml$")
        title_style = re.search(r"<p:titleStyle>.*?</p:titleStyle>", master, re.S).group(0)
        self.assertIn('cap="all"', title_style)
        self.assertIn(f'typeface="{HEADLINE_SEMIBOLD_FONT}"', title_style)
        self.assertIn('<a:lnSpc><a:spcPct val="100000"/></a:lnSpc>', title_style)
        self.assertIn(f'<a:srgbClr val="{BLACK}"/>', title_style)
        body_style = re.search(r"<p:bodyStyle>.*?</p:bodyStyle>", master, re.S).group(0)
        self.assertIn('<a:lnSpc><a:spcPct val="150000"/></a:lnSpc>', body_style)

    def test_presentation_bullets_use_the_body_font_and_no_dashes(self):
        [master] = read_entry(self.output / "propellant-presentation.pptx", r"slideMasters/slideMaster1\.xml$")
        self.assertEqual(set(re.findall(r'<a:buFont typeface="([^"]*)"', master)), {BODY_FONT})
        self.assertEqual(set(re.findall(r'<a:buChar char="([^"]*)"', master)), {"\u2022"})

    def test_presentation_embeds_whole_fonts_when_saved(self):
        [presentation] = read_entry(self.output / "propellant-presentation.pptx", r"^ppt/presentation\.xml$")
        self.assertIn('embedTrueTypeFonts="1"', presentation)
        self.assertIn('saveSubsetFonts="0"', presentation)

    def test_big_number_is_oswald_bold_in_teal(self):
        slides = read_entry(self.output / "propellant-presentation.pptx", r"^ppt/slides/slide\d+\.xml$")
        number_slide = next(slide for slide in slides if "00%" in slide)
        number_run = re.search(r"<a:r><a:rPr[^>]*>.*?</a:rPr><a:t>00%</a:t>", number_slide, re.S).group(0)
        self.assertIn('b="1"', number_run)
        self.assertIn(f'<a:srgbClr val="{TEAL}"/>', number_run)
        self.assertIn(f'typeface="{HEADLINE_FONT}"', number_run)

    def test_full_bleed_photo_layout_hides_the_master_logo(self):
        [blank_layout] = read_entry(self.output / "propellant-presentation.pptx", r"slideLayouts/slideLayout7\.xml$")
        self.assertIn('showMasterSp="0"', blank_layout)

    def test_document_headlines_are_oswald_semibold_capitals_and_body_is_spacious(self):
        [styles] = read_entry(self.output / "propellant-document.docx", r"^word/styles\.xml$")
        for style_id in ("Title", "Heading1", "Heading2"):
            style = re.search(rf'<w:style [^>]*w:styleId="{style_id}".*?</w:style>', styles, re.S).group(0)
            self.assertIn(f'w:ascii="{HEADLINE_SEMIBOLD_FONT}"', style, style_id)
            self.assertNotIn("asciiTheme", style, style_id)
            self.assertIn("<w:caps/>", style, style_id)
            self.assertIn('w:line="240"', style, style_id)
        heading_three = re.search(r'<w:style [^>]*w:styleId="Heading3".*?</w:style>', styles, re.S).group(0)
        self.assertIn(f'w:ascii="{BODY_FONT}"', heading_three)
        normal = re.search(r'<w:style [^>]*w:styleId="Normal".*?</w:style>', styles, re.S).group(0)
        self.assertIn(f'w:ascii="{BODY_FONT}"', normal)
        self.assertIn('w:line="360"', normal)

    def test_document_tables_and_callouts_use_navy_and_warm_white(self):
        [document] = read_entry(self.output / "propellant-document.docx", r"^word/document\.xml$")
        self.assertIn(f'w:fill="{NAVY}"', document)
        self.assertIn(f'w:fill="{WARM_WHITE}"', document)
        self.assertIn(f'w:color="{TEAL}"', document)

    def test_no_file_names_a_retired_font(self):
        for path in self.files:
            with zipfile.ZipFile(path) as package:
                for name in package.namelist():
                    if not name.endswith(".xml"):
                        continue
                    data = package.read(name).decode("utf-8")
                    for font in RETIRED_FONTS:
                        self.assertNotIn(f'typeface="{font}"', data, f"{path.name} {name}")
                        self.assertNotIn(f'w:ascii="{font}"', data, f"{path.name} {name}")
                        self.assertNotIn(f'<name val="{font}"', data, f"{path.name} {name}")

    def test_workbook_default_font_is_the_body_font(self):
        [styles] = read_entry(self.output / "propellant-workbook.xlsx", r"^xl/styles\.xml$")
        first_font = re.search(r"<font>.*?</font>", styles, re.S).group(0)
        self.assertIn(f'val="{BODY_FONT}"', first_font)
        self.assertIn(f'<name val="{HEADLINE_SEMIBOLD_FONT}"', styles)
        self.assertIn(f'rgb="00{NAVY}"', styles)
        self.assertIn(f'rgb="00{WARM_WHITE}"', styles)

    def test_no_file_carries_a_retired_brand_color(self):
        for path in self.files:
            with zipfile.ZipFile(path) as package:
                for name in package.namelist():
                    data = package.read(name).upper()
                    for color in RETIRED_COLORS:
                        self.assertNotIn(color.encode(), data, f"{path.name} {name}")

    def test_document_footer_carries_the_copyright_and_contact_lines(self):
        [footer] = read_entry(self.output / "propellant-document.docx", r"^word/footer\d*\.xml$")
        self.assertIn(COPYRIGHT_LINE, footer)
        self.assertIn(CONTACT_EMAIL, footer)
        self.assertNotIn("\u2122", footer)
        self.assertNotIn("\u00ae", footer)

    def test_closing_slide_carries_the_boilerplate_and_contact_lines(self):
        slides = read_entry(self.output / "propellant-presentation.pptx", r"^ppt/slides/slide\d+\.xml$")
        closing = next(slide for slide in slides if "Thank you" in slide)
        self.assertIn(SHORT_BOILERPLATE, closing)
        self.assertIn(CONTACT_EMAIL, closing)
        self.assertIn(COPYRIGHT_LINE, closing)


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


class BrandStandards(unittest.TestCase):
    def test_palette_carries_the_official_brand_values(self):
        official = {color.name: color.hex_value for color in PALETTE}
        self.assertEqual(
            official,
            {
                "MC Blue": "0EABBC",
                "MC Gray": "808285",
                "Navy": "10263F",
                "Black": "222222",
                "Warm White": "F8F8F5",
                "Deep Teal": "004F73",
                "Teal": "00708E",
                "Cyan": "54EEFF",
                "Ocean": "037AA6",
                "Yellow": "FFC801",
                "Orange": "FF6B35",
                "Raspberry": "D14170",
                "Lime": "C6F135",
            },
        )
        substitutes = {color.name: color.print_substitute for color in PALETTE if color.print_substitute}
        self.assertEqual(substitutes, {"Cyan": "00CFE8", "Orange": "F58242", "Raspberry": "D83B80", "Lime": "91D438"})
        names = [color.name for color in PALETTE + SUPPORTING_NEUTRALS]
        self.assertEqual(len(names), len(set(names)))
        for retired in ("Mist", "Ink", "Magenta", "Pale teal", "Mid teal", "Bright teal", "Logo teal", "Logo gray"):
            self.assertNotIn(retired, names)

    def test_theme_maps_the_palette_onto_the_office_slots(self):
        self.assertEqual(
            {slot: THEME_COLORS[slot] for slot in ("dk1", "lt1", "dk2", "lt2", "hlink", "folHlink")},
            {"dk1": BLACK, "lt1": WHITE, "dk2": NAVY, "lt2": WARM_WHITE, "hlink": TEAL, "folHlink": DEEP_TEAL},
        )

    def test_theme_accents_follow_the_standard_chart_order(self):
        accents = [THEME_COLORS[f"accent{position}"] for position in range(1, 7)]
        self.assertEqual(accents, list(CHART_ORDER))
        self.assertEqual(CHART_ORDER, ("00708E", "FFC801", "10263F", "0EABBC", "004F73", "848F92"))

    def test_fonts_and_fallbacks_follow_the_brand_guide(self):
        self.assertEqual((HEADLINE_FONT, HEADLINE_SEMIBOLD_FONT, BODY_FONT), ("Oswald", "Oswald SemiBold", "Lato"))
        self.assertEqual((FALLBACK_HEADLINE_FONT, FALLBACK_BODY_FONT), ("Aptos Narrow", "Aptos"))
        self.assertIn("Arial", RETIRED_FONTS)

    def test_copyright_line_has_no_trademark_symbol(self):
        self.assertEqual(COPYRIGHT_LINE, f"\u00a9 MassChallenge {BUILD_DATE.year}")
        self.assertIn(COPYRIGHT_LINE, footer_text())

    def test_foundations_list_every_color_with_hex_rgb_cmyk_and_print_substitute(self):
        foundations = (DOCS / "foundations.md").read_text("utf-8")
        for color in PALETTE + SUPPORTING_NEUTRALS:
            red, green, blue = (int(color.hex_value[index:index + 2], 16) for index in (0, 2, 4))
            row = re.search(rf"^\| {color.name} \|.*$", foundations, re.M)
            self.assertIsNotNone(row, color.name)
            self.assertIn(f"`#{color.hex_value}`", row.group(0))
            self.assertIn(f"{red} {green} {blue}", row.group(0))
            if color.approximate_cmyk:
                self.assertIn(" ".join(str(part) for part in color.approximate_cmyk), row.group(0))
            if color.print_substitute:
                self.assertIn(f"`#{color.print_substitute}`", row.group(0))
        self.assertNotIn("Pantone", foundations)
        self.assertNotIn("SWOP", foundations)

    def test_foundations_name_the_font_fallbacks_and_never_arial(self):
        foundations = (DOCS / "foundations.md").read_text("utf-8")
        self.assertIn(f"{FALLBACK_HEADLINE_FONT} Bold", foundations)
        self.assertIn(f"{FALLBACK_BODY_FONT} for", foundations)
        self.assertNotIn("falls back to Arial", foundations)

    def test_docs_quote_the_boilerplate_exactly_and_drop_retired_colors(self):
        for path in [*DOCS.glob("*.md"), ROOT / "README.md"]:
            text = path.read_text("utf-8")
            for color in RETIRED_COLORS:
                self.assertFalse(color in text.upper(), f"{path.name} {color}")
            self.assertFalse("\u2014" in text or "\u2013" in text, path.name)
        self.assertIn(SHORT_BOILERPLATE, (DOCS / "foundations.md").read_text("utf-8"))


class LogoRules(unittest.TestCase):
    def test_full_color_logo_only_on_white_or_warm_white(self):
        for background in (WHITE, WARM_WHITE):
            self.assertEqual(logo_for_background(background), LOGO_FILES["color"])
        self.assertEqual(logo_for_background(WARM_WHITE.lower()), LOGO_FILES["color"])

    def test_white_logo_on_the_approved_dark_colors(self):
        for background in (NAVY, BLACK, DEEP_TEAL, TEAL, MC_BLUE):
            self.assertEqual(logo_for_background(background), LOGO_FILES["white"])
        self.assertEqual(logo_for_background(NAVY, mark="monogram"), LOGO_FILES["monogram_white"])

    def test_no_logo_on_light_or_warm_accent_colors(self):
        for background in (CYAN, YELLOW, LIME, ORANGE, RASPBERRY, MC_GRAY):
            with self.assertRaises(ValueError):
                logo_for_background(background)

    def test_clear_space_is_the_height_of_the_wordmark_m(self):
        with Image.open(LOGOS / LOGO_FILES["color"]) as logo:
            self.assertEqual(logo.size, HORIZONTAL_LOGO_PIXELS)
            alpha = logo.getchannel("A")
            width, height = logo.size
            letter_m_columns = range(470, 561)
            opaque_rows = [
                row for row in range(height) if any(alpha.getpixel((column, row)) > 128 for column in letter_m_columns)
            ]
        self.assertEqual(max(opaque_rows) - min(opaque_rows) + 1, WORDMARK_M_HEIGHT_PIXELS)
        self.assertAlmostEqual(logo_clear_space(HORIZONTAL_LOGO_PIXELS[1]), WORDMARK_M_HEIGHT_PIXELS)

    def test_logo_width_keeps_the_artwork_proportions(self):
        self.assertAlmostEqual(logo_width_for_height(225), 1671)

    def test_document_logo_meets_the_print_minimum(self):
        width_millimeters = logo_width_for_height(HEADER_LOGO_HEIGHT_INCHES) * MILLIMETERS_PER_INCH
        self.assertGreaterEqual(width_millimeters, MINIMUM_PRINT_WIDTH_MM["horizontal"])


class PresentationLogos(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        output = Path(tempfile.mkdtemp())
        build_powerpoint_template(output, LOGOS)
        cls.presentation = Presentation(str(output / "propellant-presentation.pptx"))
        cls.logo_bytes = {
            treatment: (LOGOS / LOGO_FILES[treatment]).read_bytes() for treatment in ("color", "white")
        }

    def pictures(self, owner):
        return [shape for shape in owner.shapes if shape.shape_type == 13]

    def owners(self):
        yield self.presentation.slide_master, WHITE
        for layout in self.presentation.slide_layouts:
            background = re.search(r'<p:bg>\s*<p:bgPr>\s*<a:solidFill>\s*<a:srgbClr val="([0-9A-F]{6})"/>', layout.element.xml)
            yield layout, background.group(1) if background else WHITE

    def test_each_logo_matches_its_background(self):
        checked = 0
        for owner, background in self.owners():
            for picture in self.pictures(owner):
                expected = "color" if background in (WHITE, WARM_WHITE) else "white"
                self.assertEqual(picture.image.blob, self.logo_bytes[expected], owner.name)
                checked += 1
        self.assertEqual(checked, 3)

    def test_logos_keep_clear_space_from_edges_and_placeholders(self):
        slide_width = self.presentation.slide_width
        slide_height = self.presentation.slide_height
        for owner, _ in self.owners():
            for picture in self.pictures(owner):
                clear_space = Emu(round(logo_clear_space(picture.height)))
                self.assertGreaterEqual(picture.left, clear_space, owner.name)
                self.assertGreaterEqual(picture.top, clear_space, owner.name)
                self.assertGreaterEqual(slide_width - picture.left - picture.width, clear_space, owner.name)
                self.assertGreaterEqual(slide_height - picture.top - picture.height, clear_space, owner.name)
                for placeholder in owner.placeholders:
                    if placeholder.left is None:
                        continue
                    separated = (
                        placeholder.left >= picture.left + picture.width + clear_space
                        or placeholder.left + placeholder.width <= picture.left - clear_space
                        or placeholder.top >= picture.top + picture.height + clear_space
                        or placeholder.top + placeholder.height <= picture.top - clear_space
                    )
                    self.assertTrue(separated, f"{owner.name} {placeholder.name}")

    def test_slide_logos_meet_the_screen_minimum(self):
        for owner, _ in self.owners():
            for picture in self.pictures(owner):
                width_pixels = picture.width / EMU_PER_INCH * SCREEN_PIXELS_PER_INCH
                self.assertGreaterEqual(width_pixels, MINIMUM_SCREEN_WIDTH_PIXELS["horizontal"], owner.name)


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

    def test_explains_why_a_conversion_failed(self):
        failure = previews.subprocess.CalledProcessError(1, ["soffice"], stderr="source file could not be loaded\n")
        with mock.patch.object(previews.subprocess, "run", side_effect=failure):
            with self.assertRaisesRegex(RuntimeError, "source file could not be loaded"):
                previews.render_preview("soffice", Path("in.docx"), Path(tempfile.mkdtemp()) / "out.png")

    def test_gives_up_on_a_conversion_that_hangs(self):
        hang = previews.subprocess.TimeoutExpired(["soffice"], previews.CONVERSION_TIMEOUT_SECONDS)
        with mock.patch.object(previews.subprocess, "run", side_effect=hang) as run:
            with self.assertRaisesRegex(RuntimeError, "longer than 120 seconds"):
                previews.render_preview("soffice", Path("in.docx"), Path(tempfile.mkdtemp()) / "out.png")
        self.assertEqual(run.call_args.kwargs["timeout"], 120)

    def test_renders_text_unhinted_in_grayscale_on_every_machine(self):
        config = previews.RENDER_FONT_CONFIG.read_text("utf-8")
        self.assertIn('<include ignore_missing="yes">/etc/fonts/fonts.conf</include>', config)
        for setting in [
            '<edit name="hinting" mode="assign"><bool>false</bool></edit>',
            '<edit name="hintstyle" mode="assign"><const>hintnone</const></edit>',
            '<edit name="antialias" mode="assign"><bool>true</bool></edit>',
            '<edit name="rgba" mode="assign"><const>none</const></edit>',
        ]:
            self.assertIn(setting, config)
        environment = previews.rendering_environment()
        self.assertEqual(environment["FONTCONFIG_FILE"], str(previews.RENDER_FONT_CONFIG))
        self.assertEqual(environment.get("PATH"), previews.os.environ.get("PATH"))

    def test_renders_oswald_semibold_as_the_semibold_instance(self):
        config = previews.RENDER_FONT_CONFIG.read_text("utf-8")
        self.assertIn(f"<test name=\"family\"><string>{HEADLINE_SEMIBOLD_FONT}</string></test>", config)
        self.assertIn(f"<string>{HEADLINE_FONT}</string></edit>", config)
        self.assertIn("<const>semibold</const>", config)

    def test_renders_with_the_pinned_font_settings(self):
        hang = previews.subprocess.TimeoutExpired(["soffice"], previews.CONVERSION_TIMEOUT_SECONDS)
        with mock.patch.object(previews.subprocess, "run", side_effect=hang) as run:
            with self.assertRaises(RuntimeError):
                previews.render_preview("soffice", Path("in.docx"), Path(tempfile.mkdtemp()) / "out.png")
        self.assertEqual(run.call_args.kwargs["env"]["FONTCONFIG_FILE"], str(previews.RENDER_FONT_CONFIG))

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

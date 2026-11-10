from copy import deepcopy
from io import BytesIO
from pathlib import Path

from lxml import etree
import pptx
from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.opc.constants import RELATIONSHIP_TYPE
from pptx.oxml.ns import qn
from pptx.util import Inches, Pt

from .brand import BRIGHT_TEAL, BUILD_DATE, DEEP_TEAL, INK, LOGO_FILES, SLATE, WHITE
from .theme import as_template_package, brand_package_themes, theme_file_package

BASE_THEME = Path(pptx.__file__).parent / "templates" / "theme.xml"

SLIDE_WIDTH = Inches(13.333)
SLIDE_HEIGHT = Inches(7.5)

TITLE_SLIDE = 0
TITLE_AND_CONTENT = 1
SECTION_HEADER = 2
TWO_CONTENT = 3
TITLE_ONLY = 5
BLANK = 6
PICTURE_WITH_CAPTION = 8

DARK_LAYOUTS = (TITLE_SLIDE, SECTION_HEADER)
CAPTION_LAYOUTS = (7, PICTURE_WITH_CAPTION)


MARGIN = 0.9
CONTENT_WIDTH = 13.333 - 2 * MARGIN
TITLE_BOX = (MARGIN, 0.5, CONTENT_WIDTH, 1.1)
BODY_BOX = (MARGIN, 1.85, CONTENT_WIDTH, 4.7)
HALF_WIDTH = (CONTENT_WIDTH - 0.5) / 2
FOOTER_BOXES = {
    "DATE": (MARGIN + 3.4, 6.85, 2.0, 0.4),
    "FOOTER": (MARGIN + 0.9, 6.85, 2.5, 0.4),
    "SLIDE_NUMBER": (MARGIN, 6.85, 0.8, 0.4),
}

LAYOUT_GEOMETRY = {
    TITLE_SLIDE: {0: (MARGIN, 2.6, 10.5, 1.6), 1: (MARGIN, 4.3, 10.5, 0.8)},
    TITLE_AND_CONTENT: {0: TITLE_BOX, 1: BODY_BOX},
    SECTION_HEADER: {0: (MARGIN, 2.9, 10.5, 1.3), 1: (MARGIN, 4.25, 10.5, 0.8)},
    TWO_CONTENT: {0: TITLE_BOX, 1: (MARGIN, 1.85, HALF_WIDTH, 4.7), 2: (MARGIN + HALF_WIDTH + 0.5, 1.85, HALF_WIDTH, 4.7)},
    4: {
        0: TITLE_BOX,
        1: (MARGIN, 1.85, HALF_WIDTH, 0.6),
        2: (MARGIN, 2.55, HALF_WIDTH, 4.0),
        3: (MARGIN + HALF_WIDTH + 0.5, 1.85, HALF_WIDTH, 0.6),
        4: (MARGIN + HALF_WIDTH + 0.5, 2.55, HALF_WIDTH, 4.0),
    },
    TITLE_ONLY: {0: TITLE_BOX},
    7: {0: (MARGIN, 0.5, 4.2, 1.6), 1: (MARGIN + 4.7, 0.5, CONTENT_WIDTH - 4.7, 6.05), 2: (MARGIN, 2.2, 4.2, 4.35)},
    PICTURE_WITH_CAPTION: {0: (7.6, 1.6, 4.8, 1.2), 1: (0, 0, 6.9, 7.5), 2: (7.6, 2.9, 4.8, 3.0)},
    9: {0: TITLE_BOX, 1: BODY_BOX},
    10: {0: (13.333 - MARGIN - 2.2, 0.5, 2.2, 6.05), 1: (MARGIN, 0.5, CONTENT_WIDTH - 2.6, 6.05)},
}


def place(shape, box):
    left, top, width, height = box
    shape.left, shape.top, shape.width, shape.height = Inches(left), Inches(top), Inches(width), Inches(height)


def placeholder_kind(placeholder):
    return str(placeholder.placeholder_format.type).split(".")[-1].split(" ")[0]


def lay_out_placeholders(presentation):
    master = presentation.slide_master
    for placeholder in master.placeholders:
        kind = placeholder_kind(placeholder)
        place(placeholder, FOOTER_BOXES.get(kind, TITLE_BOX if kind == "TITLE" else BODY_BOX))
    for layout_index, layout in enumerate(presentation.slide_layouts):
        geometry = LAYOUT_GEOMETRY.get(layout_index, {})
        for placeholder in layout.placeholders:
            kind = placeholder_kind(placeholder)
            if kind in FOOTER_BOXES:
                place(placeholder, FOOTER_BOXES[kind])
            elif placeholder.placeholder_format.idx in geometry:
                place(placeholder, geometry[placeholder.placeholder_format.idx])


def set_level_defaults(level_properties, size_pt=None, color=None, caps=None, font_reference=None, align=None, bullets=True):
    if align:
        level_properties.set("algn", align)
    defaults = level_properties.find(qn("a:defRPr"))
    if defaults is None:
        defaults = etree.SubElement(level_properties, qn("a:defRPr"))
    if not bullets:
        level_properties.set("marL", "0")
        level_properties.set("indent", "0")
        if level_properties.find(qn("a:buNone")) is None:
            defaults.addprevious(etree.Element(qn("a:buNone")))
    if size_pt:
        defaults.set("sz", str(int(size_pt * 100)))
    if caps is not None:
        defaults.set("cap", "all" if caps else "none")
    for existing in defaults.findall(qn("a:solidFill")):
        defaults.remove(existing)
    if color:
        fill = etree.Element(qn("a:solidFill"))
        etree.SubElement(fill, qn("a:srgbClr")).set("val", color)
        defaults.insert(0, fill)
    if font_reference:
        for existing in defaults.findall(qn("a:latin")):
            defaults.remove(existing)
        etree.SubElement(defaults, qn("a:latin")).set("typeface", font_reference)


def style_master_text(master):
    text_styles = master.element.find(qn("p:txStyles"))
    title_level = text_styles.find(qn("p:titleStyle")).find(qn("a:lvl1pPr"))
    set_level_defaults(title_level, size_pt=40, color=INK, caps=True, font_reference="+mj-lt", align="l")
    body_style = text_styles.find(qn("p:bodyStyle"))
    for level_number, size_pt in ((1, 24), (2, 20), (3, 18), (4, 18), (5, 18)):
        level = body_style.find(qn(f"a:lvl{level_number}pPr"))
        if level is not None:
            set_level_defaults(level, size_pt=size_pt, color=INK if level_number == 1 else SLATE, font_reference="+mn-lt")


def placeholder_level(placeholder):
    text_body = placeholder.element.find(qn("p:txBody"))
    list_style = text_body.find(qn("a:lstStyle"))
    if list_style is None:
        list_style = etree.Element(qn("a:lstStyle"))
        text_body.insert(1, list_style)
    level = list_style.find(qn("a:lvl1pPr"))
    if level is None:
        level = etree.SubElement(list_style, qn("a:lvl1pPr"))
    return level


def set_background(layout, color):
    common_slide_data = layout.element.find(qn("p:cSld"))
    existing = common_slide_data.find(qn("p:bg"))
    if existing is not None:
        common_slide_data.remove(existing)
    background = etree.Element(qn("p:bg"))
    properties = etree.SubElement(background, qn("p:bgPr"))
    fill = etree.SubElement(properties, qn("a:solidFill"))
    etree.SubElement(fill, qn("a:srgbClr")).set("val", color)
    etree.SubElement(properties, qn("a:effectLst"))
    common_slide_data.insert(0, background)


def move_picture_to(presentation, owner, image_path, left, top, height):
    scratch_slide = presentation.slides.add_slide(presentation.slide_layouts[BLANK])
    picture = scratch_slide.shapes.add_picture(str(image_path), left, top, height=height)
    blip = picture.element.find(".//" + qn("a:blip"))
    image_part = scratch_slide.part.related_part(blip.get(qn("r:embed")))
    blip.set(qn("r:embed"), owner.part.relate_to(image_part, RELATIONSHIP_TYPE.IMAGE))
    owner.shapes._spTree.append(deepcopy(picture.element))
    slide_ids = presentation.slides._sldIdLst
    last_slide = slide_ids[-1]
    presentation.part.drop_rel(last_slide.get(qn("r:id")))
    slide_ids.remove(last_slide)


def reset_layout_text_styles(layout):
    for placeholder in layout.placeholders:
        text_body = placeholder.element.find(qn("p:txBody"))
        if text_body is None:
            continue
        list_style = text_body.find(qn("a:lstStyle"))
        if list_style is not None:
            for child in list(list_style):
                list_style.remove(child)


def style_caption_layout(layout):
    for placeholder in layout.placeholders:
        kind = placeholder_kind(placeholder)
        if kind == "TITLE":
            set_level_defaults(placeholder_level(placeholder), size_pt=32)
        elif kind == "BODY":
            set_level_defaults(placeholder_level(placeholder), size_pt=18, color=SLATE, bullets=False)


def style_dark_layout(presentation, layout, logos):
    set_background(layout, DEEP_TEAL)
    layout.element.set("showMasterSp", "0")
    for placeholder in layout.placeholders:
        kind = placeholder_kind(placeholder)
        if kind in ("TITLE", "CENTER_TITLE"):
            set_level_defaults(placeholder_level(placeholder), size_pt=54, color=WHITE, align="l")
        elif kind in ("SUBTITLE", "BODY"):
            set_level_defaults(placeholder_level(placeholder), size_pt=22, color=BRIGHT_TEAL, align="l", bullets=False)
    move_picture_to(presentation, layout, logos / LOGO_FILES["white"], Inches(MARGIN), Inches(0.6), Inches(0.42))


def add_master_logo(presentation, logos):
    master = presentation.slide_master
    logo_height = Inches(0.3)
    move_picture_to(
        presentation,
        master,
        logos / LOGO_FILES["color"],
        SLIDE_WIDTH - Inches(2.6),
        SLIDE_HEIGHT - Inches(0.62),
        logo_height,
    )


def fill_text(shape, lines):
    frame = shape.text_frame
    frame.text = lines[0]
    for line in lines[1:]:
        frame.add_paragraph().text = line


def add_text_box(slide, text, left, top, width, height, size_pt, color, bold=False, font="+mn-lt"):
    box = slide.shapes.add_textbox(left, top, width, height)
    frame = box.text_frame
    frame.word_wrap = True
    run = frame.paragraphs[0].add_run()
    run.text = text
    run.font.size = Pt(size_pt)
    run.font.bold = bold
    run.font.color.rgb = RGBColor.from_string(color)
    run.font.name = font
    return box


def add_sample_slides(presentation):
    layouts = presentation.slide_layouts
    title_slide = presentation.slides.add_slide(layouts[TITLE_SLIDE])
    title_slide.shapes.title.text = "Presentation title"
    title_slide.placeholders[1].text = "Subtitle, presenter and date"

    agenda = presentation.slides.add_slide(layouts[TITLE_AND_CONTENT])
    agenda.shapes.title.text = "What we will cover"
    fill_text(agenda.placeholders[1], ["Start with the point", "One idea per slide", "End with what you need from the room"])

    section = presentation.slides.add_slide(layouts[SECTION_HEADER])
    section.shapes.title.text = "Section title"
    section.placeholders[1].text = "A short line about this section"

    comparison = presentation.slides.add_slide(layouts[TWO_CONTENT])
    comparison.shapes.title.text = "Two ideas side by side"
    fill_text(comparison.placeholders[1], ["Before", "What it was like"])
    fill_text(comparison.placeholders[2], ["After", "What changed"])

    number = presentation.slides.add_slide(layouts[TITLE_ONLY])
    number.shapes.title.text = "One number that matters"
    add_text_box(number, "00%", Inches(0.9), Inches(2.2), Inches(6), Inches(2), 120, DEEP_TEAL, font="+mj-lt")
    add_text_box(number, "Say what the number means and where it comes from.", Inches(0.9), Inches(4.6), Inches(7), Inches(1), 22, SLATE)

    quote = presentation.slides.add_slide(layouts[TITLE_ONLY])
    quote.shapes.title.text = "In their words"
    add_text_box(quote, "“Add a short quote from a founder, mentor or partner.”", Inches(0.9), Inches(2.3), Inches(10.5), Inches(2.2), 36, INK)
    add_text_box(quote, "Name, role and company", Inches(0.9), Inches(4.7), Inches(8), Inches(0.6), 18, SLATE)

    photo = presentation.slides.add_slide(layouts[PICTURE_WITH_CAPTION])
    photo.shapes.title.text = "Photo with a caption"
    for placeholder in photo.placeholders:
        if placeholder.placeholder_format.idx == 2:
            placeholder.text = "Describe what is happening and who is in the photo."

    closing = presentation.slides.add_slide(layouts[SECTION_HEADER])
    closing.shapes.title.text = "Thank you"
    closing.placeholders[1].text = "Your name, email and next step"


def build_powerpoint_template(output_directory: Path, logos: Path):
    presentation = Presentation()
    presentation.slide_width = SLIDE_WIDTH
    presentation.slide_height = SLIDE_HEIGHT
    master = presentation.slide_master
    lay_out_placeholders(presentation)
    style_master_text(master)
    for layout in presentation.slide_layouts:
        reset_layout_text_styles(layout)
    for layout_index in CAPTION_LAYOUTS:
        style_caption_layout(presentation.slide_layouts[layout_index])
    add_master_logo(presentation, logos)
    for layout_index in DARK_LAYOUTS:
        style_dark_layout(presentation, presentation.slide_layouts[layout_index], logos)
    add_sample_slides(presentation)
    presentation.core_properties.title = "Propellant presentation"
    presentation.core_properties.author = "MassChallenge"
    presentation.core_properties.last_modified_by = "MassChallenge"
    presentation.core_properties.created = BUILD_DATE
    presentation.core_properties.modified = BUILD_DATE
    presentation.core_properties.revision = 1
    buffer = BytesIO()
    presentation.save(buffer)
    branded = brand_package_themes(buffer.getvalue())
    (output_directory / "propellant-presentation.pptx").write_bytes(branded)
    (output_directory / "propellant-presentation.potx").write_bytes(as_template_package(branded))
    (output_directory / "Propellant.thmx").write_bytes(theme_file_package(BASE_THEME.read_text("utf-8")))

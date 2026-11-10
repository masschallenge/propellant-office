from io import BytesIO
from pathlib import Path

from docx import Document
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml import OxmlElement
from docx.oxml.ns import qn
from docx.shared import Inches, Pt, RGBColor

from .brand import BODY_FONT, BUILD_DATE, DEEP_TEAL, DOCUMENT_STYLES, INK, LINE, LOGO_FILES, MIST, PALE_TEAL, SLATE, TEAL, WHITE
from .theme import as_template_package, brand_package_themes


def set_font_family(run_properties_owner, family):
    run_properties = run_properties_owner.get_or_add_rPr()
    fonts = run_properties.find(qn("w:rFonts"))
    if fonts is None:
        fonts = OxmlElement("w:rFonts")
        run_properties.insert(0, fonts)
    for attribute in ("w:asciiTheme", "w:hAnsiTheme", "w:cstheme", "w:eastAsiaTheme"):
        fonts.attrib.pop(qn(attribute), None)
    for attribute in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        fonts.set(qn(attribute), family)
    for spacing in run_properties.findall(qn("w:spacing")):
        run_properties.remove(spacing)


def apply_text_style(document, text_style):
    style = document.styles[text_style.name]
    style.font.name = text_style.font
    set_font_family(style.element, text_style.font)
    style.font.size = Pt(text_style.size_pt)
    style.font.bold = text_style.bold
    style.font.italic = False
    style.font.all_caps = text_style.all_caps
    style.font.color.rgb = RGBColor.from_string(text_style.color)
    paragraph_format = style.paragraph_format
    paragraph_format.space_before = Pt(text_style.space_before_pt)
    paragraph_format.space_after = Pt(text_style.space_after_pt)
    paragraph_format.line_spacing = text_style.line_spacing
    paragraph_format.keep_with_next = text_style.name.startswith("Heading") or text_style.name == "Title"
    title_border = style.element.get_or_add_pPr().find(qn("w:pBdr"))
    if title_border is not None:
        style.element.get_or_add_pPr().remove(title_border)


def shade_cell(cell, fill):
    cell_properties = cell._tc.get_or_add_tcPr()
    shading = OxmlElement("w:shd")
    shading.set(qn("w:val"), "clear")
    shading.set(qn("w:color"), "auto")
    shading.set(qn("w:fill"), fill)
    cell_properties.append(shading)


def set_table_borders(table, color):
    table_properties = table._tbl.tblPr
    borders = OxmlElement("w:tblBorders")
    for edge in ("top", "bottom", "insideH"):
        border = OxmlElement(f"w:{edge}")
        border.set(qn("w:val"), "single")
        border.set(qn("w:sz"), "4")
        border.set(qn("w:color"), color)
        borders.append(border)
    for edge in ("left", "right", "insideV"):
        border = OxmlElement(f"w:{edge}")
        border.set(qn("w:val"), "nil")
        borders.append(border)
    table_properties.append(borders)


def add_page_number(paragraph):
    run = paragraph.add_run()
    for field_type, text in (("begin", None), (None, "PAGE"), ("end", None)):
        if field_type:
            character = OxmlElement("w:fldChar")
            character.set(qn("w:fldCharType"), field_type)
            run._r.append(character)
        else:
            instruction = OxmlElement("w:instrText")
            instruction.set(qn("xml:space"), "preserve")
            instruction.text = text
            run._r.append(instruction)


def style_small_run(run, color=SLATE):
    run.font.size = Pt(9)
    run.font.color.rgb = RGBColor.from_string(color)


def add_header_and_footer(document, logos):
    section = document.sections[0]
    header_paragraph = section.header.paragraphs[0]
    header_paragraph.add_run().add_picture(str(logos / LOGO_FILES["color"]), height=Inches(0.28))
    footer_paragraph = section.footer.paragraphs[0]
    footer_paragraph.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    style_small_run(footer_paragraph.add_run("MassChallenge  |  Page "))
    add_page_number(footer_paragraph)
    style_small_run(footer_paragraph.runs[-1])


def add_sample_table(document):
    rows = (
        ("Milestone", "Owner", "Due"),
        ("Applications open", "Programs team", "March 3"),
        ("Judging round one", "Judges", "April 14"),
        ("Cohort announced", "Communications", "May 5"),
    )
    table = document.add_table(rows=len(rows), cols=len(rows[0]))
    set_table_borders(table, LINE)
    for row_index, values in enumerate(rows):
        for column_index, value in enumerate(values):
            cell = table.cell(row_index, column_index)
            cell.text = ""
            run = cell.paragraphs[0].add_run(value)
            cell.paragraphs[0].paragraph_format.space_after = Pt(0)
            if row_index == 0:
                shade_cell(cell, DEEP_TEAL)
                run.font.bold = True
                run.font.color.rgb = RGBColor.from_string(WHITE)
            elif row_index % 2 == 0:
                shade_cell(cell, MIST)


def add_callout(document, text):
    paragraph = document.add_paragraph()
    paragraph_properties = paragraph._p.get_or_add_pPr()
    border = OxmlElement("w:pBdr")
    left = OxmlElement("w:left")
    left.set(qn("w:val"), "single")
    left.set(qn("w:sz"), "24")
    left.set(qn("w:space"), "8")
    left.set(qn("w:color"), TEAL)
    border.append(left)
    paragraph_properties.append(border)
    shading = OxmlElement("w:shd")
    shading.set(qn("w:val"), "clear")
    shading.set(qn("w:fill"), PALE_TEAL)
    paragraph_properties.append(shading)
    paragraph.add_run(text)


def write_sample_content(document):
    document.add_paragraph("Program report", style="Title")
    document.add_paragraph("Spring cohort, first quarter", style="Subtitle")
    status = document.add_paragraph()
    status_run = status.add_run("Status: Draft")
    status_run.italic = True
    status.add_run("\nAuthor: Your name")
    document.add_heading("Overview", level=1)
    document.add_paragraph(
        "Start with the point. Say in one or two short paragraphs what this document covers and "
        "what you need from the reader. Replace this text with your own."
    )
    document.add_heading("What happened", level=1)
    document.add_paragraph(
        "Use Heading 1 for sections and Heading 2 for the parts inside them. Keep paragraphs short, "
        "use everyday words and write as a person: we for MassChallenge, you for the reader."
    )
    document.add_heading("Key dates", level=2)
    add_sample_table(document)
    document.add_paragraph()
    document.add_heading("What we need from you", level=2)
    for item in (
        "Use real bullets from the Bullets button, not typed dashes.",
        "Keep each bullet to one idea.",
        "Use sentence case for headings, with a capital first letter only.",
    ):
        document.add_paragraph(item, style="List Bullet")
    add_callout(document, "Callouts like this one hold a single key takeaway. Use one per page at most.")


def build_word_template(output_directory: Path, logos: Path):
    document = Document()
    section = document.sections[0]
    section.page_width = Inches(8.5)
    section.page_height = Inches(11)
    for margin in ("top_margin", "bottom_margin", "left_margin", "right_margin"):
        setattr(section, margin, Inches(1))
    for text_style in DOCUMENT_STYLES:
        apply_text_style(document, text_style)
    for list_style_name in ("List Bullet", "List Number"):
        list_style = document.styles[list_style_name]
        list_style.font.name = BODY_FONT
        set_font_family(list_style.element, BODY_FONT)
        list_style.font.size = Pt(11)
        list_style.font.color.rgb = RGBColor.from_string(INK)
    style_names = {style.name for style in document.styles}
    hyperlink = document.styles["Hyperlink"] if "Hyperlink" in style_names else document.styles.add_style("Hyperlink", WD_STYLE_TYPE.CHARACTER)
    hyperlink.font.color.rgb = RGBColor.from_string(TEAL)
    hyperlink.font.underline = True
    document.core_properties.title = "Propellant document"
    document.core_properties.author = "MassChallenge"
    document.core_properties.last_modified_by = "MassChallenge"
    document.core_properties.created = BUILD_DATE
    document.core_properties.modified = BUILD_DATE
    document.core_properties.revision = 1
    document.core_properties.comments = "Propellant template for Word and Google Docs."
    add_header_and_footer(document, logos)
    write_sample_content(document)
    buffer = BytesIO()
    document.save(buffer)
    branded = brand_package_themes(buffer.getvalue())
    (output_directory / "propellant-document.docx").write_bytes(branded)
    (output_directory / "propellant-document.dotx").write_bytes(as_template_package(branded))

import re
import zipfile
from io import BytesIO

from .brand import BODY_FONT, BUILD_DATE, HEADLINE_FONT, THEME_COLORS, THEME_NAME

DRAWINGML = "http://schemas.openxmlformats.org/drawingml/2006/main"

COLOR_SLOTS = (
    "dk1",
    "lt1",
    "dk2",
    "lt2",
    "accent1",
    "accent2",
    "accent3",
    "accent4",
    "accent5",
    "accent6",
    "hlink",
    "folHlink",
)


def color_scheme_xml():
    slots = "".join(
        f'<a:{slot}><a:srgbClr val="{THEME_COLORS[slot]}"/></a:{slot}>' for slot in COLOR_SLOTS
    )
    return f'<a:clrScheme name="{THEME_NAME}">{slots}</a:clrScheme>'


def font_scheme_xml():
    major = f'<a:majorFont><a:latin typeface="{HEADLINE_FONT}"/><a:ea typeface=""/><a:cs typeface=""/></a:majorFont>'
    minor = f'<a:minorFont><a:latin typeface="{BODY_FONT}"/><a:ea typeface=""/><a:cs typeface=""/></a:minorFont>'
    return f'<a:fontScheme name="{THEME_NAME}">{major}{minor}</a:fontScheme>'


def brand_theme_xml(theme_xml):
    branded = re.sub(r"<a:clrScheme\b.*?</a:clrScheme>", color_scheme_xml(), theme_xml, flags=re.S)
    branded = re.sub(r"<a:fontScheme\b.*?</a:fontScheme>", font_scheme_xml(), branded, flags=re.S)
    return re.sub(r'(<a:theme\b[^>]*\bname=")[^"]*(")', rf"\g<1>{THEME_NAME}\g<2>", branded, count=1)


def rewrite_zip_entries(package_bytes, rewrite):
    source = zipfile.ZipFile(BytesIO(package_bytes))
    output = BytesIO()
    with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED) as target:
        for entry in source.infolist():
            data = source.read(entry.filename)
            replaced = rewrite(entry.filename, data)
            fixed = zipfile.ZipInfo(entry.filename, date_time=(2026, 1, 1, 0, 0, 0))
            fixed.compress_type = zipfile.ZIP_DEFLATED
            target.writestr(fixed, replaced if replaced is not None else data)
    return output.getvalue()


def brand_package_themes(package_bytes):
    def rewrite(filename, data):
        if re.search(r"(^|/)theme/theme\d*\.xml$", filename):
            return brand_theme_xml(data.decode("utf-8")).encode("utf-8")
        if filename == "docProps/core.xml":
            stamp = BUILD_DATE.strftime("%Y-%m-%dT%H:%M:%SZ")
            text = re.sub(r"(<dcterms:modified[^>]*>)[^<]*(</dcterms:modified>)", rf"\g<1>{stamp}\g<2>", data.decode("utf-8"))
            return text.encode("utf-8")
        return None

    return rewrite_zip_entries(package_bytes, rewrite)


TEMPLATE_CONTENT_TYPES = {
    "wordprocessingml.document.main+xml": "wordprocessingml.template.main+xml",
    "presentationml.presentation.main+xml": "presentationml.template.main+xml",
    "spreadsheetml.sheet.main+xml": "spreadsheetml.template.main+xml",
}


def as_template_package(package_bytes):
    def rewrite(filename, data):
        if filename != "[Content_Types].xml":
            return None
        text = data.decode("utf-8")
        for document_type, template_type in TEMPLATE_CONTENT_TYPES.items():
            text = text.replace(document_type, template_type)
        return text.encode("utf-8")

    return rewrite_zip_entries(package_bytes, rewrite)


def theme_file_package(theme_xml):
    content_types = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">'
        '<Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>'
        '<Default Extension="xml" ContentType="application/xml"/>'
        '<Override PartName="/theme/theme/theme1.xml" ContentType="application/vnd.openxmlformats-officedocument.theme+xml"/>'
        "</Types>"
    )
    root_relationships = (
        '<?xml version="1.0" encoding="UTF-8" standalone="yes"?>'
        '<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">'
        '<Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/theme" Target="theme/theme/theme1.xml"/>'
        "</Relationships>"
    )
    output = BytesIO()
    with zipfile.ZipFile(output, "w", zipfile.ZIP_DEFLATED) as package:
        for name, text in (
            ("[Content_Types].xml", content_types),
            ("_rels/.rels", root_relationships),
            ("theme/theme/theme1.xml", brand_theme_xml(theme_xml)),
        ):
            entry = zipfile.ZipInfo(name, date_time=(2026, 1, 1, 0, 0, 0))
            entry.compress_type = zipfile.ZIP_DEFLATED
            package.writestr(entry, text)
    return output.getvalue()

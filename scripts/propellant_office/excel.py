from io import BytesIO
from pathlib import Path

from openpyxl import Workbook
from openpyxl.chart import BarChart, Reference
from openpyxl.drawing.image import Image
from openpyxl.styles import Alignment, Font, PatternFill
from openpyxl.worksheet.table import Table, TableStyleInfo

from .brand import (
    BLACK,
    BODY_FONT,
    BUILD_DATE,
    HEADLINE_SEMIBOLD_FONT,
    NAVY,
    SLATE,
    WARM_WHITE,
    WHITE,
    logo_for_background,
)
from .theme import as_template_package, brand_package_themes

EXAMPLE_ROWS = (
    ("Program", "Applications", "Finalists", "Startups in cohort"),
    ("Example program A", 120, 30, 12),
    ("Example program B", 90, 24, 10),
    ("Example program C", 60, 18, 8),
)

GUIDANCE = (
    "Put the takeaway in the sheet title, for example Applications grew in every program.",
    "Keep one table per sheet, with the header in the first row and no blank rows or columns.",
    "Keep the Navy header row and Warm White stripes, or use Format as Table for filters.",
    "Right align numbers, use the same number of decimals in a column, and add units to headers.",
    "Charts take their colors from the theme. Start with a bar or line chart and label it directly.",
    "Do not use color alone to show status. Add a word such as On track or Late.",
)


def set_default_font(workbook):
    normal = next(style for style in workbook._named_styles if style.name == "Normal")
    normal.font = Font(name=BODY_FONT, size=11, color=BLACK)
    workbook._fonts[0] = Font(name=BODY_FONT, size=11, color=BLACK)


def add_title(sheet, text, cell="B2"):
    sheet[cell] = text
    sheet[cell].font = Font(name=HEADLINE_SEMIBOLD_FONT, size=24, color=BLACK)
    sheet.row_dimensions[sheet[cell].row].height = 36


def build_start_sheet(sheet, logos):
    sheet.title = "Start here"
    sheet.sheet_view.showGridLines = False
    sheet.page_setup.fitToWidth = 1
    sheet.page_setup.fitToHeight = 0
    sheet.sheet_properties.pageSetUpPr.fitToPage = True
    sheet.column_dimensions["A"].width = 3
    sheet.column_dimensions["B"].width = 90
    logo = Image(str(logos / logo_for_background(WHITE)))
    logo.width, logo.height = round(logo.width * 28 / logo.height), 28
    sheet.add_image(logo, "B1")
    sheet.row_dimensions[1].height = 34
    add_title(sheet, "WORKBOOK TITLE", "B3")
    sheet["B4"] = "Say in one sentence what this workbook answers and who it is for."
    sheet["B4"].font = Font(name=BODY_FONT, size=12, color=SLATE)
    sheet["B6"] = "How to use this template"
    sheet["B6"].font = Font(name=BODY_FONT, size=14, bold=True, color=BLACK)
    for offset, line in enumerate(GUIDANCE):
        cell = sheet.cell(row=7 + offset, column=2, value=f"•  {line}")
        cell.alignment = Alignment(wrap_text=True, vertical="top")


def build_data_sheet(workbook):
    sheet = workbook.create_sheet("Example data")
    sheet.sheet_view.showGridLines = False
    add_title(sheet, "PROGRAM RESULTS", "A1")
    sheet["A2"] = "Example only. Replace these rows with your own numbers."
    sheet["A2"].font = Font(name=BODY_FONT, size=11, italic=True, color=SLATE)
    first_row = 4
    for row_offset, values in enumerate(EXAMPLE_ROWS):
        for column_offset, value in enumerate(values):
            cell = sheet.cell(row=first_row + row_offset, column=1 + column_offset, value=value)
            if row_offset == 0:
                cell.font = Font(name=BODY_FONT, size=11, bold=True, color=WHITE)
                cell.fill = PatternFill("solid", fgColor=NAVY)
            elif row_offset % 2 == 0:
                cell.fill = PatternFill("solid", fgColor=WARM_WHITE)
            if column_offset:
                cell.alignment = Alignment(horizontal="right")
            if row_offset and column_offset:
                cell.number_format = "#,##0"
    last_row = first_row + len(EXAMPLE_ROWS) - 1
    table = Table(displayName="ProgramResults", ref=f"A{first_row}:D{last_row}")
    table.tableStyleInfo = TableStyleInfo(name="TableStyleLight1", showRowStripes=False)
    sheet.add_table(table)
    for column, width in zip("ABCD", (28, 16, 14, 20)):
        sheet.column_dimensions[column].width = width
    sheet.freeze_panes = f"A{first_row + 1}"
    sheet.page_setup.orientation = "landscape"
    sheet.page_setup.fitToWidth = 1
    sheet.page_setup.fitToHeight = 0
    sheet.sheet_properties.pageSetUpPr.fitToPage = True
    chart = BarChart()
    chart.type = "col"
    chart.title = "Applications by program"
    chart.y_axis.title = "Applications"
    chart.legend = None
    chart.add_data(Reference(sheet, min_col=2, min_row=first_row, max_row=last_row), titles_from_data=True)
    chart.set_categories(Reference(sheet, min_col=1, min_row=first_row + 1, max_row=last_row))
    chart.height = 8
    chart.width = 16
    sheet.add_chart(chart, f"F{first_row}")


def build_excel_template(output_directory: Path, logos: Path):
    workbook = Workbook()
    set_default_font(workbook)
    build_start_sheet(workbook.active, logos)
    build_data_sheet(workbook)
    workbook.properties.title = "Propellant workbook"
    workbook.properties.creator = "MassChallenge"
    workbook.properties.lastModifiedBy = "MassChallenge"
    workbook.properties.created = BUILD_DATE
    workbook.properties.modified = BUILD_DATE
    buffer = BytesIO()
    workbook.save(buffer)
    branded = brand_package_themes(buffer.getvalue())
    (output_directory / "propellant-workbook.xlsx").write_bytes(branded)
    (output_directory / "propellant-workbook.xltx").write_bytes(as_template_package(branded))

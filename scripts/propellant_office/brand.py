from datetime import datetime
from dataclasses import dataclass

DEEP_TEAL = "044451"
TEAL = "065E6F"
MID_TEAL = "068DA4"
BRIGHT_TEAL = "0FACBD"
PALE_TEAL = "D9F6FA"
MIST = "F3FBFC"
MAGENTA = "BF0261"
YELLOW = "FFC801"
INK = "1E282B"
SLATE = "4B575B"
WHITE = "FFFFFF"
GRAY_100 = "DBE1E3"
GRAY_300 = "848F92"


@dataclass(frozen=True)
class BrandColor:
    name: str
    hex_value: str
    print_cmyk: tuple


PALETTE = (
    BrandColor("Deep teal", DEEP_TEAL, (100, 64, 53, 50)),
    BrandColor("Teal", TEAL, (100, 55, 45, 24)),
    BrandColor("Mid teal", MID_TEAL, (87, 31, 31, 2)),
    BrandColor("Bright teal", BRIGHT_TEAL, (78, 11, 26, 0)),
    BrandColor("Pale teal", PALE_TEAL, (13, 0, 2, 0)),
    BrandColor("Mist", MIST, (3, 0, 1, 0)),
    BrandColor("Magenta", MAGENTA, (21, 100, 42, 5)),
    BrandColor("Yellow", YELLOW, (0, 22, 100, 0)),
    BrandColor("Ink", INK, (81, 66, 63, 83)),
    BrandColor("Slate", SLATE, (73, 57, 55, 35)),
    BrandColor("White", WHITE, (0, 0, 0, 0)),
)

SUPPORTING_NEUTRALS = (
    BrandColor("Gray 100", GRAY_100, (13, 7, 8, 0)),
    BrandColor("Gray 300", GRAY_300, (53, 38, 39, 4)),
)

CHART_ORDER = (TEAL, YELLOW, SLATE, BRIGHT_TEAL, DEEP_TEAL, GRAY_300)

THEME_NAME = "Propellant"

BUILD_DATE = datetime(2026, 1, 1)

THEME_COLORS = {
    "dk1": INK,
    "lt1": WHITE,
    "dk2": DEEP_TEAL,
    "lt2": MIST,
    **{
        f"accent{position}": color
        for position, color in enumerate(CHART_ORDER, start=1)
    },
    "hlink": TEAL,
    "folHlink": DEEP_TEAL,
}

HEADLINE_FONT = "Oswald"
BODY_FONT = "Lato"

CONTACT_EMAIL = "contact@masschallenge.org"
COPYRIGHT_LINE = f"© MassChallenge {BUILD_DATE.year}"
SHORT_BOILERPLATE = (
    "Born in Massachusetts and built for the world, MassChallenge backs the rare humans with the "
    "grit to solve the world's hardest challenges."
)


@dataclass(frozen=True)
class TextStyle:
    name: str
    font: str
    size_pt: float
    bold: bool
    color: str
    all_caps: bool = False
    space_before_pt: float = 0
    space_after_pt: float = 0
    line_spacing: float = 1.15


DOCUMENT_STYLES = (
    TextStyle("Title", HEADLINE_FONT, 32, False, DEEP_TEAL, all_caps=True, space_after_pt=6, line_spacing=1.0),
    TextStyle("Subtitle", BODY_FONT, 14, False, SLATE, space_after_pt=12),
    TextStyle("Heading 1", BODY_FONT, 20, True, INK, space_before_pt=24, space_after_pt=8, line_spacing=1.15),
    TextStyle("Heading 2", BODY_FONT, 15, True, INK, space_before_pt=18, space_after_pt=6, line_spacing=1.2),
    TextStyle("Heading 3", BODY_FONT, 12.5, True, INK, space_before_pt=12, space_after_pt=4, line_spacing=1.25),
    TextStyle("Normal", BODY_FONT, 11, False, INK, space_after_pt=8, line_spacing=1.4),
)

LOGO_FILES = {
    "color": "masschallenge-logo-horizontal-color.png",
    "white": "masschallenge-logo-horizontal-white.png",
    "monogram_color": "masschallenge-logo-monogram-color.png",
    "monogram_white": "masschallenge-logo-monogram-white.png",
}

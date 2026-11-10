from datetime import datetime
from dataclasses import dataclass

INK = "1E282B"
SLATE = "4B575B"
WHITE = "FFFFFF"
MIST = "F3F6F7"
LINE = "DBE1E3"
TEAL = "065E6F"
DEEP_TEAL = "044451"
BRIGHT_TEAL = "0FACBD"
PALE_TEAL = "D9F6FA"
YELLOW = "FFC801"
GRAY = "848F92"

THEME_NAME = "Propellant"

BUILD_DATE = datetime(2026, 1, 1)

THEME_COLORS = {
    "dk1": INK,
    "lt1": WHITE,
    "dk2": DEEP_TEAL,
    "lt2": MIST,
    "accent1": TEAL,
    "accent2": YELLOW,
    "accent3": SLATE,
    "accent4": BRIGHT_TEAL,
    "accent5": DEEP_TEAL,
    "accent6": GRAY,
    "hlink": TEAL,
    "folHlink": DEEP_TEAL,
}

HEADLINE_FONT = "Oswald"
BODY_FONT = "Lato"


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

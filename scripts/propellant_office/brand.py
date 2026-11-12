from datetime import datetime
from dataclasses import dataclass

MC_BLUE = "0EABBC"
MC_GRAY = "808285"
NAVY = "10263F"
BLACK = "222222"
WARM_WHITE = "F8F8F5"
DEEP_TEAL = "004F73"
TEAL = "00708E"
CYAN = "54EEFF"
OCEAN = "037AA6"
YELLOW = "FFC801"
ORANGE = "FF6B35"
RASPBERRY = "D14170"
LIME = "C6F135"
WHITE = "FFFFFF"
LIGHT_TINT = "F3FAFC"
NAVY_BLACK = "051925"
SLATE = "4B575B"
GRAY_100 = "DBE1E3"
GRAY_300 = "848F92"


@dataclass(frozen=True)
class BrandColor:
    name: str
    hex_value: str
    approximate_cmyk: tuple
    print_substitute: str = ""


CORE_COLORS = (
    BrandColor("MC Blue", MC_BLUE, (93, 9, 0, 26)),
    BrandColor("MC Gray", MC_GRAY, (4, 2, 0, 48)),
    BrandColor("Navy", NAVY, (75, 40, 0, 75)),
    BrandColor("Black", BLACK, (0, 0, 0, 87)),
    BrandColor("Warm White", WARM_WHITE, (0, 0, 1, 3)),
)

SUPPORTING_BLUES = (
    BrandColor("Deep Teal", DEEP_TEAL, (100, 31, 0, 55)),
    BrandColor("Teal", TEAL, (100, 21, 0, 44)),
    BrandColor("Cyan", CYAN, (100, 11, 0, 9), "00CFE8"),
    BrandColor("Ocean", OCEAN, ()),
)

WARM_ACCENTS = (
    BrandColor("Yellow", YELLOW, (0, 22, 100, 0)),
    BrandColor("Orange", ORANGE, (0, 47, 73, 4), "F58242"),
    BrandColor("Raspberry", RASPBERRY, (0, 73, 41, 15), "D83B80"),
    BrandColor("Lime", LIME, (32, 0, 74, 17), "91D438"),
)

PALETTE = CORE_COLORS + SUPPORTING_BLUES + WARM_ACCENTS

SUPPORTING_NEUTRALS = (
    BrandColor("White", WHITE, (0, 0, 0, 0)),
    BrandColor("Light tint", LIGHT_TINT, ()),
    BrandColor("Slate", SLATE, (73, 57, 55, 35)),
    BrandColor("Gray 100", GRAY_100, (13, 7, 8, 0)),
    BrandColor("Gray 300", GRAY_300, (53, 38, 39, 4)),
)

CHART_ORDER = (TEAL, YELLOW, NAVY, MC_BLUE, DEEP_TEAL, GRAY_300)

DARK_SECTION_COLORS = (NAVY, BLACK, DEEP_TEAL)
LIGHT_SECTION_COLORS = (WHITE, WARM_WHITE)

THEME_NAME = "Propellant"

BUILD_DATE = datetime(2026, 1, 1)

THEME_COLORS = {
    "dk1": BLACK,
    "lt1": WHITE,
    "dk2": NAVY,
    "lt2": WARM_WHITE,
    **{
        f"accent{position}": color
        for position, color in enumerate(CHART_ORDER, start=1)
    },
    "hlink": TEAL,
    "folHlink": DEEP_TEAL,
}

HEADLINE_FONT = "Oswald"
HEADLINE_SEMIBOLD_FONT = "Oswald SemiBold"
BODY_FONT = "Lato"
FALLBACK_HEADLINE_FONT = "Aptos Narrow"
FALLBACK_BODY_FONT = "Aptos"
RETIRED_FONTS = ("Arial", "Gotham", "Bebas", "Montserrat", "Open Sans")

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


DISPLAY_LINE_SPACING = 1.0
BODY_LINE_SPACING = 1.5

DOCUMENT_STYLES = (
    TextStyle("Title", HEADLINE_SEMIBOLD_FONT, 32, False, BLACK, all_caps=True, space_after_pt=6, line_spacing=DISPLAY_LINE_SPACING),
    TextStyle("Subtitle", BODY_FONT, 14, False, SLATE, space_after_pt=12, line_spacing=BODY_LINE_SPACING),
    TextStyle("Heading 1", HEADLINE_SEMIBOLD_FONT, 18, False, TEAL, all_caps=True, space_before_pt=24, space_after_pt=8, line_spacing=DISPLAY_LINE_SPACING),
    TextStyle("Heading 2", HEADLINE_SEMIBOLD_FONT, 14, False, BLACK, all_caps=True, space_before_pt=18, space_after_pt=6, line_spacing=DISPLAY_LINE_SPACING),
    TextStyle("Heading 3", BODY_FONT, 12, True, BLACK, space_before_pt=12, space_after_pt=4, line_spacing=1.25),
    TextStyle("Normal", BODY_FONT, 11, False, BLACK, space_after_pt=8, line_spacing=BODY_LINE_SPACING),
)

LOGO_FILES = {
    "color": "masschallenge-logo-horizontal-color.png",
    "white": "masschallenge-logo-horizontal-white.png",
    "black": "masschallenge-logo-horizontal-black.png",
    "monogram_color": "masschallenge-logo-monogram-color.png",
    "monogram_white": "masschallenge-logo-monogram-white.png",
    "monogram_black": "masschallenge-logo-monogram-black.png",
}

FULL_COLOR_LOGO_BACKGROUNDS = (WHITE, WARM_WHITE)
WHITE_LOGO_BACKGROUNDS = (NAVY, BLACK, DEEP_TEAL, TEAL, MC_BLUE)

HORIZONTAL_LOGO_PIXELS = (1671, 225)
WORDMARK_M_HEIGHT_PIXELS = 91

MINIMUM_PRINT_WIDTH_MM = {"vertical": 20, "horizontal": 30, "monogram": 8}
MINIMUM_SCREEN_WIDTH_PIXELS = {"vertical": 60, "horizontal": 160}
MINIMUM_MONOGRAM_SCREEN_HEIGHT_PIXELS = 16


def logo_for_background(background, mark="horizontal"):
    background = background.upper()
    if background in FULL_COLOR_LOGO_BACKGROUNDS:
        treatment = "color"
    elif background in WHITE_LOGO_BACKGROUNDS:
        treatment = "white"
    else:
        raise ValueError(f"No approved logo treatment for a #{background} background")
    return LOGO_FILES[treatment if mark == "horizontal" else f"{mark}_{treatment}"]


def logo_width_for_height(logo_height):
    logo_width_pixels, logo_height_pixels = HORIZONTAL_LOGO_PIXELS
    return logo_height * logo_width_pixels / logo_height_pixels


def logo_clear_space(logo_height):
    return logo_height * WORDMARK_M_HEIGHT_PIXELS / HORIZONTAL_LOGO_PIXELS[1]

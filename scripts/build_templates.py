import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from propellant_office.excel import build_excel_template
from propellant_office.powerpoint import build_powerpoint_template
from propellant_office.word import build_word_template

ROOT = Path(__file__).resolve().parent.parent
LOGOS = ROOT / "assets" / "logos"


def main():
    builders = (
        ("word", build_word_template),
        ("powerpoint", build_powerpoint_template),
        ("excel", build_excel_template),
    )
    for folder, build in builders:
        output = ROOT / "templates" / folder
        output.mkdir(parents=True, exist_ok=True)
        build(output, LOGOS)
        print(f"Built {folder} templates in {output.relative_to(ROOT)}")


if __name__ == "__main__":
    main()

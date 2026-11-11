import shutil
import subprocess
import tempfile
from pathlib import Path

PREVIEW_SOURCES = (
    Path("word") / "propellant-document.docx",
    Path("powerpoint") / "propellant-presentation.pptx",
    Path("excel") / "propellant-workbook.xlsx",
)

PREVIEW_FOLDER = "previews"


def preview_name(source):
    return f"{Path(source).stem}.png"


def office_command():
    return shutil.which("soffice") or shutil.which("libreoffice")


def conversion_arguments(command, source, output_folder, profile_folder):
    return [
        command,
        f"-env:UserInstallation={Path(profile_folder).resolve().as_uri()}",
        "--headless",
        "--norestore",
        "--convert-to",
        "png",
        "--outdir",
        str(output_folder),
        str(source),
    ]


def render_preview(command, source, output):
    with tempfile.TemporaryDirectory() as working_folder:
        working = Path(working_folder)
        subprocess.run(
            conversion_arguments(command, source, working / "out", working / "profile"),
            check=True,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
        rendered = working / "out" / preview_name(source)
        if not rendered.exists():
            raise RuntimeError(f"LibreOffice did not render {source}")
        output.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(rendered, output)


def render_previews(templates_root, command=None):
    command = command or office_command()
    if command is None:
        return []
    output_folder = Path(templates_root) / PREVIEW_FOLDER
    rendered = []
    for source in PREVIEW_SOURCES:
        output = output_folder / preview_name(source)
        render_preview(command, Path(templates_root) / source, output)
        rendered.append(output)
    return rendered

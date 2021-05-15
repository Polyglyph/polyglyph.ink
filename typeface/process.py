from pathlib import Path
from svgpathtools import svg2paths2, wsvg
from xml.etree import ElementTree as ET
from bs4 import BeautifulSoup as BS
from bs4 import Comment
import shutil
import os

DESCRIPTION = "Part of the Polyglyph project. Visit us at polyglyph.ink"

def strip_comments(soup: BS) -> BS:
    comments = soup.find_all(string=lambda text: isinstance(text, Comment))

    for comment in comments:
        c = comment.extract()
        del c

    return soup

def find_image_object(tag) -> bool:
    return tag.name == "g" and tag["id"] == "Image"

def find_pen_object(tag) -> bool:
    return tag.name == "g" and tag["id"] == "Pen"


def read_svg(p: Path) -> BS:
    with open (p) as f:
        soup = BS(f.read(), "xml")

    return soup


def write_svg(soup: BS, p: Path) -> None:
    p.parent.mkdir(parents=True, exist_ok=True)

    with open(p, "w") as f:
        f.write(soup.prettify())


def process_soup(soup: BS, unicode: str) -> None:
    """
    Processes a soup object in place.
    """
    # Remove comments
    strip_comments(soup)

    # Retitle
    soup.title.string = unicode

    # Redescribe
    soup.desc.string = DESCRIPTION

    # Delete defs
    soup.defs.decompose()

    # Delete image
    images = soup.find_all(find_image_object)
    for image in images:
        image.decompose()

    # Rename Pen
    pen = soup.find(find_pen_object)
    pen["id"] = "Glyph"


if __name__ == "__main__":
    svgs = Path("svgs")

    output = Path("output")
    output_flat = Path("output_flat")

    shutil.rmtree(output, ignore_errors=True)
    shutil.rmtree(output_flat, ignore_errors=True)

    print("Processing raw glyphs...")

    for root, dir, files in os.walk(svgs):
        for file in files:
            fp = Path(root, file)

            unicode = fp.stem
            soup = read_svg(fp)

            process_soup(soup, unicode=unicode)

            # Flat
            write_svg(soup, output_flat / fp.name)
            write_svg(soup, Path(output, *fp.parts[1:]))

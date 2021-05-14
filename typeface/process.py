from pathlib import Path
from svgpathtools import svg2paths2, wsvg
from xml.etree import ElementTree as ET
from bs4 import BeautifulSoup as BS
from bs4 import Comment
import shutil

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

def process_file(name: str) -> None:
    fn = svgs / (name + ".svg")

    with open(fn) as f:
        soup = BS(f.read(), "xml")

    # Remove comments
    strip_comments(soup)

    # Retitle
    soup.title.string = name

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

    # Output
    with open(output / (name + ".svg"), "w") as f:
        f.write(soup.prettify())


if __name__ == "__main__":
    svgs = Path("svgs")

    output = Path("output")
    shutil.rmtree(output, ignore_errors=True)
    output.mkdir()

    for input_ in svgs.glob("*.svg"):
        name = input_.stem

        print(f"Processing {input_}...")
        process_file(name)
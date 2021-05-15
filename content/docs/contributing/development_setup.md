---
title: "Development Setup"
description: "Regularly update the installed npm packages to keep your Doks website stable, usable, and secure."
lead: "Regularly update the installed npm packages to keep your Doks website stable, usable, and secure."
date: 2021-05-15T22:15:35Z
lastmod: 2021-05-15T22:15:35Z
draft: false
images: []
menu:
  docs:
    parent: "contributing"
weight: 810
toc: true
---

## Concepts

I make the SVG files using [Concepts](https://concepts.app/en/) and the PNG template found [here](https://github.com/Polyglyph/polyglyph.ink/tree/master/typeface).

The SVG XML tree is manipulated afterwards in Python to:

1. Remove Concepts comments
2. Rename titles
3. Remove the PNG template image

### Gotchas

Concepts implements the eraser as a layer of the background color placed on top of the strokes you want to erase.

{{< alert icon="💡" text="To prevent these from being in the SVG, only use the `Undo` key to erase." >}}

## SVG files

The raw SVG files from concept are stored [here](https://github.com/Polyglyph/polyglyph.ink/tree/master/typeface).

The processed SVG files are not stored in Git, but are just generated when needed.

You can get the latest glyphs [here](/polyglyph.zip).

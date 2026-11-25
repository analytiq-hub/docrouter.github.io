#!/usr/bin/env python3
"""Build the DocRouter.AI pen wrap: "docrouter docrouter ..." all over, on navy.

    python3 _brand/pen/build-pen.py

VistaPrint Design Wrap Ballpoint Pen spec: bleed 2.77 x 1.40 in (document
size), trim 2.64 x 1.36 in, safety 2.54 x 1.25 in. The 1.40 in height wraps
around the barrel, so the pattern runs edge to edge and reads the same from
every side. No logo: the repeated name is the branding.

Outputs (next to this script):
    docrouter-pen-print.pdf   CMYK vectors, full document size with bleed
    docrouter-pen.png         600 dpi RGB image of the full document
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

from pypdf import PdfReader, PdfWriter
from pypdf.generic import RectangleObject
from reportlab.lib.colors import CMYKColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfgen import canvas

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]

# Reuse the business card's brand colours and fonts.
_spec = importlib.util.spec_from_file_location(
    "business_card", ROOT / "_brand" / "business-card" / "build-business-card.py")
card = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(card)

IN = 72.0
PAGE_W, PAGE_H = 2.77 * IN, 1.40 * IN
TRIM_W, TRIM_H = 2.64 * IN, 1.36 * IN
BLEED_X, BLEED_Y = (PAGE_W - TRIM_W) / 2, (PAGE_H - TRIM_H) / 2

WORD = "docrouter"
FONT, SIZE = "Inter-Bold", 9.0
LEADING = 11.0             # row spacing
GAP = 4.5                  # space between words
ROW_SHIFT = 27.0           # each row starts offset, so the words stagger
BACKGROUND = card.NAVY
COLOURS = [                # cycled word by word
    card.WHITE,
    CMYKColor(0.55, 0.15, 0.00, 0.00),   # light brand blue
    CMYKColor(0.00, 0.46, 0.74, 0.00),   # logo-mark orange #FF8A42
]

PDF = HERE / "docrouter-pen-print.pdf"
PNG = HERE / "docrouter-pen.png"


def draw(c: canvas.Canvas) -> None:
    c.setFillColor(BACKGROUND)
    c.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)

    c.saveState()
    clip = c.beginPath()
    clip.rect(0, 0, PAGE_W, PAGE_H)
    c.clipPath(clip, stroke=0, fill=0)
    c.setFont(FONT, SIZE)
    word_w = pdfmetrics.stringWidth(WORD, FONT, SIZE) + GAP
    row, k = 0, 0
    yv = PAGE_H - SIZE * 0.9
    while yv > -SIZE:
        xv = -((row * ROW_SHIFT) % word_w) - word_w
        while xv < PAGE_W:
            c.setFillColor(COLOURS[k % len(COLOURS)])
            c.drawString(xv, yv, WORD)
            xv += word_w
            k += 1
        k += 1                   # so colours don't line up vertically
        yv -= LEADING
        row += 1
    c.restoreState()


def build() -> None:
    card.register_fonts()
    tmp = HERE / ".docrouter-pen.pdf"
    c = canvas.Canvas(str(tmp), pagesize=(PAGE_W, PAGE_H), pageCompression=1)
    c.setTitle("DocRouter.AI pen wrap")
    draw(c)
    c.showPage()
    c.save()

    reader = PdfReader(str(tmp))
    page = reader.pages[0]
    page.mediabox = RectangleObject([0, 0, PAGE_W, PAGE_H])
    page.bleedbox = RectangleObject([0, 0, PAGE_W, PAGE_H])
    page.trimbox = RectangleObject([BLEED_X, BLEED_Y, PAGE_W - BLEED_X, PAGE_H - BLEED_Y])
    writer = PdfWriter()
    writer.add_page(page)
    writer.add_metadata({
        "/Title": "DocRouter.AI pen wrap",
        "/Subject": "2.77 x 1.40 in with bleed, 2.64 x 1.36 in trim, CMYK",
        "/Author": "DocRouter.AI",
    })
    with PDF.open("wb") as fh:
        writer.write(fh)
    tmp.unlink()

    import pymupdf  # proof image only
    pymupdf.open(PDF)[0].get_pixmap(dpi=600, alpha=False).save(PNG)
    print(PDF)
    print(PNG)


if __name__ == "__main__":
    build()

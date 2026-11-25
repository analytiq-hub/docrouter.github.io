#!/usr/bin/env python3
"""Build the DocRouter.AI pen wrap: navy background, white wordmark, orange mark.

    python3 _brand/pen/build-pen.py

Matches the printer template: 2.77 x 1.4 in document including bleed. The
1.4 in height wraps around the barrel, so the logo sits in the centre band
and the rest is flat navy (the wrap seam disappears into the solid colour).

Outputs (next to this script):
    docrouter-pen-print.pdf   CMYK vectors, full document size with bleed
    docrouter-pen.png         600 dpi RGB image of the full document
"""

from __future__ import annotations

import importlib.util
from pathlib import Path

from pypdf import PdfReader, PdfWriter
from pypdf.generic import RectangleObject
from reportlab.pdfgen import canvas

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]

# Reuse the business card's brand colours and vector logo drawing.
_spec = importlib.util.spec_from_file_location(
    "business_card", ROOT / "_brand" / "business-card" / "build-business-card.py")
card = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(card)

IN = 72.0
PAGE_W, PAGE_H = 2.77 * IN, 1.4 * IN   # template document size, bleed included
BLEED = 0.055 * IN                      # same printer as the business card
SAFE = 0.11 * IN                        # safety inset from the document edge
LOGO_W = 1.75 * IN                      # wordmark + mark width (don't go below ~1.6 in: thin mark strokes)

PDF = HERE / "docrouter-pen-print.pdf"
PNG = HERE / "docrouter-pen.png"


def build() -> None:
    tmp = HERE / ".docrouter-pen.pdf"
    c = canvas.Canvas(str(tmp), pagesize=(PAGE_W, PAGE_H), pageCompression=1)
    c.setTitle("DocRouter.AI pen wrap")

    c.setFillColor(card.NAVY)
    c.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)

    card.WORDMARK = card.WHITE          # white wordmark on navy; mark keeps its gradient
    logo_h = LOGO_W * 1000.0 / 5701.62  # logo SVG aspect ratio
    assert LOGO_W <= PAGE_W - 2 * SAFE and logo_h <= PAGE_H - 2 * SAFE
    card.draw_logo(c, (PAGE_W - LOGO_W) / 2, PAGE_H / 2 + logo_h / 2, LOGO_W)

    c.showPage()
    c.save()

    reader = PdfReader(str(tmp))
    page = reader.pages[0]
    page.mediabox = RectangleObject([0, 0, PAGE_W, PAGE_H])
    page.bleedbox = RectangleObject([0, 0, PAGE_W, PAGE_H])
    page.trimbox = RectangleObject([BLEED, BLEED, PAGE_W - BLEED, PAGE_H - BLEED])
    writer = PdfWriter()
    writer.add_page(page)
    writer.add_metadata({
        "/Title": "DocRouter.AI pen wrap",
        "/Subject": "2.77 x 1.4 in with bleed, CMYK",
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

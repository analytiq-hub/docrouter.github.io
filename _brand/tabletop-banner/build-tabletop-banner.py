#!/usr/bin/env python3
"""Build the DocRouter.AI tabletop retractable banner.

    python3 _brand/tabletop-banner/build-tabletop-banner.py

Same design as the 33 x 79 in pull-up banner
(_brand/datos-insights/build-retractable-banner.py), scaled uniformly to the
tabletop spec, with three differences: the logo mark keeps its orange gradient,
the QR code is larger (tabletop viewers stand close), and the background is
the website hero / business card front (pale blue gradient, faint dot grid,
large faint rings in the top-right corner) instead of plain white.

    Bleed   8.74 x 14.21 in   (document size)
    Trim    8.50 x 13.98 in
    Safety  8.00 x 11.76 in   0.36 in from the top edge, ~2.09 in from the
                              bottom edge (the stand hides the bottom)

Outputs (next to this script):
    docrouter-tabletop-banner-cmyk.tif     upload file: 300 dpi, Generic CMYK, LZW
    docrouter-tabletop-banner-print.pdf    CMYK vectors with trim/bleed boxes
    docrouter-tabletop-banner-proof.png    RGB proof for review
"""

from __future__ import annotations

import importlib.util
import re
from pathlib import Path

import pymupdf
from PIL import Image, ImageCms
from pypdf import PdfReader, PdfWriter
from pypdf.generic import RectangleObject
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.colors import CMYKColor
from reportlab.pdfgen import canvas

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
BRAND = ROOT / "_brand" / "datos-insights"

# Reuse the pull-up banner's colours, icons, connectors, text and QR drawing.
_spec = importlib.util.spec_from_file_location("banner", BRAND / "build-retractable-banner.py")
banner = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(banner)

# The business card's gradient-mark drawing (full-colour logo mark).
_spec = importlib.util.spec_from_file_location(
    "card", ROOT / "_brand" / "business-card" / "build-business-card.py")
card = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(card)

IN = 72.0
PAGE_W, PAGE_H = 8.74 * IN, 14.21 * IN
TRIM_W, TRIM_H = 8.50 * IN, 13.98 * IN
BLEED_X, BLEED_Y = (PAGE_W - TRIM_W) / 2, (PAGE_H - TRIM_H) / 2
SAFE_W, SAFE_H = 8.00 * IN, 11.76 * IN
SAFE_TOP = 0.36 * IN                       # from the top of the document
SAFE_LEFT = (PAGE_W - SAFE_W) / 2

# The pull-up banner is laid out on a 435-unit-wide grid. Scale it so the
# grid spans the tabletop trim width, then centre its content (grid rows
# 42 .. 591) vertically inside the safety area.
S = TRIM_W / banner.SOURCE_W
CONTENT_TOP, CONTENT_BOTTOM = 42, 591
TOP = SAFE_TOP + (SAFE_H - (CONTENT_BOTTOM - CONTENT_TOP) * S) / 2
DPI = 300

PDF = HERE / "docrouter-tabletop-banner-print.pdf"
TIFF = HERE / "docrouter-tabletop-banner-cmyk.tif"
PROOF = HERE / "docrouter-tabletop-banner-proof.png"


def x(v: float) -> float:
    return PAGE_W / 2 + (v - banner.SOURCE_W / 2) * S


def y(v: float) -> float:
    """Top-down grid row to PDF coordinates."""
    return PAGE_H - (TOP + (v - CONTENT_TOP) * S)


# Point the banner helpers at this geometry.
banner.x, banner.y = x, y
banner.SX = banner.SY = banner.U = S
banner.PAGE_W, banner.PAGE_H = PAGE_W, PAGE_H


def check_safe(left: float, top: float, right: float, bottom: float) -> None:
    """Fail the build if a content box (grid units) leaves the safety area."""
    sl, sr = SAFE_LEFT, SAFE_LEFT + SAFE_W
    st, sb = PAGE_H - SAFE_TOP, PAGE_H - SAFE_TOP - SAFE_H
    assert sl <= x(left) and x(right) <= sr and sb <= y(bottom) and y(top) <= st, (
        f"content box {left, top, right, bottom} is outside the safety area")


ACCENT_LIGHT = CMYKColor(0.03, 0.015, 0.00, 0.00)   # half-strength --dr-bg-accent


def hero_background(c: canvas.Canvas) -> None:
    """Website hero / business card front background: pale blue gradient,
    faint dot grid fading downwards, and large faint rings in the top-right."""
    c.saveState()
    p = c.beginPath()
    p.rect(0, 0, PAGE_W, PAGE_H)
    c.clipPath(p, stroke=0, fill=0)
    # --dr-bg-accent at the top, easing to a lighter tint (never plain white).
    c.linearGradient(0, PAGE_H, 0, y(CONTENT_BOTTOM + 40), (card.ACCENT, ACCENT_LIGHT), extend=True)
    c.restoreState()

    step = 14.0
    fade_end = y(330)
    c.setFillColor(card.DOT)
    yv = PAGE_H - step / 2
    while yv > fade_end:
        r = 0.5 + 0.45 * (yv - fade_end) / (PAGE_H - fade_end)
        xv = step / 2
        while xv < PAGE_W:
            c.circle(xv, yv, r, stroke=0, fill=1)
            xv += step
        yv -= step

    # Same proportions as the card front: two concentric rings off the corner.
    c.setStrokeColor(card.RING)
    c.setLineWidth(1.5)
    cx, cy = PAGE_W - BLEED_X + 0.25 * IN, PAGE_H - BLEED_Y + 0.40 * IN
    c.circle(cx, cy, 3.30 * IN, stroke=1, fill=0)
    c.circle(cx, cy, 2.13 * IN, stroke=1, fill=0)


def build_pdf() -> None:
    pdfmetrics.registerFont(TTFont(
        "IBM-Plex-Sans-SemiBold", str(ROOT / "_brand/fonts/IBM-Plex-Sans-SemiBold.ttf")))
    blue, navy, white, pale = banner.BLUE, banner.NAVY, banner.WHITE, banner.PALE

    tmp_pdf = HERE / ".docrouter-tabletop-banner.pdf"
    c = canvas.Canvas(str(tmp_pdf), pagesize=(PAGE_W, PAGE_H), pageCompression=1)
    c.setTitle("DocRouter.AI tabletop banner")
    hero_background(c)

    # Logo mark in its full-colour orange gradient (the pull-up banner uses blue).
    svg = (BRAND / "docrouter-mark-color.svg").read_text()
    vb_w, vb_h = (float(v) for v in re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"', svg).groups())
    mark_w = 84 * S
    mark_h = mark_w * vb_h / vb_w
    card.draw_mark(c, svg, PAGE_W / 2 - mark_w / 2, y(42), mark_w / vb_w)
    check_safe(217.5 - 42, 42, 217.5 + 42, 42 + mark_h / S)

    banner.centered_text(c, "DocRouter.AI", 144, "IBM-Plex-Sans-SemiBold", 38, blue)
    banner.centered_text(c, "AI-powered document workflows", 204, "IBM-Plex-Sans-SemiBold", 20.5, navy)
    for text, size in (("DocRouter.AI", 38), ("AI-powered document workflows", 20.5)):
        half = pdfmetrics.stringWidth(text, "IBM-Plex-Sans-SemiBold", size) / 2
        check_safe(217.5 - half, 144, 217.5 + half, 144 + size)

    c.setStrokeColor(blue)
    c.setLineWidth(3.5 * S)
    c.setLineCap(1)
    c.line(x(165), y(243), x(271), y(243))

    banner.centered_text(c, "Scan for a live demo", 288, "IBM-Plex-Sans-SemiBold", 27, blue)

    # QR enlarged vs. the pull-up banner (84 -> 116 units) since tabletop
    # viewers are close; it fills the gap above the workflow strip.
    enc = 116 * S
    enc_x, enc_y = PAGE_W / 2 - enc / 2, y(336) - enc
    c.setFillColor(white)
    c.setStrokeColor(pale)
    c.setLineWidth(0.8 * S)
    c.roundRect(enc_x, enc_y, enc, enc, 14 * S, stroke=1, fill=1)
    qr = 100 * S
    banner.draw_qr(c, banner.qr_matrix(), PAGE_W / 2 - qr / 2, enc_y + (enc - qr) / 2, qr)

    stages = [
        (37, 61, 521, "Index", banner.icon_document),
        (142, 166, 515, "Structure", banner.icon_structure),
        (246, 270, 521, "Extract", banner.icon_extract),
        (349, 373, 515, "Integrate", banner.icon_integrate),
    ]
    banner.connector(c, 93, 545, 134, 539)
    banner.connector(c, 198, 539, 238, 545)
    banner.connector(c, 302, 545, 341, 539)
    for left, center, top, title, icon in stages:
        banner.rounded_box(c, left, top)
        icon(c, left, top)
        banner.workflow_text(c, center, top + 54, title)
        half = pdfmetrics.stringWidth(title, "IBM-Plex-Sans-SemiBold", 16) / 2
        check_safe(min(left, center - half), top, max(left + 48, center + half), top + 54 + 20)

    c.showPage()
    c.save()

    reader = PdfReader(str(tmp_pdf))
    page = reader.pages[0]
    page.mediabox = RectangleObject([0, 0, PAGE_W, PAGE_H])
    page.bleedbox = RectangleObject([0, 0, PAGE_W, PAGE_H])
    page.trimbox = RectangleObject([BLEED_X, BLEED_Y, PAGE_W - BLEED_X, PAGE_H - BLEED_Y])
    writer = PdfWriter()
    writer.add_page(page)
    writer.add_metadata({
        "/Title": "DocRouter.AI tabletop banner — print artwork",
        "/Subject": "8.74 x 14.21 in with bleed, 8.50 x 13.98 in trim, CMYK",
        "/Author": "DocRouter.AI",
    })
    with PDF.open("wb") as fh:
        writer.write(fh)
    tmp_pdf.unlink()


def build_rasters() -> None:
    pix = pymupdf.open(PDF)[0].get_pixmap(dpi=DPI, alpha=False)
    rgb = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)

    proof_w = 1200
    rgb.resize((proof_w, round(rgb.height * proof_w / rgb.width)),
               Image.Resampling.LANCZOS).save(PROOF, optimize=True)

    rgb_profile = "/System/Library/ColorSync/Profiles/Generic RGB Profile.icc"
    cmyk_profile = "/System/Library/ColorSync/Profiles/Generic CMYK Profile.icc"
    cmyk = ImageCms.profileToProfile(rgb, rgb_profile, cmyk_profile, outputMode="CMYK",
                                     renderingIntent=ImageCms.Intent.PERCEPTUAL)
    cmyk.save(TIFF, dpi=(DPI, DPI), compression="tiff_lzw",
              icc_profile=Path(cmyk_profile).read_bytes())


if __name__ == "__main__":
    build_pdf()
    build_rasters()
    for p in (TIFF, PDF, PROOF):
        print(p)

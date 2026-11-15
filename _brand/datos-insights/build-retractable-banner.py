#!/usr/bin/env python3
"""Build the 33 x 79 inch DocRouter pull-up banner with 1/8 inch bleed."""

from __future__ import annotations

import re
from pathlib import Path

import fitz
from PIL import Image, ImageCms, ImageDraw
from pypdf import PdfReader, PdfWriter
from pypdf.generic import RectangleObject
import qrcode
from qrcode.constants import ERROR_CORRECT_H
from reportlab.lib.colors import CMYKColor
from reportlab.lib.pagesizes import inch
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from svglib.svglib import svg2rlg


ROOT = Path(__file__).resolve().parents[2]
BRAND = ROOT / "_brand" / "datos-insights"

PDF = BRAND / "docrouter-retractable-banner-33x79-print.pdf"
TIFF = BRAND / "docrouter-retractable-banner-33x79-cmyk.tif"
PROOF = BRAND / "docrouter-retractable-banner-proof.png"
QR_CROP = BRAND / "docrouter-retractable-banner-qr.png"
TEMP_PDF = BRAND / ".docrouter-retractable-banner.pdf"
TEMP_MARK = BRAND / ".docrouter-mark-blue.svg"
QR_URL = "https://docrouter.ai/demo"

TRIM_W_IN = 33
TRIM_H_IN = 79
BLEED_IN = 0.125
DPI = 150
SOURCE_W = 435
SOURCE_H = 1024

PAGE_W = (TRIM_W_IN + 2 * BLEED_IN) * inch
PAGE_H = (TRIM_H_IN + 2 * BLEED_IN) * inch
BLEED = BLEED_IN * inch
TRIM_W = TRIM_W_IN * inch
TRIM_H = TRIM_H_IN * inch
SX = TRIM_W / SOURCE_W
SY = TRIM_H / SOURCE_H
U = SY

# Print colors. The PDF uses DeviceCMYK; the TIFF carries Generic CMYK.
BLUE = CMYKColor(1.00, 0.68, 0.00, 0.02)
NAVY = CMYKColor(0.89, 0.86, 0.00, 0.54)
MUTED = CMYKColor(0.58, 0.48, 0.00, 0.31)
PALE = CMYKColor(0.22, 0.07, 0.00, 0.00)
LIGHT_BLUE = CMYKColor(0.42, 0.12, 0.00, 0.00)
WHITE = CMYKColor(0, 0, 0, 0)


def x(value: float) -> float:
    return BLEED + value * SX


def y(value: float) -> float:
    """Map a top-down source coordinate to PDF coordinates."""
    return PAGE_H - BLEED - value * SY


def centered_text(
    c: canvas.Canvas,
    text: str,
    top: float,
    font: str,
    size: float,
    color: CMYKColor,
) -> None:
    c.setFont(font, size * U)
    c.setFillColor(color)
    c.drawCentredString(PAGE_W / 2, y(top + size * 0.82), text)


def rounded_box(c: canvas.Canvas, left: float, top: float) -> None:
    bw, bh = 58, 54
    c.setStrokeColor(PALE)
    c.setLineWidth(0.9 * U)
    c.setFillColor(WHITE)
    c.roundRect(x(left), y(top + bh), bw * SX, bh * SY, 10 * U, stroke=1, fill=1)


def icon_document(c: canvas.Canvas, left: float, top: float) -> None:
    ox, oy = x(left + 20), y(top + 14)
    c.setStrokeColor(BLUE)
    c.setLineWidth(2.0 * U)
    c.setLineJoin(1)
    p = c.beginPath()
    p.moveTo(ox, oy)
    p.lineTo(x(left + 31), y(top + 14))
    p.lineTo(x(left + 39), y(top + 22))
    p.lineTo(x(left + 39), y(top + 42))
    p.lineTo(x(left + 20), y(top + 42))
    p.close()
    c.drawPath(p, stroke=1, fill=0)
    c.line(x(left + 27), y(top + 31), x(left + 35), y(top + 31))
    c.line(x(left + 27), y(top + 36), x(left + 35), y(top + 36))


def icon_structure(c: canvas.Canvas, left: float, top: float) -> None:
    c.setStrokeColor(BLUE)
    c.setLineWidth(2.0 * U)
    for px in (left + 16, left + 33):
        for py in (top + 14, top + 31):
            c.roundRect(x(px), y(py + 10), 10 * SX, 10 * SY, 2 * U, stroke=1, fill=0)


def icon_extract(c: canvas.Canvas, left: float, top: float) -> None:
    c.setStrokeColor(BLUE)
    c.setLineWidth(2.0 * U)
    cx = left + 29
    p = c.beginPath()
    p.moveTo(x(cx), y(top + 9))
    p.lineTo(x(cx + 4), y(top + 23))
    p.lineTo(x(cx + 15), y(top + 27))
    p.lineTo(x(cx + 4), y(top + 31))
    p.lineTo(x(cx), y(top + 45))
    p.lineTo(x(cx - 4), y(top + 31))
    p.lineTo(x(cx - 15), y(top + 27))
    p.lineTo(x(cx - 4), y(top + 23))
    p.close()
    c.drawPath(p, stroke=1, fill=0)
    c.line(x(cx - 15), y(top + 9), x(cx - 15), y(top + 19))
    c.line(x(cx - 20), y(top + 14), x(cx - 10), y(top + 14))
    c.line(x(cx - 16), y(top + 39), x(cx - 16), y(top + 47))
    c.line(x(cx - 20), y(top + 43), x(cx - 12), y(top + 43))


def icon_integrate(c: canvas.Canvas, left: float, top: float) -> None:
    c.setStrokeColor(BLUE)
    c.setLineWidth(2.0 * U)
    c.setLineCap(1)
    c.line(x(left + 24), y(top + 18), x(left + 16), y(top + 27))
    c.line(x(left + 16), y(top + 27), x(left + 24), y(top + 36))
    c.line(x(left + 36), y(top + 18), x(left + 44), y(top + 27))
    c.line(x(left + 44), y(top + 27), x(left + 36), y(top + 36))
    c.line(x(left + 34), y(top + 13), x(left + 27), y(top + 41))


def connector(c: canvas.Canvas, start_x: float, end_x: float, center_y: float) -> None:
    c.setStrokeColor(LIGHT_BLUE)
    c.setLineWidth(1.5 * U)
    c.setDash(1.2 * U, 3.5 * U)
    p = c.beginPath()
    p.moveTo(x(start_x), y(center_y))
    p.curveTo(
        x(start_x + 12),
        y(center_y - 8),
        x(end_x - 12),
        y(center_y + 8),
        x(end_x),
        y(center_y),
    )
    c.drawPath(p, stroke=1, fill=0)
    c.setDash()


def workflow_text(c: canvas.Canvas, center_x: float, top: float, title: str) -> None:
    c.setFillColor(NAVY)
    c.setFont("IBM-Plex-Sans-SemiBold", 17 * U)
    c.drawCentredString(x(center_x), y(top + 16), title)


def qr_matrix() -> list[list[bool]]:
    qr = qrcode.QRCode(
        version=None,
        error_correction=ERROR_CORRECT_H,
        box_size=1,
        border=4,
    )
    qr.add_data(QR_URL)
    qr.make(fit=True)
    return qr.get_matrix()


def finder_starts(count: int) -> tuple[tuple[int, int], ...]:
    border = 4
    return (
        (border, border),
        (border, count - border - 7),
        (count - border - 7, border),
    )


def is_finder_module(row: int, col: int, count: int) -> bool:
    """Identify modules replaced by custom rounded finder targets."""
    return any(
        start_row <= row < start_row + 7 and start_col <= col < start_col + 7
        for start_row, start_col in finder_starts(count)
    )


def qr_image(matrix: list[list[bool]], size: int) -> Image.Image:
    """Draw rounded data modules and square finder targets at raster size."""
    count = len(matrix)
    image = Image.new("RGB", (size, size), "white")
    draw = ImageDraw.Draw(image)
    blue = (7, 85, 245)
    edges = [round(i * size / count) for i in range(count + 1)]
    for row, values in enumerate(matrix):
        for col, filled in enumerate(values):
            if filled:
                box = (edges[col], edges[row], edges[col + 1] - 1, edges[row + 1] - 1)
                if not is_finder_module(row, col, count):
                    radius = max(1, round((edges[col + 1] - edges[col]) * 0.20))
                    draw.rounded_rectangle(box, radius=radius, fill=blue)

    for start_row, start_col in finder_starts(count):
        module = edges[start_col + 1] - edges[start_col]
        outer = (
            edges[start_col],
            edges[start_row],
            edges[start_col + 7] - 1,
            edges[start_row + 7] - 1,
        )
        inner = (
            edges[start_col + 1],
            edges[start_row + 1],
            edges[start_col + 6] - 1,
            edges[start_row + 6] - 1,
        )
        center = (
            edges[start_col + 2],
            edges[start_row + 2],
            edges[start_col + 5] - 1,
            edges[start_row + 5] - 1,
        )
        draw.rounded_rectangle(outer, radius=max(1, round(module * 0.45)), fill=blue)
        draw.rounded_rectangle(inner, radius=max(1, round(module * 0.30)), fill="white")
        draw.rounded_rectangle(center, radius=max(1, round(module * 0.20)), fill=blue)
    return image


def draw_qr(
    c: canvas.Canvas,
    matrix: list[list[bool]],
    left: float,
    bottom: float,
    size: float,
) -> None:
    """Draw rounded CMYK vector modules with square finder targets."""
    count = len(matrix)
    module = size / count
    c.setFillColor(WHITE)
    c.rect(left, bottom, size, size, stroke=0, fill=1)
    c.setFillColor(BLUE)
    for row, values in enumerate(matrix):
        module_y = bottom + (count - row - 1) * module
        for col, filled in enumerate(values):
            if filled:
                module_x = left + col * module
                if not is_finder_module(row, col, count):
                    c.roundRect(
                        module_x,
                        module_y,
                        module,
                        module,
                        module * 0.20,
                        stroke=0,
                        fill=1,
                    )

    for start_row, start_col in finder_starts(count):
        finder_x = left + start_col * module
        finder_y = bottom + (count - start_row - 7) * module
        c.setFillColor(BLUE)
        c.roundRect(
            finder_x,
            finder_y,
            7 * module,
            7 * module,
            0.45 * module,
            stroke=0,
            fill=1,
        )
        c.setFillColor(WHITE)
        c.roundRect(
            finder_x + module,
            finder_y + module,
            5 * module,
            5 * module,
            0.30 * module,
            stroke=0,
            fill=1,
        )
        c.setFillColor(BLUE)
        c.roundRect(
            finder_x + 2 * module,
            finder_y + 2 * module,
            3 * module,
            3 * module,
            0.20 * module,
            stroke=0,
            fill=1,
        )


def build_pdf() -> tuple[float, float, float]:
    pdfmetrics.registerFont(
        TTFont(
            "IBM-Plex-Sans-SemiBold",
            str(ROOT / "_brand/fonts/IBM-Plex-Sans-SemiBold.ttf"),
        )
    )

    # Generate the QR directly from the destination URL.
    matrix = qr_matrix()
    qr_image(matrix, len(matrix) * 20).save(QR_CROP)

    # Recolor the existing vector mark to the banner blue.
    mark_svg = (BRAND / "docrouter-mark-color.svg").read_text()
    mark_svg = re.sub(r'fill="url\(#mark\)"', 'fill="#0755F5"', mark_svg)
    TEMP_MARK.write_text(mark_svg)
    mark = svg2rlg(str(TEMP_MARK))

    def recolor_mark(node: object) -> None:
        if getattr(node, "fillColor", None) is not None:
            node.fillColor = BLUE
        if getattr(node, "strokeColor", None) is not None:
            node.strokeColor = BLUE
        for child in getattr(node, "contents", ()):
            recolor_mark(child)

    recolor_mark(mark)

    c = canvas.Canvas(str(TEMP_PDF), pagesize=(PAGE_W, PAGE_H), pageCompression=1)
    c.setTitle("DocRouter.AI retractable banner — 33 × 79 in plus 1/8 in bleed")
    c.setAuthor("DocRouter.AI")
    c.setSubject("CMYK print artwork, 850 × 2000 mm pull-up banner")
    c.setFillColor(WHITE)
    c.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)

    # Logo mark.
    mark_w = 84 * SX
    mark_h = mark_w * mark.height / mark.width
    mark_x = PAGE_W / 2 - mark_w / 2
    mark_y = y(42) - mark_h
    c.saveState()
    c.translate(mark_x, mark_y)
    c.scale(mark_w / mark.width, mark_h / mark.height)
    from reportlab.graphics import renderPDF

    renderPDF.draw(mark, c, 0, 0)
    c.restoreState()

    centered_text(c, "DocRouter.AI", 144, "IBM-Plex-Sans-SemiBold", 38, BLUE)
    centered_text(
        c,
        "AI-powered document workflows",
        204,
        "IBM-Plex-Sans-SemiBold",
        20.5,
        NAVY,
    )

    c.setStrokeColor(BLUE)
    c.setLineWidth(3.5 * U)
    c.setLineCap(1)
    c.line(x(165), y(243), x(271), y(243))

    centered_text(
        c,
        "Scan for a live demo",
        288,
        "IBM-Plex-Sans-SemiBold",
        27,
        BLUE,
    )

    # Match the QR enclosure to the width of the head mark.
    enclosure_size = 84 * SX
    enclosure_x = PAGE_W / 2 - enclosure_size / 2
    enclosure_top = y(336)
    enclosure_y = enclosure_top - enclosure_size
    c.setFillColor(WHITE)
    c.setStrokeColor(PALE)
    c.setLineWidth(0.8 * U)
    c.roundRect(
        enclosure_x,
        enclosure_y,
        enclosure_size,
        enclosure_size,
        11 * U,
        stroke=1,
        fill=1,
    )

    qr_size = 72 * SX
    qr_x = PAGE_W / 2 - qr_size / 2
    qr_y = enclosure_y + (enclosure_size - qr_size) / 2
    draw_qr(c, matrix, qr_x, qr_y, qr_size)

    box_top = 518
    stages = [
        (32, 61, "Index", icon_document),
        (137, 166, "Structure", icon_structure),
        (241, 270, "Extract", icon_extract),
        (344, 373, "Integrate", icon_integrate),
    ]

    # The path sits behind the boxes and reads as one continuous pipeline.
    connector(c, 90, 137, 545)
    connector(c, 195, 241, 545)
    connector(c, 299, 344, 545)

    for left, center, title, icon in stages:
        rounded_box(c, left, box_top)
        icon(c, left, box_top)
        workflow_text(c, center, 577, title)

    c.showPage()
    c.save()

    # Add explicit trim and bleed boxes.
    reader = PdfReader(str(TEMP_PDF))
    page = reader.pages[0]
    page.mediabox = RectangleObject([0, 0, PAGE_W, PAGE_H])
    page.bleedbox = RectangleObject([0, 0, PAGE_W, PAGE_H])
    page.trimbox = RectangleObject([BLEED, BLEED, PAGE_W - BLEED, PAGE_H - BLEED])
    writer = PdfWriter()
    writer.add_page(page)
    writer.add_metadata(
        {
            "/Title": "DocRouter.AI retractable banner — print artwork",
            "/Subject": "33 × 79 in trim, 1/8 in bleed, CMYK",
            "/Author": "DocRouter.AI",
        }
    )
    with PDF.open("wb") as output:
        writer.write(output)

    TEMP_PDF.unlink(missing_ok=True)
    TEMP_MARK.unlink(missing_ok=True)
    return qr_x, qr_y, qr_size


def build_rasters(qr_x: float, qr_y: float, qr_size: float) -> None:
    # Rasterize the print PDF at the requested minimum resolution.
    doc = fitz.open(PDF)
    page = doc[0]
    pix = page.get_pixmap(matrix=fitz.Matrix(DPI / 72, DPI / 72), alpha=False)
    rgb = Image.frombytes("RGB", (pix.width, pix.height), pix.samples)

    # Draw the QR directly at final raster size with hard module edges.
    target = max(1, round(qr_size / 72 * DPI))
    qr_scaled = qr_image(qr_matrix(), target)
    left = round(qr_x / 72 * DPI)
    # PDF y is bottom-up; raster y is top-down.
    top = round((PAGE_H - (qr_y + qr_size)) / 72 * DPI)
    rgb.paste(qr_scaled, (left, top))

    # A compact RGB proof for review.
    proof_w = 1700
    proof_h = round(rgb.height * proof_w / rgb.width)
    proof = rgb.resize((proof_w, proof_h), Image.Resampling.LANCZOS)
    proof_scale = proof_w / rgb.width
    proof_qr_size = round(target * proof_scale)
    proof.paste(
        qr_image(qr_matrix(), proof_qr_size),
        (round(left * proof_scale), round(top * proof_scale)),
    )
    proof.save(PROOF, optimize=True)

    # Color-manage the print raster into Generic CMYK and embed the profile.
    rgb_profile = "/System/Library/ColorSync/Profiles/Generic RGB Profile.icc"
    cmyk_profile = "/System/Library/ColorSync/Profiles/Generic CMYK Profile.icc"
    cmyk = ImageCms.profileToProfile(
        rgb,
        rgb_profile,
        cmyk_profile,
        outputMode="CMYK",
        renderingIntent=ImageCms.Intent.PERCEPTUAL,
    )
    cmyk.save(
        TIFF,
        dpi=(DPI, DPI),
        compression="tiff_lzw",
        icc_profile=Path(cmyk_profile).read_bytes(),
    )


def main() -> None:
    qr_x, qr_y, qr_size = build_pdf()
    build_rasters(qr_x, qr_y, qr_size)
    print(PDF)
    print(TIFF)
    print(PROOF)
    print(QR_CROP)


if __name__ == "__main__":
    main()

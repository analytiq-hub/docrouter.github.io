#!/usr/bin/env python3
"""Build a two-sided DocRouter.AI business card (US 3.5 x 2 in trim, 3.61 x 2.11 in with bleed).

Template: edit the CARD settings below and rerun to make a card for someone else.

    python3 _brand/business-card/build-business-card.py

Outputs (next to this script, file names keyed by SLUG):
    <slug>-business-card-print.pdf   2 pages (front, back), CMYK vectors, trim/bleed boxes
    <slug>-business-card-front.png   RGB proof of the front, 600 dpi, trimmed
    <slug>-business-card-back.png    RGB proof of the back, 600 dpi, trimmed
"""

from __future__ import annotations

import re
from pathlib import Path

import qrcode
from qrcode.constants import ERROR_CORRECT_M
from pypdf import PdfReader, PdfWriter
from pypdf.generic import RectangleObject
from reportlab.graphics import renderPDF
from reportlab.lib.colors import CMYKColor
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from svglib.svglib import svg2rlg

# ---------------------------------------------------------------------------
# Card content (the template part)
# ---------------------------------------------------------------------------
CARD = {
    "slug": "andrei-radulescu-banu",
    "name": "Andrei Radulescu-Banu",
    "title": "CEO & Founder",
    "email": "andrei@docrouter.ai",
    "phone": "617.216.8509",
    "qr_url": "https://www.linkedin.com/in/andrei-radulescu-banu",
    "qr_caption": "LinkedIn",
    "tagline": "AI data layer for operational documents",
}

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
FONTS = ROOT / "_brand" / "fonts"
LOGO_SVG = ROOT / "_brand" / "datos-insights" / "docrouter-logo-horizontal-color.svg"

# ---------------------------------------------------------------------------
# Geometry (points). Matches the printer template: 3.61 x 2.11 in document
# (3.5 x 2 in trim + 0.055 in bleed per side) with the safety area 0.11 in in
# from the document edge (0.055 in inside trim). All text, logo, icons and the
# QR code sit inside MARGIN, which must be >= SAFE; only background art
# (wash, dot grid, rings) runs into the bleed.
# ---------------------------------------------------------------------------
IN = 72.0
TRIM_W, TRIM_H = 3.5 * IN, 2.0 * IN
BLEED = 0.055 * IN
PAGE_W, PAGE_H = TRIM_W + 2 * BLEED, TRIM_H + 2 * BLEED
SAFE = 0.055 * IN                      # safety inset from trim
MARGIN = 0.1875 * IN                   # content inset from trim
assert MARGIN >= SAFE

# ---------------------------------------------------------------------------
# Colors: homepage tokens (assets/css/enterprise.css) converted to CMYK.
# ---------------------------------------------------------------------------
NAVY = CMYKColor(0.66, 0.43, 0.00, 0.70)       # --dr-navy  #1a2b4c
BLUE = CMYKColor(1.00, 0.52, 0.00, 0.00)       # --dr-blue  #007bff
SLATE = CMYKColor(0.28, 0.17, 0.00, 0.45)      # --dr-slate #64748b
ACCENT = CMYKColor(0.06, 0.03, 0.00, 0.00)     # --dr-bg-accent #f0f7ff
TILE_BORDER = CMYKColor(0.09, 0.05, 0.00, 0.06)  # slate-200 #e2e8f0
RING = CMYKColor(0.13, 0.06, 0.00, 0.00)       # blue at ~12% on white
DOT = CMYKColor(0.05, 0.03, 0.00, 0.05)        # navy dot grid at low tint
CONNECTOR = CMYKColor(0.42, 0.12, 0.00, 0.00)  # dotted path between stages
WORDMARK = CMYKColor(0.72, 0.42, 0.00, 0.49)   # logo wordmark #244C82
MARK_STOPS = (                                   # logo mark gradient
    CMYKColor(0.00, 0.29, 0.72, 0.00),         # #FFB547
    CMYKColor(0.00, 0.46, 0.74, 0.00),         # #FF8A42
    CMYKColor(0.00, 0.62, 0.72, 0.00),         # #FF6247
)
WHITE = CMYKColor(0, 0, 0, 0)


def tx(v: float) -> float:
    """Trim-relative x (from left trim edge) to page coordinates."""
    return BLEED + v


def ty(v: float) -> float:
    """Trim-relative y measured DOWN from the top trim edge to page coordinates."""
    return PAGE_H - BLEED - v


def register_fonts() -> None:
    for name in ("Regular", "Medium", "SemiBold", "Bold"):
        pdfmetrics.registerFont(TTFont(f"Inter-{name}", str(FONTS / f"Inter-{name}.ttf")))


def tracked(c: canvas.Canvas, x: float, y: float, text: str, font: str, size: float,
            tracking_em: float) -> None:
    """Draw letter-spaced text (like the site's uppercase section labels)."""
    c.saveState()  # char spacing otherwise leaks into later drawString calls
    t = c.beginText(x, y)
    t.setFont(font, size)
    t.setCharSpace(size * tracking_em)
    t.textOut(text)
    c.drawText(t)
    c.restoreState()


# ---------------------------------------------------------------------------
# Backgrounds (shared with the homepage hero: accent wash, dot grid, rings)
# ---------------------------------------------------------------------------
def hero_background(c: canvas.Canvas, rings: bool) -> None:
    c.setFillColor(WHITE)
    c.rect(0, 0, PAGE_W, PAGE_H, stroke=0, fill=1)
    c.saveState()
    p = c.beginPath()
    p.rect(0, 0, PAGE_W, PAGE_H)
    c.clipPath(p, stroke=0, fill=0)
    c.linearGradient(0, PAGE_H, 0, 0, (ACCENT, WHITE), extend=True)
    c.restoreState()

    # Dot grid fading toward the bottom, as in .enterprise-hero::before.
    step = 6.0
    c.setFillColor(DOT)
    row = 0
    yv = PAGE_H - step / 2
    while yv > PAGE_H * 0.35:
        fade = (yv - PAGE_H * 0.35) / (PAGE_H * 0.65)
        r = 0.22 + 0.18 * fade
        xv = step / 2
        while xv < PAGE_W:
            c.circle(xv, yv, r, stroke=0, fill=1)
            xv += step
        yv -= step
        row += 1

    if rings:
        c.setStrokeColor(RING)
        c.setLineWidth(0.5)
        c.circle(tx(TRIM_W + 6), ty(-10), 62, stroke=1, fill=0)
        c.circle(tx(TRIM_W + 6), ty(-10), 40, stroke=1, fill=0)


# ---------------------------------------------------------------------------
# Logo: wordmark via svglib, gradient mark redrawn from its own path data
# ---------------------------------------------------------------------------
def _svg_path_tokens(d: str):
    for cmd, args in re.findall(r"([MLCZ])([^MLCZ]*)", d):
        yield cmd, [float(v) for v in re.findall(r"-?\d*\.?\d+", args)]


def draw_logo(c: canvas.Canvas, left: float, top: float, width: float) -> float:
    """Draw the horizontal colour logo; return its rendered height."""
    svg = LOGO_SVG.read_text()
    vb_w, vb_h = (float(v) for v in re.search(r'viewBox="0 0 ([\d.]+) ([\d.]+)"', svg).groups())
    s = width / vb_w
    height = vb_h * s

    # Wordmark: strip the gradient mark and render the rest as vectors.
    word_svg = re.sub(r'<path fill="url\(#mark\)"[^>]*/>', "", svg)
    tmp = HERE / ".logo-wordmark.svg"
    tmp.write_text(word_svg)
    drawing = svg2rlg(str(tmp))
    tmp.unlink()

    def recolor(node: object) -> None:
        if getattr(node, "fillColor", None) is not None:
            node.fillColor = WORDMARK
        for child in getattr(node, "contents", ()):
            recolor(child)

    recolor(drawing)
    c.saveState()
    c.translate(left, top - height)
    c.scale(width / drawing.width, height / drawing.height)
    renderPDF.draw(drawing, c, 0, 0)
    c.restoreState()

    # Mark: rebuild its path in SVG space, clip, and fill with the gradient.
    d = re.search(r'fill="url\(#mark\)"[^>]*\sd="([^"]+)"', svg).group(1)
    gx, gy, gs = (float(v) for v in re.search(
        r'translate\(([-\d.]+) ([-\d.]+)\) scale\(([\d.]+)\)', svg).groups())

    def pt(x: float, y: float) -> tuple[float, float]:
        X = (gx + gs * x) * s
        Y = (gy + gs * y) * s
        return left + X, top - Y

    path = c.beginPath()
    ys = []
    for cmd, a in _svg_path_tokens(d):
        if cmd == "M":
            path.moveTo(*pt(a[0], a[1])); ys.append(a[1])
        elif cmd == "L":
            path.lineTo(*pt(a[0], a[1])); ys.append(a[1])
        elif cmd == "C":
            path.curveTo(*pt(a[0], a[1]), *pt(a[2], a[3]), *pt(a[4], a[5])); ys.append(a[5])
        elif cmd == "Z":
            path.close()
    c.saveState()
    c.clipPath(path, stroke=0, fill=0, fillMode=0)  # even-odd, as in the SVG
    _, y_top = pt(0, min(ys))
    _, y_bot = pt(0, max(ys))
    c.linearGradient(left, y_top, left, y_bot, MARK_STOPS, (0, 0.5, 1), extend=True)
    c.restoreState()
    return height


# ---------------------------------------------------------------------------
# Small line icons drawn in a 24-unit SVG box (y down), like the site icons
# ---------------------------------------------------------------------------
class Icon:
    def __init__(self, c: canvas.Canvas, left: float, top: float, size: float,
                 color: CMYKColor, stroke: float = 1.5):
        self.c, self.left, self.top, self.k = c, left, top, size / 24.0
        c.saveState()
        c.setStrokeColor(color)
        c.setLineWidth(stroke * self.k)
        c.setLineCap(1)
        c.setLineJoin(1)

    def p(self, x: float, y: float) -> tuple[float, float]:
        return self.left + x * self.k, self.top - y * self.k

    def line(self, x1, y1, x2, y2):
        self.c.line(*self.p(x1, y1), *self.p(x2, y2))

    def poly(self, pts, close=False):
        path = self.c.beginPath()
        path.moveTo(*self.p(*pts[0]))
        for q in pts[1:]:
            path.lineTo(*self.p(*q))
        if close:
            path.close()
        self.c.drawPath(path, stroke=1, fill=0)

    def rrect(self, x, y, w, h, r):
        X, Y = self.p(x, y + h)
        self.c.roundRect(X, Y, w * self.k, h * self.k, r * self.k, stroke=1, fill=0)

    def done(self):
        self.c.restoreState()


def icon_document(i: Icon) -> None:
    i.line(9, 12, 15, 12)
    i.line(9, 16, 15, 16)
    i.poly([(7, 3), (13, 3), (19, 9), (19, 19), (17, 21), (7, 21), (5, 19), (5, 5)], close=True)
    i.poly([(13, 3), (13, 9), (19, 9)])


def icon_structure(i: Icon) -> None:
    for x in (4, 14):
        for y in (4, 14):
            i.rrect(x, y, 6, 6, 2)


def icon_extract(i: Icon) -> None:
    i.poly([(13, 3), (15.286, 9.857), (21, 12), (15.286, 14.143), (13, 21),
            (10.714, 14.143), (5, 12), (10.714, 9.857)], close=True)
    i.line(5, 3, 5, 7); i.line(3, 5, 7, 5)
    i.line(6, 17, 6, 21); i.line(4, 19, 8, 19)


def icon_integrate(i: Icon) -> None:
    i.line(10, 20, 14, 4)
    i.poly([(18, 8), (22, 12), (18, 16)])
    i.poly([(6, 16), (2, 12), (6, 8)])


def icon_mail(i: Icon) -> None:
    i.rrect(3, 5, 18, 14, 2)
    i.poly([(3.5, 6.5), (12, 13), (20.5, 6.5)])


def icon_phone(i: Icon) -> None:
    i.rrect(7, 2.5, 10, 19, 2)
    i.line(11, 18.5, 13, 18.5)


# ---------------------------------------------------------------------------
# QR code
# ---------------------------------------------------------------------------
def qr_matrix(url: str) -> list[list[bool]]:
    qr = qrcode.QRCode(error_correction=ERROR_CORRECT_M, box_size=1, border=0)
    qr.add_data(url)
    qr.make(fit=True)
    return qr.get_matrix()


def draw_qr(c: canvas.Canvas, matrix, left: float, bottom: float, size: float) -> None:
    """Rounded data modules and rounded finder targets, matching the banner QR."""
    n = len(matrix)
    m = size / n
    finders = ((0, 0), (0, n - 7), (n - 7, 0))

    def in_finder(r, col):
        return any(fr <= r < fr + 7 and fc <= col < fc + 7 for fr, fc in finders)

    c.setFillColor(NAVY)
    for r, row in enumerate(matrix):
        for col, on in enumerate(row):
            if on and not in_finder(r, col):
                c.roundRect(left + col * m, bottom + (n - r - 1) * m, m, m, m * 0.2, stroke=0, fill=1)
    for fr, fc in finders:
        fx, fy = left + fc * m, bottom + (n - fr - 7) * m
        c.setFillColor(NAVY); c.roundRect(fx, fy, 7 * m, 7 * m, 0.45 * m, stroke=0, fill=1)
        c.setFillColor(WHITE); c.roundRect(fx + m, fy + m, 5 * m, 5 * m, 0.30 * m, stroke=0, fill=1)
        c.setFillColor(NAVY); c.roundRect(fx + 2 * m, fy + 2 * m, 3 * m, 3 * m, 0.20 * m, stroke=0, fill=1)


# ---------------------------------------------------------------------------
# Faces
# ---------------------------------------------------------------------------
def draw_front(c: canvas.Canvas) -> None:
    hero_background(c, rings=True)

    draw_logo(c, tx(MARGIN), ty(MARGIN), width=1.55 * IN)

    # Identity block, anchored to the bottom safe margin.
    base = TRIM_H - MARGIN            # baseline of the last contact line (from top)
    line_gap = 11.5
    phone_y, email_y = base, base - line_gap
    rule_y = email_y - 11
    title_y = rule_y - 8
    name_y = title_y - 11

    c.setFillColor(NAVY)
    c.setFont("Inter-Bold", 11.5)
    c.drawString(tx(MARGIN), ty(name_y), CARD["name"])

    c.setFillColor(BLUE)
    tracked(c, tx(MARGIN), ty(title_y), CARD["title"].upper(), "Inter-SemiBold", 6.2, 0.08)

    c.setStrokeColor(BLUE)
    c.setLineWidth(1.1)
    c.setLineCap(1)
    c.line(tx(MARGIN), ty(rule_y), tx(MARGIN + 18), ty(rule_y))

    for y_from_top, text, icon in ((email_y, CARD["email"], icon_mail),
                                   (phone_y, CARD["phone"], icon_phone)):
        ic = Icon(c, tx(MARGIN), ty(y_from_top - 6.9), 8.0, BLUE, stroke=1.7)
        icon(ic)
        ic.done()
        c.setFillColor(NAVY)
        c.setFont("Inter-Medium", 7.4)
        c.drawString(tx(MARGIN + 12), ty(y_from_top), text)

    # QR tile, bottom right (enterprise-icon-tile styling).
    tile = 0.92 * IN
    tile_left = TRIM_W - MARGIN - tile
    tile_top = TRIM_H - MARGIN - tile
    c.setFillColor(WHITE)
    c.setStrokeColor(TILE_BORDER)
    c.setLineWidth(0.5)
    c.roundRect(tx(tile_left), ty(tile_top + tile), tile, tile, 6, stroke=1, fill=1)
    qr = 0.76 * IN
    pad = (tile - qr) / 2
    draw_qr(c, qr_matrix(CARD["qr_url"]), tx(tile_left + pad), ty(tile_top + pad + qr), qr)

    c.setFillColor(SLATE)
    label = CARD["qr_caption"].upper()
    size = 5.4
    t = label
    w = pdfmetrics.stringWidth(t, "Inter-SemiBold", size) + size * 0.12 * (len(t) - 1)
    tracked(c, tx(tile_left + tile / 2 - w / 2), ty(tile_top - 5), t, "Inter-SemiBold", size, 0.12)


def draw_back(c: canvas.Canvas) -> None:
    hero_background(c, rings=False)

    # Tagline, centred, homepage hero wording with the blue emphasis.
    lead, emph = "AI data layer for ", "operational documents"
    size = 9.2
    w1 = pdfmetrics.stringWidth(lead, "Inter-SemiBold", size)
    w2 = pdfmetrics.stringWidth(emph, "Inter-SemiBold", size)
    x0 = tx(TRIM_W / 2 - (w1 + w2) / 2)
    y0 = ty(0.47 * IN)
    c.setFont("Inter-SemiBold", size)
    c.setFillColor(NAVY); c.drawString(x0, y0, lead)
    c.setFillColor(BLUE); c.drawString(x0 + w1, y0, emph)

    # Workflow strip: Index -> Structure -> Extract -> Integrate.
    stages = [("Index", icon_document), ("Structure", icon_structure),
              ("Extract", icon_extract), ("Integrate", icon_integrate)]
    tile = 0.40 * IN
    span = TRIM_W - 2 * (MARGIN + 6)
    pitch = (span - tile) / 3
    base_top = 0.80 * IN
    stagger = 2.0                      # the banner's gentle up/down rhythm
    tops = [base_top + (stagger if k % 2 == 0 else -stagger) for k in range(4)]
    lefts = [MARGIN + 6 + k * pitch for k in range(4)]

    c.setStrokeColor(CONNECTOR)
    c.setLineWidth(0.7)
    c.setLineCap(1)
    c.setDash(0.1, 2.2)
    for k in range(3):
        sx, sy = lefts[k] + tile + 4, tops[k] + tile / 2
        ex, ey = lefts[k + 1] - 4, tops[k + 1] + tile / 2
        path = c.beginPath()
        path.moveTo(tx(sx), ty(sy))
        path.curveTo(tx(sx + 8), ty(sy), tx(ex - 8), ty(ey), tx(ex), ty(ey))
        c.drawPath(path, stroke=1, fill=0)
    c.setDash()

    for (title, icon), left, top in zip(stages, lefts, tops):
        c.setFillColor(WHITE)
        c.setStrokeColor(TILE_BORDER)
        c.setLineWidth(0.5)
        c.roundRect(tx(left), ty(top + tile), tile, tile, 5, stroke=1, fill=1)
        isz = tile * 0.52
        ic = Icon(c, tx(left + (tile - isz) / 2), ty(top + (tile - isz) / 2), isz, BLUE, stroke=1.6)
        icon(ic)
        ic.done()
        c.setFillColor(NAVY)
        c.setFont("Inter-SemiBold", 6.6)
        c.drawCentredString(tx(left + tile / 2), ty(top + tile + 9), title)

    # Small blue rule + site address at the foot.
    c.setFillColor(SLATE)
    tracked_text = "DOCROUTER.AI"
    sz = 5.6
    w = pdfmetrics.stringWidth(tracked_text, "Inter-SemiBold", sz) + sz * 0.14 * (len(tracked_text) - 1)
    tracked(c, tx(TRIM_W / 2 - w / 2), ty(TRIM_H - MARGIN), tracked_text, "Inter-SemiBold", sz, 0.14)


# ---------------------------------------------------------------------------
# Build
# ---------------------------------------------------------------------------
def build() -> list[Path]:
    register_fonts()
    slug = CARD["slug"]
    pdf_path = HERE / f"{slug}-business-card-print.pdf"
    tmp = HERE / f".{slug}-business-card.pdf"

    c = canvas.Canvas(str(tmp), pagesize=(PAGE_W, PAGE_H), pageCompression=1)
    c.setTitle(f"DocRouter.AI business card — {CARD['name']}")
    draw_front(c); c.showPage()
    draw_back(c); c.showPage()
    c.save()

    reader = PdfReader(str(tmp))
    writer = PdfWriter()
    for page in reader.pages:
        page.mediabox = RectangleObject([0, 0, PAGE_W, PAGE_H])
        page.bleedbox = RectangleObject([0, 0, PAGE_W, PAGE_H])
        page.trimbox = RectangleObject([BLEED, BLEED, PAGE_W - BLEED, PAGE_H - BLEED])
        writer.add_page(page)
    writer.add_metadata({
        "/Title": f"DocRouter.AI business card — {CARD['name']}",
        "/Subject": "US business card, 3.61 x 2.11 in with bleed, 3.5 x 2 in trim, CMYK",
        "/Author": "DocRouter.AI",
    })
    with pdf_path.open("wb") as fh:
        writer.write(fh)
    tmp.unlink()

    outputs = [pdf_path]
    import pymupdf  # proofs only
    doc = pymupdf.open(pdf_path)
    for page, face in zip(doc, ("front", "back")):
        clip = pymupdf.Rect(BLEED, BLEED, PAGE_W - BLEED, PAGE_H - BLEED)
        pix = page.get_pixmap(dpi=600, clip=clip, alpha=False)
        out = HERE / f"{slug}-business-card-{face}.png"
        pix.save(out)
        outputs.append(out)
    return outputs


if __name__ == "__main__":
    for p in build():
        print(p)

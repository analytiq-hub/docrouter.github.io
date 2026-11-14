#!/usr/bin/env python3
"""Build DocRouter.AI logo lockups for the Datos Insights showcase.

Traces the existing Analytiq head mark, sets it in the site gradient, and
pairs it with outlined wordmarks. Writes SVG, EPS, and transparent PNG for
horizontal and stacked lockups in full color and white.
"""

from __future__ import annotations

from pathlib import Path

import cairosvg
import numpy as np
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont
from PIL import Image, ImageDraw
from potrace import Bitmap

ROOT = Path(__file__).resolve().parent.parent
SRC_MARK = ROOT / "assets/images/analytiq_hub_logo_small.png"
FONT_PATH = ROOT / "_brand/fonts/IBM-Plex-Sans-SemiBold.ttf"
OUT = ROOT / "_brand/datos-insights"

NAVY = "#244C82"
# Warm, memorable gradient that avoids an alert-like saturated red.
GRADIENT_STOPS = (
    (0.0, "#FFB547"),
    (0.50, "#FF8A42"),
    (1.0, "#FF6247"),
)
WORDMARK = "DocRouter.AI"

# Icon is normalized to this height. Wordmark cap-height is a fraction of it.
ICON_HEIGHT = 1000.0
# Cap height relative to the full mark (including the neck trace).
CAP_RATIO = 0.52
# Gap between mark and wordmark, as a fraction of icon height.
GAP_RATIO = 0.14
# Optical lift so the wordmark sits with the face, not the dangling trace.
BASELINE_LIFT = 0.045


def trace_mark() -> tuple[str, float]:
    im = Image.open(SRC_MARK).convert("RGBA")
    alpha = np.array(im.split()[-1])
    mask = (alpha > 40).astype(np.uint8) * 255
    path = Bitmap(Image.fromarray(mask, mode="L"), blacklevel=0.5).trace(
        turdsize=8, alphamax=1.0, opticurve=True, opttolerance=0.15
    )
    # Curve 0 is the page background left by the trace. The rest is the mark
    # (stroke bodies plus the four node holes).
    curves = list(path)[1:]
    parts: list[str] = []
    minx = miny = 10**9
    maxx = maxy = -10**9
    for curve in curves:
        start = curve.start_point
        parts.append(f"M {start.x:.2f} {start.y:.2f}")
        for seg in curve:
            if seg.is_corner:
                parts.append(
                    f"L {seg.c.x:.2f} {seg.c.y:.2f} L {seg.end_point.x:.2f} {seg.end_point.y:.2f}"
                )
                pts = (seg.c, seg.end_point, start)
            else:
                parts.append(
                    f"C {seg.c1.x:.2f} {seg.c1.y:.2f} {seg.c2.x:.2f} {seg.c2.y:.2f} "
                    f"{seg.end_point.x:.2f} {seg.end_point.y:.2f}"
                )
                pts = (seg.c1, seg.c2, seg.end_point)
            for pt in pts:
                minx, miny = min(minx, pt.x), min(miny, pt.y)
                maxx, maxy = max(maxx, pt.x), max(maxy, pt.y)
        parts.append("Z")
    d = " ".join(parts)
    # Normalize into a 0..ICON_HEIGHT box, preserving aspect, y-down.
    bw, bh = maxx - minx, maxy - miny
    scale = ICON_HEIGHT / bh
    return (
        f'<g transform="translate({-minx * scale:.3f} {-miny * scale:.3f}) scale({scale:.6f})">'
        f'<path fill="currentColor" fill-rule="evenodd" d="{d}"/>'
        f"</g>",
        bw * scale,
    )


def wordmark_group(color: str) -> tuple[str, float, float, float]:
    """Return (svg group, width, cap height, descent) in the same units as the icon."""
    font = TTFont(FONT_PATH)
    glyphset = font.getGlyphSet()
    cmap = font.getBestCmap()
    upem = font["head"].unitsPerEm
    hmtx = font["hmtx"]
    os2 = font["OS/2"]
    cap = os2.sCapHeight or int(upem * 0.72)
    scale = (ICON_HEIGHT * CAP_RATIO) / cap
    width = 0.0
    chunks: list[str] = []
    for char in WORDMARK:
        name = cmap[ord(char)]
        pen = SVGPathPen(glyphset)
        # Flip Y so the glyph is upright in SVG, then place it on a shared baseline.
        wrapper = TransformPen(pen, (1, 0, 0, -1, 0, 0))
        glyphset[name].draw(wrapper)
        d = pen.getCommands()
        advance = hmtx[name][0]
        if d:
            chunks.append(
                f'<path fill="{color}" transform="translate({width:.3f} 0) scale({scale:.6f})" d="{d}"/>'
            )
        width += advance * scale
    descent = abs(os2.usWinDescent) * scale
    cap_h = cap * scale
    group = f'<g transform="translate(0 {cap_h:.3f})">{"".join(chunks)}</g>'
    return group, width, cap_h, descent


def svg_doc(width: float, height: float, body: str, defs: str = "") -> str:
    return (
        '<?xml version="1.0" encoding="UTF-8"?>\n'
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width:.2f} {height:.2f}" '
        f'width="{width:.2f}" height="{height:.2f}" role="img" aria-label="DocRouter.AI">\n'
        f"{defs}{body}\n</svg>\n"
    )


def gradient_defs() -> str:
    stops = "\n".join(
        f'    <stop offset="{offset * 100:.0f}%" stop-color="{color}"/>'
        for offset, color in GRADIENT_STOPS
    )
    return (
        "  <defs>\n"
        '    <linearGradient id="mark" x1="0" y1="0" x2="0" y2="1">\n'
        f"{stops}\n"
        "    </linearGradient>\n"
        "  </defs>\n"
    )


def mark_svg(mark: str, width: float, color: str) -> str:
    painted = mark.replace('fill="currentColor"', f'fill="{color}"')
    return svg_doc(width, ICON_HEIGHT, f"  {painted}")


def horizontal_svg(
    mark: str,
    mark_w: float,
    word: str,
    word_w: float,
    cap_h: float,
    descent: float,
    defs: str = "",
    gap_ratio: float = GAP_RATIO,
    baseline_lift: float = BASELINE_LIFT,
    center_caps: bool = False,
) -> tuple[str, float, float]:
    gap = ICON_HEIGHT * gap_ratio
    word_h = cap_h + descent
    if center_caps:
        # Vertical middle of the cap-height lines up with the middle of the icon.
        word_y = (ICON_HEIGHT - cap_h) / 2
    else:
        # Sit the wordmark on the face: center of caps aligned slightly above the mark center.
        word_y = (ICON_HEIGHT - word_h) / 2 - ICON_HEIGHT * baseline_lift
    width = mark_w + gap + word_w
    body = (
        f'  <g>{mark}</g>\n'
        f'  <g transform="translate({mark_w + gap:.3f} {word_y:.3f})">{word}</g>'
    )
    return svg_doc(width, ICON_HEIGHT, body, defs), width, ICON_HEIGHT


def stacked_svg(
    mark: str,
    mark_w: float,
    word: str,
    word_w: float,
    cap_h: float,
    descent: float,
    defs: str = "",
    gap_ratio: float = GAP_RATIO,
) -> tuple[str, float, float]:
    gap = ICON_HEIGHT * gap_ratio
    word_h = cap_h + descent
    width = max(mark_w, word_w)
    height = ICON_HEIGHT + gap + word_h
    mark_x = (width - mark_w) / 2
    word_x = (width - word_w) / 2
    body = (
        f'  <g transform="translate({mark_x:.3f} 0)">{mark}</g>\n'
        f'  <g transform="translate({word_x:.3f} {ICON_HEIGHT + gap:.3f})">{word}</g>'
    )
    return svg_doc(width, height, body, defs), width, height


def export(name: str, svg: str, pixel_width: int) -> None:
    svg_path = OUT / f"{name}.svg"
    svg_path.write_text(svg)
    cairosvg.svg2png(bytestring=svg.encode(), write_to=str(OUT / f"{name}.png"), output_width=pixel_width)
    cairosvg.svg2eps(bytestring=svg.encode(), write_to=str(OUT / f"{name}.eps"))


def contact_sheet() -> None:
    """Light and dark preview so the lockups can be checked by eye."""
    files = [
        "docrouter-logo-horizontal-color.png",
        "docrouter-logo-stacked-color.png",
        "docrouter-mark-color.png",
        "docrouter-logo-horizontal-white.png",
        "docrouter-logo-stacked-white.png",
        "docrouter-mark-white.png",
    ]
    thumbs = []
    for name in files:
        im = Image.open(OUT / name).convert("RGBA")
        target_w = 900
        target_h = int(im.height * (target_w / im.width))
        thumbs.append(im.resize((target_w, target_h), Image.Resampling.LANCZOS))
    pad, label_h, gap = 36, 28, 28
    cols = 3
    rows = 2
    cell_w = max(t.width for t in thumbs) + pad * 2
    cell_h = max(t.height for t in thumbs) + pad * 2 + label_h
    sheet = Image.new("RGB", (cols * cell_w + gap, rows * cell_h + gap), "#E7E5E4")
    draw = ImageDraw.Draw(sheet)
    labels = [
        "Horizontal, full color",
        "Stacked, full color",
        "Mark, full color",
        "Horizontal, white",
        "Stacked, white",
        "Mark, white",
    ]
    for i, (thumb, label) in enumerate(zip(thumbs, labels)):
        r, c = divmod(i, cols)
        x0 = gap // 2 + c * cell_w
        y0 = gap // 2 + r * cell_h
        bg = "#F8FAFC" if r == 0 else "#1A2B4C"
        draw.rectangle([x0, y0, x0 + cell_w - gap, y0 + cell_h - gap], fill=bg)
        tx = x0 + (cell_w - gap - thumb.width) // 2
        ty = y0 + label_h + (cell_h - gap - label_h - thumb.height) // 2
        sheet.paste(thumb, (tx, ty), thumb)
        fill = "#1A2B4C" if r == 0 else "#FFFFFF"
        draw.text((x0 + 16, y0 + 8), label, fill=fill)
    sheet.save(OUT / "_preview.png")


def main() -> None:
    if OUT.exists():
        for old in OUT.iterdir():
            if old.suffix in {".svg", ".png", ".eps"}:
                old.unlink()
    OUT.mkdir(parents=True, exist_ok=True)
    mark, mark_w = trace_mark()
    color_mark = mark.replace('fill="currentColor"', 'fill="url(#mark)"')
    white_mark = mark.replace('fill="currentColor"', 'fill="#FFFFFF"')
    word_navy, word_w, cap_h, descent = wordmark_group(NAVY)
    word_white, _, _, _ = wordmark_group("#FFFFFF")

    jobs: list[tuple[str, str, int]] = []

    mark_color = svg_doc(mark_w, ICON_HEIGHT, f"  {color_mark}", gradient_defs())
    mark_white = mark_svg(white_mark, mark_w, "#FFFFFF")
    jobs.append(("docrouter-mark-color", mark_color, 2000))
    jobs.append(("docrouter-mark-white", mark_white, 2000))

    h_color, _, _ = horizontal_svg(
        color_mark, mark_w, word_navy, word_w, cap_h, descent,
        gradient_defs(), center_caps=True,
    )
    h_white, _, _ = horizontal_svg(
        white_mark, mark_w, word_white, word_w, cap_h, descent,
        center_caps=True,
    )
    jobs.append(("docrouter-logo-horizontal-color", h_color, 4800))
    jobs.append(("docrouter-logo-horizontal-white", h_white, 4800))

    s_color, _, _ = stacked_svg(color_mark, mark_w, word_navy, word_w, cap_h, descent, gradient_defs())
    s_white, _, _ = stacked_svg(white_mark, mark_w, word_white, word_w, cap_h, descent)
    jobs.append(("docrouter-logo-stacked-color", s_color, 2800))
    jobs.append(("docrouter-logo-stacked-white", s_white, 2800))

    for name, svg, width in jobs:
        export(name, svg, width)
        print(name)

    contact_sheet()
    print("preview", OUT / "_preview.png")


if __name__ == "__main__":
    main()

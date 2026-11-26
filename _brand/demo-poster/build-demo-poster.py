#!/usr/bin/env python3
"""Build a poster (the still shown before playback) for a DocRouter video.

    python3 _brand/demo-poster/build-demo-poster.py \\
        --label "PRODUCT DEMO  ·  3:40" \\
        --title "An AI index for the archive" \\
        --subtitle "From first notice of loss to a cited answer" \\
        --out _brand/demo-poster/datos-2026-poster-v2.jpg

Series design, shared by every video: navy background with the pen pattern
("docrouter" in staggered rows of white / light blue / orange, see _brand/pen),
toned down and set on a diagonal, fading out behind a left-aligned text block.

Layout rules, from checking the poster in place on the site:
  * no drawn play button: the browser shows its own, and on phones they collide;
  * all text in the top ~75%: the browser's control bar covers the bottom;
  * large type: on a phone the poster is ~330 px wide and must still read.

Upload under a new versioned name (never overwrite a published poster; it is
cached for a year), e.g. demos/<collection>/poster-v2.jpg on media.docrouter.ai.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageChops, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
BRAND = HERE.parent
FONTS = BRAND / "fonts"

W, H = 1920, 1080
SS = 2                                   # supersample factor, for crisp text
SW, SH = W * SS, H * SS

NAVY = (26, 43, 76)                      # --dr-navy #1a2b4c
WHITE = (255, 255, 255)
LIGHT_BLUE = (104, 179, 227)             # pen colours, sampled from _brand/pen/docrouter-pen.png
ORANGE = (248, 156, 84)
SUBTITLE_GREY = (203, 213, 225)          # slate-300
WORD = "docrouter"
WORD_COLOURS = [WHITE, LIGHT_BLUE, ORANGE]

# Pattern and type settings for the series. Change them here, not per video.
PATTERN_SIZE = 46
PATTERN_ALPHA = 0.09                     # faint: texture, not text
PATTERN_ANGLE = 14
LEFT_SHADE = 0.85                        # how much the pattern fades behind the text
TEXT_X, TEXT_Y = 140, 200
LOGO_W = 560
LABEL_SIZE, TITLE_SIZE, SUBTITLE_SIZE = 34, 108, 48
TITLE_MAX_W = 1640                       # long titles shrink to fit


def font(name: str, size: float) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(str(FONTS / f"Inter-{name}.ttf"), int(size * SS))


def word_pattern() -> Image.Image:
    """Staggered rows of the word, as on the pen wrap, rotated. Returns an RGBA layer."""
    f = font("Bold", PATTERN_SIZE)
    pad = int(max(SW, SH) * 0.5)
    lw, lh = SW + 2 * pad, SH + 2 * pad
    layer = Image.new("RGBA", (lw, lh), (0, 0, 0, 0))
    d = ImageDraw.Draw(layer)
    word_w = d.textlength(WORD, font=f) + 0.5 * PATTERN_SIZE * SS
    step_y = PATTERN_SIZE * SS * 1.3
    alpha = int(255 * PATTERN_ALPHA)
    row, k, y = 0, 0, -step_y
    while y < lh:
        x = -((row * 3.0 * PATTERN_SIZE * SS) % word_w) - word_w
        while x < lw:
            d.text((x, y), WORD, font=f, fill=(*WORD_COLOURS[k % len(WORD_COLOURS)], alpha))
            x += word_w
            k += 1
        k += 1                            # so colours don't line up vertically
        y += step_y
        row += 1
    layer = layer.rotate(PATTERN_ANGLE, resample=Image.BICUBIC)
    return layer.crop((pad, pad, pad + SW, pad + SH))


def tracked_text(d: ImageDraw.ImageDraw, xy, text, f, fill, tracking: float = 0.14) -> None:
    """Letter-spaced text, like the site's uppercase section labels."""
    x, y = xy
    for ch in text:
        d.text((x, y), ch, font=f, fill=fill)
        x += d.textlength(ch, font=f) + f.size * tracking


def build_poster(label: str, title: str, subtitle: str, out: Path) -> Path:
    c = Image.new("RGBA", (SW, SH), (*NAVY, 255))
    c.alpha_composite(word_pattern())
    shade = Image.new("RGBA", (SW, SH), (*NAVY, 255))
    # rotate(90) of the top-to-bottom gradient is 0 at left -> 255 at right; invert it.
    grad = ImageChops.invert(Image.linear_gradient("L").rotate(90)).resize((SW, SH))
    shade.putalpha(grad.point(lambda v: int(v * LEFT_SHADE)))
    c.alpha_composite(shade)

    d = ImageDraw.Draw(c)
    x, y = TEXT_X * SS, TEXT_Y * SS
    logo = Image.open(BRAND / "datos-insights" / "docrouter-logo-horizontal-white.png").convert("RGBA")
    lw = LOGO_W * SS
    logo = logo.resize((lw, int(logo.height * lw / logo.width)), Image.LANCZOS)
    c.alpha_composite(logo, (x, y))
    y += logo.height + 70 * SS

    fl = font("SemiBold", LABEL_SIZE)
    tracked_text(d, (x, y), label, fl, ORANGE)
    y += fl.size + 34 * SS

    ft = font("Bold", TITLE_SIZE)
    tw = d.textlength(title, font=ft)
    if tw > TITLE_MAX_W * SS:
        ft = font("Bold", TITLE_SIZE * TITLE_MAX_W * SS / tw)
    d.text((x, y), title, font=ft, fill=WHITE)
    y += int(ft.size * 1.32)

    d.text((x, y), subtitle, font=font("Medium", SUBTITLE_SIZE), fill=SUBTITLE_GREY)

    out.parent.mkdir(parents=True, exist_ok=True)
    c.convert("RGB").resize((W, H), Image.LANCZOS).save(out, quality=88, optimize=True, progressive=True)
    return out


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--label", required=True, help='small orange line, e.g. "PRODUCT DEMO  ·  3:40"')
    ap.add_argument("--title", required=True, help="main line (shrinks to fit if long)")
    ap.add_argument("--subtitle", required=True, help="one short line under the title")
    ap.add_argument("--out", type=Path, default=HERE / "poster.jpg", help="output JPEG (1920x1080)")
    args = ap.parse_args()
    print(build_poster(args.label, args.title, args.subtitle, args.out))


if __name__ == "__main__":
    main()

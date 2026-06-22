#!/usr/bin/env python3
"""Generate splash image for the DocRouter Flows blog post."""

from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H = 1376, 768
ROOT = Path(__file__).resolve().parents[1]
SCREENSHOT = Path(
    "/Users/andrei/.cursor/projects/Users-andrei-build-analytiq-docrouter-github-io"
    "/assets/Screenshot_2026-06-21_at_11.14.06_PM-9ff741ff-231e-4c56-903f-180bffb5a5db.png"
)
OUT = ROOT / "assets/images/docrouter-flows-splash.png"

FONT_BOLD = [
    "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
]
FONT_REGULAR = [
    "/System/Library/Fonts/Supplemental/Arial.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
]


def try_font(paths, size):
    for path in paths:
        try:
            return ImageFont.truetype(path, size)
        except OSError:
            pass
    return ImageFont.load_default()


def make_gradient():
    arr = np.zeros((H, W, 4), dtype=np.uint8)
    xs = np.linspace(0, 1, W)
    ys = np.linspace(0, 1, H)
    xg, yg = np.meshgrid(xs, ys)
    t = xg * 0.35 + yg * 0.65
    arr[:, :, 0] = (15 + t * (29 - 15)).astype(np.uint8)
    arr[:, :, 1] = (40 + t * (107 - 40)).astype(np.uint8)
    arr[:, :, 2] = (100 + t * (191 - 100)).astype(np.uint8)
    arr[:, :, 3] = 255
    return Image.fromarray(arr, "RGBA")


def rounded_rect_mask(size, radius):
    mask = Image.new("L", size, 0)
    draw = ImageDraw.Draw(mask)
    draw.rounded_rectangle([0, 0, size[0] - 1, size[1] - 1], radius=radius, fill=255)
    return mask


def draw_flow_icon(draw, cx, cy, size, alpha=170):
    color = (255, 255, 255, alpha)
    lw = max(3, size // 22)
    r = size * 0.14
    nodes = [
        (cx - size * 0.42, cy - size * 0.05),
        (cx - size * 0.08, cy - size * 0.28),
        (cx + size * 0.28, cy - size * 0.05),
        (cx + size * 0.08, cy + size * 0.28),
    ]
    for x, y in nodes:
        draw.ellipse([x - r, y - r, x + r, y + r], outline=color, width=lw)
    line_color = (255, 255, 255, int(alpha * 0.75))
    pairs = [(0, 1), (1, 2), (1, 3), (2, 3)]
    for a, b in pairs:
        draw.line([nodes[a][0], nodes[a][1], nodes[b][0], nodes[b][1]], fill=line_color, width=lw)


def wrap_text(draw, text, font, max_width):
    words = text.split()
    lines, current = [], []
    for word in words:
        trial = " ".join(current + [word])
        if draw.textbbox((0, 0), trial, font=font)[2] <= max_width:
            current.append(word)
        else:
            if current:
                lines.append(" ".join(current))
            current = [word]
    if current:
        lines.append(" ".join(current))
    return lines


def composite_screenshot(base, screenshot_path):
    shot = Image.open(screenshot_path).convert("RGBA")
    card_w, card_h = 720, 360
    pad = 18
    inner_w = card_w - pad * 2
    scale = inner_w / shot.width
    inner_h = int(shot.height * scale)
    shot = shot.resize((inner_w, inner_h), Image.Resampling.LANCZOS)

    card = Image.new("RGBA", (card_w, card_h), (0, 0, 0, 0))
    card_draw = ImageDraw.Draw(card)
    card_draw.rounded_rectangle(
        [0, 0, card_w - 1, card_h - 1],
        radius=22,
        fill=(255, 255, 255, 245),
    )

    shadow = Image.new("RGBA", (card_w + 40, card_h + 40), (0, 0, 0, 0))
    shadow_draw = ImageDraw.Draw(shadow)
    shadow_draw.rounded_rectangle(
        [20, 20, card_w + 19, card_h + 19],
        radius=22,
        fill=(0, 0, 0, 90),
    )
    shadow = shadow.filter(ImageFilter.GaussianBlur(12))

    card_x = W - card_w - 40
    card_y = (H - card_h) // 2
    base.alpha_composite(shadow, (card_x - 20, card_y - 12))
    base.alpha_composite(card, (card_x, card_y))

    shot_x = card_x + pad
    shot_y = card_y + (card_h - inner_h) // 2
    base.paste(shot, (shot_x, shot_y), shot)
    return base


def main():
    img = make_gradient()
    draw = ImageDraw.Draw(img)

    draw_flow_icon(draw, cx=130, cy=120, size=120, alpha=180)

    title_font = try_font(FONT_BOLD, 62)
    subtitle_font = try_font(FONT_REGULAR, 30)
    tagline_font = try_font(FONT_REGULAR, 26)

    text_x = 56
    text_max_w = 520
    text_y = 200

    title = "DocRouter Flows"
    draw.text((text_x, text_y), title, font=title_font, fill=(255, 255, 255, 255))

    bb = draw.textbbox((text_x, text_y), title, font=title_font)
    text_y = bb[3] + 18

    subtitle_lines = wrap_text(
        draw,
        "Visual Workflow Automation for Intelligent Document Processing",
        subtitle_font,
        text_max_w,
    )
    for line in subtitle_lines:
        draw.text((text_x, text_y), line, font=subtitle_font, fill=(230, 240, 255, 245))
        text_y = draw.textbbox((text_x, text_y), line, font=subtitle_font)[3] + 8

    text_y += 18
    tagline = "Visual workflows · triggers · LLM & OCR nodes"
    draw.text((text_x, text_y), tagline, font=tagline_font, fill=(180, 210, 255, 220))

    img = composite_screenshot(img, SCREENSHOT)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.convert("RGB").save(OUT, "PNG", optimize=True)
    print(f"Saved {OUT} ({W}x{H})")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Generate splash image for the Flow Durability blog post."""

from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H = 1376, 768
ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets/images/flow-durability-splash.png"

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


def draw_shield_icon(draw, cx, cy, size, alpha=180):
    color = (255, 255, 255, alpha)
    lw = max(3, size // 22)
    w, h = size * 0.42, size * 0.52
    top = cy - h * 0.55
    bottom = cy + h * 0.45
    points = [
        (cx, top),
        (cx + w, top + h * 0.18),
        (cx + w, bottom - h * 0.22),
        (cx, bottom),
        (cx - w, bottom - h * 0.22),
        (cx - w, top + h * 0.18),
    ]
    draw.polygon(points, outline=color, width=lw)
    draw.line([cx, top + h * 0.12, cx, bottom - h * 0.1], fill=color, width=lw)


def draw_temporal_panel(draw, x0, y0, w, h):
    label_font = try_font(FONT_BOLD, 22)
    small_font = try_font(FONT_REGULAR, 14)

    draw.rounded_rectangle(
        [x0, y0, x0 + w, y0 + h],
        radius=16,
        fill=(248, 250, 255, 255),
        outline=(191, 219, 254, 255),
        width=2,
    )
    draw.text((x0 + 18, y0 + 14), "Temporal", font=label_font, fill=(30, 64, 175, 255))
    draw.text(
        (x0 + 18, y0 + 42),
        "Event history replay",
        font=small_font,
        fill=(75, 85, 99, 255),
    )

    cx = x0 + w * 0.42
    top = y0 + 78
    event_h, gap = 22, 10
    events = ["task scheduled", "activity done", "timer fired", "worker died"]
    colors = [(59, 130, 246), (59, 130, 246), (59, 130, 246), (239, 68, 68)]
    for i, (label, color) in enumerate(zip(events, colors)):
        ey = top + i * (event_h + gap)
        draw.rounded_rectangle(
            [cx - 88, ey, cx + 88, ey + event_h],
            radius=8,
            fill=(*color, 28),
            outline=(*color, 180),
            width=2,
        )
        draw.text((cx - 78, ey + 4), label, font=small_font, fill=(31, 41, 55, 255))

    replay_x = x0 + w - 42
    draw.arc(
        [replay_x - 26, top - 8, replay_x + 26, top + 3 * (event_h + gap) + event_h + 8],
        200,
        340,
        fill=(37, 99, 235, 220),
        width=3,
    )
    draw.polygon(
        [
            (replay_x - 4, top + 8),
            (replay_x + 10, top + 8),
            (replay_x + 3, top - 2),
        ],
        fill=(37, 99, 235, 220),
    )


def draw_docrouter_panel(draw, x0, y0, w, h):
    label_font = try_font(FONT_BOLD, 22)
    small_font = try_font(FONT_REGULAR, 14)

    draw.rounded_rectangle(
        [x0, y0, x0 + w, y0 + h],
        radius=16,
        fill=(255, 251, 235, 255),
        outline=(253, 230, 138, 255),
        width=2,
    )
    draw.text((x0 + 18, y0 + 14), "DocRouter", font=label_font, fill=(180, 83, 9, 255))
    draw.text(
        (x0 + 18, y0 + 42),
        "Checkpoint resume",
        font=small_font,
        fill=(75, 85, 99, 255),
    )

    cy = y0 + h * 0.58
    node_r = 18
    nodes = [
        ("N1", (34, 180, 34)),
        ("N2", (34, 180, 34)),
        ("N3", (34, 180, 34)),
        ("N4", (239, 68, 68)),
    ]
    xs = [x0 + 42 + i * 58 for i in range(4)]

    for i in range(3):
        draw.line([xs[i] + node_r, cy, xs[i + 1] - node_r, cy], fill=(156, 163, 175, 255), width=3)

    for (label, color), nx in zip(nodes, xs):
        draw.ellipse(
            [nx - node_r, cy - node_r, nx + node_r, cy + node_r],
            fill=(*color, 36),
            outline=(*color, 220),
            width=2,
        )
        bb = draw.textbbox((0, 0), label, font=small_font)
        tw = bb[2] - bb[0]
        draw.text((nx - tw // 2, cy - 8), label, font=small_font, fill=(31, 41, 55, 255))

    for nx in xs[:3]:
        draw.line([nx - 6, cy + 28, nx, cy + 34], fill=(22, 163, 74, 255), width=3)
        draw.line([nx, cy + 34, nx + 8, cy + 24], fill=(22, 163, 74, 255), width=3)

    draw.line([xs[3] - 7, cy - 30, xs[3] + 7, cy - 16], fill=(220, 38, 38, 255), width=3)
    draw.line([xs[3] + 7, cy - 30, xs[3] - 7, cy - 16], fill=(220, 38, 38, 255), width=3)

    resume_y = cy + 52
    draw.line([xs[3], cy + node_r + 4, xs[3], resume_y - 8], fill=(37, 99, 235, 220), width=2)
    draw.polygon(
        [(xs[3] - 7, resume_y - 14), (xs[3] + 7, resume_y - 14), (xs[3], resume_y - 4)],
        fill=(37, 99, 235, 220),
    )
    draw.text((x0 + 18, resume_y + 2), "skip completed · redo N4", font=small_font, fill=(75, 85, 99, 255))


def draw_comparison_card(base):
    card_w, card_h = 760, 420
    card_x = W - card_w - 40
    card_y = (H - card_h) // 2

    shadow = Image.new("RGBA", (card_w + 40, card_h + 40), (0, 0, 0, 0))
    shadow_draw = ImageDraw.Draw(shadow)
    shadow_draw.rounded_rectangle(
        [20, 20, card_w + 19, card_h + 19],
        radius=24,
        fill=(0, 0, 0, 90),
    )
    shadow = shadow.filter(ImageFilter.GaussianBlur(12))
    base.alpha_composite(shadow, (card_x - 20, card_y - 12))

    card = Image.new("RGBA", (card_w, card_h), (0, 0, 0, 0))
    card_draw = ImageDraw.Draw(card)
    card_draw.rounded_rectangle(
        [0, 0, card_w - 1, card_h - 1],
        radius=24,
        fill=(255, 255, 255, 248),
    )

    header_font = try_font(FONT_BOLD, 24)
    card_draw.text((24, 20), "Worker dies mid-run", font=header_font, fill=(17, 24, 39, 255))

    panel_w = (card_w - 72) // 2
    panel_h = card_h - 88
    draw_temporal_panel(card_draw, 24, 64, panel_w, panel_h)
    draw_docrouter_panel(card_draw, 24 + panel_w + 24, 64, panel_w, panel_h)

    vs_font = try_font(FONT_BOLD, 20)
    card_draw.text((card_w // 2 - 10, card_h // 2 - 4), "vs", font=vs_font, fill=(107, 114, 128, 255))

    base.alpha_composite(card, (card_x, card_y))
    return base


def main():
    img = make_gradient()
    draw = ImageDraw.Draw(img)

    draw_shield_icon(draw, cx=130, cy=120, size=120, alpha=180)

    title_font = try_font(FONT_BOLD, 58)
    subtitle_font = try_font(FONT_REGULAR, 30)
    tagline_font = try_font(FONT_REGULAR, 26)

    text_x = 56
    text_max_w = 520
    text_y = 200

    title = "Flow Durability"
    draw.text((text_x, text_y), title, font=title_font, fill=(255, 255, 255, 255))

    bb = draw.textbbox((text_x, text_y), title, font=title_font)
    text_y = bb[3] + 18

    subtitle_lines = wrap_text(
        draw,
        "What Happens When a Worker Dies?",
        subtitle_font,
        text_max_w,
    )
    for line in subtitle_lines:
        draw.text((text_x, text_y), line, font=subtitle_font, fill=(230, 240, 255, 245))
        text_y = draw.textbbox((text_x, text_y), line, font=subtitle_font)[3] + 8

    text_y += 18
    tagline = "Temporal replay · DocRouter checkpoints"
    draw.text((text_x, text_y), tagline, font=tagline_font, fill=(180, 210, 255, 220))

    img = draw_comparison_card(img)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.convert("RGB").save(OUT, "PNG", optimize=True)
    print(f"Saved {OUT} ({W}x{H})")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Generate splash image for the mem0 blog post."""

from PIL import Image, ImageDraw, ImageFont
import math

W, H = 1376, 768

# Create gradient background (dark blue top-left to lighter blue bottom-right)
img = Image.new("RGBA", (W, H), (0, 0, 0, 255))
draw = ImageDraw.Draw(img)

# Blue gradient similar to existing splash images
# Top-left: #1a3a6b (dark navy blue), Bottom-right: #2563eb (bright blue)
for y in range(H):
    for x in range(W):
        t = (x / W * 0.4 + y / H * 0.6)  # blend factor
        r = int(15 + t * (37 - 15))
        g = int(40 + t * (99 - 40))
        b = int(100 + t * (235 - 100))
        draw.point((x, y), fill=(r, g, b, 255))

# Better approach: use numpy for speed
import numpy as np

arr = np.zeros((H, W, 4), dtype=np.uint8)
xs = np.linspace(0, 1, W)
ys = np.linspace(0, 1, H)
xg, yg = np.meshgrid(xs, ys)
t = xg * 0.35 + yg * 0.65

# Dark navy (#0f2864) to medium blue (#1d6bbf)
arr[:, :, 0] = (15 + t * (29 - 15)).astype(np.uint8)
arr[:, :, 1] = (40 + t * (107 - 40)).astype(np.uint8)
arr[:, :, 2] = (100 + t * (191 - 100)).astype(np.uint8)
arr[:, :, 3] = 255

img = Image.fromarray(arr, 'RGBA')
draw = ImageDraw.Draw(img)

# --- Draw icons ---

def draw_brain_icon(draw, cx, cy, size, alpha=180):
    """Draw a stylized brain/memory icon."""
    color = (255, 255, 255, alpha)
    # Simple rounded brain shape using ellipses
    lw = max(3, size // 20)
    # Left hemisphere
    draw.ellipse([cx - size*0.55, cy - size*0.4, cx + size*0.05, cy + size*0.3],
                 outline=color, width=lw)
    # Right hemisphere
    draw.ellipse([cx - size*0.05, cy - size*0.4, cx + size*0.55, cy + size*0.3],
                 outline=color, width=lw)
    # Center line
    draw.line([cx, cy - size*0.35, cx, cy + size*0.25], fill=color, width=lw)
    # Bottom stem
    draw.line([cx - size*0.1, cy + size*0.3, cx + size*0.1, cy + size*0.45],
              fill=color, width=lw)
    # Folds on left
    draw.arc([cx - size*0.45, cy - size*0.15, cx - size*0.1, cy + size*0.1],
             0, 180, fill=color, width=lw)
    # Folds on right
    draw.arc([cx + size*0.1, cy - size*0.15, cx + size*0.45, cy + size*0.1],
             0, 180, fill=color, width=lw)


def draw_database_icon(draw, cx, cy, size, alpha=180):
    """Draw a cylinder database icon."""
    color = (255, 255, 255, alpha)
    lw = max(3, size // 20)
    rx = size * 0.45
    ry = size * 0.12
    h = size * 0.6
    # Bottom ellipse
    draw.ellipse([cx - rx, cy + h/2 - ry, cx + rx, cy + h/2 + ry],
                 outline=color, width=lw)
    # Top ellipse
    draw.ellipse([cx - rx, cy - h/2 - ry, cx + rx, cy - h/2 + ry],
                 outline=color, width=lw)
    # Sides
    draw.line([cx - rx, cy - h/2, cx - rx, cy + h/2], fill=color, width=lw)
    draw.line([cx + rx, cy - h/2, cx + rx, cy + h/2], fill=color, width=lw)
    # Middle stripe
    mid_y = cy - h/6
    draw.ellipse([cx - rx, mid_y - ry, cx + rx, mid_y + ry],
                 outline=color, width=lw)


def draw_vector_dots(draw, cx, cy, size, alpha=150):
    """Draw scattered dots representing vectors/embeddings."""
    import random
    random.seed(42)
    color = (200, 230, 255, alpha)
    dot_r = max(2, size // 18)
    positions = [
        (-0.4, -0.35), (0.1, -0.45), (0.45, -0.2),
        (-0.2, 0.0),   (0.3, 0.1),   (-0.45, 0.3),
        (0.0, 0.4),    (0.4, 0.4),   (-0.1, -0.1),
    ]
    for dx, dy in positions:
        px = cx + dx * size
        py = cy + dy * size
        draw.ellipse([px - dot_r, py - dot_r, px + dot_r, py + dot_r],
                     fill=color)
    # Connect some dots
    line_color = (200, 230, 255, 80)
    pairs = [(0, 1), (1, 2), (0, 3), (3, 4), (3, 5), (6, 7), (3, 8)]
    pts = [(cx + dx * size, cy + dy * size) for dx, dy in positions]
    for a, b in pairs:
        draw.line([pts[a][0], pts[a][1], pts[b][0], pts[b][1]],
                  fill=line_color, width=max(1, size // 40))


# Top-right icon: database + vector dots
draw_database_icon(draw, cx=W - 160, cy=130, size=110, alpha=180)
draw_vector_dots(draw, cx=W - 120, cy=240, size=90, alpha=160)

# --- Text ---
# Try to load system fonts
def try_font(paths, size):
    for p in paths:
        try:
            return ImageFont.truetype(p, size)
        except Exception:
            pass
    return ImageFont.load_default()

bold_paths = [
    "/usr/share/fonts/liberation/LiberationSans-Bold.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf",
    "/usr/share/fonts/dejavu/DejaVuSans-Bold.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
]
regular_paths = [
    "/usr/share/fonts/liberation/LiberationSans-Regular.ttf",
    "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf",
    "/usr/share/fonts/dejavu/DejaVuSans.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
]

title_font = try_font(bold_paths, 64)
subtitle_font = try_font(regular_paths, 38)

# Title: two lines
line1 = "How AI Agent Memory Works"
line2 = "(and How We Integrated Mem0)"

# Center of text area (shifted slightly left to account for icons)
text_cx = W // 2 + 10
text_cy = H // 2 - 30

# Draw title line 1
bb1 = draw.textbbox((0, 0), line1, font=title_font)
tw1, th1 = bb1[2] - bb1[0], bb1[3] - bb1[1]
draw.text((text_cx - tw1 // 2, text_cy - th1 - 8), line1,
          font=title_font, fill=(255, 255, 255, 255))

# Draw title line 2 (slightly smaller)
title2_font = try_font(bold_paths, 58)
bb2 = draw.textbbox((0, 0), line2, font=title2_font)
tw2, th2 = bb2[2] - bb2[0], bb2[3] - bb2[1]
draw.text((text_cx - tw2 // 2, text_cy + 8), line2,
          font=title2_font, fill=(255, 255, 255, 255))

# Subtitle
subtitle = "Async ingestion · reconciliation · retrieval"
bb3 = draw.textbbox((0, 0), subtitle, font=subtitle_font)
tw3 = bb3[2] - bb3[0]
subtitle_y = text_cy + th2 + 30
draw.text((text_cx - tw3 // 2, subtitle_y), subtitle,
          font=subtitle_font, fill=(180, 210, 255, 220))

# Save
out_path = "/home/andrei/build/analytiq/docrouter.github.io/assets/images/mem0-integration-splash.png"
img = img.convert("RGB")
img.save(out_path, "PNG", optimize=True)
print(f"Saved {out_path} ({W}x{H})")

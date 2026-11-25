"""Splash image for the "How the Flows Code Node Sandboxes Python" post.

Reuses the palette and drawing helpers from build-index-once-images.py so the
two heroes read as one series. Icons are rendered with headless Chrome (set CHROME
to its path if it is not in the default macOS location). Run from the repo root:

    python3 _brand/build-code-sandbox-images.py
"""

import importlib.util
import os
import subprocess
import tempfile
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

_spec = importlib.util.spec_from_file_location(
    "index_once", Path(__file__).with_name("build-index-once-images.py")
)
io_ = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(io_)

OUT, LOGO = io_.OUT, io_.LOGO
BG, WHITE, NAVY, BLUE = io_.BG, io_.WHITE, io_.NAVY, io_.BLUE
PALE, LIGHT, MUTED = io_.PALE, io_.LIGHT, io_.MUTED
RED, RED_BG = io_.RED, io_.RED_BG
font, rr, centered, label = io_.font, io_.rr, io_.centered, io_.label

_MONO_CANDIDATES = (
    "/System/Library/Fonts/Menlo.ttc",
    "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
)


def mono(size):
    for path in _MONO_CANDIDATES:
        if Path(path).exists():
            return ImageFont.truetype(path, size)
    return font(size)


def badge(draw, box, prefix, emphasis):
    x0, y0, x1, y1 = box
    rr(draw, box, 30, fill=WHITE, outline=PALE, width=2)
    cy = (y0 + y1) / 2
    draw.ellipse((x0 + 16, cy - 9, x0 + 34, cy + 9), outline="#FF6B4A", width=3)
    draw.ellipse((x0 + 22, cy - 3, x0 + 28, cy + 3), fill="#FF6B4A")
    f = font(22)
    pw = draw.textlength(prefix, font=f)
    total = pw + draw.textlength(emphasis, font=f)
    left = (x0 + 40 + x1) / 2 - total / 2
    draw.text((left, cy), prefix, font=f, fill=BLUE, anchor="lm")
    draw.text((left + pw, cy), emphasis, font=f, fill=NAVY, anchor="lm")


def shield(draw, cx, cy, size=30, fill=BLUE):
    """Small shield marking the sandbox boundary."""
    s = size
    draw.polygon(
        [
            (cx, cy - s),
            (cx + s * 0.85, cy - s * 0.62),
            (cx + s * 0.78, cy + s * 0.25),
            (cx, cy + s),
            (cx - s * 0.78, cy + s * 0.25),
            (cx - s * 0.85, cy - s * 0.62),
        ],
        fill=fill,
    )
    draw.line(
        (cx - s * 0.36, cy, cx - s * 0.06, cy + s * 0.3, cx + s * 0.42, cy - s * 0.28),
        fill=WHITE,
        width=max(3, round(s / 7)),
        joint="curve",
    )


CODE_LINES = (
    (("def ", BLUE), ("run", NAVY), ("(items, context):", MUTED)),
    (("    writer = ", NAVY), ("PdfWriter", BLUE), ("()", MUTED)),
    (("    for ", BLUE), ("it ", NAVY), ("in ", BLUE), ("items:", NAVY)),
    (("        writer.append(...)", MUTED),),
    (("    return ", BLUE), ("[merged]", NAVY)),
)


CODE_LINES_NODE = CODE_LINES[:4] + (
    (("    sid = ", NAVY), ("store_binary", BLUE), ("(...)", MUTED)),
) + CODE_LINES[4:]


def code_lines(draw, x, y, size=19, step=27, lines=CODE_LINES):
    m = mono(size)
    for row, parts in enumerate(lines):
        cx = x
        for text, color in parts:
            draw.text((cx, y + row * step), text, font=m, fill=color)
            cx += draw.textlength(text, font=m)


def blocked(draw, cx, cy, text, width=168):
    rr(draw, (cx - width / 2, cy - 22, cx + width / 2, cy + 22), 22, fill=RED_BG, outline="#F0C8C3")
    content = 18 + 18 + draw.textlength(text, font=font(15))
    x = cx - content / 2 + 9
    draw.ellipse((x - 9, cy - 9, x + 9, cy + 9), outline=RED, width=3)
    draw.line((x - 6, cy + 6, x + 6, cy - 6), fill=RED, width=3)
    draw.text((x + 18, cy), text, font=font(15), fill=RED, anchor="lm")


# Nodes and edges are drawn like the DocRouter Flows canvas. Values below come from packages/typescript/frontend/src/components/flows in doc-router:
# FlowCanvasNode.tsx (96px body, rounded-xl, border #d2d6dc, trigger rounded-l-[36px], label
# text-sm #1a1d21 + text-xs gray-500), handle class (10px, 2px #d0d5dd, white), FlowCanvasEdge.tsx
# (stroke #a8b0bd 1.5px, ArrowClosed 10px, "N items" 11px #5a6270), flowNodeBrand.ts (DocRouter
# icons primary-600 #0754a6, other process icons #94a3b8), FlowEditor <Background> dots #b8c0cc /
# 24px. Icons are the same Heroicons (24/solid) the canvas renders.

S = 1.5  # canvas px → splash px
NODE = round(96 * S)
NODE_BORDER = "#d2d6dc"
HANDLE_BORDER = "#d0d5dd"
EDGE = "#a8b0bd"
EDGE_LABEL = "#5a6270"
NODE_TITLE = "#1a1d21"
NODE_SUB = "#6b7280"
DOT = "#b8c0cc"
PRIMARY_600 = "#0754a6"
PROCESS_ICON = "#94a3b8"
TRIGGER_ICON = "#a8b0ba"  # non-DocRouter trigger glyph

HEROICONS = {
    "code_bracket_square": (
        '<path fill-rule="evenodd" clip-rule="evenodd" d="M3 6a3 3 0 0 1 3-3h12a3 3 0 0 1 3 3v12a3 3 0 0 1-3 3H6a3 3 0 0 1-3-3V6Zm14.25 6a.75.75 0 0 1-.22.53l-2.25 2.25a.75.75 0 1 1-1.06-1.06L15.44 12l-1.72-1.72a.75.75 0 1 1 1.06-1.06l2.25 2.25c.141.14.22.331.22.53Zm-10.28-.53a.75.75 0 0 0 0 1.06l2.25 2.25a.75.75 0 1 0 1.06-1.06L8.56 12l1.72-1.72a.75.75 0 1 0-1.06-1.06l-2.25 2.25Z"/>'
    ),
    "globe_alt": (
        '<path d="M21.721 12.752a9.711 9.711 0 0 0-.945-5.003 12.754 12.754 0 0 1-4.339 2.708 18.991 18.991 0 0 1-.214 4.772 17.165 17.165 0 0 0 5.498-2.477ZM14.634 15.55a17.324 17.324 0 0 0 .332-4.647c-.952.227-1.945.347-2.966.347-1.021 0-2.014-.12-2.966-.347a17.515 17.515 0 0 0 .332 4.647 17.385 17.385 0 0 0 5.268 0ZM9.772 17.119a18.963 18.963 0 0 0 4.456 0A17.182 17.182 0 0 1 12 21.724a17.18 17.18 0 0 1-2.228-4.605ZM7.777 15.23a18.87 18.87 0 0 1-.214-4.774 12.753 12.753 0 0 1-4.34-2.708 9.711 9.711 0 0 0-.944 5.004 17.165 17.165 0 0 0 5.498 2.477ZM21.356 14.752a9.765 9.765 0 0 1-7.478 6.817 18.64 18.64 0 0 0 1.988-4.718 18.627 18.627 0 0 0 5.49-2.098ZM2.644 14.752c1.682.971 3.53 1.688 5.49 2.099a18.64 18.64 0 0 0 1.988 4.718 9.765 9.765 0 0 1-7.478-6.816ZM13.878 2.43a9.755 9.755 0 0 1 6.116 3.986 11.267 11.267 0 0 1-3.746 2.504 18.63 18.63 0 0 0-2.37-6.49ZM12 2.276a17.152 17.152 0 0 1 2.805 7.121c-.897.23-1.837.353-2.805.353-.968 0-1.908-.122-2.805-.353A17.151 17.151 0 0 1 12 2.276ZM10.122 2.43a18.629 18.629 0 0 0-2.37 6.49 11.266 11.266 0 0 1-3.746-2.504 9.754 9.754 0 0 1 6.116-3.985Z"/>'
    ),
    "bolt": (
        '<path fill-rule="evenodd" clip-rule="evenodd" d="M14.615 1.595a.75.75 0 0 1 .359.852L12.982 9.75h7.268a.75.75 0 0 1 .548 1.262l-10.5 11.25a.75.75 0 0 1-1.272-.71l1.992-7.302H3.75a.75.75 0 0 1-.548-1.262l10.5-11.25a.75.75 0 0 1 .913-.143Z"/>'
    ),
}

CHROME = os.environ.get(
    "CHROME", "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
)
_ICON_CACHE = {}


def heroicon(name, size, color):
    """Rasterize a Heroicon with headless Chrome (Pillow has no SVG renderer)."""
    key = (name, size, color)
    if key in _ICON_CACHE:
        return _ICON_CACHE[key]
    with tempfile.TemporaryDirectory() as tmp:
        svg = Path(tmp) / "icon.svg"
        png = Path(tmp) / "icon.png"
        svg.write_text(
            f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="{size}" '
            f'height="{size}" fill="{color}">{HEROICONS[name]}</svg>',
            encoding="utf-8",
        )
        subprocess.run(
            [
                CHROME,
                "--headless=new",
                "--disable-gpu",
                "--hide-scrollbars",
                "--force-device-scale-factor=1",
                "--default-background-color=00000000",
                f"--window-size={size},{size}",
                f"--screenshot={png}",
                svg.as_uri(),
            ],
            check=True,
            capture_output=True,
        )
        icon = Image.open(png).convert("RGBA").crop((0, 0, size, size))
        icon.load()
    _ICON_CACHE[key] = icon
    return icon


def paste_icon(image, name, size, color, cx, cy):
    icon = heroicon(name, size, color)
    image.paste(icon, (round(cx - size / 2), round(cy - size / 2)), icon)


def canvas_dots(draw, box):
    x0, y0, x1, y1 = box
    gap = round(24 * S)
    r = 1.2 * S / 2 + 0.6
    for y in range(y0, y1, gap):
        for x in range(x0, x1, gap):
            draw.ellipse((x - r, y - r, x + r, y + r), fill=DOT)


def handle(draw, cx, cy):
    r = 5 * S
    draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill=WHITE, outline=HANDLE_BORDER, width=round(2 * S))


def text_on_bg(draw, xy, text, size, fill, bg, anchor="mm"):
    """Text on a patch of background, so canvas dots never run through it."""
    f = font(size)
    l, t, r, b = draw.textbbox(xy, text, font=f, anchor=anchor)
    draw.rectangle((l - 8, t - 5, r + 8, b + 5), fill=bg)
    draw.text(xy, text, font=f, fill=fill, anchor=anchor)


def flow_node(image, draw, cx, cy, icon, icon_color, title, subtitle, trigger=False, inputs=True, bg=BG):
    x0, y0 = cx - NODE / 2, cy - NODE / 2
    x1, y1 = x0 + NODE, y0 + NODE
    width = max(2, round(1 * S))
    if trigger:
        # rounded-l-[36px] rounded-r-xl: draw the left pill and right rounded box, then the outline.
        rl, rr_ = round(36 * S), round(12 * S)
        mask = Image.new("L", image.size, 0)
        md = ImageDraw.Draw(mask)
        md.rounded_rectangle((x0, y0, x1 - NODE / 2 + rl, y1), radius=rl, fill=255)
        md.rounded_rectangle((x0 + NODE / 2 - rr_, y0, x1, y1), radius=rr_, fill=255)
        md.rectangle((x0 + rl, y0, x1 - rr_, y1), fill=255)
        inner = Image.new("L", image.size, 0)
        idr = ImageDraw.Draw(inner)
        idr.rounded_rectangle((x0 + width, y0 + width, x1 - NODE / 2 + rl - width, y1 - width), radius=rl - width, fill=255)
        idr.rounded_rectangle((x0 + NODE / 2 - rr_ + width, y0 + width, x1 - width, y1 - width), radius=rr_ - width, fill=255)
        idr.rectangle((x0 + rl, y0 + width, x1 - rr_, y1 - width), fill=255)
        image.paste(Image.new("RGB", image.size, NODE_BORDER), (0, 0), mask)
        image.paste(Image.new("RGB", image.size, WHITE), (0, 0), inner)
        paste_icon(image, "bolt", round(20 * S), PRIMARY_600, x0 - 14 * S, cy)
    else:
        draw.rounded_rectangle((x0, y0, x1, y1), radius=round(12 * S), fill=WHITE, outline=NODE_BORDER, width=width)
    paste_icon(image, icon, round(40 * S), icon_color, cx, cy)
    if inputs:
        handle(draw, x0, cy)
    handle(draw, x1, cy)
    text_on_bg(draw, (cx, y1 + 16 * S + 11), title, round(14 * S), NODE_TITLE, bg)
    text_on_bg(draw, (cx, y1 + 16 * S + 38), subtitle, round(12 * S), NODE_SUB, bg)
    return (x0, y0, x1, y1)


PLUS_BORDER = "#c5cad3"
PLUS_FILL = "#f4f5f6"
PLUS_ICON = "#374151"


def plus_button(draw, cx, cy):
    """FlowCanvasAppendPlusButton: h-7 w-7 rounded, border #c5cad3, bg #f4f5f6, PlusIcon 14px."""
    half = 28 * S / 2
    # shadow-sm
    draw.rounded_rectangle(
        (cx - half, cy - half + 2, cx + half, cy + half + 2), radius=round(4 * S), fill="#e5e8ec"
    )
    draw.rounded_rectangle(
        (cx - half, cy - half, cx + half, cy + half),
        radius=round(4 * S),
        fill=PLUS_FILL,
        outline=PLUS_BORDER,
        width=max(2, round(1 * S)),
    )
    arm = 14 * S * 7.5 / 24  # PlusIcon: M12 4.5v15 m7.5-7.5h-15 in a 24 box
    w = max(3, round(2 * 14 * S / 24 + 0.5))
    draw.line((cx - arm, cy, cx + arm, cy), fill=PLUS_ICON, width=w)
    draw.line((cx, cy - arm, cx, cy + arm), fill=PLUS_ICON, width=w)


def append_stub(draw, x, cy):
    """Output port with no edge: a short line and the + button, as on the canvas."""
    line_end = x + 6 * S + 16 * S
    draw.line((x + 6 * S, cy, line_end, cy), fill=PLUS_BORDER, width=max(2, round(1 * S)))
    plus_button(draw, line_end + 4 * S + 14 * S, cy)


def flow_edge(draw, start, end, items, mid_x=None, bg=BG):
    """Straight canvas edge: ArrowClosed marker, mid-edge + button, item count above it."""
    (sx, sy), (tx, ty) = start, end
    arrow = 10 * S
    draw.line((sx, sy, tx - arrow + 1, ty), fill=EDGE, width=round(1.5 * S + 0.5))
    draw.polygon([(tx, ty), (tx - arrow, ty - arrow / 2), (tx - arrow, ty + arrow / 2)], fill=EDGE)
    x = (sx + tx) / 2 if mid_x is None else mid_x
    plus_button(draw, x, sy)
    text = f"{items} item{'' if items == 1 else 's'}"
    text_on_bg(draw, (x, sy - 14 * S - 10), text, round(11 * S), EDGE_LABEL, bg, anchor="ms")


def code_node(image, draw, cx, cy, width, height, title, subtitle, bg, top=None):
    """The Code node as a canvas node whose body is its code. Ports sit at ``cy``."""
    x0 = cx - width / 2
    y0 = cy - height / 2 if top is None else top
    x1, y1 = x0 + width, y0 + height
    draw.rounded_rectangle(
        (x0, y0, x1, y1), radius=round(12 * S), fill=WHITE, outline=NODE_BORDER, width=max(2, round(1 * S))
    )
    paste_icon(image, "code_bracket_square", 34, PROCESS_ICON, x0 + 36, y0 + 34)
    label(draw, (x1 - 26, y0 + 34), "PYTHON", 15, MUTED, "rm")
    draw.line((x0 + 20, y0 + 64, x1 - 20, y0 + 64), fill="#EEF1F4", width=2)
    code_lines(draw, x0 + 30, y0 + 84, size=21, step=30, lines=CODE_LINES_NODE)
    handle(draw, x0, cy)
    handle(draw, x1, cy)
    text_on_bg(draw, (cx, y1 + 16 * S + 11), title, round(14 * S), NODE_TITLE, bg)
    text_on_bg(draw, (cx, y1 + 16 * S + 38), subtitle, round(12 * S), NODE_SUB, bg)
    return (x0, y0, x1, y1)


def no_access_row(draw, cy, cx=800, pill=196, gap=18):
    """'NO ACCESS TO' followed by the four blocked pills, centered as one row."""
    lead = "NO ACCESS TO"
    f = font(20)
    lead_w = draw.textlength(lead, font=f)
    items = ("HOST FILES", "NETWORK", "ENV VARS", "PROCESSES")
    total = lead_w + 26 + len(items) * pill + (len(items) - 1) * gap
    x = cx - total / 2
    draw.text((x, cy), lead, font=f, fill=RED, anchor="lm")
    x += lead_w + 26
    for text in items:
        blocked(draw, x + pill / 2, cy, text, pill)
        x += pill + gap


def make_hero():
    image = Image.new("RGB", (1600, 900), BG)
    draw = ImageDraw.Draw(image)
    for y in range(54, 900, 72):
        draw.line((0, y, 1600, y), fill="#F0F6FC", width=1)

    with Image.open(LOGO) as source_logo:
        logo = source_logo.resize((360, 63), Image.Resampling.LANCZOS)
        image.paste(logo, (90, 46), logo)
    badge(draw, (90, 132, 450, 198), "IN FOCUS: ", "FLOWS")
    title, subtitle = "SANDBOXED PYTHON.", "Every Code node runs in its own sandbox."
    # Left-aligned block whose widest line ends at the right margin.
    tx = 1520 - max(draw.textlength(title, font=font(70)), draw.textlength(subtitle, font=font(37)))
    draw.text((tx, 46), title, font=font(70), fill=NAVY)
    draw.text((tx, 130), subtitle, font=font(37), fill=BLUE)

    # Canvas dots behind the flow, outside the sandbox.
    canvas_dots(draw, (60, 250, 1560, 810))

    row = 492
    sx0, sy0, sx1, sy1 = 500, 284, 1100, 806
    rr(draw, (sx0, sy0, sx1, sy1), 36, fill=LIGHT, outline=BLUE, width=4)
    rr(draw, (sx0 + 34, sy0 - 22, sx0 + 360, sy0 + 22), 22, fill=BLUE, outline=BLUE)
    centered(draw, (sx0 + 197, sy0), "WEBASSEMBLY SANDBOX", 17, WHITE)
    shield(draw, sx1 - 54, sy0 + 54, 26)

    trig = flow_node(
        image, draw, 210, row, "globe_alt", TRIGGER_ICON,
        "Webhook", "Trigger", trigger=True, inputs=False,
    )
    code = code_node(image, draw, 800, row, 460, 296, "Code Node", "Python (WASI)", LIGHT, top=362)
    http = flow_node(
        image, draw, 1330, row, "globe_alt", PROCESS_ICON,
        "HTTP Request", "Upload results",
    )
    handle_r = 5 * S
    # The + and item count sit on the part of each edge outside the sandbox.
    flow_edge(draw, (trig[2] + handle_r, row), (code[0] - handle_r, row), 13, mid_x=(trig[2] + sx0) / 2)
    flow_edge(draw, (code[2] + handle_r, row), (http[0] - handle_r, row), 4, mid_x=(sx1 + http[0]) / 2)
    append_stub(draw, http[2], row)
    # Redraw handles over the edge ends.
    for x in (trig[2], code[0], code[2], http[0], http[2]):
        handle(draw, x, row)

    label(draw, ((sx0 + sx1) / 2, sy1 - 24), "CPYTHON · WASI · STDLIB + PYPDF · 256 MB", 14, MUTED)

    no_access_row(draw, 858)

    image.save(OUT / "flows-code-sandbox-splash.png", optimize=True)


if __name__ == "__main__":
    make_hero()
    path = OUT / "flows-code-sandbox-splash.png"
    with Image.open(path) as image:
        print(path.name, image.size, path.stat().st_size)

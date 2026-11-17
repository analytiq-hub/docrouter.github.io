from pathlib import Path

from PIL import Image, ImageDraw, ImageFont


OUT = Path(__file__).parents[1] / "assets" / "images"
FONT = Path(__file__).parent / "fonts" / "IBM-Plex-Sans-SemiBold.ttf"
LOGO = (
    Path(__file__).parent
    / "datos-insights"
    / "docrouter-logo-horizontal-color.png"
)

BG = "#F8FBFF"
WHITE = "#FFFFFF"
NAVY = "#172554"
BLUE = "#0B63CE"
PALE = "#CFE6FF"
LIGHT = "#EAF4FF"
MUTED = "#64748B"
LINE = "#93C5FD"
RED = "#D85B50"
RED_BG = "#FFF3F1"
GREEN = "#0F8A6A"

FONTS = {}


def font(size):
    FONTS.setdefault(size, ImageFont.truetype(FONT, size))
    return FONTS[size]


def rr(draw, box, radius, fill=WHITE, outline=PALE, width=2):
    draw.rounded_rectangle(
        box, radius=radius, fill=fill, outline=outline, width=width
    )


def centered(draw, xy, text, size, fill=NAVY):
    draw.text(xy, text, font=font(size), fill=fill, anchor="mm")


def label(draw, xy, text, size=22, fill=MUTED, anchor="mm"):
    draw.text(xy, text.upper(), font=font(size), fill=fill, anchor=anchor)


def curve(draw, points, fill=LINE, width=4, dashed=False):
    p0, p1, p2, p3 = points
    sampled = []
    for index in range(81):
        t = index / 80
        u = 1 - t
        sampled.append(
            (
                u**3 * p0[0]
                + 3 * u * u * t * p1[0]
                + 3 * u * t * t * p2[0]
                + t**3 * p3[0],
                u**3 * p0[1]
                + 3 * u * u * t * p1[1]
                + 3 * u * t * t * p2[1]
                + t**3 * p3[1],
            )
        )
    if dashed:
        for index in range(0, len(sampled) - 1, 4):
            draw.line(sampled[index : min(index + 3, len(sampled))], fill=fill, width=width)
        if (len(sampled) - 1) % 4:
            draw.line(sampled[-((len(sampled) - 1) % 4 + 1) :], fill=fill, width=width)
    else:
        draw.line(sampled, fill=fill, width=width, joint="curve")


def document(
    draw, x, y, width=104, height=136, color=BLUE, fill=WHITE, shadow=True
):
    if shadow:
        rr(
            draw,
            (x + 8, y + 9, x + width + 8, y + height + 9),
            14,
            fill="#E8F1FB",
            outline="#E8F1FB",
            width=1,
        )
    rr(
        draw,
        (x, y, x + width, y + height),
        14,
        fill=fill,
        outline=PALE,
        width=3,
    )
    draw.line(
        (x + width - 30, y, x + width - 30, y + 30, x + width, y + 30),
        fill=color,
        width=3,
    )
    draw.line((x + width - 30, y, x + width, y + 30), fill=color, width=3)
    draw.line((x + 20, y + 62, x + width - 20, y + 62), fill=color, width=4)
    draw.line((x + 20, y + 82, x + width - 32, y + 82), fill=LINE, width=4)
    draw.line((x + 20, y + 102, x + width - 25, y + 102), fill=LINE, width=4)


def index_icon(draw, cx, cy, radius=82):
    scale = radius / 82
    draw.ellipse(
        (cx - radius, cy - radius, cx + radius, cy + radius),
        fill=BLUE,
        outline=BLUE,
    )
    points = [
        (cx + offset_x * scale, cy + offset_y * scale)
        for offset_x, offset_y in (
            (-38, -26),
            (4, -44),
            (42, -14),
            (-25, 31),
            (28, 38),
        )
    ]
    line_width = max(3, round(7 * scale))
    node = max(4, round(10 * scale))
    for start, end in ((0, 1), (1, 2), (0, 3), (3, 4), (2, 4)):
        draw.line((*points[start], *points[end]), fill="#A9D2FF", width=line_width)
    for x, y in points:
        draw.ellipse((x - node, y - node, x + node, y + node), fill=WHITE)


def agent(draw, x, y, title, width=270, height=118):
    rr(
        draw,
        (x, y, x + width, y + height),
        24,
        fill=WHITE,
        outline=PALE,
        width=3,
    )
    draw.ellipse((x + 22, y + 26, x + 76, y + 80), outline=BLUE, width=4)
    draw.line((x + 49, y + 40, x + 49, y + 68), fill=BLUE, width=4)
    draw.ellipse((x + 43, y + 34, x + 55, y + 46), fill=WHITE, outline=BLUE, width=3)
    draw.line((x + 49, y + 55, x + 62, y + 46), fill=BLUE, width=4)
    centered(draw, (x + 171, y + 50), title, 24)
    label(draw, (x + 171, y + 80), "AGENT", 16)


def make_hero():
    image = Image.new("RGB", (1600, 900), BG)
    draw = ImageDraw.Draw(image)
    for y in range(54, 900, 72):
        draw.line((0, y, 1600, y), fill="#F0F6FC", width=1)

    with Image.open(LOGO) as source_logo:
        logo = source_logo.resize((360, 63), Image.Resampling.LANCZOS)
        image.paste(logo, (90, 46), logo)

    rr(
        draw,
        (90, 132, 450, 198),
        30,
        fill=WHITE,
        outline=PALE,
        width=2,
    )
    draw.ellipse((106, 156, 124, 174), outline="#FF6B4A", width=3)
    draw.ellipse((112, 162, 118, 168), fill="#FF6B4A")
    badge_font = font(22)
    prefix = "IN FOCUS: "
    emphasis = "INSURANCE"
    prefix_width = draw.textlength(prefix, font=badge_font)
    total_width = prefix_width + draw.textlength(emphasis, font=badge_font)
    badge_left = 290 - total_width / 2
    draw.text(
        (badge_left, 165),
        prefix,
        font=badge_font,
        fill=BLUE,
        anchor="lm",
    )
    draw.text(
        (badge_left + prefix_width, 165),
        emphasis,
        font=badge_font,
        fill=NAVY,
        anchor="lm",
    )

    draw.text((880, 46), "INDEX ONCE.", font=font(70), fill=NAVY)
    draw.text((880, 126), "Let every agent use it.", font=font(42), fill=BLUE)

    for offset in (38, 19, 0):
        document(draw, 110 + offset, 442 - offset, 140, 184, shadow=False)
    label(draw, (198, 686), "DOCUMENT STORE", 20, NAVY)

    for y in (475, 535, 595):
        curve(
            draw,
            ((300, y), (430, y), (440, 500), (560, 500)),
            dashed=True,
        )
    index_icon(draw, 690, 520, 100)
    centered(draw, (690, 658), "DOCROUTER INDEX", 22)

    for start_y, end_y in ((480, 390), (520, 520), (560, 650)):
        curve(
            draw,
            ((790, start_y), (920, start_y), (930, end_y), (1050, end_y)),
            dashed=True,
        )
    agent(draw, 1050, 330, "Claims")
    agent(draw, 1100, 470, "Underwriting")
    agent(draw, 1050, 610, "Recovery")

    image.save(OUT / "index-once-hero.png", optimize=True)


def make_architecture():
    image = Image.new("RGB", (1600, 1000), BG)
    draw = ImageDraw.Draw(image)
    label(draw, (88, 62), "SHARED EVIDENCE ARCHITECTURE", 18, BLUE, "lm")
    draw.text(
        (88, 98), "Stop rebuilding the document pipeline.", font=font(50), fill=NAVY
    )

    rr(draw, (70, 190, 1530, 490), 34, outline="#F1D4D0", width=3)
    label(draw, (110, 230), "BEFORE", 20, RED, "lm")
    for index in range(3):
        document(
            draw,
            125 + index * 32,
            280 - index * 12,
            72,
            94,
            color=MUTED,
            shadow=False,
        )
    label(draw, (200, 430), "DOCUMENT STORE", 17)

    for name, y in (("CLAIMS", 250), ("UNDERWRITING", 330), ("RECOVERY", 410)):
        curve(
            draw,
            ((300, 350), (410, 350), (430, y + 7), (515, y + 7)),
            fill="#E7AAA3",
            width=3,
            dashed=True,
        )
        for index, text in enumerate(("OCR", "EXTRACT", "SUMMARIZE")):
            x = 525 + index * 180
            rr(
                draw,
                (x, y - 25, x + 145, y + 39),
                16,
                fill=RED_BG,
                outline="#F0C8C3",
            )
            centered(draw, (x + 72, y + 7), text, 16, RED)
            if index < 2:
                draw.line((x + 145, y + 7, x + 180, y + 7), fill="#E7AAA3", width=3)
        rr(draw, (1085, y - 25, 1325, y + 39), 16, outline="#F0C8C3")
        centered(draw, (1205, y + 7), name, 18)
    label(draw, (1420, 350), "3×", 50, RED)
    label(draw, (1420, 392), "REPEATED", 16, RED)

    rr(draw, (70, 540, 1530, 930), 34, outline=PALE, width=3)
    label(draw, (110, 582), "AFTER", 20, GREEN, "lm")
    for index in range(3):
        document(
            draw,
            125 + index * 32,
            675 - index * 12,
            72,
            94,
            shadow=False,
        )
    label(draw, (200, 824), "DOCUMENT STORE", 17)
    curve(draw, ((300, 730), (420, 730), (430, 730), (535, 730)), dashed=True)
    rr(draw, (540, 645, 905, 815), 30, fill=LIGHT, outline=BLUE, width=3)
    index_icon(draw, 625, 730, 52)
    centered(draw, (785, 702), "SHARED INDEX", 24)
    centered(draw, (785, 742), "OCR • EXTRACT • ORGANIZE", 15, BLUE)
    centered(draw, (785, 774), "PAGE-LEVEL EVIDENCE", 15, MUTED)

    for y, name in ((630, "CLAIMS"), (730, "UNDERWRITING"), (830, "RECOVERY")):
        curve(
            draw,
            ((905, 730), (1010, 730), (1020, y), (1100, y)),
            dashed=True,
        )
        rr(draw, (1105, y - 35, 1390, y + 35), 18)
        centered(draw, (1248, y), name, 19)
    label(draw, (1450, 730), "1×", 50, GREEN)
    label(draw, (1450, 772), "PREPARED", 16, GREEN)

    image.save(OUT / "index-once-shared-architecture.png", optimize=True)


def system_of_record(draw, cx, cy):
    """Cylinder icon for a core system of record."""
    width, height = 92, 78
    left, top = cx - width / 2, cy - height / 2
    right, bottom = left + width, top + height
    draw.ellipse((left, top + 46, right, bottom), fill=LIGHT, outline=BLUE, width=3)
    draw.rectangle((left, top + 16, right, top + 62), fill=LIGHT)
    draw.line((left, top + 16, left, top + 62), fill=BLUE, width=3)
    draw.line((right, top + 16, right, top + 62), fill=BLUE, width=3)
    draw.ellipse((left, top, right, top + 32), fill=WHITE, outline=BLUE, width=3)
    draw.arc((left, top + 18, right, top + 50), 0, 180, fill=LINE, width=3)


def data_lake(draw, x, y, width=86, height=62):
    """Layered store, distinct from a single document stack."""
    for offset, tone in ((16, "#D7E9FF"), (8, LIGHT), (0, WHITE)):
        rr(
            draw,
            (x + offset, y - offset, x + width + offset, y + height - offset),
            10,
            fill=tone,
            outline=BLUE,
            width=2,
        )
    draw.line((x + 16, y + 24, x + width - 16, y + 24), fill=LINE, width=3)
    draw.line((x + 16, y + 40, x + width - 28, y + 40), fill=LINE, width=3)


def dashed_line(draw, start, end, fill=LINE, width=4, dash=12, gap=10):
    x1, y1 = start
    x2, y2 = end
    length = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    if length == 0:
        return
    step = dash + gap
    traveled = 0
    while traveled < length:
        run = min(dash, length - traveled)
        draw.line(
            (
                x1 + (x2 - x1) * traveled / length,
                y1 + (y2 - y1) * traveled / length,
                x1 + (x2 - x1) * (traveled + run) / length,
                y1 + (y2 - y1) * (traveled + run) / length,
            ),
            fill=fill,
            width=width,
        )
        traveled += step


def white_bubble(draw, cx, cy, width, height):
    box = (cx - width / 2, cy - height / 2, cx + width / 2, cy + height / 2)
    rr(draw, box, 28, fill=WHITE, outline=PALE, width=3)
    return box


def make_claims_flow():
    """FNOL enters the claims system, then DocRouter. The two stores match that bubble."""
    image = Image.new("RGB", (1600, 980), BG)
    draw = ImageDraw.Draw(image)
    label(draw, (80, 52), "CLAIMS EVIDENCE FLOW", 18, BLUE, "lm")
    draw.text((80, 88), "From notice to a cited claims assessment.", font=font(46), fill=NAVY)

    bubble_w, bubble_h = 250, 220
    row_y = 330
    steps = (205, 602, 999, 1396)

    for left, right in zip(steps, steps[1:]):
        dashed_line(
            draw,
            (left + bubble_w / 2 + 12, row_y),
            (right - bubble_w / 2 - 12, row_y),
        )

    # FNOL
    white_bubble(draw, steps[0], row_y, bubble_w, bubble_h)
    document(draw, steps[0] - 26, row_y - 78, 52, 68, shadow=False)
    centered(draw, (steps[0], row_y + 36), "FNOL", 22)
    label(draw, (steps[0], row_y + 70), "NOTICE", 15)

    # Claim CMS, same bubble language as the stores below.
    white_bubble(draw, steps[1], row_y, bubble_w, bubble_h)
    system_of_record(draw, steps[1], row_y - 36)
    centered(draw, (steps[1], row_y + 36), "CLAIM CMS", 20)
    label(draw, (steps[1], row_y + 70), "SYSTEM OF RECORD", 14)

    # DocRouter matches the other bubbles: one search mark, two lines under it.
    doc_x = steps[2]
    rr(
        draw,
        (
            doc_x - bubble_w / 2,
            row_y - bubble_h / 2,
            doc_x + bubble_w / 2,
            row_y + bubble_h / 2,
        ),
        28,
        fill=NAVY,
        outline=NAVY,
    )
    centered(draw, (doc_x, row_y - 78), "DOCROUTER", 16, "#93C5FD")
    index_icon(draw, doc_x, row_y - 24, 30)
    centered(draw, (doc_x, row_y + 32), "FILE INDEX", 16, WHITE)
    centered(draw, (doc_x, row_y + 62), "OCR/EXTRACTION/FLOWS", 15, WHITE)

    # Claims assessment agent.
    white_bubble(draw, steps[3], row_y, bubble_w, bubble_h)
    draw.ellipse((steps[3] - 58, row_y - 82, steps[3] - 8, row_y - 32), outline=BLUE, width=4)
    draw.arc((steps[3] - 74, row_y - 44, steps[3] + 8, row_y + 22), 180, 360, fill=BLUE, width=4)
    document(draw, steps[3] + 16, row_y - 82, 46, 60, shadow=False)
    label(draw, (steps[3], row_y + 36), "AI agent", 15, BLUE)
    centered(draw, (steps[3], row_y + 68), "CLAIMS ASSESSMENT", 15)

    # File store and data lake use the same bubble as the claim system.
    lower_y = 760
    stores = (
        (doc_x - 140, "file"),
        (doc_x + 140, "lake"),
    )
    for source_x, kind in stores:
        white_bubble(draw, source_x, lower_y, bubble_w, bubble_h)
        if kind == "file":
            document(draw, source_x - 26, lower_y - 72, 52, 68, shadow=False)
            centered(draw, (source_x, lower_y + 36), "FILE STORE", 20)
            label(draw, (source_x, lower_y + 70), "System of record", 14)
        else:
            data_lake(draw, source_x - 48, lower_y - 58, 80, 56)
            centered(draw, (source_x, lower_y + 36), "DATA LAKE", 20)
            label(draw, (source_x, lower_y + 70), "Batch jobs", 14)

    # One curve into each store. Both ends sit inside the bubbles.
    for start_x, end_x in ((doc_x - 48, doc_x - 140), (doc_x + 48, doc_x + 140)):
        start = (start_x, row_y + 78)
        end = (end_x, lower_y - 68)
        curve(
            draw,
            (start, (start[0], start[1] + 80), (end[0], end[1] - 80), end),
            width=4,
            dashed=True,
        )

    image.save(OUT / "index-once-claims-evidence-flow.png", optimize=True)


def make_takeaway():
    image = Image.new("RGB", (1600, 520), BG)
    draw = ImageDraw.Draw(image)

    rr(
        draw,
        (40, 40, 1560, 480),
        52,
        fill=NAVY,
        outline=NAVY,
        width=1,
    )

    # Minimal document → index → workflows motif.
    for offset in (18, 9, 0):
        x, y = 674 + offset, 92 - offset
        rr(
            draw,
            (x, y, x + 48, y + 62),
            8,
            fill="#20366F",
            outline="#93C5FD",
            width=2,
        )
    draw.line((744, 118, 780, 118), fill="#93C5FD", width=3)
    draw.ellipse((780, 94, 828, 142), fill=BLUE)
    for angle in (-28, 0, 28):
        end_x = 875
        end_y = 118 + angle
        draw.line((828, 118, end_x, end_y), fill="#93C5FD", width=3)
        draw.ellipse(
            (end_x - 6, end_y - 6, end_x + 6, end_y + 6),
            fill=WHITE,
        )

    centered(draw, (800, 236), "INDEX DOCUMENTS ONCE.", 62, WHITE)
    centered(
        draw,
        (800, 326),
        "Let every AI workflow find and reuse",
        35,
        "#A9D2FF",
    )
    centered(
        draw,
        (800, 374),
        "the evidence it needs.",
        35,
        "#A9D2FF",
    )

    image.save(OUT / "index-once-key-takeaway.png", optimize=True)


if __name__ == "__main__":
    make_hero()
    make_architecture()
    make_claims_flow()
    make_takeaway()
    for name in (
        "index-once-hero.png",
        "index-once-shared-architecture.png",
        "index-once-claims-evidence-flow.png",
        "index-once-key-takeaway.png",
    ):
        path = OUT / name
        with Image.open(path) as image:
            print(name, image.size, path.stat().st_size)

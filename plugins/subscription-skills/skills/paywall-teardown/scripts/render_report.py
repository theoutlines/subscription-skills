#!/usr/bin/env python3
"""Render a paywall teardown report card as a PNG.

The card has two panels:
  left  - the user's paywall screenshot with numbered pins on the elements
          each hypothesis refers to (filled pin = change this, ring pin = add here)
  right - the 100-point paywall score, the six dimension bars, and the ranked
          hypotheses with priority and expected impact

Usage:
  python3 render_report.py --data teardown.json --out report.png [--image paywall.png]

Without --image (or if the file can't be opened) the card renders the right
panel only. Requires Pillow (pip install pillow).

teardown.json shape (see example.json next to this script):
{
  "subtitle": "Fitness app - onboarding paywall",
  "verdict":  "Clean layout, but pricing hides what annual saves.",
  "score": {
    "dimensions": [
      {"label": "Value clarity", "score": 14, "max": 20}, ...
    ]
  },
  "strengths": ["Outcome-led headline", "Full-width CTA"],
  "items": [
    {"n": 1, "priority": "Fix first", "pattern": "Transparent billing framing",
     "test": "Show the billing period next to the big price.",
     "impact": "CR +3-8%",
     "pin": {"x": 0.52, "y": 0.61, "type": "change"}}
  ]
}
pin.x / pin.y are fractions (0-1) of the screenshot's width / height.
pin.type is "change" (an element that exists) or "add" (where a missing
element should go). Omit pin or set it to null for items with no location.
"""

import argparse
import json
import math
import os
import sys

try:
    from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps
except ImportError:  # pragma: no cover
    sys.exit("Pillow is required: pip install pillow")

HERE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = os.path.normpath(os.path.join(HERE, "..", "assets", "fonts"))

# ---------------------------------------------------------------- palette ---
SURFACE = (252, 252, 251)        # card background
PANEL = (243, 242, 238)          # screenshot panel background
INK = (11, 11, 11)               # primary text
INK_2 = (82, 81, 78)             # secondary text
INK_3 = (128, 127, 122)          # muted text
RULE = (228, 227, 222)           # hairlines, bar tracks
ACCENT = (103, 32, 255)          # brand accent (bars, header mark, link)

# Priority colors follow a status scale; every pin also carries a number and
# every list row a text label, so color never carries meaning alone.
PRIORITY = {
    "fix first": {"fill": (208, 59, 59), "text": (255, 255, 255), "label": "Fix first"},
    "high": {"fill": (236, 131, 90), "text": (255, 255, 255), "label": "High"},
    "medium": {"fill": (250, 178, 25), "text": (11, 11, 11), "label": "Medium"},
    "low": {"fill": (138, 137, 132), "text": (255, 255, 255), "label": "Low"},
}

GRADES = [  # (min score, label, chip color)
    (85, "Strong", (12, 163, 12)),
    (70, "Solid", (42, 120, 214)),
    (50, "Leaking", (236, 131, 90)),
    (0, "Needs work", (208, 59, 59)),
]

FOOTER_DISCLAIMER = (
    "Patterns are drawn from Adapty's teardowns of top apps across numerous "
    "verticals; impact ranges are expected effect, not measured lift for your app."
)
FOOTER_CTA = "Build and A/B test these in Adapty's Flow & Paywall Builder"
FOOTER_URL = "adapty.io/flow-paywall-builder"

# ----------------------------------------------------------------- layout ---
SCALE = 2                         # render at 2x for crisp text
W_RIGHT = 760                     # right panel width (1x units)
SHOT_H = 760                      # screenshot display height (1x)
PAD = 40
GAP = 40


def s(v):
    return int(round(v * SCALE))


# ------------------------------------------------------------------ fonts ---
_FALLBACKS = {
    "regular": [
        "DejaVuSans.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/System/Library/Fonts/Supplemental/Arial.ttf", "C:/Windows/Fonts/arial.ttf",
    ],
    "semibold": [
        "DejaVuSans-Bold.ttf", "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        "/System/Library/Fonts/Supplemental/Arial Bold.ttf", "C:/Windows/Fonts/arialbd.ttf",
    ],
}
_FILES = {"regular": "Inter-Regular.ttf", "semibold": "Inter-SemiBold.ttf", "bold": "Inter-Bold.ttf"}
_cache = {}


def font(weight, size):
    key = (weight, size)
    if key in _cache:
        return _cache[key]
    candidates = [os.path.join(FONT_DIR, _FILES[weight])]
    candidates += _FALLBACKS["regular" if weight == "regular" else "semibold"]
    f = None
    for path in candidates:
        try:
            f = ImageFont.truetype(path, s(size))
            break
        except (OSError, IOError):
            continue
    if f is None:
        try:
            f = ImageFont.load_default(size=s(size))
        except TypeError:  # Pillow < 10.1
            f = ImageFont.load_default()
    _cache[key] = f
    return f


# ---------------------------------------------------------------- helpers ---
def text_w(draw, txt, fnt):
    return draw.textlength(txt, font=fnt)


def wrap(draw, txt, fnt, width, max_lines=None):
    words = str(txt).split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if text_w(draw, trial, fnt) <= width:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    if max_lines and len(lines) > max_lines:
        lines = lines[:max_lines]
        last = lines[-1]
        while last and text_w(draw, last + "\u2026", fnt) > width:
            last = last[:-1]
        lines[-1] = last.rstrip(" ,.;:") + "\u2026"
    return lines or [""]


def line_h(fnt, lead=1.32):
    asc, desc = fnt.getmetrics()
    return int((asc + desc) * lead)


def priority_style(p):
    return PRIORITY.get(str(p or "").strip().lower(), PRIORITY["medium"])


def grade_for(total):
    for floor, label, color in GRADES:
        if total >= floor:
            return label, color
    return GRADES[-1][1], GRADES[-1][2]


def normalize(data):
    dims = (data.get("score") or {}).get("dimensions") or []
    for d in dims:
        d["max"] = max(1, int(d.get("max", 0) or 0))
        d["score"] = max(0, min(int(round(float(d.get("score", 0) or 0))), d["max"]))
    total_max = sum(d["max"] for d in dims) or 100
    total = sum(d["score"] for d in dims)
    if dims and total_max != 100:
        total = int(round(total * 100.0 / total_max))
    given = (data.get("score") or {}).get("total")
    if given is not None and dims and abs(int(given) - total) > 1:
        print("note: score.total (%s) != sum of dimensions (%s); using the sum" % (given, total),
              file=sys.stderr)
    if not dims and given is not None:
        total = int(given)
    data["_total"] = max(0, min(100, total))
    items = data.get("items") or []
    for i, it in enumerate(items):
        it.setdefault("n", i + 1)
    data["items"] = items
    return data


# ------------------------------------------------------------------- pins ---
GUTTER = 64                       # callout gutter on each side of the screenshot (1x)
BADGE_R = 15                      # callout badge radius (1x)


def pin_targets(items, w, h):
    """Return [(n, x, y, kind)] in screenshot pixel space."""
    out = []
    for it in items:
        pin = it.get("pin")
        if not pin or pin.get("x") is None or pin.get("y") is None:
            continue
        inset = s(14)  # keep dots off the rounded corners
        x = min(max(float(pin["x"]) * w, inset), w - inset)
        y = min(max(float(pin["y"]) * h, inset), h - inset)
        out.append((it["n"], x, y, (pin.get("type") or "change").lower()))
    return out


def stack(ys, lo, hi, gap):
    """Spread desired y positions so neighbours are at least `gap` apart, inside [lo, hi]."""
    order = sorted(range(len(ys)), key=lambda i: ys[i])
    placed = [0.0] * len(ys)
    prev = lo - gap
    for i in order:
        placed[i] = max(ys[i], prev + gap, lo)
        prev = placed[i]
    overflow = prev - hi
    if overflow > 0:  # push everything back up from the bottom
        nxt = hi + gap
        for i in reversed(order):
            placed[i] = min(placed[i], nxt - gap)
            nxt = placed[i]
    return placed


def badge(d, cx, cy, r, n, style, kind, fsize=14):
    ring = s(3)
    d.ellipse([cx - r - ring, cy - r - ring, cx + r + ring, cy + r + ring], fill=(255, 255, 255))
    if kind == "add":
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(255, 255, 255), outline=style["fill"], width=s(3))
        color = style["fill"] if style["fill"] != PRIORITY["medium"]["fill"] else (150, 100, 0)
    else:
        d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=style["fill"])
        color = style["text"]
    d.text((cx, cy), str(n), font=font("bold", fsize), fill=color, anchor="mm")


# ------------------------------------------------------------ left panel ---
def load_shot(path, max_h):
    try:
        shot = Image.open(path)
        shot = ImageOps.exif_transpose(shot).convert("RGBA")
    except Exception as e:  # noqa: BLE001
        print("note: couldn't open screenshot (%s); rendering without it" % e, file=sys.stderr)
        return None
    target_h = max_h
    ratio = target_h / float(shot.height)
    target_w = int(shot.width * ratio)
    max_w = s(560)
    if target_w > max_w:  # very wide image (tablet / landscape)
        ratio = max_w / float(shot.width)
        target_w, target_h = max_w, int(shot.height * ratio)
    return shot.resize((target_w, target_h), Image.LANCZOS)


def compose_left(shot, items, panel_h):
    g, pad, radius = s(GUTTER), s(PAD) - s(8), s(28)
    panel_w = shot.width + 2 * g + 2 * pad
    panel = Image.new("RGBA", (panel_w, panel_h), PANEL + (255,))
    sx, sy = pad + g, s(PAD)
    # rounded screenshot with soft shadow
    mask = Image.new("L", shot.size, 0)
    ImageDraw.Draw(mask).rounded_rectangle([0, 0, shot.width - 1, shot.height - 1], radius, fill=255)
    sh = Image.new("RGBA", panel.size, (0, 0, 0, 0))
    ImageDraw.Draw(sh).rounded_rectangle([sx, sy + s(8), sx + shot.width, sy + s(8) + shot.height],
                                         radius, fill=(0, 0, 0, 60))
    panel.alpha_composite(sh.filter(ImageFilter.GaussianBlur(s(14))))
    panel.paste(shot, (sx, sy), mask)
    d = ImageDraw.Draw(panel)
    d.rounded_rectangle([sx, sy, sx + shot.width - 1, sy + shot.height - 1], radius,
                        outline=(0, 0, 0, 40), width=s(1))

    by_n = {it["n"]: it for it in items}
    targets = pin_targets(items, shot.width, shot.height)
    r = s(BADGE_R)
    gap = 2 * r + s(10)
    sides = {"L": [], "R": []}
    for t in targets:
        sides["L" if t[1] < shot.width / 2.0 else "R"].append(t)
    callouts = []
    for side, ts in sides.items():
        if not ts:
            continue
        ys = stack([sy + t[2] for t in ts], sy + r, sy + shot.height - r, gap)
        bx = pad + g / 2.0 if side == "L" else sx + shot.width + g / 2.0
        for t, by in zip(ts, ys):
            callouts.append((t, bx, by, side))
    # leader lines first (white halo + ink), then dots, then badges on top
    for (n, tx, ty, kind), bx, by, side in callouts:
        px, py = sx + tx, sy + ty
        ex = bx + (r if side == "L" else -r)
        d.line([ex, by, px, py], fill=(255, 255, 255), width=s(5))
    for (n, tx, ty, kind), bx, by, side in callouts:
        px, py = sx + tx, sy + ty
        ex = bx + (r if side == "L" else -r)
        d.line([ex, by, px, py], fill=(40, 40, 40), width=s(2))
    for (n, tx, ty, kind), bx, by, side in callouts:
        st = priority_style(by_n[n].get("priority"))
        px, py = sx + tx, sy + ty
        dr = s(6)
        d.ellipse([px - dr - s(3), py - dr - s(3), px + dr + s(3), py + dr + s(3)], fill=(255, 255, 255))
        if kind == "add":
            d.ellipse([px - dr, py - dr, px + dr, py + dr], fill=(255, 255, 255), outline=st["fill"], width=s(3))
        else:
            d.ellipse([px - dr, py - dr, px + dr, py + dr], fill=st["fill"])
        badge(d, bx, by, r, n, st, kind)

    if callouts:
        y = sy + shot.height + s(26)
        f = font("regular", 13)
        x = sx
        rr = s(7)
        grey = PRIORITY["low"]["fill"]
        d.ellipse([x, y - rr, x + 2 * rr, y + rr], fill=grey)
        d.text((x + 2 * rr + s(8), y), "Change this element", font=f, fill=INK_2, anchor="lm")
        x += 2 * rr + s(8) + int(text_w(d, "Change this element", f)) + s(22)
        d.ellipse([x, y - rr, x + 2 * rr, y + rr], fill=(255, 255, 255), outline=grey, width=s(3))
        d.text((x + 2 * rr + s(8), y), "Add something here", font=f, fill=INK_2, anchor="lm")
    return panel


# ----------------------------------------------------------- right panel ---
def draw_right(data, width):
    """Draw the right panel on a tall scratch canvas, return it cropped to content."""
    canvas = Image.new("RGBA", (width, s(4000)), SURFACE + (255,))
    d = ImageDraw.Draw(canvas)
    x0, inner = s(PAD), width - 2 * s(PAD)
    y = s(PAD)

    # eyebrow
    d.rounded_rectangle([x0, y + s(2), x0 + s(10), y + s(12)], s(2), fill=ACCENT)
    d.text((x0 + s(18), y), "PAYWALL TEARDOWN", font=font("bold", 13), fill=INK_2)
    y += s(28)
    sub = data.get("subtitle")
    if sub:
        for ln in wrap(d, sub, font("semibold", 22), inner, 2):
            d.text((x0, y), ln, font=font("semibold", 22), fill=INK)
            y += line_h(font("semibold", 22), 1.25)
        y += s(10)

    # score hero
    total = data["_total"]
    grade, gcolor = grade_for(total)
    big = font("bold", 64)
    d.text((x0, y), str(total), font=big, fill=INK)
    bw = text_w(d, str(total), big)
    d.text((x0 + bw + s(6), y + s(38)), "/100", font=font("semibold", 22), fill=INK_3)
    cx = x0 + bw + s(6) + text_w(d, "/100", font("semibold", 22)) + s(18)
    chip_f = font("bold", 15)
    cw = text_w(d, grade, chip_f) + s(28)
    cy = y + s(30)
    d.rounded_rectangle([cx, cy, cx + cw, cy + s(32)], s(16), fill=gcolor)
    d.text((cx + cw / 2, cy + s(16)), grade, font=chip_f,
           fill=(255, 255, 255) if gcolor != (250, 178, 25) else INK, anchor="mm")
    y += s(84)
    verdict = data.get("verdict")
    if verdict:
        vf = font("regular", 17)
        for ln in wrap(d, verdict, vf, inner, 3):
            d.text((x0, y), ln, font=vf, fill=INK_2)
            y += line_h(vf)
    y += s(18)

    # dimension bars
    dims = (data.get("score") or {}).get("dimensions") or []
    if dims:
        lab_f, val_f = font("regular", 14), font("semibold", 14)
        label_w = s(150)
        val_w = s(56)
        bar_x = x0 + label_w
        bar_w = inner - label_w - val_w
        for dm in dims:
            d.text((x0, y + s(9)), str(dm.get("label", "")), font=lab_f, fill=INK_2, anchor="lm")
            d.rounded_rectangle([bar_x, y + s(4), bar_x + bar_w, y + s(14)], s(5), fill=RULE)
            frac = dm["score"] / float(dm["max"])
            if frac > 0:
                d.rounded_rectangle([bar_x, y + s(4), bar_x + max(s(10), int(bar_w * frac)), y + s(14)],
                                    s(5), fill=ACCENT)
            d.text((x0 + inner, y + s(9)), "%d/%d" % (dm["score"], dm["max"]), font=val_f,
                   fill=INK, anchor="rm")
            y += s(28)
        y += s(14)

    # strengths
    strengths = [t for t in (data.get("strengths") or []) if t]
    if strengths:
        d.line([x0, y, x0 + inner, y], fill=RULE, width=s(1))
        y += s(16)
        hf = font("bold", 12)
        d.text((x0, y), "KEEP", font=hf, fill=(12, 120, 12))
        tf = font("regular", 15)
        txt = " \u00b7 ".join(strengths)
        for ln in wrap(d, txt, tf, inner - s(56), 2):
            d.text((x0 + s(56), y - s(2)), ln, font=tf, fill=INK_2)
            y += line_h(tf)
        y += s(12)

    # hypotheses
    d.line([x0, y, x0 + inner, y], fill=RULE, width=s(1))
    y += s(18)
    d.text((x0, y), "WHAT TO TEST", font=font("bold", 12), fill=INK_2)
    d.text((x0 + inner, y), "EXPECTED IMPACT", font=font("bold", 12), fill=INK_2, anchor="ra")
    y += s(28)
    pf, tf, imf, chf = font("semibold", 16), font("regular", 14), font("semibold", 14), font("bold", 11)
    impact_w = s(150)
    text_x = x0 + s(44)
    text_w_avail = inner - s(44) - impact_w - s(12)
    for it in data["items"]:
        st = priority_style(it.get("priority"))
        r = s(14)
        cyc = y + s(12)
        kind = ((it.get("pin") or {}).get("type") or "change").lower()
        if kind == "add":
            d.ellipse([x0, cyc - r, x0 + 2 * r, cyc + r], fill=(255, 255, 255), outline=st["fill"], width=s(3))
            numc = st["fill"] if st["fill"] != PRIORITY["medium"]["fill"] else (150, 100, 0)
        else:
            d.ellipse([x0, cyc - r, x0 + 2 * r, cyc + r], fill=st["fill"])
            numc = st["text"]
        d.text((x0 + r, cyc), str(it["n"]), font=font("bold", 13), fill=numc, anchor="mm")
        # priority chip + pattern
        chip = st["label"].upper()
        chw = text_w(d, chip, chf) + s(14)
        d.rounded_rectangle([text_x, y + s(2), text_x + chw, y + s(22)], s(5), outline=st["fill"], width=s(2))
        d.text((text_x + chw / 2, y + s(12)), chip, font=chf, fill=INK, anchor="mm")
        pat_lines = wrap(d, it.get("pattern", ""), pf, text_w_avail - chw - s(10), 1)
        d.text((text_x + chw + s(10), y + s(12)), pat_lines[0], font=pf, fill=INK, anchor="lm")
        # impact, right-aligned, may wrap to 2 lines
        iy = y + s(4)
        imp_lines = []
        for part in str(it.get("impact", "")).split(","):
            imp_lines += wrap(d, part.strip(), imf, impact_w) if part.strip() else []
        if len(imp_lines) > 3:
            imp_lines = imp_lines[:3]
            imp_lines[-1] = imp_lines[-1].rstrip(" ,.;:") + "\u2026"
        for ln in imp_lines:
            d.text((x0 + inner, iy), ln, font=imf, fill=INK, anchor="ra")
            iy += line_h(imf, 1.25)
        y += s(30)
        for ln in wrap(d, it.get("test", ""), tf, text_w_avail, 2):
            d.text((text_x, y), ln, font=tf, fill=INK_2)
            y += line_h(tf)
        y = max(y, iy) + s(14)

    # footer
    y += s(4)
    d.line([x0, y, x0 + inner, y], fill=RULE, width=s(1))
    y += s(14)
    ff = font("regular", 12)
    for ln in wrap(d, FOOTER_DISCLAIMER, ff, inner):
        d.text((x0, y), ln, font=ff, fill=INK_3)
        y += line_h(ff)
    y += s(10)
    cf, uf = font("semibold", 14), font("bold", 14)
    d.text((x0, y), FOOTER_CTA, font=cf, fill=INK)
    d.text((x0 + inner, y), FOOTER_URL + "  \u2192", font=uf, fill=ACCENT, anchor="ra")
    if text_w(d, FOOTER_CTA, cf) + text_w(d, FOOTER_URL + "  \u2192", uf) + s(16) > inner:
        # not enough room on one line: move URL below
        d.rectangle([x0 + text_w(d, FOOTER_CTA, cf) + s(4), y, x0 + inner, y + line_h(cf)], fill=SURFACE)
        y += line_h(cf)
        d.text((x0, y), FOOTER_URL + "  \u2192", font=uf, fill=ACCENT)
    y += line_h(cf) + s(PAD) - s(8)
    return canvas.crop((0, 0, width, y))


# ------------------------------------------------------------------- main ---
def render(data, image_path, out_path):
    data = normalize(data)
    right = draw_right(data, s(W_RIGHT))
    card = right
    if image_path:
        legend = s(56)
        shot_h = max(s(SHOT_H), min(s(1100), right.height - s(PAD) - legend))
        shot = load_shot(image_path, shot_h)
        if shot is not None:
            h = max(right.height, shot.height + s(PAD) + legend)
            left = compose_left(shot, data["items"], h)
            card = Image.new("RGBA", (left.width + right.width, h), SURFACE + (255,))
            card.alpha_composite(left, (0, 0))
            card.alpha_composite(right, (left.width, 0))
    card = card.convert("RGB")
    out_dir = os.path.dirname(os.path.abspath(out_path))
    os.makedirs(out_dir, exist_ok=True)
    card.save(out_path, "PNG", optimize=True)
    return out_path, card.size


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--data", required=True, help="teardown JSON file")
    ap.add_argument("--image", help="paywall screenshot (png/jpg/webp)")
    ap.add_argument("--out", default="paywall-teardown.png", help="output PNG path")
    a = ap.parse_args()
    with open(a.data, "r", encoding="utf-8") as fh:
        data = json.load(fh)
    path, size = render(data, a.image, a.out)
    print("saved %s (%dx%d)" % (path, size[0], size[1]))


if __name__ == "__main__":
    main()

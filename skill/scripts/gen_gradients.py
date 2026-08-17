#!/usr/bin/env python3
"""Generate Premier Cloud brand gradient background images for pptxgenjs decks.

pptxgenjs cannot render gradient fills, so we bake them as PNGs and place them as
images. Rounded panels/cards are emitted with rounded-corner alpha so they can be
placed as PLAIN images (never use addImage rounding:true — it makes an ellipse).

Outputs (into ./assets):
  bg_dark_glow.png   dark hero: #033552 -> #000000 with a soft blue glow (title/section/closing)
  bg_blue.png        blue gradient: #38B4E7 -> #1E66AB (full-bleed)
  rounded_panel.png  wide rounded blue-gradient panel (e.g. benefits triad backdrop)
  rounded_card.png   card-aspect rounded blue-gradient (highlighted card)
  callout_blue.png   short rounded blue-gradient bar (key-insight callouts)

Usage:  python3 gen_gradients.py [output_dir]   (default: assets)
Requires: Pillow  (pip install --user --break-system-packages Pillow)
"""
import sys, os, math
from PIL import Image, ImageDraw

OUT = sys.argv[1] if len(sys.argv) > 1 else "assets"
os.makedirs(OUT, exist_ok=True)

def hx(s): return tuple(int(s[i:i+2], 16) for i in (0, 2, 4))
def lerp(a, b, t): return tuple(round(a[i] + (b[i]-a[i])*t) for i in range(3))

def grad(w, h, c1, c2, angle):
    img = Image.new("RGB", (w, h)); px = img.load()
    a = math.radians(angle); dx, dy = math.cos(a), math.sin(a)
    pr = [x*dx + y*dy for x, y in [(0,0),(w,0),(0,h),(w,h)]]
    pmin, pmax = min(pr), max(pr)
    for y in range(h):
        for x in range(w):
            t = ((x*dx + y*dy) - pmin) / (pmax - pmin)
            px[x, y] = lerp(c1, c2, t)
    return img

# Dark hero with radial glow
d = grad(1920, 1080, hx("033552"), hx("000000"), 135)
px = d.load(); w, h = d.size; cx, cy = w*0.72, h*0.35; R = w*0.55; gl = hx("0A4E7A")
for y in range(h):
    for x in range(w):
        dd = math.hypot(x-cx, y-cy) / R
        if dd < 1:
            t = (1-dd)*0.35; r, g, b = px[x, y]
            px[x, y] = (min(255, round(r+(gl[0]-r)*t)),
                        min(255, round(g+(gl[1]-g)*t)),
                        min(255, round(b+(gl[2]-b)*t)))
d.save(os.path.join(OUT, "bg_dark_glow.png"))

grad(1920, 1080, hx("38B4E7"), hx("1E66AB"), 135).save(os.path.join(OUT, "bg_blue.png"))

def rounded(w, h, rad, fn, angle=120):
    base = grad(w, h, hx("38B4E7"), hx("1E66AB"), angle).convert("RGBA")
    m = Image.new("L", (w, h), 0)
    ImageDraw.Draw(m).rounded_rectangle([0, 0, w-1, h-1], radius=rad, fill=255)
    base.putalpha(m); base.save(os.path.join(OUT, fn))

rounded(1480, 546, 42, "rounded_panel.png", 120)
rounded(1163, 760, 30, "rounded_card.png", 120)
rounded(1480, 300, 26, "callout_blue.png", 120)
print("gradients written to", OUT)

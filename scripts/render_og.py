#!/usr/bin/env python3
"""Render the Alwakile social card at 1200x630. Build-time only; no runtime dependencies."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import math

ROOT = Path(__file__).resolve().parents[1]
W, H, SCALE = 1200, 630, 2
BACKGROUND = (14, 16, 20)
CREAM = (236, 231, 220)
BLUE = (157, 176, 255)
MUTED = (170, 176, 190)
STROKE = (60, 68, 90)
im = Image.new("RGB", (W*SCALE, H*SCALE), BACKGROUND)
d = ImageDraw.Draw(im)

def px(n):
    return round(n * SCALE)

def font(candidates, size):
    for path in candidates:
        if Path(path).exists():
            return ImageFont.truetype(path, px(size))
    return ImageFont.load_default()

SERIF = font([
    "/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf",
    "/usr/share/fonts/truetype/liberation2/LiberationSerif-Regular.ttf",
], 68)
ITALIC = font([
    "/usr/share/fonts/truetype/dejavu/DejaVuSerif-Italic.ttf",
    "/usr/share/fonts/truetype/liberation2/LiberationSerif-Italic.ttf",
], 64)
MONO = font([
    "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
    "/usr/share/fonts/truetype/liberation2/LiberationMono-Regular.ttf",
], 15)
MONO_SMALL = font([
    "/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf",
], 13)
ARABIC = font([
    "/usr/share/fonts/truetype/noto/NotoNaskhArabic-Regular.ttf",
    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
], 90)

def line(points, color, width=1):
    d.line([(px(x),px(y)) for x,y in points], fill=color, width=px(width))

def ellipse(box, color, width=1, fill=None):
    d.ellipse(tuple(px(v) for v in box), outline=color, width=px(width), fill=fill)

def txt(pos, text, f, color):
    d.text((px(pos[0]),px(pos[1])), text, font=f, fill=color)

d.rectangle((px(34),px(32),px(1166),px(598)), outline=STROKE, width=px(1))
line([(34,100),(1166,100)], STROKE)
line([(34,545),(1166,545)], STROKE)
txt((75,53), "ALWAKILE.COM", MONO, CREAM)
txt((75,128), "THE AUTHORIZED AGENT", MONO, BLUE)
txt((75,197), "AI can act.", SERIF, CREAM)
txt((75,295), "Who gave it", ITALIC, BLUE)
txt((75,373), "the authority?", ITALIC, BLUE)
txt((77,495), "IDENTITY  ·  DELEGATION  ·  ACCOUNTABILITY", MONO_SMALL, MUTED)
txt((76,559), "STRATEGIC ACQUISITION OPPORTUNITY", MONO_SMALL, MUTED)

cx,cy = 948,317
for radius in (203,190,157,134):
    ellipse((cx-radius,cy-radius,cx+radius,cy+radius),
            BLUE if radius in (203,134) else STROKE,
            2 if radius == 203 else 1)
for a in range(0,360,30):
    rad=math.radians(a)
    line([(cx+175*math.cos(rad),cy+175*math.sin(rad)),
          (cx+185*math.cos(rad),cy+185*math.sin(rad))], BLUE)
for a in (0,90,180,270):
    rad=math.radians(a)
    x,y=cx+190*math.cos(rad),cy+190*math.sin(rad)
    ellipse((x-4,y-4,x+4,y+4),BLUE,fill=BLUE)
try:
    d.text((px(cx),px(cy-53)), "الوكيل", font=ARABIC, fill=CREAM,
           anchor="mm", direction="rtl", language="ar")
except (ValueError, KeyError):
    d.text((px(cx-113),px(cy-80)), "الوكيل", font=ARABIC, fill=CREAM)
txt((cx-85,cy+75), "AUTHORIZED", MONO_SMALL, BLUE)

im=im.resize((W,H),Image.Resampling.LANCZOS)
out=ROOT/"public"/"og-card.png"
im.save(out,format="PNG",optimize=True)
print(f"Rendered {out} ({out.stat().st_size:,} bytes)")

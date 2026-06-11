# -*- coding: utf-8 -*-
"""
Genera le icone PWA di Pinakes (dorsi di libri su una mensola, palette del progetto).
Esegui:  python _build_icons.py
Output:  icons/icon-192.png, icon-512.png, icon-maskable-512.png, apple-touch-icon.png, favicon-32.png
"""
import os
from PIL import Image, ImageDraw

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "icons")
os.makedirs(OUT, exist_ok=True)

INK    = (26, 26, 46)      # #1a1a2e  sfondo
ACCENT = (205, 133, 63)    # #cd853f
GOLD   = (184, 134, 11)    # #b8860b
GOLDL  = (218, 165, 32)    # #daa520  mensola
GREEN  = (45, 106, 79)     # #2d6a4f
BROWN  = (139, 69, 19)     # #8b4513
LABEL  = (245, 240, 230)   # etichetta dorso

BOOKS = [
    (0.165, 0.62, ACCENT),
    (0.150, 0.78, GOLD),
    (0.165, 0.54, GREEN),
    (0.145, 0.70, BROWN),
]

def draw_books(img, inset_frac):
    d = ImageDraw.Draw(img)
    S = img.size[0]
    inset = S * inset_frac
    x0, x1 = inset, S - inset
    region_w = x1 - x0
    maxh = region_w * 0.86
    baseline = S - inset - region_w * 0.10
    gap = region_w * 0.022
    total = sum(b[0] for b in BOOKS) * region_w + gap * (len(BOOKS) - 1)
    cx = x0 + (region_w - total) / 2
    r = max(3, int(region_w * 0.018))
    for relw, relh, col in BOOKS:
        w = relw * region_w
        h = relh * maxh
        top = baseline - h
        d.rounded_rectangle([cx, top, cx + w, baseline], radius=r, fill=col)
        # etichetta sul dorso
        ly = top + h * 0.22
        d.rounded_rectangle([cx + w * 0.18, ly, cx + w * 0.82, ly + h * 0.1],
                            radius=max(2, int(w * 0.08)), fill=LABEL)
        cx += w + gap
    # mensola
    sh = max(6, int(S * 0.016))
    d.rounded_rectangle([x0 + region_w * 0.04, baseline, x1 - region_w * 0.04, baseline + sh],
                        radius=sh // 2, fill=GOLDL)

def make(master_size, rounded, inset_frac):
    img = Image.new("RGBA", (master_size, master_size), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)
    if rounded:
        d.rounded_rectangle([0, 0, master_size - 1, master_size - 1],
                            radius=int(master_size * 0.18), fill=INK)
    else:
        d.rectangle([0, 0, master_size, master_size], fill=INK)
    draw_books(img, inset_frac)
    return img

M = 1024
any_master  = make(M, rounded=True,  inset_frac=0.20)   # icona "any"
mask_master = make(M, rounded=False, inset_frac=0.24)   # full-bleed, safe-zone

def save(img, name, size):
    img.resize((size, size), Image.LANCZOS).save(os.path.join(OUT, name))
    print("  ", name, size)

print("Genero icone in", OUT)
save(any_master,  "icon-192.png", 192)
save(any_master,  "icon-512.png", 512)
save(mask_master, "icon-maskable-512.png", 512)
save(mask_master, "apple-touch-icon.png", 180)
save(any_master,  "favicon-32.png", 32)
print("Fatto.")

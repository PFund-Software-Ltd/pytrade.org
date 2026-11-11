"""Generate a 1600x900 (16:9) thumbnail for a content type of PyTrade.org.

Usage (needs rsvg-convert, e.g. `brew install librsvg`):
    python generate_thumbnail.py --title Examples \
        --tagline "The Home for Python Trading" --tagline "Minimal code, one concept" \
        [--tag pfeed --tag polars] [--art code --code snippet.py] --out examples
    (writes examples.png; without --art the text is centered, for normal posts)

The chart uses a fixed random seed, so only the texts change between runs.
"""

import argparse
import io
import keyword
import tokenize
import random
import re
import subprocess
from html import escape
from pathlib import Path

LOGO = Path(__file__).resolve().parent / "static" / "logo.svg"
NAVY_TOP, NAVY_BOTTOM = "#0A1428", "#142544"
BLUE, YELLOW, GREEN, RED, WHITE = "#1F6BA6", "#FED540", "#3DD9A4", "#FF6B47", "#F5F7FB"
SANS = "'Avenir Next', Inter, 'Helvetica Neue', sans-serif"
MONO = "Menlo, monospace"
W, H = 1600, 900

parser = argparse.ArgumentParser()
parser.add_argument("--title", required=True)
parser.add_argument("--tagline", action="append", default=[])
parser.add_argument("--tag", action="append", default=[])
parser.add_argument("--out", required=True)
parser.add_argument("--art", choices=["none", "candles", "code"], default="none", help="right-hand side art, for the banner post")
parser.add_argument("--code", type=Path, help="Python file shown in the editor window (keep it to ~6 short lines)")
args = parser.parse_args()

# candlesticks on the right half
random.seed(7)
x0, x1, ytop, ybot = 860, 1500, 210, 690
n = 26
step = (x1 - x0) / n
p = 100.0
cs = []
for _ in range(n):
    o = p
    c = o + random.gauss(0.35, 2.2)
    hi = max(o, c) + abs(random.gauss(0, 1.2))
    lo = min(o, c) - abs(random.gauss(0, 1.2))
    cs.append((o, hi, lo, c))
    p = c
lo_all = min(x[2] for x in cs)
hi_all = max(x[1] for x in cs)


def Y(v):
    return ybot - (v - lo_all) / (hi_all - lo_all) * (ybot - ytop)


candles = []
for i, (o, hi, lo, c) in enumerate(cs):
    cx = x0 + step * (i + 0.5)
    col = GREEN if c >= o else RED
    bw = step * 0.56
    top, bot = Y(max(o, c)), Y(min(o, c))
    candles.append(f'<line x1="{cx:.1f}" y1="{Y(hi):.1f}" x2="{cx:.1f}" y2="{Y(lo):.1f}" stroke="{col}" stroke-width="3" stroke-linecap="round"/>')
    candles.append(f'<rect x="{cx - bw / 2:.1f}" y="{top:.1f}" width="{bw:.1f}" height="{max(bot - top, 3):.1f}" rx="3" fill="{col}"/>')
pts = " ".join(f"{x0 + step * (i + 0.5):.1f},{Y(c[3]):.1f}" for i, c in enumerate(cs))


# right side, "code" art: an editor window with a short Python snippet and its chart output
KW, STR, NUM, FN, TXT, DIM = "#7FB8F0", GREEN, RED, YELLOW, WHITE, "#8A97B0"
DEFAULT_CODE = """import pandas as pd

df = pd.read_parquet("btc.parquet")
df["sma"] = df.close.rolling(20).mean()
df.plot(y=["close", "sma"])
"""


def highlight(src):
    """Split Python source into lines of (text, color) spans, using the stdlib tokenizer."""
    lines = src.rstrip("\n").split("\n")
    spans = [[] for _ in lines]
    cols = [0] * len(lines)
    toks = list(tokenize.generate_tokens(io.StringIO(src).readline))
    for i, tok in enumerate(toks):
        if tok.type in (tokenize.NEWLINE, tokenize.NL, tokenize.INDENT, tokenize.DEDENT, tokenize.ENDMARKER):
            continue
        (r, c), text = tok.start, tok.string
        nxt = toks[i + 1].string if i + 1 < len(toks) else ""
        if tok.type == tokenize.STRING:
            color = STR
        elif tok.type == tokenize.NUMBER:
            color = NUM
        elif tok.type == tokenize.COMMENT:
            color = DIM
        elif tok.type == tokenize.NAME and keyword.iskeyword(text):
            color = KW
        elif tok.type == tokenize.NAME and nxt == "(":
            color = FN
        elif tok.type == tokenize.OP:
            color = DIM
        else:
            color = TXT
        row = r - 1
        if row >= len(lines):
            continue
        if c > cols[row]:
            spans[row].append((" " * (c - cols[row]), TXT))
        spans[row].append((text.split("\n")[0], color))
        cols[row] = c + len(text)
    return spans


code_src = args.code.read_text(encoding="utf-8") if args.code else DEFAULT_CODE
code_name = args.code.name if args.code else "example.py"
CODE = highlight(code_src)
if len(CODE) > 7 or max(len(line) for line in code_src.splitlines()) > 47:
    print("warning: code is longer than ~7 lines or 47 columns and may not fit the editor window")
cx0, cy0, cw, ch = 800, 140, 720, 620
code_svg = [
    f'<rect x="{cx0 + 14}" y="{cy0 + 22}" width="{cw}" height="{ch}" rx="22" fill="#000" fill-opacity="0.35"/>',
    f'<rect x="{cx0}" y="{cy0}" width="{cw}" height="{ch}" rx="22" fill="#0D1830" stroke="{WHITE}" stroke-opacity="0.12"/>',
    f'<path d="M{cx0} {cy0 + 56} h{cw}" stroke="{WHITE}" stroke-opacity="0.08"/>',
]
for i, col in enumerate([RED, YELLOW, GREEN]):
    code_svg.append(f'<circle cx="{cx0 + 30 + i * 26}" cy="{cy0 + 28}" r="8" fill="{col}" fill-opacity="0.85"/>')
code_svg.append(f'<text x="{cx0 + cw / 2}" y="{cy0 + 36}" text-anchor="middle" font-family="{MONO}" font-size="20" fill="{DIM}">{escape(code_name)}</text>')
for i, line in enumerate(CODE):
    y_line = cy0 + 108 + i * 40
    code_svg.append(f'<text x="{cx0 + 28}" y="{y_line}" font-family="{MONO}" font-size="20" fill="{DIM}" fill-opacity="0.6">{i + 1}</text>')
    spans = "".join(f'<tspan fill="{c}">{escape(t)}</tspan>' for t, c in line)
    code_svg.append(f'<text x="{cx0 + 64}" y="{y_line}" font-family="{MONO}" font-size="22" xml:space="preserve">{spans}</text>')
# output: close line with a soft fill, and its moving average
code_bottom = cy0 + 108 + (len(CODE) - 1) * 40 + 32
oy0, oy1, ox0, ox1 = code_bottom + 50, cy0 + ch - 40, cx0 + 40, cx0 + cw - 40
closes = [c[3] for c in cs]
sma = [sum(closes[max(0, i - 4): i + 1]) / len(closes[max(0, i - 4): i + 1]) for i in range(n)]
lo_c, hi_c = min(closes + sma), max(closes + sma)


def OY(v):
    return oy1 - (v - lo_c) / (hi_c - lo_c) * (oy1 - oy0)


def OX(i):
    return ox0 + (ox1 - ox0) * i / (n - 1)


close_pts = " ".join(f"{OX(i):.1f},{OY(v):.1f}" for i, v in enumerate(closes))
sma_pts = " ".join(f"{OX(i):.1f},{OY(v):.1f}" for i, v in enumerate(sma))
code_svg += [
    f'<path d="M{cx0 + 24} {code_bottom} h{cw - 48}" stroke="{WHITE}" stroke-opacity="0.08" stroke-dasharray="4 6"/>',
    f'<text x="{cx0 + 28}" y="{code_bottom + 30}" font-family="{MONO}" font-size="18" fill="{DIM}">Out:</text>',
    f'<polygon points="{ox0},{oy1} {close_pts} {ox1},{oy1}" fill="url(#area)"/>',
    f'<polyline points="{close_pts}" fill="none" stroke="{GREEN}" stroke-width="3" stroke-linejoin="round"/>',
    f'<polyline points="{sma_pts}" fill="none" stroke="{YELLOW}" stroke-width="3" stroke-linejoin="round" stroke-dasharray="10 7"/>',
    f'<circle cx="{OX(n - 1):.1f}" cy="{OY(closes[-1]):.1f}" r="7" fill="{GREEN}"/>',
    f'<circle cx="{OX(n - 1):.1f}" cy="{OY(closes[-1]):.1f}" r="16" fill="{GREEN}" fill-opacity="0.2"/>',
]
right_art = {"candles": "<g>" + "".join(candles) + f'</g><polyline points="{pts}" fill="none" stroke="{YELLOW}" stroke-opacity="0.7" stroke-width="3" stroke-linejoin="round"/>',
             "code": "".join(code_svg), "none": ""}[args.art]

has_art = args.art != "none"
# text block: left-aligned when there is art on the right, centered otherwise
tx, anchor = (124, "start") if has_art else (W / 2, "middle")

grid = [f'<line x1="{gx}" y1="0" x2="{gx}" y2="{H}"/>' for gx in range(0, W + 1, 80)]
grid += [f'<line x1="0" y1="{gy}" x2="{W}" y2="{gy}"/>' for gy in range(0, H + 1, 80)]

logo_paths = "".join(re.findall(r"<path[^>]*/>", LOGO.read_text()))

texts = []
y = 652
for line in args.tagline:
    texts.append(f'<text x="{tx}" y="{y}" text-anchor="{anchor}" font-family="{MONO}" font-size="28" fill="{WHITE}" fill-opacity="0.65">{escape(line)}</text>')
    y += 44
# tool tags: pills showing which libraries a post uses
widths = [22 + 17 * len(t) for t in args.tag]
x = tx if has_art else W / 2 - (sum(widths) + 14 * (len(widths) - 1)) / 2
y += 16
for tag in args.tag:
    w = 22 + 17 * len(tag)
    texts.append(
        f'<rect x="{x}" y="{y - 32}" width="{w}" height="46" rx="23" fill="{YELLOW}" fill-opacity="0.12" stroke="{YELLOW}" stroke-opacity="0.5"/>'
        f'<text x="{x + w / 2}" y="{y - 1}" text-anchor="middle" font-family="{MONO}" font-size="26" fill="{YELLOW}">{escape(tag)}</text>'
    )
    x += w + 14

svg = f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{NAVY_TOP}"/><stop offset="1" stop-color="{NAVY_BOTTOM}"/>
    </linearGradient>
    <radialGradient id="glow" cx="{0.72 if has_art else 0.5}" cy="0.5" r="0.55">
      <stop offset="0" stop-color="{GREEN}" stop-opacity="0.12"/><stop offset="1" stop-color="{GREEN}" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="fade" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset="0.5" stop-color="#fff" stop-opacity="1"/>
    </linearGradient>
    <linearGradient id="area" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{GREEN}" stop-opacity="0.35"/><stop offset="1" stop-color="{GREEN}" stop-opacity="0"/></linearGradient>
    <mask id="gridmask"><rect width="{W}" height="{H}" fill="url(#fade)"/></mask>
  </defs>
  <rect width="{W}" height="{H}" fill="url(#bg)"/>
  <rect width="{W}" height="{H}" fill="url(#glow)"/>
  <g stroke="#ffffff" stroke-opacity="0.05" stroke-width="1"{' mask="url(#gridmask)"' if has_art else ""}>{"".join(grid)}</g>
  {right_art}
  <g transform="translate({120 if has_art else W / 2 - 65} 150)">
    <rect width="130" height="130" rx="28" fill="{WHITE}" fill-opacity="0.06" stroke="{WHITE}" stroke-opacity="0.15"/>
    <svg x="12" y="12" width="106" height="106" viewBox="190 172 640 640">{logo_paths}</svg>
  </g>
  <text x="{116 if has_art else tx}" y="430" text-anchor="{anchor}" font-family="{SANS}" font-size="128" font-weight="900" letter-spacing="-3"><tspan fill="{BLUE}">Py</tspan><tspan fill="{YELLOW}">Trade</tspan></text>
  <text x="{tx}" y="525" text-anchor="{anchor}" font-family="{SANS}" font-size="64" font-weight="500" fill="{WHITE}">{escape(args.title)}</text>
  <rect x="{124 if has_art else W / 2 - 48}" y="570" width="96" height="6" rx="3" fill="{YELLOW}"/>
  {"".join(texts)}
  <text x="{tx}" y="{820 if args.tag else 770}" text-anchor="{anchor}" font-family="{MONO}" font-size="24" fill="{WHITE}" fill-opacity="0.35">pytrade.org</text>
</svg>'''
svg_path = Path(args.out + ".svg")
svg_path.write_text(svg, encoding="utf-8")
subprocess.run(["rsvg-convert", str(svg_path), "-o", args.out + ".png"], check=True)
svg_path.unlink()

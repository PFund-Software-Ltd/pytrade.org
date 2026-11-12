"""Generate 1600x900 (16:9) thumbnails for PyTrade.org.

Needs rsvg-convert, e.g. `brew install librsvg`. Writes <type>/static/<out>, relative to this file,
so it can be run from anywhere. Standard library only, so any Python 3.13+ runs it.

    # writes example/static/default_thumbnail.png
    uv run afterpython/generate_thumbnail.py --type example

    # code on the right, with tags; --art code asks you to paste the code snippet in the terminal
    uv run afterpython/generate_thumbnail.py --type example --tag pfeed --tag polars --art code \
        --out featured_thumbnail.png

    # or pipe the copied code (macOS clipboard) in, instead of pasting it
    pbpaste | uv run afterpython/generate_thumbnail.py --type example --art code --out featured_thumbnail

A default thumbnail is set as `[website.<type>].thumbnail = "default_thumbnail.png"` in afterpython.toml;
a post's own thumbnail is set in its frontmatter, e.g. `thumbnail: ./static/featured_thumbnail.png`.
The charts use a fixed random seed, so the same inputs always give the same image.
"""

import argparse
import io
import keyword
import os
import random
import re
import select
import subprocess
import sys
import tokenize
from html import escape
from pathlib import Path

HERE = Path(__file__).resolve().parent
LOGO = HERE / "static" / "logo.svg"
W, H = 1600, 900
NAVY_TOP, NAVY_BOTTOM = "#0A1428", "#142544"
BLUE, YELLOW, GREEN, RED, WHITE, DIM = "#1F6BA6", "#FED540", "#3DD9A4", "#FF6B47", "#F5F7FB", "#8A97B0"
# code colors after the Python logo: blue keywords and numbers, yellow calls and strings
KEYWORD, STRING = "#5A9FD4", "#FFE873"
SANS = "'Avenir Next', Inter, 'Helvetica Neue', sans-serif"
MONO = "Menlo, monospace"
# content type -> title, same as the website's listing titles
CONTENT_TYPES = {"blog": "Blog", "tutorial": "Tutorials", "example": "Examples", "guide": "Guides"}
TAGLINES = ["The Home for Python Trading", "Where Python Trading Begins"]


def prices(n=26):
    """A fixed random walk of (open, high, low, close) candles."""
    random.seed(7)
    p = 100.0
    cs = []
    for _ in range(n):
        o = p
        c = o + random.gauss(0.35, 2.2)
        hi = max(o, c) + abs(random.gauss(0, 1.2))
        lo = min(o, c) - abs(random.gauss(0, 1.2))
        cs.append((o, hi, lo, c))
        p = c
    return cs


def candles_svg():
    x0, x1, ytop, ybot = 860, 1500, 210, 690
    cs = prices()
    step = (x1 - x0) / len(cs)
    lo_all = min(x[2] for x in cs)
    hi_all = max(x[1] for x in cs)

    def Y(v):
        return ybot - (v - lo_all) / (hi_all - lo_all) * (ybot - ytop)

    out = []
    for i, (o, hi, lo, c) in enumerate(cs):
        cx = x0 + step * (i + 0.5)
        col = GREEN if c >= o else RED
        bw = step * 0.56
        top, bot = Y(max(o, c)), Y(min(o, c))
        out.append(f'<line x1="{cx:.1f}" y1="{Y(hi):.1f}" x2="{cx:.1f}" y2="{Y(lo):.1f}" stroke="{col}" stroke-width="3" stroke-linecap="round"/>')
        out.append(f'<rect x="{cx - bw / 2:.1f}" y="{top:.1f}" width="{bw:.1f}" height="{max(bot - top, 3):.1f}" rx="3" fill="{col}"/>')
    # close-price line through the candles
    pts = " ".join(f"{x0 + step * (i + 0.5):.1f},{Y(c[3]):.1f}" for i, c in enumerate(cs))
    out.append(f'<polyline points="{pts}" fill="none" stroke="{YELLOW}" stroke-opacity="0.7" stroke-width="3" stroke-linejoin="round"/>')
    return "".join(out)


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
            color = STRING
        elif tok.type == tokenize.NUMBER:
            color = KEYWORD
        elif tok.type == tokenize.COMMENT or tok.type == tokenize.OP:
            color = DIM
        elif tok.type == tokenize.NAME and keyword.iskeyword(text):
            color = KEYWORD
        elif tok.type == tokenize.NAME and nxt == "(":
            color = YELLOW
        else:
            color = WHITE
        row = r - 1
        if row >= len(lines):
            continue
        if c > cols[row]:
            spans[row].append((" " * (c - cols[row]), WHITE))
        spans[row].append((text.split("\n")[0], color))
        cols[row] = c + len(text)
    return spans


def code_svg(src):
    """An editor window with the code snippet, sized to the code and centered vertically."""
    code = highlight(src)
    if len(code) > 14 or max(len(line) for line in src.splitlines()) > 47:
        print("warning: the code is longer than ~14 lines or 47 columns and may not fit the editor window")
    cx0, cw = 760, 720  # 120px right margin, matching the text's left margin
    ch = 108 + (len(code) - 1) * 40 + 52
    cy0 = (H - ch) / 2
    out = [
        f'<rect x="{cx0 + 14}" y="{cy0 + 22}" width="{cw}" height="{ch}" rx="22" fill="#000" fill-opacity="0.35"/>',
        f'<rect x="{cx0}" y="{cy0}" width="{cw}" height="{ch}" rx="22" fill="#0D1830" stroke="{WHITE}" stroke-opacity="0.12"/>',
        f'<path d="M{cx0} {cy0 + 56} h{cw}" stroke="{WHITE}" stroke-opacity="0.08"/>',
    ]
    for i, col in enumerate([RED, YELLOW, GREEN]):
        out.append(f'<circle cx="{cx0 + 30 + i * 26}" cy="{cy0 + 28}" r="8" fill="{col}" fill-opacity="0.85"/>')
    for i, line in enumerate(code):
        y_line = cy0 + 108 + i * 40
        out.append(f'<text x="{cx0 + 28}" y="{y_line}" font-family="{MONO}" font-size="20" fill="{DIM}" fill-opacity="0.6">{i + 1}</text>')
        spans = "".join(f'<tspan fill="{c}">{escape(t)}</tspan>' for t, c in line)
        out.append(f'<text x="{cx0 + 64}" y="{y_line}" font-family="{MONO}" font-size="22" xml:space="preserve">{spans}</text>')
    return "".join(out)


def render(title, taglines, tags=(), art=""):
    """The thumbnail as SVG. `art` is the right-hand side's SVG; without it, the text is centered."""
    has_art = bool(art)
    # text block: left-aligned when there is art on the right, centered otherwise
    tx, anchor = (124, "start") if has_art else (W / 2, "middle")

    grid = [f'<line x1="{gx}" y1="0" x2="{gx}" y2="{H}"/>' for gx in range(0, W + 1, 80)]
    grid += [f'<line x1="0" y1="{gy}" x2="{W}" y2="{gy}"/>' for gy in range(0, H + 1, 80)]

    texts = []
    y = 652
    for line in taglines:
        texts.append(f'<text x="{tx}" y="{y}" text-anchor="{anchor}" font-family="{MONO}" font-size="28" fill="{WHITE}" fill-opacity="0.65">{escape(line)}</text>')
        y += 44
    # tags: pills, in a row that starts at the text's left edge or is centered
    if tags:
        widths = [22 + 17 * len(t) for t in tags]
        gap = 14
        px = tx if has_art else W / 2 - (sum(widths) + gap * (len(widths) - 1)) / 2
        y += 32
        for t, pw in zip(tags, widths):
            texts.append(
                f'<rect x="{px}" y="{y - 32}" width="{pw}" height="46" rx="23" fill="{YELLOW}" fill-opacity="0.12" stroke="{YELLOW}" stroke-opacity="0.5"/>'
                f'<text x="{px + pw / 2}" y="{y - 1}" text-anchor="middle" font-family="{MONO}" font-size="26" fill="{YELLOW}">{escape(t)}</text>'
            )
            px += pw + gap
        y += 30
    texts.append(f'<text x="{tx}" y="{y + 30}" text-anchor="{anchor}" font-family="{MONO}" font-size="24" fill="{WHITE}" fill-opacity="0.35">pytrade.org</text>')
    # center the text block vertically: it runs from the logo's top (150) to the footer's baseline
    dy = H / 2 - (150 + y + 30) / 2

    logo_paths = "".join(re.findall(r"<path[^>]*/>", LOGO.read_text()))
    logo_x = 120 if has_art else W / 2 - 65
    bar_x = 124 if has_art else W / 2 - 48
    glow_cx = 0.72 if has_art else 0.5
    # with art, the grid fades in from the left; without, it is uniform
    grid_mask = ' mask="url(#gridmask)"' if has_art else ""

    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}">
  <defs>
    <linearGradient id="bg" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="{NAVY_TOP}"/><stop offset="1" stop-color="{NAVY_BOTTOM}"/>
    </linearGradient>
    <radialGradient id="glow" cx="{glow_cx}" cy="0.5" r="0.55">
      <stop offset="0" stop-color="{GREEN}" stop-opacity="0.12"/><stop offset="1" stop-color="{GREEN}" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="fade" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset="0.5" stop-color="#fff" stop-opacity="1"/>
    </linearGradient>
    <mask id="gridmask"><rect width="{W}" height="{H}" fill="url(#fade)"/></mask>
  </defs>
  <rect width="{W}" height="{H}" fill="url(#bg)"/>
  <rect width="{W}" height="{H}" fill="url(#glow)"/>
  <g stroke="#ffffff" stroke-opacity="0.05" stroke-width="1"{grid_mask}>{"".join(grid)}</g>
  {art}
  <g transform="translate(0 {dy})">
  <!-- logo mark -->
  <g transform="translate({logo_x} 150)">
    <rect width="130" height="130" rx="28" fill="{WHITE}" fill-opacity="0.06" stroke="{WHITE}" stroke-opacity="0.15"/>
    <svg x="12" y="12" width="106" height="106" viewBox="190 172 640 640">{logo_paths}</svg>
  </g>
  <text x="{116 if has_art else tx}" y="430" text-anchor="{anchor}" font-family="{SANS}" font-size="128" font-weight="900" letter-spacing="-3"><tspan fill="{BLUE}">Py</tspan><tspan fill="{YELLOW}">Trade</tspan></text>
  <text x="{tx}" y="525" text-anchor="{anchor}" font-family="{SANS}" font-size="64" font-weight="500" fill="{WHITE}">{escape(title)}</text>
  <rect x="{bar_x}" y="570" width="96" height="6" rx="3" fill="{YELLOW}"/>
  {"".join(texts)}
  </g>
</svg>'''


def write_png(svg, path):
    path.parent.mkdir(parents=True, exist_ok=True)
    svg_path = path.with_suffix(".svg")
    svg_path.write_text(svg, encoding="utf-8")
    subprocess.run(["rsvg-convert", str(svg_path), "-o", str(path)], check=True)
    svg_path.unlink()
    print(f"Wrote {path.relative_to(HERE) if path.is_relative_to(HERE) else path}")


def read_code():
    """Read the code snippet from the terminal, or from piped input."""
    if not sys.stdin.isatty():
        src = sys.stdin.read()
    else:
        print("Paste the code snippet, then press Enter twice.")
        # the terminal hands over one line per read. A pasted snippet arrives all at once, so an empty
        # line with more input already waiting is part of the code; one typed after the paste ends it
        fd = sys.stdin.fileno()
        lines = []
        while chunk := os.read(fd, 65536).decode():
            lines += chunk.removesuffix("\n").split("\n")
            if lines[-1] == "" and not select.select([fd], [], [], 0.05)[0]:
                break
        src = "\n".join(lines)
    src = src.strip("\n") + "\n"
    if not src.strip():
        sys.exit("error: no code snippet was given")
    return src


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--type", required=True, choices=CONTENT_TYPES, help="content type: sets the title and writes to <type>/static/")
    parser.add_argument("--out", default="default_thumbnail.png", help="output filename in <type>/static/ (default: %(default)s)")
    parser.add_argument("--title", help="replaces the content type's title")
    parser.add_argument("--tagline", action="append", help=f"replaces the default taglines {TAGLINES}; repeat for more lines")
    parser.add_argument("--tag", action="append", default=[], help="a tag pill, e.g. a library the post uses; repeat for more tags")
    parser.add_argument("--art", choices=["none", "candles", "code"], default="none", help="right-hand side art; code asks for a code snippet")
    args = parser.parse_args()

    title = args.title or CONTENT_TYPES[args.type]
    art = {"none": lambda: "", "candles": candles_svg, "code": lambda: code_svg(read_code())}[args.art]()
    out = HERE / args.type / "static" / Path(args.out).with_suffix(".png")
    write_png(render(title, args.tagline or TAGLINES, args.tag, art), out)


if __name__ == "__main__":
    main()

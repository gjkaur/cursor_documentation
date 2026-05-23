"""Shared SVG helpers for Marp slide diagrams."""

from __future__ import annotations

import html
import re

RED = "#cc0000"
TEXT = "#1a1a1a"
MUTED = "#666666"
BG = "#ffffff"
PANEL = "#f7f7f7"
HEADER_BG = "#ffebeb"
BORDER = "#d0d0d0"
FONT = "Arial, Helvetica, sans-serif"
MONO = "Consolas, 'Courier New', monospace"

FS_TITLE = 22
FS_HEADING = 20
FS_BODY = 18
FS_SMALL = 16
FS_MONO = 19

HEADER_H = 54
HEADER_GAP = 16
ROW_H = 46
PANEL_PAD = 16


def slugify(text: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug[:60] or "diagram"


def _text_baseline_in_box(box_y: float, box_h: float, font_size: float) -> float:
    return box_y + box_h / 2 + font_size * 0.35


def monospace_panel_svg(lines: list[str], width: int = 920) -> str:
    """Render monospace ASCII block on a fixed character grid inside a panel."""
    pad_x = 24
    pad_y = 24
    char_w = FS_MONO * 0.62
    line_h = FS_MONO * 1.45
    max_len = max((len(line) for line in lines), default=0)
    content_w = max_len * char_w
    width = max(width, int(pad_x * 2 + content_w))
    height = int(pad_y * 2 + len(lines) * line_h)
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="{width}" height="{height}">',
        f'<rect width="{width}" height="{height}" rx="10" ry="10" fill="{PANEL}" '
        f'stroke="{BORDER}" stroke-width="2"/>',
    ]
    y = pad_y + FS_MONO * 0.85
    for line in lines:
        x = pad_x
        for ch in line:
            if ch != " ":
                parts.append(
                    f'<text x="{x + char_w / 2}" y="{y}" text-anchor="middle" '
                    f'font-family="{MONO}" font-size="{FS_MONO}" fill="{TEXT}">'
                    f"{html.escape(ch)}</text>"
                )
            x += char_w
        y += line_h
    parts.append("</svg>")
    return "\n".join(parts)


def lines_from_monospace_svg(svg_text: str) -> list[str]:
    """Recover source lines from a previously generated monospace panel SVG."""
    import html as html_mod

    rows: dict[float, list[tuple[float, str]]] = {}
    for match in re.finditer(
        r'<text x="([0-9.]+)" y="([0-9.]+)"[^>]*>([^<]*)</text>', svg_text
    ):
        x, y, ch = float(match.group(1)), float(match.group(2)), html_mod.unescape(match.group(3))
        rows.setdefault(y, []).append((x, ch))

    lines: list[str] = []
    char_w = FS_MONO * 0.62
    pad_x = 24
    for y in sorted(rows):
        chars = sorted(rows[y], key=lambda item: item[0])
        if len(chars) == 1 and len(chars[0][1]) > 1:
            lines.append(chars[0][1])
            continue
        max_col = 0
        grid: dict[int, str] = {}
        for x, ch in chars:
            col = round((x - pad_x - char_w / 2) / char_w)
            grid[col] = ch
            max_col = max(max_col, col)
        line = "".join(grid.get(i, " ") for i in range(max_col + 1)).rstrip()
        lines.append(line)
    return lines

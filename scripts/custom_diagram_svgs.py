#!/usr/bin/env python3
"""Hand-crafted SVG diagrams for modules 2+ (replace auto-generated ASCII panels)."""

from __future__ import annotations

from marp_svg_common import BORDER, FONT, FS_BODY, FS_SMALL, MUTED, PANEL, RED, TEXT


def _markers() -> str:
    return f"""
<defs>
  <marker id="arrow-end" viewBox="0 0 10 10" markerWidth="7" markerHeight="7"
          refX="9" refY="5" orient="auto" markerUnits="userSpaceOnUse">
    <path d="M0,1 L9,5 L0,9 Z" fill="{RED}"/>
  </marker>
  <marker id="arrow-start" viewBox="0 0 10 10" markerWidth="7" markerHeight="7"
          refX="1" refY="5" orient="auto" markerUnits="userSpaceOnUse">
    <path d="M9,1 L0,5 L9,9 Z" fill="{RED}"/>
  </marker>
</defs>"""


def mode_continuum_svg(width: int = 920) -> str:
    height = 290
    cx = width / 2
    left_x = 150
    right_x = width - 150
    mode_w, mode_h = 190, 54
    mode_y = 108
    chat_w, chat_h = 340, 54
    chat_x = cx - chat_w / 2
    chat_y = 196
    branch_y = chat_y - 18

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="{width}" height="{height}">',
        _markers(),
        f'<rect width="{width}" height="{height}" rx="10" ry="10" fill="{PANEL}" '
        f'stroke="{BORDER}" stroke-width="2"/>',
        f'<text x="{left_x}" y="42" text-anchor="middle" font-family="{FONT}" '
        f'font-size="{FS_BODY}" font-weight="700" fill="{RED}">READ-ONLY</text>',
        f'<text x="{right_x}" y="42" text-anchor="middle" font-family="{FONT}" '
        f'font-size="{FS_BODY}" font-weight="700" fill="{RED}">FULL ACTION</text>',
        f'<line x1="{left_x + 70}" y1="52" x2="{right_x - 70}" y2="52" stroke="{RED}" '
        f'stroke-width="2" marker-start="url(#arrow-start)" marker-end="url(#arrow-end)"/>',
        f'<line x1="{left_x}" y1="58" x2="{left_x}" y2="{mode_y - 8}" stroke="{RED}" '
        f'stroke-width="2" marker-end="url(#arrow-end)"/>',
        f'<line x1="{right_x}" y1="58" x2="{right_x}" y2="{mode_y - 8}" stroke="{RED}" '
        f'stroke-width="2" marker-end="url(#arrow-end)"/>',
    ]

    for box_x, label in ((left_x - mode_w / 2, "Ask Mode"), (right_x - mode_w / 2, "Agent Mode")):
        parts.append(
            f'<rect x="{box_x}" y="{mode_y}" width="{mode_w}" height="{mode_h}" rx="10" '
            f'fill="#ffffff" stroke="{RED}" stroke-width="2"/>'
        )
        parts.append(
            f'<text x="{box_x + mode_w / 2}" y="{mode_y + 34}" text-anchor="middle" '
            f'font-family="{FONT}" font-size="{FS_BODY}" font-weight="700" fill="{TEXT}">'
            f"{label}</text>"
        )

    parts.extend(
        [
            f'<path d="M{left_x},{mode_y + mode_h} L{left_x},{branch_y} L{cx - 80},{branch_y} '
            f'L{cx - 80},{chat_y}" fill="none" stroke="{RED}" stroke-width="2" '
            f'marker-end="url(#arrow-end)"/>',
            f'<path d="M{right_x},{mode_y + mode_h} L{right_x},{branch_y} L{cx + 80},{branch_y} '
            f'L{cx + 80},{chat_y}" fill="none" stroke="{RED}" stroke-width="2" '
            f'marker-end="url(#arrow-end)"/>',
            f'<rect x="{chat_x}" y="{chat_y}" width="{chat_w}" height="{chat_h}" rx="10" '
            f'fill="#ffffff" stroke="{RED}" stroke-width="2"/>',
            f'<text x="{cx}" y="{chat_y + 34}" text-anchor="middle" font-family="{FONT}" '
            f'font-size="{FS_BODY}" font-weight="700" fill="{TEXT}">Chat (middle ground)</text>',
            f'<text x="{cx}" y="{chat_y + chat_h + 28}" text-anchor="middle" '
            f'font-family="{FONT}" font-size="{FS_SMALL}" fill="{MUTED}">'
            f"(Can read, can&apos;t write)</text>",
            "</svg>",
        ]
    )
    return "\n".join(parts)


CUSTOM_DIAGRAMS: dict[str, callable] = {
    "module-03/the-mode-continuum.svg": mode_continuum_svg,
}

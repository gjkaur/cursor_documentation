#!/usr/bin/env python3
"""Hand-crafted SVG diagrams for modules 2+ (replace auto-generated ASCII panels)."""

from __future__ import annotations

from marp_svg_common import BORDER, FONT, FS_BODY, FS_SMALL, MONO, MUTED, PANEL, RED, TEXT, monospace_panel_svg


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


def cloud_handoff_flow_svg(width: int = 920) -> str:
    height = 360
    left_cx = 220
    right_cx = width - 220
    box_w, box_h = 230, 118
    box_y = 118
    left_x = left_cx - box_w / 2
    right_x = right_cx - box_w / 2
    prompt_y = 168
    result_y = 214
    web_y = 292

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" '
        f'width="{width}" height="{height}">',
        _markers(),
        f'<rect width="{width}" height="{height}" rx="10" ry="10" fill="{PANEL}" '
        f'stroke="{BORDER}" stroke-width="2"/>',
        f'<rect x="0" y="0" width="{width}" height="52" rx="10" fill="{PANEL}" '
        f'stroke="{BORDER}" stroke-width="2"/>',
        f'<line x1="0" y1="52" x2="{width}" y2="52" stroke="{BORDER}" stroke-width="2"/>',
        f'<text x="{width / 2}" y="34" text-anchor="middle" font-family="{FONT}" '
        f'font-size="{FS_BODY}" font-weight="700" fill="{RED}">CLOUD HANDOFF FLOW</text>',
        f'<text x="{left_cx}" y="88" text-anchor="middle" font-family="{FONT}" '
        f'font-size="{FS_BODY}" font-weight="700" fill="{TEXT}">Local Terminal</text>',
        f'<text x="{right_cx}" y="88" text-anchor="middle" font-family="{FONT}" '
        f'font-size="{FS_BODY}" font-weight="700" fill="{TEXT}">Cloud</text>',
        f'<rect x="{left_x}" y="{box_y}" width="{box_w}" height="{box_h}" rx="8" '
        f'fill="#ffffff" stroke="{BORDER}" stroke-width="2"/>',
        f'<rect x="{right_x}" y="{box_y}" width="{box_w}" height="{box_h}" rx="8" '
        f'fill="#ffffff" stroke="{BORDER}" stroke-width="2"/>',
    ]

    for cx, lines in (
        (left_cx, ("agent", "(interactive", "session)")),
        (right_cx, ("Cloud Agent", "(runs async)")),
    ):
        start_y = box_y + 38 if len(lines) == 3 else box_y + 52
        line_step = 28
        for i, line in enumerate(lines):
            parts.append(
                f'<text x="{cx}" y="{start_y + i * line_step}" text-anchor="middle" '
                f'font-family="{MONO}" font-size="{FS_BODY}" fill="{TEXT}">{line}</text>'
            )

    arrow_left = left_x + box_w + 12
    arrow_right = right_x - 12
    parts.extend(
        [
            f'<line x1="{arrow_left}" y1="{prompt_y}" x2="{arrow_right}" y2="{prompt_y}" '
            f'stroke="{RED}" stroke-width="2" marker-end="url(#arrow-end)"/>',
            f'<text x="{(arrow_left + arrow_right) / 2}" y="{prompt_y - 10}" '
            f'text-anchor="middle" font-family="{MONO}" font-size="{FS_SMALL}" fill="{MUTED}">'
            f"&amp; prompt</text>",
            f'<line x1="{arrow_right}" y1="{result_y}" x2="{arrow_left}" y2="{result_y}" '
            f'stroke="{RED}" stroke-width="2" marker-end="url(#arrow-end)"/>',
            f'<text x="{(arrow_left + arrow_right) / 2}" y="{result_y - 10}" '
            f'text-anchor="middle" font-family="{MONO}" font-size="{FS_SMALL}" fill="{MUTED}">'
            f"result</text>",
            f'<line x1="{right_cx}" y1="{box_y + box_h}" x2="{right_cx}" y2="{web_y - 28}" '
            f'stroke="{RED}" stroke-width="2" marker-end="url(#arrow-end)"/>',
            f'<text x="{right_cx}" y="{web_y}" text-anchor="middle" font-family="{MONO}" '
            f'font-size="{FS_BODY}" fill="{TEXT}">cursor.com/agents</text>',
            f'<text x="{right_cx}" y="{web_y + 28}" text-anchor="middle" '
            f'font-family="{FONT}" font-size="{FS_SMALL}" fill="{MUTED}">'
            f"(web/mobile access)</text>",
            "</svg>",
        ]
    )
    return "\n".join(parts)


def terminal_tool_flow_svg(width: int = 920) -> str:
    lines = [
        'User: "Run the tests and fix any failures"',
        "        ↓",
        "Agent: I'll run pytest",
        "        ↓",
        'Tool: Execute "pytest tests/"',
        "        ↓",
        'Tool returns: Exit code 1, "2 failed, 5 passed"',
        "        ↓",
        "Agent: Two tests failed. Let me read them.",
        "        ↓",
        "Agent: Fixes the code",
        "        ↓",
        "Agent: Rerunning tests...",
        "        ↓",
        "Agent: All tests passed.",
    ]
    return monospace_panel_svg(lines, width=width, max_panel_height=460)


CUSTOM_DIAGRAMS: dict[str, callable] = {
    "module-03/the-mode-continuum.svg": mode_continuum_svg,
    "module-03/terminal-tool-flow.svg": terminal_tool_flow_svg,
    "module-05/cloud-handoff-flow.svg": cloud_handoff_flow_svg,
}

#!/usr/bin/env python3
"""Generate SVG diagrams for module-01 Marp slides."""

from __future__ import annotations

from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "slides" / "assets" / "module-01"

RED = "#cc0000"
TEXT = "#1a1a1a"
MUTED = "#666666"
BG = "#ffffff"
PANEL = "#f7f7f7"
HEADER_BG = "#ffebeb"
BORDER = "#d0d0d0"
ACCENT = "#cc0000"
FONT = "Arial, Helvetica, sans-serif"
MONO = "Consolas, 'Courier New', monospace"

# Diagram typography (aligned with slide body ~32px default)
FS_TITLE = 26
FS_HEADING = 24
FS_BODY = 22
FS_SMALL = 20
FS_MONO = 23

HEADER_H = 54
HEADER_GAP = 16
ROW_H = 46
PANEL_PAD = 16


def _text_baseline_in_box(box_y: float, box_h: float, font_size: float) -> float:
    """SVG text y is the baseline; place single-line text vertically centered in a box."""
    return box_y + box_h / 2 + font_size * 0.35


def _fit_lines(text: str, max_width: float, font_size: float) -> list[str]:
    """Word-wrap text to fit within an estimated pixel width."""
    char_w = font_size * 0.52
    max_chars = max(6, int((max_width - 8) / char_w))
    words = text.split()
    lines: list[str] = []
    current = ""
    for word in words:
        trial = f"{current} {word}".strip()
        if len(trial) <= max_chars:
            current = trial
        else:
            if current:
                lines.append(current)
            current = word
    if current:
        lines.append(current)
    return lines if lines else [text]


def _markers() -> str:
    """Arrow markers: separate start/end tips for reliable bidirectional lines."""
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


def _v_connector(parts: list[str], x: float, y1: float, y2: float) -> None:
    parts.append(
        f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2}" stroke="{RED}" stroke-width="2" '
        f'marker-end="url(#arrow-end)"/>'
    )


def _h_bidirectional(parts: list[str], x1: float, x2: float, y: float) -> None:
    parts.append(
        f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="{RED}" stroke-width="2" '
        f'marker-start="url(#arrow-start)" marker-end="url(#arrow-end)"/>'
    )


def _h_arrow(parts: list[str], x1: float, x2: float, y: float) -> None:
    parts.append(
        f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke="{RED}" stroke-width="2" '
        f'marker-end="url(#arrow-end)"/>'
    )


def _header(title: str, width: float) -> str:
    return f"""
  <rect x="1" y="1" width="{width - 2}" height="{HEADER_H}" rx="8" ry="8" fill="{HEADER_BG}" stroke="{RED}" stroke-width="2"/>
  <text x="{width / 2}" y="{HEADER_H / 2 + FS_TITLE * 0.35}" text-anchor="middle" font-family="{FONT}" font-size="{FS_TITLE}" font-weight="700" fill="{RED}">{title}</text>
  <line x1="1" y1="{HEADER_H + 1}" x2="{width - 1}" y2="{HEADER_H + 1}" stroke="{BORDER}" stroke-width="1"/>
"""


def list_panel_svg(title: str, rows: list[tuple[str, str]], width: int = 920) -> str:
    content_top = HEADER_H + HEADER_GAP
    height = content_top + len(rows) * ROW_H + PANEL_PAD
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">',
        f'<rect width="{width}" height="{height}" rx="10" ry="10" fill="{BG}" stroke="{BORDER}" stroke-width="2"/>',
        _header(title, width),
    ]
    for i, (label, desc) in enumerate(rows):
        row_y = content_top + i * ROW_H
        fill = PANEL if i % 2 == 0 else BG
        parts.append(
            f'<rect x="12" y="{row_y}" width="{width - 24}" height="{ROW_H - 6}" rx="4" fill="{fill}"/>'
        )
        parts.append(
            f'<text x="28" y="{_text_baseline_in_box(row_y, ROW_H - 6, FS_BODY)}" '
            f'font-family="{FONT}" font-size="{FS_BODY}" fill="{TEXT}">'
            f'<tspan font-weight="700">{label}</tspan>'
            f'<tspan fill="{MUTED}">  →  </tspan>'
            f'<tspan font-family="{MONO}" font-size="{FS_MONO}">{desc}</tspan></text>'
        )
    parts.append("</svg>")
    return "\n".join(parts)


def flow_steps_svg(steps: list[str], width: int = 920) -> str:
    x, box_w = 40, width - 80
    line_h = FS_MONO * 1.35
    all_lines = [_fit_lines(step, box_w - 32, FS_MONO) for step in steps]
    max_lines = max(len(lines) for lines in all_lines)
    box_h = max(46, int(max_lines * line_h + 18))
    row_h = box_h + 28
    height = 24 + len(steps) * row_h
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">',
        _markers(),
    ]
    y = 20
    for i, step in enumerate(steps):
        lines = all_lines[i]
        parts.append(
            f'<rect x="{x}" y="{y}" width="{box_w}" height="{box_h}" rx="8" fill="{PANEL}" stroke="{BORDER}"/>'
        )
        block_h = len(lines) * line_h
        text_y = y + (box_h - block_h) / 2 + FS_MONO * 0.85
        for j, line in enumerate(lines):
            parts.append(
                f'<text x="{x + 16}" y="{text_y + j * line_h}" font-family="{MONO}" '
                f'font-size="{FS_MONO}" fill="{TEXT}">{line}</text>'
            )
        y += box_h
        if i < len(steps) - 1:
            _v_connector(parts, width / 2, y + 2, y + 22)
            y += row_h - box_h
    parts.append("</svg>")
    return "\n".join(parts)


def pyramid_svg(width: int = 920) -> str:
    height = 400
    layers = [
        ("Critical", "MUST include (~10–20%)", 220, "#cc0000"),
        ("Important", "Should include (~20–30%)", 320, "#e63333"),
        ("Helpful", "Nice to have (~30–40%)", 420, "#ff6666"),
        ("Low Value", "Omit if possible", 520, "#ffcccc"),
    ]
    cx = width / 2
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">',
        f'<text x="{cx}" y="32" text-anchor="middle" font-family="{FONT}" font-size="{FS_TITLE}" font-weight="700" fill="{RED}">Context Prioritization Pyramid</text>',
    ]
    y = 68
    for label, desc, w, color in layers:
        x = cx - w / 2
        parts.append(
            f'<polygon points="{cx},{y} {x},{y + 62} {x + w},{y + 62}" fill="{color}" stroke="{RED}" stroke-width="2"/>'
        )
        parts.append(
            f'<text x="{cx}" y="{y + 38}" text-anchor="middle" font-family="{FONT}" font-size="{FS_HEADING}" font-weight="700" fill="{BG if color != "#ffcccc" else TEXT}">{label}</text>'
        )
        parts.append(
            f'<text x="{cx + w / 2 + 14}" y="{y + 38}" font-family="{FONT}" font-size="{FS_BODY}" fill="{MUTED}">{desc}</text>'
        )
        y += 76
    parts.append("</svg>")
    return "\n".join(parts)


def attention_chart_svg(width: int = 920) -> str:
    height = 250
    bars = [
        ("BEGINNING", 0.92, "high"),
        ("MIDDLE", 0.28, "low"),
        ("END", 0.92, "high"),
    ]
    chart_x, chart_w = 180, 620
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">',
        f'<rect width="{width}" height="{height}" rx="10" fill="{BG}" stroke="{BORDER}" stroke-width="2"/>',
        f'<text x="28" y="36" font-family="{FONT}" font-size="{FS_TITLE}" font-weight="700" fill="{RED}">Context Position Attention</text>',
    ]
    y = 64
    for label, pct, level in bars:
        bar_w = int(chart_w * pct)
        parts.append(f'<text x="28" y="{y + 20}" font-family="{FONT}" font-size="{FS_BODY}" font-weight="700" fill="{TEXT}">{label}</text>')
        parts.append(f'<rect x="{chart_x}" y="{y}" width="{chart_w}" height="28" rx="4" fill="{PANEL}" stroke="{BORDER}"/>')
        parts.append(f'<rect x="{chart_x}" y="{y}" width="{bar_w}" height="28" rx="4" fill="{RED}"/>')
        parts.append(
            f'<text x="{chart_x + chart_w + 12}" y="{y + 20}" font-family="{FONT}" font-size="{FS_SMALL}" fill="{MUTED}">({level})</text>'
        )
        y += 52
    parts.append("</svg>")
    return "\n".join(parts)


def mcp_architecture_svg(width: int = 920) -> str:
    height = 230
    boxes = [
        (80, "AI Model", ["Claude, GPT, etc."]),
        (360, "MCP Host", ["Cursor, etc."]),
        (640, "Tools", ["Files, Terminal,", "Web, etc."]),
    ]
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">',
        _markers(),
    ]
    for x, title, lines in boxes:
        bw = 200
        parts.append(f'<rect x="{x}" y="40" width="{bw}" height="130" rx="10" fill="{PANEL}" stroke="{RED}" stroke-width="2"/>')
        parts.append(
            f'<text x="{x + bw / 2}" y="78" text-anchor="middle" font-family="{FONT}" font-size="{FS_HEADING}" font-weight="700" fill="{RED}">{title}</text>'
        )
        for i, line in enumerate(lines):
            parts.append(
                f'<text x="{x + bw / 2}" y="{106 + i * 26}" text-anchor="middle" font-family="{FONT}" font-size="{FS_BODY}" fill="{TEXT}">{line}</text>'
            )
    # Box edges: 80+200=280, 360, 360+200=560, 640
    _h_bidirectional(parts, 284, 356, 110)
    _h_bidirectional(parts, 564, 636, 110)
    parts.append("</svg>")
    return "\n".join(parts)


def agent_loop_svg(width: int = 920) -> str:
    cx = width / 2
    main_w = 440
    main_h = 58
    main_x = cx - main_w / 2
    v_gap = 34
    height = 490

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">',
        _markers(),
    ]

    def main_box(y: float, title: str, desc: str) -> float:
        parts.append(
            f'<rect x="{main_x}" y="{y}" width="{main_w}" height="{main_h}" rx="10" '
            f'fill="{PANEL}" stroke="{RED}" stroke-width="2"/>'
        )
        parts.append(
            f'<text x="{cx}" y="{y + 36}" text-anchor="middle" font-family="{FONT}" font-size="{FS_BODY}" fill="{TEXT}">'
            f'<tspan font-weight="700" fill="{RED}">{title}:</tspan><tspan> {desc}</tspan></text>'
        )
        return y + main_h

    def down_arrow(y1: float, y2: float, x: float = cx) -> None:
        _v_connector(parts, x, y1 + 4, y2 - 4)

    y = 20

    # GOAL
    y = main_box(y, "GOAL", "Add dark mode to entire app")
    down_arrow(y, y + v_gap)
    y += v_gap

    # PLAN
    y = main_box(y, "PLAN", "Break goal into steps")
    down_arrow(y, y + v_gap)
    y += v_gap

    # ACT ↔ OBSERVE (single container, two columns)
    pair_h = 86
    pair_w = 500
    pair_x = cx - pair_w / 2
    mid_x = cx
    parts.append(
        f'<rect x="{pair_x}" y="{y}" width="{pair_w}" height="{pair_h}" rx="10" '
        f'fill="{PANEL}" stroke="{RED}" stroke-width="2"/>'
    )
    # ACT column (left)
    parts.append(
        f'<text x="{pair_x + pair_w * 0.25}" y="{y + 30}" text-anchor="middle" '
        f'font-family="{FONT}" font-size="{FS_HEADING}" font-weight="700" fill="{RED}">ACT</text>'
    )
    parts.append(
        f'<text x="{pair_x + pair_w * 0.25}" y="{y + 60}" text-anchor="middle" '
        f'font-family="{FONT}" font-size="{FS_SMALL}" fill="{TEXT}">Run tools</text>'
    )
    # OBSERVE column (right)
    parts.append(
        f'<text x="{pair_x + pair_w * 0.75}" y="{y + 34}" text-anchor="middle" '
        f'font-family="{FONT}" font-size="{FS_HEADING}" font-weight="700" fill="{RED}">OBSERVE</text>'
    )
    parts.append(
        f'<text x="{pair_x + pair_w * 0.75}" y="{y + 60}" text-anchor="middle" '
        f'font-family="{FONT}" font-size="{FS_SMALL}" fill="{TEXT}">Tool call → result</text>'
    )
    # Bidirectional arrow between ACT and OBSERVE columns
    _h_bidirectional(parts, mid_x - 72, mid_x + 72, y + 42)

    y += pair_h
    down_arrow(y, y + v_gap)
    y += v_gap

    # THINK
    y = main_box(y, "THINK", "Evaluate progress, adjust")
    down_arrow(y, y + v_gap)
    y += v_gap

    # REPEAT
    main_box(y, "REPEAT", "Until goal done or blocked")

    parts.append("</svg>")
    return "\n".join(parts)


def horizontal_flow_svg(steps: list[str], width: int = 920) -> str:
    n = len(steps)
    margin = 36
    arrow_gap = 40
    usable = width - 2 * margin - (n - 1) * arrow_gap
    box_w = usable / n
    line_h = FS_BODY * 1.3
    all_lines = [_fit_lines(step, box_w - 20, FS_BODY) for step in steps]
    max_lines = max(len(lines) for lines in all_lines)
    box_h = max(56, int(max_lines * line_h + 20))
    height = box_h + 56
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">',
        _markers(),
    ]
    x = margin
    y = 28
    cy = y + box_h / 2
    for i, step in enumerate(steps):
        lines = all_lines[i]
        parts.append(
            f'<rect x="{x}" y="{y}" width="{box_w}" height="{box_h}" rx="8" '
            f'fill="{PANEL}" stroke="{RED}" stroke-width="2"/>'
        )
        block_h = len(lines) * line_h
        text_y = y + (box_h - block_h) / 2 + FS_BODY * 0.85
        for j, line in enumerate(lines):
            parts.append(
                f'<text x="{x + box_w / 2}" y="{text_y + j * line_h}" text-anchor="middle" '
                f'font-family="{FONT}" font-size="{FS_BODY}" fill="{TEXT}">{line}</text>'
            )
        x += box_w
        if i < n - 1:
            _h_arrow(parts, x + 6, x + arrow_gap - 6, cy)
            x += arrow_gap
    parts.append("</svg>")
    return "\n".join(parts)


def next_token_svg(width: int = 920) -> str:
    height = 290
    tokens = [("return", 85), ("print", 8), ("pass", 4), ("for", 2), ("Other", 1)]
    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">',
        f'<rect width="{width}" height="{height}" rx="10" fill="{BG}" stroke="{BORDER}" stroke-width="2"/>',
        f'<text x="28" y="36" font-family="{MONO}" font-size="{FS_MONO}" fill="{TEXT}">Input: "def calculate_sum(a, b):"</text>',
        f'<text x="28" y="66" font-family="{FONT}" font-size="{FS_BODY}" fill="{MUTED}">Model thinks: "What&apos;s most likely next?"</text>',
        f'<text x="28" y="98" font-family="{FONT}" font-size="{FS_HEADING}" font-weight="700" fill="{RED}">Probabilities</text>',
    ]
    y = 118
    max_w = 640
    for label, pct in tokens:
        bar_w = int(max_w * pct / 100)
        parts.append(f'<text x="40" y="{y + 18}" font-family="{MONO}" font-size="{FS_MONO}" fill="{TEXT}">{label}</text>')
        parts.append(f'<rect x="160" y="{y}" width="{max_w}" height="26" rx="4" fill="{PANEL}" stroke="{BORDER}"/>')
        parts.append(f'<rect x="160" y="{y}" width="{bar_w}" height="26" rx="4" fill="{RED}"/>')
        parts.append(f'<text x="{160 + max_w + 12}" y="{y + 18}" font-family="{FONT}" font-size="{FS_SMALL}" fill="{MUTED}">{pct}%</text>')
        y += 34
    parts.append("</svg>")
    return "\n".join(parts)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    files = {
        "next-token-prediction.svg": next_token_svg(),
        "factors-output.svg": list_panel_svg(
            "Factors That Shape Output",
            [
                ("1. Training Data", 'What the model "learned"'),
                ("2. Prompt", "Your instruction (most influential)"),
                ("3. Temperature", "Randomness level (0 = deterministic)"),
                ("4. Top-p / Top-k", "Token selection pool size"),
                ("5. System Prompt", "Persistent behavioral guidelines"),
                ("6. Context Window", 'What the model can "see"'),
                ("7. Model Architecture", "Different models, different biases"),
            ],
        ),
        "hallucination-causes.svg": list_panel_svg(
            "Root Causes of Hallucination",
            [
                ("Training Data Gaps", 'Model "guesses" when uncertain'),
                ("Probability Pressure", "Must output SOMETHING"),
                ("Pattern Overfitting", "Sees patterns that don't exist"),
                ("No True/False Circuit", "Models don't have truth checking"),
                ("Confidence Calibration", "Sounds confident when wrong"),
            ],
        ),
        "context-inputs.svg": list_panel_svg(
            "What Goes Into Context",
            [
                ("System Prompt", '"You are a helpful coding assistant"'),
                ("User Prompt", '"Fix this bug: ..."'),
                ("Code Files", "Current file, related files"),
                ("Conversation", "Previous exchanges"),
                ("Retrieved Docs", "Library documentation, examples"),
                ("Tool Outputs", "Results from search, file reads"),
                ("Constraints", '"Only use standard library"'),
            ],
        ),
        "context-pyramid.svg": pyramid_svg(),
        "lost-in-middle.svg": attention_chart_svg(),
        "tool-calling-flow.svg": flow_steps_svg(
            [
                'User: "What\'s the weather in Tokyo?"',
                "AI decides: need weather data",
                'AI outputs: tool_call { name: "get_weather", args: { city: "Tokyo" } }',
                'Your system executes get_weather("Tokyo")',
                "Result returned to AI",
                'AI: "The weather in Tokyo is 22°C and sunny"',
            ]
        ),
        "mcp-architecture.svg": mcp_architecture_svg(),
        "agent-loop.svg": agent_loop_svg(),
        "role-flow-agent-assisted.svg": horizontal_flow_svg(
            [
                "Developer defines intent",
                "Agent executes",
                "Developer reviews",
                "Agent iterates",
            ]
        ),
        "role-flow-traditional.svg": horizontal_flow_svg(
            ["Developer writes every line", "tests", "deploys"]
        ),
    }
    for name, svg in files.items():
        (OUT / name).write_text(svg, encoding="utf-8")
        print(f"Wrote {OUT / name}")


if __name__ == "__main__":
    main()

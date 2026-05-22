#!/usr/bin/env python3
"""
Clean Marp --pptx-editable exports for manual editing in PowerPoint.

LibreOffice often decomposes Gaia's diagonal background into hundreds of tiny
shapes. This script keeps text boxes, sets a flat Gaia-style background, and
removes decorative/non-text shapes.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from pptx import Presentation
from pptx.dml.color import RGBColor
from pptx.enum.shapes import MSO_SHAPE_TYPE
from pptx.enum.text import MSO_ANCHOR, MSO_AUTO_SIZE, PP_ALIGN
from pptx.oxml.xmlchemy import OxmlElement
from pptx.util import Emu, Pt

from marp_tables import extract_fenced_code_blocks, extract_markdown_tables, split_marp_slides


GAIA_CREAM = RGBColor(0xFF, 0xFF, 0xFF)
HEADING_RED = RGBColor(0xCC, 0x00, 0x00)
BODY_BLACK = RGBColor(0x00, 0x00, 0x00)
TABLE_HEADER_BG = RGBColor(0xFF, 0xEB, 0xEB)
TABLE_ROW_BG = RGBColor(0xF7, 0xF7, 0xF7)
TABLE_ROW_ALT_BG = RGBColor(0xFF, 0xFF, 0xFF)
TABLE_BORDER = "E0E0E0"
CODE_FONT = "Consolas"
CODE_FONT_PT = 18
CODE_BG = RGBColor(0xF4, 0xF4, 0xF4)
CODE_BORDER = RGBColor(0xD0, 0xD0, 0xD0)
CODE_TEXT = RGBColor(0x1A, 0x1A, 0x1A)
CODE_INSET = Emu(40000)
CODE_LINE_HEIGHT_PT = 24
CODE_CHAR_WIDTH_PT = 10.8
CODE_SIZE_BUFFER_PT = 8
MIN_BODY_FONT_PT = 20
HEADING_FONT_PT = 32
LEAD_H1_FONT_PT = 40
LEAD_H2_FONT_PT = 32
TABLE_FONT_PT = 14
TABLE_ROW_HEIGHT_PT = 22
TABLE_CHAR_WIDTH_PT = 8.4
TABLE_CELL_INSET = Emu(30000)
TABLE_SIZE_BUFFER_PT = 6
TABLE_MIN_COL_WIDTH = Emu(520000)
TABLE_MAX_COL_CHARS = 44
CHROME_MAX_FONT_PT = 15
HEADING_MIN_FONT_PT = 26
MIN_LAYOUT_FONT_PT = 14
OVERLAP_GAP = Emu(25000)
CONTENT_GAP = Emu(80000)
HEADING_BODY_GAP = Emu(150000)
FOOTER_SAFE_RATIO = 0.86
CONTENT_LEFT_RATIO = 0.061
HEADING_TOP_CONTENT = Emu(850000)
SECTION_CENTER_TOLERANCE = 0.08
MARP_HEADER_RE = re.compile(r"<!--\s*_header:\s*['\"](.+?)['\"]\s*-->")
MARP_FOOTER_RE = re.compile(r"<!--\s*_footer:\s*['\"](.+?)['\"]\s*-->")
CHROME_FONT_PT = 13.5
HEADER_CHROME_TOP_RATIO = 0.15
FOOTER_CHROME_TOP_RATIO = 0.85


def _shape_fill_rgb(shape) -> str | None:
    try:
        fill = shape.fill
        if fill.type is None or fill.type != 1:
            return None
        return str(fill.fore_color.rgb).upper()
    except Exception:
        return None


def _is_full_slide(shape, slide_width: int, slide_height: int, tolerance: float = 0.98) -> bool:
    w, h = int(shape.width), int(shape.height)
    return w >= slide_width * tolerance and h >= slide_height * tolerance


def _shape_text(shape) -> str:
    try:
        if not shape.has_text_frame:
            return ""
        return shape.text_frame.text.strip()
    except Exception:
        return ""


def _set_slide_background(slide, color: RGBColor = GAIA_CREAM) -> None:
    fill = slide.background.fill
    fill.solid()
    fill.fore_color.rgb = color


def _max_run_font_pt(shape) -> float | None:
    if not shape.has_text_frame:
        return None
    sizes = [
        run.font.size.pt
        for paragraph in shape.text_frame.paragraphs
        for run in paragraph.runs
        if run.font.size is not None
    ]
    return max(sizes) if sizes else None


def _is_chrome_shape(shape) -> bool:
    text = _shape_text(shape)
    if not text:
        return False
    if text.isdigit():
        return True
    if text.startswith("Module ") and " — " in text:
        return True
    max_pt = _max_run_font_pt(shape)
    if "Cursor Training Program" in text:
        return max_pt is None or max_pt <= CHROME_MAX_FONT_PT
    return max_pt is not None and max_pt <= CHROME_MAX_FONT_PT


def _scale_body_fonts(shape, min_pt: float = MIN_BODY_FONT_PT) -> None:
    _normalize_body_fonts(shape, min_pt=min_pt)


def _normalize_body_fonts(shape, min_pt: float = MIN_BODY_FONT_PT) -> None:
    if not shape.has_text_frame or _is_chrome_shape(shape):
        return
    if _is_heading_shape(shape):
        return
    if _is_code_shape(shape):
        return
    if _shape_uses_monospace(shape):
        for paragraph in shape.text_frame.paragraphs:
            for run in paragraph.runs:
                run.font.name = CODE_FONT
                run.font.size = Pt(min_pt)
                run.font.color.rgb = CODE_TEXT
        return
    for paragraph in shape.text_frame.paragraphs:
        for run in paragraph.runs:
            run.font.size = Pt(min_pt)
            run.font.color.rgb = BODY_BLACK


def _normalize_code_block_fonts(shape) -> None:
    if not _is_code_shape(shape) or not shape.has_text_frame:
        return
    for paragraph in shape.text_frame.paragraphs:
        for run in paragraph.runs:
            run.font.name = CODE_FONT
            run.font.size = Pt(CODE_FONT_PT)
            run.font.color.rgb = CODE_TEXT


def _shape_text_color(shape) -> RGBColor:
    text = _shape_text(shape)
    if text.startswith("Module ") and " — " in text:
        return HEADING_RED
    max_pt = _max_run_font_pt(shape)
    if max_pt is not None and max_pt >= HEADING_MIN_FONT_PT:
        return HEADING_RED
    return BODY_BLACK


def _apply_text_colors(shape) -> None:
    if not shape.has_text_frame or _shape_uses_monospace(shape):
        return
    color = _shape_text_color(shape)
    for paragraph in shape.text_frame.paragraphs:
        for run in paragraph.runs:
            run.font.color.rgb = color


def _is_heading_shape(shape) -> bool:
    if not shape.has_text_frame or _is_chrome_shape(shape) or _is_code_shape(shape):
        return False
    text = _shape_text(shape)
    if text.startswith("Cursor Training Program"):
        return False
    max_pt = _max_run_font_pt(shape)
    return max_pt is not None and max_pt >= HEADING_MIN_FONT_PT


def _parse_marp_frontmatter_chrome(markdown: str) -> tuple[str | None, str | None]:
    text = markdown.lstrip("\ufeff")
    if not text.startswith("---"):
        return None, None
    end = text.find("\n---\n", 3)
    if end == -1:
        return None, None
    header = footer = None
    for line in text[3:end].splitlines():
        stripped = line.strip()
        if stripped.startswith("header:"):
            header = stripped.split(":", 1)[1].strip().strip("'\"")
        elif stripped.startswith("footer:"):
            footer = stripped.split(":", 1)[1].strip().strip("'\"")
    return header, footer


def _cumulative_slide_chrome(
    md_slides: list[str],
    default_header: str | None,
    default_footer: str | None,
) -> list[tuple[str, str]]:
    header = default_header or ""
    footer = default_footer or ""
    chrome: list[tuple[str, str]] = []
    for slide_md in md_slides:
        header_match = MARP_HEADER_RE.search(slide_md)
        if header_match:
            header = header_match.group(1)
        footer_match = MARP_FOOTER_RE.search(slide_md)
        if footer_match:
            footer = footer_match.group(1)
        chrome.append((header, footer))
    return chrome


def _header_chrome_shape(slide, slide_height: int):
    header_line = int(slide_height * HEADER_CHROME_TOP_RATIO)
    for shape in slide.shapes:
        if not shape.has_text_frame or not _is_chrome_shape(shape):
            continue
        text = _shape_text(shape)
        if not text or text.isdigit():
            continue
        if int(shape.top) < header_line:
            return shape
    return None


def _footer_chrome_shape(slide, slide_height: int):
    footer_line = int(slide_height * FOOTER_CHROME_TOP_RATIO)
    for shape in slide.shapes:
        if not shape.has_text_frame or not _is_chrome_shape(shape):
            continue
        text = _shape_text(shape)
        if not text or text.isdigit():
            continue
        if int(shape.top) >= footer_line:
            return shape
    return None


def _set_chrome_shape_text(shape, text: str, color: RGBColor) -> None:
    if not shape.has_text_frame:
        return
    text_frame = shape.text_frame
    text_frame.clear()
    paragraph = text_frame.paragraphs[0]
    run = paragraph.add_run()
    run.text = text
    run.font.size = Pt(CHROME_FONT_PT)
    run.font.color.rgb = color
    run.font.bold = False


def _build_pptx_chrome_map(
    prs: Presentation,
    md_slides: list[str],
    chrome_per_md: list[tuple[str, str]],
) -> list[tuple[str, str]]:
    result: list[tuple[str, str]] = []
    md_index = 0
    pptx_index = 0
    current = chrome_per_md[0] if chrome_per_md else ("", "")

    while pptx_index < len(prs.slides):
        matched = False
        while md_index < len(md_slides):
            current = chrome_per_md[md_index]
            slide_index = _find_pptx_slide_index(
                prs, md_slides[md_index], start_index=pptx_index
            )
            if slide_index == pptx_index:
                result.append(chrome_per_md[md_index])
                md_index += 1
                pptx_index += 1
                matched = True
                break
            if slide_index is None:
                md_index += 1
                continue
            if slide_index > pptx_index:
                break
            md_index += 1
        if not matched:
            result.append(current)
            pptx_index += 1

    return result


def apply_slide_chrome_from_markdown(prs: Presentation, md_path: Path) -> int:
    markdown = md_path.read_text(encoding="utf-8")
    md_slides = split_marp_slides(markdown)
    default_header, default_footer = _parse_marp_frontmatter_chrome(markdown)
    chrome_per_md = _cumulative_slide_chrome(md_slides, default_header, default_footer)
    chrome_map = _build_pptx_chrome_map(prs, md_slides, chrome_per_md)
    slide_height = int(prs.slide_height)
    updated = 0

    for slide_index, (header, footer) in enumerate(chrome_map):
        if slide_index >= len(prs.slides):
            break
        slide = prs.slides[slide_index]
        header_shape = _header_chrome_shape(slide, slide_height)
        footer_shape = _footer_chrome_shape(slide, slide_height)
        if header_shape is not None and _shape_text(header_shape) != header:
            _set_chrome_shape_text(header_shape, header, HEADING_RED)
            updated += 1
        if footer_shape is not None and footer and _shape_text(footer_shape) != footer:
            _set_chrome_shape_text(footer_shape, footer, BODY_BLACK)
            updated += 1

    return updated


def _center_text_frame(text_frame) -> None:
    for paragraph in text_frame.paragraphs:
        paragraph.alignment = PP_ALIGN.CENTER


def _left_align_text_frame(text_frame) -> None:
    for paragraph in text_frame.paragraphs:
        paragraph.alignment = PP_ALIGN.LEFT


def _content_left_margin(slide_width: int) -> int:
    return int(slide_width * CONTENT_LEFT_RATIO)


def _center_shape_horizontally(shape, slide_width: int) -> None:
    shape.left = max(0, int((slide_width - int(shape.width)) // 2))


def _is_horizontally_centered(shape, slide_width: int) -> bool:
    center_x = int(shape.left) + int(shape.width) // 2
    return abs(center_x - slide_width // 2) < slide_width * SECTION_CENTER_TOLERANCE


def _is_module_lead_slide(slide) -> bool:
    if _is_course_title_slide(slide) or _is_lesson_lead_slide(slide):
        return False
    texts: list[str] = []
    has_large_title = False
    for shape in slide.shapes:
        if not shape.has_text_frame or _is_chrome_shape(shape):
            continue
        text = _shape_text(shape)
        if text:
            texts.append(text)
        max_pt = _max_run_font_pt(shape)
        if max_pt is not None and max_pt >= HEADING_FONT_PT - 2:
            has_large_title = True
    if not has_large_title:
        return False
    return any(re.search(r"Module \d+\s*[·•]", text) for text in texts)


def _module_lead_shapes(slide) -> tuple:
    title = module_line = tagline = None
    for shape in slide.shapes:
        if not shape.has_text_frame or _is_chrome_shape(shape):
            continue
        text = _shape_text(shape)
        if re.search(r"Module \d+\s*[·•]", text):
            module_line = shape
        elif (_max_run_font_pt(shape) or 0) >= HEADING_MIN_FONT_PT and title is None:
            title = shape
        elif text and tagline is None and shape is not title and shape is not module_line:
            tagline = shape
    return title, module_line, tagline


def _stack_section_shapes_centered(
    shapes: list,
    slide_height: int,
    slide_width: int,
    *,
    center_text: bool = True,
    gaps: list[int] | None = None,
) -> None:
    if not shapes:
        return
    if gaps is None:
        gaps = [int(Emu(100000)), int(Emu(80000))]

    for shape in shapes:
        _trim_oversized_body_textbox(shape)

    total_height = sum(int(shape.height) for shape in shapes)
    total_height += sum(gaps[: len(shapes) - 1])
    start_y = max(int(Emu(1400000)), int((slide_height - total_height) // 2))
    cursor = start_y
    for index, shape in enumerate(shapes):
        _center_shape_horizontally(shape, slide_width)
        shape.top = cursor
        if center_text and shape.has_text_frame:
            _center_text_frame(shape.text_frame)
        cursor += int(shape.height)
        if index < len(shapes) - 1:
            cursor += gaps[index]


def _align_content_slide(slide, slide_width: int) -> None:
    content_left = _content_left_margin(slide_width)

    for shape in _content_layout_shapes(slide):
        if shape.shape_type == MSO_SHAPE_TYPE.TABLE:
            shape.left = content_left
            continue
        if not shape.has_text_frame:
            continue
        _left_align_text_frame(shape.text_frame)
        if _is_heading_shape(shape):
            shape.left = content_left
        elif _is_horizontally_centered(shape, slide_width) or int(shape.left) < content_left:
            shape.left = content_left


def _format_module_lead_slide(slide, slide_height: int, slide_width: int) -> None:
    title, module_line, tagline = _module_lead_shapes(slide)
    specs = [
        (title, LEAD_H1_FONT_PT, True, HEADING_RED),
        (module_line, LEAD_H2_FONT_PT, False, HEADING_RED),
        (tagline, MIN_BODY_FONT_PT, False, BODY_BLACK),
    ]
    shapes: list = []
    for shape, target_pt, bold, color in specs:
        if shape is None:
            continue
        for paragraph in shape.text_frame.paragraphs:
            for run in paragraph.runs:
                run.font.size = Pt(target_pt)
                run.font.bold = bold
                run.font.color.rgb = color
        shapes.append(shape)

    _stack_section_shapes_centered(shapes, slide_height, slide_width)


def _is_course_title_slide(slide) -> bool:
    title = subtitle = False
    for shape in slide.shapes:
        if not shape.has_text_frame or _is_chrome_shape(shape):
            continue
        text = _shape_text(shape)
        if text == "Cursor Training Program":
            title = True
        if "AI-Assisted Development" in text:
            subtitle = True
    return title and subtitle


def _is_course_agenda_slide(slide) -> bool:
    heading = _pptx_slide_heading(slide)
    if not heading:
        return False
    return heading.startswith("course agenda") or heading.startswith("day 1 —") or heading.startswith("day 2 —")


def _is_lesson_lead_slide(slide) -> bool:
    for shape in slide.shapes:
        if not shape.has_text_frame or _is_chrome_shape(shape):
            continue
        if re.match(r"^Lesson \d+\.\d+$", _shape_text(shape).strip()):
            return True
    return False


def _is_lead_slide(slide) -> bool:
    if _is_course_title_slide(slide):
        return True
    if _is_lesson_lead_slide(slide):
        return True
    texts: list[str] = []
    has_large_title = False
    for shape in slide.shapes:
        if not shape.has_text_frame or _is_chrome_shape(shape):
            continue
        text = _shape_text(shape)
        if text:
            texts.append(text)
        max_pt = _max_run_font_pt(shape)
        if max_pt is not None and max_pt >= HEADING_FONT_PT - 2:
            has_large_title = True
    if not has_large_title:
        return False
    return any(re.search(r"Module \d+\s*[·•]", text) for text in texts)


def _normalize_slide_headings(slide) -> None:
    if _is_course_title_slide(slide):
        return
    if _is_lesson_lead_slide(slide):
        lesson_shape = None
        topic_shape = None
        for shape in slide.shapes:
            if not shape.has_text_frame or _is_chrome_shape(shape):
                continue
            text = _shape_text(shape).strip()
            if re.match(r"^Lesson \d+\.\d+$", text):
                lesson_shape = shape
            elif (
                lesson_shape is not None
                and shape is not lesson_shape
                and (_max_run_font_pt(shape) or 0) >= HEADING_MIN_FONT_PT
                and topic_shape is None
            ):
                topic_shape = shape
        if lesson_shape is not None:
            for paragraph in lesson_shape.text_frame.paragraphs:
                for run in paragraph.runs:
                    run.font.size = Pt(HEADING_FONT_PT)
                    run.font.bold = True
                    run.font.color.rgb = HEADING_RED
        if topic_shape is not None:
            for paragraph in topic_shape.text_frame.paragraphs:
                for run in paragraph.runs:
                    run.font.size = Pt(HEADING_FONT_PT)
                    run.font.bold = False
                    run.font.color.rgb = HEADING_RED
        return
    is_lead = _is_lead_slide(slide)
    for shape in slide.shapes:
        if not _is_heading_shape(shape):
            continue
        text = _shape_text(shape)
        if is_lead and re.search(r"Module \d+\s*[·•]", text):
            target_pt = LEAD_H2_FONT_PT
            bold = False
        elif is_lead:
            target_pt = LEAD_H1_FONT_PT
            bold = True
        else:
            target_pt = HEADING_FONT_PT
            bold = True

        for paragraph in shape.text_frame.paragraphs:
            for run in paragraph.runs:
                run.font.size = Pt(target_pt)
                run.font.bold = bold
                run.font.color.rgb = HEADING_RED


def _course_title_shapes(slide) -> tuple:
    title = subtitle = tagline = None
    for shape in slide.shapes:
        if not shape.has_text_frame or _is_chrome_shape(shape):
            continue
        text = _shape_text(shape)
        if text == "Cursor Training Program":
            title = shape
        elif "AI-Assisted Development" in text:
            subtitle = shape
        elif "Springpeople ·" in text or "2-day instructor" in text.lower():
            tagline = shape
    return title, subtitle, tagline


def _format_course_title_slide(slide, slide_height: int, slide_width: int) -> None:
    title, subtitle, tagline = _course_title_shapes(slide)
    if title is None:
        return

    specs = [
        (title, LEAD_H1_FONT_PT, True, HEADING_RED),
        (subtitle, LEAD_H2_FONT_PT, False, HEADING_RED),
        (tagline, MIN_BODY_FONT_PT, False, BODY_BLACK),
    ]
    stacked: list = []
    for shape, target_pt, bold, color in specs:
        if shape is None:
            continue
        for paragraph in shape.text_frame.paragraphs:
            for run in paragraph.runs:
                run.font.size = Pt(target_pt)
                run.font.bold = bold
                run.font.color.rgb = color
        stacked.append(shape)

    _stack_section_shapes_centered(stacked, slide_height, slide_width)


def _course_agenda_body_shape(slide):
    candidates = []
    for shape in slide.shapes:
        if not shape.has_text_frame or _is_chrome_shape(shape) or _is_heading_shape(shape):
            continue
        text = _shape_text(shape)
        if not text:
            continue
        if shape.shape_type == MSO_SHAPE_TYPE.TABLE:
            continue
        candidates.append(shape)
    if not candidates:
        return None
    return max(candidates, key=lambda shape: int(shape.top))


def _shrink_table_to_height(shape, max_height: int) -> None:
    table = shape.table
    if max_height <= 0 or int(shape.height) <= max_height:
        return
    scale = max_height / int(shape.height)
    for row in table.rows:
        row.height = max(int(Emu(70000)), int(int(row.height) * scale))
    font_pt = max(11, TABLE_FONT_PT * scale)
    line_pt = max(14, TABLE_ROW_HEIGHT_PT * scale)
    for row_idx in range(len(table.rows)):
        for col_idx in range(len(table.columns)):
            cell = table.cell(row_idx, col_idx)
            for paragraph in cell.text_frame.paragraphs:
                paragraph.line_spacing = Pt(line_pt)
                for run in paragraph.runs:
                    run.font.size = Pt(font_pt)
    shape.height = sum(int(row.height) for row in table.rows)


def _format_course_agenda_slide(slide, slide_height: int, slide_width: int) -> None:
    heading = None
    table = None
    for shape in slide.shapes:
        if _is_chrome_shape(shape):
            continue
        if shape.shape_type == MSO_SHAPE_TYPE.TABLE:
            table = shape
        elif shape.has_text_frame and _is_heading_shape(shape):
            heading = shape

    body = _course_agenda_body_shape(slide)
    heading_top = int(Emu(1200000))
    footer_line = int(slide_height * FOOTER_SAFE_RATIO)

    if heading is not None:
        heading.top = heading_top
        _trim_oversized_body_textbox(heading)
        for paragraph in heading.text_frame.paragraphs:
            for run in paragraph.runs:
                run.font.size = Pt(HEADING_FONT_PT)
                run.font.bold = True
                run.font.color.rgb = HEADING_RED
        cursor = int(heading.top) + int(heading.height) + HEADING_BODY_GAP
    else:
        cursor = heading_top

    if body is not None:
        _trim_oversized_body_textbox(body)
        for paragraph in body.text_frame.paragraphs:
            for run in paragraph.runs:
                run.font.size = Pt(MIN_BODY_FONT_PT)
                run.font.color.rgb = BODY_BLACK

    body_height = int(body.height) if body is not None else 0
    body_gap = int(CONTENT_GAP) if body is not None else 0
    max_table_bottom = footer_line - body_height - body_gap

    if table is not None:
        table.top = cursor
        table.left = max(0, int((slide_width - int(table.width)) // 2))
        available = max_table_bottom - int(table.top)
        _shrink_table_to_height(table, available)
        cursor = int(table.top) + int(table.height) + CONTENT_GAP

    if body is not None:
        body.top = min(cursor, footer_line - body_height)
        for paragraph in body.text_frame.paragraphs:
            for run in paragraph.runs:
                run.font.bold = "Total:" in paragraph.text


def _format_lesson_lead_slide(slide, slide_height: int, slide_width: int) -> None:
    ordered: list = []
    for shape in slide.shapes:
        if not shape.has_text_frame or _is_chrome_shape(shape):
            continue
        text = _shape_text(shape).strip()
        if re.match(r"^Lesson \d+\.\d+$", text):
            ordered.append((0, shape))
        elif (_max_run_font_pt(shape) or 0) >= HEADING_MIN_FONT_PT:
            ordered.append((1, shape))
        elif text:
            ordered.append((2, shape))
    ordered.sort(key=lambda item: item[0])
    shapes = [shape for _, shape in ordered]
    if not shapes:
        return

    for shape in shapes:
        _trim_oversized_body_textbox(shape)
        if (_max_run_font_pt(shape) or 0) < HEADING_MIN_FONT_PT:
            _normalize_body_fonts(shape)

    _stack_section_shapes_centered(shapes, slide_height, slide_width)


def _format_course_intro_slides(prs: Presentation) -> None:
    slide_height = int(prs.slide_height)
    slide_width = int(prs.slide_width)
    for slide in prs.slides:
        if _is_course_title_slide(slide):
            _format_course_title_slide(slide, slide_height, slide_width)
        elif _is_course_agenda_slide(slide):
            _format_course_agenda_slide(slide, slide_height, slide_width)


def _normalize_slide_formatting(slide) -> None:
    for shape in slide.shapes:
        if shape.shape_type == MSO_SHAPE_TYPE.TABLE:
            continue
        if shape.has_text_frame:
            if _is_code_shape(shape):
                _normalize_code_block_fonts(shape)
            elif not _is_chrome_shape(shape):
                if not _is_heading_shape(shape):
                    _normalize_body_fonts(shape)
    _normalize_slide_headings(slide)


def _normalize_presentation_formatting(prs: Presentation) -> None:
    for slide in prs.slides:
        _normalize_slide_formatting(slide)


def _normalize_text(text: str) -> str:
    text = re.sub(r"`([^`]*)`", r"\1", text)
    text = re.sub(r"\*\*", "", text)
    text = text.replace("→", "->")
    return " ".join(text.split()).lower()


def _markdown_slide_heading(slide_md: str) -> str | None:
    for line in slide_md.splitlines():
        if line.startswith("## "):
            return _normalize_text(line[3:])
    for line in slide_md.splitlines():
        if line.startswith("# "):
            return _normalize_text(line[2:])
    return None


def _pptx_slide_heading(slide) -> str | None:
    best_text: str | None = None
    best_size = 0.0
    for shape in slide.shapes:
        if not shape.has_text_frame or _is_chrome_shape(shape):
            continue
        text = _shape_text(shape).split("\n", 1)[0].strip()
        if not text:
            continue
        size = _max_run_font_pt(shape) or 0.0
        if size >= HEADING_MIN_FONT_PT and size >= best_size:
            best_size = size
            best_text = _normalize_text(text)
    return best_text


def _find_pptx_slide_index(
    prs: Presentation,
    slide_md: str,
    *,
    start_index: int = 0,
) -> int | None:
    target = _markdown_slide_heading(slide_md)
    if not target:
        return None

    for index in range(start_index, len(prs.slides)):
        heading = _pptx_slide_heading(prs.slides[index])
        if heading == target:
            return index

    best_index: int | None = None
    best_score = 0
    for index in range(start_index, len(prs.slides)):
        heading = _pptx_slide_heading(prs.slides[index])
        if not heading:
            continue
        if target in heading or heading in target:
            score = min(len(target), len(heading))
            if score > best_score:
                best_score = score
                best_index = index
    return best_index


def _cell_match_score(shape_text: str, cell_text: str) -> int:
    left = _normalize_text(shape_text)
    right = _normalize_text(cell_text)
    if not left or not right:
        return 0
    if left == right:
        return 10_000
    if left in right and len(left) < len(right) * 0.95:
        return len(left)
    if right in left and len(left) <= len(right) * 1.15:
        return len(right)
    return 0


def _table_cell_texts(table_data: list[list[str]]) -> list[str]:
    return [cell for row in table_data for cell in row if cell.strip()]


def _shape_matches_table(shape, table_data: list[list[str]], min_score: int = 10) -> bool:
    text = _shape_text(shape)
    if not text:
        return False
    score = max(
        (_cell_match_score(text, cell) for cell in _table_cell_texts(table_data)),
        default=0,
    )
    if score >= min_score:
        return True
    if len(text.strip()) <= 12:
        return score >= max(8, len(text.strip()))
    return False


def _content_text_shapes(slide) -> list:
    return [
        shape
        for shape in slide.shapes
        if shape.has_text_frame and _shape_text(shape) and not _is_chrome_shape(shape)
    ]


def _shape_bounds(shape) -> tuple[int, int, int, int]:
    return (
        int(shape.left),
        int(shape.top),
        int(shape.left + shape.width),
        int(shape.top + shape.height),
    )


def _bounds_for_shapes(shapes) -> tuple[int, int, int, int]:
    left = min(_shape_bounds(shape)[0] for shape in shapes)
    top = min(_shape_bounds(shape)[1] for shape in shapes)
    right = max(_shape_bounds(shape)[2] for shape in shapes)
    bottom = max(_shape_bounds(shape)[3] for shape in shapes)
    return left, top, right - left, bottom - top


def _shape_in_bounds(shape, bounds: tuple[int, int, int, int], padding: int = 80000) -> bool:
    left, top, width, height = bounds
    right = left + width
    bottom = top + height
    sl, st, sr, sb = _shape_bounds(shape)
    return (
        sl >= left - padding
        and sr <= right + padding
        and st >= top - padding
        and sb <= bottom + padding
    )


def _match_table_shapes(available, assigned_ids: set[int], table_data: list[list[str]]):
    matched = [
        shape
        for shape in available
        if id(shape) not in assigned_ids and _shape_matches_table(shape, table_data)
    ]
    if not matched:
        matched = [
            shape
            for shape in available
            if id(shape) not in assigned_ids
            and max(
                (
                    _cell_match_score(_shape_text(shape), cell)
                    for cell in _table_cell_texts(table_data)
                ),
                default=0,
            )
            >= 8
        ]
    if not matched:
        return []

    bounds = _bounds_for_shapes(matched)
    expanded = list(matched)
    for shape in available:
        if id(shape) in assigned_ids or shape in expanded:
            continue
        if _shape_in_bounds(shape, bounds):
            expanded.append(shape)
    return expanded


def _remove_shapes(shapes) -> None:
    for shape in shapes:
        element = shape._element
        element.getparent().remove(element)


def _set_cell_fill(cell, color: RGBColor) -> None:
    fill = cell.fill
    fill.solid()
    fill.fore_color.rgb = color


def _set_cell_border(cell, color: str = TABLE_BORDER, width: str = "12700") -> None:
    tc = cell._tc
    tc_pr = tc.get_or_add_tcPr()
    for edge in ("lnL", "lnR", "lnT", "lnB"):
        ln = OxmlElement(f"a:{edge}")
        ln.set("w", width)
        ln.set("cap", "flat")
        ln.set("cmpd", "sng")
        ln.set("algn", "ctr")

        solid_fill = OxmlElement("a:solidFill")
        srgb = OxmlElement("a:srgbClr")
        srgb.set("val", color)
        solid_fill.append(srgb)
        ln.append(solid_fill)

        dash = OxmlElement("a:prstDash")
        dash.set("val", "solid")
        ln.append(dash)

        tc_pr.append(ln)


def _clean_table_cell_text(text: str) -> str:
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"`(.+?)`", r"\1", text)
    text = re.sub(r"\*(.+?)\*", r"\1", text)
    return text.strip()


def _format_table_cell(
    cell,
    text: str,
    *,
    row_idx: int,
    header_row: bool,
) -> None:
    frame = cell.text_frame
    frame.clear()
    frame.word_wrap = True
    frame.margin_left = TABLE_CELL_INSET
    frame.margin_right = TABLE_CELL_INSET
    frame.margin_top = Emu(15000)
    frame.margin_bottom = Emu(15000)
    paragraph = frame.paragraphs[0]
    paragraph.line_spacing = Pt(TABLE_ROW_HEIGHT_PT)
    paragraph.space_before = Pt(0)
    paragraph.space_after = Pt(0)
    run = paragraph.add_run()
    run.text = _clean_table_cell_text(text)
    run.font.size = Pt(TABLE_FONT_PT)
    run.font.bold = header_row
    run.font.color.rgb = HEADING_RED if header_row else BODY_BLACK

    if header_row:
        fill_color = TABLE_HEADER_BG
    elif row_idx % 2 == 1:
        fill_color = TABLE_ROW_BG
    else:
        fill_color = TABLE_ROW_ALT_BG

    _set_cell_fill(cell, fill_color)
    _set_cell_border(cell)


def _table_dimensions(
    table_data: list[list[str]],
    *,
    max_width: int | None = None,
) -> tuple[list[int], list[int]]:
    rows = len(table_data)
    cols = max(len(row) for row in table_data)
    char_width = int(Pt(TABLE_CHAR_WIDTH_PT).emu)
    line_height = int(Pt(TABLE_ROW_HEIGHT_PT).emu)
    inset = int(TABLE_CELL_INSET) * 2
    buffer = int(Pt(TABLE_SIZE_BUFFER_PT).emu)

    col_max_chars: list[int] = []
    for col_idx in range(cols):
        max_chars = 0
        for row in table_data:
            value = _clean_table_cell_text(row[col_idx] if col_idx < len(row) else "")
            max_chars = max(max_chars, len(value))
        col_max_chars.append(max_chars)

    col_widths: list[int] = []
    for max_chars in col_max_chars:
        effective_chars = min(max_chars, TABLE_MAX_COL_CHARS)
        width = max(int(TABLE_MIN_COL_WIDTH), effective_chars * char_width + inset + buffer)
        col_widths.append(width)

    if max_width is not None:
        while sum(col_widths) > max_width:
            widest = max(range(cols), key=lambda idx: col_widths[idx])
            reduced = col_widths[widest] - char_width
            if reduced <= int(TABLE_MIN_COL_WIDTH):
                break
            col_widths[widest] = max(int(TABLE_MIN_COL_WIDTH), reduced)

    row_heights: list[int] = []
    for row in table_data:
        max_lines = 1
        for col_idx in range(cols):
            value = _clean_table_cell_text(row[col_idx] if col_idx < len(row) else "")
            usable = max(char_width, col_widths[col_idx] - inset)
            chars_per_line = max(1, usable // char_width)
            line_count = max(1, (len(value) + chars_per_line - 1) // chars_per_line)
            max_lines = max(max_lines, line_count)
        row_heights.append(max_lines * line_height + inset + buffer)

    return col_widths, row_heights


def _insert_table(
    slide,
    table_data: list[list[str]],
    bounds: tuple[int, int, int, int],
    *,
    slide_width: int | None = None,
) -> None:
    rows = len(table_data)
    cols = max(len(row) for row in table_data)
    left, top, _, _ = bounds
    max_width = int(slide_width * 0.92) if slide_width else None
    col_widths, row_heights = _table_dimensions(table_data, max_width=max_width)
    width = sum(col_widths)
    height = sum(row_heights)

    graphic = slide.shapes.add_table(rows, cols, left, top, width, height)
    table = graphic.table

    for col_idx, col_width in enumerate(col_widths):
        table.columns[col_idx].width = col_width
    for row_idx, row_height in enumerate(row_heights):
        table.rows[row_idx].height = row_height

    for row_idx, row in enumerate(table_data):
        for col_idx in range(cols):
            value = row[col_idx] if col_idx < len(row) else ""
            _format_table_cell(
                table.cell(row_idx, col_idx),
                value,
                row_idx=row_idx,
                header_row=row_idx == 0,
            )


def _rebuild_slide_tables(slide, tables: list[list[list[str]]], *, slide_width: int | None = None) -> int:
    rebuilt = 0
    assigned_ids: set[int] = set()
    available = _content_text_shapes(slide)

    for table_data in tables:
        matched = _match_table_shapes(available, assigned_ids, table_data)
        if not matched:
            continue

        for shape in matched:
            assigned_ids.add(id(shape))

        bounds = _bounds_for_shapes(matched)
        _remove_shapes(matched)
        _insert_table(slide, table_data, bounds, slide_width=slide_width)
        rebuilt += 1

    return rebuilt


def _shape_uses_monospace(shape) -> bool:
    if not shape.has_text_frame:
        return False
    for paragraph in shape.text_frame.paragraphs:
        for run in paragraph.runs:
            name = (run.font.name or "").lower()
            if "consolas" in name or "courier" in name or "mono" in name:
                return True
    return False


def _shape_has_code_fill(shape) -> bool:
    try:
        if shape.fill.type and str(shape.fill.fore_color.rgb).upper() == "F4F4F4":
            return True
    except Exception:
        pass
    return False


def _is_inline_monospace_shape(shape) -> bool:
    if not shape.has_text_frame or _is_chrome_shape(shape):
        return False
    if not _shape_uses_monospace(shape) or _shape_has_code_fill(shape):
        return False
    text = _shape_text(shape)
    if not text or "\n" in text:
        return False
    return len(text) <= 100


def _is_code_shape(shape) -> bool:
    if _is_chrome_shape(shape):
        return False
    if _is_inline_monospace_shape(shape):
        return False
    if _shape_uses_monospace(shape):
        return True
    if _shape_has_code_fill(shape):
        return True
    return False


def _text_matches_code_line(shape_text: str, code_line: str) -> bool:
    left = shape_text.rstrip()
    right = code_line.rstrip()
    if left == right:
        return True
    return _normalize_text(left) == _normalize_text(right)


def _code_block_match_score(shape_text: str, code_text: str) -> int:
    if not shape_text.strip() or not code_text.strip():
        return 0
    if _normalize_text(shape_text) == _normalize_text(code_text):
        return 10_000

    shape_lines = [line.rstrip() for line in shape_text.splitlines()]
    code_lines = [line.rstrip() for line in code_text.splitlines() if line.strip()]
    if not shape_lines or not code_lines:
        return 0

    score = 0
    for code_line in code_lines:
        for shape_line in shape_lines:
            if _text_matches_code_line(shape_line, code_line):
                score += max(len(code_line), 8)
                break
    return score


def _match_code_block_shapes(
    available,
    assigned_ids: set[int],
    code_text: str,
) -> list:
    code_lines = [line.rstrip() for line in code_text.splitlines() if line.strip()]
    if not code_lines:
        return []

    line_matched = []
    for shape in available:
        if id(shape) in assigned_ids or _is_heading_shape(shape):
            continue
        shape_lines = [line.rstrip() for line in _shape_text(shape).splitlines() if line.strip()]
        if any(
            _text_matches_code_line(shape_line, code_line)
            for shape_line in shape_lines
            for code_line in code_lines
        ):
            line_matched.append(shape)

    if not line_matched:
        min_score = max(40, sum(len(line) for line in code_lines) // 4)
        line_matched = [
            shape
            for shape in available
            if id(shape) not in assigned_ids
            and _code_block_match_score(_shape_text(shape), code_text) >= min_score
        ]

    if not line_matched:
        return []

    bounds = _bounds_for_shapes(line_matched)
    expanded = list(line_matched)
    for shape in available:
        if id(shape) in assigned_ids or shape in expanded:
            continue
        if _shape_in_bounds(shape, bounds, padding=120000) and (
            _shape_uses_monospace(shape)
            or _shape_has_code_fill(shape)
            or any(
                _text_matches_code_line(line.rstrip(), code_line)
                for line in _shape_text(shape).splitlines()
                for code_line in code_lines
            )
        ):
            expanded.append(shape)

    matched_lines = set()
    for shape in expanded:
        for shape_line in _shape_text(shape).splitlines():
            for code_line in code_lines:
                if _text_matches_code_line(shape_line.rstrip(), code_line):
                    matched_lines.add(code_line)

    required = max(2, len(code_lines) // 3)
    if len(matched_lines) < required:
        return []

    return expanded


def _code_lines(code_text: str) -> list[str]:
    if not code_text:
        return [""]
    return code_text.split("\n")


def _format_code_text_frame(text_frame, code_text: str) -> None:
    text_frame.clear()
    text_frame.word_wrap = False
    text_frame.auto_size = MSO_AUTO_SIZE.NONE
    text_frame.vertical_anchor = MSO_ANCHOR.TOP

    for index, line in enumerate(_code_lines(code_text)):
        paragraph = text_frame.paragraphs[0] if index == 0 else text_frame.add_paragraph()
        paragraph.alignment = PP_ALIGN.LEFT
        paragraph.space_before = Pt(0)
        paragraph.space_after = Pt(0)
        paragraph.line_spacing = Pt(CODE_LINE_HEIGHT_PT)
        run = paragraph.add_run()
        run.text = line
        run.font.name = CODE_FONT
        run.font.size = Pt(CODE_FONT_PT)
        run.font.color.rgb = CODE_TEXT


def _code_block_size(code_text: str, max_width: int | None = None) -> tuple[int, int]:
    lines = _code_lines(code_text)
    line_count = len(lines)
    max_chars = max(len(line) for line in lines)

    line_height = int(Pt(CODE_LINE_HEIGHT_PT).emu)
    char_width = int(Pt(CODE_CHAR_WIDTH_PT).emu)
    frame_pad = int(CODE_INSET) * 2
    buffer = int(Pt(CODE_SIZE_BUFFER_PT).emu)

    width = max_chars * char_width + frame_pad + buffer
    height = line_count * line_height + frame_pad + buffer

    if max_width is not None:
        width = min(width, max_width)

    return width, height


def _insert_code_block(
    slide,
    code_text: str,
    bounds: tuple[int, int, int, int],
    *,
    slide_width: int | None = None,
) -> None:
    left, top, _, _ = bounds
    max_width = int(slide_width * 0.9) if slide_width else None
    width, height = _code_block_size(code_text, max_width=max_width)

    textbox = slide.shapes.add_textbox(left, top, width, height)
    textbox.fill.solid()
    textbox.fill.fore_color.rgb = CODE_BG
    textbox.line.color.rgb = CODE_BORDER
    textbox.line.width = Pt(0.75)

    frame = textbox.text_frame
    frame.margin_left = CODE_INSET
    frame.margin_right = CODE_INSET
    frame.margin_top = CODE_INSET
    frame.margin_bottom = CODE_INSET
    _format_code_text_frame(frame, code_text)


def _rebuild_slide_code_blocks(slide, code_blocks: list[str], *, slide_width: int | None = None) -> int:
    rebuilt = 0
    assigned_ids: set[int] = set()
    available = _content_text_shapes(slide)

    for code_text in code_blocks:
        matched = _match_code_block_shapes(available, assigned_ids, code_text)
        if not matched:
            continue

        for shape in matched:
            assigned_ids.add(id(shape))

        bounds = _bounds_for_shapes(matched)
        _remove_shapes(matched)
        _insert_code_block(slide, code_text, bounds, slide_width=slide_width)
        rebuilt += 1

    return rebuilt


def rebuild_code_blocks_from_markdown(prs: Presentation, md_path: Path) -> int:
    markdown = md_path.read_text(encoding="utf-8")
    md_slides = split_marp_slides(markdown)
    rebuilt = 0
    slide_width = int(prs.slide_width)
    search_from = 0

    for slide_md in md_slides:
        code_blocks = extract_fenced_code_blocks(slide_md)
        if not code_blocks:
            continue
        slide_index = _find_pptx_slide_index(prs, slide_md, start_index=search_from)
        if slide_index is None:
            continue
        search_from = slide_index + 1
        rebuilt += _rebuild_slide_code_blocks(
            prs.slides[slide_index], code_blocks, slide_width=slide_width
        )

    return rebuilt


def _content_layout_shapes(slide) -> list:
    shapes = []
    for shape in slide.shapes:
        if _is_chrome_shape(shape):
            continue
        if shape.shape_type == MSO_SHAPE_TYPE.TABLE:
            shapes.append(shape)
        elif shape.has_text_frame and _shape_text(shape):
            shapes.append(shape)
    return shapes


def _horizontal_overlap(first, second, gap: int = 0) -> bool:
    left_a, _, right_a, _ = _shape_bounds(first)
    left_b, _, right_b, _ = _shape_bounds(second)
    return not (right_a + gap <= left_b or right_b + gap <= left_a)


def _trim_oversized_body_textbox(shape) -> None:
    if not shape.has_text_frame or _is_chrome_shape(shape) or _is_code_shape(shape):
        return

    is_heading = _is_heading_shape(shape)
    line_count = 0
    max_pt = HEADING_FONT_PT if is_heading else MIN_BODY_FONT_PT
    for paragraph in shape.text_frame.paragraphs:
        text = paragraph.text or "".join(run.text for run in paragraph.runs)
        if text.strip():
            line_count += 1
        for run in paragraph.runs:
            if run.font.size:
                max_pt = max(max_pt, run.font.size.pt)

    if line_count == 0:
        return

    line_height = int(Pt(max(max_pt * 1.2, MIN_BODY_FONT_PT)).emu)
    padding = int(Emu(40000))
    needed = line_count * line_height + padding
    if int(shape.height) > needed + (0 if is_heading else padding):
        shape.height = needed + padding


def _trim_oversized_body_textboxes(slide) -> None:
    for shape in slide.shapes:
        _trim_oversized_body_textbox(shape)


def _layout_shapes(slide) -> list:
    return [
        shape
        for shape in _content_layout_shapes(slide)
        if not _is_code_shape(shape)
    ]


def _rects_overlap(
    left_a: int,
    top_a: int,
    right_a: int,
    bottom_a: int,
    left_b: int,
    top_b: int,
    right_b: int,
    bottom_b: int,
    gap: int = 0,
) -> bool:
    return not (
        right_a + gap <= left_b
        or right_b + gap <= left_a
        or bottom_a + gap <= top_b
        or bottom_b + gap <= top_a
    )


def _shape_pair_overlaps(first, second, gap: int = 0) -> bool:
    a = _shape_bounds(first)
    b = _shape_bounds(second)
    return _rects_overlap(a[0], a[1], a[2], a[3], b[0], b[1], b[2], b[3], gap)


def _slide_has_layout_issues(slide, slide_height: int) -> bool:
    shapes = _content_layout_shapes(slide)
    footer_line = int(slide_height * FOOTER_SAFE_RATIO)
    if any(_shape_bounds(shape)[3] > footer_line for shape in shapes):
        return True
    for index, first in enumerate(shapes):
        for second in shapes[index + 1 :]:
            if not _horizontal_overlap(first, second):
                continue
            gap = CONTENT_GAP
            if _is_heading_shape(first) and _is_heading_shape(second):
                gap = Emu(20000)
            if _shape_pair_overlaps(first, second, gap):
                return True
    return False


def _resolve_content_flow(
    slide,
    slide_height: int,
    *,
    content_order: list | None = None,
) -> None:
    footer_line = int(slide_height * FOOTER_SAFE_RATIO)
    heading_top = int(HEADING_TOP_CONTENT)

    if _is_course_agenda_slide(slide):
        return

    if _is_lesson_lead_slide(slide):
        return

    if _is_module_lead_slide(slide):
        return

    all_shapes = _content_layout_shapes(slide)
    headings = [shape for shape in all_shapes if _is_heading_shape(shape)]
    if content_order is None:
        content = [shape for shape in all_shapes if not _is_heading_shape(shape)]
        content.sort(key=lambda shape: (int(shape.top), int(shape.left)))
    else:
        content = list(content_order)

    if headings:
        primary = min(headings, key=lambda shape: int(shape.top))
        primary.top = heading_top
        cursor = int(primary.top) + int(primary.height) + HEADING_BODY_GAP
        stacked = sorted(headings, key=lambda shape: int(shape.top))
        for index in range(1, len(stacked)):
            previous = stacked[index - 1]
            current = stacked[index]
            min_top = _shape_bounds(previous)[3] + Emu(20000)
            if int(current.top) < min_top:
                current.top = min_top
            cursor = max(cursor, int(current.top) + int(current.height) + HEADING_BODY_GAP)
    else:
        cursor = heading_top

    for shape in content:
        shape.top = cursor
        cursor = int(shape.top) + int(shape.height) + CONTENT_GAP

    for _ in range(12):
        shapes = _content_layout_shapes(slide)
        if not shapes:
            return
        max_bottom = max(_shape_bounds(shape)[3] for shape in shapes)
        if max_bottom <= footer_line:
            return
        shift = max_bottom - footer_line + Emu(40000)
        for shape in shapes:
            shape.top = max(0, int(shape.top) - shift)


def _fit_oversized_code_blocks(slide, slide_height: int) -> None:
    footer_line = int(slide_height * FOOTER_SAFE_RATIO)

    for shape in slide.shapes:
        if not _is_code_shape(shape):
            continue

        max_bottom = footer_line - int(CONTENT_GAP)
        available = max_bottom - int(shape.top)
        if available <= 0 or int(shape.height) <= available:
            continue

        scale = available / int(shape.height)
        font_pt = max(13, CODE_FONT_PT * scale)
        line_pt = max(16, CODE_LINE_HEIGHT_PT * scale)
        line_count = max(1, len(_code_lines(_shape_text(shape))))

        for paragraph in shape.text_frame.paragraphs:
            paragraph.line_spacing = Pt(line_pt)
            for run in paragraph.runs:
                run.font.size = Pt(font_pt)

        frame_pad = int(CODE_INSET) * 2
        buffer = int(Pt(CODE_SIZE_BUFFER_PT).emu)
        line_height = int(Pt(line_pt).emu)
        shape.height = min(available, line_count * line_height + frame_pad + buffer)


def _shrink_table_fonts(shape, delta_pt: float) -> None:
    if shape.shape_type != MSO_SHAPE_TYPE.TABLE:
        return
    table = shape.table
    for row_idx in range(len(table.rows)):
        for col_idx in range(len(table.columns)):
            cell = table.cell(row_idx, col_idx)
            for paragraph in cell.text_frame.paragraphs:
                for run in paragraph.runs:
                    if run.font.size:
                        run.font.size = Pt(max(10, run.font.size.pt + delta_pt))


def _shrink_shape_fonts(shape, delta_pt: float) -> None:
    if not shape.has_text_frame or _is_code_shape(shape) or _is_heading_shape(shape):
        return
    shape.text_frame.word_wrap = True
    for paragraph in shape.text_frame.paragraphs:
        for run in paragraph.runs:
            if run.font.size and run.font.size.pt > MIN_LAYOUT_FONT_PT:
                run.font.size = Pt(max(MIN_LAYOUT_FONT_PT, run.font.size.pt + delta_pt))


def _nudge_shape_up(shape, amount: int) -> None:
    shape.top = max(0, int(shape.top) - amount)


def _fix_stacked_tables(slide) -> None:
    tables = [
        shape for shape in slide.shapes if shape.shape_type == MSO_SHAPE_TYPE.TABLE
    ]
    if len(tables) < 2:
        return

    tables.sort(key=lambda shape: int(shape.top))
    for index in range(1, len(tables)):
        previous = tables[index - 1]
        current = tables[index]
        prev_bottom = int(previous.top) + int(previous.height)
        gap = Emu(120000)
        if int(current.top) < prev_bottom + gap:
            current.top = prev_bottom + gap


def _fix_slide_layout(slide, slide_height: int, slide_width: int) -> None:
    _fix_stacked_tables(slide)
    _trim_oversized_body_textboxes(slide)

    initial_content = [
        shape
        for shape in _content_layout_shapes(slide)
        if not _is_heading_shape(shape)
    ]
    initial_content.sort(key=lambda shape: (int(shape.top), int(shape.left)))

    _resolve_content_flow(slide, slide_height, content_order=initial_content)
    _align_content_slide(slide, slide_width)
    _fit_oversized_code_blocks(slide, slide_height)

    footer_line = int(slide_height * FOOTER_SAFE_RATIO)
    for _ in range(20):
        if not _slide_has_layout_issues(slide, slide_height):
            return

        _resolve_content_flow(slide, slide_height, content_order=initial_content)
        _align_content_slide(slide, slide_width)
        _trim_oversized_body_textboxes(slide)
        _fit_oversized_code_blocks(slide, slide_height)

        for shape in _layout_shapes(slide):
            if _shape_bounds(shape)[3] > footer_line:
                _nudge_shape_up(shape, Emu(80000))
            if shape.has_text_frame:
                shape.text_frame.word_wrap = True
            _shrink_shape_fonts(shape, -1)
            _shrink_table_fonts(shape, -1)
            _trim_oversized_body_textbox(shape)


def fix_presentation_layout(prs: Presentation) -> None:
    slide_height = int(prs.slide_height)
    slide_width = int(prs.slide_width)
    for slide in prs.slides:
        if _is_course_title_slide(slide) or _is_course_agenda_slide(slide):
            continue
        if _is_lesson_lead_slide(slide):
            _format_lesson_lead_slide(slide, slide_height, slide_width)
            continue
        if _is_module_lead_slide(slide):
            _format_module_lead_slide(slide, slide_height, slide_width)
            continue
        _fix_slide_layout(slide, slide_height, slide_width)
    _format_course_intro_slides(prs)


def rebuild_tables_from_markdown(prs: Presentation, md_path: Path) -> int:
    markdown = md_path.read_text(encoding="utf-8")
    md_slides = split_marp_slides(markdown)
    rebuilt = 0
    slide_width = int(prs.slide_width)
    search_from = 0

    for slide_md in md_slides:
        tables = extract_markdown_tables(slide_md)
        if not tables:
            continue
        slide_index = _find_pptx_slide_index(prs, slide_md, start_index=search_from)
        if slide_index is None:
            continue
        search_from = slide_index + 1
        rebuilt += _rebuild_slide_tables(
            prs.slides[slide_index], tables, slide_width=slide_width
        )

    return rebuilt


def clean_pptx(
    input_path: Path,
    output_path: Path,
    *,
    mode: str = "minimal",
    dry_run: bool = False,
    source_md: Path | None = None,
) -> tuple[int, int, int, int, int]:
    prs = Presentation(str(input_path))
    slide_width = int(prs.slide_width)
    slide_height = int(prs.slide_height)
    removed = 0
    slides_touched = 0
    tables_rebuilt = 0
    code_blocks_rebuilt = 0
    chrome_slides_updated = 0

    for slide in prs.slides:
        to_remove = []

        for shape in slide.shapes:
            text = _shape_text(shape)
            rgb = _shape_fill_rgb(shape)
            full = _is_full_slide(shape, slide_width, slide_height)

            if mode == "minimal":
                if full and rgb == "FFFFFF":
                    to_remove.append(shape)
                continue

            # text-only: keep shapes with readable text; drop decoration meshes.
            if text:
                continue
            to_remove.append(shape)

        if to_remove:
            slides_touched += 1
            removed += len(to_remove)
            if not dry_run:
                for shape in to_remove:
                    sp = shape._element
                    sp.getparent().remove(sp)

        if mode == "text-only" and not dry_run:
            _set_slide_background(slide)
            for shape in slide.shapes:
                _scale_body_fonts(shape)
                _apply_text_colors(shape)

    if mode == "text-only" and source_md and not dry_run:
        tables_rebuilt = rebuild_tables_from_markdown(prs, source_md)
        code_blocks_rebuilt = rebuild_code_blocks_from_markdown(prs, source_md)
        fix_presentation_layout(prs)
        _normalize_presentation_formatting(prs)
        fix_presentation_layout(prs)
        _format_course_intro_slides(prs)
        for slide in prs.slides:
            if _is_lesson_lead_slide(slide):
                _format_lesson_lead_slide(slide, slide_height, slide_width)
            elif _is_module_lead_slide(slide):
                _format_module_lead_slide(slide, slide_height, slide_width)
        _normalize_presentation_formatting(prs)
        chrome_slides_updated = apply_slide_chrome_from_markdown(prs, source_md)

    if not dry_run:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        prs.save(str(output_path))

    return removed, slides_touched, tables_rebuilt, code_blocks_rebuilt, chrome_slides_updated


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("-o", "--output", type=Path)
    parser.add_argument(
        "--mode",
        choices=("minimal", "text-only"),
        default="text-only",
        help="minimal removes white overlays; text-only keeps text boxes + flat background",
    )
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument(
        "--source-md",
        type=Path,
        help="Marp markdown source used to rebuild pipe tables as native PowerPoint tables",
    )
    args = parser.parse_args()

    if not args.input.exists():
        print(f"Not found: {args.input}", file=sys.stderr)
        return 1

    output = args.output or args.input.with_name(
        args.input.stem.replace(".cleaned", "") + ".cleaned.pptx"
    )

    removed, slides, tables_rebuilt, code_blocks_rebuilt, chrome_slides_updated = clean_pptx(
        args.input, output, mode=args.mode, dry_run=args.dry_run, source_md=args.source_md
    )
    action = "Would remove" if args.dry_run else "Removed"
    print(f"{action} {removed} shape(s) across {slides} slide(s) [{args.mode}]")
    if tables_rebuilt:
        print(f"Rebuilt {tables_rebuilt} native table(s) from markdown")
    if code_blocks_rebuilt:
        print(f"Rebuilt {code_blocks_rebuilt} styled code block(s) from markdown")
    if chrome_slides_updated:
        print(f"Updated header/footer chrome on {chrome_slides_updated} slide(s) from markdown")
    if not args.dry_run:
        print(f"Saved: {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

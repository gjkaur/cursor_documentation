#!/usr/bin/env python3
"""Generate detailed instructor speaker scripts for the complete course Marp deck."""

from __future__ import annotations

import argparse
import importlib.util
import re
import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))

from marp_tables import extract_fenced_code_blocks, extract_markdown_tables, split_marp_slides
from speaker_notes_enrichment import EnrichmentMatch, exercise_step_hints, match_enrichment

_spec = importlib.util.spec_from_file_location(
    "generate_slide_exercises",
    Path(__file__).resolve().parent / "generate-slide-exercises.py",
)
_mod = importlib.util.module_from_spec(_spec)
assert _spec.loader is not None
_spec.loader.exec_module(_mod)
EXERCISE_META = _mod.EXERCISE_META

REPO = Path(__file__).resolve().parent.parent
DEFAULT_SOURCE = REPO / "slides" / "course-complete-marp.md"
DEFAULT_NOTES = REPO / "slides" / "course-complete-speaker-notes.md"
DEFAULT_MARP = REPO / "slides" / "course-complete-marp-with-notes.md"

MODULE_NAMES = {
    1: "Mental Models for AI-Assisted Development",
    2: "Cursor Editor Essentials",
    3: "Agent Modes and Tools",
    4: "Customizing Cursor for Your Team",
    5: "Cursor CLI and Local Automation",
    6: "Cloud Agents in the UI",
    7: "Cursor API Foundations",
    8: "Cloud Agents API and Webhooks",
    9: "Admin and Analytics APIs",
    10: "AI Code Tracking and Reporting",
}


@dataclass
class SlideContext:
    module: int | None = None
    module_title: str = "Course intro"
    lesson: str | None = None
    lesson_title: str | None = None
    exercise: tuple[int, int] | None = None
    day: str | None = None
    exercise_briefing_for: tuple[int, int] | None = None
    prev_heading: str | None = None


def _strip_directives(text: str) -> str:
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    text = re.sub(r"^_.+_$", "", text, flags=re.MULTILINE)
    return text


def _clean_inline(text: str) -> str:
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"\*([^*]+)\*", r"\1", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    return text.strip()


def _plain_text(slide: str) -> str:
    text = _strip_directives(slide)
    text = re.sub(r"!\[[^\]]*\]\([^)]+\)", "", text)
    text = re.sub(r"<img[^>]+>", "", text)
    text = re.sub(r"```.*?```", "", text, flags=re.DOTALL)
    text = re.sub(r"^#+\s+", "", text, flags=re.MULTILINE)
    text = re.sub(r"^>\s?", "", text, flags=re.MULTILINE)
    text = re.sub(r"\|", " ", text)
    text = re.sub(r"-{3,}", " ", text)
    text = re.sub(r"\s+", " ", text).strip()
    return _clean_inline(text)


def _heading(slide: str) -> str:
    for line in slide.splitlines():
        stripped = line.strip()
        if stripped.startswith("## Exercise "):
            return stripped[3:].strip()
    for line in slide.splitlines():
        stripped = line.strip()
        if stripped.startswith("# "):
            return stripped[2:].strip()
        if stripped.startswith("## "):
            return stripped[3:].strip()
    plain = _plain_text(slide)
    return plain[:80] + ("…" if len(plain) > 80 else "") if plain else "Untitled slide"


def _slide_kind(slide: str, ctx: SlideContext) -> str:
    body = slide.strip()
    if "<!-- _class: lead -->" in body:
        if re.search(r"^#\s+Lesson\s+\d+\.\d+", body, re.MULTILINE):
            return "lesson_intro"
        if re.search(r"^#\s+Day\s+\d", body, re.MULTILINE):
            return "day_break"
        if ctx.module is None and "Cursor Training Program" in body:
            return "course_title"
        return "module_intro"
    if body.lstrip().startswith("## Course Agenda"):
        return "course_agenda"
    if body.lstrip().startswith("## Day 1") or body.lstrip().startswith("## Day 2"):
        return "day_overview"
    if "## Module Overview" in body:
        return "module_overview"
    if "## Learning Objectives" in body:
        return "learning_objectives"
    if "## Agenda" in body:
        return "module_agenda"
    if "## Module Summary" in body:
        return "module_summary"
    if "## Quick Reference Card" in body:
        return "quick_reference"
    if "## Windows Exercise Environment" in body:
        return "exercise_setup"
    if re.search(r"^## Exercise \d+\.\d+", body, re.MULTILINE):
        return "exercise"
    if re.search(r"^## Demo:", body, re.MULTILINE):
        return "demo"
    if re.search(r"^## Walkthrough:", body, re.MULTILINE):
        return "walkthrough"
    if "<img" in body or re.search(r"!\[[^\]]*\]\(", body):
        return "diagram"
    if "|" in body and re.search(r"^\|[^|]+\|", body, re.MULTILINE):
        return "table"
    if re.search(r"^>\s", body, re.MULTILINE):
        return "quote"
    if "```" in body:
        return "code"
    if re.search(r"^[-*]\s", body, re.MULTILINE):
        return "bullets"
    return "content"


def _timing(slide: str) -> str | None:
    match = re.search(r"_([^_]*\d+\s*min[^_]*)_", slide)
    return match.group(1).strip() if match else None


def _bullets(slide: str, limit: int = 8) -> list[str]:
    items: list[str] = []
    for line in slide.splitlines():
        match = re.match(r"^[-*]\s+(.+)$", line.strip())
        if match:
            items.append(_clean_inline(match.group(1)))
        if len(items) >= limit:
            break
    return items


def _blockquote(slide: str) -> str | None:
    lines = []
    for line in slide.splitlines():
        if line.strip().startswith(">"):
            lines.append(_clean_inline(line.strip().lstrip(">").strip()))
    return " ".join(lines) if lines else None


def _body_paragraphs(slide: str) -> list[str]:
    paragraphs: list[str] = []
    in_fence = False
    for line in slide.splitlines():
        stripped = line.strip()
        if stripped.startswith("```"):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        if not stripped or stripped.startswith("#") or stripped.startswith("|"):
            continue
        if stripped.startswith(">") or stripped.startswith("<!--"):
            continue
        if stripped.startswith("*") and stripped.endswith("*") and not stripped.startswith("**"):
            continue
        if stripped.startswith("**Step") or stripped.startswith("**Implication"):
            paragraphs.append(_clean_inline(stripped))
            continue
        if stripped.startswith("**") and stripped.endswith("**"):
            paragraphs.append(_clean_inline(stripped))
            continue
        paragraphs.append(_clean_inline(stripped))
    return [p for p in paragraphs if p and p not in {"---"}]


def _table_rows(slide: str) -> list[list[str]]:
    tables = extract_markdown_tables(slide)
    if not tables:
        return []
    return [[_clean_inline(cell) for cell in row] for row in tables[0]]


def _prompt_blocks(slide: str) -> list[str]:
    blocks = extract_fenced_code_blocks(slide)
    prompts: list[str] = []
    for block in blocks:
        text = block.strip()
        if text.startswith("git ") or "curl" in text or "import " in text or "def " in text:
            continue
        if len(text) > 20:
            prompts.append(text)
    return prompts


def _exercise_ref(slide: str) -> tuple[int, int] | None:
    match = re.search(r"## Exercise (\d+)\.(\d+)", slide)
    if match:
        return int(match.group(1)), int(match.group(2))
    return None


def _lab_path(module: int, ex_num: int) -> str | None:
    folder = REPO / "slide-exercises" / f"module-{module:02d}"
    if not folder.exists():
        return None
    matches = sorted(folder.glob(f"exercise-{module}.{ex_num}-*.md"))
    return matches[0].relative_to(REPO).as_posix() if matches else None


def _lab_file(module: int, ex_num: int) -> Path | None:
    folder = REPO / "slide-exercises" / f"module-{module:02d}"
    if not folder.exists():
        return None
    matches = sorted(folder.glob(f"exercise-{module}.{ex_num}-*.md"))
    return matches[0] if matches else None


def _parse_lab_troubleshooting(text: str) -> list[str]:
    tips: list[str] = []
    if "## Troubleshooting" not in text:
        return tips
    section = text.split("## Troubleshooting", 1)[1].split("\n## ", 1)[0]
    for line in section.splitlines():
        if line.strip().startswith("|") and "---" not in line:
            cells = [c.strip() for c in line.strip("|").split("|")]
            if len(cells) >= 2 and cells[0].lower() not in {"problem", "what to try"}:
                tips.append(f"If {cells[0]}: {cells[1]}")
    return tips[:3]


def _parse_lab_step_blocks(text: str) -> dict[str, dict[str, str]]:
    """Map lowercase step keywords to goal/look_for from lab guide."""
    blocks: dict[str, dict[str, str]] = {}
    current_key = "default"
    current: dict[str, str] = {}
    for line in text.splitlines():
        step_match = re.match(r"\*\*Step (\d+)[^*]*\*\*|\*\*Step (\d+) — ([^*]+)\*\*", line.strip(), re.I)
        if step_match:
            if current:
                blocks[current_key] = current
            title = (step_match.group(3) or step_match.group(0) or "step").lower()
            current_key = re.sub(r"[^a-z0-9]+", " ", title).strip()
            current = {}
            continue
        goal = re.match(r"\*\*Goal:\*\*\s*(.+)", line.strip())
        if goal:
            current["goal"] = _clean_inline(goal.group(1))
            continue
        look = re.match(r"\*\*Look for:\*\*\s*(.+)", line.strip())
        if look:
            current["look_for"] = _clean_inline(look.group(1))
            continue
    if current:
        blocks[current_key] = current
    return blocks


def _lab_context(module: int, ex_num: int) -> tuple[dict[str, dict[str, str]], list[str]]:
    path = _lab_file(module, ex_num)
    if not path:
        return {}, []
    text = path.read_text(encoding="utf-8")
    return _parse_lab_step_blocks(text), _parse_lab_troubleshooting(text)


def _match_lab_step(heading: str, step_blocks: dict[str, dict[str, str]]) -> dict[str, str]:
    h = heading.lower()
    for key, data in step_blocks.items():
        if key != "default" and key in h:
            return data
    for key, data in step_blocks.items():
        tokens = [t for t in key.split() if len(t) > 3]
        if tokens and all(t in h for t in tokens[:2]):
            return data
    return step_blocks.get("default", {})


def _transition(prev: str | None, heading: str, kind: str) -> str | None:
    if not prev or prev == heading:
        return None
    if kind in {"lesson_intro", "module_intro", "module_overview", "course_agenda", "day_overview", "exercise"}:
        return None
    if kind in {"diagram", "table", "code", "quote", "bullets", "content"}:
        return f"Next: {heading}."
    return None


def _apply_enrichment(
    spoken: list[str],
    heading: str,
    kind: str,
    ctx: SlideContext,
    *,
    slide_summary: str | None = None,
    max_summary_words: int = 35,
) -> None:
    enrich: EnrichmentMatch = match_enrichment(heading, kind, ctx.module)
    transition = _transition(ctx.prev_heading, heading, kind)
    if transition:
        spoken.append(transition)
    spoken.extend(enrich.paragraphs)
    if slide_summary:
        words = slide_summary.split()
        if len(words) > max_summary_words:
            slide_summary = " ".join(words[:max_summary_words]) + "… (see slide)"
        if enrich.paragraphs:
            spoken.append(f"On screen: {slide_summary}")
        elif slide_summary:
            spoken.append(slide_summary)
    spoken.extend(enrich.engagement)


def _update_context(slide: str, ctx: SlideContext) -> None:
    header = re.search(r"<!-- _header: 'Module (\d+) — (.+)' -->", slide)
    if header:
        ctx.module = int(header.group(1))
        ctx.module_title = header.group(2)
        ctx.lesson = None
        ctx.lesson_title = None
        ctx.exercise = None
        return

    module_lead = re.search(r"^#\s+(.+)$", slide, re.MULTILINE)
    if "<!-- _class: lead -->" in slide and module_lead:
        title = module_lead.group(1).strip()
        for num, name in MODULE_NAMES.items():
            if title == name:
                ctx.module = num
                ctx.module_title = name
                ctx.lesson = None
                ctx.lesson_title = None
                ctx.exercise = None
                ctx.day = "Day 1" if num <= 5 else "Day 2"
                return
        if title.startswith("Day "):
            ctx.day = title.split()[0] + " " + title.split()[1]

    lesson = re.search(r"^#\s+Lesson\s+(\d+\.\d+)$", slide, re.MULTILINE)
    if lesson:
        ctx.lesson = lesson.group(1)
        parts = ctx.lesson.split(".")
        ctx.module = int(parts[0])
        ctx.module_title = MODULE_NAMES.get(ctx.module, ctx.module_title)
        sub = re.search(r"^##\s+(.+)$", slide, re.MULTILINE)
        ctx.lesson_title = sub.group(1).strip() if sub else None
        ctx.exercise = None
        return

    ex = _exercise_ref(slide)
    if ex:
        ctx.exercise = ex
        ctx.module = ex[0]
        if ctx.exercise_briefing_for != ex:
            ctx.exercise_briefing_for = None


def _join_script(paragraphs: list[str]) -> list[str]:
    return [p for p in paragraphs if p.strip()]


def _is_table_header_row(row: list[str]) -> bool:
    if not row or not row[0].strip():
        return True
    label = row[0].strip().lower()
    if label.startswith("-") or label in {"aspect", "module", "lesson", "parameter", "strategy", "scenario", "type", "problem"}:
        return True
    return all(ch in "-— " for ch in label)


def _narrate_kv_table(rows: list[list[str]]) -> str:
    parts: list[str] = []
    for row in rows:
        if len(row) >= 2 and not _is_table_header_row(row):
            parts.append(f"{row[0]}: {row[1]}.")
    return " ".join(parts)


def _compare_data_rows(rows: list[list[str]]) -> list[tuple[str, str]]:
    pairs: list[tuple[str, str]] = []
    for row in rows:
        if len(row) >= 2 and not _is_table_header_row(row):
            pairs.append((row[0], row[1]))
    if len(pairs) >= 2:
        short = sum(len(pairs[0][i]) for i in range(2)) / 2
        long = sum(len(pairs[1][i]) for i in range(2)) / 2
        if short < long * 0.65:
            pairs = pairs[1:]
    return pairs


def _narrate_compare_table(rows: list[list[str]]) -> str:
    pairs = _compare_data_rows(rows)
    if not pairs:
        return ""
    sentences = [f"{left}: {right}." for left, right in pairs]
    return " ".join(sentences)


def _narrate_three_col_table(rows: list[list[str]]) -> str:
    parts: list[str] = []
    for row in rows:
        if len(row) >= 3 and not _is_table_header_row(row):
            parts.append(f"{row[0]}: {row[1]}. Use this when {row[2]}.")
    return " ".join(parts)


def _narrate_agenda_table(rows: list[list[str]]) -> str:
    parts: list[str] = []
    for row in rows:
        if len(row) >= 3 and not _is_table_header_row(row):
            if row[0].isdigit() or re.match(r"^\d+\.\d+$", row[0]):
                parts.append(f"Lesson {row[0]}, {row[1]}, about {row[2]}")
            else:
                parts.append(f"Module {row[0]}, {row[1]}, {row[2]}")
    if not parts:
        return _narrate_compare_table(rows)
    return "Here is how we will spend our time: " + "; ".join(parts) + "."


def _narrate_bullets(bullets: list[str], heading: str, intro: str | None = None) -> list[str]:
    if not bullets:
        return []
    parts: list[str] = []
    if intro:
        parts.append(intro)
    if len(bullets) <= 3:
        for i, item in enumerate(bullets):
            parts.append(f"Point {i + 1}: {item}.")
    else:
        parts.append(
            f"There are {len(bullets)} items on this slide. I'll emphasize the first two, then you can scan the rest."
        )
        parts.append(f"First: {bullets[0]}.")
        parts.append(f"Second: {bullets[1]} — this one usually matters most in practice.")
        if len(bullets) > 2:
            parts.append(f"Also on screen: {', '.join(bullets[2:4])}" + ("…" if len(bullets) > 4 else "") + ".")
    return parts


def _narrate_quote(quote: str, body: list[str], heading: str) -> list[str]:
    q = quote.strip().strip('"').strip("'")
    parts: list[str] = [f'Start with the line on screen: "{q}"']
    if body:
        parts.append(
            "Expand in your own words — do not read the bullet text verbatim: "
            + " ".join(body[:2])
        )
    return parts


def _narrate_diagram(heading: str, alt_text: str, quote: str | None, body: list[str]) -> list[str]:
    topic = alt_text or heading
    parts: list[str] = [f"This slide shows {topic.lower() if topic.isupper() else topic}."]
    lower = f"{heading} {alt_text}".lower()
    if "next-token" in lower or "token prediction" in lower:
        parts.append(
            "The model reads the text so far, assigns a probability to each possible next token, "
            "samples one, appends it, and repeats. That loop is how an entire answer is generated."
        )
    elif "factor" in lower and "output" in lower:
        parts.append(
            "Your prompt, system instructions, attached files, model choice, and parameters such as temperature "
            "all feed into the same response. When quality shifts, one of these inputs usually changed."
        )
    elif "hallucination" in lower and "cause" in lower:
        parts.append(
            "Hallucinations come from gaps in training data, missing context, overconfidence, and pressure to answer "
            "even when the model should say it does not know."
        )
    elif "context" in lower and ("pyramid" in lower or "input" in lower):
        parts.append(
            "Not all context is equal. Recent messages, open files, rules, and repository structure compete for "
            "the same token budget — put the most important material where the model will actually use it."
        )
    elif "agent loop" in lower or "tool calling" in lower:
        parts.append(
            "The agent proposes an action, Cursor runs the tool, the result returns to the model, and the loop "
            "continues until the task is done or you stop it."
        )
    elif "mcp" in lower:
        parts.append(
            "MCP connects Cursor to external systems through a standard protocol so tools stay outside the model "
            "but still appear in the agent loop."
        )
    elif body:
        parts.append(" ".join(body))
    elif quote:
        parts.append(quote)
    else:
        parts.append(
            "Walk through each box and arrow once, naming what enters the flow, what happens in the middle, "
            "and what comes out the other side."
        )
    return parts


def _narrate_code(heading: str, body: list[str], blocks: list[str]) -> list[str]:
    intro = " ".join(body[:3]) if body else heading
    parts = [intro] if intro else [heading]
    if blocks:
        block = blocks[0].strip()
        lines = [ln for ln in block.splitlines() if ln.strip() and not ln.strip().startswith("#")]
        if "temperature" in block.lower():
            parts.append(
                "These are sensible defaults for focused coding work: a low temperature around 0.2, "
                "top-p near 0.9 for balance, and a max token cap to control cost."
            )
        elif "temperature 0.1" in block.lower() or "temperature 0.7" in block.lower():
            parts.append(
                "The same prompt produces different code at different temperatures. "
                "Lower values stay close to the obvious solution; higher values add variation and sometimes instability."
            )
        elif "requests.async" in block or "hallucinated" in block.lower():
            parts.append(
                "The top snippet looks plausible but invents an API that does not exist. "
                "The correct approach is to use httpx or aiohttp for async HTTP in Python."
            )
        elif "curl" in block.lower() or "api.cursor.com" in block.lower():
            parts.append(
                "Run this from PowerShell with your key in an environment variable. "
                "Never paste live credentials into chat or commit them to git."
            )
        elif len(lines) <= 4:
            parts.append(f"The important lines are: {'; '.join(lines[:3])}.")
        else:
            parts.append(f"Focus on the first few lines — for example: {lines[0][:100]}.")
    return parts


def _lesson_format(timing: str | None) -> tuple[str, str]:
    if not timing:
        return "mixed", "listen, participate, or follow along as indicated on the next slides"
    lower = timing.lower()
    if "concept" in lower:
        return "concept", "listen and take notes — you do not need to type along yet"
    if "exercise" in lower or "hands-on" in lower:
        return "hands-on", "open Cursor and work through the steps on the upcoming slides"
    if "demo" in lower or "demonstration" in lower:
        return "demonstration", "watch the live demo and note where each control lives in the UI"
    if "walkthrough" in lower:
        return "walkthrough", "follow on screen as I show the configuration or file layout"
    return "mixed", "follow along as we go"


def _exercise_spoken(
    slide: str,
    heading: str,
    ex: tuple[int, int],
    meta: dict,
    body: list[str],
    prompts: list[str],
    ctx: SlideContext,
) -> tuple[list[str], list[str]]:
    title = meta.get("title", heading)
    spoken: list[str] = []
    facilitator: list[str] = []
    step_blocks, trouble = _lab_context(ex[0], ex[1])
    step_data = _match_lab_step(heading, step_blocks)

    if "Success Criteria" in heading:
        criteria = _bullets(slide)
        spoken.append(f"Let's debrief Exercise {ex[0]}.{ex[1]} — {title}.")
        if criteria:
            spoken.append(
                "Check off what you actually completed — not what the Agent claimed: "
                + "; ".join(criteria[:4])
                + ("…" if len(criteria) > 4 else "")
                + "."
            )
        spoken.extend(exercise_step_hints(ex[0], ex[1], "success"))
        spoken.append(
            "Ask two volunteers: what did the Agent get wrong, and what prompt change fixed it? "
            "That reflection is the learning outcome."
        )
        if trouble:
            facilitator.append("Common issues: " + "; ".join(trouble))
        return spoken, facilitator

    first_slide = ctx.exercise_briefing_for != ex
    hints = exercise_step_hints(ex[0], ex[1], heading, first_step=first_slide)

    if first_slide:
        ctx.exercise_briefing_for = ex
        spoken.append(f"Starting Exercise {ex[0]}.{ex[1]} — {title}. {meta.get('time', '15 min')} scheduled.")
        if meta.get("objective"):
            spoken.append(meta["objective"])
        lab = _lab_path(ex[0], ex[1])
        if lab:
            spoken.append(f"The full lab guide with troubleshooting is in {lab}.")
        if "Demonstration (Windows)" in slide or ex[0] >= 2:
            spoken.append(
                "Windows setup: PowerShell terminal — Ctrl+backtick — Agent panel — Ctrl+I. "
                "Open the repo folder, not a single file."
            )
        spoken.extend(hints)
    else:
        spoken.append(f"Next step — {heading.replace(f'Exercise {ex[0]}.{ex[1]} — ', '')}.")

    if step_data.get("goal"):
        spoken.append(f"Goal for this step: {step_data['goal']}")
    if step_data.get("look_for"):
        spoken.append(f"A good result looks like: {step_data['look_for']}")

    for line in body:
        if re.match(r"^Step \d+", line, re.I):
            spoken.append(line + ".")
        elif line.startswith("Where:") or line.startswith("Terminal:"):
            spoken.append(line + ".")

    for prompt in prompts:
        flat = " ".join(prompt.split())
        spoken.append(
            f"Paste this into the Agent — constraints matter as much as the ask: \"{flat}\""
        )
        if "@" in flat and "calculator" in flat.lower():
            spoken.append("Keep @calculator.c in the prompt so the Agent cannot wander to other files.")

    spoken.extend(h for h in hints if h not in spoken)

    closings = [
        "Work for about two to four minutes — I'll answer questions when hands go up.",
        "Try it now; if you finish early, help a neighbor or refine your follow-up prompt.",
        "Pause here — most groups need a few minutes before the next step.",
    ]
    spoken.append(closings[(ex[0] + ex[1] + len(heading)) % len(closings)])

    if meta.get("type") == "api":
        facilitator.extend(trouble or ["Watch Admin vs User keys and PowerShell quoting."])
    elif meta.get("type") == "cli":
        facilitator.append("Watch PATH, working directory, and resumed session branch.")
    else:
        facilitator.extend(trouble[:2] or ["Watch unread diffs and wrong repo folder."])

    return spoken, facilitator


def _script_for_slide(slide: str, slide_num: int, ctx: SlideContext) -> tuple[list[str], list[str]]:
    kind = _slide_kind(slide, ctx)
    heading = _heading(slide)
    timing = _timing(slide)
    quote = _blockquote(slide)
    body = _body_paragraphs(slide)
    bullets = _bullets(slide)
    rows = _table_rows(slide)
    prompts = _prompt_blocks(slide)
    spoken: list[str] = []
    facilitator: list[str] = []

    if timing:
        facilitator.append(f"Pacing: {timing}. Shorten repetition before cutting exercise time.")

    if kind == "course_title":
        subtitle = next((p for p in body if "Springpeople" in p or "Modules" in p), "")
        spoken.extend(
            _join_script(
                [
                    "Good morning, and welcome to the Cursor Training Program — AI-Assisted Development with Cursor. "
                    "Thank you for being here. Over the next two days we will move from mental models to daily editor "
                    "workflows, then into automation, Cloud Agents, and the Cursor APIs.",
                    f"{subtitle + '. ' if subtitle else ''}"
                    "Before we start, please confirm three things: Cursor is installed, you are signed in, and you have "
                    "a Git repository you can experiment in — sample repos are fine if you do not want to use production code.",
                    "This course is roughly seventy percent hands-on and thirty percent concept and discussion. "
                    "Questions are welcome during a slide if they are quick; save longer ones for breaks or module transitions.",
                ]
            )
        )
    elif kind == "course_agenda":
        spoken.extend(
            _join_script(
                [
                    "Here is the full two-day arc for our time together.",
                    "Day one builds editor fluency. Module one gives us shared mental models for how AI assistants actually work. "
                    "Modules two through four are hands-on in the Cursor editor — understanding codebases, making safe changes, "
                    "working with agent modes, and customizing rules and skills. Module five introduces the CLI for terminal "
                    "and scripting workflows.",
                    "Day two shifts to automation and integration: Cloud Agents in the UI, API authentication and reliability, "
                    "programmatic Cloud Agent launches and webhooks, admin and analytics reporting, and AI code tracking.",
                    "The total scheduled time is about eleven and a half hours across both days, plus breaks. "
                    "If you have never opened Cursor before, let me know now so I can allow extra setup time in Module two.",
                ]
            )
        )
    elif kind == "day_overview":
        enrich = match_enrichment(heading, kind, ctx.module)
        if "Day 1" in heading:
            spoken.append(
                "Day one is about editor confidence — mental models first, then hands-on Cursor through Module 5. "
                "We will not call external APIs until tomorrow."
            )
        else:
            spoken.append(
                "Day two assumes yesterday's habits stuck — API keys ready, PowerShell working, and realistic expectations "
                "about agent autonomy."
            )
        spoken.extend(enrich.paragraphs)
        if rows:
            highlights = []
            for row in rows[:5]:
                if len(row) >= 3 and not _is_table_header_row(row):
                    highlights.append(f"Module {row[0].strip('*')} ({row[2]})")
            if highlights:
                spoken.append("Today's modules in one breath: " + ", ".join(highlights) + ". Details are on the slide.")
    elif kind == "day_break":
        spoken.extend(
            _join_script(
                [
                    f"Welcome back — {heading}.",
                    "Yesterday we established how AI models behave and how to use Cursor safely in real repositories. "
                    "Today we extend that work outside the IDE: the CLI, Cloud Agents, and production-grade API integration.",
                    "Before we continue, make sure API keys are available where needed and that you can open PowerShell "
                    "and reach api.cursor.com from this network. We will store every key in environment variables — "
                    "never paste secrets on screen or into chat logs.",
                ]
            )
        )
    elif kind == "module_intro":
        _apply_enrichment(spoken, heading, kind, ctx)
        subtitle = next((p for p in body if p), "")
        if subtitle and "min" in subtitle:
            spoken.append(f"Timing on slide: {subtitle}")
    elif kind == "module_overview":
        _apply_enrichment(spoken, heading, kind, ctx)
        if rows:
            goal = next((r[1] for r in rows if len(r) >= 2 and "goal" in r[0].lower()), None)
            if goal:
                spoken.append(f"The module goal in plain language: {goal}")
        spoken.append("Glance at duration and prerequisites on screen — raise a hand if anything blocks you.")
    elif kind == "learning_objectives":
        spoken.append(
            f"These outcomes define success for Module {ctx.module} — not a reading list, but skills you will practice."
        )
        if bullets:
            spoken.append(
                "Highlight three that matter for your role: "
                + "; ".join(bullets[:3])
                + ("; plus more on screen" if len(bullets) > 3 else "")
                + "."
            )
        _apply_enrichment(spoken, "learning objectives", "bullets", ctx)
    elif kind == "module_agenda":
        spoken.append(
            _narrate_agenda_table(rows) or "Use this agenda to pace the module — protect exercise time if we run long."
        )
        facilitator.append("Announce when the next hands-on block starts so people can close email and open Cursor.")
    elif kind == "lesson_intro":
        lesson_title = ctx.lesson_title or heading
        _fmt, participation = _lesson_format(timing)
        meta = None
        if ctx.lesson:
            parts = ctx.lesson.split(".")
            if len(parts) == 2:
                meta = EXERCISE_META.get((int(parts[0]), int(parts[1])))
        spoken.append(
            f"Lesson {ctx.lesson}: {lesson_title}. {timing + ' ' if timing else ''}"
            f"Participation: {participation}."
        )
        if meta and meta.get("objective"):
            spoken.append(f"Why this lesson exists: {meta['objective']}")
        _apply_enrichment(spoken, lesson_title, "lesson_intro", ctx)
        if ctx.lesson:
            mod, les = ctx.lesson.split(".")
            lab = _lab_path(int(mod), int(les))
            if lab and meta:
                spoken.append(f"Lab reference: {lab}")
    elif kind == "exercise_setup":
        spoken.extend(
            _join_script(
                [
                    "Let's pause for environment setup. Open PowerShell in Cursor's integrated terminal — Ctrl+backtick.",
                    "For API exercises, set your keys in the session, for example "
                    "`$env:CURSOR_ADMIN_API_KEY` or `$env:CURSOR_USER_API_KEY`. Never commit keys to git.",
                    "On Windows, use `curl.exe` when a lab shows curl — not the PowerShell alias.",
                    "Once your test call succeeds, give me a thumbs-up and we will continue.",
                ]
            )
        )
        facilitator.append("Allow two to three minutes. Pair anyone blocked on keys or curl with a neighbor.")
    elif kind == "exercise":
        ex = _exercise_ref(slide) or ctx.exercise
        meta = EXERCISE_META.get(ex, {}) if ex else {}
        if ex:
            ex_spoken, ex_fac = _exercise_spoken(slide, heading, ex, meta, body, prompts, ctx)
            spoken.extend(ex_spoken)
            facilitator.extend(ex_fac)
        else:
            spoken.append(" ".join(body) if body else _plain_text(slide))
    elif kind == "demo":
        demo_title = heading.replace("Demo: ", "")
        spoken.append(
            f"I am going to demonstrate {demo_title} live on my machine. "
            f"{' '.join(body) if body else 'Watch where each control appears in Cursor.'} "
            "I will narrate each click and keystroke as I go."
        )
        spoken.append(
            f"When the demo finishes, we will discuss when {demo_title.lower()} belongs in production workflow "
            "and when a lighter-weight approach is enough."
        )
        facilitator.append("If the network fails, describe the expected result and use a screenshot backup.")
    elif kind == "walkthrough":
        walk_title = heading.replace("Walkthrough: ", "")
        spoken.append(
            f"In this walkthrough we will look at {walk_title}. "
            f"{' '.join(body) if body else 'I will show the file or setting on my screen.'} "
            "Watch where this lives in Cursor or in the repository — that location matters as much as the content."
        )
    elif kind == "diagram":
        alt = re.search(r'alt="([^"]+)"', slide)
        alt_text = alt.group(1) if alt else heading
        spoken.extend(_narrate_diagram(heading, alt_text, quote, body))
        _apply_enrichment(spoken, heading, kind, ctx, slide_summary=alt_text)
    elif kind == "table":
        _apply_enrichment(spoken, heading, kind, ctx)
        max_cols = max((len(r) for r in rows), default=0)
        if max_cols >= 3:
            brief = _narrate_three_col_table(rows)
        else:
            brief = _narrate_compare_table(rows) or _narrate_kv_table(rows)
        if brief:
            spoken.append(f"Slide reference (skim, do not read every cell): {brief[:280]}")
        if "Key Insight" in slide and rows:
            insights = [
                f"{row[0]} → {row[2]}"
                for row in rows
                if len(row) >= 3 and not _is_table_header_row(row)
            ]
            if insights:
                spoken.append("Recap ask: " + "; ".join(insights[:4]) + ".")
    elif kind == "quote":
        if quote:
            spoken.extend(_narrate_quote(quote, body, heading))
            _apply_enrichment(spoken, heading, kind, ctx)
        else:
            _apply_enrichment(spoken, heading, kind, ctx, slide_summary=" ".join(body) if body else heading)
    elif kind == "code":
        blocks = extract_fenced_code_blocks(slide)
        spoken.extend(_narrate_code(heading, body, blocks))
        _apply_enrichment(spoken, heading, kind, ctx)
    elif kind == "bullets":
        spoken.extend(_narrate_bullets(bullets, heading))
        _apply_enrichment(spoken, heading, kind, ctx)
        if body:
            spoken.append(" ".join(body[:2]))
    elif kind == "module_summary":
        if rows:
            recap = []
            for row in rows:
                if len(row) >= 3 and not _is_table_header_row(row):
                    recap.append(f"Lesson {row[0]}, {row[1]} — key insight: {row[2]}")
            summary = "; ".join(recap) if recap else _plain_text(slide)
        else:
            summary = _plain_text(slide)
        spoken.extend(
            _join_script(
                [
                    f"That completes Module {ctx.module}. {summary}",
                    "What will you do differently on Monday? I will take two or three answers before we break or move on.",
                ]
            )
        )
    elif kind == "quick_reference":
        spoken.extend(
            _join_script(
                [
                    "This quick reference slide is for you to keep after the course — screenshot it or copy the commands "
                    "into your team wiki.",
                    " ".join(bullets) if bullets else _plain_text(slide),
                ]
            )
        )
        facilitator.append("Allow about two minutes for final questions on this module.")
    else:
        text = " ".join(body) if body else _plain_text(slide)
        if text:
            if text.lower().startswith(heading.lower()):
                text = text[len(heading) :].lstrip(" .:-")
            if text.lower().startswith("implication:"):
                text = text.split(":", 1)[1].strip()
        _apply_enrichment(spoken, heading, kind, ctx, slide_summary=text or None)

    ctx.prev_heading = heading
    return _join_script(spoken), _join_script(facilitator)


def generate_notes_document(source: Path) -> tuple[str, list[tuple[int, str, SlideContext, list[str], list[str]]]]:
    markdown = source.read_text(encoding="utf-8")
    slides = split_marp_slides(markdown)
    ctx = SlideContext()
    entries: list[tuple[int, str, SlideContext, list[str], list[str]]] = []

    for index, slide in enumerate(slides, start=1):
        _update_context(slide, ctx)
        heading = _heading(slide)
        spoken, facilitator = _script_for_slide(slide, index, ctx)
        entries.append((index, heading, SlideContext(**vars(ctx)), spoken, facilitator))

    lines = [
        "# Cursor Training Program — Speaker Scripts",
        "",
        f"Full instructor scripts for [`course-complete-marp.md`](course-complete-marp.md) "
        f"({len(slides)} slides). **Script** = teaching narrative; **Facilitator notes** = pacing and room management.",
        "",
        f"*Generated: {date.today().isoformat()}*",
        "",
        "## How to use",
        "",
        "- Match **Slide N** to the page number in the deck footer or Marp presenter view (`p`).",
        "- **Script** = what to teach (examples, pitfalls, debriefs) — not a verbatim repeat of the slide.",
        "- Hands-on slides reference lab guides in [`slide-exercises/`](../slide-exercises/).",
        "- Embedded presenter notes: [`course-complete-marp-with-notes.md`](course-complete-marp-with-notes.md).",
        "",
        "---",
        "",
    ]

    current_module: int | None = None
    for slide_num, heading, slide_ctx, spoken, facilitator in entries:
        if slide_ctx.module != current_module:
            current_module = slide_ctx.module
            if current_module is None:
                lines.extend(["## Course introduction", ""])
            else:
                lines.extend([f"## Module {current_module} — {slide_ctx.module_title}", ""])

        lines.append(f"### Slide {slide_num} — {heading}")
        lines.append("")
        meta = [f"**Type:** {_slide_kind(slides[slide_num - 1], slide_ctx)}"]
        if slide_ctx.lesson:
            meta.append(f"**Lesson:** {slide_ctx.lesson}")
        if slide_ctx.exercise:
            meta.append(f"**Exercise:** {slide_ctx.exercise[0]}.{slide_ctx.exercise[1]}")
        lines.append(" · ".join(meta))
        lines.append("")
        lines.append("**Script**")
        lines.append("")
        for paragraph in spoken:
            lines.append(paragraph)
            lines.append("")
        if facilitator:
            lines.append("**Facilitator notes**")
            lines.append("")
            for note in facilitator:
                lines.append(f"- {note}")
            lines.append("")
        lines.append("---")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n", entries


def inject_marp_notes(source: Path, entries: list[tuple[int, str, SlideContext, list[str], list[str]]]) -> str:
    markdown = source.read_text(encoding="utf-8")
    slides = split_marp_slides(markdown)

    if len(slides) != len(entries):
        raise ValueError(f"Slide count mismatch: {len(slides)} slides vs {len(entries)} note entries")

    enriched: list[str] = []
    for slide, (_slide_num, _heading, _ctx, spoken, _facilitator) in zip(slides, entries):
        note_text = "\n\n".join(spoken)
        body = slide.rstrip() + f"\n\n<!--\n{note_text}\n-->\n"
        enriched.append(body)

    frontmatter_end = markdown.find("\n---\n", 3)
    if not markdown.startswith("---") or frontmatter_end == -1:
        raise ValueError("Expected Marp frontmatter in source deck")

    frontmatter = markdown[: frontmatter_end + 5]
    return frontmatter + "\n\n" + "\n\n---\n\n".join(s.rstrip() for s in enriched) + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-s", "--source", type=Path, default=DEFAULT_SOURCE)
    parser.add_argument("-o", "--output", type=Path, default=DEFAULT_NOTES)
    parser.add_argument("--marp-output", type=Path, default=DEFAULT_MARP)
    parser.add_argument("--no-marp", action="store_true")
    args = parser.parse_args()

    source = args.source if args.source.is_absolute() else REPO / args.source
    output = args.output if args.output.is_absolute() else REPO / args.output
    marp_output = args.marp_output if args.marp_output.is_absolute() else REPO / args.marp_output

    doc, entries = generate_notes_document(source)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(doc, encoding="utf-8")
    print(f"Wrote {output} ({len(entries)} slides)")

    if not args.no_marp:
        marp = inject_marp_notes(source, entries)
        marp_output.write_text(marp, encoding="utf-8")
        print(f"Wrote {marp_output}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

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
    lead = intro or f"On {heading},"
    if len(bullets) == 1:
        return [f"{lead} the main point is this: {bullets[0]}."]
    if len(bullets) <= 5:
        body = ", ".join(bullets[:-1]) + f", and {bullets[-1]}"
        return [f"{lead} cover the following: {body}."]
    body = ", ".join(bullets[:4]) + f", and several more items on screen including {bullets[-1]}"
    return [f"{lead} cover the following: {body}."]


def _narrate_quote(quote: str, body: list[str], heading: str) -> list[str]:
    q = quote.strip().strip('"').strip("'")
    parts = [f'The headline on this slide is "{q}".']
    if body:
        parts.append(" ".join(body))
    elif "hallucination" in heading.lower():
        parts.append(
            "The danger is not that the model hesitates — it is that it answers with complete confidence "
            "while being completely wrong."
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
) -> list[str]:
    title = meta.get("title", heading)
    parts: list[str] = []

    if "Success Criteria" in heading:
        criteria = _bullets(slide)
        parts.append(f"That wraps up Exercise {ex[0]}.{ex[1]} — {title}.")
        if criteria:
            joined = "; ".join(criteria)
            parts.append(f"You should be able to check off: {joined}.")
        elif meta.get("objective"):
            parts.append(f"The intended outcome was: {meta.get('objective')}")
        parts.append(
            "Who completed everything? What did the Agent get wrong, or what surprised you? "
            "Those answers are as valuable as getting a green checkmark."
        )
        return parts

    parts.append(f"We are on {heading} for Exercise {ex[0]}.{ex[1]} — {title}.")
    if meta.get("objective"):
        parts.append(meta["objective"])

    if "Demonstration (Windows)" in slide or "PowerShell" in slide:
        parts.append(
            "On Windows, use the integrated PowerShell terminal — Ctrl+backtick — "
            "and the Agent panel with Ctrl+I unless the slide says otherwise."
        )

    for line in body:
        if re.match(r"^Step \d+", line, re.IGNORECASE):
            parts.append(line + ".")
        elif line.startswith("Where:") or line.startswith("Terminal:"):
            parts.append(line + ".")
        elif line.startswith("Goal:") or line.startswith("Look for:"):
            parts.append(line + ".")

    for prompt in prompts:
        flat = " ".join(prompt.split())
        parts.append(f'In the Agent chat, paste this prompt exactly: "{flat}"')

    if not prompts and not any(re.match(r"^Step", p, re.I) for p in body):
        step_text = " ".join(body)
        if step_text:
            parts.append(step_text + ".")

    parts.append("Take a few minutes now to complete this step before we move on.")
    return parts


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
        if rows:
            modules = []
            for row in rows:
                if len(row) >= 4 and not _is_table_header_row(row):
                    modules.append(
                        f"Module {row[0].strip('*')}, {row[1]}, focused on {row[2]}, about {row[3]}"
                    )
                elif len(row) >= 3 and not _is_table_header_row(row):
                    modules.append(f"Module {row[0].strip('*')}, {row[1]}, {row[2]}")
            module_text = "; ".join(modules)
        else:
            module_text = _plain_text(slide)
        footer = " ".join(body)
        if "Day 1" in heading:
            spoken.append(
                f"Day one is {heading}. {module_text}. "
                f"{footer + ' ' if footer else ''}"
                "The theme today is building confidence in the editor before we ask anyone to call an API."
            )
        else:
            spoken.append(
                f"Day two is {heading}. {module_text}. "
                f"{footer + ' ' if footer else ''}"
                "Today assumes yesterday's mental models and editor habits are in place. "
                "Modules seven through ten need API keys, and modules nine and ten need enterprise admin access. "
                "If you do not have keys, pair with someone who does for those exercises."
            )
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
        subtitle = next((p for p in body if p), "")
        format_hint = "concept discussion" if "concept" in subtitle.lower() else "hands-on work"
        spoken.extend(
            _join_script(
                [
                    f"We are starting Module {ctx.module}: {ctx.module_title}. {subtitle}",
                    f"This block is mostly {format_hint}. "
                    f"By the end of Module {ctx.module}, you should be able to apply what we cover on a real project next week.",
                    "If this is a hands-on module, open Cursor now and confirm your repo folder is loaded. "
                    "If it is concept-only, listen for one idea you can use on Monday morning.",
                ]
            )
        )
    elif kind == "module_overview":
        narration = _narrate_kv_table(rows) or _plain_text(slide)
        spoken.append(
            f"Before we dive in, here is what to expect from Module {ctx.module}. {narration} "
            "If any prerequisite on this slide would block you, raise your hand now so we can help before we continue."
        )
    elif kind == "learning_objectives":
        if bullets:
            obj = ". ".join(f"{b.rstrip('.')}" for b in bullets)
            spoken.extend(
                _join_script(
                    [
                        f"By the end of Module {ctx.module}, you should be able to do the following: {obj}.",
                        "You do not need to memorize this list word for word — you should recognize each outcome "
                        "after we have practiced it in an exercise or demo.",
                    ]
                )
            )
        else:
            spoken.append(_plain_text(slide))
    elif kind == "module_agenda":
        spoken.append(_narrate_agenda_table(rows) or _plain_text(slide))
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
            f"We now begin Lesson {ctx.lesson}: {lesson_title}. "
            f"{timing + '. ' if timing else ''}"
            f"For this lesson, please {participation}."
        )
        if meta and meta.get("objective"):
            spoken.append(meta["objective"])
        if ctx.lesson:
            mod, les = ctx.lesson.split(".")
            lab = _lab_path(int(mod), int(les))
            if lab and meta:
                spoken.append(
                    f"When we reach the exercise slides, the detailed lab guide is in {lab}."
                )
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
            spoken.extend(_exercise_spoken(slide, heading, ex, meta, body, prompts))
            if meta.get("type") == "api":
                facilitator.append("Watch for Admin vs User key mix-ups, curl quoting, and JSON escaping in PowerShell.")
            elif meta.get("type") == "cli":
                facilitator.append("Watch for agent not on PATH, wrong directory, or wrong resumed session.")
            else:
                facilitator.append("Watch for unread diffs, missing @mentions, or work in the wrong repo.")
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
    elif kind == "table":
        max_cols = max((len(r) for r in rows), default=0)
        if max_cols >= 3:
            narration = _narrate_three_col_table(rows)
        else:
            narration = _narrate_compare_table(rows) or _narrate_kv_table(rows)
        if narration:
            spoken.append(narration)
        elif body:
            spoken.append(" ".join(body))
        else:
            spoken.append(_plain_text(slide))
        if "Key Insight" in slide and rows:
            insights = []
            for row in rows:
                if len(row) >= 3 and not _is_table_header_row(row):
                    insights.append(f"Lesson {row[0]}: {row[2]}")
            if insights:
                spoken.append("To recap the module: " + "; ".join(insights) + ".")
    elif kind == "quote":
        if quote:
            spoken.extend(_narrate_quote(quote, body, heading))
        else:
            spoken.append(" ".join(body) if body else _plain_text(slide))
    elif kind == "code":
        blocks = extract_fenced_code_blocks(slide)
        spoken.extend(_narrate_code(heading, body, blocks))
    elif kind == "bullets":
        spoken.extend(_narrate_bullets(bullets, heading))
        if body:
            spoken.append(" ".join(body))
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
                text = f"The practical implication is this: {text.split(':', 1)[1].strip()}"
            spoken.append(text if text else heading)

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
        f"({len(slides)} slides). Read the **Script** sections aloud; **Facilitator notes** are pacing and room management only.",
        "",
        f"*Generated: {date.today().isoformat()}*",
        "",
        "## How to use",
        "",
        "- Match **Slide N** to the page number in the deck footer or Marp presenter view (`p`).",
        "- **Script** = words to say. **Facilitator notes** = timing and logistics (not read to the room).",
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

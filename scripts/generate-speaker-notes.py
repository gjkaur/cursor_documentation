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
    for line in slide.splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#") or stripped.startswith("|"):
            continue
        if stripped.startswith(">") or stripped.startswith("```") or stripped.startswith("<!--"):
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


def _script_for_slide(slide: str, slide_num: int, ctx: SlideContext) -> list[str]:
    kind = _slide_kind(slide, ctx)
    heading = _heading(slide)
    timing = _timing(slide)
    quote = _blockquote(slide)
    body = _body_paragraphs(slide)
    bullets = _bullets(slide)
    rows = _table_rows(slide)
    prompts = _prompt_blocks(slide)
    paragraphs: list[str] = []

    if timing:
        paragraphs.append(
            f"[Timing: {timing}. Adjust depth if the room is fast or slow — do not rush hands-on blocks.]"
        )

    if kind == "course_title":
        subtitle = next((p for p in body if "Springpeople" in p or "Modules" in p), "")
        paragraphs.extend(
            _join_script(
                [
                    "Good morning, and welcome to the Cursor Training Program — AI-Assisted Development with Cursor. "
                    "Thank you for being here. Over the next two days we will move from mental models to daily editor "
                    "workflows, then into automation, Cloud Agents, and the Cursor APIs.",
                    f"{subtitle + '. ' if subtitle else ''}"
                    "Before we start, please confirm three things: Cursor is installed, you are signed in, and you have "
                    "a Git repository you can experiment in — sample repos are fine if you do not want to use production code.",
                    "This course is roughly seventy percent hands-on and thirty percent concept and discussion. "
                    "You will see slide numbers in the footer; match them to this speaker script or to Marp presenter view. "
                    "Questions are welcome — short ones during a slide, longer ones at breaks or module transitions.",
                ]
            )
        )
    elif kind == "course_agenda":
        paragraphs.extend(
            _join_script(
                [
                    "Let me orient you to the full two-day arc shown on this agenda slide.",
                    "Day one builds editor fluency: Module one gives shared mental models for how AI assistants actually work. "
                    "Modules two through four are hands-on in the Cursor editor — understanding codebases, safe changes, "
                    "agent modes, rules, and skills. Module five introduces the CLI for terminal and scripting workflows.",
                    "Day two shifts to automation and integration: Cloud Agents in the UI, API authentication and reliability, "
                    "programmatic Cloud Agent launches and webhooks, admin and analytics reporting, and AI code tracking.",
                    "The total scheduled time is about eleven and a half hours across both days, plus breaks. "
                    "I will adjust pacing based on your experience — raise your hand if you have never opened Cursor before "
                    "so I can spend a little extra time on setup in the first hands-on module.",
                ]
            )
        )
    elif kind == "day_overview":
        paragraphs.append(
            f"This slide previews {heading}. "
            "Walk the module table row by row: name the module number, what participants will do there, "
            "and whether it is mostly concept, hands-on, or demonstration. "
            "Emphasize that day one is about building confidence in the editor before we ask anyone to call an API."
            if "Day 1" in heading
            else f"This slide previews {heading}. "
            "Explain that day two assumes day-one mental models and editor habits are in place. "
            "Modules seven through ten require API keys; enterprise features are needed for modules nine and ten. "
            "If anyone lacks admin access, pair them with someone who has keys for those exercises."
        )
    elif kind == "day_break":
        paragraphs.extend(
            _join_script(
                [
                    f"Welcome back to {heading}. "
                    "Yesterday we established how AI models behave and how to use Cursor safely in real repositories. "
                    "Today we extend that work outside the IDE — CLI, Cloud Agents, and production-grade API integration.",
                    "Before we continue, confirm API keys are available where needed and that everyone can open a terminal "
                    "and reach api.cursor.com from this network. We will use environment variables for every key — "
                    "never paste secrets on screen or into chat logs.",
                ]
            )
        )
    elif kind == "module_intro":
        subtitle = next((p for p in body if "Cursor Training Program" in p or "min" in p), "")
        paragraphs.extend(
            _join_script(
                [
                    f"We are starting Module {ctx.module}: {ctx.module_title}. "
                    f"{subtitle + ' ' if subtitle else ''}"
                    "State the module goal in plain language: what participants will be able to do when we finish — "
                    "not just what topics we will mention.",
                    "Preview whether this module is lecture, hands-on, or mixed. "
                    "If it is hands-on, tell people when to open their laptops and which folder or repo to use. "
                    "If it is concept-only, ask them to listen for one idea they can use on Monday morning.",
                ]
            )
        )
    elif kind == "module_overview":
        rows_text = ""
        for row in rows:
            if len(row) >= 2 and row[0].lower() not in {"aspect", "--------"}:
                rows_text += f"{row[0]} is {row[1]}. "
        paragraphs.append(
            f"This module overview slide sets expectations. In your own words, cover: {rows_text or _plain_text(slide)} "
            "Call out prerequisites explicitly and pause until anyone blocked by missing tools has help. "
            "Do not read the table word-for-word — translate it into what the room will experience in the next hour."
        )
    elif kind == "learning_objectives":
        obj_text = ". ".join(bullets) if bullets else _plain_text(slide)
        paragraphs.extend(
            _join_script(
                [
                    "These learning objectives describe outcomes, not topics. "
                    f"Paraphrase them: {obj_text}.",
                    "Ask the room: which of these would help your team most this quarter? "
                    "Note one or two answers — you can refer back at the module summary.",
                    "Tell participants they are not expected to memorize this list; they should recognize each outcome "
                    "when they have done it during an exercise or demo.",
                ]
            )
        )
    elif kind == "module_agenda":
        agenda_lines = []
        for row in rows:
            if len(row) >= 3 and row[0] not in {"Lesson", "--------"} and not row[0].startswith("-"):
                agenda_lines.append(f"Lesson {row[0]}, {row[1]}, about {row[2]}")
        agenda_speech = "; ".join(agenda_lines[:6]) if agenda_lines else _plain_text(slide)
        paragraphs.append(
            f"Use this agenda as your pacing map for the module. "
            f"You will cover: {agenda_speech}. "
            "Announce when the next hands-on block starts so people can close email and open Cursor. "
            "If you fall behind, shorten concept repetition before cutting exercise time."
        )
    elif kind == "lesson_intro":
        lesson_title = ctx.lesson_title or heading
        meta = None
        if ctx.lesson:
            parts = ctx.lesson.split(".")
            if len(parts) == 2:
                meta = EXERCISE_META.get((int(parts[0]), int(parts[1])))
        paragraphs.extend(
            _join_script(
                [
                    f"We now begin Lesson {ctx.lesson}: {lesson_title}. "
                    f"{timing + '. ' if timing else ''}"
                    "Name the lesson type aloud — concept, hands-on exercise, demonstration, or walkthrough — "
                    "so participants know whether to listen, type along, or watch.",
                    f"{meta['objective'] + ' ' if meta and meta.get('objective') else ''}"
                    f"{'Open the lab guide at ' + _lab_path(int(ctx.lesson.split('.')[0]), int(ctx.lesson.split('.')[1])) + ' when we reach the exercise slides. ' if meta and ctx.lesson and _lab_path(int(ctx.lesson.split('.')[0]), int(ctx.lesson.split('.')[1])) else ''}"
                    "Transition from the previous lesson with one sentence on how this topic connects to what they just learned.",
                ]
            )
        )
    elif kind == "exercise_setup":
        paragraphs.extend(
            _join_script(
                [
                    "Pause the slide deck for environment setup. Everyone should open PowerShell or Git Bash in Cursor's integrated terminal.",
                    "For API exercises: set keys with `$env:CURSOR_ADMIN_API_KEY` or `$env:CURSOR_USER_API_KEY` — never commit keys to git. "
                    "On Windows, use `curl.exe` rather than the PowerShell curl alias when the lab shows curl commands.",
                    "Walk the room for two to three minutes. Common blockers: wrong key type, missing curl, wrong working directory. "
                    "Do not advance until most pairs show a successful test call or are paired with someone who has.",
                ]
            )
        )
    elif kind == "exercise":
        ex = _exercise_ref(slide) or ctx.exercise
        meta = EXERCISE_META.get(ex, {}) if ex else {}
        lab = _lab_path(ex[0], ex[1]) if ex else None
        step_text = " ".join(body)
        if "Success Criteria" in heading:
            paragraphs.extend(
                _join_script(
                    [
                        f"We are closing Exercise {ex[0]}.{ex[1]} — {meta.get('title', 'this lab')}. "
                        "Read each success criterion on the slide and ask the room to mentally check what they completed.",
                        f"Expected outcome: {meta.get('objective', 'participants followed the lab successfully')}. "
                        "Invite one or two volunteers to share what surprised them or what the Agent got wrong.",
                        "If many groups are behind, offer five more minutes or demonstrate the last step on your machine. "
                        "Do not leave the exercise without a shared definition of done.",
                    ]
                )
            )
        else:
            paragraphs.extend(
                _join_script(
                    [
                        f"Hands-on time for {heading}. "
                        f"This exercise is {meta.get('title', heading)}. "
                        f"Goal: {meta.get('objective', 'complete the steps on screen')}. "
                        f"{'Follow the detailed steps in ' + lab + '. ' if lab else ''}",
                        step_text if step_text else "Direct participants to reproduce exactly what appears on this slide.",
                    ]
                )
            )
            for prompt in prompts:
                paragraphs.append(
                    f"Tell them to paste this prompt into the Agent (or read it aloud while they type): "
                    f'"{prompt.replace(chr(10), " ").strip()}"'
                )
            paragraphs.append(
                "Give work time now. Circulate quietly. "
                + (
                    "Watch for Admin versus User API key mix-ups, curl quoting issues, and JSON escaping in PowerShell."
                    if meta.get("type") == "api"
                    else "Watch for people accepting diffs without reading, missing @mentions, or working in the wrong repo."
                    if meta.get("type") != "cli"
                    else "Watch for agent not on PATH, wrong directory, or resumed session pointing at the wrong branch."
                )
                + " When most are done, ask: who got a useful result? Who hit an error we should discuss?"
            )
    elif kind == "demo":
        paragraphs.extend(
            _join_script(
                [
                    f"This slide supports a live demonstration: {heading.replace('Demo: ', '')}. "
                    "Narrate every click and keystroke — assume no one has seen this screen before.",
                    "If the network fails, describe what would happen and show a screenshot or backup recording. "
                    "Save questions until the demo completes unless someone is completely lost.",
                    "Close the demo by stating when they would use this in production and when they would not.",
                ]
            )
        )
    elif kind == "walkthrough":
        paragraphs.extend(
            _join_script(
                [
                    f"This is a walkthrough slide: {heading.replace('Walkthrough: ', '')}. "
                    "Show the configuration or file location on your machine; participants observe unless time allows typing along.",
                    "Explain where the setting lives in Cursor or in the repository, who on a team would maintain it, "
                    "and how it differs from a rule, skill, or MCP server.",
                ]
            )
        )
    elif kind == "diagram":
        alt = re.search(r'alt="([^"]+)"', slide)
        alt_text = alt.group(1) if alt else heading
        paragraphs.extend(
            _join_script(
                [
                    f"This slide is visual: {alt_text}. "
                    "Point to each part of the diagram in order — left to right or top to bottom — and name it once.",
                    "After explaining the flow, ask: does this match how you thought the system worked? "
                    "Misconceptions here will cause mistakes later, so pause for one question.",
                ]
            )
        )
        if quote:
            paragraphs.append(f'Tie the diagram to this idea: "{quote}"')
    elif kind == "table":
        if rows:
            narrated = []
            for row in rows[:6]:
                if len(row) >= 2 and not row[0].startswith("-"):
                    narrated.append(f"{row[0]} — {row[1]}" + (f", {row[2]}" if len(row) > 2 else ""))
            table_speech = ". ".join(narrated)
            paragraphs.append(
                f"Walk this table conversationally: {table_speech}. "
                "Pick the two rows that matter most to your audience and spend extra time there; "
                "summarize the rest in one sentence."
            )
        else:
            paragraphs.append(f"Explain the comparison on this slide: {_plain_text(slide)}")
        if "Key Insight" in slide:
            paragraphs.append(
                "This is a module recap table. For each lesson, ask someone to restate the key insight in their own words."
            )
    elif kind == "quote":
        if quote:
            q = quote.strip('"')
            paragraphs.extend(
                _join_script(
                    [
                        f'Read or closely paraphrase the quote on screen: "{q}"',
                        " ".join(body) if body else "Expand with one concrete example from your own engineering experience.",
                        "Pause two beats after the quote so it lands. Then ask whether anyone has seen the opposite problem in real projects.",
                    ]
                )
            )
        else:
            paragraphs.append(f"Cover the main message: {_plain_text(slide)}")
    elif kind == "code":
        blocks = extract_fenced_code_blocks(slide)
        intro = " ".join(body[:3]) if body else heading
        paragraphs.append(
            f"{intro} "
            "Do not read every line of code unless you are teaching syntax. "
            "Highlight what participants should notice — a parameter value, a pattern, or a mistake to avoid."
        )
        if blocks:
            sample = blocks[0].strip().splitlines()[0][:120]
            paragraphs.append(f'For example, point at this line: "{sample}" and explain why it matters.')
        if "curl" in slide.lower() or "api.cursor.com" in slide.lower():
            paragraphs.append(
                "Remind the room: use environment variables for keys, redact secrets in screen shares, "
                "and never commit `.env` files with live credentials."
            )
    elif kind == "bullets":
        if bullets:
            lead = f"On this slide, {heading}, cover these points in order: "
            lead += " ".join(f"First, {bullets[0]}." if bullets else "")
            for item in bullets[1:4]:
                lead += f" Next, {item}."
            if len(bullets) > 4:
                lead += f" The remaining bullets are detail you can skip if time is short: {', '.join(bullets[4:])}."
            paragraphs.append(lead)
        else:
            paragraphs.append(f"Explain: {_plain_text(slide)}")
    elif kind == "module_summary":
        paragraphs.extend(
            _join_script(
                [
                    f"Module {ctx.module} summary. In sixty seconds, walk the lesson table and restate one key insight per row.",
                    "Ask the closing question: what will you do differently on Monday? Take two or three answers.",
                    "Announce the break or introduce the next module with one connecting sentence.",
                ]
            )
        )
    elif kind == "quick_reference":
        paragraphs.extend(
            _join_script(
                [
                    "This quick reference slide is meant for post-course use. "
                    "Tell participants to screenshot it or copy the commands into their team wiki.",
                    "Offer two minutes for questions on this module only, then move on.",
                ]
            )
        )
    else:
        text = " ".join(body) if body else _plain_text(slide)
        paragraphs.extend(
            _join_script(
                [
                    f"For slide {slide_num}, {heading}: {text}",
                    "Check for questions before you advance. If the room is silent, ask a specific question tied to the slide content.",
                ]
            )
        )

    return _join_script(paragraphs)


def generate_notes_document(source: Path) -> tuple[str, list[tuple[int, str, SlideContext, list[str]]]]:
    markdown = source.read_text(encoding="utf-8")
    slides = split_marp_slides(markdown)
    ctx = SlideContext()
    entries: list[tuple[int, str, SlideContext, list[str]]] = []

    for index, slide in enumerate(slides, start=1):
        _update_context(slide, ctx)
        heading = _heading(slide)
        script = _script_for_slide(slide, index, ctx)
        entries.append((index, heading, SlideContext(**vars(ctx)), script))

    lines = [
        "# Cursor Training Program — Speaker Scripts",
        "",
        f"Full instructor scripts for [`course-complete-marp.md`](course-complete-marp.md) "
        f"({len(slides)} slides). Read aloud or adapt — not bullet hints.",
        "",
        f"*Generated: {date.today().isoformat()}*",
        "",
        "## How to use",
        "",
        "- Match **Slide N** to the page number in the deck footer or Marp presenter view (`p`).",
        "- **[Timing: …]** lines are pacing reminders; they are not spoken verbatim.",
        "- Hands-on slides reference lab guides in [`slide-exercises/`](../slide-exercises/).",
        "- Embedded presenter notes: [`course-complete-marp-with-notes.md`](course-complete-marp-with-notes.md).",
        "",
        "---",
        "",
    ]

    current_module: int | None = None
    for slide_num, heading, slide_ctx, script in entries:
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
        for paragraph in script:
            lines.append(paragraph)
            lines.append("")
        lines.append("---")
        lines.append("")

    return "\n".join(lines).rstrip() + "\n", entries


def inject_marp_notes(source: Path, entries: list[tuple[int, str, SlideContext, list[str]]]) -> str:
    markdown = source.read_text(encoding="utf-8")
    slides = split_marp_slides(markdown)

    if len(slides) != len(entries):
        raise ValueError(f"Slide count mismatch: {len(slides)} slides vs {len(entries)} note entries")

    enriched: list[str] = []
    for slide, (_slide_num, _heading, _ctx, script) in zip(slides, entries):
        note_text = "\n\n".join(script)
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

#!/usr/bin/env python3
"""Generate FINAL_TABLE_OF_CONTENTS.md from slide decks and slide-exercises."""

from __future__ import annotations

import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SLIDES_DIR = ROOT / "slides"
EX_DIR = ROOT / "slide-exercises"
OUTPUT = ROOT / "FINAL_TABLE_OF_CONTENTS.md"

MODULE1_LESSONS = [
    (
        "1.1",
        "How AI Models Work",
        "12 min",
        "Concept",
        "Why AI outputs are probabilistic; next-token prediction; parameters (temperature, top-p); training gap.",
    ),
    (
        "1.2",
        "Hallucinations",
        "10 min",
        "Concept",
        "What hallucinations are in code; why models invent APIs; mitigation strategies and detection checklist.",
    ),
    (
        "1.3",
        "Tokens and Pricing",
        "10 min",
        "Concept",
        "Token basics; input vs. output pricing; cost calculation; optimization and cache effects.",
    ),
    (
        "1.4",
        "Context",
        "12 min",
        "Concept",
        "Context window limits; prioritization pyramid; lost-in-the-middle; good vs. bad context examples.",
    ),
    (
        "1.5",
        "Tool Calling and MCP",
        "8 min",
        "Concept",
        "Tool calling flow; common dev tools; Model Context Protocol architecture and best practices.",
    ),
    (
        "1.6",
        "Agents",
        "8 min",
        "Concept",
        "Agent vs. chatbot; the agent loop; levels of autonomy; how agents change the developer role.",
    ),
]

CORE_MAP = {
    "2.1": "core-exercises/exercise-1/01-open-agent-first-prompt.md",
    "2.2": "core-exercises/exercise-2/02-explain-a-specific-file.md",
    "2.3": "core-exercises/exercise-3/03-make-a-safe-change.md",
    "2.4": "core-exercises/exercise-4/04-use-plan-mode.md",
    "2.5": "core-exercises/exercise-5/05-compare-two-models.md",
    "2.6": "core-exercises/exercise-6/06-use-mentions.md",
    "2.7": "core-exercises/exercise-7/07-use-checkpoints.md",
    "2.8": "core-exercises/exercise-8/08-run-terminal-command.md",
    "3.1": "core-exercises/exercise-13/13-ask-mode-vs-agent-mode.md",
    "3.2": "core-exercises/exercise-9/09-browser-tool-view-page.md",
    "3.3": "core-exercises/exercise-11/11-terminal-tool-run-tests.md",
    "4.1": "core-exercises/exercise-14/14-create-a-rule.md",
    "4.2": "core-exercises/exercise-15/15-use-agents-md.md",
    "4.3": "core-exercises/exercise-16/16-create-a-skill.md",
    "5.1": "core-exercises/exercise-19/19-cli-interactive-mode.md",
    "5.2": "core-exercises/exercise-20/20-cli-one-shot-mode.md",
    "5.3": "core-exercises/exercise-21/21-cli-cloud-handoff.md",
    "5.4": "core-exercises/exercise-22/22-cli-list-resume-sessions.md",
    "6.1": "core-exercises/exercise-23/23-cloud-agent-web-dashboard.md",
    "6.2": "core-exercises/exercise-25/25-cloud-agent-artifacts.md",
}

EXTRA_CORE = [
    ("10", "Browser Tool — Read Console", "core-exercises/exercise-10/10-browser-tool-read-console.md"),
    ("12", "Terminal Tool — Fix Errors", "core-exercises/exercise-12/12-terminal-tool-fix-errors.md"),
    ("17", "Invoke a Skill", "core-exercises/exercise-17/17-invoke-a-skill.md"),
    ("18", "Create a Subagent", "core-exercises/exercise-18/18-create-a-subagent.md"),
    ("24", "Cloud Agent from Slack", "core-exercises/exercise-24/24-cloud-agent-from-slack.md"),
]

SKIP_TITLE_PREFIXES = (
    "Exercise",
    "Module",
    "Learning",
    "Agenda",
    "Windows",
    "Demo:",
    "Walkthrough:",
    "Quick Reference",
)


def parse_agenda(text: str) -> dict[str, dict[str, str | None]]:
    agenda: dict[str, dict[str, str | None]] = {}
    in_agenda = False
    for line in text.splitlines():
        if line.strip() == "## Agenda":
            in_agenda = True
            continue
        if in_agenda:
            if line.startswith("---"):
                break
            match = re.match(r"^\| (\d+\.\d+) \| (.+?) \| ([^|]+)(?:\| ([^|]+))?\|$", line)
            if match:
                lesson_id, topic, time, lesson_type = match.groups()
                agenda[lesson_id] = {
                    "topic": topic.strip(),
                    "time": time.strip(),
                    "type": lesson_type.strip() if lesson_type else None,
                }
    return agenda


def parse_module_overview(text: str) -> dict[str, str]:
    overview: dict[str, str] = {}
    for key in ("Duration", "Format", "Prerequisites", "Module Goal"):
        match = re.search(rf"\*\*{key}\*\*\s*\|\s*([^\|]+)", text)
        if match:
            overview[key] = match.group(1).strip()
    return overview


def parse_learning_objectives(text: str) -> list[str]:
    objectives: list[str] = []
    capture = False
    for line in text.splitlines():
        if line.startswith("## Learning Objectives"):
            capture = True
            continue
        if capture:
            if line.startswith("---"):
                break
            if line.startswith("- "):
                objectives.append(line[2:].strip())
    return objectives


def parse_lessons(text: str) -> dict[str, dict]:
    lines = text.splitlines()
    lessons: dict[str, dict] = {}
    index = 0
    while index < len(lines):
        match = re.match(r"^# Lesson (\d+\.\d+)$", lines[index])
        if not match:
            index += 1
            continue

        lesson_id = match.group(1)
        title = ""
        duration = ""
        end = index + 1
        while end < len(lines):
            if re.match(r"^# Lesson ", lines[end]) or lines[end].startswith("# Up Next"):
                break
            if lines[end].startswith("## ") and not title:
                candidate = lines[end][3:].strip()
                if not candidate.startswith(SKIP_TITLE_PREFIXES):
                    title = candidate
            if lines[end].startswith("_") and ("min" in lines[end].lower() or "Concept" in lines[end]):
                duration = lines[end].strip("_").strip()
            end += 1

        slide_sections: list[str] = []
        demos: list[str] = []
        walkthroughs: list[str] = []
        for pos in range(index, end):
            exercise_match = re.match(r"^## Exercise (\d+\.\d+) — (.+)$", lines[pos])
            if exercise_match and exercise_match.group(1) == lesson_id:
                slide_sections.append(exercise_match.group(2))
            demo_match = re.match(r"^## Demo: (.+)$", lines[pos])
            if demo_match:
                demos.append(demo_match.group(1))
            walkthrough_match = re.match(r"^## Walkthrough: (.+)$", lines[pos])
            if walkthrough_match:
                walkthroughs.append(walkthrough_match.group(1))

        lessons[lesson_id] = {
            "title": title,
            "duration": duration,
            "slide_sections": slide_sections,
            "demos": demos,
            "walkthroughs": walkthroughs,
        }
        index = end
    return lessons


def parse_exercise_file(path: Path) -> tuple[str, dict]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    title = lines[0][2:].strip() if lines and lines[0].startswith("# ") else path.stem
    meta: dict[str, str] = {}
    for line in lines[1:20]:
        for key in ("Module", "Slides", "Time", "Difficulty", "Objective"):
            match = re.match(rf"^\*\*{key}:\*\*\s*(.+)$", line.strip())
            if match:
                meta[key.lower()] = match.group(1).strip()
    match = re.search(r"exercise-(\d+\.\d+)-", path.name)
    lesson_id = match.group(1) if match else ""
    rel_path = path.relative_to(ROOT).as_posix()
    return lesson_id, {"title": title, "path": rel_path, **meta}


def lesson_sort_key(lesson_id: str) -> list[int]:
    return [int(part) for part in lesson_id.split(".")]


def infer_lesson_type(
    lesson_id: str,
    agenda: dict,
    lesson: dict,
    exercise: dict | None,
) -> str:
    if agenda.get(lesson_id, {}).get("type"):
        return str(agenda[lesson_id]["type"])
    if exercise:
        return "Exercise"
    if lesson.get("demos"):
        return "Demo"
    if lesson.get("walkthroughs"):
        return "Walkthrough"
    return "Concept"


def build() -> str:
    exercises: dict[str, dict] = {}
    for path in sorted(EX_DIR.rglob("exercise-*.md")):
        lesson_id, data = parse_exercise_file(path)
        exercises[lesson_id] = data

    lines: list[str] = []
    append = lines.append

    append("# Cursor Training Program — Final Table of Contents")
    append("")
    append(
        "Complete reference for all **10 modules**, **52 lessons**, and **40 hands-on slide exercises** "
        "in the Cursor Training Program. Generated from instructor slide decks (`slides/module-*-marp.md`) "
        "and step-by-step lab guides (`slide-exercises/`)."
    )
    append("")
    append(f"*Generated: {date.today().isoformat()}*")
    append("")
    append(
        "> **Note:** This is a supplementary index. The original "
        "[`TABLE_OF_CONTENTS.md`](TABLE_OF_CONTENTS.md) remains unchanged."
    )
    append("")
    append("---")
    append("")
    append("## At a Glance")
    append("")
    append("| | |")
    append("|---|---|")
    append("| **Duration** | 2 days (~11.5 hours) |")
    append("| **Modules** | 10 |")
    append("| **Lessons** | 52 total |")
    append("| **Slide exercises** | 40 written lab guides in `slide-exercises/` |")
    append("| **Core exercises** | 25 optional hands-on labs in `core-exercises/` |")
    append(
        "| **Slide deck** | "
        "`slides/course-complete-marp-with-notes.md` · "
        "`slides/course-complete-marp.md` |"
    )
    append("| **Combined deck** | `slides/course-complete-marp.md` |")
    append("")
    append("### Day 1 — Cursor Editor and Agent Fluency")
    append("")
    append("Modules 1–5: mental models, editor essentials, agent tools, team customization, CLI automation.")
    append("")
    append("### Day 2 — Cloud Agents, APIs, and Analytics")
    append("")
    append("Modules 6–10: cloud agents UI, API foundations, Cloud Agents API/webhooks, admin analytics, AI code tracking.")
    append("")
    append("---")
    append("")
    append("## Module Index")
    append("")
    append("| # | Day | Module | Format | Duration | Lessons | Exercises | Slide deck |")
    append("|---|-----|--------|--------|----------|---------|-----------|------------|")

    for module_num in range(1, 11):
        deck_path = SLIDES_DIR / f"module-{module_num:02d}-marp.md"
        text = deck_path.read_text(encoding="utf-8")
        title_match = re.search(r"^# (.+)$", text, re.M)
        module_title = title_match.group(1) if title_match else f"Module {module_num}"
        overview = parse_module_overview(text)
        agenda = parse_agenda(text)
        lesson_data = parse_lessons(text)
        day = "Day 1" if module_num <= 5 else "Day 2"
        lesson_count = len(MODULE1_LESSONS) if module_num == 1 else len(agenda) or len(lesson_data)
        exercise_count = 0 if module_num == 1 else sum(
            1
            for lesson_id in lesson_data
            if exercises.get(lesson_id)
            or agenda.get(lesson_id, {}).get("type") == "Exercise"
        )
        append(
            f"| **{module_num}** | {day} | {module_title} | "
            f"{overview.get('Format', '—')} | {overview.get('Duration', '—')} | "
            f"{lesson_count} | {exercise_count} | "
            f"[`module-{module_num:02d}-marp.md`](slides/module-{module_num:02d}-marp.md) |"
        )

    append("")
    append("---")
    append("")

    for module_num in range(1, 11):
        deck_path = SLIDES_DIR / f"module-{module_num:02d}-marp.md"
        text = deck_path.read_text(encoding="utf-8")
        title_match = re.search(r"^# (.+)$", text, re.M)
        module_title = title_match.group(1) if title_match else f"Module {module_num}"
        overview = parse_module_overview(text)
        objectives = parse_learning_objectives(text)
        agenda = parse_agenda(text)
        lesson_data = parse_lessons(text)
        day = "Day 1" if module_num <= 5 else "Day 2"

        append(f"## Module {module_num}. {module_title}")
        append("")
        append(
            f"**Day:** {day} · **Duration:** {overview.get('Duration', '—')} · "
            f"**Format:** {overview.get('Format', '—')}"
        )
        append("")
        if overview.get("Module Goal"):
            append(f"**Module goal:** {overview['Module Goal']}")
            append("")
        if overview.get("Prerequisites"):
            append(f"**Prerequisites:** {overview['Prerequisites']}")
            append("")
        append(
            f"**Slide deck:** [`slides/module-{module_num:02d}-marp.md`]"
            f"(slides/module-{module_num:02d}-marp.md) · "
            f"**HTML:** [`slides/module-{module_num:02d}-marp.html`]"
            f"(slides/module-{module_num:02d}-marp.html)"
        )
        append("")
        if objectives:
            append("**Learning objectives**")
            append("")
            for objective in objectives:
                append(f"- {objective}")
            append("")
        append("### Lessons and exercises")
        append("")

        if module_num == 1:
            lesson_items = MODULE1_LESSONS
            for lesson_id, topic, time, lesson_type, summary in lesson_items:
                append(f"#### Lesson {lesson_id} — {topic}")
                append("")
                append(f"**Time:** {time} · **Type:** {lesson_type}")
                append("")
                append(summary)
                append("")
                append("*Concept-only lesson — no hands-on exercise.*")
                append("")
            append("---")
            append("")
            continue

        lesson_ids = sorted(set(list(agenda.keys()) + list(lesson_data.keys())), key=lesson_sort_key)
        for lesson_id in lesson_ids:
            agenda_row = agenda.get(lesson_id, {})
            lesson = lesson_data.get(lesson_id, {})
            topic = agenda_row.get("topic") or lesson.get("title") or lesson_id
            time = agenda_row.get("time") or lesson.get("duration") or ""
            exercise = exercises.get(lesson_id)
            lesson_type = infer_lesson_type(lesson_id, agenda, lesson, exercise)

            append(f"#### Lesson {lesson_id} — {topic}")
            append("")
            meta = [f"**Type:** {lesson_type}"]
            if time:
                meta.insert(0, f"**Time:** {time}")
            append(" · ".join(meta))
            append("")

            if lesson.get("demos"):
                append("**Demonstrations:**")
                for demo in lesson["demos"]:
                    append(f"- {demo}")
                append("")
            if lesson.get("walkthroughs"):
                append("**Walkthroughs:**")
                for walkthrough in lesson["walkthroughs"]:
                    append(f"- {walkthrough}")
                append("")

            if exercise:
                append("**Exercise**")
                append("")
                append("| Field | Detail |")
                append("|-------|--------|")
                append(f"| **Title** | {exercise['title']} |")
                if exercise.get("time"):
                    append(f"| **Lab time** | {exercise['time']} |")
                if exercise.get("difficulty"):
                    append(f"| **Difficulty** | {exercise['difficulty']} |")
                if exercise.get("objective"):
                    append(f"| **Objective** | {exercise['objective']} |")
                append(f"| **Lab guide** | [`{exercise['path']}`]({exercise['path']}) |")
                if exercise.get("slides"):
                    append(f"| **Slides** | {exercise['slides']} |")
                if lesson_id in CORE_MAP:
                    core_path = CORE_MAP[lesson_id]
                    append(f"| **Related core exercise** | [`{core_path}`]({core_path}) |")
                append("")
                if lesson.get("slide_sections"):
                    append("**Slide sections covered:**")
                    for section in lesson["slide_sections"]:
                        append(f"- Exercise {lesson_id} — {section}")
                    append("")
            elif lesson_type == "Demo" or lesson.get("demos"):
                append("*Demonstration-only lesson — no written slide exercise file.*")
                append("")
            elif lesson_type == "Walkthrough" or lesson.get("walkthroughs"):
                append("*Walkthrough-only lesson — no written slide exercise file.*")
                append("")
            elif module_num == 7 and lesson_id == "7.1":
                append("*Concept-only lesson (API landscape overview) — hands-on exercises begin at Lesson 7.2.*")
                append("")
            elif module_num == 8 and lesson_id == "8.6":
                append("*Capstone integration exercise covered in slide deck — no separate slide-exercises file.*")
                append("")

        append("---")
        append("")

    append("## Slide Exercise Master Index")
    append("")
    append("All hands-on lab guides under `slide-exercises/`, sorted by module.")
    append("")
    append("| Exercise | Title | Module | Time | Difficulty | Lab guide |")
    append("|----------|-------|--------|------|------------|-----------|")
    for lesson_id in sorted(exercises.keys(), key=lesson_sort_key):
        exercise = exercises[lesson_id]
        short_title = exercise["title"].split(": ", 1)[-1]
        append(
            f"| **{lesson_id}** | {short_title} | {exercise.get('module', '—')} | "
            f"{exercise.get('time', '—')} | {exercise.get('difficulty', '—')} | "
            f"[`{Path(exercise['path']).name}`]({exercise['path']}) |"
        )

    append("")
    append("---")
    append("")
    append("## Core Exercises Cross-Reference")
    append("")
    append(
        "Optional calculator-based labs in `core-exercises/` that align with slide exercises (Modules 2–6). "
        "See [`core-exercises/optional-core-exercises-guide.md`](core-exercises/optional-core-exercises-guide.md) "
        "for essential vs. optional guidance."
    )
    append("")
    append("| Slide exercise | Core exercise | Path |")
    append("|----------------|---------------|------|")
    for lesson_id in sorted(CORE_MAP.keys(), key=lesson_sort_key):
        core_path = CORE_MAP[lesson_id]
        folder = core_path.split("/")[1]
        append(f"| **{lesson_id}** | {folder} | [`{core_path}`]({core_path}) |")

    append("")
    append("**Additional core exercises** (no direct slide-exercise counterpart in this repo):")
    append("")
    append("| Core # | Title | Path |")
    append("|--------|-------|------|")
    for core_num, title, core_path in EXTRA_CORE:
        append(f"| **{core_num}** | {title} | [`{core_path}`]({core_path}) |")

    append("")
    append("---")
    append("")
    append("## Supporting Materials")
    append("")
    append("| Resource | Location | Description |")
    append("|----------|----------|-------------|")
    append("| Original TOC | [`TABLE_OF_CONTENTS.md`](TABLE_OF_CONTENTS.md) | High-level program overview and sample schedule |")
    append("| Combined slide deck | [`slides/course-complete-marp.md`](slides/course-complete-marp.md) | All modules in one Marp file |")
    append("| Module source docs | [`modules-basedon-toc/`](modules-basedon-toc/) | Module planning documents (modules 1–10) |")
    append("| Learn readmes | [`learn/learn-readmes-index.md`](learn/learn-readmes-index.md) | Curated concept reading paths |")
    append("| API content readmes | [`api-content-readmes/api-content-readmes-index.md`](api-content-readmes/api-content-readmes-index.md) | API reference reading paths |")
    append("| Docs content readmes | [`docs-content-readmes/docs-content-readmes-index.md`](docs-content-readmes/docs-content-readmes-index.md) | Cursor docs reading paths |")
    append("| Core exercises guide | [`core-exercises/optional-core-exercises-guide.md`](core-exercises/optional-core-exercises-guide.md) | Essential vs. optional exercise recommendations |")

    return "\n".join(lines) + "\n"


def main() -> None:
    content = build()
    OUTPUT.write_text(content, encoding="utf-8")
    print(f"Wrote {OUTPUT} ({len(content.splitlines())} lines)")


if __name__ == "__main__":
    main()

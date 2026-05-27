#!/usr/bin/env python3
"""Rebuild module 5-10 exercise slide chains from lab guides (2 steps/slide, no overflow)."""

from __future__ import annotations

import re
from pathlib import Path

from marp_tables import split_marp_slides

REPO = Path(__file__).resolve().parent.parent
DECK = REPO / "slides" / "course-complete-marp-with-notes.md"
SE = REPO / "slide-exercises"

_STEP = re.compile(
    r"### Step (\d+) — (.+?)\n\n(.*?)(?=\n---\n\n### Step |\n---\n\n\*\*Success|\n---\n\n## |\Z)",
    re.DOTALL,
)
_EX_HEAD = re.compile(r"^##\s+Exercise\s+(\d+)\.(\d+)\s+—", re.MULTILINE)
_FENCE = re.compile(r"```(?:powershell|bash|python)?\n(.*?)```", re.DOTALL)
_SUCCESS = re.compile(r"\*\*Success criteria:\*\*\s*(.+)", re.IGNORECASE | re.DOTALL)


def _visible(slide: str) -> str:
    return re.sub(r"<!--.*?-->", "", slide, flags=re.DOTALL).strip()


def _exercise_key(slide: str) -> tuple[int, int] | None:
    m = _EX_HEAD.search(_visible(slide))
    return (int(m.group(1)), int(m.group(2))) if m else None


def _parse_guide(path: Path) -> tuple[list[dict], str | None]:
    text = path.read_text(encoding="utf-8")
    start = text.find("## Steps from the training slides")
    if start == -1:
        return [], None
    end = text.find("\n---\n\n## ", start + 10)
    section = text[start:end] if end != -1 else text[start:]
    steps: list[dict] = []
    for m in _STEP.finditer(section):
        body = m.group(3).strip()
        codes = [f.strip() for f in _FENCE.findall(body)]
        # prose after **Do this:**
        do = re.sub(r"```.*?```", "", body, flags=re.DOTALL)
        do = re.sub(r"\*\*Expected result:\*\*.*", "", do, flags=re.DOTALL | re.IGNORECASE)
        do = re.sub(r"\*\*Do this[^*]*\*\*:?", "", do, flags=re.DOTALL | re.IGNORECASE)
        do = re.sub(r"\s+", " ", do).strip()
        em = re.search(r"\*\*Expected result:\*\*\s*(.+)", body, re.IGNORECASE | re.DOTALL)
        expected = em.group(1).strip().split("\n")[0] if em else ""
        steps.append(
            {
                "n": int(m.group(1)),
                "title": m.group(2).strip(),
                "do": do[:200],
                "codes": codes,
                "expected": expected[:140],
            }
        )
    sm = _SUCCESS.search(section)
    success = sm.group(1).strip().split("\n")[0] if sm else None
    return steps, success


def _code_lang(code: str) -> str:
    if any(
        x in code
        for x in ("$env:", "agent", "curl.exe", "Get-Date", "ConvertFrom", "Invoke-RestMethod")
    ):
        return "powershell"
    return ""


def _step_weight(step: dict) -> int:
    w = 2
    if step["do"]:
        w += 1
    for code in step.get("codes", []):
        w += len(code.splitlines()) + 2
    if step["expected"]:
        w += 1
    return w


def _long_code(step: dict) -> bool:
    return any(len(c.splitlines()) > 7 for c in step.get("codes", []))


def _chunk_steps(steps: list[dict]) -> list[list[dict]]:
    chunks: list[list[dict]] = []
    i = 0
    while i < len(steps):
        solo = _long_code(steps[i])
        if not solo and i + 1 < len(steps):
            pair_w = _step_weight(steps[i]) + _step_weight(steps[i + 1])
            solo = pair_w > 10 or _long_code(steps[i + 1])
        if solo or i + 1 >= len(steps):
            chunks.append([steps[i]])
            i += 1
        else:
            chunks.append([steps[i], steps[i + 1]])
            i += 2
    return chunks


def _format_step(step: dict) -> list[str]:
    lines = [f"**Step {step['n']}:** {step['title']}"]
    if step["do"]:
        lines.append(f"- {step['do']}")
    for code in step.get("codes", []):
        lang = _code_lang(code)
        lines.append(f"```{lang}")
        lines.append(code)
        lines.append("```")
    if step["expected"]:
        lines.append(f"- **Expected:** {step['expected']}")
    lines.append("")
    return lines


def _slide_class(part: list[dict], first: bool, mod: int) -> str:
    body_lines = sum(_step_weight(s) for s in part) + (2 if first and mod >= 5 else 0)
    max_code = max(
        (len(c.splitlines()) for s in part for c in s.get("codes", [])),
        default=0,
    )
    if max_code > 10 or body_lines > 14:
        return "fit-xs"
    if max_code > 5 or body_lines > 10 or len(part) > 1:
        return "fit-sm"
    return "fit-md"


def _build_exercise_slides(
    mod: int, ex: int, steps: list[dict], success: str | None, guide_rel: str
) -> list[str]:
    if not steps:
        return []
    out: list[str] = []
    chunks = _chunk_steps(steps)
    for idx, part in enumerate(chunks):
        n0, n1 = part[0]["n"], part[-1]["n"]
        cont = " (cont.)" if idx else ""
        if n0 == n1:
            title = f"## Exercise {mod}.{ex} — Step {n0}{cont}"
        else:
            title = f"## Exercise {mod}.{ex} — Steps {n0}–{n1}{cont}"
        cls = _slide_class(part, idx == 0, mod)
        lines = [f"<!-- _class: {cls} -->", "", title, ""]
        if idx == 0 and mod <= 6:
            lines.append(
                "**Windows:** Use **PowerShell** in Cursor (``Ctrl+` `` → **PowerShell**)"
            )
            lines.append("")
        elif idx == 0 and mod >= 7:
            lines.append(
                "**Windows:** PowerShell · `$env:…` API keys · **`curl.exe`** for API calls"
            )
            lines.append("")
        for s in part:
            lines.extend(_format_step(s))
        note = f"Exercise {mod}.{ex} — steps {n0}–{n1}. Lab: `{guide_rel}`"
        out.append("\n".join(lines).rstrip() + f"\n\n<!--\n{note}\n-->")

    if success:
        sc_note = f"Exercise {mod}.{ex} success criteria. Lab: `{guide_rel}`"
        lines = [
            "<!-- _class: fit-md -->",
            "",
            f"## Exercise {mod}.{ex} — Success criteria",
            "",
            f"**Check:** {success}",
            "",
            f"<!--\n{sc_note}\n-->",
        ]
        out.append("\n".join(lines))
    return out


def _groups(slides: list[str], min_mod: int = 5) -> list[tuple[tuple[int, int], int, int]]:
    groups: list[tuple[tuple[int, int], int, int]] = []
    i = 0
    while i < len(slides):
        key = _exercise_key(slides[i])
        if not key or key[0] < min_mod:
            i += 1
            continue
        j = i + 1
        while j < len(slides):
            v = _visible(slides[j])
            k = _exercise_key(slides[j])
            if k and k != key:
                break
            if re.search(r"^#\s+Lesson\s+\d+\.\d+", v, re.MULTILINE):
                break
            j += 1
        groups.append((key, i, j))
        i = j
    return groups


def rebuild() -> tuple[int, int]:
    guides: dict[tuple[int, int], Path] = {}
    for mod in range(5, 11):
        folder = SE / f"module-{mod:02d}"
        if not folder.is_dir():
            continue
        for p in sorted(folder.glob("exercise-*.md")):
            m = re.search(r"exercise-(\d+)\.(\d+)", p.name)
            if m:
                guides[(int(m.group(1)), int(m.group(2)))] = p

    text = DECK.read_text(encoding="utf-8")
    fm_end = text.find("\n---\n", 3) + 5
    frontmatter, body = text[:fm_end], text[fm_end:]
    slides = split_marp_slides(body)

    groups = _groups(slides)
    replaced = 0
    new_count = 0
  # rebuild tail-first
    for key, start, end in reversed(groups):
        if key not in guides:
            continue
        steps, success = _parse_guide(guides[key])
        rel = guides[key].relative_to(REPO).as_posix()
        new_slides = _build_exercise_slides(key[0], key[1], steps, success, rel)
        if not new_slides:
            continue
        slides[start:end] = new_slides
        replaced += 1
        new_count += len(new_slides)

    # Remove any leftover Follow along on non-rebuilt slides
    cleaned = 0
    for i, slide in enumerate(slides):
        if "Follow along (Windows)" in _visible(slide):
            body = slide.split("\n<!--\n", 1)[0]
            body = re.sub(
                r"\*\*Follow along \(Windows\).*?(?=\n\n\*\*On the next|\n\n_Full lab|\n\n## |\Z)",
                "",
                body,
                flags=re.DOTALL,
            )
            body = re.sub(r"\n\n_Full lab guide[^\n]*\n*", "\n", body)
            body = re.sub(r"\n\n\*\*On the next slides:\*\*[^\n]*\n*", "\n", body)
            slides[i] = body.rstrip() + (
                "\n<!--\n" + slide.split("\n<!--\n", 1)[1]
                if "\n<!--\n" in slide
                else "\n<!--\n-->\n"
            )
            cleaned += 1

    slides = [s.strip() for s in slides if _visible(s).strip()]

    out = frontmatter + "\n\n" + "\n\n---\n\n".join(slides) + "\n"
    DECK.write_text(out, encoding="utf-8")
    before = len(split_marp_slides(body))
    after = len(slides)
    print(f"Rebuilt {replaced} exercises ({new_count} slides); removed stray Follow along on {cleaned}")
    print(f"Slide count: {before} -> {after}")
    return before, after


if __name__ == "__main__":
    rebuild()

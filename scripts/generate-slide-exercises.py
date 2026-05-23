#!/usr/bin/env python3
"""Generate detailed slide-aligned exercise guides in slide-exercises/."""

from __future__ import annotations

import re
from collections import defaultdict
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SLIDES = REPO / "slides"
OUT = REPO / "slide-exercises"
CORE = REPO / "core-exercises"
API = REPO / "api-exercises"

MODULE_TITLES = {
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

# (module, exercise_num) -> lesson title, objective, time, optional source file
EXERCISE_META: dict[tuple[int, int], dict] = {
    (2, 1): {"title": "Codebase Understanding", "time": "20 min", "type": "cursor",
             "core": "exercise-1/01-open-agent-first-prompt.md",
             "objective": "Use the Cursor Agent to orient yourself in an unfamiliar repository."},
    (2, 2): {"title": "Explaining a Specific File or Symbol", "time": "13 min", "type": "cursor",
             "core": "exercise-2/02-explain-a-specific-file.md",
             "objective": "Get targeted explanations of one file or symbol without reading the whole repo."},
    (2, 3): {"title": "Making a Safe, Reviewable Change", "time": "13 min", "type": "cursor",
             "core": "exercise-3/03-make-a-safe-change.md",
             "objective": "Let the Agent propose a small change and review the diff before accepting."},
    (2, 4): {"title": "Plan Mode", "time": "13 min", "type": "cursor",
             "core": "exercise-4/04-use-plan-mode.md",
             "objective": "Use Plan Mode to design a change before the Agent edits files."},
    (2, 5): {"title": "Comparing Two Models", "time": "13 min", "type": "cursor",
             "core": "exercise-5/05-compare-two-models.md",
             "objective": "Run the same prompt on two models and compare quality, speed, and cost."},
    (2, 6): {"title": "Precise Context with @mentions", "time": "13 min", "type": "cursor",
             "core": "exercise-6/06-use-mentions.md",
             "objective": "Use @mentions to point the Agent at exact files, symbols, and context."},
    (2, 7): {"title": "Checkpoints", "time": "8 min", "type": "cursor",
             "core": "exercise-7/07-use-checkpoints.md",
             "objective": "Create and restore checkpoints before risky Agent experiments."},
    (2, 8): {"title": "Terminal Integration", "time": "13 min", "type": "cursor",
             "core": "exercise-8/08-run-terminal-command.md",
             "objective": "Let the Agent run terminal commands and react to command output."},
    (3, 1): {"title": "Ask Mode vs. Agent Mode", "time": "18 min", "type": "cursor",
             "core": "exercise-13/13-ask-mode-vs-agent-mode.md",
             "objective": "Learn when Ask Mode is read-only and when Agent Mode can edit files."},
    (3, 2): {"title": "Browser Tool", "time": "18 min", "type": "cursor",
             "core": "exercise-9/09-browser-tool-view-page.md",
             "objective": "Use the Browser tool so the Agent can inspect live web pages."},
    (3, 3): {"title": "Terminal Tool", "time": "20 min", "type": "cursor",
             "core": "exercise-11/11-terminal-tool-run-tests.md",
             "objective": "Use the Terminal tool to run tests, read output, and fix failures."},
    (3, 4): {"title": "Effective Prompting in Practice", "time": "22 min", "type": "cursor",
             "objective": "Write constrained prompts and reusable templates for real tasks."},
    (4, 1): {"title": "Creating a Rule", "time": "20 min", "type": "cursor",
             "core": "exercise-14/14-create-a-rule.md",
             "objective": "Create Cursor rules that persist coding standards for your team."},
    (4, 2): {"title": "Repository Instructions", "time": "13 min", "type": "cursor",
             "core": "exercise-15/15-use-agents-md.md",
             "objective": "Add repository instructions the Agent reads automatically."},
    (4, 3): {"title": "Creating and Invoking a Skill", "time": "20 min", "type": "cursor",
             "core": "exercise-16/16-create-a-skill.md",
             "objective": "Build and invoke reusable Agent skills for repeated workflows."},
    (5, 1): {"title": "Interactive CLI", "time": "20 min", "type": "cli",
             "core": "exercise-19/19-cli-interactive-mode.md",
             "objective": "Start an interactive Cursor CLI session from the terminal."},
    (5, 2): {"title": "One-Shot CLI", "time": "20 min", "type": "cli",
             "core": "exercise-20/20-cli-one-shot-mode.md",
             "objective": "Run single-shot Agent commands from scripts and CI."},
    (5, 3): {"title": "Cloud Handoff", "time": "18 min", "type": "cli",
             "core": "exercise-21/21-cli-cloud-handoff.md",
             "objective": "Hand off a local CLI task to a Cloud Agent with &."},
    (5, 4): {"title": "Listing and Resuming Sessions", "time": "20 min", "type": "cli",
             "core": "exercise-22/22-cli-list-resume-sessions.md",
             "objective": "List, name, resume, and compress CLI Agent sessions."},
    (6, 1): {"title": "Launching a Cloud Agent", "time": "25 min", "type": "cloud",
             "core": "exercise-23/23-cloud-agent-web-dashboard.md",
             "objective": "Launch a Cloud Agent from the Cursor UI and track its run."},
    (6, 2): {"title": "Cloud Agent Artifacts", "time": "25 min", "type": "cloud",
             "core": "exercise-25/25-cloud-agent-artifacts.md",
             "objective": "Collect and download artifacts produced by Cloud Agents."},
    (7, 2): {"title": "Generate and Test API Keys", "time": "15 min", "type": "api",
             "api": "exercise-1/01-generate-and-test-api-keys.md",
             "objective": "Create Admin and User API keys and verify authentication."},
    (7, 3): {"title": "Rate Limits and Error Handling", "time": "15 min", "type": "api",
             "api": "exercise-2/02-rate-limits-and-error-handling.md",
             "objective": "Handle 429 responses with backoff and rate-limit headers."},
    (7, 4): {"title": "ETag Caching", "time": "15 min", "type": "api",
             "api": "exercise-3/03-etag-caching.md",
             "objective": "Use ETags to avoid re-downloading unchanged API data."},
    (7, 5): {"title": "List Available Models", "time": "10 min", "type": "api",
             "api": "exercise-4/04-list-available-models.md",
             "objective": "Query available models and pick the right one programmatically."},
    (8, 1): {"title": "Create a Cloud Agent via API", "time": "15 min", "type": "api",
             "api": "exercise-5/05-create-cloud-agent.md",
             "objective": "Create a Cloud Agent run using curl or Python."},
    (8, 2): {"title": "Stream Agent Responses (SSE)", "time": "15 min", "type": "api",
             "api": "exercise-6/06-stream-agent-responses.md",
             "objective": "Stream Cloud Agent events with Server-Sent Events."},
    (8, 3): {"title": "List and Download Artifacts", "time": "15 min", "type": "api",
             "api": "exercise-7/07-list-and-download-artifacts.md",
             "objective": "Wait for completion, list artifacts, and download outputs."},
    (8, 4): {"title": "Webhooks and HMAC Verification", "time": "15 min", "type": "api",
             "api": "exercise-20/20-create-webhook-endpoint.md",
             "objective": "Receive webhooks and verify HMAC signatures."},
    (8, 5): {"title": "Test Webhooks with ngrok", "time": "15 min", "type": "api",
             "api": "exercise-21/21-test-webhooks-with-ngrok.md",
             "objective": "Expose a local server with ngrok and inspect webhook payloads."},
    (9, 1): {"title": "List Team Members", "time": "13 min", "type": "api",
             "api": "exercise-8/08-list-team-members.md",
             "objective": "List team members with pagination and export to CSV."},
    (9, 2): {"title": "Daily Usage Data", "time": "15 min", "type": "api",
             "api": "exercise-9/09-get-daily-usage-data.md",
             "objective": "Pull daily usage and build a weekly cost report."},
    (9, 3): {"title": "Set User Spend Limits", "time": "13 min", "type": "api",
             "api": "exercise-10/10-set-user-spend-limits.md",
             "objective": "Set and bulk-update per-user spending limits."},
    (9, 4): {"title": "Model Usage Analytics", "time": "13 min", "type": "api",
             "api": "exercise-12/12-get-model-usage-analytics.md",
             "objective": "Analyze model usage and identify optimization opportunities."},
    (9, 5): {"title": "Daily Active Users (DAU)", "time": "10 min", "type": "api",
             "api": "exercise-13/13-get-daily-active-users.md",
             "objective": "Report daily active users over a date range."},
    (9, 6): {"title": "Leaderboards", "time": "11 min", "type": "api",
             "api": "exercise-14/14-get-leaderboard.md",
             "objective": "Build leaderboards for tabs, AI lines, and agent runs."},
    (10, 1): {"title": "AI Commit Metrics", "time": "8 min", "type": "api",
              "api": "exercise-16/16-get-ai-commit-metrics.md",
              "objective": "Fetch AI commit metrics and calculate contribution percentage."},
    (10, 2): {"title": "Bulk Export via CSV Streaming", "time": "7 min", "type": "api",
              "api": "exercise-17/17-download-ai-commit-metrics-csv.md",
              "objective": "Stream large CSV exports for BI tools."},
    (10, 3): {"title": "Granular AI Change Events", "time": "7 min", "type": "api",
              "api": "exercise-18/18-get-granular-ai-change-metrics.md",
              "objective": "Query per-change AI events for compliance reporting."},
    (10, 4): {"title": "Reporting Dashboard Architecture", "time": "Take-home", "type": "api",
              "api": "exercise-23/23-build-complete-dashboard.md",
              "objective": "Design a leadership dashboard combining analytics APIs."},
}

CURSOR_BASICS = """## Cursor basics (read this first)

| Task | Windows / Linux | Mac | Where in Cursor |
|------|-----------------|-----|-----------------|
| Open a project folder | `Ctrl+K Ctrl+O` or **File → Open Folder** | `Cmd+O` | Title bar / Explorer |
| Open **Agent** panel | `Ctrl+I` | `Cmd+I` | Right side panel |
| Open **Chat** panel | `Ctrl+L` | `Cmd+L` | Side panel (Ask/Chat) |
| Integrated terminal | ``Ctrl+` `` | ``Ctrl+` `` | Bottom panel |
| Command Palette | `Ctrl+Shift+P` | `Cmd+Shift+P` | Search any command |
| Accept Agent diff | Click **Accept** / **Accept All** | Same | Inline diff in editor |
| Reject Agent diff | Click **Reject** | Same | Inline diff in editor |
| Switch Agent mode | Mode dropdown at bottom of Agent panel | Same | Agent panel footer |
| Toggle Plan Mode | `Shift+Tab` in Agent | Same | Agent panel |

**Tip for beginners:** Keep the **Explorer** (left), **editor** (center), and **Agent** (right) visible. Send prompts in the Agent panel; review every diff before accepting.
"""

CLI_BASICS = """## CLI basics (read this first)

1. Open **PowerShell** in Cursor: ``Ctrl+` `` → select **PowerShell**.
2. Confirm the CLI is installed: `agent --version`
3. If missing, install from Cursor: **Command Palette** → `Shell Command: Install 'cursor' command in PATH` (or follow Cursor docs for `agent` CLI).
4. Run commands from your **project root** unless the exercise says otherwise.
"""

API_BASICS = """## API basics (read this first)

1. Use **PowerShell** or **Git Bash** in Cursor's terminal (``Ctrl+` ``).
2. Store keys in environment variables — never commit them:

```powershell
$env:CURSOR_ADMIN_API_KEY = "crsr_your_key_here"
$env:CURSOR_USER_API_KEY = "cursor_user_your_key_here"
```

3. Prefer `curl.exe` on Windows (not the `curl` alias) or Python `requests`.
4. Run scripts from a dedicated folder inside this repo or your own sandbox project.
"""

CLOUD_BASICS = """## Cloud Agents in the UI (read this first)

1. Sign in to Cursor with a plan that includes **Cloud Agents**.
2. Open the **Cloud Agents** view from the Cursor sidebar (or Command Palette → "Cloud Agents").
3. Keep the web dashboard open in a browser tab if the exercise references cursor.com/agents.
4. Use the **Agent panel** (`Ctrl+I`) for local prompts; use Cloud UI for remote runs.
"""


def slugify(text: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return slug[:70] or "exercise"


def strip_frontmatter(text: str) -> str:
    text = text.lstrip("\ufeff")
    if not text.startswith("---"):
        return text
    end = text.find("\n---\n", 3)
    return text[end + 5 :] if end != -1 else text


def split_slides(body: str) -> list[str]:
    return [p.strip("\n") for p in re.split(r"\n---\n", body) if p.strip("\n")]


def extract_exercise_slides(module_num: int) -> dict[int, list[str]]:
    path = SLIDES / f"module-{module_num:02d}-marp.md"
    if not path.exists():
        return {}
    body = strip_frontmatter(path.read_text(encoding="utf-8"))
    slides = split_slides(body)
    grouped: dict[int, list[str]] = defaultdict(list)
    for slide in slides:
        match = re.search(rf"## Exercise {module_num}\.(\d+)", slide)
        if match:
            grouped[int(match.group(1))].append(slide)
    return grouped


def rewrite_core_reference_paths(text: str, core_rel: str = "") -> str:
    """Core exercise docs use paths relative to core-exercises/; slide guides need ../../core-exercises/."""
    core_prefix = "../../core-exercises"

    text = re.sub(
        r"\]\(\.\./exercise-(\d+)/([^)]+)\)",
        rf"]({core_prefix}/exercise-\1/\2)",
        text,
    )
    text = text.replace(
        "](../08-browser-tool/08-browser-tool.md)",
        f"]({core_prefix}/exercise-10/10-browser-tool-read-console.md)",
    )
    text = text.replace(
        "Exercise 8 – Browser Tool (extended lab)",
        "Exercise 10 – Browser Tool (Read Console)",
    )
    text = re.sub(
        r"\]\(calculator\.c\)",
        f"]({core_prefix}/exercise-1/calculator.c)",
        text,
    )

    if core_rel:
        ex_dir = core_rel.split("/")[0]
        calc_link = f"[`calculator.c`]({core_prefix}/{ex_dir}/calculator.c)"
        calc_dir = f"`core-exercises/{ex_dir}/`"

        prose_fixes = [
            (
                "Continue with `calculator.c` in **this** folder (same directory as this doc). "
                "If you already split helpers in earlier exercises, you can copy `math_utils.h` / "
                "`math_utils.c` here too.",
                f"Open {calc_dir} in Cursor and continue with {calc_link}. If you already split "
                f"helpers in earlier exercises, you can copy "
                f"[`math_utils.h`]({core_prefix}/exercise-6/math_utils.h) / "
                f"[`math_utils.c`]({core_prefix}/exercise-6/math_utils.c) from "
                f"`core-exercises/exercise-6/`.",
            ),
            (
                "Continue with `calculator.c` in **this** folder (same directory as this doc):",
                f"Open {calc_dir} in Cursor and continue with {calc_link}:",
            ),
            (
                "Continue with `calculator.c` from previous exercises (or the copy in this folder):",
                f"Continue with {calc_link} from {calc_dir}:",
            ),
            (
                "A ready-to-use copy is included in this folder as [`calculator.c`](calculator.c). "
                "Open the `exercise-1` folder (under `core-exercises` in this repo) in Cursor and work from there.",
                f"A ready-to-use copy is at {calc_link}. Open {calc_dir} "
                f"(under `core-exercises` in this repo) in Cursor and work from there.",
            ),
            (
                "Save this as `calculator.c` in an empty folder (or use the file in this folder), "
                "then open that folder in Cursor.",
                f"Save this as `calculator.c` in an empty folder (or use {calc_link}), "
                f"then open that folder in Cursor.",
            ),
            (
                "If you don't have existing tests, the `test_calculator.c` file in this folder "
                "already contains the example below. You can also recreate it from scratch.",
                f"If you don't have existing tests, "
                f"[`test_calculator.c`]({core_prefix}/exercise-11/test_calculator.c) in "
                f"`core-exercises/exercise-11/` already contains the example below. "
                f"You can also recreate it from scratch.",
            ),
        ]
        for old, new in prose_fixes:
            text = text.replace(old, new)

    return text


def rewrite_slide_asset_paths(text: str) -> str:
    """Slide decks use assets/ relative to slides/; exercise guides need slides/assets/."""
    return re.sub(
        r'src="assets/',
        'src="../../slides/assets/',
        text,
    )


def clean_slide_for_doc(slide: str) -> str:
    lines = slide.splitlines()
    cleaned: list[str] = []
    for line in lines:
        if line.startswith("<!--"):
            continue
        if re.match(rf"^## Exercise \d+\.\d+", line):
            continue
        cleaned.append(line)
    text = "\n".join(cleaned).strip()
    text = re.sub(r"\n{3,}", "\n\n", text)
    return rewrite_slide_asset_paths(text)


def extract_success_criteria(slides: list[str]) -> list[str]:
    items: list[str] = []
    for slide in slides:
        if "**Success Criteria:**" not in slide and "Success Criteria:" not in slide:
            continue
        for line in slide.splitlines():
            line = line.strip()
            if line.startswith("- ") and "Success Criteria" not in line:
                items.append(line[2:].strip())
            elif line.startswith("**Success Criteria:**"):
                rest = line.replace("**Success Criteria:**", "").strip()
                if rest.startswith("-"):
                    rest = rest.lstrip("-").strip()
                if rest:
                    items.append(rest)
    return items


def load_reference(meta: dict) -> str:
    for key in ("core", "api"):
        rel = meta.get(key)
        if not rel:
            continue
        base = CORE if key == "core" else API
        path = base / rel
        if path.exists():
            text = path.read_text(encoding="utf-8")
            # Drop top title block through first --- if present
            parts = text.split("\n---\n", 1)
            body = parts[1].strip() if len(parts) > 1 else text
            return rewrite_core_reference_paths(body, rel)
    return ""


def build_document(module_num: int, ex_num: int, meta: dict, slide_chunks: list[str]) -> str:
    title = meta["title"]
    slug = slugify(title)
    module_title = MODULE_TITLES[module_num]
    ex_type = meta.get("type", "cursor")

    if ex_type == "cursor":
        basics = CURSOR_BASICS
    elif ex_type == "cli":
        basics = CLI_BASICS
    elif ex_type == "api":
        basics = API_BASICS
    elif ex_type == "cloud":
        basics = CLOUD_BASICS
    else:
        basics = CURSOR_BASICS

    slide_body = "\n\n---\n\n".join(clean_slide_for_doc(s) for s in slide_chunks if clean_slide_for_doc(s))
    criteria = extract_success_criteria(slide_chunks)
    reference = load_reference(meta)

    lines = [
        f"# Exercise {module_num}.{ex_num}: {title}",
        "",
        f"**Module {module_num}:** {module_title}  ",
        f"**Slides:** `slides/module-{module_num:02d}-marp.md` (Lesson {module_num}.{ex_num})  ",
        f"**Time:** {meta.get('time', '15 min')}  ",
        "**Difficulty:** Beginner",
        "",
        f"**Objective:** {meta['objective']}",
        "",
        "---",
        "",
        basics,
        "",
        "---",
        "",
        "## Steps from the training slides",
        "",
        "Follow these steps in order. Copy prompts exactly unless the exercise tells you to adapt them.",
        "",
        slide_body or "_No slide steps extracted — use the reference section below._",
        "",
    ]

    if criteria:
        lines.extend(["---", "", "## Success criteria", ""])
        for item in criteria:
            lines.append(f"- [ ] {item}")
        lines.append("")

    if reference:
        lines.extend([
            "---",
            "",
            "## Detailed reference (expanded instructions)",
            "",
            "The section below adds troubleshooting, examples, and extra detail beyond the slides.",
            "",
            reference,
            "",
        ])

    lines.extend([
        "---",
        "",
        "## Troubleshooting (common beginner issues)",
        "",
        "| Problem | What to try |",
        "|---------|-------------|",
        "| Agent panel won't open | Click inside Cursor first; try `Ctrl+Shift+P` → **Open Agent** |",
        "| No diff appears | Switch from Ask Mode to **Agent Mode** in the panel footer |",
        "| Agent can't see my files | **File → Open Folder** (not a single file) |",
        "| Terminal command fails on Windows | Use **PowerShell**; use `curl.exe` instead of `curl` |",
        "| API returns 401 | Re-copy API key; check `Authorization: Bearer` header |",
        "| API returns 429 | Wait and retry; see Exercise 7.3 for backoff |",
        "",
        "---",
        "",
        "## Exercise complete",
        "",
        "- [ ] Finished all steps above",
        "- [ ] Checked success criteria",
        "- [ ] Noted one thing you would do differently on a real project",
        "",
    ])

    return "\n".join(lines)


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    count = 0
    for (module_num, ex_num), meta in sorted(EXERCISE_META.items()):
        grouped = extract_exercise_slides(module_num)
        slide_chunks = grouped.get(ex_num, [])
        doc = build_document(module_num, ex_num, meta, slide_chunks)
        module_dir = OUT / f"module-{module_num:02d}"
        module_dir.mkdir(parents=True, exist_ok=True)
        filename = f"exercise-{module_num}.{ex_num}-{slugify(meta['title'])}.md"
        out_path = module_dir / filename
        out_path.write_text(doc, encoding="utf-8", newline="\n")
        print(f"Wrote {out_path.relative_to(REPO)}")
        count += 1
    print(f"Done. {count} exercise guide(s) in slide-exercises/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

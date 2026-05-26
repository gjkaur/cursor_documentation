"""Teaching enrichment for instructor speaker scripts — beyond slide text."""

from __future__ import annotations

import re
from dataclasses import dataclass

# (regex on heading + optional kind filter) -> extra instructor paragraphs
ENRICHMENT_RULES: list[tuple[str, str | None, list[str]]] = [
    (
        r"how ai models work",
        "lesson_intro",
        [
            "This lesson installs the engine-under-the-hood mental model — no Cursor shortcuts yet. "
            "Participants should leave understanding why the same prompt can produce different code.",
            "Connect forward: Module 2 failures often trace back to treating the Agent like a deterministic compiler.",
        ],
    ),
    (
        r"why outputs are probabilistic",
        "quote",
        [
            "Open with a concrete contrast: run the same unit test twice — same result every time. "
            "Run the same prompt twice in ChatGPT or Cursor — you may get different wording, structure, or even logic.",
            "The mental model to install today: LLMs do not execute a stored program. They roll weighted dice for the next token, "
            "millions of times per answer. That is why we never ship the first output without review.",
            "Ask the room: where has non-determinism already burned you — flaky tests, or flaky AI summaries?",
        ],
    ),
    (
        r"next-token prediction",
        "diagram",
        [
            "Use the diagram to demystify the magic. Each step is not 'understanding' in the human sense — it is picking "
            "the most likely next piece of text given everything so far.",
            "Analogy: autocomplete on your phone, extended for pages of code. The model does not re-read your intent; "
            "it extends the pattern.",
            "If someone asks 'but it feels intelligent' — agree, then redirect: pattern completion at scale can look like reasoning, "
            "but the mechanism is still probabilistic completion.",
        ],
    ),
    (
        r"traditional code vs",
        "table",
        [
            "Do not read the table row by row. Frame it as a mindset shift: yesterday you debugged logic; with AI you debug inputs — "
            "prompt, context, model, and parameters.",
            "The row about errors being 'features of probability' lands hard — give an example: a confident wrong import "
            "is not a bug in your repo; it is the model filling a gap.",
        ],
    ),
    (
        r"implication.*ground truth",
        None,
        [
            "This one line is worth repeating later in the course: always verify — run the code, read the diff, check the docs.",
            "Teams that skip this step accumulate 'AI debt' — code that looks fine in chat but fails in CI.",
        ],
    ),
    (
        r"what determines ai output|factors.*output",
        "diagram",
        [
            "When a participant says 'the model got worse today,' walk this diagram mentally: did the model change, "
            "or did the context shrink, the prompt get vaguer, or the temperature rise?",
            "Practical tip: before blaming the model, diff your prompt and attached files against yesterday's session.",
        ],
    ),
    (
        r"key parameters",
        "table",
        [
            "Developers rarely tune these directly in Cursor day to day, but admins and API users do. "
            "Knowing they exist explains why two teammates get different styles from the 'same' prompt.",
            "Rule of thumb for coding: lower temperature when fixing bugs; slightly higher when exploring design alternatives — "
            "then turn it back down before merging.",
        ],
    ),
    (
        r"temperature impact",
        "code",
        [
            "Run this verbally if you have time: same ask, three temperatures. Point out that high temperature did not "
            "get 'more creative' — it got less predictable, which is not always desirable in production code.",
        ],
    ),
    (
        r"training gap",
        None,
        [
            "This slide prevents the most expensive misconception: 'the model should know our internal API.' "
            "It will not unless you put it in context — paste docs, open files, or add rules.",
            "Story beat: a team once debugged for an hour because the model used a deprecated SDK — the fix was "
            "attaching the current internal README, not switching models.",
        ],
    ),
    (
        r"what are hallucinations",
        "quote",
        [
            "Emphasize confidence: the model's tone is not calibrated to truth. A wrong answer can sound like a senior engineer.",
            "In code review, treat AI output like a junior's first PR — polite, thorough review required.",
        ],
    ),
    (
        r"hallucinations in code",
        "table",
        [
            "Walk one row deeply — fake APIs are the most common in this room. Mention that Python's import error is your friend; "
            "TypeScript often catches invented methods faster than runtime.",
            "Encourage a team norm: if the Agent cites a library method, one person verifies in official docs before merge.",
        ],
    ),
    (
        r"hallucination mitigation",
        "table",
        [
            "Grounding and verification are the habits to take home. Rules and @mentions are how Cursor makes grounding automatic.",
            "Ask: which strategy could your team adopt Monday — paste docs, require citations, or JSON-only outputs?",
        ],
    ),
    (
        r"what is a token|tokens and pricing",
        None,
        [
            "Tokens are how vendors meter and limit context — not characters, not lines. Rough guide: 100 tokens ≈ 75 words of English.",
            "Why instructors cover this: without token awareness, people attach entire repos and wonder why answers degrade or bills spike.",
        ],
    ),
    (
        r"cost optimization|cost calculation",
        None,
        [
            "Connect to business reality: a daily standup prompt is cheap; an agent loop over 200 files is not.",
            "Teach bounded tasks: narrow @mentions, clear stop conditions, and checkpoints before long agent runs.",
        ],
    ),
    (
        r"lost in the middle",
        None,
        [
            "Research finding: models attend strongly to the start and end of context, weaker in the middle. "
            "Put critical constraints at the top of the prompt and repeat them after long pasted logs.",
        ],
    ),
    (
        r"context prioritization pyramid|context pyramid",
        "diagram",
        [
            "Use this when teaching @mentions in Module 2: pointing at three files beats pasting ten files 'just in case.'",
            "The pyramid is a prioritization exercise — what must the model see versus what is nice to have?",
        ],
    ),
    (
        r"what is tool calling|tool calling",
        None,
        [
            "Tool calling is how the model stops guessing and starts acting — read file, run terminal, fetch URL.",
            "Contrast with plain chat: chat only produces text; tools close the loop with real environment feedback.",
        ],
    ),
    (
        r"\bmcp\b|model context protocol",
        None,
        [
            "MCP is plumbing: one standard way to plug databases, browsers, and internal services into Cursor without "
            "custom hacks per vendor.",
            "You will see MCP again in team customization — rules tell the model how to behave; MCP gives it new hands.",
        ],
    ),
    (
        r"agent loop",
        "diagram",
        [
            "Narrate one full cycle slowly: user goal → model plans → tool runs → output returns → model continues.",
            "Safety hook: each cycle is a chance to stop — checkpoints and diff review exist because loops can run far.",
        ],
    ),
    (
        r"agent vs\. chatbot|levels of agent",
        None,
        [
            "Chatbots answer questions; agents pursue outcomes across multiple steps. That difference drives cost, risk, and review burden.",
            "Ask the room where they are today — mostly chat, or already letting the agent edit and run commands?",
        ],
    ),
    (
        r"problem.*solution|codebase understanding",
        "quote",
        [
            "This is the emotional hook for Module 2: onboarding panic is normal. The Agent is a tour guide, not a replacement for reading code.",
            "Set expectation: the first answer will be imperfect — the skill is follow-up prompts that narrow and verify.",
        ],
    ),
    (
        r"ask mode vs|ask mode",
        None,
        [
            "Ask Mode is your safe inspection lane — architecture questions, code reading, no surprise diffs.",
            "Demo the footer toggle live: same question in Ask vs Agent and show that only Agent proposes edits.",
        ],
    ),
    (
        r"browser tool",
        None,
        [
            "Frontend developers love this — CSS lies, the rendered page does not. The Agent can see what users see.",
            "Caveat: dynamic SPAs may need wait instructions; mention that if the page looks empty in the demo.",
        ],
    ),
    (
        r"terminal tool",
        None,
        [
            "This closes the loop: tests and builds become ground truth. The Agent should read stderr, not invent success.",
            "Windows note: prefer `.\run_tests.bat` and `curl.exe` — say that once, not every slide.",
        ],
    ),
    (
        r"effective prompting",
        None,
        [
            "The through-line: vague prompts produce vague, wide diffs. Constraints — files, functions, output format — shrink the blast radius.",
            "Exercise 3.4 on calculator.c is deliberately small so you can see how one vague sentence refactors half the file.",
        ],
    ),
    (
        r"plan mode",
        None,
        [
            "Plan Mode buys review time before files change — use it for multi-file refactors and unfamiliar code.",
            "Compare to jumping straight to Agent: plans are cheaper to throw away than bad diffs.",
        ],
    ),
    (
        r"comparing two models",
        None,
        [
            "Same prompt, two models — compare correctness first, speed second, cost third. Fancy answers that fail tests lose.",
            "Encourage documenting 'default model per task' for the team after this exercise.",
        ],
    ),
    (
        r"checkpoint",
        None,
        [
            "Checkpoints are undo for agent experiments — use before risky prompts or broad @folder mentions.",
            "Analogy: git stash for conversation state when you want to explore without fear.",
        ],
    ),
    (
        r"creating a rule|repository instructions|skill",
        None,
        [
            "Team leverage slide: rules and AGENTS.md scale your standards without repeating them in every prompt.",
            "Who owns these on a real team? Usually tech lead or platform — not every developer inventing their own.",
        ],
    ),
    (
        r"cloud agent|cloud handoff",
        None,
        [
            "Cloud Agents run where your laptop is closed — long tasks, CI handoffs, parallel work.",
            "Trust boundary: they need repo access and clear task descriptions — same review discipline when the PR returns.",
        ],
    ),
    (
        r"api key|rate limit|etag|webhook",
        None,
        [
            "Production API work is boring on purpose: auth, retries, caching, verified signatures.",
            "Windows labs use `$env:VAR` and `curl.exe` — if a command fails, check quoting before re-generating the key.",
        ],
    ),
    (
        r"quick reference",
        "quick_reference",
        [
            "This slide is a takeaway — photograph it or copy into your runbook. It is not meant to be taught line by line now.",
        ],
    ),
]

MODULE_FRAMING: dict[int, list[str]] = {
    1: [
        "Module 1 is deliberately conceptual — no Cursor setup required. We are building shared vocabulary so Module 2 "
        "hands-on work makes sense instead of feeling like magic.",
        "If anyone feels impatient for 'real Cursor tips,' tell them the probabilistic mindset prevents the worst "
        "production mistakes later.",
    ],
    2: [
        "Module 2 is the longest hands-on block today. Laptops open, repo loaded, Agent panel ready — Ctrl+I on Windows.",
        "Success here is not memorizing shortcuts; it is comfort with orientation, safe diffs, and knowing when to stop the Agent.",
    ],
    3: [
        "Module 3 connects modes and tools to the mental models from Module 1 — Ask vs Agent, browser, terminal, prompting craft.",
    ],
    4: [
        "Module 4 is about scaling Cursor across a team — rules travel with the repo, skills encode repeat workflows.",
    ],
    5: [
        "Module 5 moves automation to the terminal — same agent brain, different interface for scripts and CI.",
    ],
    6: [
        "Module 6 introduces Cloud Agents in the product UI — watch runs, artifacts, and handoffs from local work.",
    ],
    7: [
        "Module 7 is API foundations — keys, errors, caching. Boring infrastructure that keeps integrations alive in production.",
    ],
    8: [
        "Module 8 wires Cloud Agents programmatically — create runs, stream events, verify webhooks.",
    ],
    9: [
        "Module 9 is admin analytics — who uses Cursor, spend, models. Enterprise audience; pair if someone lacks admin keys.",
    ],
    10: [
        "Module 10 closes with AI code tracking — measuring adoption and change, not just vibes.",
    ],
}

EXERCISE_STEP_GUIDANCE: dict[tuple[int, int], dict[str, list[str]]] = {
    (2, 1): {
        "setup": [
            "For this exercise, any unfamiliar repo works — detectron2 is large on purpose; smaller repos are fine if time is tight.",
            "Verify File → Open Folder, not a single file — the Agent needs the tree to orient.",
        ],
        "orientation": [
            "A strong answer names entry points and a reading order, not a file dump. If the Agent lists fifty files, "
            "follow up: 'Which three should I read first?'",
            "Debrief question: what did the Agent get wrong about dependencies or architecture?",
        ],
        "trace": [
            "Follow-up prompts are the skill — the first answer is a map; this step tests whether the Agent can chain calls logically.",
            "If the trace is wrong, ask the Agent to cite file:line for each hop — cheap verification habit.",
        ],
        "visual": [
            "ASCII diagrams are good enough for onboarding docs — the point is communicating structure, not pretty graphics.",
        ],
        "success": [
            "Close by comparing two groups: who trusted the first answer blindly vs who verified one claim in the repo?",
        ],
    },
    (2, 3): {
        "default": [
            "This exercise trains review discipline — the change is tiny on purpose. If someone accepts without reading the diff, "
            "stop and redo the step.",
        ],
    },
    (3, 3): {
        "default": [
            "Break the test on purpose if the lab says so — the Agent should read failing output, not guess.",
            "If tests pass immediately, ask what command the Agent ran and whether output matched stderr/stdout.",
        ],
    },
    (3, 4): {
        "default": [
            "Step 2's vague prompt is the lesson — expect a wide diff. Step 1's constrained prompt should touch only divide().",
            "Use @calculator.c every time; without it the Agent may edit the wrong file.",
        ],
    },
    (7, 2): {
        "default": [
            "Admin keys and User keys are not interchangeable — 401 often means wrong key type, not a bad copy-paste.",
            "First success is a 200 with expected JSON — celebrate that before moving to harder exercises.",
        ],
    },
}

ENGAGEMENT_BY_KIND: dict[str, list[str]] = {
    "quote": ["Pause after the quote — let it land before you add examples."],
    "table": ["Pick one row that matches your audience's stack and go deep; skim the rest."],
    "diagram": ["Trace the diagram once with your finger or cursor — motion helps retention."],
    "bullets": ["Ask who has seen the opposite problem in production — one story beats five bullets."],
    "exercise": ["Circulate during work time; rescue stuck pairs with a narrower prompt, not by doing it for them."],
}


@dataclass
class EnrichmentMatch:
    paragraphs: list[str]
    engagement: list[str]


def match_enrichment(heading: str, kind: str, module: int | None) -> EnrichmentMatch:
    h = heading.lower()
    paragraphs: list[str] = []
    engagement: list[str] = list(ENGAGEMENT_BY_KIND.get(kind, []))

    for pattern, kind_filter, tips in ENRICHMENT_RULES:
        if kind_filter and kind_filter != kind:
            continue
        if re.search(pattern, h, re.I):
            paragraphs.extend(tips)

    if module and module in MODULE_FRAMING and kind == "module_intro":
        paragraphs = MODULE_FRAMING[module] + paragraphs

    # Deduplicate while preserving order
    seen: set[str] = set()
    unique: list[str] = []
    for p in paragraphs:
        if p not in seen:
            seen.add(p)
            unique.append(p)

    return EnrichmentMatch(paragraphs=unique[:4], engagement=engagement[:2])


def exercise_step_hints(module: int, ex_num: int, heading: str, *, first_step: bool = False) -> list[str]:
    hints_map = EXERCISE_STEP_GUIDANCE.get((module, ex_num), {})
    h = heading.lower()
    if first_step:
        setup = hints_map.get("setup", [])
        if setup:
            return setup
    for key, hints in hints_map.items():
        if key == "default":
            continue
        if key in h:
            return hints
    return hints_map.get("default", [])

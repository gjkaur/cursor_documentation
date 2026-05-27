"""Speakable instructor scripts keyed by slide topic — read aloud to the room."""

from __future__ import annotations

import re
from dataclasses import dataclass

# (regex on heading, optional kind filter) -> paragraphs to read aloud
ENRICHMENT_RULES: list[tuple[str, str | None, list[str]]] = [
    (
        r"how ai models work",
        "lesson_intro",
        [
            "In this lesson we look under the hood at how large language models actually produce text. "
            "You won't need Cursor open yet — just listen and connect this to the Agent behavior you'll see all day tomorrow.",
            "The key takeaway is this: the same prompt can produce different code on different runs. "
            "That is normal, not a broken tool.",
        ],
    ),
    (
        r"why outputs are probabilistic",
        "quote",
        [
            "Run the same unit test twice and you get the same result every time. "
            "Run the same prompt in Cursor twice and you may get different wording, structure, or even logic.",
            "An LLM is not executing a program you wrote. It predicts the next token, samples one, appends it, and repeats — "
            "millions of times per answer. That is why we never treat a single Agent run as final without review.",
            "Has anyone been burned by that — a summary that changed overnight, or code that worked once and not the second time?",
        ],
    ),
    (
        r"next-token prediction",
        "diagram",
        [
            "Look at the diagram. The model reads everything so far, ranks possible next tokens by probability, "
            "picks one, appends it, and runs the loop again. That is the entire answer — autocomplete at scale.",
            "It can feel like reasoning, but the mechanism is still pattern completion. "
            "Keeping that in mind will save you hours of false expectations later today.",
        ],
    ),
    (
        r"traditional code vs",
        "table",
        [
            "Traditional software is deterministic — same input, same output. You own every branch and bug fix.",
            "AI models are probabilistic — you influence them through prompts, context, and settings, but you do not fully control them.",
            "When the model invents a wrong import, that is not a bug in your repo the way a null pointer is — "
            "it is the model filling a gap. You manage that with review, grounding, and constraints — not only more prompts.",
        ],
    ),
    (
        r"implication",
        None,
        [
            "The practical rule is on the slide: never trust a single run as ground truth. "
            "Run the code, read the diff, check the docs — every time.",
            "Teams that skip verification accumulate AI debt — code that looked fine in chat but fails in CI.",
        ],
    ),
    (
        r"implication.*ground truth",
        None,
        [
            "The practical rule is on the slide: never trust a single run as ground truth. "
            "Run the code, read the diff, check the docs — every time.",
        ],
    ),
    (
        r"what determines ai output|factors.*output",
        "diagram",
        [
            "When output quality drops, walk through these inputs: your prompt, system instructions, open files, "
            "model choice, and parameters like temperature. One of them changed — not necessarily the model itself.",
            "Before you switch models, compare today's prompt and attachments to yesterday's session. "
            "That diff often explains the regression.",
        ],
    ),
    (
        r"key parameters",
        "table",
        [
            "Temperature controls randomness — keep it low for bug fixes, slightly higher for brainstorming, then back down before you merge.",
            "Top-p and max tokens shape breadth and length. Two teammates with the same prompt can still differ if their settings differ.",
        ],
    ),
    (
        r"temperature impact",
        "code",
        [
            "Same ask, three temperatures on the slide. Notice low temperature stays close to the obvious solution; "
            "high temperature adds variation — and sometimes instability you do not want in production code.",
        ],
    ),
    (
        r"training gap",
        None,
        [
            "Models are frozen at a training cutoff. They do not automatically know your internal APIs, "
            "your architecture decisions, or libraries released last month unless you put that information in context.",
            "If the Agent guesses wrong about your stack, the fix is usually better context — not a different model.",
        ],
    ),
    (
        r"what are hallucinations",
        "quote",
        [
            "A hallucination is a confident answer that is wrong — a library that does not exist, a method that was never in the API, "
            "outdated syntax presented as current best practice.",
            "The danger is the tone: the model sounds as sure as a senior engineer in a code review.",
        ],
    ),
    (
        r"hallucinations in code",
        "table",
        [
            "Fake imports and invented methods show up constantly. Your fastest checks are: does it import, does the type checker agree, "
            "does the official doc mention this API?",
            "Build a team habit: if the Agent cites an API, someone verifies it before merge.",
        ],
    ),
    (
        r"hallucination mitigation",
        "table",
        [
            "Ground the model with docs and @mentions. Ask it to cite sources. Use structured outputs when you need predictable shape.",
            "Which of these can your team adopt Monday — paste docs, require citations, or JSON-only responses for scripts?",
        ],
    ),
    (
        r"what is a token|tokens and pricing",
        None,
        [
            "Tokens are how models meter context and cost — roughly three quarters of a word in English.",
            "Small chat prompts are cheap; agent loops over large repos are not. Narrow context saves money and often improves quality.",
        ],
    ),
    (
        r"cost optimization|cost calculation",
        None,
        [
            "Bound your tasks: specific @mentions, clear stop conditions, checkpoints before long agent runs.",
            "A five-minute agent loop on two files beats a twenty-minute loop on the whole tree.",
        ],
    ),
    (
        r"lost in the middle",
        None,
        [
            "Models attend strongly to the beginning and end of context and weaker to the middle. "
            "Put critical constraints at the top of your prompt and repeat them after large pasted logs.",
        ],
    ),
    (
        r"context prioritization pyramid|context pyramid",
        "diagram",
        [
            "Not all context is equal. Recent messages, open files, and rules compete for the same token budget. "
            "Three precise @mentions beat ten files attached just in case.",
        ],
    ),
    (
        r"what is tool calling|tool calling",
        None,
        [
            "Tool calling is how the model stops guessing and starts acting — read a file, run a terminal command, fetch a URL.",
            "Plain chat only produces text. Tools close the loop with real feedback from your environment.",
        ],
    ),
    (
        r"\bmcp\b|model context protocol",
        None,
        [
            "MCP is standard plumbing for connecting Cursor to databases, browsers, and internal services — "
            "one protocol instead of a custom integration per tool.",
        ],
    ),
    (
        r"agent loop",
        "diagram",
        [
            "Follow the loop on the slide: you state a goal, the model plans, Cursor runs a tool, results return, and the cycle repeats "
            "until the task finishes or you stop it. Each cycle is a chance to review before more changes land.",
        ],
    ),
    (
        r"agent vs\. chatbot|levels of agent",
        None,
        [
            "Chatbots answer questions. Agents pursue outcomes across multiple steps — edits, commands, follow-ups.",
            "That difference drives cost, risk, and how carefully you review each step.",
        ],
    ),
    (
        r"problem.*solution|codebase understanding",
        "quote",
        [
            "Every one of us has opened a repo and wondered where to start. The Agent can produce a roadmap in minutes — "
            "but the first answer is a draft, not gospel. Your job is to verify and follow up.",
        ],
    ),
    (
        r"ask mode vs|ask mode",
        None,
        [
            "Ask Mode is read-only — great for architecture questions and understanding code without surprise diffs.",
            "Agent Mode can edit files. Same question, different risk profile. Watch the mode indicator in the panel footer before you send.",
        ],
    ),
    (
        r"browser tool",
        None,
        [
            "The Browser tool lets the Agent see what users see — rendered pages, console errors, layout issues CSS alone won't reveal.",
        ],
    ),
    (
        r"terminal tool",
        None,
        [
            "The Terminal tool lets the Agent run tests and builds and read real output. "
            "That is how we turn guesses into evidence.",
        ],
    ),
    (
        r"effective prompting",
        None,
        [
            "Vague prompts produce wide diffs. Constraints — which file, which function, what format — shrink the blast radius.",
            "In the next exercise we use calculator.c on purpose: you will see one vague sentence refactor half the file.",
        ],
    ),
    (
        r"plan mode",
        None,
        [
            "Plan Mode shows you the design before files change. Use it for multi-file work and unfamiliar codebases — "
            "plans are cheaper to throw away than bad diffs.",
        ],
    ),
    (
        r"comparing two models",
        None,
        [
            "Run the same prompt on two models. Judge correctness first, then speed, then cost. "
            "The prettiest answer that fails tests loses.",
        ],
    ),
    (
        r"checkpoint",
        None,
        [
            "Checkpoints are undo for agent experiments — create one before risky prompts or broad @folder mentions.",
        ],
    ),
    (
        r"creating a rule|repository instructions|skill",
        None,
        [
            "Rules and AGENTS.md travel with the repo so the whole team gets the same standards without repeating them in every prompt.",
        ],
    ),
    (
        r"cloud agent|cloud handoff",
        None,
        [
            "Cloud Agents keep working when your laptop is closed — long tasks, parallel runs, handoffs from local sessions.",
            "When the PR comes back, the same review discipline applies.",
        ],
    ),
    (
        r"api key|rate limit|etag|webhook",
        None,
        [
            "Production API work comes down to auth, retries, caching, and verified webhooks. "
            "On Windows we use environment variables and curl.exe — details are in the lab steps on screen.",
        ],
    ),
]

MODULE_FRAMING: dict[int, list[str]] = {
    1: [
        "Welcome to Module 1. This block is about sixty minutes of concepts — keep Cursor closed for now.",
        "We are building vocabulary so tomorrow's hands-on work feels predictable instead of magical.",
    ],
    2: [
        "Module 2 is our longest hands-on block. Open Cursor now, load your repo with File → Open Folder, "
        "and keep the Agent panel ready — Ctrl+I on Windows.",
    ],
    3: [
        "Module 3 connects Ask Mode, Agent Mode, the browser, the terminal, and prompting craft "
        "to the mental models from Module 1.",
    ],
    4: [
        "Module 4 is about scaling Cursor for your team — rules, repository instructions, and reusable skills.",
    ],
    5: [
        "Module 5 moves the same agent to the terminal and to scripts you can automate.",
    ],
    6: [
        "Module 6 introduces Cloud Agents in the Cursor UI — launching runs, tracking progress, and collecting artifacts.",
    ],
    7: [
        "Module 7 covers API foundations — keys, errors, and caching — the infrastructure that keeps integrations running.",
    ],
    8: [
        "Module 8 wires Cloud Agents programmatically: create runs, stream events, and verify webhooks.",
    ],
    9: [
        "Module 9 is admin and analytics — usage, spend, and models across your organization.",
    ],
    10: [
        "Module 10 closes with AI code tracking — measuring adoption and change in your codebase.",
    ],
}

EXERCISE_STEP_SPEECH: dict[tuple[int, int], dict[str, list[str]]] = {
    (2, 1): {
        "setup": [
            "Any unfamiliar repository works here — detectron2 is on the slide, but a smaller repo is fine if we are short on time.",
            "Use File → Open Folder, not a single file, so the Agent can see the project tree.",
        ],
        "orientation": [
            "You want a reading order and named entry points — not a flat list of every filename.",
            "If the Agent dumps dozens of files, reply in chat: which three should I read first?",
            "When we debrief, I will ask what the Agent got wrong about dependencies or architecture.",
        ],
        "trace": [
            "The first answer was a map; this follow-up tests whether the Agent can chain function calls logically.",
            "If the trace looks wrong, ask it to cite file and line for each hop — that is a verification habit worth keeping.",
        ],
        "visual": [
            "An ASCII diagram is enough for onboarding — we care about communicating structure, not graphic design.",
        ],
        "success": [
            "Who completed all three parts? What did the Agent get wrong, and what prompt change fixed it?",
        ],
    },
    (2, 3): {
        "default": [
            "The change is tiny on purpose — read every line of the diff before you click Accept. "
            "If you accepted without reading, undo and do it again; that is the exercise.",
        ],
    },
    (3, 3): {
        "default": [
            "If the lab asked you to break a test, the Agent should read the failing output — not guess the fix.",
        ],
    },
    (3, 4): {
        "default": [
            "Step two's vague prompt may refactor more than divide() — that is the lesson.",
            "Keep @calculator.c in every prompt so the Agent stays in the right file.",
        ],
    },
    (7, 2): {
        "default": [
            "A 401 usually means the wrong key type — Admin versus User — not a bad copy-paste.",
            "Once you see a 200 with the expected JSON, you are ready for the rest of today's API labs.",
        ],
    },
}


@dataclass
class EnrichmentMatch:
    paragraphs: list[str]


def match_enrichment(heading: str, kind: str, module: int | None) -> EnrichmentMatch:
    h = heading.lower()
    paragraphs: list[str] = []

    for pattern, kind_filter, tips in ENRICHMENT_RULES:
        if kind_filter and kind_filter != kind:
            continue
        if re.search(pattern, h, re.I):
            paragraphs.extend(tips)

    if module and module in MODULE_FRAMING and kind == "module_intro":
        paragraphs = MODULE_FRAMING[module] + paragraphs

    seen: set[str] = set()
    unique: list[str] = []
    for p in paragraphs:
        if p not in seen:
            seen.add(p)
            unique.append(p)

    return EnrichmentMatch(paragraphs=unique[:4])


def exercise_step_speech(module: int, ex_num: int, heading: str, *, first_step: bool = False) -> list[str]:
    speech_map = EXERCISE_STEP_SPEECH.get((module, ex_num), {})
    h = heading.lower()
    if first_step:
        setup = speech_map.get("setup", [])
        if setup:
            return setup
    for key, lines in speech_map.items():
        if key == "default":
            continue
        if key in h:
            return lines
    return speech_map.get("default", [])

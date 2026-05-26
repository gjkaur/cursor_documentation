"""Expand acronyms and define technical terms for read-aloud speaker notes."""

from __future__ import annotations

import re
from dataclasses import dataclass

from marp_tables import extract_fenced_code_blocks


@dataclass(frozen=True)
class GlossaryEntry:
    key: str
    speech: str
    full_form: str | None = None
    aliases: tuple[str, ...] = ()


def _entries() -> list[GlossaryEntry]:
    """Course glossary — longest phrases should sort before shorter substrings."""
    raw: list[tuple[str, str, str | None, tuple[str, ...]]] = [
        # --- Acronyms (full form + meaning) ---
        ("LLM", "LLM stands for Large Language Model — a neural network trained to generate text one token at a time.", "Large Language Model", ()),
        ("MCP", "MCP stands for Model Context Protocol — a standard for connecting AI assistants to external tools, databases, and APIs.", "Model Context Protocol", ()),
        ("API", "API stands for Application Programming Interface — a defined way for programs to request data or actions from another service.", "Application Programming Interface", ()),
        ("SSE", "SSE stands for Server-Sent Events — a way the server pushes live updates over one long HTTP connection.", "Server-Sent Events", ()),
        ("ETag", "ETag stands for Entity Tag — a version fingerprint the server returns so clients can ask whether data changed.", "Entity Tag", ()),
        ("HMAC", "HMAC stands for Hash-based Message Authentication Code — a signed digest that proves a webhook payload was not tampered with.", "Hash-based Message Authentication Code", ("HMAC-SHA256",)),
        ("SHA-256", "SHA-256 is the Secure Hash Algorithm with a 256-bit digest — commonly used for webhook signature verification.", "Secure Hash Algorithm 256-bit", ()),
        ("JWT", "JWT stands for JSON Web Token — a compact, signed token format often used for authentication.", "JSON Web Token", ()),
        ("CLI", "CLI stands for Command-Line Interface — running Cursor or other tools from a terminal instead of the graphical editor.", "Command-Line Interface", ()),
        ("DAU", "DAU stands for Daily Active Users — the count of distinct people who used the product on a given day.", "Daily Active Users", ()),
        ("CI/CD", "CI/CD stands for Continuous Integration and Continuous Deployment — automated build, test, and release pipelines.", "Continuous Integration / Continuous Deployment", ()),
        ("SDK", "SDK stands for Software Development Kit — a library and helpers for calling an API from your language of choice.", "Software Development Kit", ()),
        ("HTTP", "HTTP stands for Hypertext Transfer Protocol — the request/response protocol browsers and APIs use.", "Hypertext Transfer Protocol", ()),
        ("HTTPS", "HTTPS is HTTP secured with TLS encryption — required for production APIs and webhooks.", "Hypertext Transfer Protocol Secure", ()),
        ("REST", "REST stands for Representational State Transfer — a style of HTTP APIs built around resources and standard verbs like GET and POST.", "Representational State Transfer", ()),
        ("JSON", "JSON stands for JavaScript Object Notation — a text format for structured data that APIs commonly return.", "JavaScript Object Notation", ()),
        ("YAML", "YAML stands for YAML Ain't Markup Language — a human-readable config format used in many DevOps tools.", "YAML Ain't Markup Language", ()),
        ("CSV", "CSV stands for Comma-Separated Values — a simple tabular export format spreadsheets and BI tools can ingest.", "Comma-Separated Values", ()),
        ("URL", "URL stands for Uniform Resource Locator — the web address you paste into a browser or API client.", "Uniform Resource Locator", ()),
        ("URI", "URI stands for Uniform Resource Identifier — a broader name for URLs and similar identifiers.", "Uniform Resource Identifier", ()),
        ("IDE", "IDE stands for Integrated Development Environment — an editor like Cursor that combines code, terminal, and tooling.", "Integrated Development Environment", ()),
        ("PR", "PR stands for Pull Request — a proposed code change others review before it merges.", "Pull Request", ()),
        ("OAuth", "OAuth stands for Open Authorization — a standard for delegated login without sharing passwords.", "Open Authorization", ()),
        ("DOM", "DOM stands for Document Object Model — the live tree structure of elements on a web page.", "Document Object Model", ()),
        ("CSRF", "CSRF stands for Cross-Site Request Forgery — an attack where a malicious site triggers actions in another site you are logged into.", "Cross-Site Request Forgery", ()),
        ("SQL", "SQL stands for Structured Query Language — the language relational databases use for queries and updates.", "Structured Query Language", ()),
        ("WSL", "WSL stands for Windows Subsystem for Linux — a way to run Linux tools on Windows.", "Windows Subsystem for Linux", ()),
        ("OpenAPI", "OpenAPI is the Open API Specification — a machine-readable description of REST endpoints.", "Open API Specification", ()),
        ("BI", "BI stands for Business Intelligence — dashboards and reports built from exported usage data.", "Business Intelligence", ()),
        ("ROI", "ROI stands for Return on Investment — whether tool spend pays back in saved time or shipped work.", "Return on Investment", ()),
        ("GDPR", "GDPR is the General Data Protection Regulation — European privacy rules that affect how you store user data.", "General Data Protection Regulation", ()),
        ("SOC2", "SOC2 is Service Organization Control 2 — a common security and compliance audit framework for SaaS vendors.", "Service Organization Control 2", ()),
        ("ISO", "ISO refers to International Organization for Standardization frameworks — audit and compliance standards many enterprises require.", "International Organization for Standardization", ()),
        ("WoW", "WoW stands for Week over Week — comparing this week's metric to last week's.", "Week over Week", ()),
        ("npm", "npm is the Node Package Manager — the default registry and tool for JavaScript packages.", "Node Package Manager", ()),
        # --- Product / mode names (not always acronyms) ---
        ("Agent", "In Cursor, the Agent is the AI assistant that can use tools, edit files, and run terminal commands — not just answer questions in chat.", None, ()),
        ("Cloud Agent", "A Cloud Agent is a Cursor agent that runs on Cursor's infrastructure against a GitHub repository — you can launch it from the web UI or API.", None, ()),
        ("Ask Mode", "Ask Mode is Cursor's read-only mode — the model can answer questions but cannot edit files or run tools.", None, ()),
        ("Agent Mode", "Agent Mode lets Cursor edit files, run terminal commands, and use tools — always with your review before changes land.", None, ()),
        ("Plan Mode", "Plan Mode makes the agent draft a step-by-step plan and ask clarifying questions before it writes code — toggle with Shift+Tab.", None, ()),
        ("Composer 2.5", "Composer 2.5 is Cursor's agent-optimized model — tuned for multi-step coding tasks and tool use inside the editor.", None, ("Composer 2",)),
        # --- Technical concepts ---
        ("next-token prediction", "Next-token prediction means the model reads everything so far, ranks likely next pieces of text, picks one, appends it, and repeats.", None, ()),
        ("probabilistic", "Probabilistic means the same input can produce different outputs — unlike traditional code that always returns the same result.", None, ()),
        ("deterministic", "Deterministic means the same input always produces the same output — how conventional software behaves.", None, ()),
        ("hallucination", "A hallucination is a confident answer that is wrong — for example an API or library that does not exist.", None, ("hallucinations",)),
        ("grounding", "Grounding means giving the model source material — files, docs, or URLs — so answers stay tied to facts instead of guesses.", None, ()),
        ("training cutoff", "Training cutoff is the date the model's knowledge was frozen — it will not know about releases after that unless you add context.", None, ()),
        ("context window", "Context window is the maximum amount of text the model can consider at once — when you exceed it, older content drops off.", None, ()),
        ("token", "A token is the billing and processing unit for LLMs — smaller than a sentence, often a word fragment or symbol.", None, ("tokens",)),
        ("input token", "Input tokens are the prompt, attached files, and instructions you send — they usually cost less than generated output.", None, ("input tokens",)),
        ("output token", "Output tokens are the text the model generates — explanations and code — and they typically cost more than input.", None, ("output tokens",)),
        ("temperature", "Temperature controls randomness — low values stay focused and repeatable; high values add creativity and variation.", None, ()),
        ("Top-p", "Top-p, also called nucleus sampling, limits the pool of tokens the model may choose from on each step.", None, ("top-p", "Top p")),
        ("max tokens", "Max tokens caps how long the model's answer can be — useful for controlling cost and verbosity.", None, ("Max Tokens",)),
        ("tool calling", "Tool calling means the model requests an action — read a file, run a command — and the host executes it; the model does not run code itself.", None, ("function calling", "Tool Calling")),
        ("agent loop", "The agent loop is plan, act with tools, observe results, and repeat until the task is done or you stop it.", None, ()),
        ("Cloud handoff", "Cloud handoff is when you prefix a message with ampersand in the CLI to continue the work as a Cloud Agent.", None, ()),
        ("webhook", "A webhook is an HTTP callback — when an event happens, the service POSTs a payload to your URL.", None, ("webhooks",)),
        ("presigned URL", "A presigned URL is a time-limited download link — common for Cloud Agent artifacts that expire after a short window.", None, ("presigned url",)),
        ("rate limit", "A rate limit caps how many API requests you can make in a time window — exceed it and you get HTTP 429.", None, ("rate limits",)),
        ("exponential backoff", "Exponential backoff means waiting longer after each failed retry — standard practice when APIs return 429 or 5xx errors.", None, ()),
        ("ETag caching", "ETag caching sends If-None-Match on repeat requests — if nothing changed, the server returns 304 and you skip re-downloading the body.", None, ()),
        ("If-None-Match", "If-None-Match is an HTTP header carrying your cached ETag — the server uses it to decide whether data changed.", None, ()),
        ("304 Not Modified", "HTTP 304 Not Modified means your cached copy is still current — no response body, so you save bandwidth and time.", None, ("304",)),
        ("streaming", "Streaming means events arrive incrementally over SSE instead of waiting for one complete response at the end.", None, ()),
        ("Last-Event-ID", "Last-Event-ID lets you resume an SSE stream after a disconnect — the server continues from the last event you received.", None, ()),
        ("semantic search", "Semantic search finds relevant code or docs by meaning, not just exact keyword matches.", None, ()),
        ("vector retrieval", "Vector retrieval stores embeddings of text so similar concepts can be found even when wording differs.", None, ()),
        ("lost in the middle", "Lost in the middle is the tendency for models to pay less attention to information buried in the middle of a long context.", None, ()),
        ("context engineering", "Context engineering is deliberately choosing what files, rules, and history you include — and what you leave out.", None, ()),
        ("human-in-the-loop", "Human-in-the-loop means a person reviews AI output before it ships — the safety pattern we use throughout this course.", None, ()),
        ("constrained decoding", "Constrained decoding restricts output shape — for example JSON mode or regex patterns the model must follow.", None, ()),
        ("self-consistency", "Self-consistency means running the same prompt several times and comparing or voting on answers to reduce random errors.", None, ()),
        ("diff review", "Diff review is reading added and removed lines before you accept an AI edit — your primary quality gate.", None, ()),
        ("checkpoint", "A checkpoint is a saved snapshot of your code and conversation you can roll back to after an experiment.", None, ("checkpoints",)),
        ("@mention", "An @mention points the agent at specific context — a file, folder, symbol, branch, or the web.", None, ("@mentions", "@file", "@folder", "@symbol", "@web", "@branch")),
        ("Browser tool", "The Browser tool lets the agent open a live page, inspect the DOM, and read console or network activity.", None, ()),
        ("Terminal tool", "The Terminal tool lets the agent propose shell commands — you approve them, then it reads stdout and stderr.", None, ()),
        ("Repository Instructions", "Repository Instructions are a single project overview file the agent reads for stack, commands, and conventions.", None, ()),
        ("slash command", "A slash command is a typed shortcut — often backed by a skill — that triggers a repeatable workflow.", None, ("slash commands",)),
        ("subagent", "A subagent is a delegated specialist agent — often run in parallel or in isolation for a subtask.", None, ("subagents",)),
        ("one-shot CLI", "One-shot CLI means a single non-interactive agent command — ideal for scripts and CI pipelines.", None, ()),
        ("interactive CLI", "Interactive CLI is a long-lived terminal session where you chat with agent, switch models, and resume later.", None, ()),
        ("artifact", "An artifact is a downloadable output from a Cloud Agent run — logs, patches, or generated files.", None, ("artifacts",)),
        ("acceptance rate", "Acceptance rate is the share of AI-suggested edits a developer accepted versus rejected.", None, ()),
        ("AI commit metrics", "AI commit metrics track how much committed code came from AI assistance versus human-only edits.", None, ()),
        ("granular change events", "Granular change events are per-edit audit records — file, lines changed, model used, and whether the edit was accepted.", None, ()),
        ("spend limit", "A spend limit is a monthly cap on a user's Cursor usage — can alert or block when exceeded.", None, ("spend limits",)),
        ("soft delete", "Soft delete deactivates a user account while retaining audit history — common before permanent removal.", None, ()),
        ("hard delete", "Hard delete permanently removes a user and associated data — irreversible and compliance-sensitive.", None, ()),
        ("anonymization", "Anonymization masks names and identifiers in reports so rankings and exports protect privacy.", None, ()),
        ("scope creep", "Scope creep is when the agent changes more files or behavior than you asked for — constrain with explicit DO NOT lists.", None, ()),
        ("User API Key", "A User API Key is scoped to your account — for launching agents and calling user-level endpoints.", None, ()),
        ("Admin API Key", "An Admin API Key is org-wide — for team membership, usage analytics, and spend limits.", None, ()),
        ("HTTP Basic auth", "HTTP Basic auth sends the API key as the username with an empty password — the pattern used in many Cursor API examples.", None, ()),
        ("Bearer token", "Bearer token auth puts the key in an Authorization Bearer header — another common API style.", None, ()),
        ("pagination", "Pagination splits large result sets into pages — you walk them with offset and limit or cursor parameters.", None, ()),
        ("ngrok", "ngrok creates a public HTTPS tunnel to your laptop so Cursor can deliver webhooks to a local dev server.", None, ()),
        ("Redis", "Redis is an in-memory data store often used for sessions, caches, and job queues.", None, ()),
        ("SQLite", "SQLite is a lightweight file-based database — no separate server process required.", None, ()),
        ("autonomous agent", "An autonomous agent pursues a goal across many steps with minimal prompting — highest autonomy needs the strongest guardrails.", None, ()),
    ]
    return [
        GlossaryEntry(key=k, speech=s, full_form=ff, aliases=a)
        for k, s, ff, a in raw
    ]


_ENTRIES = _entries()
_ENTRY_BY_KEY = {e.key.lower(): e for e in _ENTRIES}


def _slide_corpus(slide: str, heading: str) -> str:
    text = slide
    text = re.sub(r"<!--.*?-->", " ", text, flags=re.DOTALL)
    code_parts = " ".join(extract_fenced_code_blocks(slide))
    text = re.sub(r"```.*?```", " ", text, flags=re.DOTALL)
    text = re.sub(r"!\[[^\]]*\]\([^)]+\)", " ", text)
    text = re.sub(r"<img[^>]+alt=\"([^\"]+)\"[^>]*>", r" \1 ", text)
    text = re.sub(r"<img[^>]+>", " ", text)
    text = re.sub(r"\|", " ", text)
    text = re.sub(r"^#+\s*", " ", text, flags=re.MULTILINE)
    text = re.sub(r"\s+", " ", f"{heading} {text} {code_parts}").strip()
    return text


def _patterns(entry: GlossaryEntry) -> list[re.Pattern[str]]:
    patterns: list[re.Pattern[str]] = []
    keys = (entry.key, *entry.aliases)
    for key in keys:
        escaped = re.escape(key)
        if key.isupper() or re.match(r"^[A-Z0-9./+-]+$", key):
            patterns.append(re.compile(rf"(?<![A-Za-z0-9]){escaped}(?![A-Za-z0-9])", re.I))
        else:
            patterns.append(re.compile(rf"(?<!\w){escaped}(?!\w)", re.I))
    return patterns


def _full_form_on_slide(corpus: str, entry: GlossaryEntry) -> bool:
    if not entry.full_form:
        return False
    return entry.full_form.lower() in corpus.lower()


def _contains_distinct_term(haystack: str, term: str) -> bool:
    """True if term appears as its own word/phrase, not inside a hyphen compound."""
    return bool(
        re.search(rf"(?:^|\s){re.escape(term)}(?:\s|$)", haystack, re.I)
    )


def _is_superseded(key: str, matched: set[str]) -> bool:
    key_lower = key.lower()
    for other in matched:
        if other.lower() == key_lower:
            return True
        if len(other) <= len(key):
            continue
        if _contains_distinct_term(other.lower(), key_lower):
            return True
    return False


def glossary_notes_for_slide(slide: str, heading: str, *, max_notes: int = 8) -> list[str]:
    """Return read-aloud definitions for terms appearing on this slide."""
    corpus = _slide_corpus(slide, heading)
    if len(corpus) < 8:
        return []

    matched: list[GlossaryEntry] = []
    matched_keys: set[str] = set()

    for entry in sorted(_ENTRIES, key=lambda e: len(e.key), reverse=True):
        if _is_superseded(entry.key, matched_keys):
            continue
        if not any(p.search(corpus) for p in _patterns(entry)):
            continue
        if entry.full_form and _full_form_on_slide(corpus, entry):
            # Full form already visible — still define if acronym-only mention is likely jargon.
            acronym_only = re.search(
                rf"(?<![A-Za-z0-9]){re.escape(entry.key)}(?![A-Za-z0-9])",
                corpus,
                re.I,
            )
            if not acronym_only:
                continue
        matched.append(entry)
        matched_keys.add(entry.key)
        if len(matched) >= max_notes:
            break

    if not matched:
        return []

    lines = ["Terms on this slide — quick definitions for the room:"]
    for entry in matched:
        lines.append(entry.speech)
    return lines

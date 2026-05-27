# Cursor Training Program

A complete, instructor-led training program for the **Cursor AI code editor** and the **Cursor APIs**. This repository contains everything needed to run a 2-day workshop: beginner-friendly readmes that explain every concept, hands-on exercises, presentation slides, and curated reading paths.

The materials are organized into **six modules**:

1. [`learn/`](learn/) - mental-model readmes from the Cursor Learn courses (AI Foundations + Coding Agents).
2. [`docs-content-readmes/`](docs-content-readmes/) - beginner-friendly summaries of every Cursor product documentation page.
3. [`api-content-readmes/`](api-content-readmes/) - beginner-friendly summaries of every Cursor API.
4. [`core-exercises/`](core-exercises/) - 25 hands-on exercises covering the Cursor editor, Agent, CLI, and Cloud Agents.
5. [`api-exercises/`](api-exercises/) - 23 hands-on exercises covering the Cloud Agents, Admin, Analytics, AI Code Tracking, and Webhooks APIs.
6. [`slides/`](slides/) - combined course presentation deck (Markdown + HTML).

---

## Repository Layout

```
Cursor_Docs_Slides/
├── learn/                      # Cursor Learn course readmes (013 topics)
├── docs-content-readmes/       # Cursor product documentation readmes (082 topics)
├── api-content-readmes/        # Cursor API readmes (005 topics)
├── core-exercises/             # 25 hands-on Cursor product exercises
│   ├── exercise-1/  ...  exercise-25/
│   └── optional-core-exercises-guide.md
├── api-exercises/              # 23 hands-on Cursor API exercises
│   ├── exercise-1/  ...  exercise-23/
│   └── optional-api-exercises-guide.md
├── slides/                     # Combined course deck (Marp + HTML + speaker notes)
├── slide-exercises/            # Slide-aligned lab guides (modules 2–10)
├── assessment/                 # Pre- and post-course assessments
├── scripts/                    # Deck maintenance (diagrams, speaker notes, Marp theme)
└── FINAL_TABLE_OF_CONTENTS.md  # Full course index
```

---

## Module 1 — Cursor Learn Readmes (`learn/`)

Beginner-friendly explanations of the **Cursor Learn** course material. Builds the mental models a developer needs before using AI tools effectively.

Two connected courses:

- **AI Foundations (001 – 007)** — how AI models work, why outputs are probabilistic, hallucinations, tokens and pricing, context, tool calling, and agents.
- **Coding Agents (008 – 013)** — working with agents, understanding a codebase, developing features, debugging, reviewing and testing code, and customizing agents with rules, skills, and MCP.

### Content

| # | Topic | What it covers |
|---|-------|----------------|
| 001 | AI Foundations Overview | Transportation analogy (walk / bike / car ↔ manual / IDE / AI), why mental models matter, frustration cycle, core patterns (generation, explanation, debugging, refactoring, docs, tests). |
| 002 | How AI Models Work | Deterministic vs. probabilistic outputs, training data + prompt = output, model trade-offs (intelligence / speed / cost / expertise), modalities (text, images, voice, video). |
| 003 | Hallucinations | What they are, why models hallucinate, coding-specific hallucinations (invented APIs, wrong imports), knowledge cutoff, verification mindset, editor feedback loop. |
| 004 | Tokens and Pricing | Tokenization, input vs. output tokens (output 2–4× more expensive), TPS, streaming, caching, example pricing for Cursor's models. |
| 005 | Context | The single most important practical skill: context management. System vs. user prompts, what counts as context, context windows (200K – 1M in Max Mode), compression, checkpoints, subagents. |
| 006 | Tool Calling | The four-step request–tool–result–incorporate loop, the three components of a tool (name, description, parameters), token cost of tools, MCP as the "USB standard". |
| 007 | Agents | "Tools in a loop", dark-mode-toggle walkthrough, goal-based delegation vs. turn-by-turn, agent strengths and weaknesses, the new architect/reviewer role. |
| 008 | Working with Agents | The agent harness (Instructions + Tools + Model), constrained vs. vague prompts, when to start new conversations, referencing past chats, scope creep. |
| 009 | Understanding Your Codebase | Grep / Instant Grep vs. semantic search (12.5% accuracy gain when combined), targeted vs. broad prompts, the Explore subagent, Mermaid diagrams, "don't change before understanding". |
| 010 | Developing Features | Plan Mode (research → questions → plan → review → build), when to start over, test-driven development with agents, design-to-code with Figma MCP, integrated browser verification. |
| 011 | Finding and Fixing Bugs | Reproduce → reduce → isolate → hypothesize → instrument → prevent. Quick fix vs. Debug Mode, parallel models, runtime data (logs, `EXPLAIN ANALYZE`, console), Sentry / Datadog MCP. |
| 012 | Reviewing and Testing Code | Self-review, watching the diff, `@Branch`, agent self-review, rework-commits workflow, Agent Review, Bugbot, verifiable goals (tests / types / lint), cloud agents for parallel variations. |
| 013 | Customizing Agents | Rules (`.cursor/rules/`) for static context, Skills for dynamic workflows, MCP for external tools (Slack, Datadog, Sentry, Figma), CLI tools (gh, aws, kubectl, docker), reusable `/commands`. |

Full index and reading paths: [`learn/learn-readmes-index.md`](learn/learn-readmes-index.md).

---

## Module 2 — Cursor Docs Readmes (`docs-content-readmes/`)

Beginner-friendly summaries of the **full Cursor product surface** (82 topics).

### Content groups

- **Getting started** — Cursor overview, quickstart, changelog.
- **Models and pricing** — model selection, pricing concepts, Claude 4.6 Sonnet, Claude Opus 4.7, Gemini 3.1 Pro, GPT-5.5, GPT-5.3 Codex, Grok 4.3, Cursor Composer 2.5.
- **Agent workflows** — Agent overview, Agents window, Agent Review, Plan Mode, Debug Mode, prompting, tools (terminal, browser, search, canvas), checkpoints, worktrees, security.
- **Customization** — plugins, rules, skills, subagents, hooks, MCP.
- **Cloud Agent** — setup, capabilities, my machines, self-hosted pool, automations, best practices, security & network, settings, API endpoints, Bugbot, security review.
- **Developer tooling** — TypeScript SDK, CLI (overview, installation, using, shell mode, ACP, headless, slash commands, parameters, authentication, permissions, configuration), deeplinks.
- **Integrations** — Slack, Microsoft Teams, Jira, Linear, GitHub, GitLab, JetBrains, Xcode, Cursor Blame.
- **Teams and account administration** — team setup, pricing, members, SSO, dashboard, analytics, SCIM, enterprise billing groups.
- **Enterprise** — enterprise overview, identity & access management, privacy & data governance, network configuration, LLM safety & controls, model & integration management, pooled usage, compliance & monitoring, BAA, deployment patterns, service accounts.

Full index and reading paths (Beginner, Agent Power User, Automation/CLI, Admin/Enterprise): [`docs-content-readmes/docs-content-readmes-index.md`](docs-content-readmes/docs-content-readmes-index.md).

---

## Module 3 — Cursor API Readmes (`api-content-readmes/`)

Beginner-friendly explanations of the **five Cursor APIs** plus shared concepts.

### Content

| # | Topic | What it covers |
|---|-------|----------------|
| 001 | API Overview | The five Cursor APIs at a glance, decision tree for picking one, authentication, rate limits, ETag caching, exponential backoff, error responses, best practices. |
| 002 | Cloud Agents API | Durable agents + per-prompt runs, every agent/run endpoint, SSE streaming with `Last-Event-ID` resume, artifacts and presigned downloads, archive/delete, worker tokens, metadata endpoints. Also: webhooks — `statusChange` event, HMAC-SHA256 verification, Python/Node receivers, ngrok testing, idempotency. |
| 003 | Admin API | Admin API keys, team members, audit logs with event-type filters, daily usage data, spending data, granular usage events, user spend limits, member removal, repository blocklists, enterprise billing groups. |
| 004 | Analytics API | Admin-scoped auth, 30-day max range, team-level endpoints (agent edits, Tab, DAU, model usage, file extensions, MCP, slash commands, Plan mode, Skills, Ask mode, conversation insights, leaderboard, Bugbot) plus matching `/analytics/by-user/...` endpoints. |
| 005 | AI Code Tracking API | On-device signature detection (Tab / Composer / human), commit metrics (JSON + streaming CSV), granular AI change events, alpha commit details with conversation references, commit sources (`ide`, `cli`, `cloud`), privacy mode effects. |

### Plan availability

| API | Best For | Auth | Availability |
|-----|----------|------|--------------|
| Cloud Agents | Launching and managing agents from code | User or service account API key | Beta — all plans |
| Admin | Team management, spending, audit logs | Admin API key | Enterprise |
| Analytics | Usage metrics, adoption, leaderboards | Admin-scoped API key | Enterprise |
| AI Code Tracking | Per-commit AI attribution | Admin-scoped API key | Enterprise (alpha) |

Full index and reading paths: [`api-content-readmes/api-content-readmes-index.md`](api-content-readmes/api-content-readmes-index.md).

---

## Module 4 — Core Exercises (`core-exercises/`)

25 hands-on Cursor product exercises in five tracks. Each exercise lives in its own `exercise-N/` folder with step-by-step instructions and any supporting code.

| Track | Exercises | Topic |
|-------|-----------|-------|
| 1 — Fundamentals | 1 – 8 | Codebase understanding, @mentions, safe changes, Plan Mode, comparing models, checkpoints, terminal commands. |
| 2 — Agent Tools | 9 – 13 | Browser tool (view + console), terminal (run tests, fix errors), Ask vs. Agent mode. |
| 3 — Customization | 14 – 18 | Create a rule, AGENTS.md, create + invoke a skill, create a subagent. |
| 4 — CLI & Automation | 19 – 22 | CLI interactive mode, one-shot mode, cloud handoff, list & resume. |
| 5 — Cloud Agents | 23 – 25 | Launch a Cloud Agent, Cloud Agent from Slack, Cloud Agent artifacts. |

Essential / Recommended / Optional classification and a per-exercise time plan: [`core-exercises/optional-core-exercises-guide.md`](core-exercises/optional-core-exercises-guide.md).

---

## Module 5 — API Exercises (`api-exercises/`)

23 hands-on Cursor API exercises in six tracks. Each exercise lives in its own `exercise-N/` folder.

| Track | Exercises | Topic |
|-------|-----------|-------|
| 1 — Foundations | 1 – 4 | API keys, rate limits & error handling, ETag caching, list available models. |
| 2 — Cloud Agents API | 5 – 7 | Create a Cloud Agent, stream responses (SSE), list & download artifacts. |
| 3 — Admin API | 8 – 11 | List team members, daily usage data, set user spend limits, remove a team member. |
| 4 — Analytics API | 12 – 15 | Model usage analytics, DAU, leaderboard, conversation insights. |
| 5 — AI Code Tracking API | 16 – 19 | AI commit metrics, CSV export, granular AI change metrics, commit details (alpha). |
| 6 — Webhooks & Workflows | 20 – 23 | Create webhook endpoint, test with ngrok, automated agent workflow, complete dashboard. |

Essential / Recommended / Optional classification and a per-exercise time plan: [`api-exercises/optional-api-exercises-guide.md`](api-exercises/optional-api-exercises-guide.md).

---

## Slides (`slides/`)

Single instructor deck for the full course (Markdown source + HTML export).

- [`course-complete-marp-with-notes.md`](slides/course-complete-marp-with-notes.md) — full course with embedded presenter notes (source)
- [`course-complete-marp-with-notes.html`](slides/course-complete-marp-with-notes.html) — open in a browser to present
- [`course-complete-speaker-notes.md`](slides/course-complete-speaker-notes.md) — standalone speaker script (optional)

---

# 2-Day Training Outline

The program is structured around **two parallel 2-day tracks**. Pick the track that matches your audience:

- **Track A — Cursor Product (2 days):** for engineers who will use Cursor day-to-day. Uses Modules 1, 2, 4, 6.
- **Track B — Cursor APIs (2 days):** for platform / admin / automation engineers integrating Cursor into their systems. Uses Modules 3, 5.

> **Tip:** Need to cover both? Run them back-to-back as a **4-day program** (Track A then Track B). Need only the must-do exercises? Each guide lists an Essential-only subset that fits in ~1 day.

---

## Track A — Cursor Product (2 Days)

Sources: [`learn/`](learn/), [`docs-content-readmes/`](docs-content-readmes/), [`core-exercises/`](core-exercises/), [`slides/`](slides/).

### Day 1 — Foundations + Agent Tools

Goal: build mental models (Module 1, lessons 001 – 009) and complete the core editor & agent workflow (Module 4, Tracks 1 – 2).

| Time | Activity | Reference |
|------|----------|-----------|
| 9:00 – 9:15 | Setup & welcome — install Cursor, sign in, open project | [`slides/course-complete-marp-with-notes.md`](slides/course-complete-marp-with-notes.md) |
| 9:15 – 9:25 | Exercise 1: Codebase Understanding | [`core-exercises/exercise-1/`](core-exercises/exercise-1/) |
| 9:25 – 9:35 | Exercise 2: Explain a Specific File | [`core-exercises/exercise-2/`](core-exercises/exercise-2/) |
| 9:35 – 9:45 | Exercise 3: Make a Safe Change | [`core-exercises/exercise-3/`](core-exercises/exercise-3/) |
| 9:45 – 9:55 | Exercise 4: Use Plan Mode | [`core-exercises/exercise-4/`](core-exercises/exercise-4/) |
| 9:55 – 10:05 | Exercise 5: Compare Two Models | [`core-exercises/exercise-5/`](core-exercises/exercise-5/) |
| 10:05 – 10:15 | Exercise 6: Use @mentions | [`core-exercises/exercise-6/`](core-exercises/exercise-6/) |
| 10:15 – 10:30 | **Break** | |
| 10:30 – 10:40 | Exercise 7: Use Checkpoints | [`core-exercises/exercise-7/`](core-exercises/exercise-7/) |
| 10:40 – 10:50 | Exercise 8: Run a Terminal Command | [`core-exercises/exercise-8/`](core-exercises/exercise-8/) |
| 10:50 – 11:00 | Exercise 13: Ask Mode vs Agent Mode | [`core-exercises/exercise-13/`](core-exercises/exercise-13/) |
| 11:00 – 11:15 | Exercise 9: Browser Tool — View Page | [`core-exercises/exercise-9/`](core-exercises/exercise-9/) |
| 11:15 – 11:30 | Exercise 10: Browser Tool — Read Console | [`core-exercises/exercise-10/`](core-exercises/exercise-10/) |
| 11:30 – 11:45 | Exercise 11: Terminal Tool — Run Tests | [`core-exercises/exercise-11/`](core-exercises/exercise-11/) |
| 11:45 – 12:00 | Exercise 12: Terminal Tool — Fix Errors | [`core-exercises/exercise-12/`](core-exercises/exercise-12/) |
| 12:00 – 1:00 | **Lunch** | |
| 1:00 – 2:00 | Open lab — repeat exercises on participants' own repos | |
| 2:00 – 2:30 | Day 1 wrap-up — review mental models (Learn 001 – 009) | [`learn/`](learn/) |

**Conceptual reading anchors (Module 1):** 001 AI Foundations Overview, 002 How AI Models Work, 003 Hallucinations, 004 Tokens & Pricing, 005 Context, 006 Tool Calling, 007 Agents, 008 Working with Agents, 009 Understanding Your Codebase.

**Documentation anchors (Module 2):** 001 Cursor overview, 002 Quickstart, 012 Agent overview, 016 Plan Mode, 017 Prompting, 018 Debug Mode, 019 – 022 Agent tools (terminal, browser, search, canvas), 024 Agent security.

---

### Day 2 — Customization + CLI + Cloud Agents

Goal: customize agents to the team and codebase (Module 1, lessons 010 – 013) and complete Module 4 Tracks 3 – 5.

| Time | Activity | Reference |
|------|----------|-----------|
| 9:00 – 9:15 | Day 1 recap | |
| 9:15 – 9:25 | Exercise 14: Create a Rule | [`core-exercises/exercise-14/`](core-exercises/exercise-14/) |
| 9:25 – 9:35 | Exercise 15: Use AGENTS.md | [`core-exercises/exercise-15/`](core-exercises/exercise-15/) |
| 9:35 – 9:50 | Exercise 16: Create a Skill | [`core-exercises/exercise-16/`](core-exercises/exercise-16/) |
| 9:50 – 10:05 | Exercise 17: Invoke a Skill | [`core-exercises/exercise-17/`](core-exercises/exercise-17/) |
| 10:05 – 10:20 | Exercise 19: CLI — Interactive Mode | [`core-exercises/exercise-19/`](core-exercises/exercise-19/) |
| 10:20 – 10:35 | **Break** | |
| 10:35 – 10:50 | Exercise 20: CLI — One-Shot Mode | [`core-exercises/exercise-20/`](core-exercises/exercise-20/) |
| 10:50 – 11:05 | Exercise 21: CLI — Cloud Handoff | [`core-exercises/exercise-21/`](core-exercises/exercise-21/) |
| 11:05 – 11:20 | Exercise 22: CLI — List & Resume | [`core-exercises/exercise-22/`](core-exercises/exercise-22/) |
| 11:20 – 11:35 | Exercise 23: Launch Cloud Agent | [`core-exercises/exercise-23/`](core-exercises/exercise-23/) |
| 11:35 – 11:50 | Exercise 18 (demo): Create a Subagent | [`core-exercises/exercise-18/`](core-exercises/exercise-18/) |
| 11:50 – 12:00 | Exercise 24 + 25 (demo): Cloud Agent from Slack + Artifacts | [`core-exercises/exercise-24/`](core-exercises/exercise-24/), [`core-exercises/exercise-25/`](core-exercises/exercise-25/) |
| 12:00 – 1:00 | **Lunch** | |
| 1:00 – 2:00 | Open lab / Q&A | |
| 2:00 – 2:30 | Wrap-up | |

**Conceptual reading anchors (Module 1):** 010 Developing Features, 011 Finding and Fixing Bugs, 012 Reviewing and Testing Code, 013 Customizing Agents.

**Documentation anchors (Module 2):** 026 Rules, 028 Skills, 029 Subagents, 030 Hooks, 031 MCP, 032 – 043 Cloud Agent, 052 – 062 CLI, 037 Bugbot, 038 Security review.

---

## Track B — Cursor APIs (2 Days)

Sources: [`api-content-readmes/`](api-content-readmes/), [`api-exercises/`](api-exercises/).

### Day 1 — Foundations + Cloud Agents + Webhooks

Goal: master authentication, rate limits, the only all-plans API (Cloud Agents), and webhook plumbing.

| Time | Activity | Reference |
|------|----------|-----------|
| 9:00 – 9:15 | Setup & welcome — provision API keys, install httpie/curl/Postman | |
| 9:15 – 9:25 | Exercise 1: Generate and Test API Keys | [`api-exercises/exercise-1/`](api-exercises/exercise-1/) |
| 9:25 – 9:35 | Exercise 2: Rate Limits and Error Handling | [`api-exercises/exercise-2/`](api-exercises/exercise-2/) |
| 9:35 – 9:45 | Exercise 3: ETag Caching | [`api-exercises/exercise-3/`](api-exercises/exercise-3/) |
| 9:45 – 9:50 | Exercise 4: List Available Models | [`api-exercises/exercise-4/`](api-exercises/exercise-4/) |
| 9:50 – 10:00 | Exercise 5: Create a Cloud Agent | [`api-exercises/exercise-5/`](api-exercises/exercise-5/) |
| 10:00 – 10:15 | **Break** | |
| 10:15 – 10:30 | Exercise 6: Stream Agent Responses (SSE) | [`api-exercises/exercise-6/`](api-exercises/exercise-6/) |
| 10:30 – 10:45 | Exercise 7: List and Download Artifacts | [`api-exercises/exercise-7/`](api-exercises/exercise-7/) |
| 10:45 – 11:00 | Exercise 20: Create a Webhook Endpoint (HMAC verify) | [`api-exercises/exercise-20/`](api-exercises/exercise-20/) |
| 11:00 – 11:10 | Exercise 21: Test Webhooks with ngrok | [`api-exercises/exercise-21/`](api-exercises/exercise-21/) |
| 11:10 – 11:20 | Exercise 22: Build Automated Agent Workflow | [`api-exercises/exercise-22/`](api-exercises/exercise-22/) |
| 11:20 – 12:00 | Open lab — wire Cloud Agents into participants' systems | |
| 12:00 – 1:00 | **Lunch** | |
| 1:00 – 2:00 | Free integration time / Q&A | |
| 2:00 – 2:30 | Day 1 wrap-up | |

**Conceptual reading anchors (Module 3):** 001 API Overview, 002 Cloud Agents API.

---

### Day 2 — Admin + Analytics + AI Code Tracking

Goal: complete the Enterprise admin/reporting surface and capstone-level reporting.

| Time | Activity | Reference |
|------|----------|-----------|
| 9:00 – 9:15 | Day 1 recap | |
| 9:15 – 9:20 | Exercise 8: List Team Members | [`api-exercises/exercise-8/`](api-exercises/exercise-8/) |
| 9:20 – 9:30 | Exercise 9: Get Daily Usage Data | [`api-exercises/exercise-9/`](api-exercises/exercise-9/) |
| 9:30 – 9:40 | Exercise 10: Set User Spend Limits | [`api-exercises/exercise-10/`](api-exercises/exercise-10/) |
| 9:40 – 9:50 | Exercise 11 (demo): Remove Team Member | [`api-exercises/exercise-11/`](api-exercises/exercise-11/) |
| 9:50 – 10:00 | Exercise 12: Get Model Usage Analytics | [`api-exercises/exercise-12/`](api-exercises/exercise-12/) |
| 10:00 – 10:10 | Exercise 13: Get Daily Active Users | [`api-exercises/exercise-13/`](api-exercises/exercise-13/) |
| 10:10 – 10:25 | **Break** | |
| 10:25 – 10:35 | Exercise 14: Get Leaderboard | [`api-exercises/exercise-14/`](api-exercises/exercise-14/) |
| 10:35 – 10:45 | Exercise 15 (demo): Conversation Insights | [`api-exercises/exercise-15/`](api-exercises/exercise-15/) |
| 10:45 – 10:55 | Exercise 16: Get AI Commit Metrics | [`api-exercises/exercise-16/`](api-exercises/exercise-16/) |
| 10:55 – 11:05 | Exercise 17: Download AI Commit Metrics CSV | [`api-exercises/exercise-17/`](api-exercises/exercise-17/) |
| 11:05 – 11:15 | Exercise 18: Granular AI Change Metrics | [`api-exercises/exercise-18/`](api-exercises/exercise-18/) |
| 11:15 – 11:25 | Exercise 19 (demo): Commit Details (Alpha) | [`api-exercises/exercise-19/`](api-exercises/exercise-19/) |
| 11:25 – 11:50 | Exercise 23 (demo / take-home): Build a Complete Dashboard | [`api-exercises/exercise-23/`](api-exercises/exercise-23/) |
| 11:50 – 12:00 | Wrap-up | |
| 12:00 – 1:00 | **Lunch** | |
| 1:00 – 2:30 | Open lab / capstone work | |

**Conceptual reading anchors (Module 3):** 003 Admin API, 004 Analytics API, 005 AI Code Tracking API.

---

## Coverage Summary

| Track | Days | Essential | Recommended | Demo / Optional | Total Exercises |
|-------|-----:|----------:|------------:|----------------:|----------------:|
| A — Cursor Product | 2 | 14 | 8 | 3 | 25 |
| B — Cursor APIs | 2 | 10 | 9 | 4 | 23 |
| **Combined (A + B)** | **4** | **24** | **17** | **7** | **48** |

---

## Prerequisites

- Cursor installed and signed in.
- A Git repository each participant can experiment in (sample repos work fine for Track A).
- For Track B: ability to generate a Cursor API key (Enterprise plan needed for Admin / Analytics / AI Code Tracking exercises; Cloud Agents and Webhooks work on all plans).
- For webhook exercises: `ngrok` (or equivalent tunnel) installed locally.

---

## Where to Start

| If you are… | Begin here |
|-------------|------------|
| A learner taking Track A | [`slides/course-complete-marp-with-notes.html`](slides/course-complete-marp-with-notes.html) → [`core-exercises/exercise-1/`](core-exercises/exercise-1/) |
| A learner taking Track B | [`api-content-readmes/001-api-overview.md`](api-content-readmes/001-api-overview.md) → [`api-exercises/exercise-1/`](api-exercises/exercise-1/) |
| An instructor planning a session | [`core-exercises/optional-core-exercises-guide.md`](core-exercises/optional-core-exercises-guide.md) and [`api-exercises/optional-api-exercises-guide.md`](api-exercises/optional-api-exercises-guide.md) |
| Someone reading on their own | The four index files: [Learn](learn/learn-readmes-index.md), [Docs](docs-content-readmes/docs-content-readmes-index.md), [APIs](api-content-readmes/api-content-readmes-index.md) |

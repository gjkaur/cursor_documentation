# Cursor Training Program

A complete, instructor-led training program for the **Cursor AI code editor** and the **Cursor APIs**. This repository contains everything needed to run a **2-day workshop**: presentation slides with presenter notes, slide-aligned lab guides, pre/post assessments, beginner-friendly concept readmes, and optional deep-dive exercises.

## At a glance

| | |
|---|---|
| **Primary delivery** | 2-day course, 10 modules, ~11.5 hours |
| **Present** | [`slides/course-complete-marp-with-notes.html`](slides/course-complete-marp-with-notes.html) |
| **Full index** | [`FINAL_TABLE_OF_CONTENTS.md`](FINAL_TABLE_OF_CONTENTS.md) — modules, lessons, exercises, links |
| **In-class labs** | [`slide-exercises/`](slide-exercises/) — 40 step-by-step guides aligned to slides |
| **Extra practice** | [`core-exercises/`](core-exercises/) (25) · [`api-exercises/`](api-exercises/) (23) |
| **Assessments** | [`assessment/pre-assessment.md`](assessment/pre-assessment.md) · [`assessment/post-assessment.md`](assessment/post-assessment.md) |

**Day 1** — Mental models, editor essentials, agent tools, team customization, CLI.  
**Day 2** — Cloud Agents UI, API foundations, Cloud Agents API/webhooks, admin analytics, AI code tracking.

---

## Repository layout

```
Cursor_Docs_Slides/
├── FINAL_TABLE_OF_CONTENTS.md  # Master index (modules 1–10, lessons, labs)
├── learn/                        # Cursor Learn readmes (13 topics)
├── docs-content-readmes/         # Product documentation summaries (82 topics)
├── api-content-readmes/          # API reference summaries (5 topics)
├── core-exercises/               # 25 optional Cursor product labs
├── api-exercises/                # 23 optional Cursor API labs
├── slides/                       # Combined Marp deck + HTML export + speaker script
│   └── assets/                   # Diagram SVGs used by the deck
├── slide-exercises/              # Slide-aligned lab guides (modules 2–10)
├── assessment/                   # Pre- and post-training assessments
└── scripts/                      # Deck maintenance (theme, diagrams, speaker notes)
```

---

## Instructor delivery

### Slides

Single deck for the full course — no per-module slide files.

| File | Use |
|------|-----|
| [`slides/course-complete-marp-with-notes.html`](slides/course-complete-marp-with-notes.html) | **Present** in a browser (recommended) |
| [`slides/course-complete-marp-with-notes.md`](slides/course-complete-marp-with-notes.md) | Edit source; embedded `<!--` presenter notes |
| [`slides/course-complete-speaker-notes.md`](slides/course-complete-speaker-notes.md) | Standalone read-aloud script (optional printout) |

**Re-export HTML** after editing the `.md` source (requires [Marp CLI](https://github.com/marp-team/marp-cli)):

```bash
npx @marp-team/marp-cli slides/course-complete-marp-with-notes.md \
  --html --allow-local-files \
  --theme-set scripts/themes/flat-gaia.css \
  -o slides/course-complete-marp-with-notes.html
```

### Slide exercises

During the deck, hands-on blocks point to [`slide-exercises/`](slide-exercises/) — one markdown guide per slide exercise (e.g. `module-02/exercise-2.1-codebase-understanding.md`). These are the **in-class** labs; they link to longer optional write-ups in `core-exercises/` and `api-exercises/` where relevant.

### Assessments

| Assessment | File | When |
|------------|------|------|
| Pre-training | [`assessment/pre-assessment.md`](assessment/pre-assessment.md) | Before Day 1 (~8–10 min) |
| Post-training | [`assessment/post-assessment.md`](assessment/post-assessment.md) | After Day 2 |

### Planning and pacing

Use [`FINAL_TABLE_OF_CONTENTS.md`](FINAL_TABLE_OF_CONTENTS.md) for module goals, lesson times, exercise lists, and cross-links. Exercise essential vs. optional picks: [`core-exercises/optional-core-exercises-guide.md`](core-exercises/optional-core-exercises-guide.md) and [`api-exercises/optional-api-exercises-guide.md`](api-exercises/optional-api-exercises-guide.md).

### Maintaining the deck (`scripts/`)

| Script | Purpose |
|--------|---------|
| [`scripts/themes/flat-gaia.css`](scripts/themes/flat-gaia.css) | Marp theme |
| [`scripts/fix-corrupted-diagram-svgs.py`](scripts/fix-corrupted-diagram-svgs.py) | Repair known-bad diagram SVGs |
| [`scripts/regenerate-marp-diagram-svgs.py`](scripts/regenerate-marp-diagram-svgs.py) | Regenerate diagram assets |
| [`scripts/generate-speaker-notes.py`](scripts/generate-speaker-notes.py) | Regenerate speaker notes / embedded notes from deck |
| [`scripts/trim-repetitive-slides.py`](scripts/trim-repetitive-slides.py) | Remove duplicate agenda/summary slides (keeps lesson dividers) |
| [`scripts/restore-lesson-dividers.py`](scripts/restore-lesson-dividers.py) | Re-insert `# Lesson X.Y` section slides from git history |
| [`scripts/inject-lab-guide-links.py`](scripts/inject-lab-guide-links.py) | Add lab guide links on first exercise slide per lab |
| [`scripts/export-editable-pptx.ps1`](scripts/export-editable-pptx.ps1) | Optional PowerPoint export |

Edit the combined deck directly; per-module Marp sources are not kept in this repo.

---

## Content libraries

Six reference libraries support the course and self-study. They are **not** the same numbering as the **10 course modules** in the slide deck.

### Learn readmes (`learn/`)

Mental models from **Cursor Learn** (AI Foundations 001–007, Coding Agents 008–013). Index: [`learn/learn-readmes-index.md`](learn/learn-readmes-index.md).

| # | Topic | What it covers |
|---|-------|----------------|
| 001 | AI Foundations Overview | Transportation analogy, mental models, core AI-assisted patterns. |
| 002 | How AI Models Work | Probabilistic outputs, model trade-offs, modalities. |
| 003 | Hallucinations | Verification mindset, coding-specific hallucinations. |
| 004 | Tokens and Pricing | Tokenization, input vs. output cost, streaming, caching. |
| 005 | Context | Context windows, compression, checkpoints, subagents. |
| 006 | Tool Calling | Request–tool–result loop, MCP overview. |
| 007 | Agents | Tools in a loop, delegation vs. turn-by-turn. |
| 008 | Working with Agents | Harness, prompts, scope creep. |
| 009 | Understanding Your Codebase | Search, Explore subagent, read-before-change. |
| 010 | Developing Features | Plan Mode, TDD with agents, design-to-code. |
| 011 | Finding and Fixing Bugs | Debug Mode, runtime data, observability MCP. |
| 012 | Reviewing and Testing Code | Diffs, Agent Review, Bugbot, verifiable goals. |
| 013 | Customizing Agents | Rules, Skills, MCP, CLI tools, slash commands. |

### Docs readmes (`docs-content-readmes/`)

Summaries of the **Cursor product documentation** (82 topics): getting started, models, agent workflows, customization, Cloud Agent, CLI, integrations, teams, enterprise. Index: [`docs-content-readmes/docs-content-readmes-index.md`](docs-content-readmes/docs-content-readmes-index.md).

### API readmes (`api-content-readmes/`)

Summaries of the **five Cursor APIs** plus shared concepts. Index: [`api-content-readmes/api-content-readmes-index.md`](api-content-readmes/api-content-readmes-index.md).

| # | Topic | What it covers |
|---|-------|----------------|
| 001 | API Overview | API selection, auth, rate limits, ETag caching, errors. |
| 002 | Cloud Agents API | Agents, runs, SSE, artifacts, webhooks. |
| 003 | Admin API | Team members, usage, spend limits, audit logs. |
| 004 | Analytics API | Adoption metrics, leaderboards, by-user endpoints. |
| 005 | AI Code Tracking API | Commit metrics, CSV export, granular change events. |

| API | Best for | Availability |
|-----|----------|--------------|
| Cloud Agents | Launching agents from code | Beta — all plans |
| Admin | Team management, spending | Enterprise |
| Analytics | Usage and adoption metrics | Enterprise |
| AI Code Tracking | Per-commit AI attribution | Enterprise (alpha) |

### Core exercises (`core-exercises/`)

25 optional **Cursor product** labs (editor, Agent, CLI, Cloud Agents). Index by essential/recommended/optional: [`core-exercises/optional-core-exercises-guide.md`](core-exercises/optional-core-exercises-guide.md).

| Track | Exercises | Topic |
|-------|-----------|-------|
| Fundamentals | 1 – 8 | Codebase, @mentions, safe changes, Plan Mode, models, checkpoints, terminal. |
| Agent tools | 9 – 13 | Browser, terminal, Ask vs. Agent mode. |
| Customization | 14 – 18 | Rules, AGENTS.md, skills, subagents. |
| CLI & automation | 19 – 22 | Interactive CLI, one-shot, cloud handoff, sessions. |
| Cloud Agents | 23 – 25 | Launch, Slack, artifacts. |

### API exercises (`api-exercises/`)

23 optional **Cursor API** labs. Index: [`api-exercises/optional-api-exercises-guide.md`](api-exercises/optional-api-exercises-guide.md).

| Track | Exercises | Topic |
|-------|-----------|-------|
| Foundations | 1 – 4 | API keys, rate limits, ETag, models. |
| Cloud Agents API | 5 – 7 | Create agent, SSE, artifacts. |
| Admin API | 8 – 11 | Members, usage, spend limits. |
| Analytics API | 12 – 15 | Model usage, DAU, leaderboard, insights. |
| AI Code Tracking | 16 – 19 | Commit metrics, CSV, granular events. |
| Webhooks & workflows | 20 – 23 | Webhooks, ngrok, automation, dashboard. |

---

## Optional workshop schedules

The **slide deck** follows the unified 2-day outline in [`FINAL_TABLE_OF_CONTENTS.md`](FINAL_TABLE_OF_CONTENTS.md). If you are **not** using the deck, these exercise-only schedules still work:

- **Track A — Cursor Product (2 days):** `learn/`, `docs-content-readmes/`, `core-exercises/`
- **Track B — Cursor APIs (2 days):** `api-content-readmes/`, `api-exercises/`

Run both back-to-back for a **4-day** program. Each optional guide lists an Essential-only subset for a ~1-day cut.

<details>
<summary>Track A — day-by-day timetable (exercise-only)</summary>

**Day 1** — Foundations + agent tools: exercises 1–13 (see [`core-exercises/`](core-exercises/)). Reading anchors: Learn 001–009; docs Agent overview, Plan Mode, tools.

**Day 2** — Customization + CLI + Cloud Agents: exercises 14–25. Reading anchors: Learn 010–013; docs Rules, Skills, MCP, Cloud Agent, CLI.

</details>

<details>
<summary>Track B — day-by-day timetable (exercise-only)</summary>

**Day 1** — API foundations + Cloud Agents + webhooks: exercises 1–7, 20–22. Reading: API readmes 001–002.

**Day 2** — Admin, analytics, AI code tracking: exercises 8–19, 23. Reading: API readmes 003–005.

</details>

---

## Coverage summary

| Track | Days | Essential | Recommended | Demo / optional | Total exercises |
|-------|-----:|----------:|------------:|----------------:|----------------:|
| Slide course (modules 1–10) | 2 | — | — | — | 40 slide labs + concept blocks |
| Core exercises (extra) | — | 14 | 8 | 3 | 25 |
| API exercises (extra) | — | 10 | 9 | 4 | 23 |

---

## Prerequisites

- Cursor installed and signed in.
- A Git repository to experiment in (sample repos are fine).
- **API modules (7–10):** Cursor API key; Enterprise plan for Admin, Analytics, and AI Code Tracking labs.
- **Webhooks:** `ngrok` or equivalent tunnel for local webhook testing.

---

## Where to start

| Role | Start here |
|------|------------|
| **Instructor** | [`FINAL_TABLE_OF_CONTENTS.md`](FINAL_TABLE_OF_CONTENTS.md) → [`slides/course-complete-marp-with-notes.html`](slides/course-complete-marp-with-notes.html) → [`slide-exercises/`](slide-exercises/) |
| **Learner in class** | Follow the deck and linked slide exercises |
| **Self-study (product)** | [`learn/learn-readmes-index.md`](learn/learn-readmes-index.md) → [`core-exercises/exercise-1/`](core-exercises/exercise-1/) |
| **Self-study (APIs)** | [`api-content-readmes/001-api-overview.md`](api-content-readmes/001-api-overview.md) → [`api-exercises/exercise-1/`](api-exercises/exercise-1/) |
| **Deep reference** | Learn, docs, and API index files under each content folder |

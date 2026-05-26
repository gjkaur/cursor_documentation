# Cursor Training Program — Final Table of Contents

Complete reference for all **10 modules**, **52 lessons**, and **40 hands-on slide exercises** in the Cursor Training Program. Generated from instructor slide decks (`slides/module-*-marp.md`) and step-by-step lab guides (`slide-exercises/`).

*Generated: 2026-05-22*

> **Note:** This is a supplementary index. The original [`TABLE_OF_CONTENTS.md`](TABLE_OF_CONTENTS.md) remains unchanged.

---

## At a Glance

| | |
|---|---|
| **Duration** | 2 days (~11.5 hours) |
| **Modules** | 10 |
| **Lessons** | 52 total |
| **Slide exercises** | 40 written lab guides in `slide-exercises/` |
| **Core exercises** | 25 optional hands-on labs in `core-exercises/` |
| **Slide decks** | `slides/module-01-marp.md` … `slides/module-10-marp.md` |
| **Combined deck** | `slides/course-complete-marp.md` |

### Day 1 — Cursor Editor and Agent Fluency

Modules 1–5: mental models, editor essentials, agent tools, team customization, CLI automation.

### Day 2 — Cloud Agents, APIs, and Analytics

Modules 6–10: cloud agents UI, API foundations, Cloud Agents API/webhooks, admin analytics, AI code tracking.

---

## Module Index

| # | Day | Module | Format | Duration | Lessons | Exercises | Slide deck |
|---|-----|--------|--------|----------|---------|-----------|------------|
| **1** | Day 1 | Mental Models for AI-Assisted Development | Concept block (foundational theory) | ~60 minutes | 6 | 0 | [`module-01-marp.md`](slides/module-01-marp.md) |
| **2** | Day 1 | Cursor Editor Essentials | Hands-on exercise | ~90 minutes | 8 | 8 | [`module-02-marp.md`](slides/module-02-marp.md) |
| **3** | Day 1 | Agent Modes and Tools | Hands-on exercise + concept | ~60 minutes | 4 | 4 | [`module-03-marp.md`](slides/module-03-marp.md) |
| **4** | Day 1 | Customizing Cursor for Your Team | Hands-on exercise + walkthrough | ~60 minutes | 5 | 3 | [`module-04-marp.md`](slides/module-04-marp.md) |
| **5** | Day 1 | Cursor CLI and Local Automation | Hands-on exercise | ~60 minutes | 4 | 4 | [`module-05-marp.md`](slides/module-05-marp.md) |
| **6** | Day 2 | Cloud Agents in the UI | Hands-on exercise + demonstration | ~90 minutes | 3 | 2 | [`module-06-marp.md`](slides/module-06-marp.md) |
| **7** | Day 2 | Cursor API Foundations | Concept + hands-on exercise | ~60 minutes | 5 | 4 | [`module-07-marp.md`](slides/module-07-marp.md) |
| **8** | Day 2 | Cloud Agents API and Webhooks | Hands-on exercise | ~60 minutes | 6 | 5 | [`module-08-marp.md`](slides/module-08-marp.md) |
| **9** | Day 2 | Admin and Analytics APIs | Hands-on exercise + demonstrations | ~75 minutes | 8 | 6 | [`module-09-marp.md`](slides/module-09-marp.md) |
| **10** | Day 2 | AI Code Tracking and Reporting | Hands-on exercise + take-home project | ~20 minutes (plus take-home project) | 4 | 4 | [`module-10-marp.md`](slides/module-10-marp.md) |

---

## Module 1. Mental Models for AI-Assisted Development

**Day:** Day 1 · **Duration:** ~60 minutes · **Format:** Concept block (foundational theory)

**Module goal:** Build accurate mental models of how AI coding assistants work, their limitations, and how to use them effectively

**Prerequisites:** None – this is the starting point

**Slide deck:** [`slides/module-01-marp.md`](slides/module-01-marp.md) · **HTML:** [`slides/module-01-marp.html`](slides/module-01-marp.html)

**Learning objectives**

- Explain why AI outputs are probabilistic, not deterministic
- Identify and mitigate hallucinations in coding contexts
- Understand token-based pricing and cost optimization
- Master context as the single most valuable AI skill
- Distinguish between tool calling, MCP, and autonomous agents
- Define the developer's evolving role with AI agents

### Lessons and exercises

#### Lesson 1.1 — How AI Models Work

**Time:** 12 min · **Type:** Concept

Why AI outputs are probabilistic; next-token prediction; parameters (temperature, top-p); training gap.

*Concept-only lesson — no hands-on exercise.*

#### Lesson 1.2 — Hallucinations

**Time:** 10 min · **Type:** Concept

What hallucinations are in code; why models invent APIs; mitigation strategies and detection checklist.

*Concept-only lesson — no hands-on exercise.*

#### Lesson 1.3 — Tokens and Pricing

**Time:** 10 min · **Type:** Concept

Token basics; input vs. output pricing; cost calculation; optimization and cache effects.

*Concept-only lesson — no hands-on exercise.*

#### Lesson 1.4 — Context

**Time:** 12 min · **Type:** Concept

Context window limits; prioritization pyramid; lost-in-the-middle; good vs. bad context examples.

*Concept-only lesson — no hands-on exercise.*

#### Lesson 1.5 — Tool Calling and MCP

**Time:** 8 min · **Type:** Concept

Tool calling flow; common dev tools; Model Context Protocol architecture and best practices.

*Concept-only lesson — no hands-on exercise.*

#### Lesson 1.6 — Agents

**Time:** 8 min · **Type:** Concept

Agent vs. chatbot; the agent loop; levels of autonomy; how agents change the developer role.

*Concept-only lesson — no hands-on exercise.*

---

## Module 2. Cursor Editor Essentials

**Day:** Day 1 · **Duration:** ~90 minutes · **Format:** Hands-on exercise

**Module goal:** Master the core workflows of AI-assisted coding in Cursor

**Prerequisites:** Module 1 completed, Cursor installed, Git repository access

**Slide deck:** [`slides/module-02-marp.md`](slides/module-02-marp.md) · **HTML:** [`slides/module-02-marp.html`](slides/module-02-marp.html)

**Learning objectives**

- Orient an AI agent to an unfamiliar codebase
- Get targeted explanations of specific files or symbols
- Make safe, reviewable changes using diff review
- Design complex changes with Plan Mode
- Compare models to choose the right one for each task
- Use @mentions for precise context control
- Navigate checkpoints as a safety net
- Let agents run terminal commands and react to output

### Lessons and exercises

#### Lesson 2.1 — Codebase Understanding

**Time:** 20 min · **Type:** Exercise

**Exercise**

| Field | Detail |
|-------|--------|
| **Title** | Exercise 2.1: Codebase Understanding |
| **Lab time** | 20 min |
| **Difficulty** | Beginner |
| **Objective** | Use the Cursor Agent to orient yourself in an unfamiliar repository. |
| **Lab guide** | [`slide-exercises/module-02/exercise-2.1-codebase-understanding.md`](slide-exercises/module-02/exercise-2.1-codebase-understanding.md) |
| **Slides** | `slides/module-02-marp.md` (Lesson 2.1) |
| **Related core exercise** | [`core-exercises/exercise-1/01-open-agent-first-prompt.md`](core-exercises/exercise-1/01-open-agent-first-prompt.md) |

**Slide sections covered:**
- Exercise 2.1 — Steps 1–2
- Exercise 2.1 — Step 3: Orientation Prompt
- Exercise 2.1 — Step 4: Trace Data Flow
- Exercise 2.1 — Step 5: Visual Overview
- Exercise 2.1 — Success Criteria

#### Lesson 2.2 — Explaining Files/Symbols

**Time:** 13 min · **Type:** Exercise

**Exercise**

| Field | Detail |
|-------|--------|
| **Title** | Exercise 2.2: Explaining a Specific File or Symbol |
| **Lab time** | 13 min |
| **Difficulty** | Beginner |
| **Objective** | Get targeted explanations of one file or symbol without reading the whole repo. |
| **Lab guide** | [`slide-exercises/module-02/exercise-2.2-explaining-a-specific-file-or-symbol.md`](slide-exercises/module-02/exercise-2.2-explaining-a-specific-file-or-symbol.md) |
| **Slides** | `slides/module-02-marp.md` (Lesson 2.2) |
| **Related core exercise** | [`core-exercises/exercise-2/02-explain-a-specific-file.md`](core-exercises/exercise-2/02-explain-a-specific-file.md) |

**Slide sections covered:**
- Exercise 2.2 — Steps 1–3
- Exercise 2.2 — Step 4: Example I/O
- Exercise 2.2 — Step 5: Dependencies

#### Lesson 2.3 — Safe Reviewable Changes

**Time:** 13 min · **Type:** Exercise

**Exercise**

| Field | Detail |
|-------|--------|
| **Title** | Exercise 2.3: Making a Safe, Reviewable Change |
| **Lab time** | 13 min |
| **Difficulty** | Beginner |
| **Objective** | Let the Agent propose a small change and review the diff before accepting. |
| **Lab guide** | [`slide-exercises/module-02/exercise-2.3-making-a-safe-reviewable-change.md`](slide-exercises/module-02/exercise-2.3-making-a-safe-reviewable-change.md) |
| **Slides** | `slides/module-02-marp.md` (Lesson 2.3) |
| **Related core exercise** | [`core-exercises/exercise-3/03-make-a-safe-change.md`](core-exercises/exercise-3/03-make-a-safe-change.md) |

**Slide sections covered:**
- Exercise 2.3 — Steps 1–2
- Exercise 2.3 — Review Questions
- Exercise 2.3 — Test After Accept
- Exercise 2.3 — If Something Goes Wrong

#### Lesson 2.4 — Plan Mode

**Time:** 13 min · **Type:** Exercise

**Exercise**

| Field | Detail |
|-------|--------|
| **Title** | Exercise 2.4: Plan Mode |
| **Lab time** | 13 min |
| **Difficulty** | Beginner |
| **Objective** | Use Plan Mode to design a change before the Agent edits files. |
| **Lab guide** | [`slide-exercises/module-02/exercise-2.4-plan-mode.md`](slide-exercises/module-02/exercise-2.4-plan-mode.md) |
| **Slides** | `slides/module-02-marp.md` (Lesson 2.4) |
| **Related core exercise** | [`core-exercises/exercise-4/04-use-plan-mode.md`](core-exercises/exercise-4/04-use-plan-mode.md) |

**Slide sections covered:**
- Exercise 2.4 — Step 1: Enable Plan Mode
- Exercise 2.4 — Step 2: Describe Change
- Exercise 2.4 — Step 3: Review the Plan
- Exercise 2.4 — Approve & Execute
- Exercise 2.4 — Success Criteria

#### Lesson 2.5 — Comparing Models

**Time:** 13 min · **Type:** Exercise

**Exercise**

| Field | Detail |
|-------|--------|
| **Title** | Exercise 2.5: Comparing Two Models |
| **Lab time** | 13 min |
| **Difficulty** | Beginner |
| **Objective** | Run the same prompt on two models and compare quality, speed, and cost. |
| **Lab guide** | [`slide-exercises/module-02/exercise-2.5-comparing-two-models.md`](slide-exercises/module-02/exercise-2.5-comparing-two-models.md) |
| **Slides** | `slides/module-02-marp.md` (Lesson 2.5) |
| **Related core exercise** | [`core-exercises/exercise-5/05-compare-two-models.md`](core-exercises/exercise-5/05-compare-two-models.md) |

**Slide sections covered:**
- Exercise 2.5 — Compare Two Models
- Exercise 2.5 — Comparison Table
- Exercise 2.5 — Cost & Decision Matrix
- Exercise 2.5 — Success Criteria

#### Lesson 2.6 — @mentions

**Time:** 13 min · **Type:** Exercise

**Exercise**

| Field | Detail |
|-------|--------|
| **Title** | Exercise 2.6: Precise Context with @mentions |
| **Lab time** | 13 min |
| **Difficulty** | Beginner |
| **Objective** | Use @mentions to point the Agent at exact files, symbols, and context. |
| **Lab guide** | [`slide-exercises/module-02/exercise-2.6-precise-context-with-mentions.md`](slide-exercises/module-02/exercise-2.6-precise-context-with-mentions.md) |
| **Slides** | `slides/module-02-marp.md` (Lesson 2.6) |
| **Related core exercise** | [`core-exercises/exercise-6/06-use-mentions.md`](core-exercises/exercise-6/06-use-mentions.md) |

**Slide sections covered:**
- Exercise 2.6 — Steps 1–2
- Exercise 2.6 — Step 3: Multiple @mentions
- Exercise 2.6 — Step 4: @branch
- Exercise 2.6 — Step 5: @chat
- Exercise 2.6 — Steps 6–7: @folder & @web
- Exercise 2.6 — Success Criteria

#### Lesson 2.7 — Checkpoints

**Time:** 8 min · **Type:** Exercise

**Exercise**

| Field | Detail |
|-------|--------|
| **Title** | Exercise 2.7: Checkpoints |
| **Lab time** | 8 min |
| **Difficulty** | Beginner |
| **Objective** | Create and restore checkpoints before risky Agent experiments. |
| **Lab guide** | [`slide-exercises/module-02/exercise-2.7-checkpoints.md`](slide-exercises/module-02/exercise-2.7-checkpoints.md) |
| **Slides** | `slides/module-02-marp.md` (Lesson 2.7) |
| **Related core exercise** | [`core-exercises/exercise-7/07-use-checkpoints.md`](core-exercises/exercise-7/07-use-checkpoints.md) |

**Slide sections covered:**
- Exercise 2.7 — Create & Restore
- Exercise 2.7 — Steps 2–3
- Exercise 2.7 — Steps 4–5

#### Lesson 2.8 — Terminal Integration

**Time:** 13 min · **Type:** Exercise

**Exercise**

| Field | Detail |
|-------|--------|
| **Title** | Exercise 2.8: Terminal Integration |
| **Lab time** | 13 min |
| **Difficulty** | Beginner |
| **Objective** | Let the Agent run terminal commands and react to command output. |
| **Lab guide** | [`slide-exercises/module-02/exercise-2.8-terminal-integration.md`](slide-exercises/module-02/exercise-2.8-terminal-integration.md) |
| **Slides** | `slides/module-02-marp.md` (Lesson 2.8) |
| **Related core exercise** | [`core-exercises/exercise-8/08-run-terminal-command.md`](core-exercises/exercise-8/08-run-terminal-command.md) |

**Slide sections covered:**
- Exercise 2.8 — Steps 1–3
- Exercise 2.8 — Agent Terminal Loop
- Exercise 2.8 — Step 5: Install Dependency
- Exercise 2.8 — Step 6: Multi-Step Workflow

---

## Module 3. Agent Modes and Tools

**Day:** Day 1 · **Duration:** ~60 minutes · **Format:** Hands-on exercise + concept

**Module goal:** Master different agent modes and the core tools that make agents powerful

**Prerequisites:** Module 2 completed, live web app available (or sample provided)

**Slide deck:** [`slides/module-03-marp.md`](slides/module-03-marp.md) · **HTML:** [`slides/module-03-marp.html`](slides/module-03-marp.html)

**Learning objectives**

- Choose between Ask Mode and Agent Mode based on task and safety needs
- Use the Browser Tool to inspect live pages and read console output
- Run terminal commands through the agent and diagnose failures
- Write effective, constrained prompts that avoid scope creep

### Lessons and exercises

#### Lesson 3.1 — Ask Mode vs. Agent Mode

**Time:** 18 min · **Type:** Exercise

**Exercise**

| Field | Detail |
|-------|--------|
| **Title** | Exercise 3.1: Ask Mode vs. Agent Mode |
| **Lab time** | 18 min |
| **Difficulty** | Beginner |
| **Objective** | Learn when Ask Mode is read-only and when Agent Mode can edit files. |
| **Lab guide** | [`slide-exercises/module-03/exercise-3.1-ask-mode-vs-agent-mode.md`](slide-exercises/module-03/exercise-3.1-ask-mode-vs-agent-mode.md) |
| **Slides** | `slides/module-03-marp.md` (Lesson 3.1) |
| **Related core exercise** | [`core-exercises/exercise-13/13-ask-mode-vs-agent-mode.md`](core-exercises/exercise-13/13-ask-mode-vs-agent-mode.md) |

**Slide sections covered:**
- Exercise 3.1 — Steps 1–2
- Exercise 3.1 — Steps 1–2 (Part 2)
- Exercise 3.1 — Steps 3–5
- Exercise 3.1 — Steps 3–5 (Part 2)
- Exercise 3.1 — Step 6 & Success Criteria

#### Lesson 3.2 — Browser Tool

**Time:** 18 min · **Type:** Exercise

**Exercise**

| Field | Detail |
|-------|--------|
| **Title** | Exercise 3.2: Browser Tool |
| **Lab time** | 18 min |
| **Difficulty** | Beginner |
| **Objective** | Use the Browser tool so the Agent can inspect live web pages. |
| **Lab guide** | [`slide-exercises/module-03/exercise-3.2-browser-tool.md`](slide-exercises/module-03/exercise-3.2-browser-tool.md) |
| **Slides** | `slides/module-03-marp.md` (Lesson 3.2) |
| **Related core exercise** | [`core-exercises/exercise-9/09-browser-tool-view-page.md`](core-exercises/exercise-9/09-browser-tool-view-page.md) |

**Slide sections covered:**
- Exercise 3.2 — Steps 1–2
- Exercise 3.2 — Steps 1–2 (Part 2)
- Exercise 3.2 — Steps 3–4
- Exercise 3.2 — Steps 3–4 (Part 2)
- Exercise 3.2 — Steps 5–6
- Exercise 3.2 — Steps 5–6 (Part 2)

#### Lesson 3.3 — Terminal Tool

**Time:** 20 min · **Type:** Exercise

**Exercise**

| Field | Detail |
|-------|--------|
| **Title** | Exercise 3.3: Terminal Tool |
| **Lab time** | 20 min |
| **Difficulty** | Beginner |
| **Objective** | Use the Terminal tool to run tests, read output, and fix failures. |
| **Lab guide** | [`slide-exercises/module-03/exercise-3.3-terminal-tool.md`](slide-exercises/module-03/exercise-3.3-terminal-tool.md) |
| **Slides** | `slides/module-03-marp.md` (Lesson 3.3) |
| **Related core exercise** | [`core-exercises/exercise-11/11-terminal-tool-run-tests.md`](core-exercises/exercise-11/11-terminal-tool-run-tests.md) |

**Slide sections covered:**
- Exercise 3.3 — Setup
- Exercise 3.3 — Step 1: Safe Command
- Exercise 3.3 — Step 2: Run Passing Tests
- Exercise 3.3 — Step 3: Break a Test
- Exercise 3.3 — Step 4: Diagnose Failure
- Exercise 3.3 — Step 5: Fix and Verify
- Exercise 3.3 — Step 6: Approval Rules

#### Lesson 3.4 — Effective Prompting in Practice

**Time:** 22 min · **Type:** Exercise

**Exercise**

| Field | Detail |
|-------|--------|
| **Title** | Exercise 3.4: Effective Prompting in Practice |
| **Lab time** | 22 min |
| **Difficulty** | Beginner |
| **Objective** | Write constrained prompts and reusable templates for real tasks. |
| **Lab guide** | [`slide-exercises/module-03/exercise-3.4-effective-prompting-in-practice.md`](slide-exercises/module-03/exercise-3.4-effective-prompting-in-practice.md) |
| **Slides** | `slides/module-03-marp.md` (Lesson 3.4) |
| **Related core exercise** | [`core-exercises/exercise-26/26-effective-prompting-in-practice.md`](core-exercises/exercise-26/26-effective-prompting-in-practice.md) |

**Slide sections covered:**
- Exercise 3.4 — Setup
- Exercise 3.4 — Step 1: Constrained Prompt
- Exercise 3.4 — Step 2: Vague vs. Constrained
- Exercise 3.4 — Step 3: Plan Before Editing
- Exercise 3.4 — Step 4: DO NOT List
- Exercise 3.4 — Step 5: One Change at a Time
- Exercise 3.4 — Step 6: Prompt Templates

---

## Module 4. Customizing Cursor for Your Team

**Day:** Day 1 · **Duration:** ~60 minutes · **Format:** Hands-on exercise + walkthrough

**Module goal:** Customize Cursor for team workflows with rules, skills, MCP, and subagents

**Prerequisites:** Modules 1–3 completed, team repository access, Cursor installed

**Slide deck:** [`slides/module-04-marp.md`](slides/module-04-marp.md) · **HTML:** [`slides/module-04-marp.html`](slides/module-04-marp.html)

**Learning objectives**

- Create Rules that encode team conventions and guardrails
- Write Repository Instructions for lightweight project guidance
- Build and invoke reusable Skills for specialized workflows
- Connect external tools via MCP and create slash workflows
- Understand when and how to use Subagents for delegation

### Lessons and exercises

#### Lesson 4.1 — Creating a Rule

**Time:** 20 min · **Type:** Exercise

**Exercise**

| Field | Detail |
|-------|--------|
| **Title** | Exercise 4.1: Creating a Rule |
| **Lab time** | 20 min |
| **Difficulty** | Beginner |
| **Objective** | Create Cursor rules that persist coding standards for your team. |
| **Lab guide** | [`slide-exercises/module-04/exercise-4.1-creating-a-rule.md`](slide-exercises/module-04/exercise-4.1-creating-a-rule.md) |
| **Slides** | `slides/module-04-marp.md` (Lesson 4.1) |
| **Related core exercise** | [`core-exercises/exercise-14/14-create-a-rule.md`](core-exercises/exercise-14/14-create-a-rule.md) |

**Slide sections covered:**
- Exercise 4.1 — Step 1: Setup
- Exercise 4.1 — Build & Test Rule
- Exercise 4.1 — Test & File-Specific Rules
- Exercise 4.1 — Test & File-Specific Rules (Part 2)

#### Lesson 4.2 — Repository Instructions

**Time:** 13 min · **Type:** Exercise

**Exercise**

| Field | Detail |
|-------|--------|
| **Title** | Exercise 4.2: Repository Instructions |
| **Lab time** | 13 min |
| **Difficulty** | Beginner |
| **Objective** | Add repository instructions the Agent reads automatically. |
| **Lab guide** | [`slide-exercises/module-04/exercise-4.2-repository-instructions.md`](slide-exercises/module-04/exercise-4.2-repository-instructions.md) |
| **Slides** | `slides/module-04-marp.md` (Lesson 4.2) |
| **Related core exercise** | [`core-exercises/exercise-15/15-use-agents-md.md`](core-exercises/exercise-15/15-use-agents-md.md) |

**Slide sections covered:**
- Exercise 4.2 — Create Instructions
- Exercise 4.2 — Verify & Maintain
- Exercise 4.2 — Verify & Maintain (Part 2)

#### Lesson 4.3 — Creating and Invoking a Skill

**Time:** 20 min · **Type:** Exercise

**Exercise**

| Field | Detail |
|-------|--------|
| **Title** | Exercise 4.3: Creating and Invoking a Skill |
| **Lab time** | 20 min |
| **Difficulty** | Beginner |
| **Objective** | Build and invoke reusable Agent skills for repeated workflows. |
| **Lab guide** | [`slide-exercises/module-04/exercise-4.3-creating-and-invoking-a-skill.md`](slide-exercises/module-04/exercise-4.3-creating-and-invoking-a-skill.md) |
| **Slides** | `slides/module-04-marp.md` (Lesson 4.3) |
| **Related core exercise** | [`core-exercises/exercise-16/16-create-a-skill.md`](core-exercises/exercise-16/16-create-a-skill.md) · [`core-exercises/exercise-17/17-invoke-a-skill.md`](core-exercises/exercise-17/17-invoke-a-skill.md) |

**Slide sections covered:**
- Exercise 4.3 — PR Review Skill
- Exercise 4.3 — Security Audit Skill
- Exercise 4.3 — Invoke Skills
- Exercise 4.3 — Invoke Skills (Part 2)
- Exercise 4.3 — Invoke Skills (Part 3)

#### Lesson 4.4 — MCP, Hooks, and Slash Workflows

**Time:** 10 min · **Type:** Walkthrough

**Walkthroughs:**
- MCP Configuration
- Slash Command Example

*Walkthrough-only lesson — no written slide exercise file.*

#### Lesson 4.5 — Subagents

**Time:** 6 min · **Type:** Walkthrough

**Walkthroughs:**
- Subagents in Action

*Walkthrough-only lesson — no written slide exercise file.*

---

## Module 5. Cursor CLI and Local Automation

**Day:** Day 1 · **Duration:** ~60 minutes · **Format:** Hands-on exercise

**Module goal:** Master the Cursor CLI for terminal-based AI workflows and automation

**Prerequisites:** Cursor CLI installed, terminal access, Modules 1–4 completed

**Slide deck:** [`slides/module-05-marp.md`](slides/module-05-marp.md) · **HTML:** [`slides/module-05-marp.html`](slides/module-05-marp.html)

**Learning objectives**

- Use the Cursor CLI in interactive mode for real-time AI collaboration
- Run one-shot CLI commands for scripting and CI/CD integration
- Hand off local sessions to Cloud Agents for remote execution
- List, resume, and manage concurrent sessions effectively

### Lessons and exercises

#### Lesson 5.1 — Interactive CLI

**Time:** 20 min · **Type:** Exercise

**Exercise**

| Field | Detail |
|-------|--------|
| **Title** | Exercise 5.1: Interactive CLI |
| **Lab time** | 20 min |
| **Difficulty** | Beginner |
| **Objective** | Start an interactive Cursor CLI session from the terminal. |
| **Lab guide** | [`slide-exercises/module-05/exercise-5.1-interactive-cli.md`](slide-exercises/module-05/exercise-5.1-interactive-cli.md) |
| **Slides** | `slides/module-05-marp.md` (Lesson 5.1) |
| **Related core exercise** | [`core-exercises/exercise-19/19-cli-interactive-mode.md`](core-exercises/exercise-19/19-cli-interactive-mode.md) |

**Slide sections covered:**
- Exercise 5.1 — Steps 1–2
- Exercise 5.1 — Steps 1–2 (Part 2)
- Exercise 5.1 — Steps 3–5
- Exercise 5.1 — Steps 3–5 (Part 2)
- Exercise 5.1 — Steps 3–5 (Part 3)
- Exercise 5.1 — Steps 6–7
- Exercise 5.1 — Steps 6–7 (Part 2)

#### Lesson 5.2 — One-Shot CLI

**Time:** 20 min · **Type:** Exercise

**Exercise**

| Field | Detail |
|-------|--------|
| **Title** | Exercise 5.2: One-Shot CLI |
| **Lab time** | 20 min |
| **Difficulty** | Beginner |
| **Objective** | Run single-shot Agent commands from scripts and CI. |
| **Lab guide** | [`slide-exercises/module-05/exercise-5.2-one-shot-cli.md`](slide-exercises/module-05/exercise-5.2-one-shot-cli.md) |
| **Slides** | `slides/module-05-marp.md` (Lesson 5.2) |
| **Related core exercise** | [`core-exercises/exercise-20/20-cli-one-shot-mode.md`](core-exercises/exercise-20/20-cli-one-shot-mode.md) |

**Slide sections covered:**
- Exercise 5.2 — Steps 1–2
- Exercise 5.2 — Steps 1–2 (Part 2)
- Exercise 5.2 — Scriptable Code Reviewer
- Exercise 5.2 — Batch & Git Hooks
- Exercise 5.2 — Batch & Git Hooks (Part 2)

#### Lesson 5.3 — Cloud Handoff

**Time:** 18 min · **Type:** Exercise

**Exercise**

| Field | Detail |
|-------|--------|
| **Title** | Exercise 5.3: Cloud Handoff |
| **Lab time** | 18 min |
| **Difficulty** | Beginner |
| **Objective** | Hand off a local CLI task to a Cloud Agent with &. |
| **Lab guide** | [`slide-exercises/module-05/exercise-5.3-cloud-handoff.md`](slide-exercises/module-05/exercise-5.3-cloud-handoff.md) |
| **Slides** | `slides/module-05-marp.md` (Lesson 5.3) |
| **Related core exercise** | [`core-exercises/exercise-21/21-cli-cloud-handoff.md`](core-exercises/exercise-21/21-cli-cloud-handoff.md) |

**Slide sections covered:**
- Exercise 5.3 — Steps 1–3
- Exercise 5.3 — Steps 1–3 (Part 2)
- Exercise 5.3 — Steps 1–3 (Part 3)
- Exercise 5.3 — Steps 4–6
- Exercise 5.3 — Steps 4–6 (Part 2)
- Exercise 5.3 — Steps 4–6 (Part 3)

#### Lesson 5.4 — Listing and Resuming Sessions

**Time:** 20 min · **Type:** Exercise

**Exercise**

| Field | Detail |
|-------|--------|
| **Title** | Exercise 5.4: Listing and Resuming Sessions |
| **Lab time** | 20 min |
| **Difficulty** | Beginner |
| **Objective** | List, name, resume, and compress CLI Agent sessions. |
| **Lab guide** | [`slide-exercises/module-05/exercise-5.4-listing-and-resuming-sessions.md`](slide-exercises/module-05/exercise-5.4-listing-and-resuming-sessions.md) |
| **Slides** | `slides/module-05-marp.md` (Lesson 5.4) |
| **Related core exercise** | [`core-exercises/exercise-22/22-cli-list-resume-sessions.md`](core-exercises/exercise-22/22-cli-list-resume-sessions.md) |

**Slide sections covered:**
- Exercise 5.4 — Steps 1–2
- Exercise 5.4 — Steps 1–2 (Part 2)
- Exercise 5.4 — Steps 3–5
- Exercise 5.4 — Steps 3–5 (Part 2)
- Exercise 5.4 — Steps 3–5 (Part 3)
- Exercise 5.4 — Steps 6–7 & Best Practices

---

## Module 6. Cloud Agents in the UI

**Day:** Day 2 · **Duration:** ~90 minutes · **Format:** Hands-on exercise + demonstration

**Module goal:** Master Cloud Agents UI for remote execution, artifact collection, and messaging integrations

**Prerequisites:** Cursor account, GitHub repository access, Modules 1–5 completed

**Slide deck:** [`slides/module-06-marp.md`](slides/module-06-marp.md) · **HTML:** [`slides/module-06-marp.html`](slides/module-06-marp.html)

**Learning objectives**

- Launch and monitor Cloud Agents from the Cursor UI
- Collect and download artifacts from completed cloud runs
- Trigger Cloud Agents from messaging platforms (Slack, Discord)
- Manage cloud agent history and settings

### Lessons and exercises

#### Lesson 6.1 — Launching a Cloud Agent

**Time:** 25 min · **Type:** Exercise

**Exercise**

| Field | Detail |
|-------|--------|
| **Title** | Exercise 6.1: Launching a Cloud Agent |
| **Lab time** | 25 min |
| **Difficulty** | Beginner |
| **Objective** | Launch a Cloud Agent from the Cursor UI and track its run. |
| **Lab guide** | [`slide-exercises/module-06/exercise-6.1-launching-a-cloud-agent.md`](slide-exercises/module-06/exercise-6.1-launching-a-cloud-agent.md) |
| **Slides** | `slides/module-06-marp.md` (Lesson 6.1) |
| **Related core exercise** | [`core-exercises/exercise-23/23-cloud-agent-web-dashboard.md`](core-exercises/exercise-23/23-cloud-agent-web-dashboard.md) |

**Slide sections covered:**
- Exercise 6.1 — Steps 1–2
- Exercise 6.1 — Steps 1–2 (Part 2)
- Exercise 6.1 — Steps 3–4
- Exercise 6.1 — Steps 3–4 (Part 2)
- Exercise 6.1 — Steps 5–6
- Exercise 6.1 — Steps 5–6 (Part 2)

#### Lesson 6.2 — Cloud Agent Artifacts

**Time:** 23 min · **Type:** Exercise

**Exercise**

| Field | Detail |
|-------|--------|
| **Title** | Exercise 6.2: Cloud Agent Artifacts |
| **Lab time** | 25 min |
| **Difficulty** | Beginner |
| **Objective** | Collect and download artifacts produced by Cloud Agents. |
| **Lab guide** | [`slide-exercises/module-06/exercise-6.2-cloud-agent-artifacts.md`](slide-exercises/module-06/exercise-6.2-cloud-agent-artifacts.md) |
| **Slides** | `slides/module-06-marp.md` (Lesson 6.2) |
| **Related core exercise** | [`core-exercises/exercise-25/25-cloud-agent-artifacts.md`](core-exercises/exercise-25/25-cloud-agent-artifacts.md) |

**Slide sections covered:**
- Exercise 6.2 — Steps 1–2
- Exercise 6.2 — Steps 1–2 (Part 2)
- Exercise 6.2 — Steps 3–5
- Exercise 6.2 — Steps 3–5 (Part 2)
- Exercise 6.2 — API Access
- Exercise 6.2 — CI/CD Integration

#### Lesson 6.3 — Cloud Agents from Messaging Platforms

**Time:** 20 min · **Type:** Demo

**Demonstrations:**
- Slack Integration
- Slack Usage
- Discord Integration

*Demonstration-only lesson — no written slide exercise file.*

---

## Module 7. Cursor API Foundations

**Day:** Day 2 · **Duration:** ~60 minutes · **Format:** Concept + hands-on exercise

**Module goal:** Understand the Cursor API ecosystem, authenticate securely, handle errors, and optimize requests

**Prerequisites:** Cursor account, basic API familiarity, Python 3.8+ installed

**Slide deck:** [`slides/module-07-marp.md`](slides/module-07-marp.md) · **HTML:** [`slides/module-07-marp.html`](slides/module-07-marp.html)

**Learning objectives**

- Identify the five Cursor APIs and their use cases
- Generate and securely manage API keys
- Implement rate limit handling and error recovery
- Use ETag caching for efficient repeat queries
- Test authentication by listing available models

### Lessons and exercises

#### Lesson 7.1 — The Cursor API Landscape

**Time:** 10 min · **Type:** Concept

*Concept-only lesson (API landscape overview) — hands-on exercises begin at Lesson 7.2.*

#### Lesson 7.2 — Authentication

**Time:** 20 min · **Type:** Exercise

**Exercise**

| Field | Detail |
|-------|--------|
| **Title** | Exercise 7.2: Generate and Test API Keys |
| **Lab time** | 15 min |
| **Difficulty** | Beginner |
| **Objective** | Create Admin and User API keys and verify authentication. |
| **Lab guide** | [`slide-exercises/module-07/exercise-7.2-generate-and-test-api-keys.md`](slide-exercises/module-07/exercise-7.2-generate-and-test-api-keys.md) |
| **Slides** | `slides/module-07-marp.md` (Lesson 7.2) |

**Slide sections covered:**
- Exercise 7.2 — Steps 1–3
- Exercise 7.2 — Steps 1–3 (Part 2)
- Exercise 7.2 — Steps 1–3 (Part 3)
- Exercise 7.2 — Steps 4–5
- Exercise 7.2 — Steps 4–5 (Part 2)
- Exercise 7.2 — Steps 6–7
- Exercise 7.2 — Steps 6–7 (Part 2)

#### Lesson 7.3 — Rate Limits and Error Handling

**Time:** 20 min · **Type:** Exercise

**Exercise**

| Field | Detail |
|-------|--------|
| **Title** | Exercise 7.3: Rate Limits and Error Handling |
| **Lab time** | 15 min |
| **Difficulty** | Beginner |
| **Objective** | Handle 429 responses with backoff and rate-limit headers. |
| **Lab guide** | [`slide-exercises/module-07/exercise-7.3-rate-limits-and-error-handling.md`](slide-exercises/module-07/exercise-7.3-rate-limits-and-error-handling.md) |
| **Slides** | `slides/module-07-marp.md` (Lesson 7.3) |

**Slide sections covered:**
- Exercise 7.3 — Exponential Backoff
- Exercise 7.3 — Rate Limiter & Client

#### Lesson 7.4 — ETag Caching

**Time:** 18 min · **Type:** Exercise

**Exercise**

| Field | Detail |
|-------|--------|
| **Title** | Exercise 7.4: ETag Caching |
| **Lab time** | 18 min |
| **Difficulty** | Beginner |
| **Objective** | Use ETags to avoid re-downloading unchanged API data. |
| **Lab guide** | [`slide-exercises/module-07/exercise-7.4-etag-caching.md`](slide-exercises/module-07/exercise-7.4-etag-caching.md) |
| **Slides** | `slides/module-07-marp.md` (Lesson 7.4) |

**Slide sections covered:**
- Exercise 7.4 — Basic ETag Usage
- Exercise 7.4 — ETagCache & CachedClient

#### Lesson 7.5 — Listing Available Models

**Time:** 10 min · **Type:** Exercise

**Exercise**

| Field | Detail |
|-------|--------|
| **Title** | Exercise 7.5: List Available Models |
| **Lab time** | 10 min |
| **Difficulty** | Beginner |
| **Objective** | Query available models and pick the right one programmatically. |
| **Lab guide** | [`slide-exercises/module-07/exercise-7.5-list-available-models.md`](slide-exercises/module-07/exercise-7.5-list-available-models.md) |
| **Slides** | `slides/module-07-marp.md` (Lesson 7.5) |

**Slide sections covered:**
- Exercise 7.5 — Steps 1–2
- Exercise 7.5 — Steps 1–2 (Part 2)
- Exercise 7.5 — Steps 3–4
- Exercise 7.5 — Steps 3–4 (Part 2)

---

## Module 8. Cloud Agents API and Webhooks

**Day:** Day 2 · **Duration:** ~60 minutes · **Format:** Hands-on exercise

**Module goal:** Programmatically create, stream, and manage Cloud Agents, and set up webhook notifications

**Prerequisites:** User API key (Module 7), Python 3.8+, ngrok installed, GitHub repository

**Slide deck:** [`slides/module-08-marp.md`](slides/module-08-marp.md) · **HTML:** [`slides/module-08-marp.html`](slides/module-08-marp.html)

**Learning objectives**

- Create a Cloud Agent programmatically using the API
- Stream agent responses in real-time using SSE with resume support
- List and download artifacts from a completed agent
- Create a webhook endpoint with HMAC verification
- Test webhooks locally using ngrok
- Build an end-to-end automated agent workflow

### Lessons and exercises

#### Lesson 8.1 — Creating a Cloud Agent Programmatically

**Time:** 15 min · **Type:** Exercise

**Exercise**

| Field | Detail |
|-------|--------|
| **Title** | Exercise 8.1: Create a Cloud Agent via API |
| **Lab time** | 15 min |
| **Difficulty** | Beginner |
| **Objective** | Create a Cloud Agent run using curl or Python. |
| **Lab guide** | [`slide-exercises/module-08/exercise-8.1-create-a-cloud-agent-via-api.md`](slide-exercises/module-08/exercise-8.1-create-a-cloud-agent-via-api.md) |
| **Slides** | `slides/module-08-marp.md` (Lesson 8.1) |

**Slide sections covered:**
- Exercise 8.1 — Create with curl
- Exercise 8.1 — Capture IDs
- Exercise 8.1 — Capture IDs (Part 2)
- Exercise 8.1 — Python Helper

#### Lesson 8.2 — Streaming Agent Responses (SSE)

**Time:** 15 min · **Type:** Exercise

**Exercise**

| Field | Detail |
|-------|--------|
| **Title** | Exercise 8.2: Stream Agent Responses (SSE) |
| **Lab time** | 15 min |
| **Difficulty** | Beginner |
| **Objective** | Stream Cloud Agent events with Server-Sent Events. |
| **Lab guide** | [`slide-exercises/module-08/exercise-8.2-stream-agent-responses-sse.md`](slide-exercises/module-08/exercise-8.2-stream-agent-responses-sse.md) |
| **Slides** | `slides/module-08-marp.md` (Lesson 8.2) |

**Slide sections covered:**
- Exercise 8.2 — Stream with curl
- Exercise 8.2 — Python SSE Client
- Exercise 8.2 — ResumableSSEClient

#### Lesson 8.3 — Listing and Downloading Artifacts

**Time:** 15 min · **Type:** Exercise

**Exercise**

| Field | Detail |
|-------|--------|
| **Title** | Exercise 8.3: List and Download Artifacts |
| **Lab time** | 15 min |
| **Difficulty** | Beginner |
| **Objective** | Wait for completion, list artifacts, and download outputs. |
| **Lab guide** | [`slide-exercises/module-08/exercise-8.3-list-and-download-artifacts.md`](slide-exercises/module-08/exercise-8.3-list-and-download-artifacts.md) |
| **Slides** | `slides/module-08-marp.md` (Lesson 8.3) |

**Slide sections covered:**
- Exercise 8.3 — Wait & List
- Exercise 8.3 — Download
- Exercise 8.3 — CI Integration

#### Lesson 8.4 — Creating a Webhook Endpoint

**Time:** 15 min · **Type:** Exercise

**Exercise**

| Field | Detail |
|-------|--------|
| **Title** | Exercise 8.4: Webhooks and HMAC Verification |
| **Lab time** | 15 min |
| **Difficulty** | Beginner |
| **Objective** | Receive webhooks and verify HMAC signatures. |
| **Lab guide** | [`slide-exercises/module-08/exercise-8.4-webhooks-and-hmac-verification.md`](slide-exercises/module-08/exercise-8.4-webhooks-and-hmac-verification.md) |
| **Slides** | `slides/module-08-marp.md` (Lesson 8.4) |

**Slide sections covered:**
- Exercise 8.4 — HMAC Verification
- Exercise 8.4 — Configure Agent

#### Lesson 8.5 — Testing Webhooks Locally with ngrok

**Time:** 13 min · **Type:** Exercise

**Exercise**

| Field | Detail |
|-------|--------|
| **Title** | Exercise 8.5: Test Webhooks with ngrok |
| **Lab time** | 15 min |
| **Difficulty** | Beginner |
| **Objective** | Expose a local server with ngrok and inspect webhook payloads. |
| **Lab guide** | [`slide-exercises/module-08/exercise-8.5-test-webhooks-with-ngrok.md`](slide-exercises/module-08/exercise-8.5-test-webhooks-with-ngrok.md) |
| **Slides** | `slides/module-08-marp.md` (Lesson 8.5) |

**Slide sections covered:**
- Exercise 8.5 — Steps 1–3
- Exercise 8.5 — Steps 1–3 (Part 2)
- Exercise 8.5 — Steps 1–3 (Part 3)
- Exercise 8.5 — Inspect & Replay

#### Lesson 8.6 — End-to-End Automated Agent Workflow

**Time:** 17 min · **Type:** Concept

*Capstone integration exercise covered in slide deck — no separate slide-exercises file.*

---

## Module 9. Admin and Analytics APIs

**Day:** Day 2 · **Duration:** ~75 minutes · **Format:** Hands-on exercise + demonstrations

**Module goal:** Master team management, usage analytics, cost governance, and safe admin operations

**Prerequisites:** Admin API key (not User key), Python 3.8+, Modules 7–8 completed

**Slide deck:** [`slides/module-09-marp.md`](slides/module-09-marp.md) · **HTML:** [`slides/module-09-marp.html`](slides/module-09-marp.html)

**Learning objectives**

- List and manage team members programmatically
- Retrieve daily usage data for cost tracking and reporting
- Set user spend limits for budget governance
- Analyze model usage for cost optimization insights
- Track daily active users for leadership reporting
- Build responsible leaderboards without privacy violations
- Analyze conversation intent and complexity (demonstration)
- Safely remove team members with proper patterns (demonstration)

### Lessons and exercises

#### Lesson 9.1 — Listing Team Members

**Time:** 8 min · **Type:** Exercise

**Exercise**

| Field | Detail |
|-------|--------|
| **Title** | Exercise 9.1: List Team Members |
| **Lab time** | 13 min |
| **Difficulty** | Beginner |
| **Objective** | List team members with pagination and export to CSV. |
| **Lab guide** | [`slide-exercises/module-09/exercise-9.1-list-team-members.md`](slide-exercises/module-09/exercise-9.1-list-team-members.md) |
| **Slides** | `slides/module-09-marp.md` (Lesson 9.1) |

**Slide sections covered:**
- Exercise 9.1 — Setup & List
- Exercise 9.1 — Pagination & Export

#### Lesson 9.2 — Daily Usage Data

**Time:** 15 min · **Type:** Exercise

**Exercise**

| Field | Detail |
|-------|--------|
| **Title** | Exercise 9.2: Daily Usage Data |
| **Lab time** | 15 min |
| **Difficulty** | Beginner |
| **Objective** | Pull daily usage and build a weekly cost report. |
| **Lab guide** | [`slide-exercises/module-09/exercise-9.2-daily-usage-data.md`](slide-exercises/module-09/exercise-9.2-daily-usage-data.md) |
| **Slides** | `slides/module-09-marp.md` (Lesson 9.2) |

**Slide sections covered:**
- Exercise 9.2 — Weekly Usage
- Exercise 9.2 — Cost Report

#### Lesson 9.3 — Setting User Spend Limits

**Time:** 8 min · **Type:** Exercise

**Exercise**

| Field | Detail |
|-------|--------|
| **Title** | Exercise 9.3: Set User Spend Limits |
| **Lab time** | 13 min |
| **Difficulty** | Beginner |
| **Objective** | Set and bulk-update per-user spending limits. |
| **Lab guide** | [`slide-exercises/module-09/exercise-9.3-set-user-spend-limits.md`](slide-exercises/module-09/exercise-9.3-set-user-spend-limits.md) |
| **Slides** | `slides/module-09-marp.md` (Lesson 9.3) |

**Slide sections covered:**
- Exercise 9.3 — Set Limits
- Exercise 9.3 — Bulk Limits

#### Lesson 9.4 — Model Usage Analytics

**Time:** 8 min · **Type:** Exercise

**Exercise**

| Field | Detail |
|-------|--------|
| **Title** | Exercise 9.4: Model Usage Analytics |
| **Lab time** | 13 min |
| **Difficulty** | Beginner |
| **Objective** | Analyze model usage and identify optimization opportunities. |
| **Lab guide** | [`slide-exercises/module-09/exercise-9.4-model-usage-analytics.md`](slide-exercises/module-09/exercise-9.4-model-usage-analytics.md) |
| **Slides** | `slides/module-09-marp.md` (Lesson 9.4) |

**Slide sections covered:**
- Exercise 9.4 — Model Breakdown
- Exercise 9.4 — Optimization Report

#### Lesson 9.5 — Daily Active Users

**Time:** 6 min · **Type:** Exercise

**Exercise**

| Field | Detail |
|-------|--------|
| **Title** | Exercise 9.5: Daily Active Users (DAU) |
| **Lab time** | 10 min |
| **Difficulty** | Beginner |
| **Objective** | Report daily active users over a date range. |
| **Lab guide** | [`slide-exercises/module-09/exercise-9.5-daily-active-users-dau.md`](slide-exercises/module-09/exercise-9.5-daily-active-users-dau.md) |
| **Slides** | `slides/module-09-marp.md` (Lesson 9.5) |

**Slide sections covered:**
- Exercise 9.5 — DAU Report

#### Lesson 9.6 — Leaderboards

**Time:** 6 min · **Type:** Exercise

**Exercise**

| Field | Detail |
|-------|--------|
| **Title** | Exercise 9.6: Leaderboards |
| **Lab time** | 11 min |
| **Difficulty** | Beginner |
| **Objective** | Build leaderboards for tabs, AI lines, and agent runs. |
| **Lab guide** | [`slide-exercises/module-09/exercise-9.6-leaderboards.md`](slide-exercises/module-09/exercise-9.6-leaderboards.md) |
| **Slides** | `slides/module-09-marp.md` (Lesson 9.6) |

**Slide sections covered:**
- Exercise 9.6 — Three Leaderboards

#### Lesson 9.7 — Conversation Insights

**Time:** 6 min · **Type:** Demo

**Demonstrations:**
- Intent Analysis
- Complexity & Categories

*Demonstration-only lesson — no written slide exercise file.*

#### Lesson 9.8 — Destructive Admin Operations

**Time:** 6 min · **Type:** Demo

**Demonstrations:**
- SafeRemovalDemo Workflow

*Demonstration-only lesson — no written slide exercise file.*

---

## Module 10. AI Code Tracking and Reporting

**Day:** Day 2 · **Duration:** ~20 minutes (plus take-home project) · **Format:** Hands-on exercise + take-home project

**Module goal:** Track AI vs. human contributions, export metrics to BI tools, build compliance dashboards

**Prerequisites:** Admin API key, Git repository access, Modules 8–9 completed

**Slide deck:** [`slides/module-10-marp.md`](slides/module-10-marp.md) · **HTML:** [`slides/module-10-marp.html`](slides/module-10-marp.html)

**Learning objectives**

- Attribute AI vs. human contributions per commit
- Stream metrics to BI tools via CSV export
- Access granular AI change events for compliance
- Build a complete reporting dashboard combining all data sources

### Lessons and exercises

#### Lesson 10.1 — AI Commit Metrics

**Time:** 8 min · **Type:** Exercise

**Exercise**

| Field | Detail |
|-------|--------|
| **Title** | Exercise 10.1: AI Commit Metrics |
| **Lab time** | 8 min |
| **Difficulty** | Beginner |
| **Objective** | Fetch AI commit metrics and calculate contribution percentage. |
| **Lab guide** | [`slide-exercises/module-10/exercise-10.1-ai-commit-metrics.md`](slide-exercises/module-10/exercise-10.1-ai-commit-metrics.md) |
| **Slides** | `slides/module-10-marp.md` (Lesson 10.1) |

**Slide sections covered:**
- Exercise 10.1 — Fetch Metrics
- Exercise 10.1 — AI Contribution %
- Exercise 10.1 — ROI Analysis

#### Lesson 10.2 — Bulk Export via CSV Streaming

**Time:** 7 min · **Type:** Exercise

**Exercise**

| Field | Detail |
|-------|--------|
| **Title** | Exercise 10.2: Bulk Export via CSV Streaming |
| **Lab time** | 7 min |
| **Difficulty** | Beginner |
| **Objective** | Stream large CSV exports for BI tools. |
| **Lab guide** | [`slide-exercises/module-10/exercise-10.2-bulk-export-via-csv-streaming.md`](slide-exercises/module-10/exercise-10.2-bulk-export-via-csv-streaming.md) |
| **Slides** | `slides/module-10-marp.md` (Lesson 10.2) |

**Slide sections covered:**
- Exercise 10.2 — Stream to File
- Exercise 10.2 — BI Integration

#### Lesson 10.3 — Granular AI Change Events

**Time:** 7 min · **Type:** Exercise

**Exercise**

| Field | Detail |
|-------|--------|
| **Title** | Exercise 10.3: Granular AI Change Events |
| **Lab time** | 7 min |
| **Difficulty** | Beginner |
| **Objective** | Query per-change AI events for compliance reporting. |
| **Lab guide** | [`slide-exercises/module-10/exercise-10.3-granular-ai-change-events.md`](slide-exercises/module-10/exercise-10.3-granular-ai-change-events.md) |
| **Slides** | `slides/module-10-marp.md` (Lesson 10.3) |

**Slide sections covered:**
- Exercise 10.3 — Query Events
- Exercise 10.3 — Compliance Report

#### Lesson 10.4 — Reporting Dashboard Architecture

**Time:** 4 min + take-home · **Type:** Exercise

**Exercise**

| Field | Detail |
|-------|--------|
| **Title** | Exercise 10.4: Reporting Dashboard Architecture |
| **Lab time** | Take-home |
| **Difficulty** | Beginner |
| **Objective** | Design a leadership dashboard combining analytics APIs. |
| **Lab guide** | [`slide-exercises/module-10/exercise-10.4-reporting-dashboard-architecture.md`](slide-exercises/module-10/exercise-10.4-reporting-dashboard-architecture.md) |
| **Slides** | `slides/module-10-marp.md` (Lesson 10.4) |

**Slide sections covered:**
- Exercise 10.4 — Dashboard Components
- Exercise 10.4 — Streamlit Dashboard
- Exercise 10.4 — Deliverables

**Note:** Take-home lab — full step-by-step instructions are in the lab guide.

---

## Slide Exercise Master Index

All hands-on lab guides under `slide-exercises/`, sorted by module.

| Exercise | Title | Module | Time | Difficulty | Lab guide |
|----------|-------|--------|------|------------|-----------|
| **2.1** | Codebase Understanding | — | 20 min | Beginner | [`exercise-2.1-codebase-understanding.md`](slide-exercises/module-02/exercise-2.1-codebase-understanding.md) |
| **2.2** | Explaining a Specific File or Symbol | — | 13 min | Beginner | [`exercise-2.2-explaining-a-specific-file-or-symbol.md`](slide-exercises/module-02/exercise-2.2-explaining-a-specific-file-or-symbol.md) |
| **2.3** | Making a Safe, Reviewable Change | — | 13 min | Beginner | [`exercise-2.3-making-a-safe-reviewable-change.md`](slide-exercises/module-02/exercise-2.3-making-a-safe-reviewable-change.md) |
| **2.4** | Plan Mode | — | 13 min | Beginner | [`exercise-2.4-plan-mode.md`](slide-exercises/module-02/exercise-2.4-plan-mode.md) |
| **2.5** | Comparing Two Models | — | 13 min | Beginner | [`exercise-2.5-comparing-two-models.md`](slide-exercises/module-02/exercise-2.5-comparing-two-models.md) |
| **2.6** | Precise Context with @mentions | — | 13 min | Beginner | [`exercise-2.6-precise-context-with-mentions.md`](slide-exercises/module-02/exercise-2.6-precise-context-with-mentions.md) |
| **2.7** | Checkpoints | — | 8 min | Beginner | [`exercise-2.7-checkpoints.md`](slide-exercises/module-02/exercise-2.7-checkpoints.md) |
| **2.8** | Terminal Integration | — | 13 min | Beginner | [`exercise-2.8-terminal-integration.md`](slide-exercises/module-02/exercise-2.8-terminal-integration.md) |
| **3.1** | Ask Mode vs. Agent Mode | — | 18 min | Beginner | [`exercise-3.1-ask-mode-vs-agent-mode.md`](slide-exercises/module-03/exercise-3.1-ask-mode-vs-agent-mode.md) |
| **3.2** | Browser Tool | — | 18 min | Beginner | [`exercise-3.2-browser-tool.md`](slide-exercises/module-03/exercise-3.2-browser-tool.md) |
| **3.3** | Terminal Tool | — | 20 min | Beginner | [`exercise-3.3-terminal-tool.md`](slide-exercises/module-03/exercise-3.3-terminal-tool.md) |
| **3.4** | Effective Prompting in Practice | — | 22 min | Beginner | [`exercise-3.4-effective-prompting-in-practice.md`](slide-exercises/module-03/exercise-3.4-effective-prompting-in-practice.md) |
| **4.1** | Creating a Rule | — | 20 min | Beginner | [`exercise-4.1-creating-a-rule.md`](slide-exercises/module-04/exercise-4.1-creating-a-rule.md) |
| **4.2** | Repository Instructions | — | 13 min | Beginner | [`exercise-4.2-repository-instructions.md`](slide-exercises/module-04/exercise-4.2-repository-instructions.md) |
| **4.3** | Creating and Invoking a Skill | — | 20 min | Beginner | [`exercise-4.3-creating-and-invoking-a-skill.md`](slide-exercises/module-04/exercise-4.3-creating-and-invoking-a-skill.md) |
| **5.1** | Interactive CLI | — | 20 min | Beginner | [`exercise-5.1-interactive-cli.md`](slide-exercises/module-05/exercise-5.1-interactive-cli.md) |
| **5.2** | One-Shot CLI | — | 20 min | Beginner | [`exercise-5.2-one-shot-cli.md`](slide-exercises/module-05/exercise-5.2-one-shot-cli.md) |
| **5.3** | Cloud Handoff | — | 18 min | Beginner | [`exercise-5.3-cloud-handoff.md`](slide-exercises/module-05/exercise-5.3-cloud-handoff.md) |
| **5.4** | Listing and Resuming Sessions | — | 20 min | Beginner | [`exercise-5.4-listing-and-resuming-sessions.md`](slide-exercises/module-05/exercise-5.4-listing-and-resuming-sessions.md) |
| **6.1** | Launching a Cloud Agent | — | 25 min | Beginner | [`exercise-6.1-launching-a-cloud-agent.md`](slide-exercises/module-06/exercise-6.1-launching-a-cloud-agent.md) |
| **6.2** | Cloud Agent Artifacts | — | 25 min | Beginner | [`exercise-6.2-cloud-agent-artifacts.md`](slide-exercises/module-06/exercise-6.2-cloud-agent-artifacts.md) |
| **7.2** | Generate and Test API Keys | — | 15 min | Beginner | [`exercise-7.2-generate-and-test-api-keys.md`](slide-exercises/module-07/exercise-7.2-generate-and-test-api-keys.md) |
| **7.3** | Rate Limits and Error Handling | — | 15 min | Beginner | [`exercise-7.3-rate-limits-and-error-handling.md`](slide-exercises/module-07/exercise-7.3-rate-limits-and-error-handling.md) |
| **7.4** | ETag Caching | — | 18 min | Beginner | [`exercise-7.4-etag-caching.md`](slide-exercises/module-07/exercise-7.4-etag-caching.md) |
| **7.5** | List Available Models | — | 10 min | Beginner | [`exercise-7.5-list-available-models.md`](slide-exercises/module-07/exercise-7.5-list-available-models.md) |
| **8.1** | Create a Cloud Agent via API | — | 15 min | Beginner | [`exercise-8.1-create-a-cloud-agent-via-api.md`](slide-exercises/module-08/exercise-8.1-create-a-cloud-agent-via-api.md) |
| **8.2** | Stream Agent Responses (SSE) | — | 15 min | Beginner | [`exercise-8.2-stream-agent-responses-sse.md`](slide-exercises/module-08/exercise-8.2-stream-agent-responses-sse.md) |
| **8.3** | List and Download Artifacts | — | 15 min | Beginner | [`exercise-8.3-list-and-download-artifacts.md`](slide-exercises/module-08/exercise-8.3-list-and-download-artifacts.md) |
| **8.4** | Webhooks and HMAC Verification | — | 15 min | Beginner | [`exercise-8.4-webhooks-and-hmac-verification.md`](slide-exercises/module-08/exercise-8.4-webhooks-and-hmac-verification.md) |
| **8.5** | Test Webhooks with ngrok | — | 15 min | Beginner | [`exercise-8.5-test-webhooks-with-ngrok.md`](slide-exercises/module-08/exercise-8.5-test-webhooks-with-ngrok.md) |
| **9.1** | List Team Members | — | 13 min | Beginner | [`exercise-9.1-list-team-members.md`](slide-exercises/module-09/exercise-9.1-list-team-members.md) |
| **9.2** | Daily Usage Data | — | 15 min | Beginner | [`exercise-9.2-daily-usage-data.md`](slide-exercises/module-09/exercise-9.2-daily-usage-data.md) |
| **9.3** | Set User Spend Limits | — | 13 min | Beginner | [`exercise-9.3-set-user-spend-limits.md`](slide-exercises/module-09/exercise-9.3-set-user-spend-limits.md) |
| **9.4** | Model Usage Analytics | — | 13 min | Beginner | [`exercise-9.4-model-usage-analytics.md`](slide-exercises/module-09/exercise-9.4-model-usage-analytics.md) |
| **9.5** | Daily Active Users (DAU) | — | 10 min | Beginner | [`exercise-9.5-daily-active-users-dau.md`](slide-exercises/module-09/exercise-9.5-daily-active-users-dau.md) |
| **9.6** | Leaderboards | — | 11 min | Beginner | [`exercise-9.6-leaderboards.md`](slide-exercises/module-09/exercise-9.6-leaderboards.md) |
| **10.1** | AI Commit Metrics | — | 8 min | Beginner | [`exercise-10.1-ai-commit-metrics.md`](slide-exercises/module-10/exercise-10.1-ai-commit-metrics.md) |
| **10.2** | Bulk Export via CSV Streaming | — | 7 min | Beginner | [`exercise-10.2-bulk-export-via-csv-streaming.md`](slide-exercises/module-10/exercise-10.2-bulk-export-via-csv-streaming.md) |
| **10.3** | Granular AI Change Events | — | 7 min | Beginner | [`exercise-10.3-granular-ai-change-events.md`](slide-exercises/module-10/exercise-10.3-granular-ai-change-events.md) |
| **10.4** | Reporting Dashboard Architecture | — | Take-home | Beginner | [`exercise-10.4-reporting-dashboard-architecture.md`](slide-exercises/module-10/exercise-10.4-reporting-dashboard-architecture.md) |

---

## Core Exercises Cross-Reference

Optional calculator-based labs in `core-exercises/` that align with slide exercises (Modules 2–6). See [`core-exercises/optional-core-exercises-guide.md`](core-exercises/optional-core-exercises-guide.md) for essential vs. optional guidance.

| Slide exercise | Core exercise | Path |
|----------------|---------------|------|
| **2.1** | exercise-1 | [`core-exercises/exercise-1/01-open-agent-first-prompt.md`](core-exercises/exercise-1/01-open-agent-first-prompt.md) |
| **2.2** | exercise-2 | [`core-exercises/exercise-2/02-explain-a-specific-file.md`](core-exercises/exercise-2/02-explain-a-specific-file.md) |
| **2.3** | exercise-3 | [`core-exercises/exercise-3/03-make-a-safe-change.md`](core-exercises/exercise-3/03-make-a-safe-change.md) |
| **2.4** | exercise-4 | [`core-exercises/exercise-4/04-use-plan-mode.md`](core-exercises/exercise-4/04-use-plan-mode.md) |
| **2.5** | exercise-5 | [`core-exercises/exercise-5/05-compare-two-models.md`](core-exercises/exercise-5/05-compare-two-models.md) |
| **2.6** | exercise-6 | [`core-exercises/exercise-6/06-use-mentions.md`](core-exercises/exercise-6/06-use-mentions.md) |
| **2.7** | exercise-7 | [`core-exercises/exercise-7/07-use-checkpoints.md`](core-exercises/exercise-7/07-use-checkpoints.md) |
| **2.8** | exercise-8 | [`core-exercises/exercise-8/08-run-terminal-command.md`](core-exercises/exercise-8/08-run-terminal-command.md) |
| **3.1** | exercise-13 | [`core-exercises/exercise-13/13-ask-mode-vs-agent-mode.md`](core-exercises/exercise-13/13-ask-mode-vs-agent-mode.md) |
| **3.2** | exercise-9 | [`core-exercises/exercise-9/09-browser-tool-view-page.md`](core-exercises/exercise-9/09-browser-tool-view-page.md) |
| **3.3** | exercise-11 | [`core-exercises/exercise-11/11-terminal-tool-run-tests.md`](core-exercises/exercise-11/11-terminal-tool-run-tests.md) |
| **4.1** | exercise-14 | [`core-exercises/exercise-14/14-create-a-rule.md`](core-exercises/exercise-14/14-create-a-rule.md) |
| **4.2** | exercise-15 | [`core-exercises/exercise-15/15-use-agents-md.md`](core-exercises/exercise-15/15-use-agents-md.md) |
| **4.3** | exercise-16 | [`core-exercises/exercise-16/16-create-a-skill.md`](core-exercises/exercise-16/16-create-a-skill.md) |
| **5.1** | exercise-19 | [`core-exercises/exercise-19/19-cli-interactive-mode.md`](core-exercises/exercise-19/19-cli-interactive-mode.md) |
| **5.2** | exercise-20 | [`core-exercises/exercise-20/20-cli-one-shot-mode.md`](core-exercises/exercise-20/20-cli-one-shot-mode.md) |
| **5.3** | exercise-21 | [`core-exercises/exercise-21/21-cli-cloud-handoff.md`](core-exercises/exercise-21/21-cli-cloud-handoff.md) |
| **5.4** | exercise-22 | [`core-exercises/exercise-22/22-cli-list-resume-sessions.md`](core-exercises/exercise-22/22-cli-list-resume-sessions.md) |
| **6.1** | exercise-23 | [`core-exercises/exercise-23/23-cloud-agent-web-dashboard.md`](core-exercises/exercise-23/23-cloud-agent-web-dashboard.md) |
| **6.2** | exercise-25 | [`core-exercises/exercise-25/25-cloud-agent-artifacts.md`](core-exercises/exercise-25/25-cloud-agent-artifacts.md) |

**Additional core exercises** (no direct slide-exercise counterpart in this repo):

| Core # | Title | Path |
|--------|-------|------|
| **10** | Browser Tool — Read Console | [`core-exercises/exercise-10/10-browser-tool-read-console.md`](core-exercises/exercise-10/10-browser-tool-read-console.md) |
| **12** | Terminal Tool — Fix Errors | [`core-exercises/exercise-12/12-terminal-tool-fix-errors.md`](core-exercises/exercise-12/12-terminal-tool-fix-errors.md) |
| **17** | Invoke a Skill | [`core-exercises/exercise-17/17-invoke-a-skill.md`](core-exercises/exercise-17/17-invoke-a-skill.md) |
| **18** | Create a Subagent | [`core-exercises/exercise-18/18-create-a-subagent.md`](core-exercises/exercise-18/18-create-a-subagent.md) |
| **24** | Cloud Agent from Slack | [`core-exercises/exercise-24/24-cloud-agent-from-slack.md`](core-exercises/exercise-24/24-cloud-agent-from-slack.md) |

---

## Supporting Materials

| Resource | Location | Description |
|----------|----------|-------------|
| Original TOC | [`TABLE_OF_CONTENTS.md`](TABLE_OF_CONTENTS.md) | High-level program overview and sample schedule |
| Combined slide deck | [`slides/course-complete-marp.md`](slides/course-complete-marp.md) | All modules in one Marp file |
| Module source docs | [`modules-basedon-toc/`](modules-basedon-toc/) | Module planning documents (modules 1–10) |
| Learn readmes | [`learn/learn-readmes-index.md`](learn/learn-readmes-index.md) | Curated concept reading paths |
| API content readmes | [`api-content-readmes/api-content-readmes-index.md`](api-content-readmes/api-content-readmes-index.md) | API reference reading paths |
| Docs content readmes | [`docs-content-readmes/docs-content-readmes-index.md`](docs-content-readmes/docs-content-readmes-index.md) | Cursor docs reading paths |
| Core exercises guide | [`core-exercises/optional-core-exercises-guide.md`](core-exercises/optional-core-exercises-guide.md) | Essential vs. optional exercise recommendations |

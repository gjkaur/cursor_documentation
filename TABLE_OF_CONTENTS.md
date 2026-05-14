# Cursor Training Program — Table of Contents

A 2-day, hands-on training program that equips working software professionals to use the **Cursor AI code editor** and the **Cursor APIs** confidently, safely, and at production quality.

---

## At a Glance

| | |
|---|---|
| **Duration** | 2 days |
| **Format** | ~70% hands-on exercises, ~30% concept and discussion |
| **Modules** | 10 total — 4 on Day 1, 6 on Day 2 |
| **Approach** | Short concept block → hands-on exercise → review and discussion |

**Day 1 — Cursor Editor and Agent Fluency.** Mental models, the editor, agent tools, and customization.

**Day 2 — Automation and Integration.** CLI, Cloud Agents, and the Cursor APIs (Cloud Agents, Admin, Analytics, AI Code Tracking, Webhooks).

---

## Audience

**Primary.** Software engineers, tech leads, and senior developers using Cursor day-to-day.

**Secondary.** Platform engineers, DevOps, enterprise admins, automation and integration engineers, BI and data engineers.

---

## Prerequisites

- Working experience as a software engineer in any language.
- Cursor installed and signed in (assistance provided during setup).
- A Git repository to experiment in (sample repos provided if needed).
- Ability to generate a Cursor API key.
- Enterprise plan recommended for Modules 9 and 10. All other modules work on any plan.

---

## Program Goals

By the end of the program, participants will be able to:

- Reason confidently about how AI models work, why outputs vary, and how to spot hallucinations.
- Manage context, tools, and agents to produce reliable engineering outcomes.
- Use the Cursor editor and Agent for day-to-day work, including understanding codebases, shipping features, debugging, reviewing, and testing.
- Customize Cursor to a team or repository using Rules, Skills, and Hooks.
- Operate Cursor outside the IDE via the CLI and Cloud Agents.
- Build production-grade integrations on top of the Cursor APIs.

---

## Module Index

| #  | Day   | Module                                       | Format                                  | Duration |
|----|-------|----------------------------------------------|-----------------------------------------|----------|
| 1  | Day 1 | Mental Models for AI-Assisted Development    | Concept block                           | ~60 min  |
| 2  | Day 1 | Cursor Editor Essentials                     | Hands-on exercise                       | ~90 min  |
| 3  | Day 1 | Agent Modes and Tools                        | Hands-on exercise + concept             | ~60 min  |
| 4  | Day 1 | Customizing Cursor for Your Team             | Hands-on exercise + walkthrough         | ~60 min  |
| 5  | Day 2 | Cursor CLI and Local Automation              | Hands-on exercise                       | ~60 min  |
| 6  | Day 2 | Cloud Agents in the UI                       | Hands-on exercise + demonstration       | ~90 min  |
| 7  | Day 2 | Cursor API Foundations                       | Concept + hands-on exercise             | ~60 min  |
| 8  | Day 2 | Cloud Agents API and Webhooks                | Hands-on exercise                       | ~60 min  |
| 9  | Day 2 | Admin and Analytics APIs                     | Hands-on exercise + demonstrations      | ~75 min  |
| 10 | Day 2 | AI Code Tracking and Reporting               | Hands-on exercise + take-home project   | ~20 min  |

---

## Day 1 — Cursor Editor and Agent Fluency

**By the end of Day 1, participants will be able to:**

- Explain how AI models work and identify hallucinations in real outputs.
- Navigate and modify an unfamiliar codebase using the Cursor Agent.
- Use Plan Mode to design changes before implementing them.
- Choose appropriate models and use checkpoints to experiment safely.
- Switch fluidly between Ask Mode and Agent Mode, and use the browser and terminal tools.
- Customize Cursor with Rules, Skills, and project-level instructions.

### Module 1. Mental Models for AI-Assisted Development

*Format: Concept block. Duration: ~60 minutes.*

**Topics**

- **1.1 How AI Models Work.** Why AI outputs are probabilistic and what determines them.
- **1.2 Hallucinations.** Why models invent things and how to spot it in coding contexts.
- **1.3 Tokens and Pricing.** What you actually pay for and how to keep costs predictable.
- **1.4 Context.** Managing what the model sees, the single most valuable AI skill.
- **1.5 Tool Calling and MCP.** How models take real actions through external tools.
- **1.6 Agents.** What an agent is and how it changes the developer's role.

### Module 2. Cursor Editor Essentials

*Format: Hands-on exercise. Duration: ~90 minutes.*

**Topics**

- **2.1 Codebase Understanding.** Orient an agent to an unfamiliar repository.
- **2.2 Explaining a Specific File or Symbol.** Targeted code explanations using precise context.
- **2.3 Making a Safe, Reviewable Change.** Diff review and approval workflow.
- **2.4 Plan Mode.** Designing complex changes before implementation.
- **2.5 Comparing Two Models.** Choosing the right model for the task.
- **2.6 Precise Context with @mentions.** Pointing the agent at exact files, symbols, branches, and past chats.
- **2.7 Checkpoints.** A safety net for experimental changes.
- **2.8 Terminal Integration.** Letting the agent run and react to commands.

### Module 3. Agent Modes and Tools

*Format: Hands-on exercise + concept. Duration: ~60 minutes.*

**Topics**

- **3.1 Ask Mode vs. Agent Mode.** When each is appropriate and the safety implications.
- **3.2 Browser Tool.** Inspecting a live page and reading the console.
- **3.3 Terminal Tool.** Running tests and diagnosing real failures.
- **3.4 Effective Prompting in Practice.** Constrained prompts and avoiding scope creep.

### Module 4. Customizing Cursor for Your Team

*Format: Hands-on exercise + walkthrough. Duration: ~60 minutes.*

**Topics**

- **4.1 Creating a Rule.** Encoding team conventions, build commands, and guardrails.
- **4.2 Repository Instructions.** Lightweight project-level guidance.
- **4.3 Creating and Invoking a Skill.** Building and using a reusable specialized workflow.
- **4.4 MCP, Hooks, and Slash Workflows.** Connecting external tools and shipping team commands *(walkthrough).*
- **4.5 Subagents.** A brief look at delegating specialized work to focused sub-agents *(walkthrough).*

### Day 1 Wrap-up

Q&A and a guided recap of the mental models from Module 1.

---

## Day 2 — Automation and Integration

**By the end of Day 2, participants will be able to:**

- Use the Cursor CLI for interactive sessions and CI-friendly scripts.
- Launch, monitor, and collect outputs from Cloud Agents in the UI.
- Authenticate against the Cursor APIs and handle rate limits and errors.
- Launch Cloud Agents programmatically and integrate them via webhooks.
- Pull team usage, spend, and adoption metrics from the Admin and Analytics APIs.
- Measure AI attribution per commit and design a reporting dashboard.

### Module 5. Cursor CLI and Local Automation

*Format: Hands-on exercise. Duration: ~60 minutes.*

**Topics**

- **5.1 Interactive CLI.** Using Cursor from the terminal.
- **5.2 One-Shot CLI.** Scripting and CI-friendly invocation.
- **5.3 Cloud Handoff.** Moving a local session to the cloud.
- **5.4 Listing and Resuming Sessions.** Managing concurrent work.

### Module 6. Cloud Agents in the UI

*Format: Hands-on exercise + demonstration. Duration: ~90 minutes.*

**Topics**

- **6.1 Launching a Cloud Agent.** The core remote execution capability.
- **6.2 Cloud Agent Artifacts.** Collecting outputs from a cloud run.
- **6.3 Cloud Agents from Messaging Platforms.** Triggering work from chat *(demonstration).*

### Module 7. Cursor API Foundations

*Format: Concept + hands-on exercise. Duration: ~60 minutes.*

**Topics**

- **7.1 The Cursor API Landscape.** The five Cursor APIs at a glance and when to use each.
- **7.2 Authentication.** Generating and testing API keys.
- **7.3 Rate Limits and Error Handling.** Production-grade reliability patterns.
- **7.4 ETag Caching.** Efficient repeat queries for analytics workloads.
- **7.5 Listing Available Models.** A quick authentication smoke-test.

### Module 8. Cloud Agents API and Webhooks

*Format: Hands-on exercise. Duration: ~60 minutes.*

**Topics**

- **8.1 Creating a Cloud Agent Programmatically.** The core launch flow from code.
- **8.2 Streaming Agent Responses with SSE.** Incremental output with resume support.
- **8.3 Listing and Downloading Artifacts.** Integrating cloud-run outputs into CI pipelines.
- **8.4 Creating a Webhook Endpoint.** HMAC verification and safe payload handling.
- **8.5 Testing Webhooks Locally with a Tunnel.** Validating receivers before deployment using a local tunnel.
- **8.6 End-to-End Automated Agent Workflow.** The integration capstone exercise.

### Module 9. Admin and Analytics APIs

*Format: Hands-on exercise + demonstrations. Duration: ~75 minutes.*

**Topics**

- **9.1 Listing Team Members.** The simplest Admin API call and a good entry point.
- **9.2 Daily Usage Data.** The most-asked-for admin report.
- **9.3 Setting User Spend Limits.** Programmatic cost governance.
- **9.4 Model Usage Analytics.** Direct insight into cost and adoption.
- **9.5 Daily Active Users.** The headline adoption metric for leadership.
- **9.6 Leaderboards.** Usage rankings and how to present them responsibly.
- **9.7 Conversation Insights.** Intent, complexity, and category analysis *(demonstration).*
- **9.8 Destructive Admin Operations.** Safe patterns for removing a team member *(demonstration).*

### Module 10. AI Code Tracking and Reporting

*Format: Hands-on exercise + take-home project. Duration: ~20 minutes.*

**Topics**

- **10.1 AI Commit Metrics.** Per-commit attribution of AI vs. human contributions.
- **10.2 Bulk Export via CSV Streaming.** Wiring metrics into BI tools.
- **10.3 Granular AI Change Events.** Per-event detail for compliance reporting.
- **10.4 Reporting Dashboard Architecture.** Combining Admin, Analytics, and AI Code Tracking data into a single dashboard *(walkthrough + take-home project).*

### Day 2 Wrap-up

Q&A and closing remarks.

---

## Sample Schedule

Times are indicative; exact pacing is tuned to participant skill level during delivery.

### Day 1 — Cursor Editor and Agent Fluency

| Time          | Session                                |
|---------------|----------------------------------------|
| 9:00 – 9:15   | Welcome and setup                      |
| 9:15 – 10:15  | Module 1 — Mental Models               |
| 10:15 – 10:30 | Break                                  |
| 10:30 – 12:00 | Module 2 — Editor Essentials           |
| 12:00 – 1:00  | Lunch                                  |
| 1:00 – 2:00   | Module 3 — Agent Modes and Tools       |
| 2:00 – 3:00   | Module 4 — Customizing Cursor          |
| 3:00 – 3:15   | Break                                  |
| 3:15 – 4:30   | Open exercises                         |
| 4:30 – 5:00   | Day 1 wrap-up and Q&A                  |

### Day 2 — Automation and Integration

| Time          | Session                                  |
|---------------|------------------------------------------|
| 9:00 – 9:15   | Day 1 recap                              |
| 9:15 – 10:15  | Module 5 — CLI and Local Automation      |
| 10:15 – 10:30 | Break                                    |
| 10:30 – 12:00 | Module 6 — Cloud Agents in the UI        |
| 12:00 – 1:00  | Lunch                                    |
| 1:00 – 2:00   | Module 7 — API Foundations               |
| 2:00 – 3:00   | Module 8 — Cloud Agents API and Webhooks |
| 3:00 – 3:15   | Break                                    |
| 3:15 – 4:30   | Module 9 — Admin and Analytics APIs      |
| 4:30 – 4:50   | Module 10 — AI Code Tracking             |
| 4:50 – 5:00   | Day 2 wrap-up and Q&A                    |

---

## Deliverables for Participants

- Curated concept readmes covering every topic in the program.
- Step-by-step hands-on exercises (one per topic).
- Instructor slide decks.
- Reference reading paths for ongoing self-study — Beginner, Agent Power User, Automation and CLI, Admin and Enterprise, Analytics and Reporting.

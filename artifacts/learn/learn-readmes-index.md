# Cursor Learn Readme Summary

This folder contains beginner-friendly explanations of the **Cursor Learn** course material. The readmes are organized as short teaching notes that explain what each lesson covers, why it matters, the mental models it teaches, and what a developer should remember when using AI tools day-to-day.

## What This Collection Covers

The readmes cover two connected Cursor Learn courses:

- **AI Foundations course (001 – 007):** how AI models work, why outputs are probabilistic, hallucinations, tokens and pricing, context, tool calling, and agents.
- **Coding Agents course (008 – 013):** working with agents in practice, understanding a codebase, developing features, debugging, reviewing and testing code, and customizing agents with rules, skills, and MCP.

Together they form a beginner-to-practitioner path: first build the mental models, then apply them inside Cursor on real codebases.

## Recommended Reading Paths

### Beginner Path

Start here if you are completely new to using AI for coding:

1. [001-ai-foundations-overview.md](001-ai-foundations-overview.md) - what the AI Foundations course is and why mental models matter.
2. [002-how-ai-models-work.md](002-how-ai-models-work.md) - probabilistic outputs, training data, prompts, modalities.
3. [003-hallucinations.md](003-hallucinations.md) - what hallucinations are and how to spot them.
4. [004-tokens-and-pricing.md](004-tokens-and-pricing.md) - tokens, input vs. output cost, streaming.
5. [005-context.md](005-context.md) - the most important concept: managing what the model sees.

### Agent Mental Model Path

Use this path to understand how agents work before opening Cursor:

1. [005-context.md](005-context.md) - context window basics.
2. [006-tool-calling.md](006-tool-calling.md) - how models take actions through tools.
3. [007-agents.md](007-agents.md) - tools in a loop and the shift from task-doer to task-manager.
4. [008-working-with-agents.md](008-working-with-agents.md) - the agent harness and how to prompt it.

### Hands-on Coding Agents Path

Use this path if you already know the basics and want to ship work with agents:

1. [008-working-with-agents.md](008-working-with-agents.md) - effective prompts and context management.
2. [009-understanding-your-codebase.md](009-understanding-your-codebase.md) - grep vs. semantic search, Explore subagent.
3. [010-developing-features.md](010-developing-features.md) - Plan Mode, TDD with agents, design to code.
4. [011-finding-and-fixing-bugs.md](011-finding-and-fixing-bugs.md) - Debug Mode, runtime evidence, MCP observability.
5. [012-reviewing-and-testing-code.md](012-reviewing-and-testing-code.md) - self-review, Agent Review, Bugbot, cloud agents.
6. [013-customizing-agents.md](013-customizing-agents.md) - rules, skills, MCP, and reusable slash workflows.

### Trainer / Curriculum Path

Use this path to teach AI-assisted development to experienced engineers:

1. [001-ai-foundations-overview.md](001-ai-foundations-overview.md) - the transportation analogy and why mental models matter.
2. [002-how-ai-models-work.md](002-how-ai-models-work.md) - deterministic vs. probabilistic systems.
3. [003-hallucinations.md](003-hallucinations.md) - verification mindset.
4. [007-agents.md](007-agents.md) - delegation and the new role of the engineer.
5. [010-developing-features.md](010-developing-features.md) - Plan Mode and TDD with agents.
6. [012-reviewing-and-testing-code.md](012-reviewing-and-testing-code.md) - quality bar and review practices.
7. [013-customizing-agents.md](013-customizing-agents.md) - rules and skills as team conventions.

## Topic Summary

### AI Foundations Overview

This file frames the AI Foundations course and sets expectations for what mental models a developer needs before using AI tools effectively.

- [001-ai-foundations-overview.md](001-ai-foundations-overview.md) - explains that the course teaches how to use AI as a developer (not how to build AI models), introduces the transportation analogy (walk / bike / car ↔ manual coding / IDE tooling / AI tooling), describes the frustration cycle without proper understanding, lists the practical patterns the course covers (code generation, explanation, debugging, refactoring, documentation, test generation), and positions the course as the prerequisite for hands-on Cursor training.

### How AI Models Work

This file explains the core mental model: AI models are like super-intelligent, general-purpose API endpoints that are probabilistic rather than deterministic.

- [002-how-ai-models-work.md](002-how-ai-models-work.md) - contrasts traditional deterministic software with probabilistic AI output, explains how training data plus prompt determines output, uses the "meaning of life" example to show why the same prompt can yield different answers, covers model trade-offs across intelligence, speed, cost, and expertise, and introduces modalities (text, images, voice, video) and their use cases in software development.

### Hallucinations

This file covers one of the most important lessons for anyone using AI: when models confidently generate plausible-sounding but incorrect information.

- [003-hallucinations.md](003-hallucinations.md) - defines hallucination, explains why models hallucinate (they predict patterns, not truth), lists coding-specific hallucinations (invented API methods, wrong imports, mixed syntax, invalid config) with real examples, explains the knowledge-cutoff problem, introduces the verification mindset and the editor feedback loop that lets Cursor catch errors and feed them back to the model.

### Tokens and Pricing

This file explains how AI models actually measure input and output, and why that matters for cost and speed.

- [004-tokens-and-pricing.md](004-tokens-and-pricing.md) - explains tokenization (tokens vs. words), the two token types (input and output, with output typically costing 2-4× more), why TPS (tokens per second) is the standard speed measure, how streaming works token-by-token and enables interruption, optimization techniques like caching, and concrete example pricing for popular models in Cursor.

### Context

This file teaches the single most important practical skill in working with AI: context management.

- [005-context.md](005-context.md) - reframes the problem from "write better prompts" to "manage better context," uses the cooking analogy, defines what counts as context (system prompt, user messages, model outputs, attached files, tool outputs, conversation history), explains the difference between system and user prompts, covers context windows and limits (from 200K up to 1M tokens in Max Mode), and previews compression, checkpoints, subagents, and tool calling as context-management techniques.

### Tool Calling

This file explains how AI models go beyond text generation to actually take actions in your environment.

- [006-tool-calling.md](006-tool-calling.md) - introduces tool calling as giving models the ability to call other APIs, walks through the four-step request-tool-result-incorporate loop, defines the three components of every tool (name, description, parameters) with JSON examples, covers the token cost of tools (definitions add input tokens, results add output tokens), and introduces MCP (Model Context Protocol) as the "USB standard" for connecting external tools to AI models.

### Agents

This file ties together tokens, context, and tool calling into the concept of an agent: tools in a loop.

- [007-agents.md](007-agents.md) - defines an agent as "tools in a loop," walks through a concrete dark-mode-toggle example showing how an agent plans, reads, edits, and verifies, contrasts old turn-by-turn interaction with new goal-based delegation, explains agent strengths (clear objectives, established patterns) versus weaknesses (complex debugging, pixel-perfect designs, brand-new libraries), and reframes the developer's role from task-doer to architect and reviewer.

### Working with Agents

This file kicks off the Coding Agents course and teaches the day-to-day mechanics of prompting and managing agents in Cursor.

- [008-working-with-agents.md](008-working-with-agents.md) - introduces the agent harness (Instructions + Tools + Model), contrasts vague vs. constrained prompts with a user-settings-page example, explains when to start a new conversation vs. continue one, shows how to reference past chats and let the agent find context with semantic search, and covers the most common failure pattern: scope creep.

### Understanding Your Codebase

This file teaches how Cursor agents search and understand code, and how to phrase questions to get the right kind of search.

- [009-understanding-your-codebase.md](009-understanding-your-codebase.md) - explains the two search tools (grep / Instant Grep for exact matches, semantic search for meaning) and why combining them produces 12.5% higher accuracy on large codebases, contrasts targeted vs. broad prompts, introduces the Explore subagent for parallel searches without bloating context, covers architectural diagrams (Mermaid) for visualizing systems, and warns against the common failure of "changing before understanding."

### Developing Features

This file is the practical playbook for shipping features with agents.

- [010-developing-features.md](010-developing-features.md) - explains Plan Mode (research, clarifying questions, structured plan, review-and-edit, then build), when to start over instead of patching, test-driven development with agents (write tests first, commit them, then let the agent make them pass so it can't trivially modify the tests), design-to-code workflows using image input and the Figma MCP server, and the integrated browser for visual verification.

### Finding and Fixing Bugs

This file covers debugging fundamentals and how to use agents (and Debug Mode) effectively for both simple and tricky bugs.

- [011-finding-and-fixing-bugs.md](011-finding-and-fixing-bugs.md) - reviews universal debugging fundamentals (reproduce, reduce, isolate, hypothesize, instrument, prevent regressions), distinguishes the quick-fix approach for clear errors from Debug Mode's evidence-first investigation, explains running multiple models in parallel to compare fixes, shows how to bring runtime data (logs, `EXPLAIN ANALYZE`, browser console) into the agent loop, covers MCP servers like Sentry and Datadog for production observability, and warns against accepting fixes you don't understand.

### Reviewing and Testing Code

This file covers how to keep quality high even as agents produce more code.

- [012-reviewing-and-testing-code.md](012-reviewing-and-testing-code.md) - explains why AI-generated code needs the same review standards as human code, self-review techniques (watching the diff, tagging `@Branch`, asking the agent to review its own work), commit hygiene via an agent-driven rework-commits workflow, the Agent Review feature, Bugbot for automated PR reviews (logic errors, not just style), the three verifiable goals (tests, type checking, linting), letting agents write tests and set up testing infrastructure, cloud agents for parallel test variations, and the importance of speeding up feedback loops.

### Customizing Agents

This file closes out the course by showing how to make the agent fit your team and codebase.

- [013-customizing-agents.md](013-customizing-agents.md) - introduces two customization layers: Rules (`.cursor/rules/`) for always-included static context and Skills for dynamically loaded specialized workflows, gives concrete examples for both, covers what rules work best for (build commands, code conventions, canonical examples, guardrails) and what to avoid (copying entire style guides, over-engineering), explains MCP for connecting external tools (Slack, Datadog, Sentry, databases, Figma), notes that the agent can run any installed CLI tool (gh, aws, kubectl, docker), and shows how to turn skills into reusable `/command` workflows checked into git.

## Complete Index by Number

### AI Foundations Course

- [001-ai-foundations-overview.md](001-ai-foundations-overview.md)
- [002-how-ai-models-work.md](002-how-ai-models-work.md)
- [003-hallucinations.md](003-hallucinations.md)
- [004-tokens-and-pricing.md](004-tokens-and-pricing.md)
- [005-context.md](005-context.md)
- [006-tool-calling.md](006-tool-calling.md)
- [007-agents.md](007-agents.md)

### Coding Agents Course

- [008-working-with-agents.md](008-working-with-agents.md)
- [009-understanding-your-codebase.md](009-understanding-your-codebase.md)
- [010-developing-features.md](010-developing-features.md)
- [011-finding-and-fixing-bugs.md](011-finding-and-fixing-bugs.md)
- [012-reviewing-and-testing-code.md](012-reviewing-and-testing-code.md)
- [013-customizing-agents.md](013-customizing-agents.md)

## Quick Concept Map

| Concept | Where It's Introduced | Where It's Applied |
|---------|----------------------|--------------------|
| Probabilistic outputs | [002](002-how-ai-models-work.md) | [008](008-working-with-agents.md), [011](011-finding-and-fixing-bugs.md) |
| Hallucinations | [003](003-hallucinations.md) | [011](011-finding-and-fixing-bugs.md), [012](012-reviewing-and-testing-code.md) |
| Tokens and cost | [004](004-tokens-and-pricing.md) | [006](006-tool-calling.md), [007](007-agents.md) |
| Context window | [005](005-context.md) | [008](008-working-with-agents.md), [009](009-understanding-your-codebase.md) |
| Tool calling | [006](006-tool-calling.md) | [009](009-understanding-your-codebase.md), [011](011-finding-and-fixing-bugs.md) |
| Agents (tools in a loop) | [007](007-agents.md) | [008](008-working-with-agents.md) – [013](013-customizing-agents.md) |
| Plan Mode | [010](010-developing-features.md) | [010](010-developing-features.md) |
| Debug Mode | [011](011-finding-and-fixing-bugs.md) | [011](011-finding-and-fixing-bugs.md) |
| Rules and Skills | [013](013-customizing-agents.md) | [013](013-customizing-agents.md) |
| MCP | [006](006-tool-calling.md) | [011](011-finding-and-fixing-bugs.md), [013](013-customizing-agents.md) |

## Bottom Line

Use this folder as a guided learning library for the Cursor Learn courses. Start with **AI Foundations** to build the mental models (how models work, hallucinations, tokens, context, tool calling, agents), then move into **Coding Agents** to apply those models in real Cursor workflows (prompting, codebase understanding, feature development, debugging, review, and customization).

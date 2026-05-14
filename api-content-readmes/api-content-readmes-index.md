# Cursor APIs Readme Summary

This folder contains beginner-friendly explanations of the Cursor APIs. The readmes are organized as short teaching notes that explain what each API does, why it matters, how to authenticate, which endpoints exist, what the data means, and what a beginner should remember.

## What This Collection Covers

The readmes cover the full Cursor API surface:

- **API map and shared concepts:** the five Cursor APIs at a glance, when to use which, authentication, rate limits, ETag caching, error handling, and best practices.
- **Cloud Agents API:** durable agents and per-prompt runs, streaming SSE responses, artifacts, lifecycle management, worker tokens, metadata endpoints, and webhooks.
- **Admin API:** team members, audit logs, daily usage data, spending data, granular usage events, user spend limits, member removal, repository blocklists, and billing groups.
- **Analytics API:** team-level and by-user metrics for agent edits, Tab usage, daily active users, model usage, file extensions, MCP, slash commands, Plan mode, Skills, Ask mode, conversation insights, leaderboard, and Bugbot.
- **AI Code Tracking API:** per-commit AI attribution metrics, granular AI change events, CSV streaming exports, and alpha commit blame details with conversation references.

## Recommended Reading Paths

### Beginner Path

Start here if you are new to Cursor APIs:

1. [001-api-overview.md](001-api-overview.md) - the API map and shared concepts (auth, rate limits, caching, errors).
2. [002-cloud-agents-api.md](002-cloud-agents-api.md) - the only API available on all plans; ideal first hands-on.
3. [004-analytics-api.md](004-analytics-api.md) - read-only usage metrics, easy to query.
4. [003-admin-api.md](003-admin-api.md) - programmatic team management for admins.
5. [005-ai-code-tracking-api.md](005-ai-code-tracking-api.md) - measure AI contribution to your codebase.

### Automation and Cloud Agents Path

Use this path to build automations on top of Cloud Agents:

1. [001-api-overview.md](001-api-overview.md) - authentication, rate limits, and error handling.
2. [002-cloud-agents-api.md](002-cloud-agents-api.md) - agent creation, runs, SSE streaming, artifacts, and lifecycle.
3. [002-cloud-agents-api.md](002-cloud-agents-api.md) - webhooks section for status-change notifications and signature verification.

### Admin and Enterprise Path

Use this path for team rollout, governance, and reporting:

1. [001-api-overview.md](001-api-overview.md) - API selection, auth, and rate limits.
2. [003-admin-api.md](003-admin-api.md) - members, audit logs, spending, blocklists, and billing groups.
3. [004-analytics-api.md](004-analytics-api.md) - adoption metrics, leaderboard, and Bugbot analytics.
4. [005-ai-code-tracking-api.md](005-ai-code-tracking-api.md) - AI attribution for compliance reporting.

### Analytics and Reporting Path

Use this path to build dashboards and recurring reports:

1. [001-api-overview.md](001-api-overview.md) - ETag caching and date format best practices.
2. [004-analytics-api.md](004-analytics-api.md) - team-level and by-user metrics.
3. [005-ai-code-tracking-api.md](005-ai-code-tracking-api.md) - commit metrics in JSON and CSV.
4. [003-admin-api.md](003-admin-api.md) - daily usage data and filtered usage events for cost analysis.

## Topic Summary

### API Map and Shared Concepts

This file introduces the five Cursor APIs as a group, helps you choose the right one for each task, and covers the cross-cutting concepts used by all of them.

- [001-api-overview.md](001-api-overview.md) - explains the five Cursor APIs (Admin, Analytics, AI Code Tracking, Cloud Agents, TypeScript SDK), provides a decision tree for picking the right API, summarizes endpoints and rate limits, and covers authentication, ETag caching, exponential backoff, error responses, and beginner best practices.

### Cloud Agents API and Webhooks

This file explains how to programmatically launch and manage Cloud Agents and how to receive automated notifications about their status.

- [002-cloud-agents-api.md](002-cloud-agents-api.md) - introduces the v1 durable agent plus per-prompt run model, documents every agent and run endpoint, explains SSE streaming and `Last-Event-ID` resume, artifacts and presigned downloads, archive and delete flows, worker tokens for My Machines, and metadata endpoints (`/v1/me`, `/v1/models`, `/v1/repositories`). It also documents webhooks: the `statusChange` event for `FINISHED` and `ERROR`, HMAC-SHA256 signature verification, payload structure, Python and Node.js receiver examples, ngrok testing, and idempotency.

### Admin API

This file explains how administrators programmatically manage their Cursor team.

- [003-admin-api.md](003-admin-api.md) - documents authentication with Admin API keys, listing team members, querying audit logs with event-type filters and flexible date formats, retrieving daily usage data with optional pagination for active vs all members, getting spending data per user, fetching detailed filtered usage events with token counts and costs, setting and clearing user spend limits, removing team members by email or ID, managing repository blocklists with glob patterns, and managing enterprise billing groups (create, get, update, delete, add/remove members).

### Analytics API

This file explains how to retrieve aggregated and per-user metrics about how a team uses Cursor.

- [004-analytics-api.md](004-analytics-api.md) - explains admin-scoped authentication, shared query parameters with date format and caching guidance, the 30-day maximum range, team-level endpoints for agent edits, Tab usage, daily active users, client versions, model usage, top file extensions, MCP adoption, slash commands, Plan mode, Skills, Ask mode, Enterprise-only conversation insights (intents, complexity, categories, guidance levels, work types), leaderboard rankings, and Bugbot PR analytics. It also covers the matching `/analytics/by-user/...` endpoints with built-in pagination.

### AI Code Tracking API

This file explains how to measure AI contributions to your codebase from git commits.

- [005-ai-code-tracking-api.md](005-ai-code-tracking-api.md) - explains how on-device signature detection attributes lines to Tab, Composer, or human; documents commit metrics in JSON and streaming CSV; granular AI change events in JSON and CSV; and the alpha commit details endpoint that returns per-file range annotations and conversation summaries. Covers commit sources (`ide`, `cli`, `cloud`), AI sources (`TAB`, `COMPOSER`), the line attribution formula, privacy mode effects, and use cases for adoption measurement and compliance reporting.

## Complete Index by Number

- [001-api-overview.md](001-api-overview.md)
- [002-cloud-agents-api.md](002-cloud-agents-api.md)
- [003-admin-api.md](003-admin-api.md)
- [004-analytics-api.md](004-analytics-api.md)
- [005-ai-code-tracking-api.md](005-ai-code-tracking-api.md)

## Quick API Comparison

| API | Best For | Auth | Availability |
|-----|----------|------|--------------|
| **Cloud Agents** | Launching and managing agents from code | User or service account API key | Beta - all plans |
| **Admin** | Team management, spending, audit logs | Admin API key | Enterprise |
| **Analytics** | Usage metrics, adoption, leaderboards | Admin-scoped API key | Enterprise |
| **AI Code Tracking** | Per-commit AI attribution | Admin-scoped API key | Enterprise (alpha) |

## Bottom Line

Use this folder as a guided learning library for the Cursor APIs. Start with the API overview, then pick the path that matches your goal: building automation with Cloud Agents, administering a team, generating analytics reports, or measuring AI contributions to your codebase.

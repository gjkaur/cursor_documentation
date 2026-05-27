#!/usr/bin/env python3
"""Restore monospace diagram SVGs corrupted by lines_from_monospace_svg column drift."""

from __future__ import annotations

from pathlib import Path

from marp_svg_common import monospace_panel_svg

# Authoritative line content for each affected asset (module-NN/name.svg).
DIAGRAM_LINES: dict[str, list[str]] = {
    "module-02/quick-reference-card.svg": [
        "SHORTCUTS:",
        "  Cmd/Ctrl + I        → Open Agent",
        "  Cmd/Ctrl + L        → Explain selected code",
        "  Shift + Tab         → Toggle Plan Mode",
        "  Cmd/Ctrl + Shift + S → Create checkpoint",
        "@MENTIONS:  @filename  @symbol  @branch  @chat  @web",
        "SAFE CHANGE: Ask → Review diff → Accept/reject → Test",
        "PLAN MODE:   Shift+Tab → Describe → Review plan → Approve → Execute",
    ],
    "module-02/expected-agent-output-sample.svg": [
        "PURPOSE: Object detection and segmentation library (PyTorch)",
        "ENTRY POINTS:",
        "• train_net.py — Main training script",
        "• demo.py — Inference demo",
        "KEY MODULES:",
        "config/ → model_zoo ←→ engine/",
        "  ↓         ↓         ↓",
        "structures ←→ modeling/ ←→ data/",
        "DATA FLOW:",
        "Config → build_model() → DataLoader → Training Loop → Loss → Backprop",
    ],
    "module-02/exercise-2-8-agent-terminal-loop.svg": [
        "Agent: I'll run the tests first.",
        "→ Executing: pytest tests/",
        "→ Output: 7 passed, 2 failed",
        "Agent: Two tests failed. Let me look at them.",
        "→ Reading: tests/test_auth.py",
        "Agent: Login test failing—timeout too short. Increasing 5→10 seconds.",
        "→ Editing: tests/test_auth.py",
        "→ Executing: pytest tests/test_auth.py",
        "→ Output: All tests passed",
    ],
    "module-03/quick-reference-card.svg": [
        "MODES:",
        "  ASK MODE   → Read-only | Questions, learning",
        "  AGENT MODE → Full tools | Implementation, debugging",
        "TOOLS:",
        "  BROWSER  → Navigate, read, console, screenshot",
        "  TERMINAL → Execute commands, read output",
        "  FILE     → Read, edit, create, delete",
        "  SEARCH   → Code search, symbol lookup",
        "PROMPTING:",
        "  • Be specific  • Define boundaries  • Plan first for complex tasks",
        "  • Specify output format  • Define success criteria",
    ],
    "module-03/expected-agent-actions.svg": [
        "→ browse_navigate(url=\"http://localhost:8000\")",
        "→ browse_snapshot() — page structure captured",
        "→ browse_console_messages()",
        "  [WARNING] deprecated API used on line 42",
        "  [ERROR] Failed to load resource: api/data 404",
        "Agent: Found a deprecated API warning and a 404 on /api/data",
    ],
    "module-03/exercise-3-3-debug-workflow-step-5.svg": [
        "→ python app.py → IndexError: list index out of range line 23",
        "→ Agent adds guard condition",
        "→ python app.py --test-empty-input → \"No data provided\"",
    ],
    "module-04/what-is-a-skill.svg": [
        ".cursor/skills/",
        "└── skill-name/",
        "    ├── SKILL.md          # Main instructions (required)",
        "    ├── scripts/          # Optional helper scripts",
        "    ├── references/       # Optional reference docs",
        "    └── templates/        # Optional output templates",
    ],
    "module-04/what-is-mcp.svg": [
        "Cursor Agent ─MCP Protocol─→ MCP Server",
        "                            ├─→ GitHub API",
        "                            ├─→ Slack API",
        "                            ├─→ Jira API",
        "                            └─→ Custom Tools",
    ],
    "module-04/walkthrough-slash-command-example.svg": [
        "name: deploy | argument: environment (staging | production)",
        "Pre-deploy: make test → make lint → git status clean",
        "Deploy staging: git push origin main → kubectl set image",
        "Deploy production: git tag → deploy-prod.sh (requires approval)",
        "Post-deploy: healthcheck → smoke tests → slack notify",
    ],
    "module-04/what-are-subagents.svg": [
        "Main Agent",
        "  ──→ Subagent: SecurityScanner → \"2 critical issues found\"",
        "  ──→ Subagent: Documentation Generator → \"Updated README.md\"",
        "  ──→ Subagent: Test Writer → \"Added 5 test cases\"",
    ],
    "module-04/quick-reference-card.svg": [
        "RULES        → .cursor/rules/*.mdc (standards, security, build)",
        "REPO INSTR.  → .cursor/repository-instructions.md (project overview)",
        "SKILLS       → .cursor/skills/*/SKILL.md (invoke with /skill-name)",
        "MCP          → ~/.cursor/mcp.json (GitHub, Slack, Jira, custom)",
        "SLASH CMDS   → .cursor/commands/*.md (/deploy, /onboard, triage)",
        "SUBAGENTS    → Parallel, isolated, specialized execution",
    ],
    "module-06/messaging-integration-architecture.svg": [
        "Slack/Discord/Teams",
        "  │ \"/cursor review PR #42\"",
        "  ↓",
        "Webhook receiver (your server or Cursor hosted)",
        "  │ POST /v1/agents with webhookUrl",
        "  ↓",
        "Cursor Cloud Agent",
        "  │ POST to webhookUrl when complete",
        "  ↓",
        "Webhook receiver → post response to Slack",
    ],
    "module-06/quick-reference-card.svg": [
        "UI ACCESS:",
        "  Cursor Editor: View → Cloud Agents",
        "  Web: https://cursor.com/agents",
        "LAUNCH: + New → repo/branch → prompt → model → launchAgent",
        "ARTIFACT: View in detail page · Download single/zip · API (30-day storage)",
        "MESSAGING:",
        "  cursor[prompt] in Slack",
        "  cursor[prompt] in Discord",
        "  Webhook POST to trigger endpoint",
    ],
    "module-07/etag-flow.svg": [
        "Request : GET /v1/analytics/usage",
        "  → 200 OK, ETag: \"abc123\", Body: { .. data ... }",
        "Request : GET with If-None-Match: \"abc123\"",
        "  → 304 Not Modified (unchanged) OR",
        "  → 200 OK, ETag: \"def456\" (updated data)",
    ],
    "module-07/quick-reference-card.svg": [
        "BASE URL: https://api.cursor.com/v1",
        "AUTH:  -u \"api_key:\" (curl) | Bearer token | OpenAISDK base_url",
        "ENDPOINTS:",
        "  GET  /models           List available models",
        "  POST /agents           Create cloud agent",
        "  GET  /agent/{id}       Get agent status",
        "  GET  /admin/members    List team members",
        "  GET  /admin/analytics/usage  Usage data",
        "ERRORS: 429/5xx → retry with backoff | 4xx → fix request",
        "CACHE:  If-None-Match → handle 304 Not Modified",
    ],
    "module-08/workflow-architecture.svg": [
        "create_agent() → wait (webhook OR polling) → download_artifacts()",
        "      ↑                ↑",
        "Flask webhook server   completion_event.set()",
        "background thread      on FINISHED status",
    ],
    "module-09/quick-reference-card.svg": [
        "ENDPOINTS:",
        "  GET    /admin/members                 List members",
        "  GET    /admin/analytics/usage/daily   Daily usage",
        "  GET    /admin/analytics/usage/models  Model usage",
        "  GET    /admin/analytics/usage/users   Per-user usage",
        "  PATCH  /admin/policies/users/{id}/limits Set spend limits",
        "  GET    /admin/members/{id}/resources  User resources",
        "LEADERBOARDS: Anonymize · positive metrics · opt-in · role context",
        "REMOVAL:     Audit → Deactivate → Transfer → Log → Confirm delete",
    ],
    "module-09/demo-saferemovaldemo-workflow.svg": [
        "Step 1: find_user(email) → userid",
        "Step 2: audit_resources() → agents, runs",
        "Step 3: deactivate() → status: inactive",
        "Step 4: transfer_resource(new_owner_email)",
        "Step 5: hard_delete() → permanent (irreversible)",
        "→ generate_audit_report()",
    ],
}


def main() -> int:
    assets = Path(__file__).resolve().parent.parent / "slides" / "assets"
    for rel, lines in DIAGRAM_LINES.items():
        path = assets / rel
        path.write_text(monospace_panel_svg(lines), encoding="utf-8")
        print(f"Fixed {rel}")
    print(f"Done. {len(DIAGRAM_LINES)} diagram(s) restored.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

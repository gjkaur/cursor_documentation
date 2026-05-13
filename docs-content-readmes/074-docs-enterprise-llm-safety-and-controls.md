This is the **LLM Safety and Controls** documentation – it explains how to control what agents can do, set up safety guardrails, and guide LLM behavior toward desired outcomes.

Think of this as the **security and governance guide** – covering everything from terminal restrictions to hooks to DLP integration, with a clear distinction between deterministic security controls and non-deterministic steering mechanisms.

Let me break this down.

---

## Understanding Model Behavior

LLMs are not deterministic databases. They:

| Behavior | Description |
|----------|-------------|
| **Generate different outputs** | For the same input |
| **Hallucinate** | Produce plausible but wrong facts or code |
| **Prompt injection** | Can be influenced by carefully crafted prompts |

> *"You can't rely on LLMs to always make safe decisions."*

---

## Two Approaches to Safety

Cursor provides **two complementary approaches**:

| Approach | Description | Example |
|----------|-------------|---------|
| **Security controls** (deterministic) | Hard boundaries that block dangerous operations regardless of LLM suggestions | Terminal restrictions, hooks, approval workflows, sandboxing |
| **LLM steering** (non-deterministic) | Guide LLM behavior by shaping context and available actions | Rules, commands, MCP integrations |

> *"Use both approaches together. Security controls provide the safety net. Steering reduces how often agents attempt problematic actions in the first place."*

---

## Security Controls (Deterministic)

These controls enforce **hard boundaries** regardless of what the LLM suggests.

### 1. Terminal Command Restrictions

| Feature | Description |
|---------|-------------|
| **Default** | Requires your approval before executing any terminal command |
| **Protects against** | Destructive commands (deleting files, dropping databases), commands that expose sensitive data, unintended side effects |
| **User experience** | See full command prompt → Approve, deny, or modify |

### Auto-Approval Risks

> *"You can enable auto-approval for terminal commands, but understand the risks."*

| Risk | Description |
|------|-------------|
| **Destructive commands** | Could run without your knowledge |
| **No review** | Commands execute before you can review |
| **Prompt injection** | Bugs or injection could cause unintended operations |

### Auto-Run Configuration (Enterprise)

Teams can configure auto-run policies in the team dashboard:

| Feature | Description |
|---------|-------------|
| **Allowlist** | Commands that don't require approval (e.g., `npm install`, `pip install`, `cargo build`, `make test`) |
| **Warning** | Allowlist is **best-effort, not a security boundary**. Determined agents or prompt injection might bypass it. |

> *"Always combine allowlists with other security controls like hooks."*

---

### 2. Enforcement Hooks

Hooks let you run custom logic at key points in the agent loop:

| Hook Point | Purpose |
|------------|---------|
| **Before prompt submission** | Scan for sensitive data (API keys, PII, proprietary info) – block submission |
| **Before file reading** | Scan files before agents read them – redact or block access to secrets, PII |
| **After code generation** | Scan generated code before writing to disk – check for vulnerabilities, licensed code, credentials |
| **Before terminal execution** | Block dangerous commands or route through approval workflows |

#### Example: Blocking Git Commands

```bash
#!/bin/bash
input=$(cat)
command=$(echo "$input" | jq -r '.command')

if [[ "$command" =~ git[[:space:]] ]]; then
  cat << EOF
{
  "permission": "deny",
  "userMessage": "Git command blocked. Please use gh tool instead.",
  "agentMessage": "Use 'gh' commands instead of raw git."
}
EOF
fi
```

#### Example: Redacting Secrets

```bash
#!/bin/bash
input=$(cat)
content=$(echo "$input" | jq -r '.content')

if echo "$content" | grep -qE 'gh[ps]_[A-Za-z0-9]{36}'; then
  cat << EOF
{
  "permission": "deny"
}
EOF
  exit 3
fi
```

> *"See Hooks for complete documentation and more examples."*

---

### 3. Protecting Sensitive Files

#### `.cursorignore`

Works like `.gitignore` but controls what Cursor can access. Excludes files from:

| Feature |
|---------|
| Semantic search |
| Agent file reading |
| Context selection |

> *"`.cursorignore` is **not a security boundary**. It's a convenience feature to exclude files from AI processing."*

**Limitations:**
- Users can manually read ignored files
- Agents might find ways to access ignored content
- Doesn't prevent file access, only excludes from indexing

> *"For true security, use file system permissions or encrypt sensitive data."*

#### `.cursor` Directory Protection (Enterprise)

Prevents agents from modifying the `.cursor` directory:

| Restriction |
|-------------|
| Cannot modify files in `.cursor/` |
| Cannot delete the `.cursor/` directory |
| Cannot change cursor rules or settings files |

> *"Configure in the team dashboard under 'cursor Directory Protection' (Enterprise only)."*

---

### 4. Browser Origin Controls (Enterprise)

Restrict which websites agents can navigate to when using the browser tool. Define an allowlist of approved domains – agents attempting to visit other origins are blocked.

> *"Configure in the team dashboard under 'Browser Controls' (Enterprise only)."*

---

### 5. Integration with DLP Tools

Three ways to integrate with existing Data Loss Prevention (DLP) tools:

#### Option 1: Endpoint DLP Agents

Most endpoint DLP software can inspect Cursor's network traffic. Configure your DLP to:

| Action |
|--------|
| Monitor traffic to `*.cursor.sh` domains |
| Scan for sensitive patterns in outbound requests |
| Block or alert on policy violations |

> *"Network DLP may impact performance. See Network Configuration for proxy considerations."*

#### Option 2: Hooks-Based DLP

Use hooks to implement custom DLP logic:

**Before prompt submission example:**
```bash
#!/bin/bash
input=$(cat)
prompt=$(echo "$input" | jq -r '.prompt')

# Check for API keys
if echo "$prompt" | grep -qE 'api[-_]?key.*[A-Za-z0-9]{32}'; then
  cat << EOF
{
  "continue": false,
  "userMessage": "Prompt contains what looks like an API key. Remove it and try again."
}
EOF
  exit 1
fi

# Allow if no sensitive data found
cat << EOF
{
  "continue": true
}
EOF
```

**After code generation example:**
```bash
#!/bin/bash
input=$(cat)
file_path=$(echo "$input" | jq -r '.file_path')
edits=$(echo "$input" | jq -r '.edits[].new_string')

# Check for hardcoded credentials
if echo "$edits" | grep -qE 'password.*=.*["'"'"'][^"'"'"']+["'"'"']'; then
  # Send to your DLP API for analysis
  curl -X POST "https://dlp.yourcompany.com/scan" \
    -H "Content-Type: application/json" \
    -d "{\"content\":\"$edits\",\"file\":\"$file_path\"}"
fi
```

#### Option 3: Third-Party DLP Integration

Call your existing DLP vendor's API from hooks:

```bash
#!/bin/bash
input=$(cat)
content=$(echo "$input" | jq -r '.content')

# Send to DLP API
response=$(curl -s -X POST "https://dlp-api.company.com/analyze" \
  -H "Authorization: Bearer $DLP_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d "{\"text\":\"$content\"}")

is_allowed=$(echo "$response" | jq -r '.allowed')

if [ "$is_allowed" = "true" ]; then
  cat << EOF
{
  "permission": "allow"
}
EOF
else
  violation=$(echo "$response" | jq -r '.violation_type')
  cat << EOF
{
  "permission": "deny",
  "userMessage": "Content blocked by DLP policy: $violation"
}
EOF
fi
```

> *"This approach gives you centralized DLP policy management across all development tools."*

---

### 6. Approval Workflows

Users can set their agent to **always ask for approval** before:

| Action |
|--------|
| Reading files |
| Editing files |
| Running terminal commands |
| Making network requests |

**Trade-off:** Significantly slows down development experience. Most teams use hooks to block dangerous operations automatically instead.

---

### 7. Operating System Security

| Practice | Description |
|----------|-------------|
| **File permissions** | `chmod 600 .env`, `chown app-user:app-user .env` |
| **Separate directories** | `chmod 700 /etc/app/secrets` |
| **Separate sensitive repos** | Don't clone to machines where Cursor runs |
| **Encrypted filesystems** | Don't mount in directories where Cursor has access |

---

### 8. Model Provider Safety

All model providers implement safety systems that:

| Feature |
|---------|
| Reject prompts requesting harmful information |
| Refuse to generate dangerous code |
| Filter outputs for safety |

> *"However, these are **not security boundaries**. Safety systems can be bypassed or tricked."*

---

## LLM Steering (Non-Deterministic Guidance)

Security controls block harmful actions **after** the LLM suggests them. Steering mechanisms guide the LLM to make **better suggestions in the first place**.

> *"These are non-deterministic. They improve outcomes but don't guarantee prevention."*

### 1. Rules

Add instructions to the LLM's context window before every request.

**Scopes:**

| Scope | Application |
|-------|-------------|
| **User rules** | Personal preferences (code style, preferred libraries) |
| **Project rules** | Project-specific standards (naming conventions, framework usage) |
| **Team rules** | Company-wide standards (security requirements, compliance rules) |

> *"The LLM sees all applicable rules when generating responses. It will attempt to follow them, but rules are suggestions, not guarantees. Combine rules with enforcement hooks for requirements that must be followed."*

### 2. Commands and Workflows

Commands package reusable prompts that agents can invoke with slash commands like `/test` or `/deploy`.

| Feature | Description |
|---------|-------------|
| **Workflows** | Multi-step processes guiding agents through complex tasks |
| **Prompt libraries** | Tested prompts for common tasks, reducing variation |
| **Scoping** | Commands can be scoped to teams, projects, or users |

> *"Team admins can create organization-wide commands that appear for all developers."*

### 3. Context Enrichment with MCPs

Model Context Protocol (MCP) servers let agents access external data sources:

| Use |
|-----|
| Pull in company documentation |
| Query internal APIs |
| Access knowledge bases |
| Integrate with development tools |

> *"MCPs are scoped to teams or users. Unlike hooks, MCPs don't enforce policies—they provide information that helps agents make better decisions."*

---

## Security vs. Steering Summary

| Aspect | Security Controls | LLM Steering |
|--------|-------------------|---------------|
| **Nature** | Deterministic | Non-deterministic |
| **Guarantee** | Hard boundaries | Improves outcomes, no guarantee |
| **When applied** | After LLM suggests action | Before LLM generates response |
| **Examples** | Terminal restrictions, hooks, sandboxing | Rules, commands, MCPs |
| **Primary defense** | ✅ Yes | ❌ No |

> *"Security controls provide the safety net. Steering reduces how often agents attempt problematic actions in the first place."*

---

## Quick Reference Card

| Control Type | Features |
|--------------|----------|
| **Terminal** | Approval required by default, auto-run allowlist |
| **Hooks** | Before prompt, file read, code generation, terminal execution |
| **File protection** | `.cursorignore`, `.cursor` directory protection (Enterprise) |
| **Browser** | Origin allowlist (Enterprise) |
| **DLP integration** | Endpoint DLP, hooks-based, third-party API |
| **Steering** | Rules, commands, MCPs |

---

## Common Beginner Questions

### Q: What's the difference between security controls and steering?
**A:** Security controls **block** dangerous actions. Steering **guides** the LLM to make better choices. Use both.

### Q: Is `.cursorignore` a security feature?
**A:** No – it's a convenience feature. For true security, use file system permissions.

### Q: Can I rely solely on model provider safety systems?
**A:** No – they are not security boundaries. Always combine with your own controls.

### Q: What's the best way to block dangerous terminal commands?
**A:** Use hooks (deterministic) combined with terminal approval defaults.

### Q: Can I integrate my existing DLP tool with Cursor?
**A:** Yes – three ways: endpoint DLP, hooks-based DLP, or third-party API integration.

### Q: Do rules guarantee the LLM will follow them?
**A:** No – rules are suggestions. Use enforcement hooks for requirements that must be followed.

---

## The Bottom Line

**LLM safety requires two complementary approaches: deterministic security controls (hard boundaries) and non-deterministic steering (guidance).**

**Key controls to implement:**
1. **Terminal command restrictions** – approval by default
2. **Enforcement hooks** – before prompts, file reads, code generation, terminal execution
3. **File protection** – `.cursorignore` + `.cursor` directory protection
4. **DLP integration** – via hooks or existing DLP tools
5. **Browser origin allowlist** – for Enterprise
6. **Steering** – rules, commands, MCPs

**The hierarchy of safety:**
- **Security controls** = Safety net 🛡️ (deterministic, blocks bad actions)
- **Steering** = Guidance 🧭 (non-deterministic, encourages good actions)

**For enterprise security teams:** Hooks are your most powerful tool for enforcing custom policies. Combine them with terminal restrictions, file protection, and DLP integration for comprehensive coverage.

Would you like me to explain any specific safety control in more detail?
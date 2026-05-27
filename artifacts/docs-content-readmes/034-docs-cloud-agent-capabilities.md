This is the **Cloud Agent Capabilities** documentation – it explains all the powerful things Cloud Agents can do that local agents cannot. This includes **computer use** (controlling desktop and browser), **artifacts** (screenshots/videos), **remote desktop control**, and **automatic CI fixing**.

Think of Cloud Agents as **virtual developers** with their own computers – they can see what they're building, test it, show you proof, and even let you take over!

Let me break this down for a beginner.

---

## What Makes Cloud Agents Special? (The 10-Second Summary)

**Each cloud agent runs in its own isolated VM with a full desktop environment.** Agents can use a mouse and keyboard to control the desktop and browser, allowing them to interact with the software they build like a human developer.

| Local Agents | Cloud Agents |
|--------------|--------------|
| Can't see what they're building | Have full desktop with browser |
| Can't test UI automatically | Can click through UI flows |
| You must test changes locally | You can remote into their computer |
| No automatic CI fixing | Can auto-fix failing tests |

> *"This means agents can start dev servers, open the app in a browser, click through UI flows, and verify their changes work before pushing a PR."*

---

## 1. Computer Use 🖥️

This is the **headline feature** of Cloud Agents.

Each cloud agent runs in its own **isolated VM with a full desktop environment**. Agents can use a mouse and keyboard to control the desktop and browser.

### What Agents Can Do:

| Capability | Example |
|------------|---------|
| Start dev servers | `npm run dev` |
| Open app in browser | Navigate to `localhost:3000` |
| Click through UI flows | Test login, signup, checkout |
| Verify changes work | Confirm bug is fixed before pushing PR |

**Think of it as:** The agent can actually **see** what it built and test it, just like a human developer would.

---

## 2. Demos and Artifacts 📸

Agents create **artifacts** such as screenshots, videos, and log references to demonstrate their work.

| Artifact | What it shows |
|----------|---------------|
| **Screenshots** | Visual proof of what the agent saw |
| **Videos** | Recording of the agent testing the software |
| **Log references** | Execution details and errors |

### Where Artifacts Go:

> *"These artifacts are attached to the PR so you can quickly validate changes without checking out the branch locally."*

**Instead of:** Checking out the branch, running the code, and testing manually  
**You can:** Look at screenshots/videos in the PR to see what the agent did

### Artifacts in GitHub (Opt-in)

You can opt-in to have Cloud Agents embed artifacts directly into GitHub pull request descriptions by enabling the **"Allow posting artifacts to GitHub"** setting in the Cloud Agents dashboard.

> *"GitHub's image proxy requires public URLs, so artifacts in PR descriptions use long, unguessable URLs that are viewable without authentication. For context, GitHub used public URLs for all issue and PR attachments until May 2023."*

---

## 3. Remote Desktop Control 🖱️

This is an **incredible** feature – you can actually take control of the agent's remote desktop!

| Feature | What it means |
|---------|---------------|
| **Take control** | Interact with the software the agent is building |
| **Hand control back** | Let the agent keep working |
| **Test without checking out** | Use the agent's VM instead of your local machine |

> *"Cloud agents run in a remote VM that can be fully onboarded with your repo, dependencies, tooling, and setup scripts. This allows you to test changes directly in the agent's VM without checking out the branch on your local machine."*

**Example workflow:**
1. Agent builds a new feature
2. You remote into the agent's desktop
3. You test the feature yourself
4. You hand control back to the agent
5. Agent continues working on fixes

---

## 4. MCP Tools (External Integrations)

Cloud agents can use **MCP (Model Context Protocol) servers** configured for your team.

| Capability | What it means |
|------------|---------------|
| **Access external tools** | Databases, APIs, third-party services |
| **OAuth support** | For MCP servers that need authentication |
| **Per-user OAuth** | Even for team-shared MCP servers |

**Add and enable MCP servers** through the MCP dropdown in `cursor.com/agents`.

### Custom MCP Servers

You can add custom MCP servers using either **HTTP** or **stdio** transport.

> *"SSE and `mcp-remote` are not supported."*

### Security: Encrypted at Rest

MCP configurations are **encrypted at rest**. Sensitive fields are **redacted** and cannot be read back by any user after saving:

| Field | What it protects |
|-------|------------------|
| `env` | Environment variables for stdio servers |
| `headers` | Request headers for HTTP servers |
| `CLIENT_SECRET` | OAuth client secret |

---

## HTTP vs. stdio MCP Servers

| Transport | How it works | Security |
|-----------|--------------|----------|
| **HTTP (recommended)** | Server configs never in VM. Tool calls proxied through backend. | More secure – agent never sees credentials |
| **stdio** | Server runs inside VM. Agent has access to config and env vars. | Less secure – agent sees everything |

> *"Stdio servers depend on the VM environment to execute. We cannot verify that a stdio server will run successfully until a cloud agent is launched. We recommend using HTTP MCPs when possible."*

---

## 5. Fixing CI Failures Automatically 🔧

This is a **game-changer** for productivity. Cloud Agents **automatically try to fix CI failures in PRs they create.**

### Supported CI:

> *"This currently supports GitHub Actions only."*

### When Cloud Agents SKIP automatic CI fixes:

| Situation | Why |
|-----------|-----|
| You pushed a new commit to the branch | Agents don't auto-fix human commits |
| You sent a follow-up message to the agent | Manual intervention overrides |
| Same check already failing on base commit | Not the agent's fault |
| PR already had 10 CI-failure follow-ups | Limit reached (prevents infinite loops) |

### How to Disable:

| Scope | How |
|-------|-----|
| **All your personal agents** | Dashboard → Cloud Agents → My Settings → Disable "Automatically fix CI Failures" |
| **Specific PR** | Comment `@cursor autofix off` on the PR |
| **Re-enable** | Comment `@cursor autofix on` |

### Manual CI Fixing:

> *"If you want cloud agents to fix CI failures in your own PRs, you can simply ask them by tagging Cursor in a comment as normal. For example, `@cursor please fix the CI failures` or `@cursor fix the CI lint check failure`."*

### Availability:

> *"Automatically fixing CI failures is currently only available on Teams; support for non-Teams accounts is coming soon."*

**In the meantime:** You can explicitly ask the cloud agent to monitor and fix CI failures on the PR.

---

## Complete Cloud Agent Workflow Example

Here's how all these capabilities work together:

| Step | What happens |
|------|--------------|
| 1 | You kick off a Cloud Agent to build a new feature |
| 2 | Agent clones your repo, sets up environment |
| 3 | Agent writes code, runs tests |
| 4 | Agent starts dev server, opens browser |
| 5 | Agent clicks through UI to verify feature works |
| 6 | Agent takes screenshots and videos |
| 7 | Agent creates PR with artifacts attached |
| 8 | CI runs on the PR |
| 9 | If CI fails, Agent automatically tries to fix it |
| 10 | You remote into agent's desktop to test yourself |
| 11 | You approve and merge |

**All without you touching your local machine!**

---

## Common Beginner Questions

### Q: What's "computer use"?
**A:** Cloud agents have their own virtual computer with a screen, mouse, and keyboard. They can see and click on things.

### Q: Can I see what the agent is doing?
**A:** Yes – artifacts (screenshots/videos) and remote desktop control let you watch or take over.

### Q: What's an "artifact"?
**A:** Proof of work – screenshots, videos, logs attached to the PR.

### Q: Can the agent fix CI failures automatically?
**A:** Yes, on Teams plans with GitHub Actions. It will try up to 10 times.

### Q: Can I stop the agent from auto-fixing CI?
**A:** Yes – disable in dashboard or comment `@cursor autofix off` on the PR.

### Q: Are MCP servers secure in Cloud Agents?
**A:** HTTP MCPs are more secure (agent never sees credentials). stdio MCPs run inside the VM.

---

## Quick Reference Card

| Capability | What it does |
|------------|--------------|
| **Computer use** | Full desktop with mouse/keyboard, can test UI |
| **Artifacts** | Screenshots, videos, logs attached to PRs |
| **Remote desktop** | You can take control of agent's computer |
| **MCP tools** | Access databases, APIs, external services |
| **Auto CI fix** | Automatically fixes failing GitHub Actions |

---

## Summary for Beginners

| Question | Answer |
|----------|--------|
| **What makes Cloud Agents special?** | They have their own computers with desktops and browsers |
| **What are artifacts?** | Screenshots, videos, logs showing what the agent did |
| **Can I take over?** | Yes – remote desktop control |
| **Can agents test UI?** | Yes – they can click through flows in a browser |
| **Do they fix CI failures?** | Yes (Teams plan, GitHub Actions) |
| **Are they secure?** | HTTP MCPs are more secure; credentials are encrypted |

---

## The Bottom Line

**Cloud Agents are like having a virtual developer with their own computer – they can see, test, and verify their own work.**

**Think of it as:**
- **Local Agent** = Developer without a computer (can only write code) 📝
- **Cloud Agent** = Developer with a full computer (can write, test, see, click) 💻

**For beginners:** You probably don't need Cloud Agents yet. But when you do, the capabilities are amazing – especially **computer use** (they can actually test UI!) and **auto CI fixing** (they fix their own test failures).

**The coolest features:**
1. **Remote desktop control** – You can literally take over the agent's computer
2. **Artifacts** – Screenshots and videos prove the work was done
3. **Auto CI fix** – Agent fixes its own broken tests
4. **Browser control** – Agent clicks through UI flows to verify changes

**Security note:** HTTP MCPs are recommended over stdio for better security (agent never sees credentials). All sensitive configs are encrypted at rest.


This is the **Agents Window** documentation – it describes Cursor's **agent-first interface** where you can manage multiple AI agents across different projects and environments.

Think of the Agents Window as your **command center** for AI agents. Instead of working with one agent in your code editor, you can run many agents simultaneously, across different projects, both locally and in the cloud.

Let me break this down for a complete beginner.

---

## What Is the Agents Window? (The 10-Second Summary)

**The Agents Window is Cursor's dedicated interface for managing AI agents.** It's like switching from a single-player mode to a multiplayer command center.

| Regular Editor | Agents Window |
|----------------|---------------|
| One agent at a time | Many agents in parallel |
| Focus on one file/project | Work across multiple projects |
| Local only | Local + Cloud + SSH |
| Classic coding interface | Agent-first command center |

**Access it with:** `Ctrl + Shift + P` (or `Cmd + Shift + P` on Mac), then type "Open Agents Window"

---

## Key Concept: Two Interfaces, One Tool

Cursor gives you **two ways** to work:

| Interface | Best for |
|-----------|----------|
| **Editor** (classic) | Traditional coding, VS Code extensions, seeing many files at once |
| **Agents Window** | Running multiple agents, managing many projects, higher-level orchestration |

**Important:** You can switch between them anytime, or have both open simultaneously!

---

## How to Open the Agents Window

### From the Editor:
```
Step 1: Press Ctrl+Shift+P (or Cmd+Shift+P on Mac)
Step 2: Type "Open Agents Window"
Step 3: Press Enter
```

### To go back to the Editor:
```
Step 1: Press Ctrl+Shift+P
Step 2: Type "Open Editor Window"
Step 3: Press Enter
```

### While in Agents Window (handy shortcuts):
| Shortcut | What it does |
|----------|--------------|
| `Ctrl+P` | Search for files |
| `Ctrl+Shift+F` | Search across all files |

---

## Features Available ONLY in the Agents Window

These features are exclusive to the Agents Window – you can't get them in the classic editor.

### 1. Multi-Workspace 🌍
**What it does:** Work with agents across all your projects from one place.

**Example:** You have three projects:
- Project A: E-commerce website
- Project B: Mobile app backend
- Project C: Internal dashboard

In the Agents Window, you can have agents working on **all three simultaneously** from a single interface.

**In the regular editor:** You'd have to open one project at a time.

---

### 2. New Diffs View 📊
**What it does:** Review and commit changes, and manage PRs (Pull Requests) without leaving Cursor.

**Why it matters:** You can see what agents changed, approve or reject changes, and manage the whole workflow inside Cursor.

---

### 3. Parallel Agents (in the Cloud) ☁️
**This is the BIG one.** You can run many agents simultaneously in the cloud.

**What "parallel agents" means:**
- Agent 1 is refactoring your backend
- Agent 2 is writing tests
- Agent 3 is updating documentation
- Agent 4 is fixing a bug

**All at the same time!**

**And you can interact with them from:**
| Platform | What you can do |
|----------|-----------------|
| **Phone** | Check progress, give new instructions |
| **Web browser** | Monitor and control agents remotely |
| **Slack** | Get updates and send commands |
| **GitHub** | Agents can create PRs automatically |
| **Linear** | Agents can update issue tracking |

**Analogy:** Regular Cursor is like having one employee. The Agents Window with parallel cloud agents is like having a whole team working for you, and you can manage them from your phone.

---

### 4. Easy Handoff Between Local and Cloud 🔄
**What it does:** Move an agent from cloud to local and back.

**Example workflow:**

| Step | What happens |
|------|--------------|
| 1 | Agent starts working in the cloud (fast, doesn't use your computer) |
| 2 | You want to iterate quickly, so you move it LOCAL |
| 3 | You make quick adjustments on your machine |
| 4 | You move it BACK to the cloud so it keeps working autonomously |

**Why this is powerful:** Get the speed of cloud computing AND the control of local development.

---

### 5. Worktrees 🌿
**What it does:** Run agents in isolated Git checkouts so each task has its own files and changes.

**What is a worktree?** It's like having multiple copies of your project that share the same Git history but keep changes separate.

**Example:**
| Worktree | Task |
|----------|------|
| Worktree 1 | Adding dark mode (agent working here) |
| Worktree 2 | Fixing login bug (different agent) |
| Worktree 3 | Updating documentation (third agent) |

**No conflicts!** Each agent works in its own isolated environment.

**For beginners:** Think of worktrees as separate "sandboxes" where agents can work without messing with each other.

---

## Choosing Between Agents Window and Editor

This is the key decision you'll make as a Cursor user.

### Use the Agents Window when:

| Situation | Why |
|-----------|-----|
| You want to run multiple agents at once | Parallel execution |
| You're managing multiple projects | Multi-workspace |
| You want agents working while you're away | Cloud agents run 24/7 |
| You want to orchestrate at a higher level | Less code-focus, more task-focus |
| You're using agents to write MOST of your code | Let agents do the heavy lifting |

### Use the Editor (classic) when:

| Situation | Why |
|-----------|-----|
| You want the classic IDE experience | Familiar coding environment |
| You need VS Code extensions | Full extension support |
| You want to see many files at once | Flexible screen splitting |
| You're writing most of the code yourself | More control, less delegation |
| You're doing detailed file-by-file work | Fine-grained control |

---

## Visualizing the Difference

| Feature | Editor | Agents Window |
|---------|--------|---------------|
| **Number of agents** | 1 | Many (parallel) |
| **Projects** | 1 at a time | Multiple (multi-workspace) |
| **Agent location** | Local only | Local + Cloud |
| **Remote access** | No | Yes (phone, web, Slack) |
| **Worktrees** | Manual | Built-in |
| **PR management** | External tools | Built-in diff view |
| **VS Code extensions** | Yes | No (different interface) |
| **Best for** | Hands-on coding | Agent orchestration |

---

## Enterprise Access Note

For companies using Cursor Enterprise:

| Timeline | Access |
|----------|--------|
| **First 2 weeks after launch (April 2, 2026)** | Admins can control rollout (give access to specific users or everyone) |
| **After rollout period** | All users have access by default |

**For beginners:** If you're on a personal plan, you already have access (assuming you're using Cursor 3 or later).

---

## Real-World Example: Using the Agents Window

Let me show you what a real session might look like:

### You're building a new web app:

| Step | What you do | What happens |
|------|-------------|--------------|
| 1 | Open Agents Window | You see your command center |
| 2 | Create Agent 1 | "Build the login page" (runs in cloud) |
| 3 | Create Agent 2 | "Set up the database" (runs in cloud) |
| 4 | Create Agent 3 | "Write API documentation" (runs locally) |
| 5 | Go to lunch | Agents keep working in the cloud |
| 6 | Check on your phone | See progress via Slack updates |
| 7 | Return to computer | Move Agent 1 local to tweak the design |
| 8 | Move it back to cloud | Agent continues autonomously |

**All of this happens simultaneously.** You're not waiting – you're orchestrating.

---

## Beginner's Guide: Which One Should You Use?

### Start with the Editor if:
- You're new to coding
- You want to learn how Cursor works
- You're working on one small project
- You want to write most code yourself

### Switch to Agents Window when:
- You have multiple tasks/projects
- You want agents working while you're away
- You're comfortable delegating to AI
- You want to scale up your productivity

### Progression path:
```
Week 1-2: Use Editor + single Agent
Week 3-4: Try Agents Window with 2-3 agents
Week 5+: Run multiple cloud agents, manage from phone
```

---

## Summary for Beginners

| Question | Answer |
|----------|--------|
| **What is it?** | A dedicated workspace for managing multiple AI agents |
| **How to open?** | `Ctrl+Shift+P` → "Open Agents Window" |
| **Key features?** | Multi-workspace, parallel agents, cloud agents, worktrees |
| **Vs. Editor?** | Editor = classic coding; Agents Window = agent orchestration |
| **Can I use both?** | Yes! Switch anytime or use simultaneously |
| **Do I need it?** | Not as a beginner, but powerful as you grow |

---

## The Bottom Line

**The Agents Window is for power users who want to run multiple AI agents across multiple projects simultaneously.**

**Think of it as:**
- **Editor** = Your personal coding desk ✍️
- **Agents Window** = Your AI command center 🎮

**For beginners:** Start with the classic Editor and one Agent. Master that first. Once you're comfortable, explore the Agents Window. It's like upgrading from driving one car to managing a whole fleet.

**The most exciting features:**
1. **Parallel agents** – Multiple agents working at once
2. **Cloud agents** – They work even when your computer is off
3. **Remote management** – Check progress from your phone
4. **Worktrees** – Isolated environments for each task

Would you like me to explain any of these features in more detail, or walk through a specific example of using multiple parallel agents?
# Cursor Training – Exercise 22

## CLI – List & Resume Sessions

**Objective:** List previous CLI sessions and resume them – maintaining context and continuing conversations across multiple terminal sessions.

**Time:** 10 minutes

**Setup:** Cursor CLI installed (from Exercise 19), at least one previous conversation to resume

---

## Step-by-Step Instructions

| Step | Action | Expected Result |
|------|--------|-----------------|
| 1 | Open your terminal | Command prompt appears |
| 2 | Run `agent ls` to list previous sessions | List of past conversations appears |
| 3 | Pick a session ID from the list | Session identified |
| 4 | Run `agent --resume <session-id>` | Conversation continues from where it left off |
| 5 | Run `agent --continue` to resume most recent | Latest conversation resumes |

---

## What are CLI Sessions?

| Aspect | Description |
|--------|-------------|
| **Session** | A complete conversation with the Agent |
| **Saved automatically** | Every interactive session is saved |
| **Contains** | Full conversation history, context, file state |
| **Session ID** | Unique identifier (timestamp or hash) |
| **Resume** | Pick up exactly where you left off |

---

## List Previous Sessions

### Command

```bash
agent ls
```

**Expected output:**

```
┌─────────────────────────────────────────────────────────────────┐
│  CURSOR CLI SESSIONS                                            │
├─────────────────────────────────────────────────────────────────┤
│  ID                  | DATE          | STATUS   | MESSAGES      │
│  2025-01-15-10-30-45 | Jan 15 10:30  | Complete | 12            │
│  2025-01-14-16-20-12 | Jan 14 16:20  | Complete | 8             │
│  2025-01-13-09-15-30 | Jan 13 09:15  | Complete | 5             │
│  2025-01-12-14-45-00 | Jan 12 14:45  | Complete | 23            │
└─────────────────────────────────────────────────────────────────┘

Run: agent --resume <id> to continue a session
```

### With Cloud Agents

```bash
agent ls --cloud
```

**Expected output:**

```
┌─────────────────────────────────────────────────────────────────┐
│  CLOUD AGENT SESSIONS                                           │
├─────────────────────────────────────────────────────────────────┤
│  AGENT ID            | STATUS    | CREATED      | OUTPUT        │
│  ca_abc123xyz        | Completed | Jan 15 10:30 | PR #123       │
│  ca_def456uvw        | Running   | Jan 15 11:00 | In progress   │
│  ca_ghi789rst        | Failed    | Jan 14 16:20 | Error: build  │
└─────────────────────────────────────────────────────────────────┘
```

---

## Resume a Session

### Resume Most Recent Session

```bash
agent --continue
```

or

```bash
agent resume
```

**Expected behavior:** Continues your most recent conversation as if you never left.

### Resume Specific Session by ID

```bash
agent --resume 2025-01-15-10-30-45
```

**Expected behavior:** Loads that exact conversation, including all previous messages and context.

---

## Complete Example Workflow

### Session 1 (Morning)

```bash
$ agent

> Explain the main function in calculator.c

[Agent explains]

> Add error handling to the divide function

[Agent makes changes]

> /quit

Goodbye!
```

### Later That Day (After Lunch)

```bash
$ agent ls

ID: 2025-01-15-10-30-45 | Date: Jan 15 10:30 | Messages: 4

$ agent --resume 2025-01-15-10-30-45

Resuming session from Jan 15 10:30
Continuing conversation...

> Now also add error handling to the other functions

[Agent continues where you left off]
```

---

## Session Management Commands

| Command | Description |
|---------|-------------|
| `agent ls` | List all local sessions |
| `agent ls --cloud` | List cloud agent sessions |
| `agent --continue` | Resume most recent session |
| `agent resume` | Same as `--continue` |
| `agent --resume <id>` | Resume specific session by ID |
| `agent --clear` | Clear conversation history (start fresh) |
| `/clear` | Clear current conversation (in interactive mode) |

---

## Why Resume Sessions?

| Benefit | Description |
|---------|-------------|
| **Context preservation** | Agent remembers everything discussed |
| **Time savings** | No need to re-explain the problem |
| **Multi-session workflows** | Complex tasks across multiple days |
| **Experiment tracking** | Return to previous attempts |
| **Team collaboration** | Share session IDs (coming soon) |

---

## Success Criteria

- [ ] Ran `agent ls` and saw previous sessions
- [ ] Identified a session to resume
- [ ] Used `agent --continue` to resume most recent
- [ ] Agent remembered previous conversation
- [ ] Used `agent --resume <id>` for a specific session
- [ ] (Optional) Used `agent ls --cloud` to see cloud agents

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| `agent ls` shows no sessions | You need at least one previous conversation. Start and quit a session first |
| Session not found | Check the ID exactly as shown. Use `agent ls` to verify |
| Resumed session doesn't remember context | Make sure you're using the correct session ID |
| Can't resume cloud agent | Cloud agents are resumed via `--resume` with agent ID, not session ID |
| Session corrupted | Start a new session with `/new-chat` in interactive mode |

---

## Key Takeaway

**Session management lets you pause and resume conversations – just like saving your game progress.**

Use it when:
- You need to step away from a complex task
- You want to continue a conversation the next day
- You're experimenting with different approaches
- You need to share context across multiple terminal sessions

---

## Bonus Challenge (If Time Permits)

Create a session, add some context, then resume it in a different terminal:

**Terminal 1:**

```bash
$ agent
> Remember that the divide function needs division by zero checking
> /quit
```

**Terminal 2:**

```bash
$ agent ls
$ agent --continue
> What did we discuss about the divide function?
```

The Agent should remember the previous discussion.

Or script session management:

```bash
#!/bin/bash
# resume-latest.sh
LATEST=$(agent ls | tail -1 | awk '{print $1}')
agent --resume "$LATEST"
```

---

## Exercise Complete ✓

Check off when done:
- [ ] Ran `agent ls` and saw sessions
- [ ] Used `agent --continue` to resume most recent
- [ ] Agent remembered previous conversation
- [ ] Used `agent --resume <id>` for specific session
- [ ] (Optional) Ran `agent ls --cloud`
- [ ] (Optional) Completed bonus challenge

**Next:** Exercise 23 – Launch Cloud Agent (Web Dashboard)

---

## Quick Reference: Session Management Cheat Sheet

```
┌─────────────────────────────────────────────────────────────────┐
│                 SESSION MANAGEMENT CHEAT SHEET                  │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  LIST SESSIONS:                                                 │
│  agent ls                 # Local sessions                      │
│  agent ls --cloud         # Cloud agent sessions                │
│                                                                 │
│  RESUME SESSIONS:                                               │
│  agent --continue         # Most recent session                 │
│  agent resume             # Same as above                       │
│  agent --resume <id>      # Specific session by ID              │
│                                                                 │
│  SESSION ID FORMATS:                                            │
│  Local: 2025-01-15-10-30-45 (timestamp)                         │
│  Cloud: ca_abc123xyz (agent ID)                                 │
│                                                                 │
│  INTERACTIVE COMMANDS:                                          │
│  /clear      - Clear current conversation                       │
│  /new-chat   - Start a brand new session                        │
│  /quit       - Save and exit                                    │
│                                                                 │
│  TYPICAL WORKFLOW:                                              │
│  Morning:                                                       │
│  $ agent                                                        │
│  > Work on feature X...                                         │
│  > /quit                                                        │
│                                                                 │
│  After lunch:                                                   │
│  $ agent --continue                                             │
│  > Continue with feature X...                                   │
│                                                                 │
│  SESSION BENEFITS:                                              │
│  • No need to re-explain context                                │
│  • Complex tasks across multiple sessions                       │
│  • Experiment without losing progress                           │
│  • Resume after computer restart                                │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

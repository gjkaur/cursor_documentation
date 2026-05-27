# Cursor Training Program — Post-Training Assessment (MCQ-Based)

## For Working Professionals — After Completing Training

---

## Instructions

| Aspect | Details |
|--------|---------|
| **Time Limit** | 15-20 minutes |
| **Format** | Multiple Choice Questions (MCQ) only |
| **Number of Questions** | 40 questions |
| **Passing Score** | 70% (28/40 correct) |
| **Purpose** | Measure knowledge gain after completing the training |

---

**Name (Optional):** ______________________________

**Date:** ______________________________

**Training Cohort:** ______________________________

---

## Section 1: Mental Models & Foundations (5 questions)

---

**Q1. You ask an AI model the same question twice and get slightly different answers. Why does this happen?**

- A) The AI is malfunctioning
- B) AI models are probabilistic, not deterministic – they predict likely tokens, not exact answers
- C) Your internet connection is unstable
- D) The AI is intentionally being unpredictable

---

**Q2. An AI confidently suggests using a function `i2c_write_register_stm32_hal_v3()` that doesn't exist in your codebase. What is this phenomenon called?**

- A) Compilation error
- B) Token limit issue
- C) Hallucination
- D) Optimization

---

**Q3. Your team wants to reduce AI costs. Which strategy would be most effective?**

- A) Always use the most expensive model for better quality
- B) Use cheaper models for simple tasks and reserve expensive models for complex work
- C) Increase context window to maximum for every request
- D) Disable all caching

---

**Q4. What is the single most valuable skill when working with AI coding assistants?**

- A) Knowing multiple programming languages
- B) Managing what the model "sees" (context engineering)
- C) Writing the shortest possible prompts
- D) Always using the latest model

---

**Q5. What is the key difference between a "chatbot" and an "agent"?**

- A) Chatbots are free; agents cost money
- B) Chatbots respond to prompts; agents pursue multi-step goals and take actions
- C) Chatbots work offline; agents require internet
- D) There is no meaningful difference

---

## Section 2: Cursor Editor Essentials (5 questions)

---

**Q6. You open a large, unfamiliar firmware codebase. What is the most effective first step?**

- A) Immediately ask the agent to refactor all drivers
- B) Ask: "Explain this codebase – main entry points, key modules"
- C) Manually read every file line by line
- D) Create a pull request with documentation

---

**Q7. You need to add a complex feature across multiple files and want the AI to plan first. What should you use?**

- A) Ask Mode
- B) Plan Mode (Shift+Tab)
- C) Direct coding request
- D) Cloud Agent only

---

**Q8. What is the purpose of @mentions (e.g., `@timers.c @TIM2_IRQHandler`) in Cursor?**

- A) Tag a team member for review
- B) Point the agent to exact files, symbols, or context
- C) Create a hyperlink in comments
- D) Format code automatically

---

**Q9. Before letting an AI make significant changes to your code, what should you create as a safety net?**

- A) A new branch in git
- B) A checkpoint in Cursor
- C) A backup of the entire project
- D) All of the above

---

**Q10. You ask the AI to change a variable name. The AI also renames other variables and reformats the file. What should you do?**

- A) Accept all changes
- B) Review the diff, reject unwanted changes, and ask the AI to be more focused
- C) Close the session and start over
- D) Disable the AI

---

## Section 3: Agent Modes & Tools (5 questions)

---

**Q11. What is the difference between Ask Mode and Agent Mode?**

- A) Ask Mode is faster; Agent Mode is slower
- B) Ask Mode is read-only; Agent Mode can make changes and run tools
- C) Ask Mode uses free models; Agent Mode uses paid models
- D) There is no difference

---

**Q12. Your firmware is crashing. You want the AI to see debug output and diagnose the issue. Which tool should the AI use?**

- A) Browser Tool
- B) Terminal Tool
- C) Files Tool only
- D) Cannot do this

---

**Q13. You want the AI to inspect a live web dashboard showing sensor data. Which tool should it use?**

- A) Terminal Tool
- B) Browser Tool
- C) Files Tool
- D) MCP only

---

**Q14. You ask the AI to run `make` and fix compilation errors. The AI requests approval. Why?**

- A) The AI is malfunctioning
- B) Terminal commands require approval by default for safety
- C) Your API key is invalid
- D) The command is malformed

---

**Q15. Which is an example of an effective, constrained prompt?**

- A) "Fix the bug"
- B) "Fix the IndexError when input list is empty. Do not change function signature. Show the diff."
- C) "Make the code better"
- D) "Rewrite everything"

---

## Section 4: Customizing Cursor (4 questions)

---

**Q16. Where should you encode team coding standards so the AI follows them automatically?**

- A) In a Slack message
- B) In a `.cursor/rules/*.mdc` file
- C) In a README.md
- D) In an email to the team

---

**Q17. What is a "Skill" in Cursor?**

- A) A keyboard shortcut
- B) A reusable, specialized workflow invoked by name (e.g., `/pr-review`)
- C) A type of AI model
- D) A debugging tool

---

**Q18. What does MCP (Model Context Protocol) enable?**

- A) Faster code completion
- B) Connecting external tools (GitHub, Slack, Jira) for the agent to use
- C) Voice control of Cursor
- D) Automatic code formatting

---

**Q19. What is a Subagent?**

- A) A less intelligent AI model
- B) A separate agent instance that handles specialized tasks in parallel
- C) A bug in the agent
- D) A type of prompt template

---

## Section 5: CLI & Automation (4 questions)

---

**Q20. How do you run a one-shot AI command from the terminal without entering an interactive session?**

- A) `agent`
- B) `agent "your prompt here"`
- C) `cursor --gui`
- D) `ai run`

---

**Q21. You need to run a long code analysis task (30+ minutes) and close your laptop. What should you use?**

- A) Local Agent in Ask Mode
- B) Cloud Agent
- C) Terminal one-shot command
- D) Cannot run long tasks offline

---

**Q22. What does the `/resume` command do in the Cursor CLI?**

- A) Restart the current session
- B) List previous sessions and resume one
- C) Save the current conversation
- D) Clear the context window

---

**Q23. How do you hand off a local session to a Cloud Agent from the CLI?**

- A) Prefix message with `&` (e.g., `& "Run this task"`)
- B) Use `--cloud` flag
- C) Use `/cloud` command
- D) Cannot do this from CLI

---

## Section 6: Cloud Agents API & Webhooks (6 questions)

---

**Q24. What are the two required fields when creating a Cloud Agent via API?**

- A) `agent.name` and `agent.description`
- B) `prompt.text` and `repos[].url`
- C) `model.id` and `temperature`
- D) `webhookUrl` and `webhookSecret`

---

**Q25. What are Server-Sent Events (SSE) used for in the Cloud Agents API?**

- A) Encrypting API requests
- B) Streaming real-time agent responses (thoughts, tool calls, output)
- C) Batch processing multiple agents
- D) Scheduled agent execution

---

**Q26. How do you verify a webhook genuinely came from Cursor?**

- A) Check the sender email address
- B) Verify the HMAC-SHA256 signature in `X-Webhook-Signature` header
- C) Trust it because it came over HTTPS
- D) Compare payload with known example

---

**Q27. What is the purpose of ngrok when testing webhooks locally?**

- A) Debug API responses
- B) Expose local webhook server to the internet for Cursor to reach
- C) Encrypt webhook payloads
- D) Cache webhook responses

---

**Q28. What are "artifacts" in Cloud Agents?**

- A) Bugs in the agent's code
- B) Files produced by the agent (logs, screenshots, generated code)
- C) The agent's configuration files
- D) Unused code

---

**Q29. How long are artifact download URLs valid?**

- A) 1 hour
- B) 15 minutes
- C) 24 hours
- D) 7 days

---

## Section 7: Admin & Analytics APIs (5 questions)

---

**Q30. What is the primary difference between a User API Key and an Admin API Key?**

- A) User keys expire faster
- B) Admin keys can access team usage data and manage members
- C) User keys are free; Admin keys cost extra
- D) There is no difference

---

**Q31. Your manager wants a report showing total AI spending per day for the last 30 days. Which endpoint should you use?**

- A) `GET /v1/admin/members`
- B) `GET /v1/admin/analytics/usage/daily`
- C) `POST /v1/agents`
- D) `GET /v1/models`

---

**Q32. How do you prevent a team member from exceeding $50 in AI usage per month?**

- A) Configure a webhook alert
- B) Set a user spend limit via `PATCH /v1/admin/policies/users/{userId}/limits`
- C) Create a repository instruction
- D) Create a skill

---

**Q33. What is the recommended safe pattern for removing a team member?**

- A) Immediately hard delete the account
- B) Audit → deactivate (soft delete) → transfer ownership → (optional) hard delete
- C) Just remove their email from the team list
- D) Revoke only their API keys

---

**Q34. When creating a leaderboard for team usage, what is a responsible practice?**

- A) Show full names and exact costs
- B) Anonymize users and focus on positive metrics (efficiency, savings)
- C) Only show it to managers
- D) Publish it publicly

---

## Section 8: AI Code Tracking & Reporting (3 questions)

---

**Q35. What does the AI commit metrics endpoint measure?**

- A) Number of commits per day
- B) Per-commit attribution of AI-generated vs. human-written lines
- C) Which AI model was used most frequently
- D) Speed of code reviews

---

**Q36. Your team uses Tableau for dashboards. What is the most efficient way to export AI usage data?**

- A) Copy-paste from Cursor UI
- B) Use streaming CSV export (`/admin/analytics/export/csv`)
- C) Take screenshots
- D) Manually type data into Excel

---

**Q37. What information does a granular AI change event include?**

- A) Only the file name
- B) File path, line range, model, user, timestamp, original and new code
- C) Only the user who made the change
- D) Only the timestamp

---

## Section 9: Practical Scenarios (3 questions)

---

**Q38. You inherit a legacy firmware codebase with no documentation. What is your first step?**

- A) Ask AI to rewrite everything
- B) Ask AI: "Trace the data flow from sensor to application. Identify all files involved."
- C) Manually read every file
- D) Give up and recommend replacing the system

---

**Q39. You need to add a watchdog timer across 5 files. What workflow ensures safety?**

- A) Tell AI "Add watchdog timer" and accept all changes
- B) Use Plan Mode → review plan → execute step by step → review each diff
- C) Make all changes manually
- D) Ask a junior engineer to do it

---

**Q40. An auditor asks for a record of all AI-generated code changes in the last 90 days. How do you provide this?**

- A) Say you don't have it
- B) Export granular events via `/admin/analytics/events` to CSV
- C) Ask each developer to self-report
- D) Provide only the total cost

---

## Answer Sheet (For Participants to Fill)

| Q# | Answer | Q# | Answer | Q# | Answer | Q# | Answer |
|----|--------|----|--------|----|--------|----|--------|
| 1 | | 11 | | 21 | | 31 | |
| 2 | | 12 | | 22 | | 32 | |
| 3 | | 13 | | 23 | | 33 | |
| 4 | | 14 | | 24 | | 34 | |
| 5 | | 15 | | 25 | | 35 | |
| 6 | | 16 | | 26 | | 36 | |
| 7 | | 17 | | 27 | | 37 | |
| 8 | | 18 | | 28 | | 38 | |
| 9 | | 19 | | 29 | | 39 | |
| 10 | | 20 | | 30 | | 40 | |

---

## Answer Key (For Instructors Only)

| Q# | Answer | Q# | Answer | Q# | Answer | Q# | Answer |
|----|--------|----|--------|----|--------|----|--------|
| 1 | B | 11 | B | 21 | B | 31 | B |
| 2 | C | 12 | B | 22 | B | 32 | B |
| 3 | B | 13 | B | 23 | A | 33 | B |
| 4 | B | 14 | B | 24 | B | 34 | B |
| 5 | B | 15 | B | 25 | B | 35 | B |
| 6 | B | 16 | B | 26 | B | 36 | B |
| 7 | B | 17 | B | 27 | B | 37 | B |
| 8 | B | 18 | B | 28 | B | 38 | B |
| 9 | D | 19 | B | 29 | B | 39 | B |
| 10 | B | 20 | B | 30 | B | 40 | B |

---

## Scoring Summary

| Section | Questions | Correct | Score |
|---------|-----------|---------|-------|
| Section 1: Mental Models | 1-5 | ___ / 5 | |
| Section 2: Editor Essentials | 6-10 | ___ / 5 | |
| Section 3: Agent Modes & Tools | 11-15 | ___ / 5 | |
| Section 4: Customizing Cursor | 16-19 | ___ / 4 | |
| Section 5: CLI & Automation | 20-23 | ___ / 4 | |
| Section 6: Cloud Agents API | 24-29 | ___ / 6 | |
| Section 7: Admin & Analytics | 30-34 | ___ / 5 | |
| Section 8: AI Code Tracking | 35-37 | ___ / 3 | |
| Section 9: Practical Scenarios | 38-40 | ___ / 3 | |
| **Total** | **1-40** | **___ / 40** | |

---

## Score Interpretation

| Score | Percentage | Interpretation |
|-------|------------|----------------|
| 36-40 | 90-100% | Excellent |
| 32-35 | 80-89% | Very Good |
| 28-31 | 70-79% | Good (Passing) |
| 24-27 | 60-69% | Needs Review |
| Below 24 | Below 60% | Recommend Retraining |

---

*End of Post-Training Assessment (MCQ-Based)*
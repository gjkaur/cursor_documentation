# Cursor Training Program — Pre-Training Knowledge Assessment

---

## Instructions

| Aspect | Details |
|--------|---------|
| **Time Limit** | 8-10 minutes |
| **Format** | Multiple choice + scenario questions |
| **Purpose** | Assess baseline knowledge of AI coding concepts (not Cursor-specific) |
| **Note** | Your survey responses already captured your role, experience, and goals. This assessment focuses only on **knowledge.** |

---

**Name (Optional):** ______________________________

**Date:** ______________________________

---

## Section 1: General AI Coding Concepts (4 minutes)

*These questions test your existing understanding of how AI coding assistants work – no Cursor experience required.*

**Instructions:** Circle the letter of the best answer for each question.

---

**1.1 When you give a prompt to an AI coding assistant, what determines its response?**

A) The AI searches the internet for matching code

B) The AI predicts the most likely sequence of tokens based on patterns it learned during training

C) The AI compiles and runs code before responding

D) The AI gives the same response every time for the same prompt

**Answer:** _______

---

**1.2 You ask an AI to "write a function to parse a CSV file." It gives you code using a library that doesn't exist. What is this called?**

A) A syntax error

B) A hallucination

C) A token limit issue

D) A compilation error

**Answer:** _______

---

**1.3 If an AI coding assistant has a "context window" of 200,000 tokens (approximately 150 pages of text), what happens when you exceed that limit?**

A) The request fails with an error

B) The oldest information gets truncated (forgotten)

C) The AI automatically summarizes the conversation

D) Nothing – context windows are unlimited

**Answer:** _______

---

**1.4 What is a "prompt" in AI-assisted coding?**

A) A keyboard shortcut to run code

B) The instruction or question you give to the AI

C) A type of programming paradigm

D) A debugging tool

**Answer:** _______

---

**1.5 Which statement best describes how an AI coding assistant handles your previous messages?**

A) It remembers everything across all your projects forever

B) It only remembers the current conversation until you close it (or within context limits)

C) It never remembers anything – each message is independent

D) Only paid versions have memory

**Answer:** _______

---

**1.6 What does it mean to "ground" an AI response?**

A) To make the AI run slower intentionally

B) To provide source material (like documentation or code) for the AI to reference

C) To limit the AI's output length

D) To switch between different AI models

**Answer:** _______

---

## Section 2: Prompting & Workflow Scenarios (3 minutes)

*These scenarios test how you currently approach tasks with AI coding tools.*

---

**2.1 You need to understand what an unfamiliar function does. Which prompt would likely get the best result?**

A) "What does this code do?"

B) "Explain this function line by line, including its inputs, outputs, edge cases, and any potential bugs"

C) "Tell me about this"

D) "Is this code correct?"

**Answer:** _______

---

**2.2 You receive AI-generated code that looks mostly correct but makes changes beyond what you asked for (e.g., renames variables, reorganizes unrelated code). What is this called, and what should you do?**

A) "Scope creep" – ask the AI to only change the specific lines next time

B) "Compilation" – accept it since it works

C) "Refactoring" – always let the AI do this

D) "Optimization" – ignore it

**Answer:** _______

---

**2.3 You want the AI to help debug an error. Which approach is most effective?**

A) Just say "This doesn't work" without showing the error

B) Provide the relevant code file, the exact error message, and describe what you expected to happen

C) Ask the AI to "rewrite everything"

D) Try a different programming language

**Answer:** _______

---

**2.4 You are about to ask an AI to make a significant change to your code. What should you do before you start?**

A) Nothing – just proceed

B) Save a copy of your current working state (e.g., commit to git or use checkpoints)

C) Delete all existing code to start fresh

D) Disable all safety features

**Answer:** _______

---

**2.5 You ask an AI to generate code. Which of these would help you trust the output more?**

A) Asking the AI to explain its reasoning before showing code

B) Reviewing the changes line by line before accepting

C) Running tests after accepting changes

D) All of the above

**Answer:** _______

---

## Section 3: Terminal & Tools Familiarity (1 minute)

*These questions assess comfort with letting AI run commands.*

---

**3.1 Would you trust an AI coding assistant to run terminal commands (e.g., `make`, `git`, `pytest`) on your behalf?**

A) Yes, without any approval

B) Only if I approve each command first

C) No, never

D) I didn't know AI could do this

**Answer:** _______

---

**3.2 Which of these would you consider safe for an AI to run without explicit approval?** (Select all that apply)

- [ ] `python --version`
- [ ] `rm -rf /`
- [ ] `git push --force`
- [ ] `ls -la`
- [ ] `pytest tests/`
- [ ] `sudo make install`

---

## Section 4: Team & Governance (1 minute)

*These questions assess familiarity with team-level AI considerations.*

---

**4.1 If your team uses AI coding assistants, do you have any concerns about?** (Select all that apply)

- [ ] Cost tracking (who is spending how much)
- [ ] Security (code being sent to external APIs)
- [ ] Consistency (different team members using different models or prompting styles)
- [ ] No concerns
- [ ] Not applicable / team doesn't use AI yet

---

**4.2 Should an AI agent be able to automatically create pull requests from its own changes?**

A) Yes, always

B) Yes, but only with review before merging

C) No, never

D) I don't know what this means

**Answer:** _______

---

## Section 5: Open-Ended (Optional)

---

**5.1 What is one thing you wish your current AI coding tool did better?**

_________________________________________________________________

_________________________________________________________________

_________________________________________________________________

_________________________________________________________________

---

**5.2 What is your biggest hesitation about relying more on AI for coding tasks?**

_________________________________________________________________

_________________________________________________________________

_________________________________________________________________

_________________________________________________________________

---

## Answer Key (For Instructor Use Only – Do Not Include in Participant Document)

### Section 1: General AI Concepts

| Question | Correct Answer |
|----------|----------------|
| 1.1 | B |
| 1.2 | B |
| 1.3 | B |
| 1.4 | B |
| 1.5 | B |
| 1.6 | B |

### Section 2: Prompting & Workflow

| Question | Correct Answer |
|----------|----------------|
| 2.1 | B |
| 2.2 | A |
| 2.3 | B |
| 2.4 | B |
| 2.5 | D |

### Section 3: Terminal & Tools

| Question | Correct Answer |
|----------|----------------|
| 3.1 | B |
| 3.2 | `python --version`, `ls -la`, `pytest tests/` |

### Section 4: Team & Governance

| Question | Purpose |
|----------|---------|
| 4.1 | Identifies team concerns (no single correct answer) |
| 4.2 | B (safe practice – review before merging) |

---

*End of Assessment*


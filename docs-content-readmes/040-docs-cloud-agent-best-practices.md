This is the **Cloud Agent Best Practices** documentation – it provides practical recommendations to get **more reliable Cloud Agent runs**.

Think of this as **how to set up your agent for success** – like giving a new team member the right tools, environment, and instructions before they start working.

Let me break this down.

---

## The Core Philosophy

> *"Think of the agent as a smart, but low-context human developer. The best way to make sure it does the right thing is to give it the context it needs to understand what to do."*

**Key insight:** Agents are smart, but they don't know your specific project. You need to **give them context** just like you would a new developer on your team.

---

## Best Practice 1: Set Up the Environment First

**Use Cloud agent setup so that Cursor has its environment configured.**

| Without Environment Setup | With Environment Setup |
|--------------------------|------------------------|
| Agent missing dependencies | All dependencies installed |
| Can't run builds or tests | Can build and test |
| Wastes time figuring out setup | Ready to work immediately |

> *"Like a human developer, Cursor does better work if its environment is set up correctly."*

**How:** Configure environment through the Cloud Agents dashboard or `.cursor/environment.json`.

---

## Best Practice 2: Ensure the Agent Can Access What It Needs

Before running a Cloud Agent, verify these **three prerequisites**:

### 1. Secrets 🔑

Make sure the agent has access to required secrets (API keys, database credentials, etc.) through the **Secrets tab** in your dashboard.

**Examples:** Database passwords, third-party API keys, service account tokens.

### 2. Egress Controls (Network Access) 🌐

If you have network access restrictions enabled, ensure **all URLs your local development requires are whitelisted**.

**Examples:** Your internal API endpoints, package registries (npm, PyPI), cloud service URLs.

### 3. Local Testability ✅

> *"Your repo should be set up to run well locally without requiring external services that cannot be reached from a VM. If it is hard for a human developer to test locally, it will also be hard for an agent."*

**What this means:** If a human needs special access or manual steps to test your code, the agent will struggle too.

**For best results:** Make sure your project can be:
- Cloned fresh
- Dependencies installed (`npm install`, `pip install`, etc.)
- Tests run (`npm test`)
- All with minimal manual configuration

---

## Best Practice 3: Use Skills and AGENTS.md to Configure Your Agent

If the cloud agent is having difficulty testing its changes, use **skills** and **AGENTS.md** to configure your agent.

### Example from Cursor (the company):

> *"At Cursor our `AGENTS.md` lists tips for running and debugging the most commonly used microservices in our mono-repo. We also have lots of skills about how to test and debug key services, each with clear instructions on when to use the skill."*

### What to Include in AGENTS.md:

| Type | Example |
|------|---------|
| **Running services** | "To start the auth service, run `npm run start:auth`" |
| **Debugging tips** | "If database connection fails, check that Docker is running" |
| **Common issues** | "The test suite requires a `.env.test` file – copy from `.env.example`" |

### What to Include in Skills:

> *"The skills contain in-depth details, such as how to debug a specific microservice or how to set up a third-party dependency when needed for testing."*

**Examples of useful skills:**
- "How to debug the payment service"
- "How to set up the test database"
- "How to run end-to-end tests"

---

## Best Practice 4: Give the Agent the Tools It Needs

> *"We have often found that agents are limited by the tools they have access to. We recommend using MCP and creating custom tools so that the agent has access to the same systems a human developer would."*

### Examples of Tools to Give Your Agent:

| Tool Type | Example |
|-----------|---------|
| **MCP servers** | Connect to databases, internal APIs, monitoring systems |
| **Custom CLI tools** | Scripts that simplify complex operations |
| **Package scripts** | Well-documented npm/pip/poetry commands |

### Without vs. With Tools:

| Without Tools | With Tools |
|---------------|------------|
| Agent has to figure out complex commands | Agent uses simple, well-defined commands |
| Might miss steps | Clear instructions for each operation |
| Inconsistent results | Reliable, repeatable actions |

---

## Best Practice 5: Mold the Tools to the Agent

> *"It is important to create tools that the agent is good at using. We recommend creating tools, and iterating based on observations of how the agent uses them."*

### Real Example from Cursor:

> *"At Cursor we have created a custom CLI for the model to run micro-services in our codebase. We found that when running custom dev commands, e.g. from a `package.json` file, some models would forget arguments, or agents would get distracted by noisy build logs which human developers knew to ignore."*

### The Problem:

| Issue | Example |
|-------|---------|
| **Forgetting arguments** | Agent runs `npm run dev` instead of `npm run dev -- --port 3000` |
| **Noisy logs** | Build logs with warnings that humans ignore distract the agent |

### The Solution:

Create **custom tools** that:
- Hide complexity behind simple commands
- Filter out irrelevant log noise
- Provide clear success/failure signals

### Iteration Process:

| Step | What to do |
|------|------------|
| 1 | Watch how the agent uses existing tools |
| 2 | Identify where it struggles |
| 3 | Create or modify tools to address those struggles |
| 4 | Repeat |

---

## Summary of Best Practices

| # | Best Practice | Key Takeaway |
|---|---------------|--------------|
| 1 | **Set up the environment first** | Configure deps, secrets, network before running |
| 2 | **Ensure access to what it needs** | Secrets, network, local testability |
| 3 | **Use skills and AGENTS.md** | Give context like you would a new developer |
| 4 | **Give it the tools it needs** | MCP + custom tools = same access as humans |
| 5 | **Mold tools to the agent** | Create tools that hide complexity, iterate |

---

## Quick Reference Card

| Concept | Recommendation |
|---------|----------------|
| **Environment** | Configure before first run |
| **Secrets** | Use Secrets tab in dashboard |
| **Network** | Whitelist required URLs |
| **Testability** | Make local testing easy |
| **Context** | Use AGENTS.md and skills |
| **Tools** | Give same access as human developers |
| **Iteration** | Watch, learn, improve tools |

---

## The Bottom Line

**Cloud agents are powerful, but they need the right setup, context, and tools to be effective.**

**Think of it as:**
- **Without best practices** = New developer with no documentation or tools 🆕😕
- **With best practices** = New developer with setup script, docs, and helpful tools 🆕✨

**The golden rule:** If a human developer would struggle to set up and test your code without help, an agent will struggle too. Make your project **agent-friendly** by:
1. Providing clear setup instructions
2. Giving access to needed secrets and services
3. Creating simple, reliable tools
4. Documenting debugging and testing steps

Would you like me to explain any specific best practice in more detail?
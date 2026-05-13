This is the **Headless CLI** documentation – it explains how to use Cursor CLI in **scripts and automation workflows** for code analysis, generation, and refactoring tasks.

Think of this as **Cursor for CI/CD** – you can run AI-powered code reviews, batch processing, and automated refactoring without any human intervention.

Let me break this down.

---

## What Is Headless Mode? (The 10-Second Summary)

**Use Cursor CLI in scripts and automation workflows for code analysis, generation, and refactoring tasks.**

| Interactive CLI | Headless CLI |
|-----------------|--------------|
| Human at keyboard | Scripts and automation |
| Confirmation prompts | No prompts (with `--force`) |
| One task at a time | Batch processing |
| Manual review | Automated pipelines |

> *"Use `--print` mode (`-p`, `--print`) for non-interactive scripting and automation."*

---

## File Modification in Scripts

By default, `--print` mode **only proposes changes** – it doesn't actually modify files.

### To Actually Modify Files:

Use `--force` (or `--quiet`):

```bash
# Enable file modifications in print mode
agent -p --force "Refactor this code to use modern ES6+ syntax"

# Without --force, changes are only proposed, not applied
agent -p "Add JSDoc comments to this file"  # Won't modify files
```

### Batch Processing Example:

```bash
# Batch processing with actual file changes
find src/ -name "*.js" | while read file; do
  agent -p --force "Add comprehensive JSDoc comments to $file"
done
```

> *"The `--force` flag allows the agent to make direct file changes without confirmation."*

---

## Setup

```bash
# Install Cursor CLI (macOS, Linux, WSL)
curl https://cursor.com/install -fsS | bash

# Install Cursor CLI (Windows PowerShell)
irm 'https://cursor.com/install?win32=true' | iex

# Set API key for scripts
export CURSOR_API_KEY=your_api_key_here

# Run headless
agent -p "Analyze this code"
```

---

## Output Formats

| Flag | Description |
|------|-------------|
| `--output-format text` | Clean, final-answer-only responses (default for `--print`) |
| `--output-format json` | Structured JSON output for scripting |
| `--output-format stream-json` | Message-level progress tracking |
| `--stream-partial-output` | Incremental streaming of deltas |

---

## Example Scripts

### Simple Codebase Question

```bash
#!/bin/bash
# Simple codebase question - uses text format by default
agent -p "What does this codebase do?"
```

### Automated Code Review

```bash
#!/bin/bash
# simple-code-review.sh - Basic code review script

echo "Starting code review..."

agent -p --force --output-format text \
  "Review the recent code changes and provide feedback on:
   - Code quality and readability
   - Potential bugs or issues
   - Security considerations
   - Best practices compliance

   Provide specific suggestions for improvement and write to review.txt"

if [ $? -eq 0 ]; then
  echo "✓ Code review completed successfully"
else
  echo "✗ Code review failed"
  exit 1
fi
```

### Real-Time Progress Tracking with `stream-json`

```bash
#!/bin/bash
# stream-progress.sh - Track progress in real-time

echo "Starting stream processing..."

accumulated_text=""
tool_count=0
start_time=$(date +%s)

agent -p --force --output-format stream-json --stream-partial-output \
  "Analyze this project structure and create a summary report in analysis.txt" | \
while IFS= read -r line; do
  type=$(echo "$line" | jq -r '.type // empty')
  subtype=$(echo "$line" | jq -r '.subtype // empty')

  case "$type" in
    "system")
      if [ "$subtype" = "init" ]; then
        model=$(echo "$line" | jq -r '.model // "unknown"')
        echo "📡 Using model: $model"
      fi
      ;;
    "assistant")
      # Process streaming deltas
      has_ts=$(echo "$line" | jq 'has("timestamp_ms")')
      has_mc=$(echo "$line" | jq 'has("model_call_id")')
      if [ "$has_ts" = "true" ] && [ "$has_mc" = "false" ]; then
        content=$(echo "$line" | jq -r '.message.content[0].text // empty')
        accumulated_text="$accumulated_text$content"
        printf "\r📝 Generating: %d chars" ${#accumulated_text}
      fi
      ;;
    "tool_call")
      if [ "$subtype" = "started" ]; then
        tool_count=$((tool_count + 1))
        # Extract tool information
        if echo "$line" | jq -e '.tool_call.writeToolCall' > /dev/null 2>&1; then
          path=$(echo "$line" | jq -r '.tool_call.writeToolCall.args.path // ""')
          echo -e "\n🔧 Tool #$tool_count: Creating $path"
        elif echo "$line" | jq -e '.tool_call.readToolCall' > /dev/null 2>&1; then
          path=$(echo "$line" | jq -r '.tool_call.readToolCall.args.path // ""')
          echo -e "\n🔧 Tool #$tool_count: Reading $path"
        fi
      elif [ "$subtype" = "completed" ]; then
        # Extract and show tool results
        if echo "$line" | jq -e '.tool_call.writeToolCall.result.success' > /dev/null 2>&1; then
          lines=$(echo "$line" | jq -r '.tool_call.writeToolCall.result.success.lines // 0')
          size=$(echo "$line" | jq -r '.tool_call.writeToolCall.result.success.sizeBytes // 0')
          echo "   ✅ Created $lines lines ($size bytes)"
        elif echo "$line" | jq -e '.tool_call.readToolCall.result.success' > /dev/null 2>&1; then
          lines=$(echo "$line" | jq -r '.tool_call.readToolCall.result.success.lines // 0')
          echo "   📖 Read $lines lines"
        fi
      fi
      ;;
    "result")
      duration=$(echo "$line" | jq -r '.duration_ms // 0')
      end_time=$(date +%s)
      total_time=$((end_time - start_time))
      echo -e "\n\n✅ Completed in ${duration}ms (${total_time}s total)"
      echo "📊 Final stats: $tool_count tools, ${#accumulated_text} chars generated"
      ;;
  esac
done
```

---

## Working with Images

You can send images and other media files to the agent by including file paths in your prompts. The agent automatically reads the files through tool calling.

### Basic Image Analysis

```bash
# Analyze an image
agent -p "Analyze this image and describe what you see: ./screenshot.png"

# Process multiple media files
agent -p "Compare these two images and identify differences: ./before.png ./after.png"

# Combine file paths with text instructions
agent -p "Review the code in src/app.ts and the design mockup in designs/homepage.png"
```

### Batch Media Processing

```bash
#!/bin/bash
# process-media.sh - Process multiple media files

for image in images/*.png; do
  echo "Processing $image..."
  agent -p --output-format text \
    "Describe what's in this image: $image" > "${image%.png}.description.txt"
done
```

### Structured Image Analysis with JSON Output

```bash
#!/bin/bash
# analyze-image.sh - Analyze images using the headless CLI

IMAGE_PATH="./screenshots/ui-mockup.png"

agent -p --output-format json \
  "Analyze this image and provide a detailed description: $IMAGE_PATH" | \
  jq -r '.result'
```

---

## How It Works

When you include file paths in your prompt:

| Step | What happens |
|------|--------------|
| 1 | Agent receives your prompt with file path references |
| 2 | Agent uses tool calling to read the files automatically |
| 3 | Images are handled transparently |
| 4 | You can reference files using relative or absolute paths |

> *"File paths can be relative to the current working directory or absolute paths. The agent will read files through tool calls, so ensure the files exist and are accessible."*

---

## Use Cases for Headless CLI

| Use Case | Example |
|----------|---------|
| **CI/CD pipelines** | Automated code review on every PR |
| **Batch refactoring** | Update syntax across hundreds of files |
| **Code analysis** | Generate reports on code quality |
| **Documentation generation** | Auto-generate JSDoc comments |
| **Image analysis** | Process screenshots and design files |
| **Security scanning** | Scan for hardcoded secrets |
| **Migration scripts** | Convert codebases to new frameworks |

---

## Quick Reference Card

| Concept | Details |
|---------|---------|
| **Headless mode** | `-p` or `--print` |
| **Enable file changes** | `--force` (or `--quiet`) |
| **Default output** | `text` (final answer only) |
| **JSON output** | `--output-format json` |
| **Streaming JSON** | `--output-format stream-json` |
| **Partial output** | `--stream-partial-output` |
| **API key** | `export CURSOR_API_KEY=...` |

---

## Common Beginner Questions

### Q: What's the difference between `-p` and regular CLI?
**A:** `-p` (print mode) runs once and exits. Regular CLI is interactive.

### Q: Does `-p` mode modify files by default?
**A:** No – it only proposes changes. Use `--force` to actually modify files.

### Q: Can I use headless mode in CI/CD?
**A:** Yes – that's the primary use case. Set `CURSOR_API_KEY` and run `agent -p`.

### Q: Can I send images to the agent?
**A:** Yes – include file paths in your prompt. The agent reads them automatically.

### Q: How do I get structured output for parsing?
**A:** Use `--output-format json` for complete responses or `--output-format stream-json` for real-time progress.

### Q: Is headless mode safe for automated refactoring?
**A:** Use with caution. The `--force` flag gives the agent write access. Always test on a copy first.

---

## The Bottom Line

**Headless CLI lets you integrate Cursor's AI agent into scripts, CI/CD pipelines, and automation workflows.**

**Think of it as:**
- **Interactive CLI** = Human-driven terminal chat 💬
- **Headless CLI** = Robot-driven automation 🤖

**For DevOps and automation engineers:** This is a game-changer. You can:
1. Run automated code reviews on every PR
2. Batch-refactor thousands of files
3. Analyze images and generate descriptions
4. Integrate AI into your existing CI/CD pipelines

**Key flags to remember:**
- `-p` / `--print` – Run once, print output
- `--force` – Actually modify files (use with caution!)
- `--output-format json` – Parseable output
- `--output-format stream-json` – Real-time progress

**Pro tip:** Always set `CURSOR_API_KEY` as an environment variable in your CI/CD environment. Never hardcode API keys in scripts.

Would you like me to explain any specific headless CLI feature in more detail?
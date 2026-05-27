# Cursor Training Program

This repository contains a complete training course for the **Cursor AI code editor** and the **Cursor APIs**.

Use it to run a 2-day instructor-led workshop, prepare for a class, or study the Cursor product and APIs on your own. The repo is mostly Markdown, slides, lab guides, and diagrams. There is no application to build or server to run.

## Quick start

Choose the path that matches what you are trying to do:

| If you are... | Start here | Then open |
|---------------|------------|-----------|
| **Teaching the course** | [`FINAL_TABLE_OF_CONTENTS.md`](FINAL_TABLE_OF_CONTENTS.md) | [`slides/course-complete-marp-with-notes.html`](slides/course-complete-marp-with-notes.html) |
| **Taking the course in class** | The instructor's slide deck | The linked labs in [`slide-exercises/`](slide-exercises/) |
| **Studying Cursor product features** | [`learn/learn-readmes-index.md`](learn/learn-readmes-index.md) | [`core-exercises/exercise-1/`](core-exercises/exercise-1/) |
| **Studying Cursor APIs** | [`api-content-readmes/001-api-overview.md`](api-content-readmes/001-api-overview.md) | [`api-exercises/exercise-1/`](api-exercises/exercise-1/) |
| **Looking up acronyms or terms** | [`COURSE-CHEATSHEET.md`](COURSE-CHEATSHEET.md) | The module you are currently studying |

## What is included

- **A complete 2-day course:** 10 modules, 52 lessons, and about 11.5 hours of material.
- **Presentation deck:** one combined Marp deck with presenter notes and an exported HTML version.
- **In-class labs:** 40 slide-aligned exercises in [`slide-exercises/`](slide-exercises/).
- **Optional practice:** 25 Cursor product labs in [`core-exercises/`](core-exercises/) and 23 API labs in [`api-exercises/`](api-exercises/).
- **Reference material:** beginner-friendly summaries of Cursor Learn, product docs, and API docs.
- **Assessments:** pre-training and post-training checks in [`assessment/`](assessment/).

## Course outline

| Day | Modules | Focus |
|-----|---------|-------|
| **Day 1** | 1-5 | AI mental models, Cursor editor basics, agent modes and tools, team customization, Cursor CLI |
| **Day 2** | 6-10 | Cloud Agents UI, Cursor API foundations, Cloud Agents API and webhooks, Admin and Analytics APIs, AI code tracking |

For the full module-by-module breakdown, lesson timing, and exercise links, use [`FINAL_TABLE_OF_CONTENTS.md`](FINAL_TABLE_OF_CONTENTS.md).

## Repository map

```text
.
├── FINAL_TABLE_OF_CONTENTS.md      # Master course index and pacing guide
├── COURSE-CHEATSHEET.md            # Acronyms, definitions, and quick references
├── assessment/                     # Pre- and post-training assessments
├── slides/                         # Course deck, HTML export, notes, and diagrams
├── slide-exercises/                # 40 labs used during the slide course
├── learn/                          # 13 Cursor Learn summaries
├── docs-content-readmes/           # 82 Cursor product documentation summaries
├── api-content-readmes/            # Cursor API documentation summaries
├── core-exercises/                 # 25 optional Cursor product exercises
├── api-exercises/                  # 23 optional Cursor API exercises
└── scripts/                        # Utilities for maintaining the deck and assets
```

## How to run the instructor-led workshop

1. **Review the course plan**
   - Start with [`FINAL_TABLE_OF_CONTENTS.md`](FINAL_TABLE_OF_CONTENTS.md).
   - It lists every module, lesson, exercise, and estimated duration.

2. **Open the slide deck**
   - Present from [`slides/course-complete-marp-with-notes.html`](slides/course-complete-marp-with-notes.html).
   - Edit the source deck in [`slides/course-complete-marp-with-notes.md`](slides/course-complete-marp-with-notes.md).
   - Use [`slides/course-complete-speaker-notes.md`](slides/course-complete-speaker-notes.md) if you want a separate speaker script.

3. **Use the slide-aligned labs**
   - Hands-on blocks in the deck point to guides under [`slide-exercises/`](slide-exercises/).
   - Each guide is named by module and exercise number, for example:
     - [`slide-exercises/module-02/exercise-2.1-codebase-understanding.md`](slide-exercises/module-02/exercise-2.1-codebase-understanding.md)

4. **Give assessments**
   - Before Day 1: [`assessment/pre-assessment.md`](assessment/pre-assessment.md)
   - After Day 2: [`assessment/post-assessment.md`](assessment/post-assessment.md)

## How to use this repo for self-study

### Product track

Use this track to learn Cursor editor workflows, Agent modes, CLI usage, customization, and Cloud Agents.

1. Read the Learn summaries in [`learn/`](learn/).
2. Use the product documentation summaries in [`docs-content-readmes/`](docs-content-readmes/) when you need more detail.
3. Work through [`core-exercises/`](core-exercises/).
4. Use [`core-exercises/optional-core-exercises-guide.md`](core-exercises/optional-core-exercises-guide.md) to choose essential, recommended, or optional labs.

### API track

Use this track to learn Cursor APIs, webhooks, analytics, admin workflows, and AI code tracking.

1. Start with [`api-content-readmes/001-api-overview.md`](api-content-readmes/001-api-overview.md).
2. Continue through the API summaries in [`api-content-readmes/`](api-content-readmes/).
3. Work through [`api-exercises/`](api-exercises/).
4. Use [`api-exercises/optional-api-exercises-guide.md`](api-exercises/optional-api-exercises-guide.md) to choose essential, recommended, or optional labs.

## Prerequisites

Most product lessons only require:

- Cursor installed and signed in.
- A Git repository to practice in. A small sample repository is fine.

API lessons may also require:

- A Cursor API key.
- Enterprise access for Admin API, Analytics API, and AI Code Tracking labs.
- `ngrok` or a similar tunneling tool for webhook exercises.

## Editing or maintaining the deck

The course uses one combined Marp deck. There are no separate per-module source decks.

| File | Purpose |
|------|---------|
| [`slides/course-complete-marp-with-notes.md`](slides/course-complete-marp-with-notes.md) | Main editable slide source |
| [`slides/course-complete-marp-with-notes.html`](slides/course-complete-marp-with-notes.html) | Browser-ready version for presenting |
| [`slides/course-complete-speaker-notes.md`](slides/course-complete-speaker-notes.md) | Standalone speaker notes |
| [`slides/assets/`](slides/assets/) | Diagrams and other slide assets |
| [`scripts/themes/flat-gaia.css`](scripts/themes/flat-gaia.css) | Marp theme |

After editing the Markdown deck, regenerate the HTML with Marp CLI:

```bash
npx @marp-team/marp-cli slides/course-complete-marp-with-notes.md \
  --html --allow-local-files \
  --theme-set scripts/themes/flat-gaia.css \
  -o slides/course-complete-marp-with-notes.html
```

Useful maintenance scripts live in [`scripts/`](scripts/):

| Script | Use |
|--------|-----|
| [`scripts/generate-speaker-notes.py`](scripts/generate-speaker-notes.py) | Regenerate speaker notes or embedded notes |
| [`scripts/regenerate-marp-diagram-svgs.py`](scripts/regenerate-marp-diagram-svgs.py) | Regenerate diagram SVG assets |
| [`scripts/fix-corrupted-diagram-svgs.py`](scripts/fix-corrupted-diagram-svgs.py) | Repair known-bad diagram SVG files |
| [`scripts/inject-lab-guide-links.py`](scripts/inject-lab-guide-links.py) | Add lab guide links to exercise slides |
| [`scripts/sync-exercise-steps-to-slides.py`](scripts/sync-exercise-steps-to-slides.py) | Sync key lab steps into slides |
| [`scripts/export-editable-pptx.ps1`](scripts/export-editable-pptx.ps1) | Optional PowerPoint export |

## Helpful indexes

| Need | File |
|------|------|
| Full course structure | [`FINAL_TABLE_OF_CONTENTS.md`](FINAL_TABLE_OF_CONTENTS.md) |
| Acronyms and definitions | [`COURSE-CHEATSHEET.md`](COURSE-CHEATSHEET.md) |
| Cursor Learn summaries | [`learn/learn-readmes-index.md`](learn/learn-readmes-index.md) |
| Cursor product docs summaries | [`docs-content-readmes/docs-content-readmes-index.md`](docs-content-readmes/docs-content-readmes-index.md) |
| Cursor API docs summaries | [`api-content-readmes/api-content-readmes-index.md`](api-content-readmes/api-content-readmes-index.md) |
| Product exercise guide | [`core-exercises/optional-core-exercises-guide.md`](core-exercises/optional-core-exercises-guide.md) |
| API exercise guide | [`api-exercises/optional-api-exercises-guide.md`](api-exercises/optional-api-exercises-guide.md) |

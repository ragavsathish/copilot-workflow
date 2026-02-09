# copilot-workflow

Automated document generation workflows for regulated (GxP) environments, powered by GitHub Copilot.

## What This Does

Copilot reads input DOCX documents, generates regulated output documents following a PDCA (Plan-Do-Check-Act) lifecycle, and produces styled DOCX files — all triggered by a single command.

## Quick Start

1. Install prerequisites (see below)
2. Drop your input `.docx` files into `workflows/task-<N>-<name>/input/`
3. Tell Copilot: **"Run workflow N"** (e.g., "Run workflow 1")
4. Approve the plan when prompted
5. Pick up the output `.docx` files from `workflows/task-<N>-<name>/output/`

## How It Works

```
input/*.docx → extract → Copilot generates content → build → output/*.docx
```

Every workflow follows a **PDCA cycle**: Copilot creates a plan (PLAN), waits for your approval, generates content (DO), presents output for review (CHECK), and revises based on feedback (ACT) until you approve.

| Step | What Happens | Who Does It |
|---|---|---|
| 0 | Extract DOCX → markdown + images | `extract_docx.py` (run by Copilot) |
| 1 | Create generation plan, wait for approval | Copilot |
| 2 | Generate output markdown following approved plan | Copilot |
| 3 | Build markdown → styled DOCX using template | `build_docx.py` (run by Copilot) |
| 4 | Present output for review, revise if needed | Copilot + User |

## Prerequisites

- **Python 3.8+**
- **Pandoc** — required for DOCX building. Install via [pandoc.org/installing](https://pandoc.org/installing.html) or your system package manager.
- **Python dependencies:**
  ```bash
  pip install -r requirements.txt
  ```
- **VS Code** with GitHub Copilot extension (Chat agent mode enabled)
- **DOCX templates** in `templates/document template/` for corporate styling

## Project Structure

```
.github/
  copilot-instructions.md              Global workflow rules & coding guidelines
  instructions/                        Per-workflow Copilot instructions (applyTo patterns)
  prompts/                             Reusable prompt templates
scripts/
  extract_docx.py                      DOCX → markdown + images
  build_docx.py                        Markdown + images → styled DOCX (via Pandoc)
  image_b64.py                         Image → base64 + metadata
  simulate/                            Test data generators for development
templates/
  document template/                   DOCX templates with company styling (fonts, logo, headers/footers)
workflows/
  task-1-tdd-icv/                      Workflow 1: Technical Design + ICV
  task-2-test-cases/                   Workflow 2: Test Case Generation
  task-3-review-test-cases/            Workflow 3: Test Case Gap Analysis & Review
  task-4-retrospect/                   Workflow 4: Retrospective & Continuous Improvement
```

Each workflow directory contains `input/` (drop DOCX here), `extracted/` (auto-generated), and `output/` (final results).

## Available Workflows

| Workflow | Input | Output | Command |
|---|---|---|---|
| **Task 1** — TDD + ICV | Application Design, Workspace Design, GxP Assessment, ICV Steps + Screenshots | Technical Design Document, ICV Document | "Run workflow 1" |
| **Task 2** — Test Cases | Requirement Specification | Test Cases Document (with traceability matrix) | "Run workflow 2" |
| **Task 3** — Review Test Cases | Requirements Specification + Test Cases Document | Review report + Revised test cases (versioned) | "Review workflow 3" |
| **Task 4** — Retrospective | Completed workflow execution | Retrospective report + Updated instruction files | "Retrospect workflow N" |

## Adding a New Workflow

1. Create `workflows/task-<N>-<name>/` with `input/`, `extracted/`, `output/` subdirectories (add `.gitkeep` files)
2. Create `.github/instructions/workflow-<N>-<name>.instructions.md` with `applyTo` frontmatter targeting `workflows/task-<N>-<name>/**/*`
3. Define inputs, outputs, mapping rules, and any special requirements in the instruction file
4. Follow the PDCA lifecycle documented in `.github/copilot-instructions.md`

## License

MIT

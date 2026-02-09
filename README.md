# copilot-workflow

Automated document generation workflows powered by GitHub Copilot.

## What This Does

Copilot reads input DOCX documents, generates regulated output documents, and produces styled DOCX files — all triggered by a single command.

## Quick Start

1. Drop your input `.docx` files into `workflows/task-<N>-<name>/input/`
2. Tell Copilot: **"Run workflow 1"**
3. Pick up the output `.docx` files from `workflows/task-<N>-<name>/output/`

## How It Works

```
input/*.docx → extract → Copilot generates content → build → output/*.docx
```

| Step | What Happens | Who Does It |
|---|---|---|
| 1 | Extract DOCX → markdown + images | `extract_docx.py` (run by Copilot) |
| 2 | Read inputs, follow template, generate output markdown | Copilot |
| 3 | Build markdown → styled DOCX using template | `build_docx.py` (run by Copilot) |

## Project Structure

```
.github/
  copilot-instructions.md              Global workflow rules
  instructions/                        Per-workflow mapping rules
  agents/                              Copilot agent definitions
  prompts/                             Reusable prompt templates
  workflows/                           CI/CD validation and testing
  PULL_REQUEST_TEMPLATE.md             PR checklist
  ISSUE_TEMPLATE/                      Bug report and workflow request forms
scripts/
  extract_docx.py                      DOCX → markdown + images
  build_docx.py                        Markdown + images → styled DOCX
  create_test_data.py                  Generate sample test data
templates/
  document template/                   DOCX templates with company styling
workflows/
  task-1-tdd-icv/                      Workflow 1: Technical Design + ICV
    input/                             Drop input DOCX here
    extracted/                         Auto-generated (text + images)
    output/                            Final output (md + DOCX)
```

## Available Workflows

| Workflow | Input | Output |
|---|---|---|
| **Task 1** — TDD + ICV | Application Design, Workspace Design, GxP Assessment, ICV Steps + Screenshots | Technical Design Document, ICV Document |

## Requirements

- Python 3.8+
- `pip install -r requirements.txt`

## Copilot Resources

| Type | Location | Purpose |
|---|---|---|
| **Agent** | `.github/agents/gxp-document-workflow.agent.md` | PDCA workflow orchestrator persona |
| **Prompts** | `.github/prompts/generate-plan.prompt.md` | Plan generation template |
| | `.github/prompts/review-output.prompt.md` | Output review checklist |
| **Instructions** | `.github/copilot-instructions.md` | Global PDCA rules |
| | `.github/instructions/workflow-1-*.instructions.md` | Workflow-specific mapping |
| | `.github/instructions/python-scripts.instructions.md` | Python coding standards |

## Adding a New Workflow

1. Create `workflows/task-<N>-<name>/` with `input/`, `extracted/`, `output/` subdirectories
2. Create `.github/instructions/workflow-<N>-<name>.instructions.md` with `applyTo` and `description` frontmatter
3. Define inputs, outputs, and mapping rules in the instruction file

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on adding workflows, modifying scripts, and submitting changes.

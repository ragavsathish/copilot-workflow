# Copilot Workflow Instructions

This repository automates document generation workflows. Copilot orchestrates the full pipeline: extract input DOCX → **plan** → user approval → generate content → build output DOCX.

## Project Overview

- **Purpose**: Automate creation of regulated (GxP) documents from input design documents
- **Language**: Python (scripts), Markdown (intermediate format)
- **Dependencies**: `python-docx`, `Pillow`, `pypandoc` (see `requirements.txt`)

## Project Layout

```
.github/
  copilot-instructions.md          ← You are here (global rules)
  instructions/                    ← Per-workflow instructions
scripts/
  extract_docx.py                  ← DOCX → markdown + images (uses python-docx)
  build_docx.py                    ← Markdown → styled DOCX (uses pypandoc + reference-doc)
templates/
  document template/               ← Word templates for styling (fonts, logo, headers/footers)
workflows/
  task-<N>-<name>/
    input/                         ← User drops input DOCX files here
    extracted/                     ← Auto-generated markdown + images
    extracted/templates/           ← Auto-generated template structure
    plan.md                        ← Generation plan (created by Copilot, approved by user)
    output/                        ← Copilot writes markdown here, script converts to DOCX
```

## Running a Workflow

When a user says **"Run workflow N"** or refers to a workflow task, execute these steps in order:

### Step 1: Install dependencies (if needed)
```bash
pip install -r requirements.txt
```
Pandoc binary is also required. Install if missing:
```bash
pypandoc.download_pandoc()
```

### Step 2: Extract input DOCX files
```bash
python scripts/extract_docx.py workflows/task-<N>-<name>
```
This converts input DOCX files to markdown + images, and extracts template structure.

### Step 3: Create a plan — STOP and wait for approval

After extraction, read all extracted content and create a plan file at `workflows/task-<N>-<name>/plan.md`.

The plan must include:

```markdown
# Workflow N Plan

## Input Documents Found
- [x] document_name.md (X lines, Y images)
- [x] another_document.md (X lines)
- [ ] missing_document.md — NOT FOUND

## Template Structure
List the sections from the template, exactly as extracted.

## Generation Plan

### Output 1: <document_name>
For each section in the template:
| Section | Source | Summary of what will be written |
|---|---|---|
| 1. Purpose | app_design.md §1 | Brief description of content |
| 2. Scope | gxp_assessment.md §2 + app_design.md §1.1 | Brief description |
| ... | ... | ... |

### Output 2: <document_name>
Same table format.

## Images
- X screenshots found, will be placed in: [list which sections]

## Gaps
- List anything missing or unclear from the inputs
- List sections that will have [To be completed] placeholders
```

**After writing the plan, show it to the user and ask: "Does this plan look right? Should I proceed?"**

**DO NOT generate any output documents until the user approves.**

### Step 4: Generate output (only after approval)

Once the user approves (says "yes", "go ahead", "approved", "proceed", etc.):
- Read the approved `plan.md` as the guide
- Generate output markdown files in `workflows/task-<N>-<name>/output/`
- **Every output markdown file must start with a YAML frontmatter block** (see below)
- Follow the plan exactly — do not deviate from what was approved
- Reference images using: `![description](images/filename.png)`

### Step 5: Build output DOCX files
```bash
python scripts/build_docx.py workflows/task-<N>-<name>
```
Pypandoc converts markdown → styled DOCX using `--reference-doc` from the Word template.

### Step 6: Confirm completion
Report to the user what was generated and where the output files are located.

## Resuming Across Conversations

If a workflow was started in a previous conversation:
- Check if `workflows/task-<N>-<name>/plan.md` exists
- If plan exists but no output files → show the plan and ask for approval
- If plan exists and output `.md` files exist but no `.docx` → run build step
- If everything exists → report completion
- Always read `plan.md` before generating — it is the source of truth for what to produce

## YAML Frontmatter

Every output markdown file **must** begin with a YAML header. Pandoc uses these variables to populate the Word template fields (title page, headers, footers, etc.):

```yaml
---
title: "Document Title"
subtitle: "Optional Subtitle"
author: "Author / Team Name"
date: "2026-02-09"
version: "1.0"
status: "Draft"
document_id: "DOC-001"
---
```

Populate these values from the input documents where available. Use `[TBD]` for values not found in the inputs.

## Document Generation Rules

### GxP Traceability
- Every output section must note which input document it draws from
- Use a traceability comment at the start of each section: `<!-- Source: input_document_name.md, Section X -->`
- Maintain accurate cross-references between documents

### Content Rules
- Follow the template structure exactly — do not add or remove sections
- Follow the approved plan exactly — do not deviate
- Keep language formal and precise (regulated document style)
- Preserve all technical details from input documents accurately
- Do not fabricate information — only use content from the input documents
- If input is missing for a section, write: `[To be completed — input not provided]`

### Screenshot and Image Handling
- Reference images extracted from input documents: `![Step description](images/filename.png)`
- Place screenshots inline with their corresponding steps
- Include a caption/description for every image
- Pillow is available if images need resizing before embedding

### Table Handling
- Preserve all tables from input documents
- Use standard markdown table format
- Ensure column alignment matches the source

## Adding a New Workflow

To add a new workflow (e.g., Task 2):

1. Create the directory: `workflows/task-2-<name>/input/`, `extracted/`, `output/`
2. Create a workflow instruction file: `.github/instructions/workflow-2-<name>.instructions.md`
3. In the instruction file, define: inputs, outputs, mapping rules, and any special requirements
4. Use `applyTo: "workflows/task-2-<name>/**/*"` in the frontmatter

## General Rules

- Python scripts and pip libraries are allowed for automation
- All document input/output is in DOCX format
- Process one set of documents at a time (no batch processing)
- Keep solutions simple and straightforward
- Always plan before generating — never skip the approval step

# Copilot Workflow Instructions

This repository automates document generation workflows. Copilot orchestrates the full pipeline: extract input DOCX → generate content → build output DOCX.

## Project Overview

- **Purpose**: Automate creation of regulated (GxP) documents from input design documents
- **Language**: Python (scripts), Markdown (intermediate format)
- **Dependencies**: `python-docx`, `Pillow` (see `requirements.txt`)

## Project Layout

```
.github/
  copilot-instructions.md          ← You are here (global rules)
  instructions/                    ← Per-workflow instructions
scripts/
  extract_docx.py                  ← DOCX → markdown + images
  build_docx.py                    ← Markdown + images → styled DOCX
templates/
  document template/               ← DOCX templates with company styling
workflows/
  task-<N>-<name>/
    input/                         ← User drops input DOCX files here
    extracted/                     ← Auto-generated markdown + images
    extracted/templates/           ← Auto-generated template structure
    output/                        ← Copilot writes markdown here, script converts to DOCX
```

## Running a Workflow

When a user says **"Run workflow N"** or refers to a workflow task, execute these steps in order:

### Step 1: Install dependencies (if needed)
```bash
pip install -r requirements.txt
```

### Step 2: Extract input DOCX files
```bash
python scripts/extract_docx.py workflows/task-<N>-<name>
```
This converts input DOCX files to markdown + images, and extracts template structure.

### Step 3: Read extracted content and generate output
- Read all files in `workflows/task-<N>-<name>/extracted/` to understand input content
- Read template structure from `workflows/task-<N>-<name>/extracted/templates/` to know the required output sections
- Read the workflow-specific instructions from `.github/instructions/` for mapping rules
- Generate output markdown files in `workflows/task-<N>-<name>/output/`
- Follow the template section structure exactly
- Reference images using: `![description](images/filename.png)`

### Step 4: Build output DOCX files
```bash
python scripts/build_docx.py workflows/task-<N>-<name>
```
This converts output markdown files to styled DOCX using the templates.

### Step 5: Confirm completion
Report to the user what was generated and where the output files are located.

## Document Generation Rules

### GxP Traceability
- Every output section must note which input document it draws from
- Use a traceability comment at the start of each section: `<!-- Source: input_document_name.md, Section X -->`
- Maintain accurate cross-references between documents

### Content Rules
- Follow the template structure exactly — do not add or remove sections
- Keep language formal and precise (regulated document style)
- Preserve all technical details from input documents accurately
- Do not fabricate information — only use content from the input documents
- If input is missing for a section, write: `[To be completed — input not provided]`

### Screenshot and Image Handling
- Reference images extracted from input documents: `![Step description](images/filename.png)`
- Place screenshots inline with their corresponding steps
- Include a caption/description for every image

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

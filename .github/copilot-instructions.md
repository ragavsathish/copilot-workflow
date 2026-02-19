# Copilot Workflow Instructions

## About This Project

Automated document generation system for **regulated (GxP) environments**. Transforms input DOCX documents into compliant output documents through a structured PDCA (Plan-Do-Check-Act) lifecycle. Copilot orchestrates the full pipeline: extract content from DOCX, generate markdown, build styled DOCX.

**Audience:** QA teams, regulatory affairs, and engineers producing GxP-compliant documentation.

## Technology Stack

| Layer | Technology | Purpose |
|---|---|---|
| Language | Python 3.8+ | Scripts for extraction, building, image processing |
| Document parsing | `python-docx` >= 1.1.0 | Read/write DOCX, extract text/tables/images |
| Image processing | `Pillow` >= 10.0.0 | Validate and process extracted images |
| Document building | `pypandoc` >= 1.13 | Convert markdown to styled DOCX via Pandoc |
| System dependency | Pandoc | Required by pypandoc (`pypandoc.download_pandoc()` to install) |

```bash
pip install -r requirements.txt
```

## Project Layout

```
.github/
  copilot-instructions.md        ← Global rules (this file — keep concise)
  instructions/                  ← Per-workflow instructions (detailed rules)
  prompts/                       ← Reusable prompt files (/run-workflow-1, etc.)
  agents/                        ← Custom agents (doc-generator, reviewer)
scripts/
  extract_docx.py                ← DOCX → markdown + images
  build_docx.py                  ← Markdown → styled DOCX (pypandoc + reference-doc)
  image_b64.py                   ← Image → base64 + metadata
  validate_output.py             ← Validate generated markdown (frontmatter, traceability)
  simulate/                      ← Test data generators
templates/
  document template/             ← Word templates for styling (fonts, logo, headers/footers)
workflows/
  task-<N>-<name>/
    input/                       ← User drops input DOCX files here
    extracted/                   ← Auto-generated markdown + images
    plan-YYYY-MM-DD.md           ← PLAN: generation plan (approved by user)
    output/                      ← Generated markdown + DOCX output
```

## Coding Guidelines

- Follow PEP 8. Use type hints. Use `pathlib.Path` for file paths.
- Never use bare `except:`. Print errors to stderr. Exit 1 (user error) or 2 (unexpected).
- Keep dependencies minimal (KISS). Update `requirements.txt` for new packages.
- Every script: module docstring with usage + `main()` + `if __name__ == "__main__"` guard.
- Markdown output: always start with YAML frontmatter. Use `<!-- Source: ... -->` traceability comments.
- File naming: `snake_case` for Python and markdown. ISO dates (`YYYY-MM-DD`) in plan filenames.
- Never fabricate content. Use `[To be completed]` for missing data.

## PDCA Lifecycle (Every Workflow)

```
EXTRACT → PLAN → DO → CHECK → ACT
            ↓              ↓
         (STOP:          (STOP:
       wait for         wait for
       approval)        review)
```

1. **EXTRACT**: Run `python scripts/extract_docx.py workflows/task-<N>-<name>` to convert input DOCX to markdown + images.
2. **PLAN**: Create `plan-YYYY-MM-DD.md` with inputs found, section mapping, gaps. **STOP and ask user for approval.**
3. **DO** (after approval): Generate output markdown in `output/`. Build DOCX: `python scripts/build_docx.py workflows/task-<N>-<name>`. Run validation: `python scripts/validate_output.py workflows/task-<N>-<name>/output/`.
4. **CHECK**: Report output files, section counts, validation results, gaps. **Ask user to review.**
5. **ACT**: Revise flagged sections and rebuild, or mark complete if approved.

**Never skip PLAN or CHECK. Never generate output before approval.**

## Resuming Across Conversations

Read the most recent `plan-YYYY-MM-DD.md` (or `review-*.md` for workflow-3) to determine phase:

| Status | Action |
|---|---|
| No plan file | Start from EXTRACT |
| `Phase: PLAN`, `Approved: pending` | Show plan, ask for approval |
| `Phase: PLAN`, `Approved: yes`, no output | Start DO phase |
| `Phase: CHECK` | Show output summary, ask for review |
| `Phase: COMPLETE` | Report workflow is done |

## YAML Frontmatter (Required)

Every output markdown file must begin with:

```yaml
---
title: "Document Title"
author: "Author / Team Name"
date: "YYYY-MM-DD"
version: "1.0"
status: "Draft"
document_id: "DOC-001"
---
```

## Document Generation Rules

- **Traceability**: Start each section with `<!-- Source: input_file.md, Section X -->`.
- **Template adherence**: Follow template structure exactly. Do not add or remove sections.
- **No fabrication**: Only use content from input documents. Use `[To be completed]` for gaps.
- **Images**: Reference as `![description](images/filename.png)` with figure number and caption.
- **Tables**: Preserve all tables from inputs in standard markdown format.
- **Language**: Formal, precise, regulated document style.

## Available Scripts

| Script | Usage |
|---|---|
| `extract_docx.py` | `python scripts/extract_docx.py workflows/task-<N>-<name>` |
| `build_docx.py` | `python scripts/build_docx.py workflows/task-<N>-<name>` |
| `image_b64.py` | `python scripts/image_b64.py <image_path> --out <dir> --raw` |
| `validate_output.py` | `python scripts/validate_output.py workflows/task-<N>-<name>/output/` |

## Error Handling

| Problem | Solution |
|---|---|
| `extract_docx.py` fails | Verify DOCX files exist in `input/` |
| `build_docx.py` "No .md files" | Generate markdown output first |
| Pandoc not found | `pypandoc.download_pandoc()` or install via system package manager |
| DOCX missing styles | Place template `.docx` in `templates/document template/` |

## General Rules

- Process one document set at a time (no batch processing)
- Keep solutions simple (KISS principle)
- Always follow PDCA — never skip PLAN or CHECK
- Validate outputs before presenting to user
- Run `python scripts/validate_output.py` after every DO phase

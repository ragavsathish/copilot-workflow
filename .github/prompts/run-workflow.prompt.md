---
description: "Run a PDCA document generation workflow end-to-end"
---

# Run Workflow

Execute the PDCA lifecycle for a specified workflow task.

## Steps

1. **EXTRACT**: Install dependencies if needed (`pip install -r requirements.txt`), then run `python scripts/extract_docx.py workflows/task-${{N}}-${{NAME}}` to convert input DOCX files to markdown and images.

2. **PLAN**: Read all extracted content from `workflows/task-${{N}}-${{NAME}}/extracted/` and create a dated plan file at `workflows/task-${{N}}-${{NAME}}/plan-YYYY-MM-DD.md`. Present the plan and wait for approval.

3. **DO** (after approval): Generate output markdown in `workflows/task-${{N}}-${{NAME}}/output/`, then build DOCX with `python scripts/build_docx.py workflows/task-${{N}}-${{NAME}}`.

4. **CHECK**: Report output files, section counts, and any gaps. Ask for review.

5. **ACT**: Revise based on feedback and rebuild, or mark complete if approved.

Refer to `.github/copilot-instructions.md` for full PDCA details and `.github/instructions/workflow-${{N}}-*.instructions.md` for workflow-specific rules.

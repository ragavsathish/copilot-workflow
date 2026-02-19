---
description: "Run a PDCA document generation workflow end-to-end"
---

# Run Workflow

Execute the PDCA lifecycle for a specified workflow task.

## Quick Start

Tell me which workflow to run:

- **Workflow 1** — Technical Design Document + ICV Document (use `/run-workflow-1`)
- **Workflow 2** — Test Cases from Requirement Specification (use `/run-workflow-2`)
- **Workflow 3** — Critical Review: Test Case Gap Analysis (use `/run-workflow-3`)
- **Workflow 4** — Retrospective & Continuous Improvement (use `/run-workflow-4`)

Or say "Run workflow N" and I'll follow the PDCA lifecycle:

1. **EXTRACT**: `python scripts/extract_docx.py workflows/task-${{N}}-${{NAME}}`
2. **PLAN**: Create dated plan file. **STOP for approval.**
3. **DO**: Generate output. Build DOCX. Validate with `python scripts/validate_output.py`.
4. **CHECK**: Report results. **STOP for review.**
5. **ACT**: Revise or complete.

## Resuming?

If this workflow was already started, use `/resume-workflow` to pick up where you left off.

Refer to `.github/copilot-instructions.md` for full PDCA details and `.github/instructions/workflow-${{N}}-*.instructions.md` for workflow-specific rules.

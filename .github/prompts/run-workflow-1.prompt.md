---
description: "Run Workflow 1: Generate Technical Design Document + ICV Document"
---

# Run Workflow 1: TDD + ICV

Execute the PDCA lifecycle for **Workflow 1 — Technical Design Document + ICV Document**.

## What to do

1. **EXTRACT**: Install deps if needed (`pip install -r requirements.txt`), then run:
   ```bash
   python scripts/extract_docx.py workflows/task-1-tdd-icv
   ```

2. **PLAN**: Read all extracted content from `workflows/task-1-tdd-icv/extracted/`. Create `workflows/task-1-tdd-icv/plan-YYYY-MM-DD.md` with:
   - Input documents found (checklist with line/image counts)
   - Template structure from `extracted/templates/`
   - Section-by-section mapping table (output section → input source → summary)
   - Screenshot placement plan
   - Gaps or missing inputs

   **STOP and ask: "Does this plan look right? Should I proceed?"**

3. **DO** (after approval): Generate `output/technical_design.md` and `output/icv_document.md` following the approved plan. Build DOCX:
   ```bash
   python scripts/build_docx.py workflows/task-1-tdd-icv
   ```
   Validate output:
   ```bash
   python scripts/validate_output.py workflows/task-1-tdd-icv/output/
   ```

4. **CHECK**: Report output files, section counts, image counts, validation results. Ask for review.

5. **ACT**: Revise flagged sections or mark complete.

Refer to `.github/instructions/workflow-1-tdd-icv.instructions.md` for detailed mapping rules.

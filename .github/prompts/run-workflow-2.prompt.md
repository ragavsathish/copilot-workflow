---
description: "Run Workflow 2: Generate Test Cases from Requirement Specification"
---

# Run Workflow 2: Test Cases

Execute the PDCA lifecycle for **Workflow 2 — Test Case Generation**.

## What to do

1. **EXTRACT**: Install deps if needed (`pip install -r requirements.txt`), then run:
   ```bash
   python scripts/extract_docx.py workflows/task-2-test-cases
   ```

2. **PLAN**: Read extracted requirements from `workflows/task-2-test-cases/extracted/`. Create `workflows/task-2-test-cases/plan-YYYY-MM-DD.md` with:
   - Requirements found (IDs, titles, priorities)
   - Planned test cases per requirement (positive/negative/boundary)
   - Total test case estimate
   - Gaps: ambiguous or untestable requirements

   **STOP and ask: "Does this plan look right? Should I proceed?"**

3. **DO** (after approval): Generate `output/test_cases.md` following KISS rules:
   - One requirement → one or more test cases
   - One step = one action
   - Observable expected results
   - TC-001, TC-002, ... format
   Build DOCX:
   ```bash
   python scripts/build_docx.py workflows/task-2-test-cases
   ```
   Validate:
   ```bash
   python scripts/validate_output.py workflows/task-2-test-cases/output/
   ```

4. **CHECK**: Report test case count, coverage, validation results. Ask for review.

5. **ACT**: Revise or mark complete.

Refer to `.github/instructions/workflow-2-test-cases.instructions.md` for KISS rules and test case format.

---
description: "Run Workflow 3: Critical Review — Test Case Gap Analysis & Revision"
---

# Run Workflow 3: Review Test Cases

Execute the extended PDCA lifecycle for **Workflow 3 — Test Case Gap Analysis**.

## What to do

1. **EXTRACT**: Install deps if needed (`pip install -r requirements.txt`), then run:
   ```bash
   python scripts/extract_docx.py workflows/task-3-review-test-cases
   ```

2. **PLAN**: Create `workflows/task-3-review-test-cases/review-YYYY-MM-DD.md` with review scope (coverage, quality, edge cases, traceability). **STOP and ask for approval.**

3. **GAP_ANALYSIS** (after approval): Populate the review document with:
   - Requirements with no test cases (CRITICAL)
   - Requirements with inadequate coverage (MAJOR)
   - Test case quality issues (ambiguous results, KISS violations)
   - Scenario gaps (what-if analysis)
   - Traceability matrix validation
   - Priority & risk assessment

   **STOP and present findings. Ask user to mark decisions.**

4. **BRAINSTORM**: Discuss findings with user. Once approved, add Revision Plan to review document.

5. **REVISE**: Apply approved changes, rebuild DOCX:
   ```bash
   python scripts/build_docx.py workflows/task-3-review-test-cases
   ```
   Validate:
   ```bash
   python scripts/validate_output.py workflows/task-3-review-test-cases/output/
   ```

6. Report completion with change summary.

Refer to `.github/instructions/workflow-3-review-test-cases.instructions.md` for detailed gap analysis format.

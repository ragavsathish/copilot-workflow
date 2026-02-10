---
description: "Run Workflow 4: Retrospective & Continuous Improvement"
---

# Run Workflow 4: Retrospective

Execute a **3-question retrospective** for a completed workflow.

## What to do

1. **TRIGGER**: Identify the target workflow from the user's request (e.g., "retrospect workflow 1").

2. **ANALYZE**: Scan `workflows/task-N-<name>/` for:
   - Plan file status (phase reached, approval)
   - Output files generated vs. expected
   - Completion percentage

3. **INTERVIEW** (3 questions, ~3 min):
   - **Q1**: "Did the workflow complete successfully? If not, where did it stop?" (Complete / Partial / Failed)
   - **Q2**: "What's the ONE most important thing you learned — good or bad?"
   - **Q3**: "What ONE change would most improve this workflow?"

4. **SYNTHESIZE**: Categorize learnings (Patterns Validated, Issues, Process Improvements, Documentation Gaps, Quality/Tool Enhancements). Assign priorities (P0/P1/P2).

5. **APPLY** (with approval): Update workflow instruction file with learnings. Create backup first.

Output: `workflows/task-4-retrospect/retrospectives/workflow-N-retro-YYYY-MM-DD.md`

Refer to `.github/instructions/workflow-4-retrospect.instructions.md` for full retrospective format.

---
description: "Resume a workflow that was started in a previous conversation"
---

# Resume Workflow

Pick up where a previous conversation left off for a specified workflow task.

## What to do

1. **Find the state file**: Look for the most recent `plan-*.md` (or `review-*.md` for workflow-3) in `workflows/task-${{N}}-${{NAME}}/`.

2. **Read the status** and determine the current phase:

   | Status Found | Action |
   |---|---|
   | No plan/review file | Start fresh — run EXTRACT |
   | `Phase: PLAN`, `Approved: pending` | Show the existing plan and ask for approval |
   | `Phase: PLAN`, `Approved: yes`, no output files | Start DO phase using the approved plan |
   | `Phase: CHECK` | Show output summary, ask for review |
   | `Phase: BRAINSTORM` (workflow-3) | Continue discussion, wait for approval |
   | `Phase: REVISE` (workflow-3) | Apply approved changes |
   | `Phase: COMPLETE` | Report workflow is already done |

3. **Continue** from the identified phase following the PDCA lifecycle.

Refer to `.github/copilot-instructions.md` for PDCA rules and the relevant workflow instruction file for details.

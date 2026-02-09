---
agent: "agent"
description: "Generate a PDCA plan for a document workflow by analyzing extracted inputs and mapping them to the template structure."
tools:
  - "codebase"
---

# Generate Workflow Plan

Analyze the extracted content in the specified workflow directory and create a comprehensive plan.

## Instructions

1. Read all files in `workflows/task-{N}-{name}/extracted/` to understand available inputs
2. Read the template structure in `workflows/task-{N}-{name}/extracted/templates/`
3. Read the workflow-specific instructions in `.github/instructions/workflow-{N}-*.instructions.md`
4. Create `workflows/task-{N}-{name}/plan.md` with:
   - List of input documents found (with line counts and image counts)
   - Template sections mapped to input sources
   - Screenshot placement plan
   - Identified gaps where input is missing
   - Revision history table

## Output Format

The plan must follow the structure defined in `.github/copilot-instructions.md` under the PLAN section. Include a generation plan table for each output document.

After writing the plan, present it and ask: "Does this plan look right? Should I proceed?"

**Do not generate output documents until the user approves.**

---
agent: "agent"
description: "Review generated output documents against the approved plan, checking for completeness, traceability, and compliance."
tools:
  - "codebase"
---

# Review Output Documents

Perform a CHECK phase review of generated output documents.

## Instructions

1. Read the approved `plan.md` to understand what was planned
2. Read each generated markdown file in `workflows/task-{N}-{name}/output/`
3. Verify the following:
   - All planned sections are present
   - YAML frontmatter is complete (title, author, date, version, status, document_id)
   - Traceability comments (`<!-- Source: ... -->`) exist in every section
   - Screenshots are referenced with figure numbers and captions
   - No fabricated content — only information from input documents
   - `[To be completed]` placeholders used where inputs were missing
   - Tables preserved accurately from source documents

## Report

Present a summary:
- Sections completed vs. placeholders
- Images embedded
- Gaps found
- Any deviations from the plan

Ask: "Please review the output. Any sections to revise, or is this good?"

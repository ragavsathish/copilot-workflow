---
description: "Validate generated output files for errors before presenting to user"
---

# Validate Output

Run validation checks on generated output files to catch errors **before** the CHECK phase.

## What to do

1. **Run the validation script**:
   ```bash
   python scripts/validate_output.py workflows/task-${{N}}-${{NAME}}/output/
   ```

2. **Review results** and fix any issues:
   - Missing YAML frontmatter fields
   - Missing traceability comments (`<!-- Source: ... -->`)
   - Empty sections or `[To be completed]` placeholders
   - Broken image references
   - Malformed markdown tables
   - Test case format violations (workflow-2 only)

3. **If issues found**: Fix the markdown files and rebuild DOCX:
   ```bash
   python scripts/build_docx.py workflows/task-${{N}}-${{NAME}}
   ```

4. **Report** validation results to the user as part of the CHECK phase.

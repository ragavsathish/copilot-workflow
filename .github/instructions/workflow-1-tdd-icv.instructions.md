---
applyTo: "workflows/task-1-tdd-icv/**/*"
---

# Workflow 1: Technical Design Document + ICV Document

## Purpose

Generate two regulated output documents from four input design documents.

## Input Documents

Place these DOCX files in `workflows/task-1-tdd-icv/input/`:

| Input File | Description |
|---|---|
| Application Design Document | Application architecture, components, interfaces, data flows |
| Workspace Design Document | Environment setup, infrastructure, workspace configuration |
| GxP Assessment Document | Regulatory requirements, risk assessment, compliance scope |
| ICV Steps and Screenshots | Step-by-step installation, configuration, and validation with evidence screenshots |

## Output Documents

Copilot generates these as markdown in `workflows/task-1-tdd-icv/output/`, then `build_docx.py` converts them to styled DOCX.

### Output 1: Technical Design Document (`technical_design.md`)

Follow the template structure from `extracted/templates/`. The content should be mapped from inputs as follows:

| Output Section | Primary Input Source |
|---|---|
| Purpose / Introduction | Application Design Document |
| Scope | GxP Assessment Document + Application Design Document |
| System Overview | Application Design Document |
| Architecture / Components | Application Design Document |
| Workspace / Environment | Workspace Design Document |
| Interfaces and Data Flow | Application Design Document |
| Security Considerations | Application Design Document + GxP Assessment Document |
| Regulatory / GxP Requirements | GxP Assessment Document |
| Dependencies | Application Design Document + Workspace Design Document |
| Glossary / References | All input documents |

### Output 2: ICV Document (`icv_document.md`)

Follow the template structure from `extracted/templates/`. The content should be mapped from inputs as follows:

| Output Section | Primary Input Source |
|---|---|
| Purpose / Introduction | GxP Assessment Document |
| Scope | GxP Assessment Document + Application Design Document |
| Prerequisites | Workspace Design Document |
| Installation Steps | ICV Steps and Screenshots |
| Configuration Steps | ICV Steps and Screenshots + Workspace Design Document |
| Validation / Verification Steps | ICV Steps and Screenshots |
| Evidence / Screenshots | ICV Steps and Screenshots (embed images inline with each step) |
| Results Summary | ICV Steps and Screenshots |
| Sign-off / Approval | [To be completed — leave placeholder] |

## Screenshot Handling

- ICV Steps input will contain screenshots as embedded images
- After extraction, screenshots are in `extracted/images/`
- In the ICV document, embed each screenshot directly after its corresponding step:
  ```
  ### Step 3: Verify Database Connection
  Execute the connection test script and confirm successful output.

  ![Database connection verification](images/icv_steps_img_003.png)
  *Figure 3: Database connection test — successful*
  ```
- Every screenshot must have a figure number and caption

## Traceability

At the beginning of each major section, include a traceability note:
```
<!-- Source: application_design.md, Section 2.1 -->
```

This ensures auditors can trace every output section back to its source input.

## Content Rules

- Use formal, precise language appropriate for regulated documents
- Preserve all technical specifications, version numbers, and configuration values exactly
- Do not invent or assume information not present in the inputs
- If an input is missing or incomplete for a section, write: `[To be completed — requires <input document name>]`
- Maintain consistent terminology across both output documents

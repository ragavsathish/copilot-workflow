---
applyTo: "workflows/task-2-test-cases/**/*"
---

# Workflow 2: Generate Test Cases from Requirement Specification

## Purpose

Generate a regulated test case document from a requirement specification DOCX. Follow KISS (Keep It Simple and Straightforward) principles: each test case is traceable to one requirement, short, executable, and observable.

## Input Documents

Place these DOCX files in `workflows/task-2-test-cases/input/`:

| Input File | Description |
|---|---|
| Requirement Specification Document | Functional & non-functional requirements, acceptance criteria, metadata (project name, version, date) |

## Output Documents

### Output: Test Case Document (`test_cases.md`)

Follow the template structure from `extracted/templates/`. Map content from the requirement specification as follows:

| Output Section | Source / Rule |
|---|---|
| Document Information | Derive from requirement spec metadata (project name, version, date). Use `[TBD]` if not present. |
| Purpose | "This document defines test cases to verify the requirements in the input specification" |
| Scope | Mirror scope from requirement specification — what is covered and excluded |
| References | Reference the requirement specification (title, version, document ID) |
| Test Case Summary | Table listing all test case IDs, titles, requirement references, and priorities |
| Test Cases | Generate test cases from each requirement — follow KISS rules below |
| Traceability Matrix | Map requirement IDs → test case ID(s) |
| Sign-off and Approval | Placeholder (`[To be completed — Sign-off]`) |

File locations to produce:
- `workflows/task-2-test-cases/plan.md` — PLAN phase (see Plan Format)
- `workflows/task-2-test-cases/output/test_cases.md` — DO phase output

## KISS Test Case Rules (enforced)

- One requirement → one or more test cases. Never combine multiple requirement IDs into a single test case.
- One test step = one action. Do not bundle actions.
- Expected results must be observable (UI text, HTTP status, return value, DB row existence, file created, etc.).
- Pre-conditions: minimal (1–3 bullets).
- No implementation details — write from the tester/user perspective.
- Use imperative verbs: click, enter, select, verify, confirm.
- Priority reflects risk: High (core/regulatory), Medium (important), Low (nice‑to‑have).
- Use consistent terminology from the requirement specification.

### Test Case Structure (exact format)

Each test case must follow this block exactly:

```markdown
<!-- Source: requirement_specification.docx, REQ-XXX -->
### TC-<NNN>: <Short descriptive title>

**Requirement:** <Requirement ID from the input spec>
**Priority:** <High | Medium | Low>
**Pre-conditions:**
- <bullet 1>
- <bullet 2>

**Test Steps:**

| Step | Action | Expected Result |
|---|---|---|
| 1 | <Single clear action> | <Observable outcome> |
| 2 | <Next action> | <Observable outcome> |

**Post-conditions:** <State of the system after the test>
<!-- Note: Requirement REQ-XXX is ambiguous — test case assumes <interpretation> -->
```

- Insert the `<!-- Source: ... -->` traceability comment immediately before each requirement's test cases.
- If a requirement is ambiguous, include a single `<!-- Note: ... -->` comment with the interpretation used.
- If a requirement is untestable (no measurable acceptance criteria), list it in `plan.md` as a gap and do not create test cases for it.

## Test Case ID Convention & Ordering

- IDs: `TC-001`, `TC-002`, ... (zero-padded to 3 digits).
- Group related test cases together (e.g., authentication tests before inventory).
- Numbering is sequential across the document.

## Coverage Rules

- Every functional requirement must have at least one test case.
- Non-functional requirements get test cases when testable (e.g., "response time <= 500 ms"); if NFR lacks thresholds, flag as a gap in `plan.md`.
- High priority requirements should include positive, negative, and boundary tests where applicable.
- For each requirement consider: positive case, negative case, boundary/limits.

## Plan Format (`plan.md`)

Create `workflows/task-2-test-cases/plan.md` during the PLAN phase. It must include:

- Status block (Phase: PLAN, Created: <date>, Approved: pending)
- Input Documents Found list with file names, lines, image counts
- Template Structure (list sections from `extracted/templates/`)
- Generation Plan table:

| Requirement ID | Requirement Title | Test Cases Planned | Priority |
|---|---|---|---|

- For each requirement, list:
  - Source (file + section or derived)
  - Planned test case IDs and type (positive/negative/boundary)
  - Priority
- Total test case estimate
- Gaps: ambiguous or untestable requirements (reasons)
- Revision history

Example row:
| REQ-001 | User login with SSO | TC-001 (positive), TC-002 (invalid creds), TC-003 (session timeout) | High |

After creating `plan.md`, STOP and ask the user for approval. DO NOT generate `test_cases.md` until approval is given.

## DO Phase: generation rules (after approval)

- Update `plan.md` to `Approved: yes` and `Phase: DO`.
- Generate `workflows/task-2-test-cases/output/test_cases.md`.
- Every output markdown must begin with YAML frontmatter:

```yaml
---
title: "Test Cases for <Project>"
author: "<Author>"
date: "<YYYY-MM-DD>"
version: "<version>"
document_id: "<DOC-ID or [TBD]>"
status: "Draft"
---
```

- Use traceability comments before each test case.
- Add a Test Case Summary table near the top:

| Test Case ID | Title | Requirement | Priority |
|---|---|---|---|

- At end, include Traceability Matrix:

| Requirement ID | Requirement Title | Test Case ID(s) |
|---|---|---|

- Leave Sign-off and Approval as placeholder for later completion.

## Traceability & GxP Rules

- Start each major section and each test-case block with `<!-- Source: requirement_specification.docx, Section X or REQ-XXX -->`.
- Preserve exact requirement IDs and titles from the source.
- Do not invent requirement IDs. If none exist, derive `REQ-###` deterministically (e.g., `REQ-DERIVED-001`) and flag as derived in `plan.md`.

## Ambiguities & Gaps

- If acceptance criteria are missing or non-measurable, flag requirement as a gap in `plan.md` and include a recommended clarification.
- If the spec lacks numeric thresholds for NFRs, propose reasonable thresholds in `plan.md` (clearly marked as proposed) and defer to user approval.

## Validation & QA Checks (automated where possible)

After generation run checks:
1. Every parsed `REQ-*` appears in the traceability matrix.
2. No test case references more than one `REQ-` in the **Requirement** field.
3. All High priority requirements have ≥2 test cases (positive + negative or boundary).
4. Non-functional tests include numeric thresholds or are flagged as gaps.
5. Count of test cases matches estimate in `plan.md` (or list deviations).

## Scripts & Implementation Notes (recommended)

- Language: Python (recommended). Reason: mature DOCX parsing (python-docx) and markdown templating.
- Suggested scripts (to be created in `scripts/`):
  - `scripts/extract_docx.py` — convert input DOCX → `extracted/` markdown + images (already present in repo pattern).
  - `scripts/generate_test_cases.py` — parse extracted markdown, identify requirements, build `plan.md`, and generate `test_cases.md` after approval.
  - `scripts/validate_test_cases.py` — run the QA checks above.
- Dependencies: `python-docx`, `jinja2`, `pypandoc` (optional for DOCX build), `PyYAML`.

## Examples

Test case snippet (copy as-is):

```markdown
<!-- Source: requirement_specification.docx, REQ-001 -->
### TC-001: User can log in with valid credentials

**Requirement:** REQ-001
**Priority:** High
**Pre-conditions:**
- Tester has a valid user account

**Test Steps:**

| Step | Action | Expected Result |
|---|---|---|
| 1 | Navigate to login page | Login page loads and displays username/password fields |
| 2 | Enter valid username and password and click Sign in | User is redirected to dashboard; HTTP 200 and session cookie set |

**Post-conditions:** User is authenticated and session cookie present
```

## PDCA & User Interaction

Follow the repository PDCA lifecycle (see `.github/copilot-instructions.md`):
- PLAN: produce `plan.md` and request approval. STOP.
- DO: after user approves, generate `test_cases.md`.
- CHECK: present generated files for review (section counts, images, gaps).
- ACT: revise per feedback, update `plan.md` revision history, and repeat.

## Outputs & Where They Go

- `workflows/task-2-test-cases/plan.md` — plan for generation, must be created prior to any output.
- `workflows/task-2-test-cases/output/test_cases.md` — generated test cases (after approval).
- Reference input path in outputs: `workflows/task-2-test-cases/input/<filename>.docx`

## Content Rules (must follow)

- Use formal precise language for regulated documents.
- Preserve technical specifications, version numbers, and configuration values exactly as in the requirement spec.
- Do not invent or assume information not present in the input spec.
- If a requirement is ambiguous, include `<!-- Note: Requirement REQ-XXX is ambiguous — test case assumes <interpretation> -->`.
- If untestable, flag in `plan.md` and do not generate a test case.
- Maintain consistent terminology from the requirement specification.

## Revision Control & Handover

- Add revision history to `plan.md` with each change or approval.
- Keep `plan.md` as the single source of truth to resume workflows later.

---

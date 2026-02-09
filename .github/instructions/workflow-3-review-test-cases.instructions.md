---
applyTo: "workflows/task-3-review-test-cases/**/*"
---

# Workflow 3: Critical Review - Test Case Gap Analysis & Revision

## Purpose

Perform critical gap analysis on a test case document against its requirements specification. Collaboratively brainstorm improvements, document all findings in a single review document, and apply approved revisions to generate an updated test case document.

## PDCA Cycle for Workflow-3

```
EXTRACT → PLAN → GAP_ANALYSIS → BRAINSTORM → REVISE → COMPLETE
            ↓         ↓              ↓            ↓
         (STOP)   (STOP)        (STOP)      (STOP)
```

**Key Principle**: Never modify test cases until the review document is approved. All findings are logged first, discussed collaboratively, then revised based on explicit approval.

---

## Input Documents

Place these DOCX files in `workflows/task-3-review-test-cases/input/`:

| Input File | Description |
|---|---|
| Requirements Specification | The baseline requirements document (can be from workflow-1 or external) |
| Test Cases Document | The test case document to review (can be from workflow-2 or external) |

---

## Output Documents

### 1. Review Document (`review-YYYY-MM-DD.md`)

**Single source of truth** for the entire review process. Created during PLAN phase, populated during GAP_ANALYSIS, updated with user decisions during BRAINSTORM, and marked complete after REVISE.

### 2. Revised Test Case Document (`test_cases_v<X.Y>.md` and `.docx`)

Generated **only after** the review document is approved. Located in `workflows/task-3-review-test-cases/output/`.

---

## Phase 1: EXTRACT (Pre-Cycle Setup)

Extract both input documents:

```bash
python scripts/extract_docx.py workflows/task-3-review-test-cases
```

This creates:
- `extracted/requirements_spec.md` + images
- `extracted/test_cases.md` + images
- `extracted/templates/` (if templates present)

---

## Phase 2: PLAN

Create `workflows/task-3-review-test-cases/review-YYYY-MM-DD.md` with:

```markdown
# Critical Review: <Test Case Document Name>

## Document Overview
- **Test Case Document**: <filename> (<version>)
- **Requirements Document**: <filename> (<version>)
- **Total Test Cases**: <count>
- **Total Requirements**: <count>
- **Review Date**: YYYY-MM-DD
- **Review Round**: 1

## Status
- Phase: PLAN
- Approved: pending

## Review Scope
What will be analyzed:
- [ ] Requirements coverage completeness
- [ ] Test case quality (KISS, traceability, observability)
- [ ] Edge cases and negative scenarios
- [ ] Ambiguous requirements needing clarification
- [ ] Traceability matrix validation

## Review Baseline
Reviewing against:
- [ ] Workflow-2 KISS rules (if applicable)
- [ ] GxP traceability requirements
- [ ] Observable expected results
- [ ] Risk-based coverage adequacy

## Sections (placeholders — will be populated in GAP_ANALYSIS phase)
- Part 1: Requirements Coverage Analysis
- Part 2: Test Case Quality Issues  
- Part 3: Scenario Gaps (What-If Analysis)
- Part 4: Requirements Needing Clarification
- Part 5: Traceability Matrix Validation
- Part 6: Priority & Risk Assessment

## Revision History
| Round | Date | Phase | Notes |
|---|---|---|---|
| 1 | YYYY-MM-DD | PLAN | Initial review plan created |
```

**STOP here. Show the plan to the user and ask: "Does this review scope look right? Should I proceed with gap analysis?"**

Do not proceed to GAP_ANALYSIS until user approves.

---

## Phase 3: GAP_ANALYSIS

After user approves the plan:

1. Update `review-YYYY-MM-DD.md` status: `Phase: GAP_ANALYSIS`, `Approved: yes`
2. Perform comprehensive analysis and populate all sections:

### Part 1: Requirements Coverage Analysis

#### 1.1 Requirements with NO Test Cases [CRITICAL]

For each requirement that has zero test case coverage:

```markdown
| Req ID | Title | Risk | Why It Matters |
|---|---|---|---|
| REQ-XXX | <title> | High/Medium/Low | <impact explanation> |
```

Then add brainstorming section:

```markdown
**Brainstorm**:
- Option A: <suggested approach>
- Option B: <alternative approach>
- Other considerations: <notes>

**Your Input**: 
**Decision**: [PENDING]
```

#### 1.2 Requirements with Inadequate Coverage [MAJOR]

For each requirement with partial coverage (e.g., only happy path, missing edge cases):

```markdown
#### REQ-XXX: <Title>
**Current Coverage**: TC-YYY (describe what's tested)
**Missing Scenarios**:
- Boundary: <scenario>
- Edge: <scenario>
- Negative: <scenario>
- Error path: <scenario>

**Brainstorm**: <options for addressing>
**Your Input**:
**Decision**: [PENDING]
```

### Part 2: Test Case Quality Issues

#### 2.1 Ambiguous Expected Results

List test cases with vague, unmeasurable, or subjective expected results:

```markdown
| TC ID | Location | Issue | Recommended Fix |
|---|---|---|---|
| TC-XXX | Step N | "System responds quickly" | "Response time < 2 seconds" |
```

#### 2.2 Missing Traceability

List test cases without requirement references or with incorrect references:

```markdown
| TC ID | Issue |
|---|---|
| TC-XXX | No requirement reference |
| TC-YYY | References non-existent REQ-999 |
```

#### 2.3 KISS Violations

List test cases that violate KISS principles:

```markdown
| TC ID | Violation | Impact |
|---|---|---|
| TC-XXX | Step combines 2 actions | Hard to identify which action failed |
| TC-YYY | Implementation details exposed | Requires technical knowledge |
```

### Part 3: Scenario Gaps (What-If Analysis)

Brainstorm untested edge cases and "what-if" scenarios:

```markdown
**Scenario**: <Description of untested scenario>
- **Risk**: High/Medium/Low
- **Current Coverage**: None / Partial
- **Related Req**: REQ-XXX
**Brainstorm**: <options>
**Your Input**:
**Decision**: [PENDING]
```

Focus on:
- Concurrency issues
- Network failures
- Data edge cases (empty, max size, special characters)
- User interruptions (browser close, navigation away)
- System failures (DB down, disk full)

### Part 4: Requirements Needing Clarification

List requirements with ambiguous acceptance criteria that block effective testing:

```markdown
| Req ID | Issue | Blocking Test Case? |
|---|---|---|
| REQ-XXX | "Acceptable performance" not measurable | Yes - TC-YYY cannot pass/fail |
```

**Brainstorm**: How to proceed? Block review until clarified? Document assumptions? Mark as untestable?

### Part 5: Traceability Matrix Validation

Generate coverage summary:

```markdown
| Status | Count | Details |
|---|---|---|
| ✅ Full coverage (2+ TCs) | X reqs | List critical ones |
| ⚠️ Minimal coverage (1 TC) | X reqs | List ones needing more |
| ❌ No coverage | X reqs | Critical gap (list all) |
| ⚠️ Orphan TCs (no req) | X TCs | List IDs |
```

### Part 6: Priority & Risk Assessment

Categorize all gaps by risk:

```markdown
### High-Risk Gaps (Must Address)
1. REQ-XXX (<issue>) - no coverage
2. REQ-YYY (<issue>) - inadequate coverage

### Medium-Risk Gaps (Should Address)
1. <Issue category> (N requirements)

### Low-Risk (Nice to Have)
1. <Issue category>

**Brainstorm**: Which tier do we tackle this round?
**Your Input**:
```

---

After completing all sections, add:

```markdown
## Executive Summary
- ✅ **Covered Requirements**: X/Y (Z%)
- ⚠️ **Missing Coverage**: N requirements have no test cases
- ⚠️ **Inadequate Coverage**: N requirements need additional scenarios
- ⚠️ **Ambiguous Test Cases**: N test cases have unclear steps/results
- ❌ **Critical Gaps**: N high-risk scenarios untested

## Brainstorming Summary
**Before proceeding to revisions, we need to:**
1. Decide on gaps to address in this iteration
2. Clarify ambiguous requirements (may need stakeholder input)
3. Agree on new test case structure (detailed vs. consolidated)
4. Prioritize: what MUST be fixed vs. nice-to-have
```

3. Update status: `Phase: BRAINSTORM`

**STOP here. Present the full review document to the user and say: "I've completed the gap analysis. Please review all findings and mark your decisions in each 'Your Input' section. Reply when ready to discuss or approve revisions."**

Do not proceed to REVISE until user approves.

---

## Phase 4: BRAINSTORM (Collaborative)

This phase is interactive. The user will:

1. Read all findings in `review-YYYY-MM-DD.md`
2. Fill in "Your Input" sections with feedback, questions, or decisions
3. Mark decisions: `ACCEPT`, `REJECT`, `MODIFY`, or `DEFER` for each gap
4. Discuss unclear items via chat

Your role:
- Answer clarifying questions
- Provide additional context if needed
- Suggest alternatives when asked
- **Do NOT make changes to test cases yet**

Once the user says "approved", "proceed with revisions", or similar:

1. Add a **Revision Plan** section to `review-YYYY-MM-DD.md`:

```markdown
## Revision Plan (Approved)

### Status: APPROVED
**Approved by**: <user name/initials>
**Approved on**: YYYY-MM-DD HH:MM

### Changes to Apply:

#### Add New Test Cases:
- [ ] TC-XXX: <description> → REQ-YYY
- [ ] TC-XXX: <description> → REQ-YYY

#### Modify Existing Test Cases:
- [ ] TC-XXX Step N: Change "<old>" → "<new>"
- [ ] TC-YYY: <modification description>

#### Fix Traceability:
- [ ] TC-XXX: Add requirement reference REQ-YYY
- [ ] TC-XXX: Change REQ-AAA → REQ-BBB

#### Update Traceability Matrix:
- [ ] Add row: REQ-XXX → TC-AAA, TC-BBB
- [ ] Update row: REQ-YYY → (add TC-CCC)

#### Update Test Case Summary Table:
- [ ] Add N new rows for TC-XXX through TC-YYY
- [ ] Update total count: X → Y test cases

#### Document Updates:
- [ ] Update version in YAML frontmatter (e.g., 1.0 → 1.1)
- [ ] Update date in YAML frontmatter to YYYY-MM-DD
- [ ] Add revision note in document's Revision History section

### Deferred Items:
- Gap-XXX: <reason for deferral>
- Scenario-YYY: <reason for deferral>
```

2. Update status: `Phase: REVISE`

---

## Phase 5: REVISE

After approval, generate the updated test case document:

### Step 1: Update Test Cases Markdown

1. Read the current test case document from `extracted/test_cases.md`
2. Apply all approved changes from the Revision Plan:
   - Add new test cases in the correct sections (maintain TC-ID order)
   - Modify existing test cases as specified
   - Fix traceability comments (`<!-- Source: ... -->`)
   - Update Test Case Summary table
   - Update Traceability Matrix
   - Update YAML frontmatter (version, date)
   - Add entry to document's Revision History section

3. Write updated document to: `workflows/task-3-review-test-cases/output/test_cases_v<X.Y>.md`

**Preserve formatting**:
- Maintain YAML frontmatter structure
- Keep KISS test case format (see workflow-2 rules)
- Keep traceability comments before each test case
- Maintain table formatting
- Keep section numbering consistent

### Step 2: Build Updated DOCX

```bash
python scripts/build_docx.py workflows/task-3-review-test-cases
```

### Step 3: Generate Change Summary

Add to `review-YYYY-MM-DD.md`:

```markdown
## Post-Revision Verification

### Changes Applied: ✅ COMPLETE

**Test Cases Before**: X
**Test Cases After**: Y
**Test Cases Added**: N
**Test Cases Modified**: N
**Traceability Issues Fixed**: N

**Files Generated**:
- `workflows/task-3-review-test-cases/output/test_cases_v<X.Y>.md`
- `workflows/task-3-review-test-cases/output/test_cases_v<X.Y>.docx`

### Change Summary:
```diff
+ Added TC-XXX: <description>
+ Added TC-YYY: <description>
~ Modified TC-ZZZ Step N: <change>
~ Modified TC-AAA: <change>
```

### Verification Checklist:
- [x] All approved new test cases added
- [x] All approved modifications applied
- [x] Traceability matrix updated
- [x] Test case summary table updated
- [x] YAML frontmatter updated
- [x] Document builds successfully to DOCX
- [x] No regression (existing TCs not accidentally changed)
```

### Step 4: Update Review Document Status

```markdown
## Status
- Phase: COMPLETE
- Approved: yes
- Revision completed: YYYY-MM-DD HH:MM

## Revision History
| Round | Date | Phase | Notes |
|---|---|---|---|
| 1 | YYYY-MM-DD | PLAN | Initial review plan created |
| 1 | YYYY-MM-DD | GAP_ANALYSIS | Analysis complete, findings documented |
| 1 | YYYY-MM-DD | BRAINSTORM | User reviewed and approved revision plan |
| 1 | YYYY-MM-DD | COMPLETE | Revisions applied, test_cases_v1.1 generated |
```

**STOP here. Report to user:**

```
Review complete! Updated test case document generated:
- Markdown: workflows/task-3-review-test-cases/output/test_cases_v1.1.md
- DOCX: workflows/task-3-review-test-cases/output/test_cases_v1.1.docx

Changes:
- Added: N test cases
- Modified: N test cases
- Fixed: N traceability issues

Review document saved: workflows/task-3-review-test-cases/review-2026-02-09.md
```

---

## Resuming Workflow-3

If workflow-3 was started in a previous conversation, read `review-YYYY-MM-DD.md` (match `review-*.md` for most recent) to determine where to resume:

| Status in `review-*.md` | What to do |
|---|---|
| No `review-*.md` exists | Start from EXTRACT |
| `Phase: PLAN`, `Approved: pending` | Show plan, ask for approval |
| `Phase: GAP_ANALYSIS`, gaps populated | Show review doc, ask user to provide decisions |
| `Phase: BRAINSTORM`, decisions pending | Continue discussion, wait for approval |
| `Phase: REVISE` | Apply approved changes, rebuild DOCX |
| `Phase: COMPLETE` | Report that review is done, show output location |

---

## KISS Test Case Format (Reference from Workflow-2)

When adding or modifying test cases, follow this exact structure:

```markdown
<!-- Source: requirement_specification.docx, REQ-XXX -->
### TC-<NNN>: <Short descriptive title>

**Requirement:** <Requirement ID>
**Priority:** <High | Medium | Low>
**Pre-conditions:**
- <bullet 1>
- <bullet 2>

**Test Steps:**

| Step | Action | Expected Result |
|---|---|---|
| 1 | <Single clear action> | <Observable outcome> |
| 2 | <Next action> | <Observable outcome> |

**Post-conditions:** <State of system after test>
```

---

## GxP Traceability Rules

- Every new or modified test case must have a traceability comment: `<!-- Source: requirements_spec.md, REQ-XXX -->`
- All changes must be tracked in the document's Revision History section
- Version numbers must increment (e.g., 1.0 → 1.1 for minor, 1.0 → 2.0 for major)
- The review document (`review-YYYY-MM-DD.md`) serves as the audit trail for all decisions

---

## General Rules

- **One review document per review cycle** (can span multiple rounds if needed)
- **Never modify test cases without approval** — all findings logged first
- **All decisions must be explicit** — no assumptions about what user wants
- **Preserve existing content** — only change what's approved
- **Maintain KISS principles** — even during revisions
- **Keep review document updated** — single source of truth for entire cycle

---

## Example Workflow-3 Execution

```
User: "Review workflow-3"
  ↓
Copilot: Extracts both documents
  ↓
Copilot: Creates review-2026-02-09.md with PLAN
  "Does this review scope look right?"
  ↓ (user: "yes")
Copilot: Performs gap analysis, populates all findings
  "I've completed analysis. Please review and mark decisions."
  ↓ (user reviews, fills in decisions)
User: "I've marked my decisions. Proceed with revisions."
  ↓
Copilot: Adds Revision Plan to review doc
Copilot: Updates test_cases.md with approved changes
Copilot: Builds test_cases_v1.1.docx
Copilot: Updates review doc to Phase: COMPLETE
  "Review complete! Files: output/test_cases_v1.1.docx"
```

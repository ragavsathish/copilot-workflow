---
applyTo: "workflows/task-4-retrospect/**/*"
---

# Workflow 4: Retrospective & Continuous Improvement

## Purpose

Lightweight, manual retrospective process to capture learnings from workflow executions and systematically improve instruction files. After completing any workflow, run a 3-question retrospective (~3 minutes) to document what worked, what broke, and what to improve.

## Core Philosophy

**Max 3 questions per workflow** - Quality over quantity. Focus on actionable insights:
1. **What happened** (execution outcome)
2. **What broke or worked** (key learning)
3. **What to fix** (actionable improvement)

## When to Run

After any workflow execution reaches:
- ✅ **COMPLETE** (successful) - Capture what worked well
- ⏸️ **Partial** (stopped at PLAN/DO/CHECK) - Capture process gaps
- ❌ **Failed** (error or blocking issue) - Capture critical issues

## PDCA Cycle for Retrospectives

```
TRIGGER → ANALYZE → INTERVIEW (3Q) → SYNTHESIZE → APPLY
   ↓         ↓          ↓              ↓           ↓
(user)   (auto)    (3 min)         (auto)     (approve)
```

---

## Phase 1: TRIGGER

**User initiates:**
```
User: "retrospect workflow N"
```

**Copilot identifies:**
- Target workflow directory: `workflows/task-N-<name>/`
- Most recent plan file: `plan-YYYY-MM-DD.md` (or `plan.md`)
- Output directory: `workflows/task-N-<name>/output/`

---

## Phase 2: ANALYZE (Automated)

**Copilot scans and analyzes:**

### Artifact Analysis
- **Plan file status**: Phase reached, approval status, creation date
- **Outputs generated**: Count files in `output/`, check vs. plan expectations
- **Extracted inputs**: Verify all required inputs present
- **Metrics**: Traceability coverage, template adherence, image embedding

### Auto-Generated Summary
```
Workflow N Analysis:
- Phase reached: [EXTRACT/PLAN/DO/CHECK/COMPLETE]
- Plan approved: [yes/no/pending]
- Outputs generated: [X/Y files]
- Completion: [percentage]
- Issues detected: [list if any]
```

**Time:** ~30 seconds

---

## Phase 3: INTERVIEW (3 Questions)

**Copilot asks exactly 3 questions:**

### Question 1: Execution Outcome
**"Did the workflow complete successfully? If not, where did it stop?"**

Options:
- ✅ Complete (reached end of CHECK/COMPLETE phase)
- ⏸️ Partial (stopped at: EXTRACT / PLAN / DO / CHECK)
- ❌ Failed (error or blocking issue)

User provides 1-2 sentence notes.

### Question 2: Critical Learning
**"What's the ONE most important thing you learned - good or bad?"**

This could be:
- Something that worked really well (preserve it)
- A blocking issue (fix it urgently)
- A confusing step (clarify it)
- A time-waster (improve it)

User provides 2-3 sentence answer.

### Question 3: Immediate Action
**"What ONE change would most improve this workflow?"**

Be specific:
- Add [example/clarification] to section X
- Fix [issue] by doing Y
- Add checkpoint/validation for Z
- Remove/simplify step W

User provides 1-2 sentence concrete action.

**Time:** ~3 minutes

---

## Phase 4: SYNTHESIZE (Automated)

**Copilot combines:**
1. Artifact analysis (from Phase 2)
2. User answers (from Phase 3)

**Categorizes learnings:**
- ✅ **Patterns Validated** (preserve)
- ⚠️ **Issues Identified** (fix)
- 🔄 **Process Improvements** (add)
- 📚 **Documentation Gaps** (clarify)
- ⭐ **Quality Enhancements** (improve)
- 🛠️ **Tool Improvements** (enhance scripts)

**Assigns priority:**
- **P0 (Critical)**: Blocking issues, failed executions
- **P1 (Important)**: Partial completions, major improvements
- **P2 (Nice-to-have)**: Minor enhancements, optimizations

**Generates retrospective report:**
- File: `workflows/task-4-retrospect/retrospectives/workflow-N-retro-YYYY-MM-DD.md`
- Includes: User answers, artifact analysis, categorized learnings, proposed changes

**Time:** ~1 minute

---

## Phase 5: APPLY (With User Approval)

**Copilot presents:**
```
Retrospective complete for Workflow N!

Found:
- [N] patterns to preserve
- [N] issues to fix (P0: X, P1: Y, P2: Z)
- [N] process improvements
- [N] documentation gaps

Ready to update workflow-N instructions? [y/n]
```

**If user approves:**

1. **Backup original instruction file:**
   ```
   .github/instructions/workflow-N-<name>.instructions.md
   → .github/instructions/workflow-N-<name>.instructions.md.backup-YYYY-MM-DD
   ```

2. **Append "Learnings & Improvements" section** to instruction file (if not exists)

3. **Add learnings** in structured format:
   ```markdown
   ## Learnings & Improvements
   
   ### Retrospective History
   | Date | Phase | Key Improvements |
   
   ### ✅ Patterns Validated
   [Learnings with references]
   
   ### ⚠️ Issues Fixed
   [Learnings with P0/P1/P2 tags]
   
   [etc. for all 6 categories]
   ```

4. **Update revision history** in instruction file

5. **Report completion:**
   ```
   Updated: .github/instructions/workflow-N-<name>.instructions.md
   Backup: .github/instructions/workflow-N-<name>.instructions.md.backup-YYYY-MM-DD
   Retrospective: workflows/task-4-retrospect/retrospectives/workflow-N-retro-YYYY-MM-DD.md
   ```

**Time:** ~2 minutes

---

## Retrospective Report Format

**File:** `workflows/task-4-retrospect/retrospectives/workflow-N-retro-YYYY-MM-DD.md`

```markdown
# Retrospective: Workflow N

**Date:** YYYY-MM-DD
**Workflow:** Task-N-<name>
**Phase Reached:** [phase]
**Status:** [✅ Complete / ⏸️ Partial / ❌ Failed]

## Artifact Analysis

- Plan file: [filename]
- Plan status: Phase [X], Approved [yes/no]
- Outputs generated: [X/Y files]
- Completion: [percentage]

## User Interview (3 Questions)

### Q1: Execution Outcome
[User answer]

### Q2: Critical Learning
[User answer]

### Q3: Immediate Action
[User answer]

## Learnings Identified

### ✅ Patterns Validated (Preserve)
**L[N].1: [Pattern Name]** *(Priority: P2)*
- **Description:** [What worked]
- **Evidence:** [Q2 or artifact reference]
- **Recommendation:** Preserve in all workflows
- **Status:** Documented ✅

### ⚠️ Issues Identified (Fix)
**L[N].2: [Issue Name]** *(Priority: P0)*
- **Description:** [What went wrong]
- **Evidence:** [Q1/Q2 or artifact reference]
- **Impact:** [Severity]
- **Recommendation:** [Specific fix]
- **Status:** Pending fix ⚠️

[Continue for all 6 categories...]

## Instruction Updates Applied

**File:** `.github/instructions/workflow-N-<name>.instructions.md`

**Changes:**
- Added "Learnings & Improvements" section
- Documented [N] learnings
- Updated revision history

**Backup:** `.github/instructions/workflow-N-<name>.instructions.md.backup-YYYY-MM-DD`
```

---

## Learnings Section Format (Added to Instruction Files)

```markdown
---

## Learnings & Improvements

This section documents lessons learned from actual executions and continuous improvements applied to this workflow.

### Retrospective History

| Date | Session | Phase Reached | Key Improvements |
|------|---------|---------------|------------------|
| YYYY-MM-DD | Retro-N | [phase] | [summary] |

---

### ✅ Patterns Validated (Preserve)

**L[N].1: [Pattern Name]** *(Added: YYYY-MM-DD)*
- **What worked:** [Description]
- **Evidence:** Retrospective [date], Q2 response + [artifact]
- **Keep doing:** [Specific practice to maintain]

---

### ⚠️ Issues Fixed

**L[N].2: [Issue Name]** *(Priority: P0, Fixed: YYYY-MM-DD)*
- **Problem:** [What went wrong]
- **Impact:** [Severity - Critical/High/Medium/Low]
- **Solution:** [How it was fixed]
- **Prevention:** [How to avoid in future]

---

### 🔄 Process Improvements Added

**L[N].3: [Improvement Name]** *(Priority: P1, Added: YYYY-MM-DD)*
- **Gap identified:** [What was missing]
- **Improvement:** [What was added to instructions]
- **Benefit:** [Expected impact]

---

### 📚 Documentation Enhancements

**L[N].4: [Enhancement Name]** *(Priority: P1, Added: YYYY-MM-DD)*
- **Confusion point:** [What was unclear]
- **Clarification added:** [Section and content added]
- **Helps with:** [Common question addressed]

---

### ⭐ Quality Enhancements

**L[N].5: [Enhancement Name]** *(Priority: P2, Added: YYYY-MM-DD)*
- **Quality gap:** [What could be better]
- **Enhancement:** [Validation/review step added]
- **Result:** [Expected improvement]

---

### 🛠️ Tool Improvements

**L[N].6: [Tool Name]** *(Priority: P2, Status: Deferred)*
- **Tool:** [Script name]
- **Enhancement needed:** [What should be improved]
- **Benefit:** [Automation/reliability gain]
- **Note:** Tool improvements may be implemented in future iterations

---

## Known Issues & Workarounds

| Issue | Workaround | Status |
|-------|------------|--------|
| [Issue description] | [Manual workaround] | Pending/In Progress/Fixed |

---

## Troubleshooting Guide

### Problem: [Common issue]
**Symptoms:** [How you know this is the problem]
**Cause:** [Why it happens]
**Solution:** [Step-by-step fix]
**Prevention:** [How to avoid it next time]

---
```

---

## Priority Assignment Logic (Automated)

**P0 (Critical) - Fix Immediately:**
- Q1 = ❌ Failed
- Q1 = ⏸️ Partial + Q2 mentions "blocking" or "stopped"
- Q2 contains keywords: "critical", "blocking", "failed", "broken", "error"
- Outputs expected but not generated

**P1 (Important) - Address Soon:**
- Q1 = ⏸️ Partial (non-blocking)
- Q2 mentions: "confusing", "unclear", "difficult", "slow"
- Q3 is achievable quick win
- Process gap affecting efficiency

**P2 (Nice-to-have) - Future Improvement:**
- Q1 = ✅ Complete
- Q2 mentions: "could be better", "would be nice"
- Q3 is enhancement (not fix)
- Tool improvements (script enhancements)

---

## Category Detection (Automated)

**From User Answers:**

**✅ Patterns Validated:**
- Keywords: "worked well", "helpful", "clear", "smooth", "great", "perfect"
- Q1 = Complete + Q2 positive

**⚠️ Issues Identified:**
- Keywords: "failed", "error", "broken", "blocked", "didn't work", "stopped"
- Q1 = Failed or Partial
- Q2 describes problem

**🔄 Process Improvements:**
- Keywords: "missing", "need", "should add", "checkpoint", "validation"
- Q3 mentions: "add checkpoint", "verify", "validate", "automate"

**📚 Documentation Gaps:**
- Keywords: "unclear", "confusing", "didn't understand", "no example"
- Q2 mentions: "unclear", "confused", "didn't know"
- Q3 mentions: "add example", "clarify", "document"

**⭐ Quality Enhancements:**
- Keywords: "quality", "review", "validate", "check"
- Q3 mentions: "add review", "improve output", "better quality"

**🛠️ Tool Improvements:**
- Keywords: "script", "automate", "tool", "build"
- Q3 mentions: "enhance script", "build tool", "automate"

---

## Output Artifacts

### Per Retrospective
1. `workflows/task-4-retrospect/retrospectives/workflow-N-retro-YYYY-MM-DD.md` - Full report
2. `.github/instructions/workflow-N-<name>.instructions.md` - Updated (with new section)
3. `.github/instructions/workflow-N-<name>.instructions.md.backup-YYYY-MM-DD` - Backup

### Aggregate (Optional)
4. `workflows/task-4-retrospect/learnings_summary.md` - Cross-workflow insights
5. `.github/learnings_registry.md` - Central tracking (future enhancement)

---

## Benefits of This Approach

1. **Minimal time:** 3 minutes of user input per workflow
2. **Focused:** Forces prioritization on what really matters
3. **Actionable:** Q3 guarantees concrete next step
4. **Sustainable:** Won't feel like burden after every workflow
5. **Sufficient:** Combined with artifact analysis = complete picture
6. **Traceable:** All learnings documented with evidence
7. **Cumulative:** Builds institutional knowledge over time

---

## Usage Example

```
User: "retrospect workflow 1"

Copilot: [Analyzes artifacts in 30 seconds]

Copilot: "Quick retrospective for Workflow 1 (3 questions, ~3 min):

Q1: Did the workflow complete successfully? If not, where did it stop?
Options: ✅ Complete / ⏸️ Partial / ❌ Failed"

User: "✅ Complete - generated both documents"

Copilot: "Q2: What's the ONE most important thing you learned?"

User: "The detailed mapping table in the plan was incredibly helpful. 
Made it crystal clear how inputs map to outputs."

Copilot: "Q3: What ONE change would most improve this workflow?"

User: "Add a validation checklist for the CHECK phase. Right now 
there's no structured way to verify outputs."

Copilot: [Synthesizes in 1 minute]

Copilot: "Retrospective complete!

Found:
- 1 pattern to preserve (mapping tables) ✅
- 1 process improvement (CHECK validation checklist) 🔄

Ready to update workflow-1 instructions? [y/n]"

User: "y"

Copilot: [Updates instruction file in 2 minutes]

Copilot: "Done!
- Updated: .github/instructions/workflow-1-tdd-icv.instructions.md
- Backup: .github/instructions/workflow-1-tdd-icv.instructions.md.backup-2026-02-09
- Report: workflows/task-4-retrospect/retrospectives/workflow-1-retro-2026-02-09.md"
```

---

## Future Enhancements (Optional)

1. **Chat log parsing:** Automate extraction from VSCode chat sessions
2. **Learnings registry:** Central dashboard of all learnings across workflows
3. **Metrics tracking:** Trend analysis (execution time, issue count over time)
4. **Cross-workflow patterns:** Identify common issues/patterns across multiple workflows
5. **Automated script improvements:** Generate code patches based on tool improvement learnings

---

## Workflow Dependencies

**Inputs:**
- Completed or partially completed workflow (any task-N)
- User availability (3 minutes for interview)

**Outputs:**
- Retrospective report in `retrospectives/`
- Updated instruction file with "Learnings & Improvements" section
- Backup of original instruction file

**No blocking dependencies** - Can run retrospective on any workflow at any time.

---

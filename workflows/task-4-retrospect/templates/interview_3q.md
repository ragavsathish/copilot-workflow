# Retrospective Interview: Workflow N

**Date:** YYYY-MM-DD
**Workflow:** Task-N-<name>
**Duration:** ~3 minutes

---

## Question 1: Execution Outcome

**Did the workflow complete successfully? If not, where did it stop?**

Select one:
- [ ] ✅ **Complete** - Reached end of CHECK/COMPLETE phase
- [ ] ⏸️ **Partial** - Stopped at: ___________ (EXTRACT / PLAN / DO / CHECK)
- [ ] ❌ **Failed** - Error or blocking issue occurred

**Brief notes (1-2 sentences):**




---

## Question 2: Critical Learning

**What's the ONE most important thing you learned - good or bad?**

This could be:
- Something that worked really well (preserve it)
- A blocking issue (fix it urgently)
- A confusing step (clarify it)
- A time-waster (improve it)

**Your answer (2-3 sentences):**






---

## Question 3: Immediate Action

**What ONE change would most improve this workflow?**

Be specific:
- Add [specific example/clarification] to section X
- Fix [specific issue] by doing Y
- Add checkpoint/validation for Z
- Remove/simplify step W

**Your recommendation (1-2 sentences with concrete action):**





---

## Auto-Captured Data (No User Input Needed)

**Copilot will analyze:**
- ✓ Plan file status (phase, approval, dates)
- ✓ Output artifacts (what was generated)
- ✓ Artifact metrics (completion %, traceability, etc.)
- ✓ Extracted inputs (presence, line counts, images)

**Combined with your 3 answers above = Complete retrospective**

---

## Time Estimate

- Question 1: 30 seconds
- Question 2: 1 minute
- Question 3: 1 minute
- **Total: ~3 minutes**

---

## What Happens Next

1. **Copilot synthesizes** your answers + artifact analysis
2. **Categorizes learnings** (✅ ⚠️ 🔄 📚 ⭐ 🛠️)
3. **Assigns priorities** (P0 Critical / P1 Important / P2 Nice-to-have)
4. **Generates retrospective report** in `retrospectives/`
5. **Proposes instruction updates** for your approval
6. **Applies learnings** to workflow-N instructions file

---

## Example Answers

### Example A: Successful Execution

**Q1:** ✅ Complete - Generated both technical_design.md and icv_document.md successfully

**Q2:** The detailed mapping table in the PLAN phase was incredibly helpful. I could see exactly how each input section mapped to outputs, which gave me confidence to approve immediately without questions.

**Q3:** Add a validation checklist template for the CHECK phase. Right now verification is informal - would be better to have a structured checklist to confirm outputs match the plan.

---

### Example B: Blocked Execution

**Q1:** ⏸️ Partial - Stopped at DO phase. Plan was approved but test cases were never generated.

**Q2:** After approving the plan, nothing happened - no progress indicator, no error message, no outputs. I waited a few minutes then had to ask where the files were. Silent failures are really frustrating.

**Q3:** Add automatic output verification after the DO phase. Something like "✓ test_cases.md (54 KB) generated successfully" or alert immediately if outputs don't exist after 30 seconds with troubleshooting steps.

---

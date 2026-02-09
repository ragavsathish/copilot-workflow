# Workflow 4: Retrospective & Continuous Improvement

## Quick Start

After completing any workflow, run a **3-minute retrospective** to capture learnings and improve instructions.

```
User: "retrospect workflow N"
```

Copilot will:
1. Analyze workflow artifacts (30 sec)
2. Ask you 3 quick questions (3 min)
3. Generate learnings report (1 min)
4. Update instruction file with improvements (2 min)

**Total time: ~6 minutes**

---

## Why Retrospectives?

**Capture what you learned** - Both successes and failures
- What worked well → Preserve in future workflows
- What broke → Fix immediately  
- What was confusing → Clarify in docs
- What was tedious → Automate or streamline

**Continuous improvement** - Each workflow execution improves the next one
- Build institutional knowledge over time
- Reduce repeated mistakes
- Standardize successful patterns
- Make workflows more robust

---

## The 3 Questions

### Q1: Execution Outcome
**"Did the workflow complete successfully? If not, where did it stop?"**
- ✅ Complete
- ⏸️ Partial (stopped at which phase?)
- ❌ Failed (blocking issue?)

### Q2: Critical Learning
**"What's the ONE most important thing you learned - good or bad?"**
- Focus on the biggest insight
- Could be positive (worked well) or negative (broke)

### Q3: Immediate Action
**"What ONE change would most improve this workflow?"**
- Be specific and actionable
- What to add, fix, clarify, or remove

**That's it!** 3 questions, ~3 minutes.

---

## What Gets Updated

After each retrospective, **workflow instructions get improved** with:

### Learnings & Improvements Section
Added to `.github/instructions/workflow-N-<name>.instructions.md`:

- ✅ **Patterns Validated** - What worked well (preserve it)
- ⚠️ **Issues Fixed** - What broke (fixed it)
- 🔄 **Process Improvements** - What was missing (added it)
- 📚 **Documentation Enhancements** - What was unclear (clarified it)
- ⭐ **Quality Enhancements** - How to improve quality
- 🛠️ **Tool Improvements** - Script enhancements needed

Each learning includes:
- Description of what was learned
- Evidence (your answer + artifact analysis)
- Specific action taken
- Priority (P0 Critical / P1 Important / P2 Nice-to-have)

---

## Example: Workflow 1 Retrospective

```
User: "retrospect workflow 1"

Copilot: "Analyzing workflow-1 artifacts... Done.

Quick retrospective (3 questions):

Q1: Did the workflow complete successfully?"

User: "Yes, complete. Generated both documents."

Copilot: "Q2: What's the ONE most important thing you learned?"

User: "The mapping table in the plan was super helpful. 
Made it crystal clear how inputs map to outputs."

Copilot: "Q3: What ONE change would most improve this workflow?"

User: "Add a CHECK phase validation checklist. Right now 
verification is informal."

Copilot: "Retrospective complete!

Found:
- 1 pattern to preserve (mapping tables) ✅
- 1 process improvement (CHECK validation) 🔄

Ready to update workflow-1 instructions? [y/n]"

User: "y"

Copilot: "Done!
✓ Updated: .github/instructions/workflow-1-tdd-icv.instructions.md
✓ Backup: .github/instructions/workflow-1-tdd-icv.instructions.md.backup-2026-02-09
✓ Report: workflows/task-4-retrospect/retrospectives/workflow-1-retro-2026-02-09.md"
```

---

## File Structure

```
workflows/task-4-retrospect/
├── README.md                               ← You are here
├── templates/
│   └── interview_3q.md                    ← 3-question template
└── retrospectives/
    ├── workflow-1-retro-2026-02-09.md     ← Completed retrospectives
    ├── workflow-2-retro-2026-02-09.md
    └── workflow-N-retro-YYYY-MM-DD.md
```

Each retrospective generates:
1. **Report** in `retrospectives/` (full details)
2. **Updated instructions** in `.github/instructions/` (with new Learnings section)
3. **Backup** of original instructions (safety)

---

## When to Run

**After successful completion:**
- Capture what worked well
- Identify patterns to preserve
- Spot minor improvements

**After partial completion:**
- Identify process gaps
- Document workarounds
- Prioritize fixes

**After failures:**
- Capture critical issues (P0)
- Document troubleshooting steps
- Prevent recurrence

**Recommended:** Run retrospective after **every** workflow execution, regardless of outcome.

---

## Priority Levels

**P0 - Critical (Fix Immediately):**
- Blocking issues that prevent completion
- Failures with no workaround
- Silent errors (no error message but didn't work)

**P1 - Important (Address Soon):**
- Confusing steps that slow down execution
- Missing documentation/examples
- Process inefficiencies
- Non-blocking partial completions

**P2 - Nice-to-have (Future Improvement):**
- Minor optimizations
- Tool enhancements
- Quality improvements for already-working features

---

## Learning Categories

### ✅ Patterns Validated (Preserve)
Successful approaches to keep using:
- Helpful formats (mapping tables, traceability comments)
- Effective checkpoints (approval gates)
- Clear structures (PDCA phases)

### ⚠️ Issues Identified (Fix)
Problems that blocked or slowed execution:
- Errors encountered
- Missing outputs
- Silent failures
- Blocking issues

### 🔄 Process Improvements (Add)
Missing steps or checkpoints:
- Validation steps
- Progress indicators
- Output verification
- Dependency checking

### 📚 Documentation Gaps (Clarify)
Unclear or missing guidance:
- Confusing instructions
- Missing examples
- No troubleshooting guide
- Ambiguous requirements

### ⭐ Quality Enhancements (Improve)
Ways to improve output quality:
- Additional review steps
- Validation rules
- Quality checklists
- Better templates

### 🛠️ Tool Improvements (Enhance)
Script or automation needs:
- Script enhancements
- New automation opportunities
- Tool reliability improvements
- Performance optimizations

---

## Tips for Good Retrospectives

### For Q1 (Execution Outcome)
✅ "Complete - generated both documents"
✅ "Partial - stopped at DO phase, outputs missing"
✅ "Failed - got error X when running script Y"

❌ "It worked" (too vague)
❌ "Some issues" (what issues?)

### For Q2 (Critical Learning)
✅ "The mapping table made it clear how inputs→outputs"
✅ "Script failed silently with no error message"
✅ "Step 3 was confusing - I didn't know what 'template structure' meant"

❌ "It was okay" (not actionable)
❌ "Multiple things worked well" (pick ONE)

### For Q3 (Immediate Action)
✅ "Add example of traceability comment to section 4.2"
✅ "Add output verification: 'ls output/ && echo Success'"
✅ "Clarify step 3: add screenshot showing template structure"

❌ "Make it better" (not specific)
❌ "Add more examples" (where? for what?)

**Be specific, be concrete, be actionable!**

---

## Retrospective Reports

Each retrospective generates a detailed report in `retrospectives/`:

**File:** `workflow-N-retro-YYYY-MM-DD.md`

Contains:
- Your 3 answers
- Artifact analysis (plan status, outputs, metrics)
- Categorized learnings with evidence
- Priority assignments
- Instruction updates applied

**These reports are your audit trail** - traceability for all improvements made over time.

---

## Benefits

1. **Minimal time:** Only 3 minutes of your input
2. **Focused:** Forces you to prioritize what really matters
3. **Actionable:** Always results in concrete improvements
4. **Cumulative:** Knowledge builds up over time
5. **Traceable:** All changes documented with evidence
6. **Sustainable:** Light enough to do after every workflow

---

## Get Started

```
User: "retrospect workflow N"
```

That's it! Copilot handles the rest.

---

## Questions?

See detailed instructions in:
- `.github/instructions/workflow-4-retrospect.instructions.md` - Full process
- `templates/interview_3q.md` - Interview template with examples

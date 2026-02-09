# Workflow 3: Critical Review - Test Case Gap Analysis & Revision

## Purpose
Perform critical gap analysis on test case documents against requirements, collaboratively brainstorm improvements, and generate revised documents based on approved feedback.

## Quick Start

### 1. Place Input Documents
Copy your documents to the `input/` folder:
- Requirements specification DOCX
- Test cases DOCX to review

### 2. Run Extraction
```bash
python scripts/extract_docx.py workflows/task-3-review-test-cases
```

### 3. Start Review
Say: **"Run workflow-3"** or **"Review workflow-3"**

## Key Principles

1. **Collaborative**: You drive decisions, Copilot provides analysis
2. **No Changes Without Approval**: All findings documented first
3. **Risk-Based**: Critical gaps prioritized over minor issues
4. **KISS Maintained**: Revisions follow Keep It Simple principles
5. **Full Traceability**: Every decision tracked in review document

# Getting Started with Copilot Workflow

Welcome! This guide will walk you through everything you need to know to start using Copilot Workflow — even if you have no programming experience.

---

## What Is Copilot Workflow?

Copilot Workflow is a tool that **automatically creates regulated documents for you**. You provide your source documents (Word files), and the tool generates polished, compliant output documents — complete with your company's branding, formatting, and traceability requirements.

Think of it like having a knowledgeable assistant who:

1. Reads your input documents
2. Shows you a plan for what it will create
3. Waits for your approval before proceeding
4. Generates the output documents
5. Lets you review and request changes
6. Delivers final, styled Word documents

All of this happens inside **Visual Studio Code** (VS Code), a free text editor, using a chat window where you type simple commands in plain English.

---

## Who Is This For?

This tool is designed for teams working in **regulated environments** (GxP) — such as quality assurance, regulatory affairs, validation, and engineering teams — who need to produce compliant documents like:

- Technical Design Documents
- Installation and Configuration Verification (ICV) Documents
- Test Case Documents
- Test Case Review Reports
- Retrospective / Continuous Improvement Reports

---

## What You Will Need

Before you begin, make sure the following are set up on your computer. If any of these are missing, ask your IT team or a technical colleague for help with the installation.

| Requirement | What It Is | How to Check |
|---|---|---|
| **VS Code** | A free text editor from Microsoft where you will do all your work | Open it from your Start menu or Applications folder |
| **GitHub Copilot** | An AI assistant that runs inside VS Code | Look for the Copilot icon in the VS Code sidebar |
| **Python** | A programming language the tool uses behind the scenes | Your IT team will install this |
| **Pandoc** | A document conversion tool used behind the scenes | Your IT team will install this |
| **Project dependencies** | Supporting libraries the tool needs | Your IT team will run `pip install -r requirements.txt` |

> **Note:** You do not need to know Python or Pandoc to use this tool. They run automatically in the background.

---

## Understanding the Folder Structure

When you open the project in VS Code, you will see a set of folders on the left side. Here are the ones you will use most:

```
workflows/
  task-1-tdd-icv/
    input/       <-- Drop your input Word files here
    output/      <-- Pick up your finished Word files here

  task-2-test-cases/
    input/       <-- Drop your input Word files here
    output/      <-- Pick up your finished Word files here

  task-3-review-test-cases/
    input/       <-- Drop your input Word files here
    output/      <-- Pick up your finished Word files here

  task-4-retrospect/
    (No input files needed — just run the command)
```

**That's the key pattern:** put your files in `input/`, run the workflow, collect your results from `output/`.

---

## The Four Workflows

### Workflow 1: Technical Design + ICV Document

**What it does:** Takes your design and assessment documents and produces a Technical Design Document and an ICV Document.

**What you provide (place in `workflows/task-1-tdd-icv/input/`):**
- Application Design Document (.docx)
- Workspace Design Document (.docx)
- GxP Assessment Document (.docx)
- ICV Steps and Screenshots (.docx)

**What you get back (in `workflows/task-1-tdd-icv/output/`):**
- `technical_design.docx`
- `icv_document.docx`

**Command to type in Copilot Chat:**
> Run workflow 1

---

### Workflow 2: Test Case Generation

**What it does:** Reads your requirements specification and generates a complete set of test cases with a traceability matrix.

**What you provide (place in `workflows/task-2-test-cases/input/`):**
- Requirement Specification (.docx)

**What you get back (in `workflows/task-2-test-cases/output/`):**
- `test_cases.docx`

**Command to type in Copilot Chat:**
> Run workflow 2

---

### Workflow 3: Test Case Review and Gap Analysis

**What it does:** Reviews an existing test case document against a requirements specification. It identifies gaps, suggests improvements, and produces a revised version.

**What you provide (place in `workflows/task-3-review-test-cases/input/`):**
- Requirement Specification (.docx)
- Test Cases Document to review (.docx)

**What you get back (in `workflows/task-3-review-test-cases/output/`):**
- A review report (markdown file with findings)
- A revised test cases document (versioned .docx)

**Command to type in Copilot Chat:**
> Run workflow 3

---

### Workflow 4: Retrospective and Continuous Improvement

**What it does:** After you finish any workflow, this helps you capture what went well, what could be improved, and automatically updates the workflow instructions so the next run is even better.

**What you provide:** Nothing — just your answers to 3 quick questions.

**What you get back (in `workflows/task-4-retrospect/retrospectives/`):**
- A retrospective report with learnings and actions

**Command to type in Copilot Chat:**
> Retrospect workflow 1

(Replace `1` with whichever workflow number you just completed.)

---

## Step-by-Step: Running Your First Workflow

Here is a complete walkthrough using Workflow 2 (Test Case Generation) as an example. The process is the same for all workflows.

### Step 1: Open the Project

1. Open **VS Code**
2. Go to **File > Open Folder**
3. Navigate to the `copilot-workflow` project folder and click **Open**

### Step 2: Place Your Input Files

1. In the left-hand file explorer, navigate to `workflows/task-2-test-cases/input/`
2. Copy your **Requirement Specification** Word file into that `input/` folder
   - You can drag and drop the file, or use copy-paste

### Step 3: Open the Copilot Chat

1. Look for the **Copilot icon** in the VS Code sidebar (it looks like a small chat bubble or the Copilot logo)
2. Click it to open the Copilot Chat panel
3. Make sure you are in **Agent mode** (you should see a dropdown or toggle near the top of the chat panel — select "Agent" if available)

### Step 4: Start the Workflow

1. In the chat input box, type:
   > Run workflow 2
2. Press **Enter**

### Step 5: Review the Plan

Copilot will:
- Read your input documents
- Create a generation plan
- Show you the plan and ask for your approval

**Read the plan carefully.** It will list:
- Which input documents were found
- What sections will be generated
- How inputs map to outputs

If everything looks correct, type:
> Approved

or

> Looks good, proceed

If something is wrong or missing, tell Copilot what needs to change, for example:
> The requirement spec file wasn't picked up — it's called "ReqSpec_v2.docx"

### Step 6: Wait for Generation

Copilot will now generate the output documents. This may involve several steps running automatically. You will see progress in the chat window. There is nothing you need to do during this step.

### Step 7: Review the Output

Once generation is complete, Copilot will:
- Tell you what files were created
- Show you a summary (number of sections, test cases, etc.)
- Ask if you want any changes

**Check the output.** You can open the generated Word file from `workflows/task-2-test-cases/output/` to review it.

- If you are happy with the result, type:
  > Approved

- If you want changes, describe them in plain language:
  > Section 3.2 is missing a test case for the login timeout requirement

  > The expected result for test case TC-005 should mention the error message text

Copilot will revise and regenerate until you approve.

### Step 8: Collect Your Output

Your finished documents are in `workflows/task-2-test-cases/output/`. Copy them to wherever you need them (shared drive, email, document management system, etc.).

---

## The PDCA Cycle Explained

Every workflow follows a structured cycle called **PDCA** (Plan-Do-Check-Act). Here is what that means in practice:

| Phase | What Happens | What You Do |
|---|---|---|
| **Plan** | Copilot reads your inputs and creates a generation plan | Review the plan and approve it (or request changes) |
| **Do** | Copilot generates the output documents | Wait — this runs automatically |
| **Check** | Copilot presents the output for your review | Review the documents and approve (or request revisions) |
| **Act** | Copilot applies your requested changes | Describe any changes you want; repeat until satisfied |

This cycle ensures **nothing happens without your approval** — you are always in control.

---

## Resuming a Workflow

If your VS Code session is interrupted (computer restart, closing the window, etc.), you can pick up where you left off:

1. Open the project in VS Code again
2. Open the Copilot Chat
3. Type the same workflow command (e.g., `Run workflow 2`)

Copilot will automatically detect the previous progress and resume from where it stopped. It knows the current state by looking at plan files saved in the workflow folder.

---

## Tips for Best Results

### Preparing Your Input Documents
- Use **standard Word (.docx) format** — not PDF, not `.doc` (the older format)
- Make sure your documents have **clear headings and structure** — Copilot uses the heading hierarchy to understand the document
- **Tables** in your documents will be preserved and converted
- **Images and screenshots** (especially for ICV workflows) will be extracted automatically

### Communicating with Copilot
- Use **plain, specific language** — describe exactly what you want
- You can refer to **section numbers or headings** from your documents
- If Copilot asks a question, answer directly — it is trying to clarify your intent
- You can say **"stop"** or **"cancel"** if something is going wrong

### Managing Your Documents
- Keep one set of input files per workflow run — remove old inputs before starting a new run
- Output files are overwritten each time you run a workflow — save important outputs elsewhere before re-running
- The `extracted/` folders contain intermediate working files — you can ignore these

---

## Running a Retrospective

After completing any workflow, it is good practice to run a quick retrospective. This only requires about 3 minutes of your time and helps the tool improve over time.

1. In Copilot Chat, type:
   > Retrospect workflow 2
   (Use the number of the workflow you just finished)

2. Copilot will ask you **3 questions:**
   - **Did the workflow complete successfully?** (Yes / Partially / No)
   - **What is the most important thing you learned?** (One key insight)
   - **What one change would improve this workflow?** (One specific suggestion)

3. After your answers, Copilot will generate a report and ask if you want to update the workflow instructions. Type **yes** to apply the improvements.

That is it. Your feedback is captured and the workflow will be slightly better next time.

---

## Frequently Asked Questions

### Do I need to know how to code?
**No.** You interact entirely through the Copilot Chat using plain English. The technical scripts run automatically in the background.

### What if I put the wrong file in the input folder?
Copilot will show you which files it found during the Plan phase. If the wrong file is listed, tell Copilot and replace the file before approving the plan.

### Can I run multiple workflows in sequence?
Yes. Finish one workflow (wait for your final approval), then start the next one. For example, you might run Workflow 2 to generate test cases, then run Workflow 3 to review them.

### What if Copilot generates something incorrect?
During the Check phase, describe the issue clearly. Copilot will revise the specific sections you flag. You can go through as many revision rounds as needed.

### What happens to my original input documents?
They are not modified. The tool only reads from the `input/` folder and writes to the `output/` folder. Your originals remain unchanged.

### Can I customize the document styling (logo, fonts, headers)?
Yes, but this requires updating the Word template files in the `templates/document template/` folder. Ask your IT team or a technical colleague for help with template changes.

### Where are the generated documents saved?
In the `output/` folder inside the specific workflow directory. For example, Workflow 1 outputs go to `workflows/task-1-tdd-icv/output/`.

### What if my VS Code session crashes mid-workflow?
Reopen the project and type the same workflow command. Copilot will detect the previous progress and resume from where it left off.

### How do I update the tool when a new version is available?
Ask your IT team to pull the latest version from the repository. Your workflow outputs and input files will not be affected.

---

## Quick Reference Card

| What You Want to Do | What to Type in Copilot Chat |
|---|---|
| Generate Technical Design + ICV docs | `Run workflow 1` |
| Generate Test Cases | `Run workflow 2` |
| Review and revise Test Cases | `Run workflow 3` |
| Run a retrospective | `Retrospect workflow N` (replace N with workflow number) |
| Approve a plan or output | `Approved` or `Looks good` |
| Request a change | Describe the change in plain English |
| Resume an interrupted workflow | Type the same workflow command again |

---

## Getting Help

- **Something not working?** Tell Copilot what you see — it can often troubleshoot on its own.
- **Technical setup issues?** Contact your IT team or the project maintainer.
- **Workflow questions?** Check the `README.md` files inside each workflow folder for additional details.
- **Want to suggest an improvement?** Run a retrospective (Workflow 4) — your feedback gets captured and applied automatically.

---

## Summary

1. **Place** your Word files in the right `input/` folder
2. **Type** the workflow command in Copilot Chat
3. **Approve** the plan
4. **Review** the output
5. **Collect** your finished documents from the `output/` folder

That is all there is to it. The tool handles the technical complexity so you can focus on the content.

# Copilot Workflow — Onboarding Guide

You drop in Word files. Copilot turns them into polished, compliant documents. No coding required.

---

## 3 Things to Know

1. **You talk to Copilot in plain English** — inside a chat window in VS Code
2. **Copilot always asks before it acts** — you approve every step
3. **Your original files are never changed** — outputs go to a separate folder

---

## Setup (One-Time)

Ask your IT team to install: **VS Code**, **GitHub Copilot**, **Python**, and **Pandoc**.

Once that is done, open the `copilot-workflow` folder in VS Code. You are ready to go.

---

## How It Works

```
input/  -->  You type "Run workflow N"  -->  output/
 (your       in the Copilot Chat           (finished
  Word                                      Word
  files)                                    files)
```

Every workflow follows three beats:

1. **Copilot shows you a plan** — you approve or adjust
2. **Copilot generates the documents** — you wait
3. **Copilot shows you the result** — you approve or request changes

Repeat step 3 until you are happy. Done.

---

## The Workflows

| # | Name | You provide | You get | Say this |
|---|---|---|---|---|
| 1 | Tech Design + ICV | 4 design/assessment docs | Technical Design + ICV docs | `Run workflow 1` |
| 2 | Test Cases | Requirement Spec | Test Cases doc | `Run workflow 2` |
| 3 | Test Case Review | Requirement Spec + Test Cases | Review report + revised Test Cases | `Run workflow 3` |
| 4 | Retrospective | Just your answers to 3 questions | Improvement report | `Retrospect workflow N` |

---

## Your First Run (5 Minutes)

**Step 1** — Drop your `.docx` file into the right `input/` folder.

> Example: for Workflow 2, put your Requirement Spec in `workflows/task-2-test-cases/input/`

**Step 2** — Open the **Copilot Chat** panel (look for the chat icon in the VS Code sidebar). Make sure it says **Agent** mode at the top.

**Step 3** — Type `Run workflow 2` and hit Enter.

**Step 4** — Copilot shows you a plan. Read it. If it looks good, type `Approved`.

**Step 5** — Copilot generates your documents. Sit back.

**Step 6** — Copilot shows you the result. Open the file from the `output/` folder to check it.
- Happy? Type `Approved`.
- Want changes? Just say what: *"Add a test case for the login timeout requirement"*

**Step 7** — Grab your finished docs from `output/`. Send them wherever they need to go.

---

## Where Do Files Go?

```
workflows/task-N-.../
   input/       <-- put your Word files here
   output/      <-- find your finished files here
   extracted/   <-- ignore this (working files)
```

Clean out `input/` before each new run. Save important outputs elsewhere — they get overwritten next time.

---

## Talking to Copilot

**To approve:** `Approved` or `Looks good`

**To request changes:** Just describe what you want in normal language.
> *"Section 3.2 needs a test case for password reset"*
> *"The expected result on TC-005 is wrong — it should say 'error 403'"*

**To stop:** `Stop` or `Cancel`

**If something breaks:** Describe what you see. Copilot can usually fix it.

---

## Session Interrupted?

Just reopen the project and type the same command again. Copilot picks up where it left off.

---

## After You Finish: Quick Retro (3 Min)

Type `Retrospect workflow N` (replace N with the workflow number).

Copilot asks 3 questions:
1. Did it complete successfully?
2. What was the most important thing you learned?
3. What one change would improve it?

Your answers get saved and the workflow automatically improves for next time.

---

## FAQ

**Do I need to code?** No. You just chat in plain English.

**Wrong file in input?** Copilot shows what it found in the plan — fix it before you approve.

**Can I chain workflows?** Yes. Finish one, then start the next. (e.g., Workflow 2 then Workflow 3.)

**Copilot got something wrong?** Tell it what to fix. You can do as many rounds of revisions as you need.

**Need different styling/logo?** Ask IT to update the templates in `templates/document template/`.

**New version available?** Ask IT to pull the latest. Your files are not affected.

---

## Cheat Sheet

| Do this | Type this |
|---|---|
| Generate Tech Design + ICV | `Run workflow 1` |
| Generate Test Cases | `Run workflow 2` |
| Review Test Cases | `Run workflow 3` |
| Run a retrospective | `Retrospect workflow N` |
| Approve | `Approved` |
| Request changes | Describe in plain English |
| Resume after interruption | Same command again |

---

## Need Help?

- **Tool acting up?** Tell Copilot what you see — it can often self-correct.
- **Setup problems?** Contact your IT team.
- **Want to improve the workflow?** Run a retrospective — it is built in.

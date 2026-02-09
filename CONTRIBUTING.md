# Contributing to copilot-workflow

Thank you for your interest in contributing. This guide explains how to add new workflows, improve existing scripts, and maintain quality.

## Getting Started

1. Fork and clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Ensure [Pandoc](https://pandoc.org/installing.html) is installed on your system

## Adding a New Workflow

Each workflow automates the generation of specific regulated documents. To add one:

1. **Create the directory structure:**

   ```
   workflows/task-<N>-<name>/
     input/       ← .gitkeep (user drops DOCX files here)
     extracted/   ← .gitkeep (auto-generated)
     output/      ← .gitkeep (auto-generated)
   ```

2. **Create a workflow instruction file:**

   ```
   .github/instructions/workflow-<N>-<name>.instructions.md
   ```

   The instruction file must include:
   - `applyTo` frontmatter targeting the workflow directory
   - Input document descriptions
   - Output document specifications
   - Section-to-source mapping tables
   - Screenshot handling rules (if applicable)
   - Traceability requirements

3. **Test with sample data:**

   Run `python scripts/create_test_data.py` to generate sample inputs, then execute the workflow to verify your mapping rules produce correct output.

## Modifying Scripts

Scripts in `scripts/` handle document extraction and building. When modifying:

- Follow the coding standards in `.github/instructions/python-scripts.instructions.md`
- Use `pathlib.Path` for file paths
- Preserve existing CLI interfaces (positional arguments)
- Test with both the sample data and real DOCX files

## Copilot Instructions

- **Global rules** are in `.github/copilot-instructions.md` — changes here affect all workflows
- **Workflow-specific rules** are in `.github/instructions/workflow-*.instructions.md`
- **Agent definitions** are in `.github/agents/` — these define Copilot personas
- **Prompts** are in `.github/prompts/` — these are reusable task templates

When editing instructions:
- Keep language precise and unambiguous
- Include concrete examples for mapping rules
- Maintain the PDCA lifecycle — never remove approval checkpoints

## Pull Request Guidelines

- Use a descriptive title summarizing the change
- Reference any related issues
- For new workflows: include the instruction file and sample test data results
- For script changes: describe what was tested

## Code of Conduct

Be respectful and constructive. This project produces regulated documents — accuracy and traceability matter more than speed.

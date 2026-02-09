---
applyTo: "scripts/**/*.py"
description: "Python coding standards for document processing scripts in this project."
---

# Python Script Standards

## Style

- Target Python 3.8+ compatibility
- Use `pathlib.Path` for all file system operations (not `os.path`)
- Specify `encoding="utf-8"` explicitly when opening files
- Use type hints for function signatures

## Error Handling

- Validate that input files exist before processing
- Print clear error messages to stderr with the failing file path
- Exit with non-zero status on failure

## Document Processing

- Preserve the original content exactly — no modifications to text content
- Use `python-docx` for DOCX reading/writing
- Use `pypandoc` for markdown-to-DOCX conversion with reference templates
- Handle missing images gracefully (log warning, continue processing)

## Security

- Sanitize filenames derived from document content (no path traversal)
- Do not execute any content from input documents
- Validate file extensions before processing

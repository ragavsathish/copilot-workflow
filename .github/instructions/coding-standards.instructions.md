---
applyTo: "scripts/**/*.py"
---

# Python Coding Standards

## Style

- Follow PEP 8 for formatting and naming conventions.
- Use `snake_case` for functions and variables, `PascalCase` for classes.
- Use type hints for all function parameters and return values.
- Use `pathlib.Path` instead of `os.path` for file path operations.
- Use f-strings for string formatting.

## Script Structure

Every script in `scripts/` must:

1. Start with a module docstring explaining purpose, usage, and example invocation.
2. Define a `main()` function as the entry point.
3. Use `if __name__ == "__main__": main()` guard.
4. Print errors to `stderr` and exit with non-zero codes on failure.
5. Print structured output (JSON where applicable) to `stdout` for callers to parse.

## Error Handling

- Never use bare `except:` — always catch specific exceptions.
- Print user-friendly error messages that include the file path or operation that failed.
- Clean up partial outputs on failure (e.g., remove incomplete files).
- Exit with code 1 for user errors (bad input), code 2 for unexpected errors.

## Dependencies

- Keep dependencies minimal — do not add packages without updating `requirements.txt`.
- Use optional imports with fallback for non-critical libraries (see `image_b64.py` Pillow pattern).
- Standard library modules are preferred over third-party when functionality is equivalent.

## File I/O

- Always specify `encoding="utf-8"` when reading/writing text files.
- Use `Path.mkdir(parents=True, exist_ok=True)` for directory creation.
- Use chunked reading for large files (see `image_b64.py` pattern).

## Testing

- Scripts should be testable: put logic in functions, not at module level.
- Test data generators live in `scripts/simulate/`.

"""
build_docx.py — Builds styled DOCX from markdown using pypandoc.

Usage:
    python scripts/build_docx.py <workflow_dir>

Example:
    python scripts/build_docx.py workflows/task-1-tdd-icv

Pandoc uses:
- --reference-doc: Your Word template for styling (fonts, logo, headers/footers)
- YAML frontmatter in markdown: Template variables (title, author, date, version, etc.)

Markdown files in output/ should start with a YAML header like:
---
title: "Technical Design Document"
author: "Team Name"
date: "2026-02-09"
version: "1.0"
---
"""

import sys
from pathlib import Path

import pypandoc


def find_template(template_dir, output_stem):
    """Find the best matching .docx template for an output file."""
    template_dir = Path(template_dir)
    if not template_dir.exists():
        return None

    templates = list(template_dir.glob("*.docx"))

    # Exact match
    for t in templates:
        if t.stem.lower().replace(" ", "_") == output_stem.lower().replace(" ", "_"):
            return t

    # Partial match
    for t in templates:
        if t.stem.lower() in output_stem.lower() or output_stem.lower() in t.stem.lower():
            return t

    # Fallback to first template
    return templates[0] if templates else None


def build_docx(md_path, template_path, output_path, extracted_dir):
    """Convert markdown to styled DOCX using pypandoc."""
    extra_args = [
        "--resource-path", str(extracted_dir),
        "--standalone",
    ]

    if template_path and template_path.exists():
        extra_args.extend(["--reference-doc", str(template_path)])
        print(f"    Template: {template_path.name}")

    pypandoc.convert_file(
        str(md_path),
        "docx",
        outputfile=str(output_path),
        extra_args=extra_args,
    )
    print(f"    → {output_path}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/build_docx.py <workflow_dir>")
        sys.exit(1)

    wf = Path(sys.argv[1])
    output_dir = wf / "output"
    extracted_dir = wf / "extracted"
    template_dir = Path("templates") / "document template"

    md_files = sorted(output_dir.glob("*.md"))
    if not md_files:
        print(f"Error: No .md files in {output_dir}")
        sys.exit(1)

    print(f"Building {len(md_files)} document(s)")

    for md in md_files:
        print(f"  {md.name}")
        template = find_template(template_dir, md.stem)
        build_docx(md, template, output_dir / f"{md.stem}.docx", extracted_dir)

    print("\nDone.")


if __name__ == "__main__":
    main()

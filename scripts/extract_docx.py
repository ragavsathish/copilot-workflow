"""
extract_docx.py — Extracts DOCX files into markdown text + images.

Usage:
    python scripts/extract_docx.py <workflow_dir>

Example:
    python scripts/extract_docx.py workflows/task-1-tdd-icv
"""

import sys
import os
import re
from pathlib import Path

from docx import Document


def slugify(text):
    """Convert text to a safe filename."""
    text = re.sub(r'[^\w\s-]', '', text.lower().strip())
    return re.sub(r'[\s_]+', '_', text)


def extract_images(doc, image_dir, prefix):
    """Extract all embedded images from a DOCX."""
    image_dir.mkdir(parents=True, exist_ok=True)
    count = 0
    for rel in doc.part.rels.values():
        if "image" in rel.reltype:
            count += 1
            ext = os.path.splitext(rel.target_part.partname)[1] or ".png"
            with open(image_dir / f"{prefix}_img_{count:03d}{ext}", "wb") as f:
                f.write(rel.target_part.blob)
    return count


def table_to_markdown(table):
    """Convert a DOCX table to markdown."""
    rows = [[c.text.strip().replace('\n', ' ') for c in row.cells] for row in table.rows]
    if not rows:
        return ""
    lines = ["| " + " | ".join(rows[0]) + " |"]
    lines.append("| " + " | ".join(["---"] * len(rows[0])) + " |")
    for row in rows[1:]:
        row += [""] * (len(rows[0]) - len(row))  # pad short rows
        lines.append("| " + " | ".join(row) + " |")
    return "\n".join(lines)


def extract_docx(docx_path, output_md, image_dir, prefix):
    """Extract a DOCX file to markdown + images."""
    doc = Document(str(docx_path))
    lines = []
    table_idx = 0

    for element in doc.element.body:
        tag = element.tag.split('}')[-1]

        if tag == 'p':
            from docx.text.paragraph import Paragraph
            para = Paragraph(element, doc)
            style = para.style.name if para.style else ""
            text = para.text.strip()

            if not text:
                lines.append("")
            elif "Heading 1" in style or style == "Title":
                lines.append(f"# {text}")
            elif "Heading 2" in style:
                lines.append(f"## {text}")
            elif "Heading 3" in style:
                lines.append(f"### {text}")
            elif "Heading 4" in style:
                lines.append(f"#### {text}")
            elif "List" in style or "Bullet" in style:
                lines.append(f"- {text}")
            elif "Number" in style:
                lines.append(f"1. {text}")
            else:
                lines.append(text)

        elif tag == 'tbl' and table_idx < len(doc.tables):
            lines.extend(["", table_to_markdown(doc.tables[table_idx]), ""])
            table_idx += 1

    img_count = extract_images(doc, image_dir, prefix)

    output_md.parent.mkdir(parents=True, exist_ok=True)
    output_md.write_text("\n".join(lines), encoding="utf-8")
    return len(lines), img_count


def extract_template_structure(docx_path, output_md):
    """Extract headings-only structure from a template DOCX."""
    doc = Document(str(docx_path))
    heading_map = {"Heading 1": "#", "Title": "#", "Heading 2": "##",
                   "Heading 3": "###", "Heading 4": "####"}
    lines = []
    for para in doc.paragraphs:
        style = para.style.name if para.style else ""
        text = para.text.strip()
        if not text:
            continue
        prefix = next((v for k, v in heading_map.items() if k in style), None)
        if prefix:
            lines.append(f"{prefix} {text}")
        else:
            lines.append(f"<!-- placeholder: {text[:100]} -->")

    output_md.parent.mkdir(parents=True, exist_ok=True)
    output_md.write_text("\n".join(lines), encoding="utf-8")
    return len(lines)


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/extract_docx.py <workflow_dir>")
        sys.exit(1)

    wf = Path(sys.argv[1])
    input_dir = wf / "input"
    extracted = wf / "extracted"
    image_dir = extracted / "images"
    template_src = Path("templates") / "document template"

    if not input_dir.exists():
        print(f"Error: {input_dir} not found")
        sys.exit(1)

    # Extract input documents
    for docx in sorted(input_dir.glob("*.docx")):
        prefix = slugify(docx.stem)
        print(f"  Extracting: {docx.name}")
        lines, imgs = extract_docx(docx, extracted / f"{prefix}.md", image_dir, prefix)
        print(f"    → {lines} lines, {imgs} images")

    # Extract template structures
    if template_src.exists():
        for docx in sorted(template_src.glob("*.docx")):
            prefix = slugify(docx.stem)
            print(f"  Template: {docx.name}")
            n = extract_template_structure(docx, extracted / "templates" / f"{prefix}_structure.md")
            print(f"    → {n} elements")

    print("\nDone.")


if __name__ == "__main__":
    main()

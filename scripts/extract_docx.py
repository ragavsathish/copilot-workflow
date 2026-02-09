"""
extract_docx.py — Extracts DOCX files into markdown text + images.

Usage:
    python scripts/extract_docx.py <workflow_dir>

Example:
    python scripts/extract_docx.py workflows/task-1-tdd-icv

This script:
1. Reads all .docx files from <workflow_dir>/input/
2. Extracts text (headings, paragraphs, tables) → markdown files in <workflow_dir>/extracted/
3. Extracts embedded images → PNG files in <workflow_dir>/extracted/images/
4. Reads template .docx files from templates/document template/
5. Extracts template structure (headings only) → <workflow_dir>/extracted/templates/
"""

import sys
import os
import re
from pathlib import Path

from docx import Document
from docx.opc.constants import RELATIONSHIP_TYPE as RT


def slugify(text):
    """Convert text to a safe filename."""
    text = text.lower().strip()
    text = re.sub(r'[^\w\s-]', '', text)
    text = re.sub(r'[\s_]+', '_', text)
    return text


def extract_table_to_markdown(table):
    """Convert a DOCX table to markdown format."""
    rows = []
    for row in table.rows:
        cells = [cell.text.strip().replace('\n', ' ') for cell in row.cells]
        rows.append(cells)

    if not rows:
        return ""

    lines = []
    # Header row
    lines.append("| " + " | ".join(rows[0]) + " |")
    # Separator
    lines.append("| " + " | ".join(["---"] * len(rows[0])) + " |")
    # Data rows
    for row in rows[1:]:
        # Pad row if it has fewer cells than header
        while len(row) < len(rows[0]):
            row.append("")
        lines.append("| " + " | ".join(row) + " |")

    return "\n".join(lines)


def extract_images(doc, image_dir, prefix):
    """Extract all images from a DOCX document."""
    image_dir = Path(image_dir)
    image_dir.mkdir(parents=True, exist_ok=True)

    image_count = 0
    for rel in doc.part.rels.values():
        if "image" in rel.reltype:
            image_count += 1
            image_data = rel.target_part.blob
            ext = os.path.splitext(rel.target_part.partname)[1] or ".png"
            image_filename = f"{prefix}_img_{image_count:03d}{ext}"
            image_path = image_dir / image_filename
            with open(image_path, "wb") as f:
                f.write(image_data)

    return image_count


def extract_docx_to_markdown(docx_path, output_path, image_dir, prefix):
    """Extract a DOCX file to markdown."""
    doc = Document(docx_path)
    lines = []
    table_index = 0
    tables = doc.tables

    # Track which paragraphs are inside tables to avoid duplication
    table_elements = set()
    for table in tables:
        table_elements.add(table._element)

    for element in doc.element.body:
        tag = element.tag.split('}')[-1] if '}' in element.tag else element.tag

        if tag == 'p':
            # It's a paragraph
            from docx.text.paragraph import Paragraph
            para = Paragraph(element, doc)
            style_name = para.style.name if para.style else ""

            text = para.text.strip()
            if not text:
                lines.append("")
                continue

            # Map heading styles to markdown
            if "Heading 1" in style_name or style_name == "Title":
                lines.append(f"# {text}")
            elif "Heading 2" in style_name:
                lines.append(f"## {text}")
            elif "Heading 3" in style_name:
                lines.append(f"### {text}")
            elif "Heading 4" in style_name:
                lines.append(f"#### {text}")
            elif "List" in style_name or "Bullet" in style_name:
                lines.append(f"- {text}")
            elif "Number" in style_name:
                lines.append(f"1. {text}")
            else:
                lines.append(text)

            # Check for inline images in this paragraph
            for run in para.runs:
                drawing_elements = run._element.findall(
                    './/{http://schemas.openxmlformats.org/wordprocessingml/2006/main}drawing'
                ) or run._element.findall(
                    './/{http://schemas.openxmlformats.org/drawingml/2006/main}blip'
                )
                if drawing_elements:
                    lines.append(f"\n![image](images/{prefix}_img_see_extracted_images.png)\n")

        elif tag == 'tbl':
            # It's a table
            if table_index < len(tables):
                md_table = extract_table_to_markdown(tables[table_index])
                lines.append("")
                lines.append(md_table)
                lines.append("")
                table_index += 1

    # Extract images
    image_count = extract_images(doc, image_dir, prefix)

    # Write markdown
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    return len(lines), image_count


def extract_template_structure(docx_path, output_path):
    """Extract only headings and structure from a template DOCX."""
    doc = Document(docx_path)
    lines = []

    for para in doc.paragraphs:
        style_name = para.style.name if para.style else ""
        text = para.text.strip()
        if not text:
            continue

        if "Heading 1" in style_name or style_name == "Title":
            lines.append(f"# {text}")
        elif "Heading 2" in style_name:
            lines.append(f"## {text}")
        elif "Heading 3" in style_name:
            lines.append(f"### {text}")
        elif "Heading 4" in style_name:
            lines.append(f"#### {text}")
        elif "Heading" in style_name:
            lines.append(f"##### {text}")
        else:
            # Include non-heading text as placeholder hints
            lines.append(f"<!-- placeholder: {text[:100]} -->")

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    return len(lines)


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/extract_docx.py <workflow_dir>")
        print("Example: python scripts/extract_docx.py workflows/task-1-tdd-icv")
        sys.exit(1)

    workflow_dir = Path(sys.argv[1])
    input_dir = workflow_dir / "input"
    extracted_dir = workflow_dir / "extracted"
    image_dir = extracted_dir / "images"
    template_extract_dir = extracted_dir / "templates"
    template_source_dir = Path("templates") / "document template"

    if not input_dir.exists():
        print(f"Error: Input directory not found: {input_dir}")
        sys.exit(1)

    # Extract input DOCX files
    input_files = list(input_dir.glob("*.docx"))
    if not input_files:
        print(f"Warning: No .docx files found in {input_dir}")
    else:
        print(f"Found {len(input_files)} input DOCX file(s)")

    for docx_file in input_files:
        prefix = slugify(docx_file.stem)
        output_file = extracted_dir / f"{prefix}.md"
        print(f"  Extracting: {docx_file.name}")

        line_count, img_count = extract_docx_to_markdown(
            str(docx_file), str(output_file), str(image_dir), prefix
        )
        print(f"    → {output_file} ({line_count} lines, {img_count} images)")

    # Extract template DOCX structure
    if template_source_dir.exists():
        template_files = list(template_source_dir.glob("*.docx"))
        if template_files:
            print(f"\nFound {len(template_files)} template DOCX file(s)")
        for docx_file in template_files:
            prefix = slugify(docx_file.stem)
            output_file = template_extract_dir / f"{prefix}_structure.md"
            print(f"  Extracting template structure: {docx_file.name}")

            heading_count = extract_template_structure(
                str(docx_file), str(output_file)
            )
            print(f"    → {output_file} ({heading_count} elements)")
    else:
        print(f"\nWarning: Template directory not found: {template_source_dir}")

    print("\nExtraction complete.")


if __name__ == "__main__":
    main()

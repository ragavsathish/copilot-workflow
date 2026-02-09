"""
build_docx.py — Builds styled DOCX files from markdown output + template.

Usage:
    python scripts/build_docx.py <workflow_dir>

Example:
    python scripts/build_docx.py workflows/task-1-tdd-icv

This script:
1. Reads markdown files from <workflow_dir>/output/
2. Reads the matching template DOCX from templates/document template/
3. Fills the template with content from the markdown
4. Embeds referenced images
5. Produces final styled DOCX files in <workflow_dir>/output/
"""

import sys
import re
from pathlib import Path

from docx import Document
from docx.shared import Inches, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH


def find_template(template_dir, output_stem):
    """Find the best matching template for an output file."""
    template_dir = Path(template_dir)
    if not template_dir.exists():
        return None

    templates = list(template_dir.glob("*.docx"))

    # Try exact stem match first
    for t in templates:
        if t.stem.lower().replace(" ", "_") == output_stem.lower().replace(" ", "_"):
            return t

    # Try partial match
    for t in templates:
        t_lower = t.stem.lower()
        out_lower = output_stem.lower()
        if t_lower in out_lower or out_lower in t_lower:
            return t

    # Return first template as fallback
    return templates[0] if templates else None


def parse_markdown(md_path):
    """Parse a markdown file into structured elements."""
    elements = []
    with open(md_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    i = 0
    while i < len(lines):
        line = lines[i].rstrip("\n")

        # Headings
        if line.startswith("##### "):
            elements.append({"type": "heading", "level": 5, "text": line[6:]})
        elif line.startswith("#### "):
            elements.append({"type": "heading", "level": 4, "text": line[5:]})
        elif line.startswith("### "):
            elements.append({"type": "heading", "level": 3, "text": line[4:]})
        elif line.startswith("## "):
            elements.append({"type": "heading", "level": 2, "text": line[3:]})
        elif line.startswith("# "):
            elements.append({"type": "heading", "level": 1, "text": line[2:]})

        # Images
        elif re.match(r'!\[.*?\]\((.+?)\)', line):
            match = re.match(r'!\[(.*?)\]\((.+?)\)', line)
            elements.append({
                "type": "image",
                "alt": match.group(1),
                "path": match.group(2)
            })

        # Table rows
        elif line.startswith("|"):
            table_lines = []
            while i < len(lines) and lines[i].strip().startswith("|"):
                table_lines.append(lines[i].strip())
                i += 1
            i -= 1  # back up one since the outer loop will increment
            elements.append({"type": "table", "lines": table_lines})

        # Bullet list
        elif line.startswith("- ") or line.startswith("* "):
            elements.append({"type": "bullet", "text": line[2:]})

        # Numbered list
        elif re.match(r'^\d+\.\s', line):
            text = re.sub(r'^\d+\.\s', '', line)
            elements.append({"type": "numbered", "text": text})

        # Empty line
        elif not line.strip():
            pass

        # Regular paragraph
        else:
            elements.append({"type": "paragraph", "text": line})

        i += 1

    return elements


def parse_table_lines(table_lines):
    """Parse markdown table lines into rows of cells."""
    rows = []
    for line in table_lines:
        line = line.strip().strip("|")
        cells = [c.strip() for c in line.split("|")]
        # Skip separator rows (---)
        if all(re.match(r'^[-:]+$', c) for c in cells if c):
            continue
        rows.append(cells)
    return rows


def build_docx_from_markdown(md_path, template_path, output_path, image_base_dir):
    """Build a DOCX from markdown using a template for styling."""

    # Use template if available, otherwise create blank doc
    if template_path and template_path.exists():
        doc = Document(str(template_path))
        # Clear existing content from template body
        for element in doc.element.body[:]:
            # Keep section properties (page layout, headers/footers)
            tag = element.tag.split('}')[-1] if '}' in element.tag else element.tag
            if tag != 'sectPr':
                doc.element.body.remove(element)
        print(f"    Using template: {template_path.name}")
    else:
        doc = Document()
        print(f"    No template found, using default styling")

    elements = parse_markdown(md_path)

    for elem in elements:
        if elem["type"] == "heading":
            level = min(elem["level"], 4)  # DOCX supports Heading 1-4 natively
            doc.add_heading(elem["text"], level=level)

        elif elem["type"] == "paragraph":
            doc.add_paragraph(elem["text"])

        elif elem["type"] == "bullet":
            doc.add_paragraph(elem["text"], style="List Bullet")

        elif elem["type"] == "numbered":
            doc.add_paragraph(elem["text"], style="List Number")

        elif elem["type"] == "image":
            image_path = Path(image_base_dir) / elem["path"]
            if not image_path.exists():
                # Try relative to the markdown file
                image_path = md_path.parent / elem["path"]
            if image_path.exists():
                doc.add_picture(str(image_path), width=Inches(5.5))
                if elem["alt"]:
                    caption = doc.add_paragraph(elem["alt"])
                    caption.alignment = WD_ALIGN_PARAGRAPH.CENTER
                    caption.style = doc.styles.get("Caption", caption.style)
            else:
                doc.add_paragraph(f"[Image not found: {elem['path']}]")

        elif elem["type"] == "table":
            rows = parse_table_lines(elem["lines"])
            if rows:
                num_cols = max(len(r) for r in rows)
                table = doc.add_table(rows=len(rows), cols=num_cols)
                table.style = "Table Grid"
                for r_idx, row in enumerate(rows):
                    for c_idx, cell_text in enumerate(row):
                        if c_idx < num_cols:
                            table.rows[r_idx].cells[c_idx].text = cell_text

    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    doc.save(str(output_path))
    print(f"    → {output_path}")


def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/build_docx.py <workflow_dir>")
        print("Example: python scripts/build_docx.py workflows/task-1-tdd-icv")
        sys.exit(1)

    workflow_dir = Path(sys.argv[1])
    output_dir = workflow_dir / "output"
    image_dir = workflow_dir / "extracted" / "images"
    template_dir = Path("templates") / "document template"

    # Find markdown files in output dir
    md_files = list(output_dir.glob("*.md"))
    if not md_files:
        print(f"Error: No markdown files found in {output_dir}")
        print("Copilot should generate output .md files before running this script.")
        sys.exit(1)

    print(f"Found {len(md_files)} output markdown file(s)")

    for md_file in md_files:
        print(f"  Building: {md_file.name}")
        docx_output = output_dir / f"{md_file.stem}.docx"

        # Find matching template
        template_path = find_template(template_dir, md_file.stem)

        build_docx_from_markdown(
            md_path=md_file,
            template_path=template_path,
            output_path=docx_output,
            image_base_dir=str(workflow_dir / "extracted")
        )

    print("\nBuild complete.")


if __name__ == "__main__":
    main()

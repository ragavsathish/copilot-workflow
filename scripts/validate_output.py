"""Validate generated markdown output files for common errors.

Checks YAML frontmatter, traceability comments, image references,
table formatting, and test case structure. Reports issues to stderr
and exits with code 1 if any errors are found.

Usage:
    python scripts/validate_output.py <output_dir>

Example:
    python scripts/validate_output.py workflows/task-1-tdd-icv/output/
    python scripts/validate_output.py workflows/task-2-test-cases/output/
"""

import json
import re
import sys
from pathlib import Path


def check_yaml_frontmatter(content: str, filepath: Path) -> list[str]:
    """Check that YAML frontmatter is present and has required fields."""
    issues = []
    if not content.startswith("---"):
        issues.append(f"{filepath.name}: Missing YAML frontmatter (must start with ---)")
        return issues

    end_match = re.search(r"\n---\s*\n", content[3:])
    if not end_match:
        issues.append(f"{filepath.name}: YAML frontmatter not closed (missing ending ---)")
        return issues

    frontmatter = content[3 : 3 + end_match.start()]
    required_fields = ["title", "date", "version", "status"]
    for field in required_fields:
        if not re.search(rf"^{field}\s*:", frontmatter, re.MULTILINE):
            issues.append(f"{filepath.name}: Missing required frontmatter field: {field}")

    return issues


def check_traceability(content: str, filepath: Path) -> list[str]:
    """Check for traceability comments in sections."""
    issues = []
    headings = re.findall(r"^(#{1,3})\s+(.+)$", content, re.MULTILINE)
    source_comments = re.findall(r"<!--\s*Source:.*?-->", content)

    if headings and not source_comments:
        issues.append(
            f"{filepath.name}: No traceability comments found "
            f"(expected <!-- Source: ... --> before sections)"
        )
    elif len(headings) > 2 and len(source_comments) < len(headings) // 2:
        issues.append(
            f"{filepath.name}: Low traceability coverage — "
            f"{len(source_comments)} comments for {len(headings)} sections"
        )

    return issues


def check_image_references(content: str, filepath: Path, output_dir: Path) -> list[str]:
    """Check that referenced images exist."""
    issues = []
    image_refs = re.findall(r"!\[([^\]]*)\]\(([^)]+)\)", content)
    for alt_text, img_path in image_refs:
        resolved = output_dir / img_path
        if not resolved.exists():
            parent_dir = output_dir.parent
            resolved_parent = parent_dir / img_path
            if not resolved_parent.exists():
                extracted_path = parent_dir / "extracted" / img_path
                if not extracted_path.exists():
                    issues.append(
                        f"{filepath.name}: Image not found: {img_path}"
                    )

    return issues


def check_empty_sections(content: str, filepath: Path) -> list[str]:
    """Check for empty sections (heading followed immediately by another heading)."""
    issues = []
    lines = content.split("\n")
    for i, line in enumerate(lines):
        if re.match(r"^#{1,3}\s+", line):
            remaining = "\n".join(lines[i + 1 :]).lstrip()
            if remaining and re.match(r"^#{1,3}\s+", remaining.split("\n")[0]):
                section_title = line.strip().lstrip("#").strip()
                issues.append(f"{filepath.name}: Empty section: {section_title}")

    return issues


def check_test_case_format(content: str, filepath: Path) -> list[str]:
    """Check test case format (KISS rules) for workflow-2 output."""
    issues = []
    if "TC-" not in content:
        return issues

    tc_blocks = re.findall(r"###\s+(TC-\d+):\s*(.+)", content)
    if not tc_blocks:
        return issues

    for tc_id, title in tc_blocks:
        tc_section_match = re.search(
            rf"###\s+{re.escape(tc_id)}:.*?(?=\n###\s+TC-|\n##\s+|\Z)",
            content,
            re.DOTALL,
        )
        if not tc_section_match:
            continue

        tc_content = tc_section_match.group()

        if "**Requirement:**" not in tc_content:
            issues.append(f"{filepath.name}: {tc_id} missing **Requirement:** field")
        if "**Priority:**" not in tc_content:
            issues.append(f"{filepath.name}: {tc_id} missing **Priority:** field")
        if "**Test Steps:**" not in tc_content and "| Step |" not in tc_content:
            issues.append(f"{filepath.name}: {tc_id} missing test steps table")

    tc_ids = [tc_id for tc_id, _ in tc_blocks]
    for i in range(len(tc_ids) - 1):
        current_num = int(re.search(r"\d+", tc_ids[i]).group())
        next_num = int(re.search(r"\d+", tc_ids[i + 1]).group())
        if next_num != current_num + 1:
            issues.append(
                f"{filepath.name}: Non-sequential test case IDs: "
                f"{tc_ids[i]} → {tc_ids[i+1]}"
            )

    return issues


def check_table_format(content: str, filepath: Path) -> list[str]:
    """Check for malformed markdown tables."""
    issues = []
    lines = content.split("\n")
    in_table = False
    table_cols = 0

    for i, line in enumerate(lines, 1):
        if "|" in line and line.strip().startswith("|"):
            cols = len(line.strip().split("|")) - 2
            if not in_table:
                in_table = True
                table_cols = cols
            elif cols != table_cols and line.strip().replace("|", "").replace("-", "").strip():
                issues.append(
                    f"{filepath.name}:{i}: Table column mismatch "
                    f"(expected {table_cols}, got {cols})"
                )
        else:
            in_table = False
            table_cols = 0

    return issues


def validate_directory(output_dir: Path) -> list[str]:
    """Validate all markdown files in the output directory."""
    all_issues = []
    md_files = sorted(output_dir.glob("*.md"))

    if not md_files:
        all_issues.append(f"No .md files found in {output_dir}")
        return all_issues

    for md_file in md_files:
        content = md_file.read_text(encoding="utf-8")
        all_issues.extend(check_yaml_frontmatter(content, md_file))
        all_issues.extend(check_traceability(content, md_file))
        all_issues.extend(check_image_references(content, md_file, output_dir))
        all_issues.extend(check_empty_sections(content, md_file))
        all_issues.extend(check_test_case_format(content, md_file))
        all_issues.extend(check_table_format(content, md_file))

    return all_issues


def main() -> None:
    if len(sys.argv) != 2:
        print("Usage: python scripts/validate_output.py <output_dir>", file=sys.stderr)
        sys.exit(1)

    output_dir = Path(sys.argv[1])
    if not output_dir.is_dir():
        print(f"Error: {output_dir} is not a directory", file=sys.stderr)
        sys.exit(1)

    issues = validate_directory(output_dir)

    result = {
        "directory": str(output_dir),
        "files_checked": len(list(output_dir.glob("*.md"))),
        "issues_found": len(issues),
        "issues": issues,
        "status": "PASS" if not issues else "FAIL",
    }

    print(json.dumps(result, indent=2))

    if issues:
        print(f"\n{len(issues)} issue(s) found:", file=sys.stderr)
        for issue in issues:
            print(f"  - {issue}", file=sys.stderr)
        sys.exit(1)
    else:
        print("\nAll checks passed.", file=sys.stderr)


if __name__ == "__main__":
    main()

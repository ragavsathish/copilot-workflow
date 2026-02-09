"""Create sample requirement specification DOCX for Workflow 2 testing."""

from docx import Document
from docx.shared import Pt
from pathlib import Path


def create_requirement_spec():
    """Create a comprehensive requirement specification document."""
    doc = Document()
    doc.add_heading("Requirement Specification", 0)

    # Document metadata
    doc.add_heading("Document Information", level=1)
    table = doc.add_table(rows=6, cols=2)
    table.style = "Table Grid"
    metadata = [
        ["Project Name", "ACME Inventory Management System (IMS)"],
        ["Version", "2.5.0"],
        ["Date", "2026-02-09"],
        ["Document ID", "REQ-SPEC-IMS-001"],
        ["Author", "Product Team"],
        ["Status", "Approved"],
    ]
    for r, (key, val) in enumerate(metadata):
        table.rows[r].cells[0].text = key
        table.rows[r].cells[1].text = val

    doc.add_heading("1. Purpose", level=1)
    doc.add_paragraph(
        "This document specifies the functional and non-functional requirements for the "
        "ACME Inventory Management System v2.5. The system provides real-time inventory "
        "tracking, automated reorder management, and compliance reporting for GxP-regulated "
        "warehouse operations."
    )

    doc.add_heading("2. Scope", level=1)
    doc.add_heading("2.1 In Scope", level=2)
    doc.add_paragraph("- User authentication and authorization")
    doc.add_paragraph("- Inventory intake and dispatch")
    doc.add_paragraph("- Storage location tracking")
    doc.add_paragraph("- Audit trail and compliance reporting")
    doc.add_paragraph("- Integration with SAP ERP and Veeva Vault QMS")

    doc.add_heading("2.2 Out of Scope", level=2)
    doc.add_paragraph("- Manufacturing execution system (MES) functions")
    doc.add_paragraph("- Supplier management")
    doc.add_paragraph("- Financial accounting")

    doc.add_heading("3. Functional Requirements", level=1)

    # Authentication Requirements
    doc.add_heading("3.1 User Authentication", level=2)

    doc.add_heading("REQ-001: Single Sign-On Login", level=3)
    doc.add_paragraph(
        "The system shall support Azure AD single sign-on (SSO) using SAML 2.0 protocol. "
        "Users shall be redirected to the Azure AD login page and returned to the application "
        "upon successful authentication."
    )
    doc.add_paragraph("**Priority**: High")
    doc.add_paragraph("**Acceptance Criteria**:")
    doc.add_paragraph(
        '- User clicks "Login" button → redirected to Azure AD', style="List Bullet"
    )
    doc.add_paragraph(
        "- Successful authentication → returned to dashboard", style="List Bullet"
    )
    doc.add_paragraph(
        "- Session cookie created with 8-hour expiration", style="List Bullet"
    )
    doc.add_paragraph(
        "- Failed authentication → error message displayed", style="List Bullet"
    )

    doc.add_heading("REQ-002: Session Timeout", level=3)
    doc.add_paragraph(
        "The system shall automatically log out users after 8 hours of inactivity. "
        "A warning message shall be displayed 5 minutes before timeout."
    )
    doc.add_paragraph("**Priority**: High")
    doc.add_paragraph("**Acceptance Criteria**:")
    doc.add_paragraph(
        "- No activity for 7h 55m → warning modal displayed", style="List Bullet"
    )
    doc.add_paragraph(
        "- No activity for 8h → session terminated, user redirected to login",
        style="List Bullet",
    )
    doc.add_paragraph(
        '- User clicks "Stay Logged In" → session extended for 8h', style="List Bullet"
    )

    doc.add_heading("REQ-003: Role-Based Access Control", level=3)
    doc.add_paragraph(
        "The system shall enforce role-based access control (RBAC) with four roles: "
        "Admin, Manager, Operator, and Viewer. Each role shall have specific permissions."
    )
    doc.add_paragraph("**Priority**: High")
    doc.add_paragraph("**Acceptance Criteria**:")
    doc.add_paragraph("- Admin: Full access to all functions", style="List Bullet")
    doc.add_paragraph(
        "- Manager: Read/write inventory, read-only users and config",
        style="List Bullet",
    )
    doc.add_paragraph(
        "- Operator: Read/write inventory, no admin functions", style="List Bullet"
    )
    doc.add_paragraph(
        "- Viewer: Read-only access to inventory and reports", style="List Bullet"
    )
    doc.add_paragraph(
        "- Unauthorized access attempt → HTTP 403 error", style="List Bullet"
    )

    # Inventory Management Requirements
    doc.add_heading("3.2 Inventory Management", level=2)

    doc.add_heading("REQ-004: Add Inventory Item", level=3)
    doc.add_paragraph(
        "Users with Operator or Manager role shall be able to add new inventory items. "
        "Each item must have: SKU, name, quantity, unit of measure, storage location, "
        "expiration date (if applicable), and batch number."
    )
    doc.add_paragraph("**Priority**: High")
    doc.add_paragraph("**Acceptance Criteria**:")
    doc.add_paragraph(
        "- All required fields provided → item saved to database", style="List Bullet"
    )
    doc.add_paragraph(
        "- Success notification displayed with item ID", style="List Bullet"
    )
    doc.add_paragraph(
        "- Audit trail entry created with user ID and timestamp", style="List Bullet"
    )
    doc.add_paragraph(
        "- Missing required field → validation error displayed", style="List Bullet"
    )
    doc.add_paragraph("- Duplicate SKU → error message displayed", style="List Bullet")

    doc.add_heading("REQ-005: Update Inventory Quantity", level=3)
    doc.add_paragraph(
        "Users shall be able to update inventory quantities. The system shall track the "
        "previous quantity, new quantity, reason for change, and user who made the change."
    )
    doc.add_paragraph("**Priority**: High")
    doc.add_paragraph("**Acceptance Criteria**:")
    doc.add_paragraph(
        "- Valid quantity and reason → quantity updated in database",
        style="List Bullet",
    )
    doc.add_paragraph(
        "- Previous value, new value, reason, user ID, and timestamp logged",
        style="List Bullet",
    )
    doc.add_paragraph(
        "- Negative quantity entered → validation error", style="List Bullet"
    )
    doc.add_paragraph(
        "- Quantity exceeds maximum (1,000,000) → validation error", style="List Bullet"
    )

    doc.add_heading("REQ-006: Search Inventory", level=3)
    doc.add_paragraph(
        "Users shall be able to search inventory by SKU, name, storage location, or batch number. "
        "Search results shall be displayed in a sortable table with pagination."
    )
    doc.add_paragraph("**Priority**: Medium")
    doc.add_paragraph("**Acceptance Criteria**:")
    doc.add_paragraph(
        "- Search query entered → matching results displayed within 2 seconds",
        style="List Bullet",
    )
    doc.add_paragraph(
        '- No matches found → "No results" message displayed', style="List Bullet"
    )
    doc.add_paragraph("- Results sortable by any column", style="List Bullet")
    doc.add_paragraph("- Pagination: 50 items per page", style="List Bullet")

    doc.add_heading("REQ-007: Delete Inventory Item", level=3)
    doc.add_paragraph(
        "Only users with Admin or Manager role shall be able to delete inventory items. "
        "Deletion requires a reason and confirmation. Deleted items are soft-deleted (marked inactive)."
    )
    doc.add_paragraph("**Priority**: Medium")
    doc.add_paragraph("**Acceptance Criteria**:")
    doc.add_paragraph(
        "- Confirmation dialog displayed with reason field", style="List Bullet"
    )
    doc.add_paragraph(
        "- User confirms → item marked inactive, audit entry created",
        style="List Bullet",
    )
    doc.add_paragraph("- User cancels → no changes made", style="List Bullet")
    doc.add_paragraph(
        "- Viewer or Operator attempts deletion → HTTP 403 error", style="List Bullet"
    )

    # Reporting Requirements
    doc.add_heading("3.3 Reporting and Audit Trail", level=2)

    doc.add_heading("REQ-008: Audit Trail Report", level=3)
    doc.add_paragraph(
        "The system shall provide an audit trail report showing all inventory changes. "
        "Report shall include: timestamp, user ID, action type, item SKU, old value, "
        "new value, and reason."
    )
    doc.add_paragraph("**Priority**: High")
    doc.add_paragraph("**Acceptance Criteria**:")
    doc.add_paragraph("- Report displays all audit entries", style="List Bullet")
    doc.add_paragraph(
        "- Filterable by date range, user, action type, and SKU", style="List Bullet"
    )
    doc.add_paragraph("- Exportable to CSV and PDF formats", style="List Bullet")
    doc.add_paragraph(
        "- Audit entries immutable (cannot be edited or deleted)", style="List Bullet"
    )

    doc.add_heading("REQ-009: Inventory Summary Report", level=3)
    doc.add_paragraph(
        "Users shall be able to generate an inventory summary report showing current stock levels "
        "by storage location, category, or expiration date range."
    )
    doc.add_paragraph("**Priority**: Medium")
    doc.add_paragraph("**Acceptance Criteria**:")
    doc.add_paragraph(
        "- User selects grouping criteria → report generated", style="List Bullet"
    )
    doc.add_paragraph(
        "- Report includes total quantity and item count per group", style="List Bullet"
    )
    doc.add_paragraph("- Exportable to Excel and PDF", style="List Bullet")

    # Integration Requirements
    doc.add_heading("3.4 System Integration", level=2)

    doc.add_heading("REQ-010: SAP ERP Integration", level=3)
    doc.add_paragraph(
        "The system shall synchronize inventory data with SAP S/4HANA every 15 minutes. "
        "When inventory quantity changes, an RFC call shall be made to update SAP."
    )
    doc.add_paragraph("**Priority**: High")
    doc.add_paragraph("**Acceptance Criteria**:")
    doc.add_paragraph(
        "- Inventory change → SAP RFC call triggered within 15 minutes",
        style="List Bullet",
    )
    doc.add_paragraph("- Successful sync → timestamp recorded", style="List Bullet")
    doc.add_paragraph(
        "- Failed sync → error logged and retry attempted (max 3 retries)",
        style="List Bullet",
    )
    doc.add_paragraph(
        "- SAP unavailable → alert sent to Admin users", style="List Bullet"
    )

    # Non-Functional Requirements
    doc.add_heading("4. Non-Functional Requirements", level=1)

    doc.add_heading("REQ-011: Response Time", level=3)
    doc.add_paragraph(
        "The system shall respond to user actions within 2 seconds under normal load "
        "(up to 100 concurrent users)."
    )
    doc.add_paragraph("**Priority**: High")
    doc.add_paragraph("**Acceptance Criteria**:")
    doc.add_paragraph(
        "- 95% of API requests complete within 2 seconds", style="List Bullet"
    )
    doc.add_paragraph("- Page load time < 3 seconds", style="List Bullet")
    doc.add_paragraph(
        "- Search queries return results < 2 seconds", style="List Bullet"
    )

    doc.add_heading("REQ-012: Data Backup and Recovery", level=3)
    doc.add_paragraph(
        "The system shall perform automated database backups every 6 hours. "
        "Recovery Point Objective (RPO): 1 hour. Recovery Time Objective (RTO): 4 hours."
    )
    doc.add_paragraph("**Priority**: High")
    doc.add_paragraph("**Acceptance Criteria**:")
    doc.add_paragraph("- Backups run every 6 hours", style="List Bullet")
    doc.add_paragraph("- Backup success/failure logged", style="List Bullet")
    doc.add_paragraph("- Database restorable within 4 hours", style="List Bullet")

    doc.add_heading("REQ-013: Browser Compatibility", level=3)
    doc.add_paragraph(
        "The application shall be compatible with the latest versions of Chrome, Firefox, "
        "Edge, and Safari. Internet Explorer is not supported."
    )
    doc.add_paragraph("**Priority**: Medium")
    doc.add_paragraph("**Acceptance Criteria**:")
    doc.add_paragraph("- All functions work on Chrome 120+", style="List Bullet")
    doc.add_paragraph("- All functions work on Firefox 121+", style="List Bullet")
    doc.add_paragraph("- All functions work on Edge 120+", style="List Bullet")
    doc.add_paragraph("- All functions work on Safari 17+", style="List Bullet")

    doc.add_heading("REQ-014: Accessibility", level=3)
    doc.add_paragraph(
        "The application shall comply with WCAG 2.1 Level AA accessibility standards."
    )
    doc.add_paragraph("**Priority**: Low")
    doc.add_paragraph("**Acceptance Criteria**:")
    doc.add_paragraph(
        "- All interactive elements keyboard accessible", style="List Bullet"
    )
    doc.add_paragraph("- Screen reader compatible", style="List Bullet")
    doc.add_paragraph("- Minimum contrast ratio 4.5:1", style="List Bullet")

    doc.add_heading("5. References", level=1)
    doc.add_paragraph("- FDA 21 CFR Part 11: Electronic Records and Signatures")
    doc.add_paragraph("- EU Annex 11: Computerised Systems")
    doc.add_paragraph("- GAMP 5: Good Automated Manufacturing Practice")
    doc.add_paragraph("- WCAG 2.1: Web Content Accessibility Guidelines")

    doc.add_heading("6. Glossary", level=1)
    table = doc.add_table(rows=6, cols=2)
    table.style = "Table Grid"
    headers = ["Term", "Definition"]
    for i, h in enumerate(headers):
        table.rows[0].cells[i].text = h
    glossary = [
        ["RBAC", "Role-Based Access Control"],
        ["SKU", "Stock Keeping Unit"],
        ["RFC", "Remote Function Call (SAP protocol)"],
        ["RPO", "Recovery Point Objective"],
        ["RTO", "Recovery Time Objective"],
    ]
    for r, (term, definition) in enumerate(glossary):
        table.rows[r + 1].cells[0].text = term
        table.rows[r + 1].cells[1].text = definition

    # Save the document
    output_path = Path(
        "workflows/task-2-test-cases/input/requirement_specification.docx"
    )
    output_path.parent.mkdir(parents=True, exist_ok=True)
    doc.save(str(output_path))
    print(f"Created: {output_path}")
    print(f"Total requirements: 14 (10 functional, 4 non-functional)")


if __name__ == "__main__":
    create_requirement_spec()

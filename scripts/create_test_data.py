"""Create sample DOCX test files for workflow testing."""
from docx import Document
from docx.shared import Inches, Pt
from docx.enum.text import WD_ALIGN_PARAGRAPH
from PIL import Image
import io
from pathlib import Path


def make_screenshot(text, filename):
    """Create a simple test screenshot image."""
    img = Image.new('RGB', (800, 400), color=(240, 240, 240))
    img.save(filename, 'PNG')
    return filename


def create_app_design():
    doc = Document()
    doc.add_heading('Application Design Document', 0)

    doc.add_heading('1. Purpose', level=1)
    doc.add_paragraph(
        'This document describes the design of the ACME Inventory Management System (IMS) v2.5. '
        'The system provides real-time inventory tracking, automated reorder management, '
        'and compliance reporting for GxP-regulated warehouse operations.'
    )

    doc.add_heading('2. Scope', level=1)
    doc.add_paragraph(
        'The application covers inventory intake, storage tracking, dispatch, and audit trail '
        'generation. It integrates with the existing ERP system (SAP S/4HANA) and the quality '
        'management system (Veeva Vault QMS).'
    )

    doc.add_heading('3. System Overview', level=1)
    doc.add_paragraph(
        'ACME IMS is a three-tier web application consisting of a React frontend, '
        'a Python/FastAPI backend, and a PostgreSQL 15 database. '
        'Deployment target: Azure Kubernetes Service (AKS) in the US East region.'
    )

    doc.add_heading('4. Architecture', level=1)
    doc.add_heading('4.1 Components', level=2)
    table = doc.add_table(rows=4, cols=3)
    table.style = 'Table Grid'
    headers = ['Component', 'Technology', 'Version']
    for i, h in enumerate(headers):
        table.rows[0].cells[i].text = h
    data = [
        ['Frontend', 'React + TypeScript', '18.2'],
        ['Backend API', 'Python / FastAPI', '3.11 / 0.104'],
        ['Database', 'PostgreSQL', '15.4'],
    ]
    for r, row_data in enumerate(data):
        for c, val in enumerate(row_data):
            table.rows[r + 1].cells[c].text = val

    doc.add_heading('4.2 Interfaces and Data Flow', level=2)
    doc.add_paragraph(
        'The frontend communicates with the backend via REST API over HTTPS (TLS 1.3). '
        'The backend connects to PostgreSQL via connection pooling (pgBouncer). '
        'SAP integration uses RFC over a secure VPN tunnel.'
    )

    doc.add_heading('5. Security Considerations', level=1)
    doc.add_paragraph(
        'Authentication: Azure AD with SAML 2.0 SSO. '
        'Authorization: Role-based access control (RBAC) with 4 roles: Admin, Manager, Operator, Viewer. '
        'Data encryption: AES-256 at rest, TLS 1.3 in transit. '
        'Audit logging: All CRUD operations logged with user ID, timestamp, and IP address.'
    )

    doc.add_heading('6. Dependencies', level=1)
    doc.add_paragraph('- SAP S/4HANA 2023 FP1')
    doc.add_paragraph('- Veeva Vault QMS 23R2')
    doc.add_paragraph('- Azure AD B2C tenant')
    doc.add_paragraph('- SendGrid email service')

    doc.save('workflows/task-1-tdd-icv/input/application_design.docx')
    print('  Created: application_design.docx')


def create_workspace_design():
    doc = Document()
    doc.add_heading('Workspace Design Document', 0)

    doc.add_heading('1. Environment Overview', level=1)
    doc.add_paragraph(
        'The ACME IMS is deployed across three environments: DEV, UAT, and PROD. '
        'All environments run on Azure Kubernetes Service (AKS) with identical configuration '
        'except for resource scaling.'
    )

    doc.add_heading('2. Infrastructure', level=1)
    table = doc.add_table(rows=4, cols=4)
    table.style = 'Table Grid'
    headers = ['Environment', 'AKS Nodes', 'DB Size', 'Region']
    for i, h in enumerate(headers):
        table.rows[0].cells[i].text = h
    data = [
        ['DEV', '2', '50 GB', 'US East'],
        ['UAT', '3', '100 GB', 'US East'],
        ['PROD', '5', '500 GB', 'US East'],
    ]
    for r, row_data in enumerate(data):
        for c, val in enumerate(row_data):
            table.rows[r + 1].cells[c].text = val

    doc.add_heading('3. Workspace Configuration', level=1)
    doc.add_paragraph(
        'Developer workstations require: Python 3.11+, Node.js 20 LTS, Docker Desktop, '
        'Azure CLI 2.53+, kubectl 1.28+, and Helm 3.13+.'
    )

    doc.add_heading('4. Network Configuration', level=1)
    doc.add_paragraph(
        'VNet: 10.0.0.0/16. AKS subnet: 10.0.1.0/24. DB subnet: 10.0.2.0/24. '
        'NSG rules restrict DB access to AKS subnet only. VPN gateway for SAP connectivity.'
    )

    doc.add_heading('5. Prerequisites', level=1)
    doc.add_paragraph('- Azure subscription with Owner role')
    doc.add_paragraph('- Service principal for AKS')
    doc.add_paragraph('- SSL certificate for *.acme-ims.com')
    doc.add_paragraph('- VPN tunnel to on-premises SAP')

    doc.save('workflows/task-1-tdd-icv/input/workspace_design.docx')
    print('  Created: workspace_design.docx')


def create_gxp_assessment():
    doc = Document()
    doc.add_heading('GxP Assessment Document', 0)

    doc.add_heading('1. Regulatory Scope', level=1)
    doc.add_paragraph(
        'The ACME IMS falls under FDA 21 CFR Part 11 (Electronic Records) and EU Annex 11 '
        '(Computerised Systems). The system is classified as GxP Category 5 (Custom Application) '
        'per GAMP 5 guidelines.'
    )

    doc.add_heading('2. Risk Assessment', level=1)
    table = doc.add_table(rows=4, cols=4)
    table.style = 'Table Grid'
    headers = ['Risk', 'Impact', 'Likelihood', 'Mitigation']
    for i, h in enumerate(headers):
        table.rows[0].cells[i].text = h
    data = [
        ['Data integrity loss', 'High', 'Low', 'Audit trail + DB backups'],
        ['Unauthorized access', 'High', 'Medium', 'RBAC + SSO + MFA'],
        ['System downtime', 'Medium', 'Low', 'HA cluster + auto-failover'],
    ]
    for r, row_data in enumerate(data):
        for c, val in enumerate(row_data):
            table.rows[r + 1].cells[c].text = val

    doc.add_heading('3. Compliance Requirements', level=1)
    doc.add_paragraph('- Electronic signatures must comply with 21 CFR Part 11.50')
    doc.add_paragraph('- Audit trail must be immutable and include user ID + timestamp')
    doc.add_paragraph('- Data backup and recovery: RPO 1 hour, RTO 4 hours')
    doc.add_paragraph('- Annual access review required')
    doc.add_paragraph('- Change control process via Veeva Vault QMS')

    doc.add_heading('4. Validation Approach', level=1)
    doc.add_paragraph(
        'Validation follows GAMP 5 risk-based approach. IQ/OQ/PQ protocols will be executed. '
        'The ICV document covers Installation and Configuration Verification. '
        'Performance Qualification (PQ) is covered in a separate protocol.'
    )

    doc.save('workflows/task-1-tdd-icv/input/gxp_assessment.docx')
    print('  Created: gxp_assessment.docx')


def create_icv_steps():
    doc = Document()
    doc.add_heading('ICV Steps and Screenshots', 0)

    doc.add_heading('1. Installation Steps', level=1)

    doc.add_heading('Step 1: Deploy AKS Cluster', level=2)
    doc.add_paragraph(
        'Run the Terraform deployment script to provision the AKS cluster. '
        'Verify the cluster is running with `kubectl get nodes`.'
    )
    # Add a test screenshot
    img_path = make_screenshot('AKS Cluster Nodes', '/tmp/test_screenshot_1.png')
    doc.add_picture(img_path, width=Inches(5))

    doc.add_heading('Step 2: Deploy Database', level=2)
    doc.add_paragraph(
        'Execute the Helm chart for PostgreSQL deployment. '
        'Connection string: postgresql://ims_admin@acme-ims-db:5432/ims_prod'
    )
    img_path = make_screenshot('Database Deployment', '/tmp/test_screenshot_2.png')
    doc.add_picture(img_path, width=Inches(5))

    doc.add_heading('Step 3: Deploy Application', level=2)
    doc.add_paragraph(
        'Deploy the application using `helm install acme-ims ./charts/acme-ims`. '
        'Verify pods are running: `kubectl get pods -n acme-ims`.'
    )
    img_path = make_screenshot('Application Pods', '/tmp/test_screenshot_3.png')
    doc.add_picture(img_path, width=Inches(5))

    doc.add_heading('2. Configuration Steps', level=1)

    doc.add_heading('Step 4: Configure Azure AD SSO', level=2)
    doc.add_paragraph(
        'Register the application in Azure AD. Configure SAML 2.0 with '
        'Entity ID: https://acme-ims.com and Reply URL: https://acme-ims.com/auth/callback'
    )
    img_path = make_screenshot('Azure AD Config', '/tmp/test_screenshot_4.png')
    doc.add_picture(img_path, width=Inches(5))

    doc.add_heading('Step 5: Configure SAP Integration', level=2)
    doc.add_paragraph(
        'Set up RFC destination in SAP. Configure the VPN tunnel endpoint. '
        'Test connectivity using the SAP RFC test tool.'
    )

    doc.add_heading('3. Validation Steps', level=1)

    doc.add_heading('Step 6: Verify User Login', level=2)
    doc.add_paragraph(
        'Log in as test user (ims_test@acme.com). Verify SSO redirect works. '
        'Confirm role assignment displays correctly on the dashboard.'
    )
    img_path = make_screenshot('Login Success', '/tmp/test_screenshot_5.png')
    doc.add_picture(img_path, width=Inches(5))

    doc.add_heading('Step 7: Verify Audit Trail', level=2)
    doc.add_paragraph(
        'Create a test inventory record. Verify the audit trail entry includes: '
        'user ID, timestamp, action type, old value, and new value.'
    )
    img_path = make_screenshot('Audit Trail', '/tmp/test_screenshot_6.png')
    doc.add_picture(img_path, width=Inches(5))

    doc.add_heading('4. Results Summary', level=1)
    table = doc.add_table(rows=8, cols=3)
    table.style = 'Table Grid'
    headers = ['Step', 'Expected Result', 'Status']
    for i, h in enumerate(headers):
        table.rows[0].cells[i].text = h
    data = [
        ['1. Deploy AKS', '3 nodes running', 'PASS'],
        ['2. Deploy DB', 'PostgreSQL accepting connections', 'PASS'],
        ['3. Deploy App', 'All pods in Running state', 'PASS'],
        ['4. Configure SSO', 'SAML authentication works', 'PASS'],
        ['5. Configure SAP', 'RFC connection test successful', 'PASS'],
        ['6. Verify Login', 'User redirected and role shown', 'PASS'],
        ['7. Verify Audit', 'Audit entry with all fields', 'PASS'],
    ]
    for r, row_data in enumerate(data):
        for c, val in enumerate(row_data):
            table.rows[r + 1].cells[c].text = val

    doc.save('workflows/task-1-tdd-icv/input/icv_steps.docx')
    print('  Created: icv_steps.docx')


def create_templates():
    """Create template DOCX files with section headings and company styling."""
    # Technical Design Document template
    doc = Document()
    style = doc.styles['Title']
    style.font.size = Pt(24)

    doc.add_heading('Technical Design Document', 0)
    doc.add_heading('1. Purpose', level=1)
    doc.add_heading('2. Scope', level=1)
    doc.add_heading('3. System Overview', level=1)
    doc.add_heading('4. Architecture and Components', level=1)
    doc.add_heading('5. Workspace and Environment', level=1)
    doc.add_heading('6. Interfaces and Data Flow', level=1)
    doc.add_heading('7. Security Considerations', level=1)
    doc.add_heading('8. Regulatory and GxP Requirements', level=1)
    doc.add_heading('9. Dependencies', level=1)
    doc.add_heading('10. Glossary and References', level=1)

    doc.save('templates/document template/technical_design.docx')
    print('  Created: technical_design.docx template')

    # ICV Document template
    doc = Document()
    doc.add_heading('Installation Configuration and Validation', 0)
    doc.add_heading('1. Purpose', level=1)
    doc.add_heading('2. Scope', level=1)
    doc.add_heading('3. Prerequisites', level=1)
    doc.add_heading('4. Installation Steps', level=1)
    doc.add_heading('5. Configuration Steps', level=1)
    doc.add_heading('6. Validation and Verification Steps', level=1)
    doc.add_heading('7. Results Summary', level=1)
    doc.add_heading('8. Sign-off and Approval', level=1)

    doc.save('templates/document template/icv_document.docx')
    print('  Created: icv_document.docx template')


if __name__ == '__main__':
    print('Creating sample input DOCX files...')
    create_app_design()
    create_workspace_design()
    create_gxp_assessment()
    create_icv_steps()
    print('\nCreating template DOCX files...')
    create_templates()
    print('\nDone.')

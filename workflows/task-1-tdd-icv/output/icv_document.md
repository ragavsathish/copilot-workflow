---
title: "Installation Configuration and Validation"
subtitle: "ACME Inventory Management System (IMS) v2.5"
author: "ACME Engineering"
date: "2026-02-09"
version: "1.0"
status: "Draft"
document_id: "ICV-IMS-001"
---

# Installation Configuration and Validation

<!-- Source: gxp_assessment.md, §4 -->
# 1. Purpose

This document provides the Installation Configuration and Validation (ICV) evidence for the ACME Inventory Management System (IMS) v2.5. Validation follows the GAMP 5 risk-based approach. IQ/OQ/PQ protocols will be executed. This ICV document covers Installation and Configuration Verification. Performance Qualification (PQ) is covered in a separate protocol.

<!-- Source: gxp_assessment.md, §1 + application_design.md, §2 -->
# 2. Scope

The system under validation is the ACME IMS v2.5, a three-tier web application for GxP-regulated warehouse operations.

**Regulatory Framework:**

- FDA 21 CFR Part 11 (Electronic Records)
- EU Annex 11 (Computerised Systems)
- GAMP 5 Category 5 (Custom Application)

**Functional Scope:**

- Inventory intake, storage tracking, dispatch
- Audit trail generation
- Integration with SAP S/4HANA and Veeva Vault QMS

<!-- Source: workspace_design.md, §5 + §2 -->
# 3. Prerequisites

The following prerequisites must be in place before starting installation:

- Azure subscription with Owner role
- Service principal for AKS
- SSL certificate for *.acme-ims.com
- VPN tunnel to on-premises SAP

## Target Environment

| Environment | AKS Nodes | DB Size | Region |
|---|---|---|---|
| DEV | 2 | 50 GB | US East |
| UAT | 3 | 100 GB | US East |
| PROD | 5 | 500 GB | US East |

<!-- Source: icv_steps.md, §1 (Steps 1–3) -->
# 4. Installation Steps

## Step 1: Deploy AKS Cluster

Run the Terraform deployment script to provision the AKS cluster. Verify the cluster is running with `kubectl get nodes`.

**Expected Result:** 3 nodes in Ready state.

![AKS cluster deployment verification](images/icv_steps_img_001.png)
*Figure 1: AKS cluster node status verification*

## Step 2: Deploy Database

Execute the Helm chart for PostgreSQL deployment.

**Connection string:** `postgresql://ims_admin@acme-ims-db:5432/ims_prod`

**Expected Result:** PostgreSQL accepting connections.

## Step 3: Deploy Application

Deploy the application using `helm install acme-ims ./charts/acme-ims`.

Verify pods are running: `kubectl get pods -n acme-ims`.

**Expected Result:** All pods in Running state.

<!-- Source: icv_steps.md, §2 (Steps 4–5) + workspace_design.md, §3–§4 -->
# 5. Configuration Steps

## Step 4: Configure Azure AD SSO

Register the application in Azure AD. Configure SAML 2.0 with:

- **Entity ID:** https://acme-ims.com
- **Reply URL:** https://acme-ims.com/auth/callback

**Expected Result:** SAML authentication works.

## Step 5: Configure SAP Integration

Set up RFC destination in SAP. Configure the VPN tunnel endpoint. Test connectivity using the SAP RFC test tool.

**Network Configuration:**

- VNet: 10.0.0.0/16
- AKS subnet: 10.0.1.0/24
- DB subnet: 10.0.2.0/24
- VPN gateway for SAP connectivity

**Expected Result:** RFC connection test successful.

<!-- Source: icv_steps.md, §3 (Steps 6–7) -->
# 6. Validation and Verification Steps

## Step 6: Verify User Login

Log in as test user (ims_test@acme.com). Verify SSO redirect works. Confirm role assignment displays correctly on the dashboard.

**Expected Result:** User redirected and role shown.

## Step 7: Verify Audit Trail

Create a test inventory record. Verify the audit trail entry includes:

- User ID
- Timestamp
- Action type
- Old value
- New value

**Expected Result:** Audit entry with all required fields.

<!-- Source: icv_steps.md, §4 -->
# 7. Results Summary

| Step | Expected Result | Status |
|---|---|---|
| 1. Deploy AKS | 3 nodes running | PASS |
| 2. Deploy DB | PostgreSQL accepting connections | PASS |
| 3. Deploy App | All pods in Running state | PASS |
| 4. Configure SSO | SAML authentication works | PASS |
| 5. Configure SAP | RFC connection test successful | PASS |
| 6. Verify Login | User redirected and role shown | PASS |
| 7. Verify Audit | Audit entry with all fields | PASS |

All 7 steps completed successfully.

# 8. Sign-off and Approval

[To be completed — requires authorized signatories]

| Role | Name | Signature | Date |
|---|---|---|---|
| Prepared by | | | |
| Reviewed by | | | |
| Approved by (QA) | | | |
| Approved by (IT) | | | |

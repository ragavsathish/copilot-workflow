# ICV Steps and Screenshots
# 1. Installation Steps
## Step 1: Deploy AKS Cluster
Run the Terraform deployment script to provision the AKS cluster. Verify the cluster is running with `kubectl get nodes`.

## Step 2: Deploy Database
Execute the Helm chart for PostgreSQL deployment. Connection string: postgresql://ims_admin@acme-ims-db:5432/ims_prod

## Step 3: Deploy Application
Deploy the application using `helm install acme-ims ./charts/acme-ims`. Verify pods are running: `kubectl get pods -n acme-ims`.

# 2. Configuration Steps
## Step 4: Configure Azure AD SSO
Register the application in Azure AD. Configure SAML 2.0 with Entity ID: https://acme-ims.com and Reply URL: https://acme-ims.com/auth/callback

## Step 5: Configure SAP Integration
Set up RFC destination in SAP. Configure the VPN tunnel endpoint. Test connectivity using the SAP RFC test tool.
# 3. Validation Steps
## Step 6: Verify User Login
Log in as test user (ims_test@acme.com). Verify SSO redirect works. Confirm role assignment displays correctly on the dashboard.

## Step 7: Verify Audit Trail
Create a test inventory record. Verify the audit trail entry includes: user ID, timestamp, action type, old value, and new value.

# 4. Results Summary

| Step | Expected Result | Status |
| --- | --- | --- |
| 1. Deploy AKS | 3 nodes running | PASS |
| 2. Deploy DB | PostgreSQL accepting connections | PASS |
| 3. Deploy App | All pods in Running state | PASS |
| 4. Configure SSO | SAML authentication works | PASS |
| 5. Configure SAP | RFC connection test successful | PASS |
| 6. Verify Login | User redirected and role shown | PASS |
| 7. Verify Audit | Audit entry with all fields | PASS |

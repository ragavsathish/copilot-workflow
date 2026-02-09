# Workspace Design Document
# 1. Environment Overview
The ACME IMS is deployed across three environments: DEV, UAT, and PROD. All environments run on Azure Kubernetes Service (AKS) with identical configuration except for resource scaling.
# 2. Infrastructure

| Environment | AKS Nodes | DB Size | Region |
| --- | --- | --- | --- |
| DEV | 2 | 50 GB | US East |
| UAT | 3 | 100 GB | US East |
| PROD | 5 | 500 GB | US East |

# 3. Workspace Configuration
Developer workstations require: Python 3.11+, Node.js 20 LTS, Docker Desktop, Azure CLI 2.53+, kubectl 1.28+, and Helm 3.13+.
# 4. Network Configuration
VNet: 10.0.0.0/16. AKS subnet: 10.0.1.0/24. DB subnet: 10.0.2.0/24. NSG rules restrict DB access to AKS subnet only. VPN gateway for SAP connectivity.
# 5. Prerequisites
- Azure subscription with Owner role
- Service principal for AKS
- SSL certificate for *.acme-ims.com
- VPN tunnel to on-premises SAP
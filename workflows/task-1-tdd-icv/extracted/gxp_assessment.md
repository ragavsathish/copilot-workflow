# GxP Assessment Document
# 1. Regulatory Scope
The ACME IMS falls under FDA 21 CFR Part 11 (Electronic Records) and EU Annex 11 (Computerised Systems). The system is classified as GxP Category 5 (Custom Application) per GAMP 5 guidelines.
# 2. Risk Assessment

| Risk | Impact | Likelihood | Mitigation |
| --- | --- | --- | --- |
| Data integrity loss | High | Low | Audit trail + DB backups |
| Unauthorized access | High | Medium | RBAC + SSO + MFA |
| System downtime | Medium | Low | HA cluster + auto-failover |

# 3. Compliance Requirements
- Electronic signatures must comply with 21 CFR Part 11.50
- Audit trail must be immutable and include user ID + timestamp
- Data backup and recovery: RPO 1 hour, RTO 4 hours
- Annual access review required
- Change control process via Veeva Vault QMS
# 4. Validation Approach
Validation follows GAMP 5 risk-based approach. IQ/OQ/PQ protocols will be executed. The ICV document covers Installation and Configuration Verification. Performance Qualification (PQ) is covered in a separate protocol.
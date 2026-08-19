---
id: security-baseline
title: HU Application Security Baseline
kind: guidance
scope: university
owner: HU security owner
status: approved
last_reviewed: 2026-08-18
review_due: 2027-02-18
overridable: false
source: Verified extract from the HU-Agents framework (standards/security/owasp-checklist.md); approved for current framework scope
---

# HU Application Security Baseline

Use the OWASP Top 10 as the minimum review vocabulary for agent-assisted software work in the current framework scope, supplemented by current HU security requirements. Re-evaluate this baseline when the framework scales.

Review at least:

- Access control and role boundaries.
- Encryption of sensitive data in storage and transit.
- Input validation and injection resistance.
- Secure design and security-sensitive defaults.
- Dependency and vulnerability management.
- Authentication and session handling.
- Software and data integrity in CI/CD and updates.
- Security logging and monitoring.
- Validation of outbound requests, including SSRF risks.

Never hardcode credentials. Validate inputs at system boundaries and treat generated output that may contain personal data as sensitive. A security review should record its reviewer, date, findings, severity, and decision.

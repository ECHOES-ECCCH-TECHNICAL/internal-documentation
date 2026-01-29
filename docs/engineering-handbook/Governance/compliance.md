# Compliance, audits and onboarding

This page combines compliance audits, onboarding operations, exceptions/waivers, and record-keeping in one place.


## Compliance audits

### Objectives
Audits SHALL verify that:
- onboarded resources continue to satisfy the requirements corresponding to their assigned level,
- nodes continue to satisfy node/federation requirements,
- conformance reports remain reproducible and evidence-backed.

### When audits run
- at onboarding (full validation),
- periodically for L2/L3 resources and nodes (cadence defined by governance),
- on trigger events (REQ-MON-011): major releases, schema changes, AAI/security changes, repeated monitoring failures.

### Audit outputs
Each audit SHALL produce:
- conformance report,
- findings list (blocking / level-gating / non-blocking / missing evidence),
- remediation actions with deadlines and responsible parties.

If remediation is not completed within the agreed timeline, the assigned level SHALL be downgraded (REQ-MON-012 discipline).


## Onboarding process 
1) Provider prepares evidence package using the templates
2) Submission includes: resource type, intended level claim, access classification
3) Validation executed (static/dynamic/operational as applicable)
4) Conformance report issued; findings categorised
5) Level assignment recorded and communicated
6) Registration/discoverability confirmed; monitoring integration confirmed (where applicable)
7) Revalidation triggers documented


## Exceptions and waivers

Exceptions MAY be granted only under controlled conditions:
- request specifies affected identifiers, rationale, risk assessment, compensating controls,
- exceptions are time-bounded and reviewed,
- exceptions are recorded and included in audit reports.

Exceptions MUST NOT be used to bypass blocking security requirements for externally reachable endpoints (e.g., TLS enforcement).

### Minimal exception record (required fields)
- exception ID
- affected REQ/SEC/NODE identifiers
- rationale + risk assessment
- compensating controls
- time window + review date
- approver(s) + decision reference


## Compliance record-keeping

All conformance-related artefacts SHALL be retained in a controlled repository:
- conformance reports,
- exception/waiver records,
- framework version references used for each validation,
- evidence artefacts (or stable links),
- audit findings and remediation outcomes.

Retention policies MUST support traceability over the lifecycle of onboarded resources.

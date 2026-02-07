# Compliance, audits and onboarding

This page combines compliance audits, onboarding operations, exceptions and waivers, and record keeping requirements.

Normative baseline: the Governance, Updates, and Compliance controls and the validation discipline in D6.2, including REQ-MON-011 and REQ-MON-012.

## Compliance audits

### Objectives

Audits SHALL verify that:

- onboarded resources continue to satisfy the requirements corresponding to their assigned level
- node environments continue to satisfy federation requirements
- conformance reports remain reproducible and evidence backed

### When audits run

Audits SHALL be performed:

- at onboarding, full conformance validation
- periodically for L2 and L3 resources and nodes, cadence defined by governance and more frequent for high criticality services
- on trigger events, REQ-MON-011, such as major releases, schema or profile changes, AAI policy changes, repeated monitoring failures

### Audit outputs

Each audit SHALL produce:

- conformance report
- findings list, blocking, level gating, non blocking, missing evidence
- remediation actions with deadlines and responsible parties

If remediation is not completed within the agreed timeframe, the assigned level SHALL be downgraded.
The resource MAY be temporarily de listed if necessary to protect federation integrity.

## Findings classification

Validation and audit findings SHALL be classified as:

- Blocking failure, blocks onboarding, for example TLS failure
- Level gating failure, blocks the claimed level and triggers downgrade to the highest satisfied lower level
- Non blocking failure, failure of a SHOULD requirement, warning or recommendation
- Evidence missing, treated as failure for mandatory requirements

## Onboarding process

Onboarding SHALL follow a deterministic process aligned with the validation workflow.

1. Provider prepares evidence package using the templates, including declared version and contact.
2. Submission includes resource type, intended level claim, access classification.
3. TVT executes validation, static, dynamic, operational, manual as applicable.
4. Conformance report issued and findings categorised.
5. Level assignment issued per level rules and onboarding decisions recorded.
6. Resource is registered and becomes discoverable; monitoring integration confirmed where applicable.
7. Revalidation triggers documented, REQ-MON-011, and remediation and downgrade discipline applied, REQ-MON-012.


## Exceptions and waivers

Exceptions MAY be granted only under controlled conditions:

- request specifies affected identifiers, rationale, risk assessment, compensating controls
- exceptions are time bounded and reviewed
- exceptions are recorded and included in audit reports

Exceptions MUST NOT be used to bypass blocking security requirements for externally reachable endpoints, for example TLS enforcement.

### Minimal exception record

- exception ID
- affected REQ, SEC, NODE identifiers
- rationale and risk assessment
- compensating controls
- time window and review date
- approver or approvers and decision reference

## Communication obligations

Governance SHALL ensure:

- each framework release includes a change summary and migration guidance
- providers are notified of deprecations and deadlines
- operational incidents affecting federation interoperability are communicated with remediation expectations

## Support, escalation, and disputes

A support model SHALL exist that includes:

- a technical support channel for onboarding questions
- an escalation process for security issues
- a process for disputing validation findings, with recorded decisions

## Compliance record keeping

All conformance related artefacts SHALL be retained in a controlled repository, including:

- conformance reports
- exception and waiver records
- framework version references used for each validation
- evidence artefacts, or stable links to them
- audit findings and remediation outcomes

Record retention policies SHALL align with applicable legal and organisational requirements and MUST support traceability over the lifecycle of onboarded resources.

# Federation and Node Requirements

This page provides **operator and validator guidance** for CH Cloud federation nodes.

The **normative** baseline is the D6.2 node requirement set and the associated security and monitoring constraints referenced by those requirements.

## Scope and roles

Node types are non‑exclusive:

- compute
- data
- service
- integration
- control‑plane participant

Responsibility model, to be documented per node and hosted resource:

- Node Operator: platform availability and security
- Service Provider: service behaviour and contract conformance
- Data Provider: metadata, provenance, access policy for datasets and artefacts
- Federation Operator: federation registries, trust anchors, monitoring integration

An incident and escalation contact must be published, aligned with `REQ-MON-001`.

## How to use this page

- Providers and operators: use the Node onboard evidence package checklist and the per‑requirement guidance below.
- Validators: use the validation classes and evidence expectations to produce consistent conformance reports, see D6.2 Validation and Conformance Testing reporting format.
- Governance and operators: use revalidation triggers to prevent interoperability drift, aligned with `REQ-MON-011`.

## Requirement interpretation for validators

- Blocking: explicitly marked. Failure blocks onboarding at any level.
- Mandatory: baseline compliance for applicable scope.
- Recommended: best practice. Failure is a warning unless governance makes it gating.
- Evidence missing for a mandatory requirement is treated as failure.

## Validation classes

- Static: artefact review, policies, diagrams, configs, release notes
- Dynamic: runtime checks against deployed endpoints, TLS, auth flows, negative tests
- Operational: monitoring‑backed checks over time, availability, alerts, log and metric pipelines
- Manual or Process: governance controls and change triggers that must exist and be auditable

## Node onboard evidence package, minimum

Operators shall provide, or provide stable links to, the minimum evidence below.

1. Node roles and types, responsibility statement, and escalation contact, aligned with `REQ-MON-001`.
2. Ingress endpoints and DNS and TLS approach, including certificate lifecycle and renewal mechanism.
3. Admin‑surface exposure statement, management UIs and APIs restricted, and network segmentation summary.
4. Runtime model or models used, containers, VM, hybrid, and isolation and quota controls, including GPU scheduling if applicable.
5. Storage interfaces used for datasets and artefacts, access‑policy enforcement approach, and backup and restore, where stateful.
6. Registry and discovery integration method and a drift‑control statement, runtime versus registry consistency.
7. For restricted services: AAI and token validation configuration and policy enforcement point declaration, `SEC-07`, `SEC-09`, `SEC-11`.
8. Monitoring coverage summary, availability and platform signals, health and readiness probing for hosted services, and revalidation trigger process, aligned with `REQ-MON-011`.

Suggested packaging, example filenames:

- `node-profile.yml` roles, endpoints, contacts, runtime model
- `security-posture.md` TLS, admin restriction, secrets mechanism
- `aai-enforcement.md` token validation config, PEP location, fail‑closed statement
- `registry-integration.md` publishing method plus runtime versus registry drift controls
- `monitoring-coverage.md` dashboards, alerts, health probes, log and metric paths
- `backup-restore.md` for stateful services

A fill‑in template is provided in `conformance-evidence.md`.

## Per‑requirement operational guidance

The table below lists validation approaches and example evidence for each `NODE-*` requirement, aligned with D6.2 Table 7.1.

| ID | Requirement summary | Level | Criticality | Typical validation | Example evidence and checks |
|---|---|:---:|---|---|---|
| NODE-NET-01 | Stable DNS and routing for published endpoints | L1+ | Mandatory | Operational | Endpoint inventory plus DNS ownership and lifecycle; synthetic checks (HTTP or TCP) and uptime record. |
| NODE-NET-02 | **BLOCKING** HTTPS and TLS enforced for externally reachable endpoints (`SEC-01`) | L1+ | Mandatory | Dynamic | TLS scan output; HTTPS‑only behaviour; certificate chain and renewal automation evidence. |
| NODE-NET-03 | Network separation; admin surfaces not publicly exposed by default | L1+ | Mandatory | Static and Operational | Network diagram showing public ingress versus internal versus admin; evidence admin UIs and APIs restricted. |
| NODE-NET-04 | Outbound connectivity for token validation, registries, monitoring export | L2+ | Mandatory | Operational | Egress allowlist or proxy rules; reachability tests to IdP and AAI, registries, monitoring endpoints. |
| NODE-CMP-01 | Isolation boundaries and multi‑tenant quotas (CPU, RAM, GPU) | L2+ | Mandatory | Operational | Kubernetes quotas and limits or VM quotas; namespace or project boundaries; GPU scheduling policy if relevant. |
| NODE-CMP-02 | Accurate time synchronisation (for example NTP) | L2+ | Mandatory | Operational | NTP or chrony config; measured drift bounds; skew tolerance used for token validation. |
| NODE-STO-01 | Object storage for large assets and workflow outputs (S3 recommended) | L2+ | Recommended | Operational | Storage interface description (S3, Ceph, other), retention and lifecycle rules; endpoint and access method. |
| NODE-STO-02 | Storage exposure enforces declared access policy (public only if declared; restricted requires authN and authZ) | L1+ | Mandatory | Dynamic and Operational | Public versus restricted access tests; deny‑by‑default for restricted; least‑privilege IAM policy. |
| NODE-STO-03 | Backup and restore for stateful services aligned with criticality | L2+ where stateful | Mandatory | Static and Operational | Backup policy; restore test records; RPO and RTO targets; evidence of periodic restore drills. |
| NODE-REG-01 | Publish and maintain machine‑readable resource metadata into federation discovery | L1+ | Mandatory | Static and Operational | Publishing method (catalogue feed or API); registry entries; update procedure and ownership. |
| NODE-REG-02 | Deployed endpoint and version matches registry; drift triggers revalidation (`REQ-MON-011`) | L2+ | Mandatory | Operational | Runtime versus registry reconciliation checks; drift detection evidence; revalidation run records. |
| NODE-SYNC-01 | Replication: declare consistency model and propagation delays | L2+ where replicated | Mandatory | Static | Consistency model documentation, strong or eventual, plus maximum delay; where configured and monitored. |
| NODE-SYNC-02 | Do not overwrite immutable versions; version and supersession explicit | L2+ | Mandatory | Operational | Release policy; versioned artefacts and specs and shapes; proof of no overwrite; explicit supersession links. |
| NODE-SYNC-03 | Cache TTL and invalidation prevents prolonged staleness (metadata and policy decisions) | L2+ | Recommended | Operational | Cache TTL and invalidation config; tests showing updates propagate within bounded time. |
| NODE-AAI-01 | **BLOCKING** Token validation consistent with `SEC-07` (issuer, audience, signature, lifetime) with bounded skew | L2+ | Mandatory | Dynamic | Positive and negative token validation tests; clock‑skew handling; documented issuer and audience configuration. |
| NODE-AAI-02 | **BLOCKING** Declare PEP; enforce authZ consistently (`SEC-09`) and fail closed (`SEC-11`) | L2+ | Mandatory | Dynamic and Operational | PEP location; authorisation tests; fail‑closed evidence when policy evaluation fails or is unavailable. |
| NODE-SEC-01 | Secrets mechanism with controlled access (`SEC-18`) | L2+ | Mandatory | Static and Operational | Vault or Kubernetes secrets approach plus RBAC; rotation policy; evidence secrets not in logs or configs. |
| NODE-SEC-02 | **BLOCKING** Admin UIs and APIs restricted; not publicly exposed | L1+ | Mandatory | Operational | Proof admin endpoints are behind VPN, private network, or IP allowlist; periodic exposure review output. |
| NODE-MON-01 | Monitor ingress availability plus platform and storage health relevant to hosted resources | L2+ | Mandatory | Operational | Dashboards and alerts for ingress plus platform and storage; thresholds and escalation. |
| NODE-MON-02 | Incident process and escalation contact aligned with `REQ-MON-001` | L1+ | Mandatory | Static | Incident process documentation; on‑call rota or service desk path; contact point in published node info. |
| NODE-MON-03 | Probe service health and readiness and alert on sustained failures (`REQ-API-016`, `REQ-API-017`, `REQ-DEP-010`) | L2+ | Mandatory | Operational | Health and readiness probe config; alert history; SLO and SLA references where defined. |
| NODE-MON-04 | Standard path for structured logs and basic metrics; protect against secret and token leakage | L2+ | Recommended | Operational | Log and metric pipeline description; redaction rules; retention and access controls; sample redacted logs. |
| NODE-MON-05 | Trigger revalidation on platform changes (ingress, TLS, AAI, runtime upgrades) | L2+ | Mandatory | Manual or Process | Change trigger policy; evidence of revalidation runs after relevant changes; audit trail. |

## Reference patterns

The CH Cloud federation does not mandate a single stack.
Typical implementations include:

- containerised services: Kubernetes or OpenShift with ingress controller plus certificate automation
- VM‑based execution: OpenStack and VMs for specialised environments where needed
- object storage: S3‑compatible storage (for example Ceph gateway) for large binaries and workflow outputs
- AAI integration: OIDC‑based authentication with consistent token validation and authorisation enforcement
- monitoring: a standard monitoring and alerting path supporting revalidation triggers and auditability

## Revalidation triggers

Revalidation should be triggered at minimum when any of the following changes occur:

- ingress and routing or DNS changes impacting exposed endpoints
- TLS termination changes, certificate chain changes, or new reverse proxy or gateway deployment
- identity integration changes, IdP, issuer, audience, signing keys, token formats
- registry and discovery integration changes or changes affecting runtime versus registry consistency
- runtime upgrades that may affect API behaviour, error model, pagination, or health endpoints
- persistent changes in monitoring signals, availability errors, repeated 5xx, auth failures

# Federation and Node Requirements


## How to use this page

- **Providers/operators**: use the *Node onboarding evidence package* checklist and the per-requirement guidance below.
- **Validators**: use the validation steps to produce consistent conformance reports (Chapter 9 format).
- **Governance/operators**: use the revalidation triggers to prevent interoperability drift (REQ-MON-011 discipline).

## Validation classes

- **Static**: review submitted artefacts (policies, diagrams, configs, release notes).
- **Dynamic**: runtime checks against deployed endpoints (e.g., TLS, auth flows, error handling).
- **Operational**: monitoring-backed checks over time (availability, alerts, log/metric pipelines).
- **Manual/Process**: governance controls and change triggers that must exist and be auditable.

## Node onboarding evidence package (examples)

Operators should submit evidence as **versioned artefacts** (or stable links), e.g.:

- `node-profile.yml` (roles, endpoints, contacts, runtime model)
- `security-posture.md` (TLS termination, admin exposure statement, secrets mechanism)
- `aai-enforcement.md` (token validation config, PEP location, fail-closed statement)
- `monitoring-coverage.md` (dashboards, alerts, health probes, log/metric paths)
- `backup-restore.md` (for stateful services)

## Per-requirement operational guidance

The table below lists suggested validation approaches and example evidence for each NODE-* requirement.

| ID | Suggested validation | Example evidence / checks |
|---|---|---|
| NODE-NET-01 | Operational | Provide endpoint inventory + DNS ownership statement; monitor synthetic checks (HTTP/TCP) and record uptime/SLA history. |
| NODE-NET-02 | Dynamic | Run TLS scan (protocols/ciphers), verify HTTPS redirect, check cert chain and renewal; keep scan output as evidence. |
| NODE-NET-03 | Operational + Static | Network diagram showing public ingress vs internal network vs admin; verify admin UIs are not publicly reachable. |
| NODE-NET-04 | Operational | Egress allowlist policy; confirm outbound to IdP/AAI endpoints, registries, monitoring exporters; keep firewall/proxy rules. |
| NODE-CMP-01 | Operational | Quota config (K8s quotas/limits or VM quotas), namespace/project boundaries; GPU scheduling policy if relevant. |
| NODE-CMP-02 | Operational | NTP/chrony config; demonstrate bounded drift; note skew tolerance used for token validation. |
| NODE-STO-01 | Operational | Describe object storage interface, retention and lifecycle rules; show endpoint or access method (S3 API, gateway). |
| NODE-STO-02 | Dynamic + Operational | Access-control tests for public vs restricted objects; demonstrate least-privilege IAM policy and deny-by-default for restricted data. |
| NODE-STO-03 | Static + Operational | Backup policy + restore test record; define RPO/RTO for stateful services; evidence of periodic restore drills. |
| NODE-REG-01 | Static + Operational | Show how metadata is published (catalogue API/harvester feed) and how updates are propagated; include registry entries. |
| NODE-REG-02 | Operational | Runtime vs registry reconciliation checks; show drift detection and revalidation trigger path (REQ-MON-011). |
| NODE-SYNC-01 | Static | Document consistency model (strong/eventual) + max propagation delay; show where it is configured/monitored. |
| NODE-SYNC-02 | Operational | Release policy: immutable artefacts; use versioned buckets/tags; show that published specs/shapes are not overwritten. |
| NODE-SYNC-03 | Operational | Cache TTL/invalidation rules; demonstrate that updated metadata/policies propagate within bounded time. |
| NODE-AAI-01 | Dynamic | Token validation tests: signature, issuer, audience, expiry; include negative tests (wrong issuer/audience/expired) and clock-skew handling. |
| NODE-AAI-02 | Dynamic + Operational | Declare the Policy Enforcement Point (ingress/service); demonstrate authz enforcement and fail-closed behaviour on policy evaluation failure. |
| NODE-SEC-01 | Static + Operational | Secrets mechanism (vault/K8s secrets) with RBAC; evidence of rotation policy; show no secrets in logs or configs. |
| NODE-SEC-02 | Operational | Verify admin endpoints are restricted (VPN, private network, IP allowlist); include periodic exposure review output. |
| NODE-MON-01 | Operational | Monitoring dashboards/alerts for ingress + storage/platform; define alert thresholds and escalation path. |
| NODE-MON-02 | Static | Incident process + contact; on-call rota or service desk path; include expected response windows. |
| NODE-MON-03 | Operational | Health/readiness probe config; alert history for sustained failures; link to SLO/SLA if defined. |
| NODE-MON-04 | Operational | Log/metric pipeline description; redaction rules; demonstrate token/secret scrubbing; retention and access controls. |
| NODE-MON-05 | Manual/Process | Change trigger policy (ingress/TLS/AAI/runtime upgrades) and evidence of revalidation runs after changes. |

## Reference patterns 

The CH Cloud federation does not mandate a single stack. Typical implementations include:

- **Containerised services**: Kubernetes/OpenShift with ingress controller + certificate automation.
- **VM-based execution**: OpenStack/VMs for specialised environments where needed.
- **Object storage**: S3-compatible storage (e.g., Ceph gateway) for large binaries and workflow outputs.
- **AAI integration**: OIDC-based authentication with consistent token validation and authorisation enforcement.
- **Monitoring**: a standard monitoring/alerting path that supports revalidation triggers and auditability.

## Revalidation triggers 

Revalidation should be triggered at minimum when any of the following changes occur:

- Ingress/routing or DNS changes impacting exposed endpoints
- TLS termination changes, certificate chain changes, or new reverse proxy/gateway deployment
- Identity integration changes (IdP, issuer, audience, signing keys, token formats)
- Runtime upgrades that may affect API behaviour, error model, pagination, or health endpoints
- Persistent changes in monitoring signals (availability errors, repeated 5xx, auth failures)

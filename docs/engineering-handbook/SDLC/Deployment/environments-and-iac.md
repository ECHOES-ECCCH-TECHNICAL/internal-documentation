# Environments and Infrastructure as Code

Components should be promoted through environments with increasing blast radius (e.g., **dev - test/staging - production**).
The environment model should be explicit, reproducible, and aligned with governance/security expectations.

This page provides **practical, non‑normative** guidance for environment discipline and Infrastructure as Code (IaC).


## 1) Environment model (recommended baseline)

| Environment | Purpose | Typical properties |
|---|---|---|
| **Dev** | rapid iteration | lower controls, synthetic data, developer-owned |
| **Test/Staging** | production‑like validation | production‑like config, controlled test data, promotion gates |
| **Production** | service delivery | strict change control, observability, backups, incident process |

### Practical rule
Staging should be **close enough to production** that failures discovered in staging would also have failed in production (network rules, auth integration, dependencies, configuration shape).


## 2) Configuration and secrets

### Configuration discipline
- Keep **one configuration structure** across environments (same keys, same schema); environments differ only by values.
- Validate configuration before startup (schema checks where feasible).
- Avoid “hidden config”: if a setting is required for production reliability, document it and validate it.

### Secrets handling (non‑negotiable)
- Never commit secrets into repositories.
- Inject secrets at runtime using environment-specific mechanisms:
    - Kubernetes secrets (prefer KMS-backed where possible)
    - Vault or cloud secrets managers
    - sealed secrets / secret operators (if standard in your platform)

### Recommended controls
- least privilege (per environment and per component)
- rotation policy and audit trail
- secret masking in CI logs


## 3) Immutable deployment artefacts (deploy by digest)

A key interoperability and reliability rule is: **deploy the exact artefact you validated**.

Recommended pattern:
- build artefacts once (e.g., container image)
- promote by immutable identifier (digest), not by `latest`
- retain last known-good artefacts for rollback

Benefits:
- reduces “it worked on staging but not prod” drift
- enables fast rollback
- improves auditability (what exactly is running)


## 4) Infrastructure as Code (IaC)

Manual infrastructure changes are hard to audit and reproduce. IaC makes environments:
- versioned,
- reviewable,
- reproducible,
- easier to rebuild after failure.

### Common IaC tooling (examples)
| Tool | Focus | Typical use |
|---|---|---|
| Terraform / OpenTofu | provisioning | VMs, networks, storage, managed services |
| Ansible | configuration | OS/service configuration, repeatable ops tasks |
| Kubernetes manifests / Helm | orchestration | service deployments, configs, ingress, policies |
| Docker Compose | lightweight stacks | local/dev or small single-host setups |

### Minimum IaC expectations
- infrastructure definitions are version-controlled
- changes go through PR/MR review with automated checks (lint/plan)
- environment-specific values are explicit (vars files), not ad-hoc edits
- sensitive values are injected via secrets mechanisms


## 5) Drift and disaster recovery

### Drift detection
Where tooling supports it, periodically compare desired state to actual state:
- Terraform plan drift checks
- configuration compliance checks
- “known baseline” snapshots for critical settings

### Rebuild readiness
Maintain the ability to rebuild critical environments from source-controlled artefacts:
- IaC + documented bootstrap steps
- backup/restore runbooks
- tested recovery procedures for critical services


## 6) Evidence to retain

- environment definitions (IaC repos, variable sets, runbooks)
- configuration schemas and validation logs (where used)
- secrets management approach description (no secrets included)
- drift check outputs (if performed)
- recovery/rollback test evidence (periodic)



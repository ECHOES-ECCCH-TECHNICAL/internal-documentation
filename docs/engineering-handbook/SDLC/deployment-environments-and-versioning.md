# Deployment, Environments, and Versioning Management

In a multi-partner project, deployments must be predictable, repeatable, and easy to troubleshoot. They must also accommodate different infrastructure choices and operational maturity across consortium members. The core principles are consistent across component types: deploy in a controlled way, automate where feasible, and make failures easy to detect and recover from.

The intent is to reduce “it worked in one place” outcomes by standardizing *principles and interfaces* (pipelines, artifacts, environments, validation signals), while allowing tool- and platform-specific implementations to evolve over time.

## Scope and minimum expectations

This guidance applies to services, APIs, and deployable components delivered by ECHOES partners (containerized or otherwise).

| Topic | Minimum expectation | Evidence (examples) |
|---|---|---|
| Repeatability | Deployments are performed via a pipeline or scripted procedure | CI workflow, deployment playbook, runbook |
| Promotion discipline | Separation of test/staging and production promotion | Environment definitions, promotion approvals |
| Rollback readiness | Rollback path exists and is periodically verified | Rollback procedure + evidence of test |
| Deployment validation | Promotion gates include automated checks | CI job results, smoke test report |
| Version transparency | Deployed version is observable and traceable | Git tag, artifact digest, `/version` |
| Artifact immutability | Released artifacts are not overwritten | Registry policies, signed tags/digests |


## Deployment Pipelines and Rollback Strategies

Every service/component should be deployed via a pipeline: a repeatable sequence that automates testing, packaging, deployment, and verification.

### Typical Pipeline Stages

A deployment pipeline typically includes the following stages:

1. **Run unit and integration tests**
2. **Package the application** (container image, binary, Python wheel, etc.)
3. **Tag the release** using Semantic Versioning (SemVer)
4. **Deploy to staging/test** for validation
5. **Promote to production** via manual or automated approval gates

### Example: Release → Staging → Production promotion 

A common promotion flow for a service might look like this:

| Step | Action | Output artifact / signal |
|---|---|---|
| Build | Build container image from a tagged commit | Image digest (immutable) |
| Test | Run unit + integration tests | CI report (pass/fail) |
| Publish | Push image + attach version tag | `vX.Y.Z` tag + digest in registry |
| Deploy (staging) | Deploy by digest (not `latest`) | Staging deployment references digest |
| Validate | Run health + smoke + dependency checks | Validation job results |
| Promote | Approval gate (manual or automated) | Promotion event recorded in CI |
| Deploy (prod) | Deploy same digest to prod | Production references same digest |
| Observe | Monitor SLOs/logs and error budget | Alerts/SLO dashboard |

Key point: **production is promoted by reusing the exact artifact built and validated in staging** (same digest).


### Rollback Principles

Rollback should be fast and safe. Key principles include:

- **Deployments should be atomic and reversible** to minimize risk
- **Previous versions remain available** (keep at least the last 2–3 versions)
- **Rollback procedures are tested periodically** to ensure they work when needed
- **Post-deploy monitoring and escalation paths are defined** for quick issue detection

### Example: Fast rollback after a regression

A typical rollback scenario:

- A new release is deployed to production (e.g., `v2.4.0`).
- Monitoring detects elevated 5xx rates and latency within minutes.
- The on-call team triggers rollback to the last known-good release (e.g., `v2.3.2`), using the previously deployed artifact digest.
- Post-rollback verification confirms readiness and key smoke tests pass.
- A short incident note records: deployed version, rollback version, timeframe, and suspected root cause.

Operational expectation: rollback should not require rebuilding artifacts; it should be a **configuration change** that points production back to a known-good immutable artifact.


### Deployment Strategies

| Strategy | Description | Typical Use Case |
|----------|-------------|------------------|
| **Rolling update** | Gradually replace old instances with new ones | Standard deployments with minimal downtime |
| **Blue-green** | Two identical environments; switch traffic instantly | Near zero-downtime, simple rollback |
| **Canary** | Deploy to a small subset of traffic/users first | Risk mitigation for critical services |
| **Recreate** | Stop old version, start new version | Simpler deployments where downtime is acceptable |

## Environments and configuration management

Components should be promoted through environments with increasing blast radius (e.g., dev → test/staging → production). The environment model should be explicit and reproducible.

### Environment baseline

| Environment | Purpose | Typical properties |
|---|---|---|
| Dev | Rapid iteration | Lower controls, synthetic data, developer-owned |
| Test/Staging | Production-like validation | Production-like config, controlled test data, promotion gates |
| Production | Service delivery | Strict change control, observability, backups, incident process |

### Configuration and secrets

- Treat configuration as code where possible (versioned templates, schema validation).
- **Never commit secrets**; use a secrets manager or environment-specific secret distribution.
- Prefer explicit configuration schemas and validation to prevent partial/invalid deployments.

### Practical patterns

| Pattern | Why it helps |
|---|---|
| Deploy by **digest**, not by mutable tags (e.g., avoid `latest`) | Guarantees the same artifact is running everywhere |
| Validate configuration via **schema checks** before startup | Prevents partial config from causing runtime failures |
| Separate config per environment but keep **one config structure** | Reduces surprises during promotion |
| Store secrets in a manager and inject at runtime | Prevents credential leakage and enables rotation |



## Infrastructure as Code (IaC)

Managing infrastructure manually is risky and hard to audit. Prefer Infrastructure as Code (IaC) so that environments are reproducible, reviewable, versioned, and shareable across teams.

### Benefits of IaC

- **Consistent environments** across test, staging, and production
- **Auditable change history** with version control integration
- **Fast rebuild** in case of failure or disaster recovery
- **Portable blueprints** across providers (cloud/on-premises)

### Tooling Overview

| Tool | Focus | Language | Best For |
|------|-------|----------|----------|
| **Terraform** | Infrastructure provisioning | HCL | Cloud resources (VMs, networks, storage) |
| **Ansible** | Configuration management | YAML | Installing software, managing configurations |

#### Lightweight Deployment Options

Even lightweight deployments benefit from codification:

- **Docker Compose** for small, single-host deployments
- **Kubernetes manifests/Helm** for orchestrated services



## Test Automation for Deployment Validation

Before a release is promoted to production, it should pass automated deployment validation tests that confirm it works in a production-like environment with real dependencies and configuration.

### What Deployment Validation Confirms


| Validation question | Examples of evidence |
|---|---|
| Can the service start in the target environment? | Successful startup; readiness probe passes |
| Is configuration complete and correct? | Required env vars/secrets present; config schema checks |
| Can the service connect to dependencies? | DB/queue/cache connectivity checks; timeouts within limits |
| Does authn/authz work end-to-end? | Token validation against real IdP; role-based access checks |
| Does it respond correctly to real requests? | Key endpoints return expected status codes and payload shapes |


### Recommended Validation Test Types

| Test Type | Purpose | Typical Examples | Notes |
|-----------|---------|------------------|-------|
| **Health checks** | Confirm service is running and responsive | Liveness/readiness endpoints; basic HTTP 200 | Keep lightweight; avoid external dependencies |
| **Smoke tests** | Verify essential workflows quickly | Minimal CRUD path; search returns results; auth validates tokens | Breadth over depth; use controlled test data |
| **Dependency integration checks** | Confirm connectivity/compatibility | DB migrations; queue publish/consume; external API reachability | Catches network/config issues mocks miss |
| **Security & compliance checks** | Ensure controls apply in deployed environment | HTTPS enforced; auth required; security headers; audit logging | Focused on deployment-relevant controls |

### Design Principles for Validation Tests

| Principle | Guideline |
|-----------|-----------|
| **Speed** | Complete in minutes to avoid blocking delivery |
| **Reliability** | Deterministic; flaky tests fixed or quarantined |
| **Clear failures** | Errors identify failing check, endpoint, and relevant dependency/config |
| **Automation and gating** | Run automatically in pipeline; failures block promotion |

### Pipeline Integration

Deployment validation should be integrated into your CI/CD pipeline with the following practices:

- **Run automatically** after deployment to test/staging environments
- **Act as a promotion gate** to prevent faulty releases from reaching production
- **Retain results** as CI artifacts/dashboards for historical tracking
- **Notify on failures** with links to logs, test reports, and deployed version metadata


## Semantic Versioning and Immutable Artifacts

All deployable components should follow Semantic Versioning (SemVer) to make compatibility expectations explicit (e.g., `v2.1.0` indicates major/minor/patch semantics).

### Immutable Artifacts

Released artifacts should be **immutable**:

- Once built and tagged, they must not change
- If a rebuild is required, publish a new version tag
- Never modify existing releases in place

### Versioning Best Practices

- **Tag releases in Git** (e.g., `git tag v2.1.0`) for traceability
- **Expose version information** via `/version` endpoint or `version.txt` file
- **Keep the same version** across all artifacts (image, docs, API spec)
- **Generate changelogs** from commit metadata (e.g., Conventional Commits + changelog tooling)
- **Never delete or overwrite** published artifacts

### Examples: Interpreting SemVer changes

| Change type | Example | Expected impact |
|---|---|---|
| Patch (`x.y.Z`) | Bug fix, no API change | Safe upgrade, low integration risk |
| Minor (`x.Y.0`) | Backward-compatible feature | Upgrade expected to work without client changes |
| Major (`X.0.0`) | Breaking API / behavior change | Requires consumer review and planned migration |

Where possible, document breaking changes explicitly in the changelog and (for APIs) reflect them in the OpenAPI/AsyncAPI schema.

# Deployment, Environments, and Versioning Management

In a multi-partner project, deployments must be predictable, repeatable, and easy to troubleshoot. They must also accommodate different infrastructure choices and operational maturity across consortium members. The core principles are consistent across component types: deploy in a controlled way, automate where feasible, and make failures easy to detect and recover from.

!!! note "Normative Boundary"
This page is implementation guidance (Living Documentation). It does not create new normative requirements beyond those defined in D6.2 Chapter 8 and validated via Chapters 9–11.


## Deployment Pipelines and Rollback Strategies

Every service/component should be deployed via a pipeline: a repeatable sequence that automates testing, packaging, and deployment.

### Typical Pipeline Stages

A deployment pipeline typically includes the following stages:

1. **Run unit and integration tests** to validate code quality
2. **Package the application** (e.g., container image, binary, Python wheel)
3. **Tag the release** using Semantic Versioning
4. **Deploy to staging/test environment** for validation
5. **Promote to production** via manual or automated approval

### Rollback Principles

Rollback should be fast and safe. Key principles include:

- **Deployments should be atomic and reversible** to minimize risk
- **Previous versions remain available** (keep at least the last 2–3 versions)
- **Rollback procedures are tested periodically** to ensure they work when needed
- **Post-deploy monitoring and escalation paths are defined** for quick issue detection

!!! tip "Immutable Artifacts"
Immutable artifacts (e.g., versioned container images) reduce "it works on my machine" drift and simplify rollback procedures.

### Deployment Strategies

| Strategy | Description | Typical Use Case |
|----------|-------------|------------------|
| **Rolling update** | Gradually replace old instances with new ones | Standard deployments with minimal downtime |
| **Blue-green** | Two identical environments; switch traffic instantly | Near zero-downtime, simple rollback |
| **Canary** | Deploy to a small subset of traffic/users first | Risk mitigation for critical services |
| **Recreate** | Stop old version, start new version | Simpler deployments where downtime is acceptable |

---

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

| Validation Question | Examples of Evidence |
|---------------------|---------------------|
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

!!! tip "Version Consistency"
Maintaining consistent version numbers across all artifacts (container images, documentation, API specifications) makes debugging and traceability much easier.
# Deployment Pipelines and Rollback Strategies

Every service/component should be deployed via a **pipeline**: a repeatable sequence that automates testing, packaging, deployment, and verification.

In federated systems, the main goal is to ensure that:
- the artefact promoted to production is **exactly** the artefact validated in staging,
- failures are detected quickly and rollback is fast and safe.

---

## 1) Typical pipeline stages (reference model)

A deployment pipeline commonly includes:

1. **Build and test**
    - unit tests, integration tests, contract validation
2. **Package artefacts**
    - container images, binaries, wheels, etc.
3. **Tag the release**
    - semantic version tag and release notes
4. **Deploy to staging/test**
    - deploy **by digest**, not by mutable tag
5. **Post-deploy validation**
    - health checks, smoke tests, dependency checks, security checks
6. **Promote to production**
    - approval gate (manual or automated, per governance)
7. **Observe and enforce SLOs**
    - dashboards, alerts, error budget monitoring

> Key rule: **promotion reuses the exact immutable artefact built and validated in staging**.

---

## 2) Promotion example (staging → production)

| Step | Action | Output / signal |
|---|---|---|
| Build | build artefact from a tagged commit | immutable digest |
| Validate | run tests + contract checks | CI reports |
| Deploy (staging) | deploy by digest | staging references digest |
| Verify | run validation suite | validation report |
| Promote | approval gate event recorded | promotion record |
| Deploy (prod) | deploy same digest | production references same digest |
| Observe | monitor KPIs/SLOs | dashboards + alerts |

## 3) Rollback principles

Rollback should be **fast** and should not require rebuilding artefacts.

Recommended baseline rules:
- deployments are atomic and reversible (strategy-dependent)
- keep at least the last **2–3 known-good versions** available
- rollback procedures are **documented** and **tested periodically**
- post-rollback verification confirms readiness and key workflows

### Typical rollback flow (example)
1. detect regression (alerts: 5xx rate, latency spike, auth failures)
2. trigger rollback to last known-good version (by digest)
3. validate (health + smoke tests)
4. record an incident note (versions, timeframe, suspected root cause)


## 4) Deployment strategies (choose per service)

| Strategy | Description | Typical use |
|---|---|---|
| **Rolling update** | replace instances gradually | standard stateless services |
| **Blue‑green** | switch traffic between two environments | near zero‑downtime, instant rollback |
| **Canary** | small traffic segment first | higher-risk changes, progressive rollout |
| **Recreate** | stop old, start new | low criticality, downtime acceptable |

Selection criteria:
- user impact tolerance,
- rollback requirements,
- dependency complexity,
- observability maturity.


## 5) Validation as a promotion gate (strong recommendation)

Promotion should be blocked unless the staging deployment passes:
- health/readiness checks
- smoke tests for critical workflows
- dependency connectivity checks (DB/queue/storage)
- authn/authz verification (where applicable)
- security baselines (TLS, headers, restricted route enforcement)

See **Deployment validation and versioning** for a reference validation suite structure.


## 6) Evidence artefacts to retain

- pipeline logs for each stage
- artefact digest + version tag used in each environment
- validation suite outputs (smoke/health/security checks)
- rollback test evidence (periodic)
- incident notes for material rollbacks

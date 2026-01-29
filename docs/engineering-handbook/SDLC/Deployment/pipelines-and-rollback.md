# Deployment Pipelines and Rollback Strategies

Every service/component should be deployed via a pipeline: a repeatable sequence that automates testing, packaging, deployment, and verification.

## Typical pipeline stages

A deployment pipeline typically includes the following stages:

1. **Run unit and integration tests**
2. **Package the application** (container image, binary, Python wheel, etc.)
3. **Tag the release** using Semantic Versioning (SemVer)
4. **Deploy to staging/test** for validation
5. **Promote to production** via manual or automated approval gates

## Example: Release → staging → production promotion

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

## Rollback principles

Rollback should be fast and safe. Key principles include:

- **Deployments should be atomic and reversible** to minimize risk
- **Previous versions remain available** (keep at least the last 2–3 versions)
- **Rollback procedures are tested periodically** to ensure they work when needed
- **Post-deploy monitoring and escalation paths are defined** for quick issue detection

## Example: Fast rollback after a regression

A typical rollback scenario:

- A new release is deployed to production (e.g., `v2.4.0`).
- Monitoring detects elevated 5xx rates and latency within minutes.
- The on-call team triggers rollback to the last known-good release (e.g., `v2.3.2`), using the previously deployed artifact digest.
- Post-rollback verification confirms readiness and key smoke tests pass.
- A short incident note records: deployed version, rollback version, timeframe, and suspected root cause.

Operational expectation: rollback should not require rebuilding artifacts; it should be a **configuration change** that points production back to a known-good immutable artifact.

## Deployment strategies

| Strategy | Description | Typical use case |
|---|---|---|
| **Rolling update** | Gradually replace old instances with new ones | Standard deployments with minimal downtime |
| **Blue-green** | Two identical environments; switch traffic instantly | Near zero-downtime, simple rollback |
| **Canary** | Deploy to a small subset of traffic/users first | Risk mitigation for critical services |
| **Recreate** | Stop old version, start new version | Simpler deployments where downtime is acceptable |

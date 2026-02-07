# Deployment, Environments, and Versioning Management

Deployments in a multi-partner environment must be predictable, repeatable, and easy to troubleshoot. This page describes practical deployment discipline that supports interoperability: **immutable artefacts**, controlled promotion, fast rollback, and transparent versioning.


## Minimum expectations (baseline)

| Topic | Minimum expectation | Typical evidence |
|---|---|---|
| Repeatability | deployment via pipeline or scripted procedure | CI workflow, playbook, runbook |
| Environment discipline | dev/staging/prod separation | environment configs, approvals |
| Rollback readiness | rollback exists and is tested | rollback procedure + test record |
| Deployment validation | promotion gates include checks | smoke test report, health checks |
| Version transparency | deployed version observable | git tag, artifact digest, `/version` |
| Artifact immutability | releases are not overwritten | registry policies, digests |


## Promotion model (recommended)

A typical promotion chain:
1. build artefact from a tagged commit
2. run tests + security checks
3. deploy to staging **by digest**
4. validate in staging
5. promote the exact same artefact to production

Key rule: production should run the same artefact that was validated in staging (same digest).


## Rollback principles

Rollback should be a **configuration change**, not a rebuild:
- keep last known-good artefacts available
- rollback steps are documented and rehearsed
- post-rollback checks confirm readiness and key workflows


## Deployment strategies (choose per service)

| Strategy | Best for | Notes |
|---|---|---|
| Rolling update | stateless services | simplest baseline |
| Blue-green | critical services | instant rollback |
| Canary | high-risk changes | requires monitoring and gating |
| Recreate | low criticality | downtime acceptable |


## Configuration and secrets

- configuration structure consistent across environments
- validate configuration (schema checks) before startup where possible
- secrets are never committed; injected at runtime via secrets manager mechanisms
- keep “one way” to configure (avoid conflicting flags/env-files)


## Deployment validation tests (recommended)

Before promotion, confirm:
- service starts and becomes ready
- config is complete and valid
- dependencies reachable (DB/queue/storage)
- authn/authz works (where applicable)
- key endpoints behave correctly (smoke tests)

Retain results as CI artefacts.


## Related pages
- [CI/CD](CICD.md)
- [Testing](testing.md)
- [Continuous monitoring and feedback loops](continuous-monitoring-and-feedback-loops.md)

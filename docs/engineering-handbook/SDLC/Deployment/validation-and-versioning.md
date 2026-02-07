# Deployment Validation and Versioning

Before a release is promoted to production, it should pass automated deployment validation that confirms the service works in a production‑like environment with real configuration and dependencies.

This page provides:

- a reference deployment validation suite structure
- guidance on semantic versioning
- rules for immutable artefacts and traceability

## 1) What deployment validation confirms

| Validation question | Typical evidence |
|---|---|
| Can the service start in the target environment | startup succeeds; readiness passes |
| Is configuration complete and correct | env and secrets present; config schema checks |
| Can the service connect to dependencies | DB, queue, cache connectivity tests |
| Does authentication and authorisation work end to end | token validation; protected routes enforced |
| Does it respond correctly to real requests | key endpoints return expected codes and shapes |

## 2) Recommended validation test types

| Test type | Purpose | Examples | Notes |
|---|---|---|---|
| Health checks | confirm service is alive and ready | liveness and readiness endpoints | lightweight, deterministic |
| Smoke tests | verify essential workflows | minimal CRUD; search returns results; auth flow works | breadth over depth |
| Dependency checks | validate integration points | migrations; publish and consume; external API reachability | catches config and network issues |
| Security checks | ensure controls apply in deployment | HTTPS enforced; auth required; headers; audit logging | deployment relevant controls only |

## 3) Design principles for validation tests

| Principle | Guideline |
|---|---|
| Speed | complete in minutes to avoid blocking delivery |
| Reliability | deterministic; flaky checks fixed or quarantined |
| Actionable failures | identify failing check, endpoint, dependency, or config |
| Gating | run automatically; failures block promotion |
| Evidence | retain outputs as CI artefacts for traceability |

## 4) Pipeline integration

- run validation automatically after staging deploy
- use results as a promotion gate to production
- retain results as CI artefacts or dashboards
- notify on failure with links to logs, reports, and deployed version metadata

## 5) Semantic versioning and immutable artefacts

### Semantic versioning

Use `MAJOR.MINOR.PATCH`:

- MAJOR: breaking changes, consumer action required
- MINOR: backward compatible features
- PATCH: backward compatible fixes

Version changes should align with interface behaviour and contracts, APIs, events, and schemas.

### Immutable artefacts

Released artefacts must be immutable:

- once built and tagged, they must not change
- if a rebuild is required, publish a new version tag
- never overwrite existing releases in registries

Recommended practices:

- tag releases in Git, for example `vX.Y.Z`, for traceability
- expose deployed version, `/version` endpoint or equivalent
- keep the same version across artefacts, image, docs, API spec
- publish changelogs and migration notes for breaking changes

## 6) Evidence artefacts to retain

- CI job summaries and logs, build, test, validate
- validation reports, health, smoke, security
- artefact digests and tags deployed to each environment
- changelog or release notes and migration guidance
- configuration validation outputs, where applicable

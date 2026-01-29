# Deployment Validation and Versioning

## Test automation for deployment validation

Before a release is promoted to production, it should pass automated deployment validation tests that confirm it works in a production-like environment with real dependencies and configuration.

### What deployment validation confirms

| Validation question | Examples of evidence |
|---|---|
| Can the service start in the target environment? | Successful startup; readiness probe passes |
| Is configuration complete and correct? | Required env vars/secrets present; config schema checks |
| Can the service connect to dependencies? | DB/queue/cache connectivity checks; timeouts within limits |
| Does authn/authz work end-to-end? | Token validation against real IdP; role-based access checks |
| Does it respond correctly to real requests? | Key endpoints return expected status codes and payload shapes |

### Recommended validation test types

| Test type | Purpose | Typical examples | Notes |
|---|---|---|---|
| **Health checks** | Confirm service is running and responsive | Liveness/readiness endpoints; basic HTTP 200 | Keep lightweight; avoid external dependencies |
| **Smoke tests** | Verify essential workflows quickly | Minimal CRUD path; search returns results; auth validates tokens | Breadth over depth; use controlled test data |
| **Dependency integration checks** | Confirm connectivity/compatibility | DB migrations; queue publish/consume; external API reachability | Catches network/config issues mocks miss |
| **Security & compliance checks** | Ensure controls apply in deployed environment | HTTPS enforced; auth required; security headers; audit logging | Focused on deployment-relevant controls |

### Design principles for validation tests

| Principle | Guideline |
|---|---|
| **Speed** | Complete in minutes to avoid blocking delivery |
| **Reliability** | Deterministic; flaky tests fixed or quarantined |
| **Clear failures** | Errors identify failing check, endpoint, and relevant dependency/config |
| **Automation and gating** | Run automatically in pipeline; failures block promotion |

### Pipeline integration

Deployment validation should be integrated into your CI/CD pipeline with the following practices:

- **Run automatically** after deployment to test/staging environments
- **Act as a promotion gate** to prevent faulty releases from reaching production
- **Retain results** as CI artifacts/dashboards for historical tracking
- **Notify on failures** with links to logs, test reports, and deployed version metadata



## Semantic versioning and immutable artifacts

All deployable components should follow Semantic Versioning (SemVer) to make compatibility expectations explicit (e.g., `v2.1.0` indicates major/minor/patch semantics).

### Immutable artifacts

Released artifacts should be **immutable**:

- Once built and tagged, they must not change
- If a rebuild is required, publish a new version tag
- Never modify existing releases in place

### Versioning best practices

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

# Testing

Automated testing enables safer change, faster iteration, and higher confidence in interoperability across partners
. In a federated environment, tests are not only for correctness they are **evidence**
that interfaces, security, and behavioural contracts remain stable across releases.

This page describes a pragmatic test strategy suitable for services, APIs, workflows, and web applications delivered into the CH Cloud.


## Scope and audience

Applies to:
- APIs and services (REST, GraphQL, messaging/event consumers)
- workflow components (pipelines, converters, enrichers)
- web applications and UIs
- infrastructure glue code where failures affect availability or security

Audience:
- developers (component owners)
- validators/reviewers (onboarding evidence)
- operators (release gates and regression control)


## Test tiers (recommended baseline)

| Tier | What it proves | Typical scope | Where it runs | Common tools |
|---|---|---|---|---|
| **Unit** | local logic is correct | functions/classes/modules | local + CI | pytest, JUnit, Jest |
| **Integration** | components work together | API ↔ DB, queue, storage, auth flows | CI + ephemeral env | Testcontainers, pytest+Docker, Robot Framework, contract tests |
| **E2E** | critical user journeys work | UI + backend + external integrations | staging / near‑prod | Playwright, Cypress, Robot Framework |

### Expectations by tier

| Tier | Should be | Should avoid | Key checks |
|---|---|---|---|
| Unit | fast, deterministic, isolated | network/database, complex setup | edge cases, boundaries, error handling |
| Integration | realistic dependencies, contract validation | broad UI coverage, flaky timing | authn/authz, migrations, config wiring, persistence |
| E2E | few, high‑value journeys | “test everything”, brittle selectors | login, search, view, create/update, permissions |


## The test pyramid (practical target)

A typical healthy distribution:
- **70–80%** unit tests (fast feedback)
- **15–20%** integration tests (interfaces and wiring)
- **5–10%** E2E tests (critical workflows only)

This balance keeps pipelines fast while still covering real-world failure modes.


## Contract testing (strongly recommended for APIs/events)

Interoperability failures are often **behavioural drift** (not compile errors). Contract tests reduce this drift.

### REST/HTTP APIs
- validate OpenAPI syntax and style
- validate responses against schemas
- enforce error model consistency (status codes + machine‑readable error IDs)

### Event-driven contracts
- version event schemas
- validate required fields (`event_id`, `event_type`, `timestamp`, `source`, `data`, correlation IDs where used)
- ensure consumers are **idempotent** (duplicate delivery should not break behaviour)


## Security and compliance tests (minimum)

Where a component exposes protected functionality or processes restricted data, include automated checks that verify:
- TLS/HTTPS enforcement
- token validation correctness (issuer/audience/signature/expiry)
- authorisation enforcement for protected routes
- no secrets committed to repository (secret scanning)

These checks can run as:
- integration tests against a test IdP / OIDC provider
- pipeline security gates (SAST/SCA/secret scanning)

(See the **Security** and **CI/CD** pages for recommended tooling and gates.)


## Where tests run (pipeline guidance)

- **On every PR**: lint + unit tests + fast integration smoke where feasible
- **On merge**: broader integration suite; contract checks; packaging
- **Nightly / scheduled**: E2E tests; longer-running integration suites; performance checks

### Evidence outputs (what to keep)
For onboarding and ongoing assurance, archive:
- CI job summaries (pass/fail + links)
- test reports (JUnit XML / Allure / ReportPortal)
- E2E screenshots/videos on failure
- coverage reports (where used)
- contract validation outputs (OpenAPI/AsyncAPI schema checks)


## Performance testing 

For user-facing APIs and critical services, add lightweight load/performance checks:
- set p95 latency thresholds
- set error-rate thresholds
- detect regressions between releases

k6 is commonly used for CI-friendly load tests; keep tests short and reproducible (avoid “freeform” benchmarks).


## Related pages
- [CI/CD](CICD.md)
- [Deployment, environments, and versioning](deployment-environments-and-versioning.md)
- [Security](security.md)

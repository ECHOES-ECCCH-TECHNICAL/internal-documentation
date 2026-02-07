# API

This page provides **living, tool-agnostic guidance** for validating APIs and network services that participate in the CH Cloud federation.
It supports the normative validation approach defined in the **D6.2 deliverable** by describing *what evidence to collect*, *what to test*, and *what to report*.

The validator’s goal is to confirm that a service is:
- **contract-driven** (machine-readable specification exists and matches runtime),
- **secure by default** (TLS, consistent authn/authz for restricted endpoints),
- **predictable** (stable behaviour and error model),
- **operable** (health/readiness, basic resiliency, monitorable).


## Scope

Applies to:
- REST APIs (OpenAPI-described where applicable),
- service endpoints (including gateways, validators, job runners),
- GraphQL endpoints (schema-based validation),
- SPARQL endpoints (protocol-level checks and agreed feature envelope).


## Inputs: evidence package

### Minimum evidence (must be provided)
- Service identifier and **base URL(s)** (including staging, if used for validation)
- Endpoint inventory and **classification** (public vs restricted)
- A machine-readable **service contract**, where applicable:
    - REST: OpenAPI 3.x
    - GraphQL: schema (SDL/introspection export)
    - SPARQL: endpoint URL + declared feature envelope
- Versioning information (how versions are expressed and announced)
- If restricted: authentication/authorisation integration notes (project federated AAI where applicable) and expected access model

### Recommended evidence
- Smoke test plan (critical endpoints + expected responses)
- Release notes/changelog (for the evaluated version)
- Synthetic monitoring checks (availability probes)
- Evidence of “fail closed” behaviour for restricted endpoints
- Telemetry accessibility details (how federation analytics can query basic operational signals, if applicable)


## Validation classes and what they test

Validation typically combines:
- **Static checks** (specification, schema, and documentation inspection)
- **Dynamic checks** (runtime probing, contract conformance tests)
- **Operational checks** (health/readiness, resilience behaviour, monitorability)
- **Supervised/manual checks** (only where UI workflows or human confirmation is necessary)


## L1 validation (baseline)

### What to confirm (typical)
- **TLS enforcement** for externally reachable endpoints
- Clear endpoint inventory and access classification
- Content negotiation behaves predictably (media types, UTF‑8 handling)
- Deterministic error behaviour for invalid requests (at minimum: consistent status codes)

### Runtime test ideas (tool-agnostic)
- HTTP → confirm redirect/reject to HTTPS
- Request representative endpoints with `Accept` headers -verify declared content types
- Send invalid input → verify predictable error response payload exists


## L2 validation (contract + behaviour)

### Static checks (typical)
- Contract exists and is parseable (OpenAPI/GraphQL schema as applicable)
- Versioning scheme is documented and consistent with runtime
- Deprecation approach is documented (how breaking changes are announced and handled)
- Contract evolution discipline: no silent breaking changes within a published compatibility boundary

### Dynamic checks (typical)
- Contract conformance tests pass (endpoint presence + response shape)
- Predictable error model (deterministic codes + machine-readable error identifiers where defined)
- Pagination/limits for collection endpoints (bounded results)
- Health/readiness endpoints behave as documented (where required)
- Basic timeouts/resilience patterns exist for dependent calls (where applicable)

### Restricted services (additional checks)
If the service has restricted endpoints:
- Authentication works end-to-end for a test user (project federated AAI where applicable)
- Token validation is correct (issuer/audience/signature/expiry; bounded clock skew)
- Authorisation enforcement is consistent and **fails closed**
- Public vs restricted classification is respected (no leakage via alternate endpoints)


## Evidence examples (what “good” looks like)

Include at least:
- The contract file(s) with a version tag (or explicit commit hash)
- Machine output from contract linting/validation
- Contract-vs-runtime probe outputs (requests + summarized results)
- For restricted endpoints: redacted auth flow traces and negative tests
- An access matrix test summary (what is public vs restricted, and expected 401/403 behaviour)


## Output: conformance report

The API/service conformance report should include:
- Service id, version, base URL(s)
- Endpoint inventory (public/restricted)
- Applied validation classes (static/dynamic/operational/manual)
- Requirement-by-requirement results (using the project REQ-* identifiers where applicable)
- Failure details (actual vs expected) and remediation guidance
- Evidence pointers (logs, reports, artefacts) that are archived and reproducible

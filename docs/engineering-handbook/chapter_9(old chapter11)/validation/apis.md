# API and service validation (D6.2 Chapter 9 — resource type: APIs/services)

This page provides implementation guidance for validating APIs/services against the normative rules in D6.2 Chapter 9 (§9.3.2).

---

## Inputs (evidence package)

Minimum:
- service identifier + runtime base URL(s)
- endpoint inventory (public vs restricted classification)
- OpenAPI 3.x contract (for L2+ APIs where applicable)
- versioning and deprecation policy docs (for L2+)
- if restricted: AAI integration evidence (EGI Check-in), token validation behaviour summary

Recommended:
- smoke test plan
- synthetic monitoring checks (critical endpoints)
- release notes + changelog
- evidence of fail-closed behaviour and authz tests for restricted endpoints

---

## L1 — dynamic checks

Checklist:
- [ ] HTTPS/TLS enforcement (SEC-01)
- [ ] Media types and UTF-8 behaviour (REQ-API-005/006)
- [ ] Endpoint classification evidence (SEC-03)
- [ ] Service description and identifier (REQ-API-001)

Runtime test ideas (tool-agnostic):
- request HTTP → confirm redirect/reject to HTTPS
- request representative endpoint with Accept headers → verify content type
- send invalid input → verify error response exists and is deterministic

---

## L2 — static + dynamic checks

Static checklist:
- [ ] OpenAPI contract exists and parses (REQ-API-002)
- [ ] Versioning scheme documented (REQ-API-013)
- [ ] Deprecation policy documented (REQ-API-014)
- [ ] No breaking changes within a major version (REQ-API-015) (contract diff or release evidence)

Dynamic checklist:
- [ ] Contract conformance tests pass (REQ-API-003)
- [ ] Deterministic error model tests (REQ-API-007)
- [ ] Pagination for collection endpoints (REQ-API-010)
- [ ] Health/readiness behave as documented (REQ-API-016/017)
- [ ] Timeouts/resilience where applicable (REQ-DEP-003)

Restricted services (dynamic) checklist:
- [ ] EGI Check-in integration for authentication (SEC-04)
- [ ] Token validation correctness (SEC-07: issuer/audience/expiry/signature)
- [ ] Authorisation enforcement consistency (SEC-09)
- [ ] Fail-closed behaviour when policy cannot be evaluated (SEC-11)

Evidence examples:
- OpenAPI file with version tag
- endpoint-by-endpoint contract probe outputs
- auth flow logs/redacted traces
- explicit “public vs restricted” access matrix test results

---

## Output expectations

The API/service conformance report should include:
- base URL(s), version, and endpoint inventory
- applied requirement IDs and per-requirement status
- failure details (actual vs expected) for dynamic checks
- links to logs/test runs used as evidence

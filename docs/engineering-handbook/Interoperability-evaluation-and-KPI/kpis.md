# KPI Catalogue

This page defines the **living KPI catalogue** used by ECHOES to evaluate and monitor interoperability across CH Cloud resources.
It complements **D6.2 Evaluation and monitoring interoperability Chapter** by providing a practical, operator-friendly set of indicators and worked examples that can be maintained and evolved without expanding the deliverable.

KPIs are derived from interoperability obligations (documentation and evidence, API contracts and behaviour, security/AAI integration, metadata quality, semantic conformance, operations and governance). They are used for:

- **Onboarding evaluation** (initial level assignment at L1/L2/L3)
- **Continuous monitoring** (detection of drift and regressions after onboarding)
- **Evidence-based reassessment** (when releases, policies, or dependencies change)

## How to use this page

1. **Identify resource type(s)** (dataset, API/service, workflow, semantic artefact).
2. **Select applicable KPIs** using the “Applies” and “Level” columns below.
3. **Collect evidence** (automated test output where possible; otherwise documented manual checks).
4. **Assign / confirm the interoperability level** based on KPI results and the level-gating rules.
5. **Re-evaluate** on change events (release, schema/profile updates, policy updates, dependency upgrades, persistent failures).


## KPI semantics

### Status values
- **PASS**: requirement intent satisfied and evidence is recorded.
- **FAIL**: requirement intent not satisfied (or evidence shows non-conformance).
- **N/A**: KPI not applicable to this resource (document why).
- **UNKNOWN**: evaluation not possible due to missing evidence (treated as FAIL for level gating).

### Criticality classes
- **BLOCKING (onboarding)**: failing this KPI prevents onboarding of the resource into the federation (or triggers immediate suspension where relevant).
- **Blocking (level assignment)**: failing this KPI prevents assignment at the claimed level (e.g., L2/L3), but may allow L1 where applicable.
- **Mandatory**: required when applicable for the stated level/type.
- **Recommended**: strengthens robustness and drift detection; should be implemented where feasible.

### Evidence rule (non-negotiable)
A KPI MUST NOT be marked PASS without evidence. If level-required evidence is missing, the resource is **capped at L1** until the missing evidence is provided and validated.

## Evaluation and monitoring lifecycle

- **Onboarding**: run the applicable KPI suite and publish a conformance report (summary + evidence links).
- **Routine monitoring**: run operational/security checks continuously; run conformance drift checks on schedule (e.g., nightly/weekly).
- **Change-triggered revalidation**: re-run the KPI suite after releases, schema/profile changes, policy changes, or dependency upgrades.
- **Incident-driven reassessment**: repeated failures (availability, auth failures, semantic failures) trigger escalation and potential downgrade.

## KPI catalogue


### Documentation and specification KPIs

| KPI ID | KPI Name | Definition | Applies | Level | Criticality | Typical evidence |
|---|---|---|---|---|---|---|
| KPI-DOC-01 | Documentation completeness | Required provider artefacts are present (service/dataset description, ownership/contact, access model, versioning, user-facing notes) | All resource types | L1+ | Mandatory | published docs; onboarding package; links to specifications |
| KPI-DOC-02 | Machine-readable API specification | OpenAPI 3.x is provided and syntactically valid | APIs/services | L2+ | Mandatory | OpenAPI file + validator output |
| KPI-DOC-03 | Machine-readable schemas/shapes | JSON Schema / XSD / SHACL artefacts are present where applicable and reachable | Datasets/APIs/Semantic | L2+ (when applicable) | Mandatory (when applicable) | schema/shapes artefacts + validation output |

**Measurement guidance:** Documentation/specification KPIs are typically **PASS/FAIL** .

### Security and AAI KPIs

| KPI ID | KPI Name | Definition | Applies | Level | Criticality | Typical evidence |
|---|---|---|---|---|---|---|
| KPI-SEC-01 | TLS enforcement | All externally reachable endpoints use HTTPS with valid certificates | All network services | L1+ | **BLOCKING (onboarding)** | TLS scan output; curl/openssl evidence; certificate lifecycle statement |
| KPI-SEC-02 | Federated authentication | Federated authentication works for protected services (project AAI: **EGI Check-in**) | Restricted services | L2+ | Blocking (level assignment) | successful OIDC flow traces; test user authentication logs |
| KPI-SEC-03 | Token validation correctness | Issuer/audience/signature/expiry are validated consistently | Restricted services | L2+ | Blocking (level assignment) | negative/positive token tests; config evidence; bounded skew statement |
| KPI-SEC-04 | Authorisation enforcement | Access control decisions are consistent across endpoints and fail closed | Restricted resources | L2+ | Blocking (level assignment) | authz tests; policy enforcement point statement; denied-by-default evidence |

**Measurement guidance:** KPI-SEC-01 blocks onboarding. KPI-SEC-02–04 block **L2/L3 assignment** for protected resources.

### API behaviour KPIs

| KPI ID | KPI Name | Definition | Applies | Level | Criticality | Typical evidence |
|---|---|---|---|---|---|---|
| KPI-API-01 | Endpoint availability | API responds correctly over a defined sampling period | APIs/services | L1+ | Mandatory | uptime/availability report; synthetic probe results |
| KPI-API-02 | Predictable error handling | Errors return deterministic status codes + machine-readable error identifiers | APIs/services | L2+ | Mandatory | contract tests; error payload samples; negative test output |
| KPI-API-03 | Pagination and filtering | Collection endpoints support bounded results and basic filtering | APIs/services | L2+ | Mandatory | conformance tests; OpenAPI evidence; sample calls |
| KPI-API-04 | Versioning discipline | Versions are explicit; breaking changes create a new major version and are announced | APIs/services | L2+ | Mandatory | changelog; versioned endpoints; deprecation notice evidence |

**Measurement guidance:** KPI-API-01 is quantitative; KPI-API-02–04 are typically PASS/FAIL from conformance tests.

### Data and metadata quality KPIs

| KPI ID | KPI Name | Definition | Applies | Level | Criticality | Typical evidence |
|---|---|---|---|---|---|---|
| KPI-DATA-01 | Identifier stability | Persistent identifiers remain stable across releases (no silent replacement) | Datasets/APIs | L1+ | Mandatory | identifier policy; diff reports; persistent URI checks |
| KPI-DATA-02 | Schema/profile conformance | Payloads conform to the declared schema/profile | Datasets/APIs | L2+ | Mandatory | validator output; sample payloads; CI test output |
| KPI-DATA-03 | Rights metadata presence | Licence/reuse conditions are present and unambiguous | All resources | L1+ | **BLOCKING (onboarding)** | metadata fields; licence URL; rights statement |
| KPI-DATA-04 | Provenance separation | Derived/enriched data are distinguishable from source | Datasets/workflows | L2+ (when applicable) | Mandatory (when applicable) | provenance documentation; workflow outputs; PROV references |

### Semantic integration KPIs (L2/L3)

| KPI ID | KPI Name | Definition | Applies | Level | Criticality | Typical evidence |
|---|---|---|---|---|---|---|
| KPI-SEM-01 | JSON-LD validity | JSON-LD expands correctly; contexts resolve; terms map to stable IRIs | Datasets/APIs | L2+ (when JSON-LD is used) | Mandatory (when applicable) | context resolvability report; expansion determinism report |
| KPI-SEM-02 | Vocabulary linkage | Controlled terms use resolvable identifiers; vocabulary versioning is explicit | Datasets/Semantic | L2+ (when used) | Mandatory (when applicable) | URI checks; vocabulary lint report; mapping checks |
| KPI-SEM-03 | RDF graph availability | RDF representations are available and linkable where declared | Datasets/APIs | L3 (when declared) | Mandatory (when applicable) | RDF endpoint checks; graph availability evidence |
| KPI-SEM-04 | Constraint validation | SHACL validation passes for declared shapes | Datasets/Semantic | L3 (when declared) | Mandatory (when applicable) | SHACL validation report; reproducible run evidence |

> **Implementation guidance:** see `semantic-monitoring.md` for non-binding operational routines aligned with KPI-SEM-*.

### Operational KPIs

| KPI ID | KPI Name | Definition | Applies | Level | Criticality | Typical evidence |
|---|---|---|---|---|---|---|
| KPI-OPS-01 | Health endpoints | `/health` and `/ready` expose deterministic status | Services | L2+ | Mandatory | probe results; endpoint definitions; alert rules |
| KPI-OPS-02 | Response time | Latency remains within declared thresholds (where thresholds exist) | APIs/services | L2+ | Mandatory (where thresholds exist) | p95 latency series; SLO statement; incident history |
| KPI-OPS-03 | Error rate | Error rate remains within declared thresholds (where thresholds exist) | APIs/services | L2+ | Mandatory (where thresholds exist) | 4xx/5xx rate metrics; alerts; ticket summaries |
| KPI-OPS-04 | Dependency resilience | Timeouts/retries prevent cascading failures | Services/workflows | L2+ | Recommended | retry policy; circuit breaker config; failure-injection evidence |

### Governance KPIs

| KPI ID | KPI Name | Definition | Applies | Level | Criticality | Typical evidence |
|---|---|---|---|---|---|---|
| KPI-GOV-01 | Ownership declared | Owner and steward are explicitly defined and reachable | All resources | L1+ | Mandatory | owner/steward metadata; escalation contact |
| KPI-GOV-02 | Policy enforcement consistency | Declared access policy matches technical enforcement | Restricted resources | L2+ | Mandatory | policy statement; authz tests; enforcement evidence |
| KPI-GOV-03 | Change transparency | Breaking changes are announced, versioned, and traceable | All resources | L2+ | Mandatory | changelog; release notes; deprecation notices |

## Level assignment and scoring 

1. **Blocking KPIs:** If a blocking KPI fails, the resource SHALL NOT be onboarded (or SHALL be downgraded), as applicable.
2. **Highest achievable level:** The assignable level is the highest level for which all **mandatory applicable KPIs** pass.
3. **Evidence gate:** Missing evidence caps the resource at **L1** until evidence is provided and validated.
4. **Drift detection:** re-evaluate KPIs after releases, schema/profile changes, policy changes, dependency upgrades, or persistent monitoring failures.

## Worked evaluation scenarios

### A) Dataset with open access (target L2)
- Expected PASS at minimum: KPI-DOC-01, KPI-DATA-03, KPI-DATA-02, KPI-SEC-01.
- If JSON-LD is used: KPI-SEM-01 applies.
- Outcome: L2 is assignable if all L2-mandatory applicable KPIs pass with evidence.

### B) Restricted API service (target L2)
- Expected PASS at minimum: KPI-SEC-01, KPI-SEC-02, KPI-SEC-03, KPI-SEC-04, KPI-API-02.
- Outcome: failure of any KPI-SEC-02–04 prevents L2 assignment for this protected service.

### C) Semantic artefact / knowledge model (target L3)
- Expected PASS where declared: KPI-DOC-03, KPI-SEM-03, KPI-SEM-04.
- Outcome: L3 is assignable only if declared RDF/SHACL assets are stable, accessible, and validate reproducibly.


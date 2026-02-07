# KPI Catalogue

This page defines the living KPI catalogue used by ECHOES to evaluate and monitor interoperability across CH Cloud resources.
It complements the D6.2 deliverable, interoperability requirements, evaluation and monitoring, validation and conformance testing, governance and compliance, by providing an operator‑friendly KPI set that can evolve without expanding the deliverable.

KPIs are derived from interoperability obligations in the project and are used for:

- onboarding evaluation, initial level assignment at L1, L2, L3
- continuous monitoring, detection of drift and regressions after onboarding
- evidence‑based reassessment, after releases, schema and profile updates, policy changes, or material dependency changes

## How to use this page

1. Identify the resource type or types, dataset, API and service, workflow, semantic artefact, application.
2. Select applicable KPIs using Applies and Level, only evaluate what applies.
3. Collect evidence, automated test output where possible, otherwise documented manual checks.
4. Assign or confirm the interoperability level based on KPI results and the level‑gating rules below.
5. Re‑evaluate on change events and persistent monitoring alerts.

## KPI semantics

### Status values

- PASS: requirement intent satisfied and evidence is recorded
- FAIL: requirement intent not satisfied, or evidence shows non‑conformance
- N and A: KPI does not apply to the resource, document why
- UNKNOWN: evaluation not possible due to missing evidence, treated as FAIL for level gating

### Criticality classes

- BLOCKING, onboarding: failing this KPI prevents onboarding, or triggers suspension where relevant
- Blocking, level assignment: failing this KPI prevents assignment at the claimed level, for example L2 and L3, but may allow L1 where applicable
- Mandatory: required when applicable for the stated level and type
- Recommended: strengthens robustness and drift detection, implement where feasible

### Evidence rule

A KPI MUST NOT be marked PASS without evidence.
If level‑required evidence is missing, the resource is capped at L1 until evidence is provided and validated.

## Privacy and ethics

When KPI evidence or telemetry involves user interaction data:

- apply data minimisation, only what is necessary for evaluation
- prefer pseudonymous identifiers for authenticated users, OIDC `sub`
- ensure guest submissions remain anonymous where required

Any collection of user feedback MUST be preceded by an informed consent notice and follow the project’s governance and retention rules.

## Evaluation and monitoring lifecycle

- onboarding: run the applicable KPI suite and publish a conformance report, summary plus evidence links
- routine monitoring: run operational and security checks continuously; run conformance drift checks on schedule, for example nightly or weekly
- change‑triggered revalidation: re‑run the KPI suite after releases, schema and profile changes, policy changes, or dependency upgrades
- incident‑driven reassessment: repeated failures trigger escalation and potential downgrade

## KPI catalogue

### Documentation and specification KPIs

| KPI ID | KPI Name | Definition | Applies | Level | Criticality | Typical evidence |
|---|---|---|---|---|---|---|
| KPI‑DOC‑01 | Documentation completeness | Required provider artefacts are present, description, ownership and contact, access model, versioning, user notes | All resource types | L1+ | Mandatory | published docs; onboarding package; links to specs |
| KPI‑DOC‑02 | Machine‑readable API specification | OpenAPI 3.x is provided and syntactically valid | APIs and services | L2+ | Mandatory | OpenAPI file plus validator output |
| KPI‑DOC‑03 | Machine‑readable schemas and shapes | JSON Schema, XSD, SHACL artefacts are present where applicable and reachable | Datasets, APIs, semantic | L2+ when applicable | Mandatory when applicable | artefacts plus validation output |

### Security and AAI KPIs

| KPI ID | KPI Name | Definition | Applies | Level | Criticality | Typical evidence |
|---|---|---|---|---|---|---|
| KPI‑SEC‑01 | TLS enforcement | All externally reachable endpoints use HTTPS with valid certificates | All network services | L1+ | BLOCKING onboarding | TLS scan output; curl and openssl evidence |
| KPI‑SEC‑02 | Federated authentication | Federated authentication works for protected services, project AAI, EGI Check‑in | Restricted services | L2+ | Blocking level assignment | OIDC flow traces; test user logs |
| KPI‑SEC‑03 | Token validation correctness | Issuer, audience, signature, expiry are validated consistently | Restricted services | L2+ | Blocking level assignment | positive and negative token tests; config evidence |
| KPI‑SEC‑04 | Authorisation enforcement | Access control decisions are consistent across endpoints and fail closed | Restricted resources | L2+ | Blocking level assignment | authz tests; enforcement evidence |

### API behaviour KPIs

| KPI ID | KPI Name | Definition | Applies | Level | Criticality | Typical evidence |
|---|---|---|---|---|---|---|
| KPI‑API‑01 | Endpoint availability | API responds correctly over a defined sampling period | APIs and services | L1+ | Mandatory | probe results; availability report |
| KPI‑API‑02 | Predictable error handling | Errors return deterministic status codes plus machine‑readable error identifiers | APIs and services | L2+ | Mandatory | contract tests; error samples |
| KPI‑API‑03 | Pagination and filtering | Collection endpoints support bounded results and basic filtering | APIs and services | L2+ | Mandatory | conformance tests; OpenAPI evidence |
| KPI‑API‑04 | Versioning discipline | Versions are explicit; breaking changes create a new major version and are announced | APIs and services | L2+ | Mandatory | changelog; versioned endpoints; deprecation notices |

### Data and metadata quality KPIs

| KPI ID | KPI Name | Definition | Applies | Level | Criticality | Typical evidence |
|---|---|---|---|---|---|---|
| KPI‑DATA‑01 | Identifier stability | Persistent identifiers remain stable across releases, no silent replacement | Datasets, APIs | L1+ | Mandatory | identifier policy; diff reports |
| KPI‑DATA‑02 | Schema and profile conformance | Payloads conform to the declared schema and profile | Datasets, APIs | L2+ | Mandatory | validator output; CI test logs |
| KPI‑DATA‑03 | Rights metadata presence | Licence and reuse conditions are present and unambiguous | All resources | L1+ | BLOCKING onboarding | licence URI; rights statement |
| KPI‑DATA‑04 | Provenance separation | Derived and enriched data are distinguishable from source | Datasets, workflows | L2+ when applicable | Mandatory when applicable | provenance docs; workflow outputs |

### Semantic integration KPIs

| KPI ID | KPI Name | Definition | Applies | Level | Criticality | Typical evidence |
|---|---|---|---|---|---|---|
| KPI‑SEM‑01 | JSON‑LD validity | JSON‑LD expands correctly; contexts resolve; terms map to stable IRIs | Datasets, APIs | L2+ when JSON‑LD used | Mandatory when applicable | context checks; expansion determinism report |
| KPI‑SEM‑02 | Vocabulary linkage | Controlled terms use resolvable identifiers; vocabulary versioning is explicit | Datasets, semantic | L2+ when used | Mandatory when applicable | URI checks; vocabulary lint report |
| KPI‑SEM‑03 | RDF graph availability | RDF representations are available and linkable where declared | Datasets, APIs | L3 when declared | Mandatory when applicable | graph availability checks |
| KPI‑SEM‑04 | Constraint validation | SHACL validation passes for declared shapes | Datasets, semantic | L3 when declared | Mandatory when applicable | SHACL validation report |

Operational routines and drift detection guidance for the semantic KPIs are maintained in `semantic-monitoring.md`.

### Operational KPIs

| KPI ID | KPI Name | Definition | Applies | Level | Criticality | Typical evidence |
|---|---|---|---|---|---|---|
| KPI‑OPS‑01 | Health endpoints | `/health` and `/ready` expose deterministic status | Services | L2+ | Mandatory | probe results; endpoint definitions |
| KPI‑OPS‑02 | Response time | Latency remains within declared thresholds, where thresholds exist | APIs, services | L2+ | Mandatory where thresholds exist | p95 latency series; SLO statement |
| KPI‑OPS‑03 | Error rate | Error rate remains within declared thresholds, where thresholds exist | APIs, services | L2+ | Mandatory where thresholds exist | 4xx and 5xx rate metrics; alerts |
| KPI‑OPS‑04 | Dependency resilience | Timeouts and retries prevent cascading failures | Services, workflows | L2+ | Recommended | retry policy; failure tests |
| KPI‑OPS‑05 | Telemetry accessibility | ECHOES analytics can query telemetry via an observability interface, endpoint or secure access to existing OTLP or API streams. Baseline L2+ signals are available using agreed naming. | APIs, services, applications | L2+ | Mandatory | endpoint URL plus auth method; sample query and response; collector access confirmation |

Baseline L2+ telemetry signals, reference: response_time, throughput, error_rate, system_uptime, active_users, aggregate or pseudonymous, auth_success_rate for protected resources, access_frequency, licensing_compliance.

### Governance KPIs

| KPI ID | KPI Name | Definition | Applies | Level | Criticality | Typical evidence |
|---|---|---|---|---|---|---|
| KPI‑GOV‑01 | Ownership declared | Owner and steward are explicitly defined and reachable | All resources | L1+ | Mandatory | owner and steward metadata; escalation contact |
| KPI‑GOV‑02 | Policy enforcement consistency | Declared access policy matches technical enforcement | Restricted resources | L2+ | Mandatory | policy statement; authz tests |
| KPI‑GOV‑03 | Change transparency | Breaking changes are announced, versioned, and traceable | All resources | L2+ | Mandatory | changelog; release notes |
| KPI‑GOV‑04 | Evaluation readiness | Feedback capture is integrated, visible trigger plus consent plus correct pseudonymous or anonymous handling, and telemetry is accessible to the ECHOES analytics framework. | Applications and app‑like services | L2+ | Mandatory | UI walkthrough or scripted test; consent text; network trace to survey endpoint; telemetry sample response |

## Level assignment and scoring

1. Blocking KPIs: if a blocking KPI fails, the resource SHALL NOT be onboarded, or SHALL be downgraded.
2. Highest achievable level: the assignable level is the highest level for which all mandatory applicable KPIs pass.
3. Evidence gate: missing evidence caps the resource at L1 until evidence is provided and validated.
4. Drift detection: re‑evaluate KPIs after releases, schema and profile changes, policy changes, dependency upgrades, or persistent monitoring failures.

## Worked evaluation scenarios

### A) Dataset with open access, target L2

- Minimum expected PASS: KPI‑DOC‑01, KPI‑DATA‑03, KPI‑DATA‑02, KPI‑SEC‑01.
- If JSON‑LD is used: KPI‑SEM‑01 applies.

### B) Restricted API service, target L2

- Minimum expected PASS: KPI‑SEC‑01, KPI‑SEC‑02, KPI‑SEC‑03, KPI‑SEC‑04, KPI‑API‑02.

### C) Semantic artefact and knowledge model, target L3

- Expected PASS where declared: KPI‑DOC‑03, KPI‑SEM‑03, KPI‑SEM‑04.

### D) Application integrated into the evaluation framework, target L2

- Minimum expected PASS: KPI‑SEC‑01, KPI‑DATA‑03, KPI‑GOV‑04, KPI‑OPS‑05.

## Document control

This is living documentation.
Updates should be proposed via change control, PR, and preserve:

- stable KPI IDs
- clear applicability and level gating
- evidence requirements
- backwards compatibility notes where KPI semantics evolve

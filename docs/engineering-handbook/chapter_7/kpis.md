# Interoperability Evaluation Framework and KPI Catalogue (D6.2 §7.1)

This page contains the **Living Documentation** version of the KPI catalogue and worked examples referenced from **D6.2 §7.1**.

**What stays normative in the PDF:** evaluation principles, required evidence types, scoring rules, and required outputs.  
**What lives here:** the KPI catalogues (tables) and worked evaluation scenarios, because KPI selection per resource type, KPI thresholds, and measurement cadence are maintained via validation governance while remaining traceable to D6.2 obligations.

---

## 7.1.4 Core Conformance KPI Definitions

The KPIs below are derived from interoperability obligations in D6.2 (documentation, API contracts, security/AAI integration, metadata quality, semantic conformance) and are intended for onboarding evaluation and continuous monitoring. KPI selection, thresholds, and cadence are maintained via the project validation governance process.

### 7.1.4.1 Documentation and Specification KPIs

| KPI ID | KPI Name | Definition | Applies | Level |
|---|---|---|---|---|
| KPI-DOC-01 | Documentation completeness | Required provider documentation artefacts are present (D6.2 §5.7) | All resource types | L1+ |
| KPI-DOC-02 | Machine-readable API spec | OpenAPI 3.x is provided and syntactically valid | APIs/services | L2+ |
| KPI-DOC-03 | Machine-readable schemas | JSON Schema / XSD / SHACL artefacts are present where applicable | Datasets/APIs/Semantic | L2+, L3 |

**Measurement rule:** A KPI in this category is evaluated as **PASS/FAIL**.

### 7.1.4.2 Security and AAI KPIs

| KPI ID | KPI Name | Definition | Applies | Level |
|---|---|---|---|---|
| KPI-SEC-01 | TLS enforcement | All endpoints use HTTPS with valid certificates | All network services | L1+ |
| KPI-SEC-02 | Federated authentication | EGI Check-in authentication works for protected services | Restricted services | L2+ |
| KPI-SEC-03 | Token validation correctness | Issuer/audience/signature/expiry are validated | Restricted services | L2+ |
| KPI-SEC-04 | Authorisation enforcement | Access control decisions are consistent across endpoints | Restricted resources | L2+ |

**Measurement rule:** Failure of **KPI-SEC-01** blocks onboarding. Failure of **KPI-SEC-02–04** blocks L2/L3 assignment.

### 7.1.4.3 API Behaviour KPIs

| KPI ID | KPI Name | Definition | Applies | Level |
|---|---|---|---|---|
| KPI-API-01 | Endpoint availability | API responds correctly over a defined sampling period | APIs/services | L1+ |
| KPI-API-02 | Predictable error handling | Errors return deterministic codes + machine-readable error IDs | APIs/services | L2+ |
| KPI-API-03 | Pagination and filtering | Collection endpoints support bounded results and filters | APIs/services | L2+ |
| KPI-API-04 | Versioning discipline | API versions are explicit; breaking changes create new major versions | APIs/services | L2+ |

**Measurement rule:** **KPI-API-01** is measured quantitatively (availability %). Others are **PASS/FAIL** based on tests.

### 7.1.4.4 Data and Metadata Quality KPIs

| KPI ID | KPI Name | Definition | Applies | Level |
|---|---|---|---|---|
| KPI-DATA-01 | Identifier stability | Persistent identifiers remain stable across releases | Datasets/APIs | L1+ |
| KPI-DATA-02 | Schema conformance | Payloads conform to declared schema/profile | Datasets/APIs | L2+ |
| KPI-DATA-03 | Rights metadata presence | Licence/reuse conditions are present and unambiguous | All resources | L1+ |
| KPI-DATA-04 | Provenance separation | Derived/enriched data distinguishable from source | Datasets/workflows | L2+, L3 |

### 7.1.4.5 Semantic Integration KPIs (L2/L3)

| KPI ID | KPI Name | Definition | Applies | Level |
|---|---|---|---|---|
| KPI-SEM-01 | JSON-LD validity | JSON-LD expands correctly and contexts resolve | Datasets/APIs | L2+ |
| KPI-SEM-02 | Vocabulary linkage | Controlled terms use resolvable identifiers | Datasets/Semantic | L2+, L3 |
| KPI-SEM-03 | RDF graph availability | RDF representations are available and linkable | Datasets/APIs | L3 |
| KPI-SEM-04 | Constraint validation | SHACL validation passes for declared shapes | Datasets/Semantic | L3 |

---

## 7.1.5 Operational KPIs (Runtime and Federation Readiness)

Operational KPIs measure whether a resource remains reliably usable in federated environments.

| KPI ID | KPI Name | Definition | Applies | Level |
|---|---|---|---|---|
| KPI-OPS-01 | Health endpoint | `/health` and `/ready` expose deterministic status | Services | L2+ |
| KPI-OPS-02 | Mean response time | API latency remains within declared thresholds | APIs/services | L2+ |
| KPI-OPS-03 | Error rate | Error rate remains within declared thresholds | APIs/services | L2+ |
| KPI-OPS-04 | Dependency resilience | Timeouts/retries prevent cascading failures | Services/workflows | L2, L3 |

**Measurement rule:** Operational KPIs are measured over defined intervals (e.g., rolling window) and reported as **quantitative indicators**.

---

## 7.1.6 Governance KPIs (Access and Reuse Consistency)

Governance KPIs assess whether declared policies match runtime behaviour.

| KPI ID | KPI Name | Definition | Applies | Level |
|---|---|---|---|---|
| KPI-GOV-01 | Ownership declared | Owner and steward are explicitly defined | All resources | L1+ |
| KPI-GOV-02 | Policy enforcement consistency | Access policy matches technical enforcement | Restricted resources | L2+ |
| KPI-GOV-03 | Change transparency | Breaking changes announced and versioned | All resources | L2+ |

---

## 7.1.7 KPI Thresholds and Scoring Rules (mandatory, for reference)

Interoperability scoring follows these rules:

1. **Blocking KPIs:** If a blocking KPI fails, the resource must not be onboarded (or is downgraded).
    - Blocking KPIs include (at minimum): TLS enforcement, authentication correctness for protected resources, absence of licence metadata.
2. **Level assignment:** The highest level assignable is the highest level for which all mandatory KPIs pass.
3. **Evidence requirement:** No KPI may be counted as PASS without evidence.
4. **Drift detection:** KPIs are re-evaluated when:
    - a new version is released,
    - schemas or policies change,
    - dependencies change materially,
    - persistent validation failures occur.

---

## 7.1.8 Worked Evaluation Scenarios (Examples A–C)

These examples illustrate application of the framework.

### Example A: Dataset with open access (target L2)

- Provider supplies JSON-LD metadata and declares licence.
- Validation checks:
    - KPI-DOC-01 PASS (docs present)
    - KPI-SEM-01 PASS (JSON-LD expands)
    - KPI-DATA-02 PASS (schema conformance)
    - KPI-SEC-01 PASS (TLS)
    - KPI-GOV-01 PASS (ownership declared)
- Result: dataset qualifies for L2 if all L2-mandatory items pass.

### Example B: Restricted API service (target L2)

- Provider integrates authentication with EGI Check-in.
- Validation checks:
    - KPI-SEC-02 PASS (EGI Check-in flow works)
    - KPI-SEC-03 PASS (token validation correct)
    - KPI-SEC-04 PASS (authorisation enforced)
    - KPI-API-02 PASS (error format deterministic)
- Result: service qualifies for L2; failure in any security KPI blocks L2.

### Example C: Semantic artefact (target L3)

- Provider supplies OWL ontology and SHACL shapes.
- Validation checks:
    - KPI-SEM-03 PASS (RDF accessible)
    - KPI-SEM-04 PASS (SHACL validation passes)
    - KPI-DOC-03 PASS (machine-readable schemas/shapes present)
- Result: semantic artefact qualifies for L3 if all mandatory L3 KPIs pass.

---

## 7.1.9 Outputs of the Evaluation Framework (mandatory, for reference)

The evaluation process produces:
- level assignment (L1/L2/L3),
- conformance report listing KPI results and evidence,
- remediation guidance for failed checks,
- periodic monitoring records for drift over time.

These outputs feed:
- validation and conformance testing (D6.2 §12),
- interoperability maturity assessment (D6.2 §7.4),
- governance and compliance audits.

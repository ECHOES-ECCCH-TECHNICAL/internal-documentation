# Validation Artefacts

This page defines the **artefact types** typically used for interoperability validation and describes the checks that can be applied to them.
It is written as living documentation to support consistent evidence collection across providers.

A good evidence package is:

- **versioned** (tied to a release or immutable identifier),
- **reproducible** (can be re-run and produce comparable outputs),
- **auditable** (includes inputs, tool versions, and outputs),
- **minimal** (no sensitive data unless strictly necessary, and redacted where possible).


## 1) Metadata artefacts

Examples:

- JSON / JSON‑LD / XML metadata records
- Profile/schema declarations
- JSON‑LD contexts (`@context`) and referenced vocabularies

Typical checks:

- required fields present (identifier, licence, owner/contact, version where applicable)
- identifier format and stability rules (and resolvability where intended)
- JSON‑LD context resolvability and deterministic expansion (for representative payloads)

Expected outputs:

- PASS/FAIL summary
- error list with paths/fields
- archived sample payloads used for validation


## 2) Structural artefacts (schemas and constraints)

Examples:

- JSON Schema (JSON payloads)
- XSD / Relax NG (XML payloads)
- CSVW metadata (tabular)
- SHACL shapes (RDF/semantic assets)

Typical checks:

- schema parses and is versioned
- validation is deterministic (same input → same result)
- profile/shape conformance (required fields, datatypes, constraints)

Expected outputs:

- validator output (pass/fail + error list)
- reference to the exact schema/shape version
- input sample(s) used


## 3) API artefacts (contracts and tests)

Examples:

- OpenAPI 3.x contract
- GraphQL schema export / introspection snapshot
- Contract conformance test suite (where maintained)
- Versioning + deprecation documentation

Typical checks:

- parse + lint contract (syntactic and basic semantic lint)
- contract-vs-runtime probes (endpoint presence + response shape)
- contract diff rules for breaking change detection (when comparing versions)

Expected outputs:

- lint output
- probe reports
- contract diff report between versions (when applicable)


## 4) Security artefacts (restricted access)

Examples:

- endpoint inventory/classification (public vs restricted)
- authentication integration evidence (federated AAI where applicable)
- token validation tests
- authorisation enforcement tests (access matrix)
- security logging policies and secrets handling statements

Typical checks:

- TLS enforcement
- auth flow checks for restricted endpoints
- token validation correctness (iss/aud/exp/signature)
- “fail closed” behaviour when policy cannot be evaluated

Expected outputs:

- redacted traces/logs that demonstrate flows
- negative test results (invalid token, expired token, insufficient scope/role)
- access matrix evidence (what is allowed and denied)


## 5) Evaluation and monitoring artefacts (feedback + telemetry)

Where resources participate in continuous evaluation and federated observability, evidence may include:

### Feedback mechanism artefacts (applications)
- UI trigger description (where the feedback entry point lives)
- informed consent text (as shown to users)
- payload definition (fields, pseudonymous/anonymous handling)
- network trace proving end-to-end submission to the central survey endpoint (e.g., HAR file, redacted logs)

### Telemetry accessibility artefacts (services/applications)
- observability interface description (endpoint, OTLP access, or delegated access to existing telemetry streams)
- authentication method for the analytics collector
- sample query + sample response proving the baseline signal set is reachable
- naming/units conventions and aggregation policy

Expected outputs:

- PASS/FAIL for accessibility
- sample payloads (redacted as needed)
- stored evidence that supports repeatable reassessment


## 6) Report artefacts (outputs)

Every validation run should produce:

- a conformance report (requirement-by-requirement)
- raw tool outputs (logs, lint reports, validation reports)
- a minimal evidence index (where artefacts are stored, checksums, timestamps)

# Tooling and CI Patterns 

This page is intentionally **tool‑agnostic**. Document the actual tools adopted in the repository (scripts, containers, CI jobs) and keep them current.
The aim is to make validation runs **reproducible** and **auditable** across providers and over time.


## Recommended repository layout

A common layout is:

```
/validation/
  scripts/
  schemas/
  shacl/
  openapi/
  examples/
  reports/
  inventories/
```

Recommendations:
- treat schemas/shapes/contracts as **versioned artefacts**
- store **example inputs** that are safe to share
- publish **reports** as CI artefacts (immutable, timestamped)


## CI integration patterns

### Static checks (on pull requests)
- schema validation (JSON Schema/XSD/SHACL linting where applicable)
- contract linting (OpenAPI/GraphQL schema parsing)
- link checking for contexts/vocabularies (where provider-controlled)

### Dynamic checks (on staging deployments)
- smoke tests for critical endpoints
- contract-vs-runtime probes
- restricted endpoint authn/authz tests (redacted logs)

### Operational checks (scheduled)
- availability probes and latency budgets
- drift detection baselines (especially for semantic assets)
- periodic evidence refresh (to keep compliance records current)


## Reproducibility rules of thumb

- Pin tool versions (container tags or explicit versions).
- Capture inputs (artefact versions, sample payloads) for every run.
- Store outputs (reports/logs) alongside metadata: timestamp, tool version, commit hash.
- Redact sensitive data (tokens, PII) and avoid storing raw secrets in reports.


## Publishing reports

Recommended practice:
- publish machine-readable report summaries (JSON) alongside human-readable reports (Markdown/PDF)
- keep a stable naming convention:
  - `reports/<resource-id>/<version>/<date>/report.md`
  - `reports/<resource-id>/<version>/<date>/raw/…`


## Troubleshooting patterns

- Keep a “known issues” section per validator (common errors and fixes).
- Provide example command lines for local runs.
- Use staged environments for dynamic tests to avoid disrupting production.

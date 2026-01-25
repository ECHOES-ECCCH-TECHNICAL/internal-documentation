# Validation artefacts and machine-testable rules (D6.2 §9.2)

This page lists artefact formats and provides example validators and expected outputs.

## Metadata artefacts
- JSON / JSON-LD / XML metadata records
- profile/schema declarations
- JSON-LD contexts (`@context`) where used

**Typical checks**
- required fields present (id, licence, contact, version)
- identifier format and resolvability (where applicable)
- JSON-LD context resolvability + deterministic expansion for representative payloads

## Structural artefacts
- JSON Schema (JSON payloads)
- XSD / RelaxNG (XML payloads)
- CSVW metadata (tabular)
- SHACL shapes (RDF assets)

**Typical checks**
- deterministic schema validation (pass/fail + errors)
- declared profile conformance

## API artefacts
- OpenAPI 3.x contract
- contract conformance test suite (where maintained)
- versioning + deprecation docs

**Typical checks**
- parse + lint OpenAPI
- contract-vs-runtime checks (endpoint presence + response shape)
- contract diff rules for breaking changes

## Security artefacts
- endpoint inventory/classification
- AAI integration evidence (restricted services)
- token validation test results
- authz enforcement tests
- security logging + secrets policies

**Typical checks**
- TLS enforcement
- auth flow checks for restricted endpoints
- token validation correctness (iss/aud/exp/signature)
- access matrix checks (public vs restricted)

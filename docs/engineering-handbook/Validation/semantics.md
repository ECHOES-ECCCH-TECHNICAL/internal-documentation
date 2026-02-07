# Semantic Validation

This page provides living guidance for validating **semantic artefacts** and semantic representations used in CH Cloud interoperability.
It supports the normative requirements defined in the **D6.2 deliverable** while focusing on how to assemble evidence and run checks reproducibly.


## Scope

Applies to:

- controlled vocabularies/thesauri (SKOS concept schemes),
- mappings and alignments (SKOS mapping relations, crosswalk files),
- ontologies/knowledge models (OWL, CIDOC‑CRM expressions/extensions),
- RDF graphs and SPARQL endpoints,
- SHACL shapes and constraint artefacts,
- JSON‑LD contexts and semantic metadata transformations.


## Inputs: evidence package

### Minimum evidence (must be provided)
- asset identifier + version
- authoritative location (URI) and distribution URL(s)
- declared dependencies/imports/references
- governance/maintenance contact
- change policy or changelog (where applicable)
- if L3 claimed: RDF + SHACL shapes + SHACL validation report

### Recommended evidence
- sentinel queries/checks (for SPARQL endpoints)
- drift monitoring outputs (trend reports, alerts)
- explicit URI deprecation policy (no silent disappearance)


## L2 validation (semantic hygiene and traceability)

Typical checks:

- versioning and change notes exist; maintenance contact is declared
- identifiers are stable; dereferenceable where provider-controlled and intended
- multilingual labels use language tags (where applicable)
- mappings are traceable to specific source/target versions (where mappings exist)
- JSON‑LD contexts resolve and representative payloads expand deterministically (where JSON‑LD used)

Common evidence:

- SKOS concept scheme with a version identifier/IRI
- mapping file that declares source/target versions and predicates used
- context resolvability proof + deterministic expansion sample output


## L3 validation (RDF + constraints + drift readiness)

Typical checks:

- RDF representation is available where declared
- SHACL shapes are provided, versioned, accessible, and validation output is reproducible
- URI stability/deprecation discipline exists (redirects, tombstones, or mapping plan)
- drift monitoring evidence exists where declared/required (broken URIs, SHACL trends, mapping drift)


Common evidence:

- SHACL shapes + validation output tied to exact input version
- monitoring reports: broken URIs list, SHACL trend pass/fail, mapping drift reports
- SPARQL sentinel query outputs (if endpoint is provided)


## Output: semantic conformance report (required)

The semantic conformance report should include:

- artefact locations + versions (vocabularies, mappings, contexts, shapes)
- validation outputs (SHACL reports, context expansion checks)
- drift monitoring evidence (if required by claimed level)
- remediation guidance and versioning/deprecation actions

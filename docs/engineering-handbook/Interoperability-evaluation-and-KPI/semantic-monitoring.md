# Semantic Monitoring

This page provides non‑binding operational guidance for semantic monitoring of CH Cloud resources.
It complements the semantic monitoring content in the D6.2 deliverable by describing practical routines for detecting drift and integrity failures in semantic assets.

Semantic failures are often silent: an endpoint may remain available while meaning, identifiers, or constraints change in ways that break interoperability across providers.

## Scope

Semantic monitoring applies when a resource uses or exposes semantic representations, including:

- JSON‑LD metadata and contexts, L2+
- controlled vocabularies and thesauri, typically SKOS, L2+
- mappings and alignments between semantic artefacts, L2 and L3
- ontologies and knowledge models, OWL, CIDOC‑CRM expressions and extensions, primarily L3
- RDF graphs and SPARQL endpoints, L3
- constraint artefacts, SHACL shapes, L3

## Relationship to KPIs

This page operationalises the semantic KPI set defined in `kpis.md`:

- KPI‑SEM‑01 - JSON‑LD validity, context resolvability, deterministic expansion
- KPI‑SEM‑02 - Vocabulary linkage, resolvable controlled terms, mapping checks where applicable
- KPI‑SEM‑03 - RDF graph availability, where RDF is declared
- KPI‑SEM‑04 - SHACL constraint validation, where shapes are declared

## Core monitoring goals

1. Detect semantic drift, changes that alter interpretation without an obvious outage
2. Detect integrity failures, broken URIs, invalid contexts, SHACL failures, ontology import issues
3. Ensure reproducibility, stable versions, traceable changes, reproducible validation outputs
4. Provide actionable remediation, clear owner, severity, and steps to restore conformance

## Inventory: what to track

Maintain a machine‑readable inventory of semantic assets in scope for monitoring.

Recommended fields:

- asset identifier and version, immutable where feasible
- authoritative location, URI, and distribution URL or URLs
- dependencies, imports, referenced contexts, mapping targets
- applicability, which datasets and services depend on it
- owner or steward contact and escalation route
- declared expectations, dereferenceable URIs, supported languages, expected shapes and features

Example, YAML:

```yaml
asset_id: VOC-EXAMPLE-001
type: skos_vocabulary
version: "1.2.0"
primary_uri: "https://example.org/vocab/"
distributions:
  - "https://example.org/vocab.ttl"
dependencies:
  - "https://example.org/context.jsonld"
owner:
  org: "Provider XYZ"
  contact: "semantic-ops@example.org"
expectations:
  dereferenceable_uris: true
  languages: ["en", "fr"]
```

Store inventories and outputs as versioned artefacts so changes are reviewable and auditable.

## Recommended monitoring signals

The signals below strengthen early detection beyond the mandatory baseline described in the deliverable.

| Signal category | Recommended checks | Typical outputs |
|---|---|---|
| Identifier and URI integrity | Detect 404 and 410; redirects that change identity; unexpected content negotiation changes | list of broken URIs; redirect diffs; HTTP evidence |
| JSON‑LD context and serialisation | Detect term remapping without versioning; undefined terms; non‑deterministic expansion | context resolution report; expansion diff |
| Vocabulary integrity, SKOS | BCP47 language tag checks; label hygiene; broader and narrower cycle detection | lint report; cycle list; missing label list |
| Mapping integrity | conflicting mappings; mapping cycles; coverage regression versus baseline | mapping diff; regression summary |
| Ontology integrity | import resolvability; pinned imports; optional reasoning checks when reasoning is declared | import report; inconsistency report |
| SHACL integrity | shape drift without version bump; inconsistent target usage; validation performance regressions | SHACL report; runtime stats |
| SPARQL integrity | sentinel ASK and SELECT queries to detect ingestion errors or vocabulary drift | sentinel results; trend deltas |

## Operationalising semantic monitoring as telemetry

Where a service participates in federated observability, consider exposing semantic health signals as metrics, or in a queryable telemetry interface, for example:

- `semantic_broken_uri_count`
- `semantic_context_resolution_failures`
- `semantic_shacl_validation_failures`
- `semantic_mapping_coverage_delta`
- `semantic_sparql_sentinel_failures`

These signals help detect silent regressions early and support cross‑provider monitoring without exposing sensitive content.

## Monitoring workflow

### 1) Baseline suite

Run nightly or on a scheduled cadence.

- Check context resolvability for all declared contexts, KPI‑SEM‑01.
- Expand representative JSON‑LD payloads and compare determinism against a stored baseline, KPI‑SEM‑01.
- Check mapping target resolvability and mapping sanity rules where mappings exist, KPI‑SEM‑02.
- Run SHACL validation for declared RDF assets and store reproducible output, KPI‑SEM‑04.
- Check dereferenceability of URIs where it is declared as an expectation.

### 2) Change‑triggered suite

Run the baseline suite after:

- vocabulary releases
- context changes
- mapping updates
- ontology version and import changes
- publication pipeline changes affecting RDF generation

Publish a drift report describing: what changed, impact, affected dependent resources, and remediation steps.

### 3) On failure

- Open an incident ticket and notify the declared owner.
- Classify severity using the deliverable’s severity language, Critical, Major, Minor.
- Decide remediation versus downgrade and reassessment and document the decision.
- Close the incident only when the baseline suite passes and evidence is archived.

## Outputs and artefacts

A semantic monitoring run should produce stable artefacts suitable for audit and reuse:

- `inventory/` - asset inventories, YAML and JSON
- `reports/` - validation outputs, URI checks, lint reports, SHACL reports, sentinel results
- `drift/` - diffs between baselines and new runs
- `evidence/` - minimal supporting artefacts, logs, screenshots where necessary
- `tickets/` - links and IDs for incidents and remediation actions

## Tooling examples

Any tooling is acceptable if it produces reproducible outputs.

Common options:

- JSON‑LD processing: JSON‑LD processors used in CI pipelines
- SHACL: pySHACL, Jena SHACL, TopBraid
- RDF and SPARQL checks: RDFLib, Jena, endpoint sentinel query jobs
- vocabulary linting: SKOS integrity scripts, language tag validators

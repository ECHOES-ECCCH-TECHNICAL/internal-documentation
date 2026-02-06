# Semantic Monitoring

This page provides **non-binding** operational guidance for semantic monitoring of CH Cloud resources.
It complements the semantic monitoring section in **D6.2 Semantic Monitoring Chapter** by describing practical routines for detecting drift and integrity failures in semantic assets.

## Scope

Semantic monitoring applies when a resource uses or exposes semantic representations, including:

- JSON-LD metadata and contexts (L2+)
- controlled vocabularies and thesauri (typically SKOS) (L2+)
- mappings and alignments between semantic artefacts (L2/L3)
- ontologies/knowledge models (OWL, CIDOC-CRM expressions/extensions) (primarily L3)
- RDF graphs and SPARQL endpoints (L3)
- constraint artefacts (SHACL shapes) (L3)

## Relationship to KPIs

This page operationalises the semantic KPI set defined in `kpis.md`:

- **KPI-SEM-01** — JSON-LD validity (context resolvability; deterministic expansion)
- **KPI-SEM-02** — Vocabulary linkage (resolvable controlled terms; mapping checks where applicable)
- **KPI-SEM-03** — RDF graph availability (where RDF is declared)
- **KPI-SEM-04** — SHACL constraint validation (where shapes are declared)

## Core monitoring goals

1. **Detect semantic drift** (changes that alter interpretation without an obvious outage)
2. **Detect integrity failures** (broken URIs, invalid contexts, invalid shapes, ontology import failures)
3. **Ensure reproducibility** (stable versions, traceable change history, reproducible validation outputs)
4. **Provide actionable remediation** (clear owner, severity, and steps to restore conformance)

## What to maintain as inventory

Maintain a **machine-readable inventory** of semantic assets that are in scope for monitoring. Recommended fields:

- asset identifier and version (immutable where feasible)
- authoritative location (URI) and distribution URL(s)
- dependencies (imports, referenced contexts, mapping targets)
- applicability (which datasets/services depend on it)
- owner/steward contact and escalation route
- declared expectations (e.g., dereferenceable URIs, supported languages, expected graph shapes)

**Example (YAML):**
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

The signals below strengthen early detection **beyond** the mandatory baseline described in the deliverable.

| Signal category | Recommended checks | Typical outputs |
|---|---|---|
| Identifier & URI integrity | Detect 404/410; redirects that change identity; unexpected content negotiation changes | list of broken URIs; redirect diffs; HTTP evidence |
| JSON-LD context & serialization | Detect term remapping without versioning; undefined terms; non-deterministic expansion | context resolution report; expansion diff |
| Vocabulary integrity (SKOS) | BCP47 language tag checks; label hygiene; broader/narrower cycle detection | lint report; cycle list; missing label list |
| Mapping integrity | conflicting mappings; mapping cycles; coverage regression vs baseline | mapping diff; regression summary |
| Ontology integrity | import resolvability; pinned imports; optional reasoning checks when reasoning is declared | import report; inconsistency report |
| SHACL integrity | shape drift without version bump; inconsistent targetClass use; validation performance regressions | SHACL report; runtime stats |
| SPARQL integrity | sentinel ASK/SELECT queries to detect ingestion errors or vocabulary drift | sentinel results; trend deltas |

## Monitoring workflow 

### 1) Nightly baseline suite
- Check **context resolvability** for all declared contexts. *(KPI-SEM-01)*
- Expand representative JSON-LD payloads and compare expansion determinism against a stored baseline. *(KPI-SEM-01)*
- Check mapping target resolvability and basic mapping sanity rules where mappings exist. *(KPI-SEM-02)*
- Run SHACL validation for declared RDF assets (when declared) and store reproducible output. *(KPI-SEM-04)*
- Check dereferenceability of URIs where it is declared as an expectation.

### 2) Change-triggered suite 
Run the baseline suite after:

- vocabulary releases
- context changes
- mapping updates
- ontology version changes or import changes
- publication pipeline changes affecting RDF generation

Publish a **drift report** describing: what changed, impact, affected dependent resources, and remediation steps.

### 3) On failure
- Open an incident ticket and notify the declared owner.
- Classify severity (Critical/Major/Minor) using the deliverable’s response rules as the shared language.
- Decide remediation vs downgrade/reassessment and document the decision.
- Close the incident only when the baseline suite passes and evidence is archived.

## Outputs and artefacts 

A semantic monitoring run should produce stable artefacts suitable for audit and re-use:

- `inventory/` — asset inventories (YAML/JSON)
- `reports/` — validation outputs (URI checks, lint reports, SHACL reports)
- `drift/` — diffs between baselines and new runs
- `evidence/` — minimal supporting artefacts (logs, screenshots where necessary)
- `tickets/` — links/IDs for incidents and remediation actions

## Tooling (examples)

Any tooling is acceptable if it produces reproducible outputs. Common options:

- JSON-LD processing: JSON-LD processors used in CI pipelines
- SHACL: pySHACL / Jena SHACL / TopBraid
- RDF/SPARQL checks: RDFLib / Jena / endpoint sentinel query jobs
- Vocabulary linting: SKOS integrity scripts; language tag validators

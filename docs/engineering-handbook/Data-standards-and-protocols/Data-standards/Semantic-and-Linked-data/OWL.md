# OWL

OWL is a W3C standard for creating **formal ontologies**: schema‑level models that define classes, properties, and logical relationships in a machine‑interpretable way.
OWL is more expressive than SKOS and supports automated reasoning, which can be valuable for advanced semantic integration and consistency checking.

In CH Cloud contexts, OWL is most relevant for higher‑maturity interoperability: knowledge models, ontology alignment, and formal semantic profiles (including CIDOC CRM patterns and extensions).

This page provides **practical, non‑normative** guidance for using OWL in interoperable semantic assets.

## What OWL is good for

Use OWL when you need:

- a shared semantic backbone or alignment to a domain ontology (for example CIDOC CRM patterns),
- explicit modelling of complex relationships (events, production processes, provenance, actors),
- reusable ontologies that multiple providers can extend consistently,
- reasoning‑enabled use cases (classification, consistency checking, inference),
- formal constraints at the schema level, often combined with SHACL for operational validation.

## When OWL is not the best choice

OWL is often unnecessary when:

- you only need controlled terms and labels (SKOS is simpler),
- you need quick discovery metadata without rich semantics (DCAT, DC, DCTERMS may suffice),
- no reasoning or ontology tooling will be used and there is no conversion plan,
- performance constraints make reasoning impractical.

A common pattern is:

- use OWL for schema‑level definitions
- use RDF for instance data
- validate instance conformance with SHACL

## OWL 2 profiles

OWL defines profiles that trade expressiveness for performance.

| Profile | Strength | Typical use |
|---|---|---|
| OWL 2 EL | Scalable classification over large hierarchies | Large taxonomies and biomedical‑style structures |
| OWL 2 QL | Query answering over large datasets | OBDA patterns |
| OWL 2 RL | Rule‑friendly subset | Rule engines and forward chaining |

Choose profiles only if you have a concrete performance or tooling need.
Otherwise, keep modelling conservative and validate operationally with SHACL.

## Governance and versioning

Ontology governance is critical.

Recommended rules:

- publish an ontology IRI (stable) and a distinct version IRI per release
- pin and document imports (avoid unpinned “latest” imports where possible)
- publish change notes and a deprecation policy
- keep editorial responsibility explicit (owner, steward, contact)
- avoid silent semantic shifts (meaning changes without a version bump)

## Reasoning vs validation

Reasoning and validation solve different problems.

- reasoning can infer additional facts and detect logical inconsistencies, depending on axioms
- SHACL provides operational constraint validation (cardinality, required properties, datatype constraints, closed shapes)

Operational best practice:

- keep reasoning optional and clearly declared
- use SHACL for repeatable conformance checks and evidence generation
- if reasoning is used, document the reasoner and profile, and define what constitutes a blocking inconsistency

## Minimal example

```turtle
@prefix crm:  <http://www.cidoc-crm.org/cidoc-crm/> .
@prefix owl:  <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .

crm:E12_Production a owl:Class ;
  rdfs:label "Production"@en .

crm:P108_has_produced a owl:ObjectProperty ;
  rdfs:domain crm:E12_Production ;
  rdfs:range  crm:E24_Physical_Human-Made_Thing .
```

## Common pitfalls

| Pitfall | Why it hurts | Better pattern |
|---|---|---|
| Ontology imports float to “latest” | Upstream drift breaks validation | Pin versions or mirror imports |
| No clear version IRI policy | Hard to reproduce results | Publish stable ontology IRI plus version IRIs |
| Using OWL for simple label lists | Unnecessary complexity | Use SKOS for controlled vocabularies |
| Treating OWL axioms as operational constraints | OWL is not SHACL | Use SHACL for operational validation |
| Publishing ontologies without change notes | Consumers can’t adapt | Publish release notes and deprecation guidance |

## References

- OWL 2 Overview (W3C): https://www.w3.org/TR/owl2-overview/
- OWL 2 Profiles (W3C): https://www.w3.org/TR/owl2-profiles/
- RDFS (W3C): https://www.w3.org/TR/rdf-schema/
- SHACL (W3C): https://www.w3.org/TR/shacl/
- CIDOC CRM: https://www.cidoc-crm.org/

# SKOS

SKOS is a W3C standard for representing controlled vocabularies, thesauri, taxonomies, and classification schemes as linked data.
It provides a shared pattern for publishing terminology systems on the web and mapping them across institutions.

In CH Cloud contexts, SKOS is a primary mechanism for terminology alignment and multilingual discovery across providers.

This page provides **practical, non‑normative** guidance for using SKOS in interoperable metadata pipelines.

## What SKOS is good for

Use SKOS when you need:

- controlled vocabularies for subjects, object types, materials, techniques, periods, and similar
- multilingual labels for concepts (language‑tagged strings)
- stable, dereferenceable identifiers for terms
- mappings between vocabularies (crosswalks)
- predictable structures for faceted search and browse interfaces

## When SKOS is not the right tool

SKOS is not ideal when:

- you need formal ontological constraints and reasoning (use OWL and domain ontologies)
- you are modelling instance data (objects, events) rather than concept schemes
- your vocabulary is an unstable internal list that changes daily without governance (stabilise first)

## Core modelling building blocks

| SKOS term | Meaning |
|---|---|
| `skos:Concept` | A concept in a vocabulary |
| `skos:ConceptScheme` | The vocabulary or scheme itself |
| `skos:prefLabel` | Preferred label, typically one per language |
| `skos:altLabel` | Alternative labels or synonyms |
| `skos:broader` / `skos:narrower` | Hierarchical relations |
| `skos:related` | Associative relation |
| `skos:exactMatch`, `skos:closeMatch` | Mappings across vocabularies |

## Governance: versioning and stability

Vocabulary governance is often the deciding factor for interoperability success.

Recommended rules:

- mint stable, dereferenceable URIs for concepts and for the concept scheme
- publish a version identifier and change notes for each release
- do not reuse concept URIs for different meanings
- if a term is retired, publish deprecation or tombstone behaviour rather than silently removing it
- document who maintains the vocabulary and how updates are proposed

## Validation and integrity checks

Common SKOS integrity checks include:

- at most one `skos:prefLabel` per language per concept
- valid BCP47 language tags
- no unintended cycles in broader or narrower hierarchies where the hierarchy is intended to be acyclic
- mapping target resolvability when `exactMatch` and `closeMatch` are used
- scheme membership completeness (concepts belong to the expected scheme)

These checks can be implemented via:

- SHACL shapes
- dedicated SKOS integrity scripts
- CI linting pipelines with archived reports

## Publishing patterns

Typical publication options:

- RDF dumps (Turtle, JSON‑LD) per version
- SPARQL endpoint where query services are required
- dereferenceable concept URIs (HTML and RDF via content negotiation)
- documentation describing scope, editorial rules, and examples

## Minimal example

```turtle
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

<https://vocab.example.org/aat/300078925> a skos:Concept ;
  skos:prefLabel "watercolor painting"@en ;
  skos:prefLabel "Aquarellmalerei"@de ;
  skos:altLabel "watercolour painting"@en ;
  skos:broader <https://vocab.example.org/aat/300054216> .
```

Example mapping to an external vocabulary concept:

```turtle
<https://archive.example.org/vocab/materials/akwarela> a skos:Concept ;
  skos:prefLabel "akwarela"@pl ;
  skos:exactMatch <http://vocab.getty.edu/aat/300078925> .
```

## Common pitfalls

| Pitfall | Why it hurts | Better pattern |
|---|---|---|
| Multiple `prefLabel` values in the same language | Breaks UI expectations | Enforce one prefLabel per language |
| Unversioned vocabulary changes | Drift and inconsistent mappings | Version releases and publish change notes |
| Non‑resolvable mapping targets | Mappings become meaningless | Validate dereferenceability or maintain stable dumps |
| Mixing instance data with vocabulary concepts | Semantic confusion | Keep SKOS for concepts; use RDF and ontologies for instances |

## References

- SKOS Reference (W3C): https://www.w3.org/TR/skos-reference/
- SKOS Primer (W3C): https://www.w3.org/TR/skos-primer/
- Getty AAT: https://www.getty.edu/research/tools/vocabularies/aat/

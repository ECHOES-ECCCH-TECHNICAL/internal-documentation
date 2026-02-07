# JSON‑LD 

JSON‑LD is a JSON‑based serialisation for **Linked Data**. It allows ordinary JSON payloads to carry explicit semantics by introducing an `@context` that maps keys to RDF IRIs.
This makes JSON‑LD a pragmatic bridge between **web‑native JSON APIs** and **semantic graph interoperability**.

This page provides **practical, non‑normative** guidance for adopting JSON‑LD in CH Cloud services and metadata pipelines.

## What JSON‑LD is good for

Use JSON‑LD when you need:

- web‑friendly delivery of **semantic metadata** (datasets, services, items, annotations),
- interoperability with JSON‑first systems while preserving RDF meaning,
- incremental adoption of linked data without forcing RDF syntax on all developers,
- compatibility with ecosystems that already use JSON‑LD (Schema.org, IIIF Presentation, Linked.Art patterns).

## When JSON‑LD is not the best choice

JSON‑LD may be unnecessary when:

- the entire toolchain already operates on RDF serialisations (Turtle, N‑Triples) and JSON adds no value,
- ontology engineering is the primary activity (specialists often prefer Turtle and OWL tooling),
- you cannot commit to stable contexts and versioning discipline (JSON‑LD without governance becomes brittle).

## Key concept: `@context` and why governance matters

`@context` defines how JSON keys map to IRIs, and can also declare datatypes, languages, and container behaviour.
In practice, the context is the **semantic contract** for JSON‑LD.

Recommended governance rules:

- treat contexts as **versioned artefacts** (for example `/context/v1`, `/context/v1.1`, `/context/v2`)
- avoid silent remapping of terms to different IRIs without a version bump
- keep contexts reachable and stable (HTTP 200, correct content type, long cache lifetime for versioned contexts)
- document intended use: required terms, optional terms, and a deprecation policy

If you use external contexts, pin versions where possible, or mirror them, to avoid unexpected upstream drift.

## Core processing modes you should understand

Most interoperability problems arise from misunderstanding how JSON‑LD processors behave.

### Expansion

Turns compact keys into full IRIs and normalises structures.

Expansion is ideal for:

- deterministic validation
- drift detection across versions

### Compaction

Uses a context to produce more developer‑friendly JSON‑LD structures.

Compaction is useful for API ergonomics, but should not be used as the only validation view.

### Framing

Reshapes JSON‑LD into a tree‑like structure for application consumption.

Framing is powerful, but is an application‑layer view.
Do not confuse framed output with the underlying RDF graph.

## Validation strategy

JSON‑LD benefits from a two‑layer validation strategy.

### 1) Structural validation (JSON level)

- validate JSON structure using **JSON Schema** (required fields, datatypes, arrays vs objects)

### 2) Semantic validation (graph level)

- expand JSON‑LD and validate the resulting RDF graph using **SHACL** (cardinality, class membership, property constraints, controlled vocabulary usage)

Operationally, this typically means:

- validate example payloads in CI
- archive validation outputs as evidence for onboarding or reassessment
- re‑run validation after changes to contexts, schemas, or mappings

## Recommended modelling conventions

### 1) Identifiers

- prefer stable HTTPS URIs for entity identifiers (`@id`)
- do not reuse identifiers for different real‑world entities
- if you must change an identifier, publish a deprecation or supersession policy and mapping

### 2) Types

- use explicit `@type` where it adds interoperability value (dataset, service, object, concept)
- keep type usage consistent across payloads and versions

### 3) Language tags

- use language maps or language‑tagged strings for multilingual labels
- avoid mixing languages in the same string without tags

### 4) Context design

- keep contexts minimal and well‑scoped (avoid “everything in one context” when different APIs need different profiles)
- prefer stable prefixes and avoid renaming terms casually
- document vocabulary sources used (Schema.org, DCTERMS, SKOS, CIDOC CRM patterns, and similar)

## Publishing and delivery patterns

Common publication patterns include:

- API responses in JSON‑LD (for discovery and item metadata)
- downloadable JSON‑LD dumps (for batch processing)
- sidecar JSON‑LD metadata next to media and 3D assets
- JSON‑LD manifests (for example IIIF Presentation)

Caching tip: versioned URLs allow long cache lifetimes and reduce load on providers.

## Minimal example

```json
{
  "@context": "https://schema.org",
  "@id": "https://museum.example.org/object/12345",
  "@type": "CreativeWork",
  "name": "Portrait of a Woman",
  "creator": {
    "@type": "Person",
    "name": "Rembrandt van Rijn",
    "sameAs": "https://vocab.getty.edu/ulan/500011051"
  },
  "license": "https://creativecommons.org/licenses/by/4.0/"
}
```

## Common pitfalls

| Pitfall | Why it hurts | Better pattern |
|---|---|---|
| Unversioned context that changes semantics | Silent breakage across providers | Version contexts and publish change notes |
| Using local IDs as identifiers | Not globally unique or resolvable | Use stable HTTPS URIs |
| Validating only JSON structure | Misses semantic errors | Expand and validate with SHACL |
| Mixing multilingual labels without tags | Poor indexing and ambiguity | Use language maps and tagged strings |
| Treating compaction and framing output as “truth” | Different frames may hide changes | Treat expanded graphs as canonical for validation |

## References

- JSON‑LD 1.1 (W3C): https://www.w3.org/TR/json-ld11/
- JSON‑LD 1.1 API (W3C): https://www.w3.org/TR/json-ld11-api/
- SHACL (W3C): https://www.w3.org/TR/shacl/
- JSON Schema: https://json-schema.org/

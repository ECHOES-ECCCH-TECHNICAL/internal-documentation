# RDF (Resource Description Framework)

RDF is a W3C standard graph data model for representing information as **triples**:

- **subject** → **predicate** → **object**

Example (informal):

> *Mona Lisa* → *was created by* → *Leonardo da Vinci*

RDF is a foundation for semantic interoperability: it supports linking datasets, annotations, vocabularies, and schemas across institutions into a queryable **knowledge graph**. Unlike table-based models, RDF allows flexible connection of heterogeneous entities (objects, people, places, concepts) without requiring a single rigid schema.


## When to use RDF

Use RDF when you need to express and query **semantic relationships** across systems:

- Express relationships between entities (artworks, people, places, concepts).
- Integrate heterogeneous datasets into a shared knowledge graph.
- Publish rich metadata intended for cross-system querying and enrichment.
- Align with cultural heritage ontologies (e.g., CIDOC CRM).
- Support multi-institution interoperability (especially L2/L3 scenarios).

## When not to use RDF

RDF is often unnecessary or inefficient in these cases:

- Only simple, flat metadata is needed (basic listings, internal spreadsheets).
- Graph processing is not supported and no conversion pipeline is planned.
- Managing large binary payloads (images, video, 3D): RDF should describe **metadata**, not carry binaries.
- Immediate delivery is required but there is no RDF expertise; a phased approach is usually safer.


## Relevance to Cultural Heritage (CH Cloud)

- Highly relevant for **Level 2 and Level 3** interoperability.
- Enables semantic alignment needed to query diverse cultural heritage datasets together.
- Widely used in European infrastructures (e.g., Europeana), making it a strong candidate for shared knowledge representation in CH Cloud contexts.


## Technical considerations

### Serializations

| Serialization | File extension | Notes |
|---|---|---|
| Turtle | `.ttl` | Compact and human-readable |
| RDF/XML | `.rdf` | XML-based; verbose but widely supported |
| N-Triples | `.nt` | Simple; suitable for streaming and tooling |
| JSON-LD | `.jsonld` | JSON-based; integrates well with web APIs |

### Validation

Validate RDF graphs against expected structures using:
- **SHACL** (Shapes Constraint Language), or
- **ShEx** (Shape Expressions)

### Querying

Use **SPARQL 1.1** for expressive queries, including federated querying across multiple RDF endpoints.

### Tools (examples)

Common RDF tooling includes: Apache Jena, RDF4J, GraphDB, Virtuoso.  
(Actual adoption depends on local implementation choices and CH Cloud architecture decisions.)

### Namespaces and URI management

RDF requires careful governance of:
- namespaces,
- persistent URI patterns,
- collision avoidance,
- stability over time.


## Example: Publishing an object as RDF

A museum publishes data about a ceramic vase using RDF triples:

```turtle
@prefix crm: <http://www.cidoc-crm.org/cidoc-crm/> .
@prefix dc:  <http://purl.org/dc/elements/1.1/> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .

<vase/12345> rdf:type crm:E22_Human-Made_Object .
<vase/12345> crm:P108i_was_produced_by <production/event789> .
<vase/12345> dc:title "Attic Red-Figure Kylix"@en .

<production/event789> crm:P14_carried_out_by <artist/Euphronios> .
<production/event789> crm:P4_has_time-span <timespan/500BCE> .
```

This enables queries such as:
- “Find all objects produced by Euphronios.”
- “Which objects were produced in the 5th century BCE?”


## References (informative)

- RDF 1.1 Concepts and Abstract Syntax (W3C): https://www.w3.org/TR/rdf11-concepts/
- Turtle (W3C): https://www.w3.org/TR/turtle/
- SPARQL 1.1 Query Language (W3C): https://www.w3.org/TR/sparql11-query/
- SHACL (W3C): https://www.w3.org/TR/shacl/
- CIDOC CRM: https://www.cidoc-crm.org/

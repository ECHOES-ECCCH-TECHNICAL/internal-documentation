# RDF

RDF is a W3C standard data model for representing information as a **graph** of statements (triples):

- subject → predicate → object

RDF is the backbone of semantic interoperability.
It enables linking entities (objects, people, places, concepts) across providers without forcing a single rigid schema.
In CH Cloud contexts, RDF supports cross‑collection discovery, enrichment, and knowledge‑graph integration.

This page provides **practical, non‑normative** guidance for adopting RDF in interoperable metadata and semantic pipelines.

## What RDF is good for

Use RDF when you need:

- integration of heterogeneous metadata into a shared knowledge graph
- explicit relationships (events, actors, places, concepts) that span datasets
- consistent linking to shared vocabularies (SKOS) and ontologies (OWL, CIDOC CRM)
- graph‑native validation (SHACL) and graph querying (SPARQL)
- cross‑provider semantic alignment at higher interoperability maturity

## When RDF is not the best choice

RDF is often unnecessary when:

- only simple flat listings are required (CSV or JSON without semantics is enough)
- the team has no semantic pipeline plan and cannot maintain URI and namespace governance
- the primary workload is large binary delivery (RDF should describe binaries, not carry them)

A common safe approach is phased adoption:

- baseline discovery metadata first
- then semantic enrichment and graph alignment as capacity grows

## Serialisations

RDF is a model; serialisations are the file formats.

| Serialisation | Typical extension | Notes |
|---|---|---|
| Turtle | `.ttl` | Compact and human‑readable |
| N‑Triples / N‑Quads | `.nt` / `.nq` | Simple; good for streaming and pipelines |
| RDF/XML | `.rdf` | Verbose; legacy but widely supported |
| JSON‑LD | `.jsonld` | Web‑friendly; useful for APIs and exchange |

Recommendation:

- use Turtle for human review
- use N‑Triples or N‑Quads for bulk pipelines
- use JSON‑LD for web APIs where semantic payloads are required

## URI and namespace governance

Interoperability depends on stable identifiers.

Recommended practice:

- define a provider namespace policy (base URI patterns, what IDs mean, stability guarantees)
- treat published URIs as persistent identifiers (avoid renaming)
- when change is unavoidable, provide redirects and deprecation or supersession notes
- avoid minting new URIs for the same entity without an explicit equivalence policy

For vocabularies and labels, prefer reusing authoritative URIs (Getty, Wikidata, VIAF, and similar) where appropriate.

## Validation strategy

Graph validation is typically done using SHACL:

- enforce required properties and datatypes
- enforce cardinalities
- enforce controlled vocabulary constraints
- validate profile conformance for published graphs

Operational guidance:

- store validation outputs as evidence
- version shapes and publish change notes
- re‑run SHACL validation after releases or pipeline changes

## Querying and access patterns

### RDF dumps (batch)

Publish versioned dumps for ingestion pipelines.
Provide checksums and basic dataset metadata.

### SPARQL endpoints (interactive)

SPARQL enables expressive queries and federation patterns, but increases operational complexity.

If you publish SPARQL:

- document supported query envelope (timeouts, limits)
- provide a small set of sentinel queries for monitoring
- keep endpoint behaviour stable across upgrades (avoid silent changes in namespace mappings)

### Content negotiation

Where you publish dereferenceable URIs, you may support content negotiation (HTML vs RDF) for usability.

## Minimal example

```turtle
@prefix crm: <http://www.cidoc-crm.org/cidoc-crm/> .
@prefix dcterms: <http://purl.org/dc/terms/> .

<https://museum.example.org/object/12345>
  a crm:E22_Human-Made_Object ;
  dcterms:title "Attic Red-Figure Kylix"@en .
```

## Common pitfalls

| Pitfall | Why it hurts | Better pattern |
|---|---|---|
| Unstable URIs | Breaks links and downstream graphs | Publish URI policy; avoid renames; use redirects |
| Mixing object‑level and catalogue‑level modelling | Confuses rights and access semantics | Separate dataset and service records from item descriptions |
| No constraints or validation | Silent data drift | Use SHACL profiles and re‑run validation |
| Publishing a SPARQL endpoint without limits | Operational risk | Document limits; implement timeouts; monitor with sentinels |
| Storing binaries inside RDF | Inefficient and non‑standard | Use RDF to describe binaries; store binaries separately |

## References

- RDF 1.1 Concepts (W3C): https://www.w3.org/TR/rdf11-concepts/
- Turtle (W3C): https://www.w3.org/TR/turtle/
- SPARQL 1.1 Query (W3C): https://www.w3.org/TR/sparql11-query/
- SHACL (W3C): https://www.w3.org/TR/shacl/
- CIDOC CRM: https://www.cidoc-crm.org/

# EDM 

EDM is an RDF‑based aggregation model used by Europeana to integrate metadata from libraries, archives, museums, and audiovisual collections.
It extends Dublin Core and other vocabularies and uses OAI‑ORE patterns to represent aggregations, proxies, and digital representations.

EDM is relevant in CH Cloud contexts because:

- many institutions already produce EDM for Europeana participation
- EDM provides a proven pattern for large‑scale aggregation of heterogeneous cultural heritage metadata

This page provides practical, non‑normative guidance for using EDM, or ingesting EDM exports, in federated workflows.

## What EDM is good for

Use EDM when you need:

- interoperability with Europeana‑style aggregation ecosystems
- ingestion of existing EDM exports from providers
- a consistent model for distinguishing:

  - the cultural heritage object
  - its digital representations
  - the aggregation record used for discovery

- an intermediate representation that can be mapped into other semantic backbones (for example CIDOC CRM) where required

## When EDM is not the best choice

EDM is usually not ideal as:

- the sole internal semantic backbone of a knowledge graph if you have chosen a different ontology as the core model
- a replacement for domain‑precise ontologies where reasoning and formal constraints are required

A common pattern is EDM for exchange and aggregation, and CIDOC CRM or domain ontologies for deep semantics.

## Key building blocks

EDM typically involves these kinds of resources:

- Provided Cultural Heritage Object as the thing being described (conceptual object)
- Web Resource(s) as digital representations (images, pages, files)
- Aggregation that ties together a provider’s record, object, and web resources for discovery
- Proxy for provider or context‑specific statements that may differ across aggregators

It also commonly uses:

- Dublin Core and DCTERMS for descriptive fields
- SKOS for controlled vocabularies
- OAI‑ORE patterns for aggregation structures

## Interoperability considerations

### 1) Stable URIs are essential

Aggregation models depend on stable identifiers:

- object identifiers
- web resource identifiers
- aggregation identifiers

If URIs change, downstream portals and linkers break.
If change is unavoidable, publish redirects and a deprecation or migration policy.

### 2) Be explicit about what is being described

EDM distinguishes between:

- the cultural heritage object
- the digital representation (files)
- the aggregation record

Avoid collapsing these into a single node.
It leads to ambiguous rights, provenance, and access semantics.

### 3) Rights and licensing consistency

Rights may apply at different levels:

- object‑level rights statements
- digital representation rights and licences
- aggregation and distribution conditions

Ensure these are not contradictory, and prefer standard rights and licence URIs.

### 4) Mapping to other semantic models

If EDM is ingested into another ontology (for example CIDOC CRM):

- document the mapping rules and version them
- record provenance (which source version produced which target graph)
- validate both the source EDM and the transformed output (SHACL can be used for both)

## Validation and quality checks

- SHACL conformance checks for the chosen EDM profile (provider and export profile)
- URI hygiene checks (resolvability where intended; no accidental duplication)
- controlled vocabulary checks (SKOS concept URIs resolvable where expected)
- separation sanity checks:

  - object and web resource not collapsed
  - aggregation structure present when required by the workflow

## Minimal illustrative pattern

```turtle
@prefix edm: <http://www.europeana.eu/schemas/edm/> .
@prefix dcterms: <http://purl.org/dc/terms/> .

<https://provider.example.org/item/123> a edm:ProvidedCHO ;
  dcterms:title "Example object"@en ;
  dcterms:license <https://creativecommons.org/licenses/by/4.0/> .

<https://provider.example.org/aggregation/123> a edm:Aggregation ;
  edm:aggregatedCHO <https://provider.example.org/item/123> ;
  edm:isShownBy <https://provider.example.org/file/123.jpg> .
```

## References

- EDM documentation: https://pro.europeana.eu/page/edm-documentation
- EDM primer: https://pro.europeana.eu/page/edm-primer
- OAI‑ORE specification: https://www.openarchives.org/ore/1.0/toc
- SHACL (W3C): https://www.w3.org/TR/shacl/

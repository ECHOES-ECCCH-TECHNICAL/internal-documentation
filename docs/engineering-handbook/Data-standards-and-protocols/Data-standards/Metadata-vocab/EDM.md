# EDM (Europeana Data Model)

EDM is an RDF-based aggregation data model defined by Europeana to integrate metadata from libraries, archives, museums, and audiovisual collections across Europe. EDM extends Dublin Core and other vocabularies and uses OAI-ORE patterns for aggregations and proxies.

EDM is a major reference point for cultural heritage aggregation at European scale:
- It demonstrates how heterogeneous CH metadata can be aggregated into a single interoperable model.
- Many CH institutions already produce or can export EDM as part of Europeana participation.


## When to use EDM

- Integrating or exchanging data with Europeana-like aggregation services.
- Providers that already have EDM exports and want to minimize conversion work.
- As a source format that can be mapped into CIDOC CRM or other ontological representations.

## When not to use EDM

- As the internal core ontology for the CH Cloud knowledge graph if another ontology (e.g., CIDOC CRM) is chosen as the semantic backbone.
- For new ontology-centric modelling where direct CIDOC CRM (or other domain ontologies) is preferred.


## Relevance to Cultural Heritage (CH Cloud)

- Important for providers participating in Europeana or producing EDM exports.
- Relevant for interoperability between CH Cloud and the Europeana ecosystem.
- EDM-to-CIDOC CRM mapping paths can support Level 2/3 interoperability, but require careful governance and validation.


## Technical considerations

### Building blocks
EDM commonly uses:
- Dublin Core / DCTERMS
- SKOS (controlled vocabularies)
- OAI-ORE concepts for aggregation structures

### URIs and aggregations
- Aggregations and proxies require stable URIs.
- EDM distinguishes between the provided cultural object, its digital representations, and the aggregation object.

### Mappings and validation
- EDM-to-CIDOC CRM mappings exist in the community but require careful configuration and validation.
- SHACL can be used to check EDM conformance before or after transformation.


## References (informative)

- Europeana Data Model (EDM) documentation: https://pro.europeana.eu/page/edm-documentation
- EDM Primer: https://pro.europeana.eu/page/edm-primer
- OAI-ORE (spec): https://www.openarchives.org/ore/1.0/toc
- SHACL (W3C): https://www.w3.org/TR/shacl/

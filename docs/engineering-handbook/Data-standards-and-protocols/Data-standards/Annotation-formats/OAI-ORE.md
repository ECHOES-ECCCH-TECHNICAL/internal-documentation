# OAI-ORE (Object Reuse and Exchange)

OAI-ORE is a framework for describing **aggregations of related digital objects**. It is used extensively in Europeana and related ecosystems to represent compound objects (e.g., a book with images, OCR text, metadata, and derivatives).


## When to use OAI-ORE

- Representing compound digital objects or multi-part collections.
- Interoperability with Europeana and other aggregation platforms.
- Expressing relationships between representations and aggregated resources.

## When not to use OAI-ORE

- As a general-purpose ontology or metadata schema for item-level modelling.
- Single simple resources that do not require aggregation semantics.


## Relevance to Cultural Heritage (CH Cloud)

- Useful for onboarding multi-part cultural heritage objects.
- Relevant when partners already produce EDM (which uses ORE patterns extensively).


## Technical considerations

- Uses RDF to describe aggregations.
- Requires stable URIs and clear relationships between aggregated components.
- Governance: ensure consistent rules for “part” vs “representation” vs “proxy”.


## References (informative)

- OAI-ORE Specification: https://www.openarchives.org/ore/1.0/toc
- Europeana EDM documentation: https://pro.europeana.eu/page/edm-documentation

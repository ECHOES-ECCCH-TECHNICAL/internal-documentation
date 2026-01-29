# Interoperability Protocols

This section provides **practical, non-normative** guidance on protocols commonly used for interoperability in the CH Cloud. It complements the normative requirements in the deliverable by explaining **when to use which protocol**, what to expect operationally, and where to find authoritative specifications.

## What this section covers

The CH Cloud integrates across institutions and tools using a mix of:

- **API styles** (REST, GraphQL) for service-to-service and UI-to-service integration,
- **query protocols** (SPARQL) for RDF/knowledge-graph access and federation,
- **domain protocols** (IIIF) for interoperable image access and manifests,
- **harvesting protocols** (OAI-PMH) for batch and incremental metadata ingestion,
- **decentralised patterns** (Solid) for user-controlled linked data (optional / exploratory).


## Pages in this section

- [API Styles and Query Protocols: REST, GraphQL, and SPARQL](Protocols.md)  
  Baseline guidance for API-based interoperability and RDF querying.
- [IIIF (International Image Interoperability Framework)](IIIF.md)  
  Image delivery, manifests, viewer interoperability, and annotation integration.
- [OAI-PMH (Open Archives Initiative Protocol for Metadata Harvesting)](OAI-PMH.md)  
  Batch and incremental metadata harvesting for repositories and aggregators.
- [Solid (Social Linked Data Protocol)](Decentralised-data-protocols.md)  
  Decentralised linked data using Pods; relevant for user-owned annotations/profiles.


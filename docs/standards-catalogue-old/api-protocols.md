# Protocols and APIs (D6.2 §3.2)

This page summarises protocols and API styles referenced for interoperable access, harvesting, querying, and exchange.

## IIIF (International Image Interoperability Framework)

IIIF provides standard APIs for image delivery and presentation, enabling consistent access patterns and viewer/tool interoperability.

**Recommended use**
- interoperable image access and presentation,
- consistent delivery of derivatives and manifests across providers.

## OAI-PMH (Open Archives Initiative Protocol for Metadata Harvesting)

OAI-PMH is an HTTP-based protocol for incremental harvesting of metadata (commonly XML records).

### Use when
- harvesting metadata from legacy repositories and aggregators,
- periodic synchronisation is required,
- providers cannot expose modern REST/JSON APIs.

### Avoid when
- real-time or event-driven synchronisation is required,
- complex semantic structures are required without additional transformation.

### Technical notes
- Supports incremental updates via datestamps
- Uses resumption tokens for large sets (pagination)
- Common metadata formats include DC, MODS, MARCXML, EDM.

## Solid (Social Linked Data Protocol)

Solid is a W3C initiative for decentralised, user-controlled data storage using Pods, aligned with Linked Data principles.

### Use when
- user-owned data is required (e.g., private annotations, preferences),
- read/write Linked Data interaction is needed.

### Avoid when
- bulk institutional dataset delivery is needed,
- stable institution-controlled APIs are required.

## REST APIs
REST remains the default integration style for web services due to broad adoption and ecosystem tooling.

**Recommended use**
- interoperable service endpoints with stable resource identifiers,
- predictable HTTP semantics for integration.

## GraphQL
GraphQL is useful where clients need flexible query shapes and aggregation within a single endpoint.

**Recommended use**
- client-driven query flexibility is a priority,
- strong schema governance is available.

## SPARQL Protocol
SPARQL provides a standard query protocol for RDF graphs and knowledge graph endpoints.

**Recommended use**
- RDF-native querying and federation patterns,
- semantic integration workflows.

## OGC Web Services (WMS, WFS, WMTS)
OGC web services provide established interoperability patterns for geospatial layers and map services.

**Recommended use**
- GIS / spatial data interoperability and geospatial client compatibility.

## API description and validation standards (D6.2 §3.2.8)
Use standard, machine-readable API descriptions and validation artefacts:
- OpenAPI for REST contract description
- JSON Schema for payload structure (JSON)
- SHACL for RDF constraint validation (semantic rules)

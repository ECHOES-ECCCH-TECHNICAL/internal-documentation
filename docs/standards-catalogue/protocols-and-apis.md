# Protocols and APIs (from D6.2 §3.2)

Protocols and APIs define how systems communicate, how data flows between services, and how external tools interact with CH Cloud components. They are essential for reproducible workflows, consistent metadata harvesting, cross-institutional access to digital assets, and integration with existing cultural heritage and research infrastructures.

!!! note "Normative boundary"
The official deliverable (PDF) defines the authoritative interoperability requirements.  
This page provides maintained implementation guidance and reference material; it does not introduce new MUST/SHALL obligations.

## What protocol choices affect in the CH Cloud

Protocol choices directly influence:
- how datasets are ingested and synchronised,
- how digital objects (images, 3D, audiovisual) are delivered,
- how metadata is harvested and exposed to external platforms,
- how user-facing applications interact with underlying services,
- how semantic data is queried or published,
- how distributed services remain discoverable and interoperable.

## Quick selection guide (practical “when to use what”)

- **IIIF**: interoperable delivery and presentation of image-based collections (manifests, deep zoom, annotations).
- **OAI-PMH**: legacy-friendly metadata harvesting and incremental synchronisation.
- **REST**: baseline for service interoperability and integration with most clients.
- **GraphQL**: flexible field selection for complex/nested domain objects via a single endpoint.
- **SPARQL**: RDF/knowledge graph querying and semantic federation (Levels 2–3).
- **OGC services**: interoperable delivery of geospatial layers and map services.
- **Solid**: user-controlled data pods and read/write Linked Data for personal workspaces and user-generated content.
- **OpenAPI / JSON Schema / SHACL**: contracts and validation artefacts enabling machine-testable interoperability.


## 3.2.1 IIIF – International Image Interoperability Framework

IIIF is a set of REST-based APIs enabling consistent access to high-resolution images and associated metadata across institutions. It defines predictable URLs and JSON-LD–based manifests describing digital objects, sequences, annotations, and structure.

### Recommended use
- web-accessible images of cultural heritage objects (manuscripts, artworks, photos, maps),
- deep zoom, region selection, tiling, multi-resolution viewing,
- annotation workflows (crowdsourcing, scholarly annotation),
- integration with existing IIIF viewers (e.g., Mirador, Universal Viewer),
- synchronisation patterns using the Change Discovery API where applicable.

### When not to use
- non-image data (3D, audio, text) unless wrapped in IIIF Presentation manifests,
- preservation-grade delivery of original master files (e.g., TIFF masters),
- cases where only thumbnails/low-resolution previews are needed.

### CH Cloud relevance
- strong candidate for **Level 1–2** interoperability for image-based collections,
- enables interoperable viewer/tool integration and annotation components.

### Technical notes
- **IIIF Image API**: region/size/quality/rotation operations
- **IIIF Presentation API**: JSON-LD manifests describing structure and metadata
- integrates with **Web Annotation**
- stable URLs for images and manifests are a prerequisite.



## 3.2.2 OAI-PMH – Open Archives Initiative Protocol for Metadata Harvesting

OAI-PMH is an HTTP-based protocol for structured, incremental harvesting of metadata, commonly used by libraries, archives, and aggregators.

### Recommended use
- harvesting metadata from legacy repositories and OAI-compatible aggregators,
- periodic synchronisation of provider metadata,
- **Level 1** ingestion where minimal transformation is sufficient,
- providers unable to expose REST/JSON(-LD) APIs.

### When not to use
- real-time synchronisation or event-driven updates,
- complex semantic structures (e.g., CIDOC-CRM, SKOS) without additional transformation,
- cases where richer APIs and formats are readily available.

### CH Cloud relevance
- provides a compatibility layer for institutions without modern APIs,
- supports automated ingestion pipelines for baseline onboarding.

### Technical notes
- common XML metadata formats: Dublin Core, MODS, MARCXML, EDM
- verbs: Identify, ListRecords, ListSets, GetRecord, etc.
- large repositories: **resumption tokens** for pagination
- datestamp consistency is essential for incremental harvesting.



## 3.2.3 Solid – Social Linked Data Protocol

Solid is a W3C initiative for decentralised, user-controlled data storage using Pods (personal online data stores). It uses Linked Data principles and standard web technologies for read/write access to structured data.

### Recommended use
- user-owned data scenarios (private annotations, personal preferences),
- research environments where individuals curate personal metadata/observations,
- components requiring read/write interaction with Linked Data resources.

### When not to use
- general-purpose metadata or media delivery,
- bulk ingestion of institutional datasets,
- cases where stable, institution-controlled APIs are required.

### CH Cloud relevance
- promising for future user-generated content, personal workspaces, and privacy-centric services,
- not intended as a mandatory institutional delivery mechanism.

### Technical notes
- RDF-native storage patterns
- standard HTTP methods (GET/POST/PATCH)
- identity via WebID; authentication via Solid-OIDC
- notification mechanisms can support near real-time updates
- stable URIs remain a core prerequisite.



## 3.2.4 REST APIs

REST is the dominant architectural style for web APIs. It uses standard HTTP methods (GET/POST/PUT/DELETE) and commonly returns JSON or JSON-LD.

### Recommended use
- exposing dataset metadata, records, validation results, and service functionality,
- building front-end applications that rely on structured data,
- baseline API interoperability (Levels 1–2),
- partner integration where technical capacity varies.

### When not to use
- graph-native semantic querying (use SPARQL for RDF graphs),
- highly complex nested retrieval that causes over/under-fetching (consider GraphQL),
- very large binary transfers where streaming/tiling is needed (use specialised protocols).

### Technical notes
- document contracts with **OpenAPI**
- validate payloads with **JSON Schema**
- explicit API versioning is strongly recommended.



## 3.2.5 GraphQL

GraphQL is a query language for APIs that lets clients request exactly the data they need, typically via a single endpoint. It can reduce over/under-fetching and support nested object graphs efficiently.

### Recommended use
- clients need precise control over fields and nested structures,
- portals/tools require rich hierarchical views,
- Level 2 APIs offering complex data structures.

### When not to use
- simple or flat metadata (REST is simpler),
- direct RDF/graph querying (SPARQL is appropriate),
- streaming or binary transfers.

### Technical notes
- requires a formal schema
- resolvers must be implemented per field
- versioning and schema evolution must be managed carefully.



## 3.2.6 SPARQL Protocol

SPARQL is the W3C standard query language and HTTP protocol for retrieving and manipulating RDF data. It is central to knowledge graphs and semantic federation.

### Recommended use
- querying RDF/knowledge graphs,
- semantic metadata retrieval and federated cross-institution queries,
- Level 3 semantic integration, contextual navigation, semantic search.

### When not to use
- non-RDF datasets,
- simple key-value or tabular use cases where simpler APIs suffice.

### Technical notes
- SPARQL 1.1 features: federation, aggregates, property paths
- result formats: JSON, XML, CSV/TSV
- requires stable URIs and consistent ontologies.



## 3.2.7 OGC Web Services (WMS, WFS, WMTS)

OGC standards support interoperable delivery of maps (WMS), vector features (WFS), and map tiles (WMTS), enabling GIS tool compatibility and mapping interfaces.

### Recommended use
- exposing geospatial layers and archaeological/spatial datasets,
- map-based discovery and visualisation in CH Cloud tools,
- Level 1–2 spatial interoperability.

### When not to use
- non-spatial datasets,
- cases where simple vector-only JSON formats (e.g., GeoJSON) are sufficient and no GIS interoperability is required.

### CH Cloud relevance
- important where CH datasets include spatial information (sites, historic maps, coordinates),
- compatible with widely used GIS ecosystems.



## 3.2.8 API description and validation standards

Interoperability requires predictable service behaviour, machine-readable contracts, and consistent validation.

### When to use
- **OpenAPI** for documenting REST contracts
- **JSON Schema** for validating JSON payloads
- **SHACL** for validating RDF graphs and semantic constraints

### CH Cloud relevance
- foundational for onboarding tools, metadata validators, and automated compliance checks,
- enables machine-testable interoperability across services.

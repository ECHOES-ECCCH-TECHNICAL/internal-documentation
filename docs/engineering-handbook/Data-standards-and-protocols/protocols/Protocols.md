# API Styles and Query Protocols: REST, GraphQL, and SPARQL

This page provides **practical, non-normative** guidance on common API styles and query protocols used in CH Cloud service interoperability: **REST**, **GraphQL**, and **SPARQL**.


## REST APIs

REST (Representational State Transfer) is the dominant architectural style for web APIs. REST services use standard HTTP methods (`GET`, `POST`, `PUT`, `PATCH`, `DELETE`) and typically exchange **JSON** or **JSON-LD**.

For CH Cloud components (catalog APIs, validation services, pipelines, visualization tools), REST provides:
- a widely supported integration mechanism,
- easy adoption by partners with varying technical capacity,
- compatibility with modern application development,
- clear contract definitions via **OpenAPI**.

### When to use REST
- Exposing dataset metadata, records, validation results, or service functionality.
- Supporting front-end applications that rely on structured data over HTTP.
- Interoperability at Level 1 and Level 2 for API-based access.

### When not to use REST
- Querying RDF graphs and semantic metadata directly (**SPARQL** is more appropriate).
- Complex nested retrieval where clients need precise control (**GraphQL** may be more efficient).
- Extremely large resources requiring streaming/tiling protocols (use specialized transfer protocols).

### Relevance to Cultural Heritage (CH Cloud)
- REST is expected to underpin many CH Cloud services and onboarding interfaces.
- Works well with **JSON-LD**, enabling lightweight semantic integration.

### Technical considerations
- Document contracts with **OpenAPI/Swagger**.
- Validate request/response payloads with **JSON Schema**.
- Use explicit API versioning (path, header, or media-type strategies).
- Provide predictable error models (status codes + structured error payload).

## GraphQL

GraphQL is a query language for APIs that allows clients to request exactly the data they need from a single endpoint. Because CH data is often complex, hierarchical, and interconnected, GraphQL can:
- reduce over-fetching and under-fetching common in REST,
- enable nested data retrieval in a single call,
- expose complex data structures in a flexible way.

### When to use GraphQL
- Client applications require precise control over which fields to retrieve.
- Portals and tools need nested object graphs (e.g., object → events → actors → places).
- Level 2 APIs that expose richer, composable data structures.

### When not to use GraphQL
- Simple/flat metadata where REST is simpler to implement and operate.
- Direct querying of RDF knowledge graphs (SPARQL is the native mechanism).
- Streaming or large binary transfers (use dedicated delivery mechanisms).

### Relevance to Cultural Heritage (CH Cloud)
- Useful when user-facing portals require configurable views over complex data.
- Can be combined with JSON-LD representations for lightweight semantics, but requires governance.

### Technical considerations
- Requires a formal **GraphQL schema** and resolvers for each field.
- Schema evolution must be managed carefully (deprecation strategy, field lifecycle).
- Introduce performance controls (query complexity limits, depth limits, caching).
- Security: enforce authorization consistently at resolver level; avoid exposing sensitive fields by default.

## SPARQL Protocol

SPARQL is a W3C standard query language and HTTP protocol for retrieving and manipulating **RDF** data. In CH Cloud contexts where RDF-based semantic representations are adopted (Levels 2–3), SPARQL supports:
- querying distributed knowledge graphs,
- accessing ontological metadata,
- semantic search and reasoning workflows,
- federated cross-institution queries.

### When to use SPARQL
- Querying RDF data or knowledge graphs.
- Semantic metadata retrieval and cross-institution federated queries.
- Integrating data aligned with CIDOC CRM, SKOS, and related ontologies.

### When not to use SPARQL
- Datasets that are not RDF-based.
- Simple key-value or tabular access patterns where REST/SQL is sufficient.

### Relevance to Cultural Heritage (CH Cloud)
- High relevance for Level 3 semantic integration.
- Enables semantic search, contextual navigation, and inference-driven exploration.

### Technical considerations
- Prefer **SPARQL 1.1** features where supported (federation, aggregates, property paths).
- Results can be returned as JSON, XML, CSV/TSV.
- Requires stable URI patterns and consistent ontology use across providers.
- Operationally: manage endpoint performance (timeouts, pagination/limits), and protect endpoints (rate limits, auth).

## Quick selection guide

| Need | Prefer | Why |
|---|---|---|
| Simple CRUD-style API, broad partner adoption | **REST** | Ubiquitous tooling; straightforward contracts |
| Client-controlled selection of nested fields | **GraphQL** | Minimizes over/under-fetching; nested retrieval |
| Querying RDF graphs across providers | **SPARQL** | Native graph querying; federation support |


## References 
- REST (architectural style): https://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm
- OpenAPI Specification: https://spec.openapis.org/oas/latest.html
- JSON Schema: https://json-schema.org/
- GraphQL Specification: https://spec.graphql.org/
- SPARQL 1.1 Query Language (W3C): https://www.w3.org/TR/sparql11-query/
- SPARQL 1.1 Protocol (W3C): https://www.w3.org/TR/sparql11-protocol/

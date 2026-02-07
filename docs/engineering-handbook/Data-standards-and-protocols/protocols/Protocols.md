# API Styles and Query Protocols 

This page provides **practical, non-normative** guidance on common API styles and query protocols used for CH Cloud service interoperability:
**REST**, **GraphQL**, and **SPARQL**.

It is intended for service providers and integrators who need to choose an API approach and implement it in a way that is:
- understandable by partners with different technical capacities,
- contract-driven and testable,
- compatible with federation (authentication/authorisation, operational monitoring),
- amenable to evolution without breaking consumers.

> **Relationship to the deliverable:** The normative requirements and conformance rules live in **D6.2** (interoperability requirements, evaluation/monitoring, validation).
> This page explains *how to implement typical API approaches well* and *how to choose between them*.



## Cross-cutting guidance (applies to all API styles)

Regardless of protocol, interoperable services tend to share the same operational and design foundations:

### 1) Contract-first design
- Publish a machine-readable contract (OpenAPI, GraphQL schema, SHACL/VoID/service descriptions for SPARQL where applicable).
- Make the contract the basis for validation and regression testing.
- Prefer *backward-compatible* evolution (additive changes) and explicit deprecation for breaking changes.

### 2) Stable identifiers and predictable behaviour
- Keep identifiers stable across versions and releases.
- Use consistent semantics for status codes / error types / “not found” behaviour.
- Avoid “silent” changes (fields disappearing, meaning shifting, undocumented filtering rules).

### 3) Security and federation readiness
- Use TLS (HTTPS) for externally reachable endpoints.
- For protected endpoints, integrate with the project’s federated AAI where applicable (OIDC-based flows) and enforce authorisation consistently.
- Ensure that security controls apply at the same granularity as the API’s data model (e.g., field-level enforcement for GraphQL where required).

### 4) Operational characteristics
- Define timeouts, rate limits, and pagination/limits for large collections.
- Provide predictable response envelopes and correlation identifiers where possible.
- Produce sufficient logs/metrics to support incident response and drift detection (how telemetry is shared is defined elsewhere in the wiki).



## REST APIs

REST (Representational State Transfer) is the dominant architectural style for web APIs. REST services use standard HTTP methods
(`GET`, `POST`, `PUT`, `PATCH`, `DELETE`) and typically exchange **JSON** or **JSON-LD**.

In CH Cloud components (catalog APIs, validation services, pipelines, visualisation tools), REST provides:
- broad partner adoption and tooling support,
- straightforward integration for web and backend clients,
- clear contract definitions via **OpenAPI**,
- natural alignment with resource-oriented models (datasets, records, jobs, runs, results).

### When REST is a good fit
- Exposing dataset metadata, records, validation results, or service functionality over HTTP.
- Supporting front-end applications that consume structured resources.
- Providing interoperability-compatible APIs where consumers need predictable behaviour and versioning.

### When REST is not the best fit
- Querying RDF graphs directly (use **SPARQL**).
- Deeply nested retrieval where clients need precise field selection (consider **GraphQL**).
- Very large binary/streaming delivery patterns (use specialised delivery mechanisms).

### Recommended REST practices (interoperability-friendly)
- **Contracts:** publish OpenAPI 3.x; keep it versioned and test it in CI.
- **Versioning:** make version semantics explicit (e.g., major versions for breaking changes).
- **Pagination/limits:** for collections, define default limits, maximum limits, and pagination semantics.
- **Errors:** return meaningful HTTP status codes and a structured error payload (e.g., problem-details style).
- **Consistency:** keep naming, filtering, and sorting conventions consistent across endpoints.
- **JSON-LD (when used):** document contexts and term mappings; ensure contexts are resolvable and stable.



## GraphQL

GraphQL is a query language for APIs that allows clients to request exactly the data they need from a single endpoint.
Because CH data is often complex, hierarchical, and interconnected, GraphQL can:
- reduce over-fetching and under-fetching common in REST,
- enable nested retrieval in a single call,
- expose a coherent domain model to multiple clients.

### When GraphQL is a good fit
- Portals and tools need nested object graphs (e.g., object → events → actors → places).
- Client applications need fine-grained control over which fields are retrieved.
- You want a single, strongly-typed API surface that composes multiple backend sources.

### When GraphQL is not the best fit
- Simple/flat resources where REST is cheaper to implement and operate.
- Native RDF querying and federation (use **SPARQL** for RDF graphs).
- Large binary or streaming transfer patterns.

### Recommended GraphQL practices (interoperability-friendly)
- **Schema governance:** treat the schema as the contract; version it and use deprecations instead of breaking changes.
- **Performance controls:** enforce query depth/complexity limits; use caching/persisted queries where possible.
- **Authorisation:** apply access control consistently at resolver level; do not rely on “client won’t ask for it.”
- **Error semantics:** provide stable error codes/messages that clients can act on.
- **Observability:** record query characteristics (complexity, execution time) to detect regressions.



## SPARQL Protocol

SPARQL is a W3C standard query language and HTTP protocol for retrieving and manipulating **RDF** data.
Where RDF-based semantic representations are adopted, SPARQL supports:
- querying knowledge graphs,
- semantic search and reasoning workflows,
- federated cross-provider queries (where enabled and governed).

### When SPARQL is a good fit
- Querying RDF graphs and semantic metadata.
- Cross-institution semantic search or linking workflows.
- Integrating data aligned with CIDOC CRM, SKOS, and related ontologies.

### When SPARQL is not the best fit
- Resources that are not RDF-based.
- Simple key-value or tabular access patterns where REST is sufficient.

### Recommended SPARQL practices (interoperability-friendly)
- **Endpoint behaviour:** document supported query features; define timeouts and result limits.
- **Service description:** publish dataset/service descriptions and namespace expectations.
- **Namespace stability:** keep URI patterns stable; version ontologies/vocabularies explicitly.
- **Operational safety:** apply rate limits and safeguards against expensive queries; monitor slow queries.
- **Security:** if protected, integrate federated AAI and define clear authorisation rules (named graphs, dataset partitions, query policies).



## Choosing between REST, GraphQL, and SPARQL

Use the simplest approach that meets the use case and can be operated reliably.

| Need | Prefer | Why |
||||
| Broad partner adoption; simple resource operations | **REST** | ubiquitous tooling; easy contracts with OpenAPI |
| Client-controlled selection of nested fields | **GraphQL** | field selection and nested retrieval in one call |
| Native RDF querying; semantic federation | **SPARQL** | standard graph querying; RDF-native semantics |

### Typical combinations (common in practice)
- **REST + JSON-LD** for resource access + lightweight semantics.
- **GraphQL** for portal-facing composition over multiple REST backends.
- **SPARQL** for RDF graph access, alongside REST/GraphQL for operational APIs.



## References (primary sources)
- REST architectural style (Fielding dissertation): https://www.ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm
- OpenAPI Specification: https://spec.openapis.org/oas/latest.html
- JSON Schema: https://json-schema.org/
- GraphQL Specification: https://spec.graphql.org/
- SPARQL 1.1 Query Language (W3C): https://www.w3.org/TR/sparql11-query/
- SPARQL 1.1 Protocol (W3C): https://www.w3.org/TR/sparql11-protocol/

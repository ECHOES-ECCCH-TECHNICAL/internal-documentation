# OAI-PMH (Open Archives Initiative Protocol for Metadata Harvesting)

OAI-PMH is an HTTP-based protocol for harvesting metadata in a structured, incremental, machine-readable way. It is widely used by digital libraries, archives, repositories, and aggregators. Many cultural heritage institutions still rely on OAI-PMH as their primary export interface.

OAI-PMH remains relevant because it:
- supports large-scale metadata harvesting,
- uses simple XML-based records (e.g., Dublin Core),
- enables incremental updates via datestamps,
- has low technical barriers for providers.


## When to use OAI-PMH

Use OAI-PMH when you need batch or incremental harvesting, especially from legacy systems:

- Harvesting metadata from legacy repositories, library systems, or OAI-compatible aggregators.
- Periodic synchronization of provider metadata into an aggregator or central catalog.
- Level 1 ingestion where minimal transformation is sufficient.
- When providers cannot expose modern REST/JSON(-LD) APIs.

## When not to use OAI-PMH

OAI-PMH is usually not appropriate for:

- Real-time synchronization or event-driven updates.
- Complex semantic data structures (CIDOC CRM, SKOS, RDF graphs) as a primary exchange mechanism.
- Cases where JSON-based APIs, JSON-LD, or richer service interfaces are available and can be adopted.

## Relevance to Cultural Heritage (CH Cloud)

- Useful for harvesting metadata from existing institutional repositories.
- Provides a fallback compatibility layer for institutions without modern APIs.
- Can support automated ingestion pipelines for Level 1 interoperability.


## Technical considerations

### Metadata formats

OAI-PMH exchanges XML records. Common formats include:
- Dublin Core (`oai_dc`)
- MODS
- MARCXML
- EDM (Europeana Data Model) when provided by relevant systems

### Core verbs (operations)

OAI-PMH defines a small set of standard verbs, including:
- `Identify`
- `ListMetadataFormats`
- `ListSets`
- `ListIdentifiers`
- `ListRecords`
- `GetRecord`

### Pagination via resumptionToken

Large result sets require pagination using `resumptionToken`. Harvesters must:
- follow tokens until exhaustion,
- handle token expiry behavior documented by the provider,
- implement retry/backoff for transient failures.

### Incremental harvesting via datestamps

Incremental sync relies on consistent `datestamp` behavior:
- define whether `datestamp` reflects metadata modification time vs. record publication time,
- ensure timezones and granularity are consistent,
- document deletion semantics (e.g., “deleted” records) to support accurate synchronization.

### Operational expectations

- Providers should document supported formats, sets, and harvesting limits.
- Harvesters should be polite (rate limits, backoff, scheduling).
- Monitor for drift (missing records, datestamp anomalies, format changes).



## References 
- Open Archives Initiative – OAI-PMH specification: https://www.openarchives.org/OAI/openarchivesprotocol.html
- OAI-PMH primer (overview): https://www.openarchives.org/OAI/2.0/primer
- Dublin Core Metadata Element Set: https://www.dublincore.org/specifications/dublin-core/dces/

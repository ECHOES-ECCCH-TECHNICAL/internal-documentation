# OAI-PMH

OAI-PMH is an HTTP-based protocol for harvesting metadata **in bulk or incrementally** from repositories using a small set of standard operations (“verbs”).  
It is widely used by libraries, archives, institutional repositories, and aggregators, and it remains a common export interface for legacy or repository-style systems.



## 1. What OAI-PMH is good for

OAI-PMH is a good fit when you need:

- **Batch ingestion** of metadata from multiple institutions into an aggregator or catalogue.
- **Incremental harvesting** based on datestamps (“only what changed since last run”).
- **Low-barrier provider onboarding** where a provider cannot expose a modern REST/JSON(-LD) API yet.
- **Compatibility** with existing digital library tooling, repository platforms, and aggregator workflows.

In practice, OAI-PMH often serves as a **compatibility layer** that enables federation while an ecosystem transitions toward richer, more service-oriented interfaces.



## 2. When to use OAI-PMH (typical CH Cloud scenarios)

Use OAI-PMH when:
- you need periodic synchronisation of provider metadata into a central catalogue,
- the provider already exposes OAI-PMH as a stable export channel,
- the integration is primarily metadata harvesting (not interactive querying),
- you need a “Level 1” or baseline interoperability path for institutions with limited technical capacity.



## 3. When *not* to use OAI-PMH

OAI-PMH is usually not appropriate when you need:

- **Real-time** or event-driven synchronisation (use change feeds, webhooks, or push-based integrations).
- **Rich semantic exchange** as the primary mechanism (RDF graphs, SHACL validation, CIDOC CRM-aligned query use cases).
- **Interactive querying** by downstream clients (use REST/GraphQL/SPARQL for query-style use cases).
- **High-frequency updates** with strict freshness expectations (OAI-PMH polling can become operationally heavy).



## 4. Key protocol concepts (provider + harvester)

### 4.1 Metadata formats
OAI-PMH transfers XML records in one or more declared formats. Common formats include:
- **Dublin Core** (`oai_dc`) - minimal baseline
- **MODS**, **MARCXML** - library/repository formats
- **EDM** (Europeana Data Model) - where supported by relevant systems

**Recommendation:** If multiple formats exist, document which format is considered authoritative for the federation use case.

### 4.2 Core verbs (operations)
OAI-PMH defines a small set of standard verbs:
- `Identify` - repository identity and admin metadata
- `ListMetadataFormats` - supported formats
- `ListSets` - optional grouping of records
- `ListIdentifiers` - identifiers only (useful for checks and diffs)
- `ListRecords` - full record harvesting
- `GetRecord` - fetch a specific record

### 4.3 Pagination via `resumptionToken`
Large result sets are paginated using a `resumptionToken`.

**Harvester guidance:**
- follow tokens until exhaustion,
- handle token expiry (some providers expire tokens quickly),
- implement retry + exponential backoff for transient failures,
- store progress so harvesting can resume after failures.

**Provider guidance:**
- document token behaviour (expiry time, maximum page size, whether tokens are opaque),
- keep token stability reasonable for large harvests.

### 4.4 Incremental harvesting via datestamps
Incremental sync relies on consistent `datestamp` behaviour.

**You should document:**
- what `datestamp` represents (metadata modification vs publication time),
- timezone and granularity (day vs second-level precision),
- how deleted records are represented (`deleted` status semantics).

**Harvester guidance:**
- apply a small overlap window to avoid missing boundary updates,
- detect “datestamp anomalies” (time going backwards, large gaps) and alert operators.



## 5. Interoperability considerations (recommended)

### 5.1 Identifier strategy
- Treat OAI identifiers as stable primary keys for harvesting.
- Maintain a mapping between OAI identifiers and CH Cloud internal identifiers (if different).
- Avoid reusing identifiers for different real-world resources.

### 5.2 Set design (`ListSets`)
Sets can be used to partition harvesting:
- per collection,
- per institution unit,
- per content type.

**Recommendation:** Use sets only if they are stable and well documented; unstable sets can create “phantom” deltas.

### 5.3 Transformation and mapping
OAI-PMH records are commonly ingested into a canonical internal model.
Document:
- mapping rules (field-to-field, normalisation, controlled vocabularies),
- enrichment steps (if any),
- provenance tracking (“which source record produced this output”).

### 5.4 Monitoring and drift detection
Because OAI-PMH is batch-oriented, drift can appear as:
- missing records,
- sudden drops in record counts,
- unexpected format/schema changes,
- datestamp inconsistencies.

Recommended monitoring signals:
- record count trends per set and per format,
- harvest duration and error rates,
- resumptionToken failures,
- datestamp distribution checks,
- format availability changes (`ListMetadataFormats` diffs).

### 5.5 Security considerations
Many OAI-PMH endpoints are open, but restricted endpoints exist in practice.
If restricted:
- document authentication expectations and HTTP status behaviour,
- ensure access control is consistent across `ListRecords` and `GetRecord`,
- avoid leaking sensitive content via error payloads.



## 6. Implementation tips (harvester-side)

- Use a **polite harvesting strategy** (rate limits, backoff, scheduled windows).
- Prefer `ListIdentifiers` for “diff-like” checks before heavy `ListRecords` pulls.
- Cache `Identify` and format/set lists but revalidate periodically.
- Persist a harvest state (last successful timestamp + token progress) for reliable recovery.
- Store raw XML as evidence (for audit/debug), and store processed output separately.



## 7. References (primary sources)

- OAI-PMH specification: https://www.openarchives.org/OAI/openarchivesprotocol.html
- OAI-PMH primer: https://www.openarchives.org/OAI/2.0/primer
- Dublin Core Metadata Element Set: https://www.dublincore.org/specifications/dublin-core/dces/

# Dublin Core (DC) and DCMI Terms (DCTERMS)

Dublin Core is a lightweight descriptive metadata standard composed of a small set of generic elements (title, creator, subject, date, etc.) and extended terms provided by **DCMI Terms (DCTERMS)**. It is designed to describe a wide range of resources in a simple, interoperable way.

Dublin Core is widely adopted globally and often serves as a “lowest common denominator” for cross-domain interoperability. Many institutions and repositories can export at least Dublin Core, making it a practical baseline for discovery and onboarding.


## When to use Dublin Core

- When only basic descriptive metadata is required (e.g., initial resource registration).
- For **Level 1 interoperability**, where minimal metadata is sufficient for discovery.
- When onboarding data from systems that cannot easily provide richer schemas.
- When building simple catalogues or cross-domain search interfaces.

## When not to use Dublin Core

- When modelling complex cultural heritage semantics (events, actors, provenance).
- As the sole internal schema for advanced CH applications (limited domain depth).
- When detailed object-level relationships or temporal structures are required (CIDOC CRM, EDM, or domain ontologies are more appropriate).

## Relevance to Cultural Heritage (CH Cloud)

- Strong candidate for a minimum metadata profile at Level 1 to ensure resources are discoverable.
- Useful as a fallback/mapping target when integrating heterogeneous legacy data.
- Low-effort export option for many external repositories and institutional systems.

## Technical considerations

### Serializations
Dublin Core can appear in multiple serializations, including:
- XML (commonly via OAI-PMH)
- RDF (often with DCTERMS)
- JSON-LD (for web APIs)

### Validation
- XML Schema (XSD) for XML-based DC profiles
- SHACL shapes for RDF-based DC profiles
- JSON Schema for JSON/JSON-LD-based representations

### Extensions and profiles
- DCTERMS provides refined properties (e.g., `dcterms:created`, `dcterms:issued`).
- Application profiles can constrain which elements are mandatory/optional and what value types/controlled vocabularies apply.


## References (informative)

- Dublin Core Metadata Element Set (DCMES): https://www.dublincore.org/specifications/dublin-core/dces/
- DCMI Metadata Terms (DCTERMS): https://www.dublincore.org/specifications/dublin-core/dcmi-terms/
- Dublin Core Application Profiles: https://www.dublincore.org/specifications/dublin-core/profile-guidelines/

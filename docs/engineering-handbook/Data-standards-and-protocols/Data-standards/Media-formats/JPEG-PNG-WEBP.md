# DCAT (Data Catalog Vocabulary)

DCAT is a W3C vocabulary for describing datasets, data services, and distributions in catalogues. It describes a dataset’s **existence, access points, formats, and basic properties** (not the internal content of the dataset).

DCAT is widely used for open data portals and interoperable dataset catalogues. It enables:
- exchange of catalogue records between portals,
- harvesting and re-exposure of catalogue entries,
- consistent discovery of datasets and services.


## When to use DCAT

- Describing datasets, APIs, and data services in a catalogue.
- When CH Cloud needs to expose or ingest dataset descriptions compatible with other portals and EOSC-related infrastructures.
- Level 1 and Level 2 onboarding workflows where datasets/services must be registered in a central catalogue.

## When not to use DCAT

- Detailed object-level or item-level description (individual artworks/documents).
- As a replacement for domain models like CIDOC CRM or EDM.
- Internal technical logs or private operational configuration content.


## Relevance to Cultural Heritage (CH Cloud)

- Natural choice for a dataset catalogue layer and interoperability with wider European data catalogue ecosystems.
- DCAT profiles can harmonize how datasets and services are exposed to external platforms.


## Technical considerations

### Core classes
- `dcat:Dataset` — a dataset as a conceptual entity
- `dcat:Distribution` — an accessible form of the dataset (file, API, etc.)
- `dcat:DataService` — a service that provides access to data

### Serializations
- RDF/Turtle
- JSON-LD

### Validation and profiles
- SHACL shapes can define DCAT application profiles (required fields, constraints).
- In EU contexts, **DCAT-AP** is a common profile baseline.


## References (informative)

- DCAT v3 (W3C Recommendation): https://www.w3.org/TR/vocab-dcat-3/
- DCAT-AP (EU profile): https://semiceu.github.io/DCAT-AP/releases/
- SHACL (W3C): https://www.w3.org/TR/shacl/

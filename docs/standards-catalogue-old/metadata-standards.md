# Metadata standards (D6.2 §3.1.2)

Metadata standards define how resources are described so they can be discovered, compared, and integrated across systems.

In the CH Cloud context, metadata supports:
- search and discovery,
- dataset registration and cataloguing,
- semantic integration and enrichment,
- aggregation from external providers.

## Dublin Core (DC / DCTERMS)

Dublin Core is a lightweight descriptive metadata standard and a common baseline across repositories.

### Use when
- only basic descriptive metadata is required (e.g., initial registration),
- Level 1 interoperability aims at discoverability,
- onboarding from legacy systems that cannot export richer schemas.

### Avoid when
- modelling complex CH semantics (events, actors, provenance) is required,
- object-level relationships must be expressed with domain depth.

### Technical notes
- Serialisations: XML (common in OAI-PMH), RDF (often with DCTERMS), JSON-LD (web APIs)
- Validation: XSD (XML), SHACL (RDF), JSON Schema (JSON/JSON-LD)
- Profiles can restrict mandatory/optional elements.

## DCAT (Data Catalog Vocabulary)

DCAT is a W3C vocabulary for describing datasets, data services, and distributions in catalogues (it describes *catalogue-level* entities, not internal object-level semantics).

### Use when
- describing datasets/APIs/data services in a catalogue,
- enabling interoperable catalogue exchange and harvesting,
- Level 1–2 onboarding requires dataset/service registration.

### Avoid when
- detailed object/item description is required,
- domain ontologies (e.g., CIDOC-CRM) are needed for internal semantic depth.

### Technical notes
- Core classes: `dcat:Dataset`, `dcat:Distribution`, `dcat:DataService`
- Serialisations: RDF/Turtle, JSON-LD
- Validation: SHACL shapes for application profiles; existing profiles such as DCAT-AP can be referenced.

## EDM (Europeana Data Model)

EDM is an RDF-based aggregation model used by Europeana to integrate metadata from libraries, archives, museums, and audiovisual collections.

### Use when
- interoperating with Europeana-like aggregation ecosystems,
- providers already have EDM exports and want to minimise conversion effort,
- establishing mapping paths to ontology-centric representations.

### Avoid when
- using EDM as the internal “core ontology” if another semantic backbone is chosen.

### Technical notes
- Building blocks: OAI-ORE (aggregations/proxies), Dublin Core / DCTERMS, SKOS
- Stable URIs are essential for aggregation resources
- SHACL can be used for conformance checks pre/post transformation.

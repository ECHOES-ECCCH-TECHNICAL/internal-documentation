# Data standards and formats (D6.2 §3.1)

This page provides a practical overview of data standards and formats commonly used in cultural heritage and relevant to CH Cloud interoperability.

## 1) Semantic Web and graph-based standards

### RDF and common serialisations
RDF is the core model for representing linked data and knowledge graphs. Common serialisations include:
- Turtle / RDF/XML (RDF-native serialisations)
- JSON-LD (web-friendly RDF serialisation)

**Recommended use**
- when publishing or integrating data into a knowledge graph,
- when cross-institutional linking and semantic enrichment are required,
- when SHACL-based validation is used.

### JSON-LD
JSON-LD enables treating data as normal JSON while remaining compatible with RDF tooling (e.g., conversion to/from other RDF serialisations).

**Validation approach**
- JSON Schema for structural checks
- SHACL for semantic constraints

## 2) Structured and semi-structured data formats

### CSV / TSV
Lightweight tabular formats for inventories, lists, registers, and bulk updates.

**Use when**
- providers export spreadsheet-style records,
- Level 1 onboarding requires a minimal submission option,
- simple transformation pipelines are used.

**Avoid when**
- hierarchical/nested structures must be preserved,
- rich semantics and relationships are required (consider RDF/JSON-LD),
- multilingual / ontology-aligned modelling is required.

### XML (TEI, EAD/EAC-CPF, METS, MODS, etc.)
XML supports rich hierarchical modelling and is widely used in libraries and archives.

**Use when**
- data is inherently hierarchical (e.g., manuscripts),
- archival metadata requires EAD/EAC-CPF,
- preservation-grade interchange is required.

**Avoid when**
- lightweight JSON APIs are required,
- graph-based structures are needed without conversion.

## 3) Media and domain-specific formats (overview)

### Images and raster data
Prefer formats that support long-term preservation and broad tool support. When interoperability with image delivery services is required, align with IIIF-based access patterns (see Protocols & APIs).

### 3D and spatial data
Use established 3D and GIS formats suited to your domain and workflows; prioritise formats that are widely supported, well-documented, and easy to validate.

### Audiovisual formats
Prefer broadly supported formats for access and preservation workflows; document codec/container choices consistently.

## 4) Annotation, linking, aggregation, and packaging

### Annotation and linking
Where annotations are exchanged across systems, use web-friendly, URI-addressable resources and prefer standards that support linking to targets via resolvable identifiers.

### Packaging and exchange formats
For reproducible workflows and exchange, prefer packaging approaches that can bundle payloads plus metadata and provenance (e.g., structured “crate” approaches, where applicable).

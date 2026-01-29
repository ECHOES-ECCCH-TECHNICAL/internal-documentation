# Data architecture – standards and formats (from D6.2 §3.1)

This page provides a technical overview of data standards and formats widely used in cultural heritage, digital humanities, and research infrastructures. It is intended as a **living reference** to support onboarding and integration in the ECHOES / CH Cloud.

!!! note "Normative boundary"
The authoritative interoperability requirements (including REQ tables referenced below) remain in the official deliverable (PDF).  
This page explains concepts, selection criteria, and practical guidance, and may evolve over time.

## Why standards matter for the CH Cloud

The CH Cloud integrates datasets, tools, and services across institutions, disciplines, and countries. Without shared standards:
- data cannot be combined or compared reliably,
- search and discovery across collections becomes inconsistent,
- tools and services cannot process heterogeneous inputs predictably,
- integrators lose time on ad-hoc conversions and mappings,
- preservation and sustainable access are harder to guarantee.

Using established standards reduces integration friction, increases reuse, and supports scalability.

## What “standards” cover

Data standards typically address three complementary layers:

- **Syntax** – how data is structured (fields, datatypes, file formats)
- **Semantics** – what the data means (concepts, relationships, vocabularies)
- **Protocols** – how data is exchanged (APIs, messages, serialisations)

Together these layers enable interoperability across heterogeneous systems.

## Key concepts (glossary)

- **Metadata**: “data about data.” Example: for a photo of a painting—artist, date, location, licence, resolution.
- **Semantic interoperability**: systems can exchange data *and* interpret it consistently (e.g., “creator” in one system corresponds to “artist” in another).
- **Serialisation**: an encoding of the same information in different concrete representations (e.g., RDF in Turtle, RDF/XML, JSON-LD).
- **Linked Data**: a graph approach where resources are connected via explicit relationships and stable identifiers (URIs), forming a “web of knowledge” rather than isolated records.
- **URI (Uniform Resource Identifier)**: a persistent identifier for a resource (often HTTP-based) used consistently across datasets and systems.
- **Ontology**: a formal model describing domain concepts and their relationships (objects, events, places, actors, etc.).

> Maintenance note: when this wiki is connected to your standards catalogue, link “Linked Data” and “URI” to your project’s preferred guidance pages (e.g., identifier policy, PID policy).

## The standards landscape (categories)

Cultural heritage standards can be grouped into several technical categories:

1. **Semantic and knowledge representation**  
   How meaning and relationships are expressed (e.g., RDF, OWL, SKOS).

2. **Metadata schemas**  
   How resources are described in a structured way (e.g., Dublin Core, EDM, DCAT).

3. **Media formats**  
   How images, 3D, audio, and video are stored and delivered.

4. **Exchange and packaging**  
   How collections are bundled and transferred with integrity (e.g., BagIt, RO-Crate).

5. **Rights and licensing**  
   How permissions, restrictions, and legal constraints are expressed in a machine-readable way.

## Interoperability levels and selection of standards

The CH Cloud defines three interoperability levels:

- **Level 1 (Basic)** – minimal metadata for discovery; simple formats accepted
- **Level 2 (Enhanced)** – richer metadata with semantic alignment and structured formats
- **Level 3 (Full)** – complete semantic integration using graph-based Linked Data and shared ontologies

Different standards are better suited to different levels. In the standards catalogue pages linked from this chapter we indicate where a standard is primarily relevant for Level 1, 2, or 3.

---

## Requirements referenced from D6.2 (informative index)

D6.2 §3.1 contains normative requirement tables for:
- **REQ–DS–\***: data service endpoint requirements (e.g., standards-based interfaces, avoidance of proprietary formats, access control, searchability, persistence)
- **REQ–MD–\***: dataset metadata requirements (binding metadata to data via persistent identifiers; provenance; licensing; temporal/spatial validity; creation metadata)
- **REQ–DQ–\***: data quality requirements (completeness, versioning, schema declaration/validation, global identifiers)

This wiki page does not restate those tables. Instead:
- treat the tables in the PDF as the **authoritative source**, and
- use the pages below as **implementation guidance** to satisfy them consistently.

Recommended follow-up pages in this catalogue:
- **Metadata standards** (D6.2 §3.1.2)
- **Structured & semi-structured formats** (D6.2 §3.1.3)
- **Image & raster formats** (D6.2 §3.1.4)
- **3D & spatial data** (D6.2 §3.1.5)
- **Audiovisual formats** (D6.2 §3.1.6)
- **Annotation, linking, aggregation** (D6.2 §3.1.7)
- **Packaging & exchange formats** (D6.2 §3.1.8)

---

## Practical guidance (how to use this section)

1. Start from your **target interoperability level** (L1/L2/L3).
2. Identify the minimum metadata and interface obligations in **REQ–DS/REQ–MD/REQ–DQ**.
3. Select the most appropriate standards from the relevant pages (metadata, APIs, media formats).
4. Document mappings and transformations (especially when onboarding from legacy formats).
5. Prefer stable identifiers (URIs/PIDs) and machine-readable rights, and preserve them across workflows.

# XML

XML is a hierarchical, structured document format widely used across libraries, archives, and textual scholarship communities.
Cultural heritage institutions have long traditions of XML‑based modelling and interchange, for example TEI, EAD, METS, and MODS.
These formats are expressive and well suited for preservation, interchange, and complex hierarchical description.

This page provides practical, non‑normative guidance for using XML in CH Cloud interoperability workflows.

## When XML is a good fit

XML is a strong choice when:

- data is inherently hierarchical (manuscripts, complex textual structures, compound archival descriptions)
- institutional workflows already use XML standards (TEI, EAD, METS, MODS)
- preservation‑grade descriptive structures must be exchanged faithfully
- you need schema‑governed validation on the provider side

XML can also be a pragmatic baseline exchange format for providers with existing XML exports, even if downstream services ultimately transform to JSON, JSON‑LD, or RDF.

## When XML is not the best fit

XML is usually not the best default when:

- the primary consumer is a modern web API expecting JSON payloads
- graph‑native semantics and linking are the primary representation (RDF and linked data)
- you need lightweight, client‑driven field selection (consider REST and GraphQL for APIs)

In practice, XML is often paired with transformation pipelines rather than used directly as a runtime API format.

## Schema governance

To support interoperability and long‑term stability:

- define schemas using XSD and or Relax NG, aligned with the chosen standard
- version schemas explicitly and publish change notes
- avoid silent breaking changes (namespace changes, removed required elements, semantic reinterpretations)
- publish a small set of representative example files validated against the published schema

### Namespaces

- use namespaces consistently and document conventions (prefixes, default namespaces)
- keep namespace URIs stable and treat them as identifiers

## Transformation workflows

XML is frequently transformed to support downstream services:

- XSLT is common for deterministic transformations into project profiles
- custom converters are sometimes required for:

    - XML to JSON for APIs
    - XML to JSON‑LD or RDF for semantic interoperability
    - normalisation of controlled vocabulary usage

Recommended operational practice:

- version transformation scripts
- record provenance (input version, output version, transformation parameters)
- validate transformed outputs (JSON Schema and or SHACL) where applicable

## Validation and quality checks

- schema validation (XSD and or Relax NG)
- namespace and prefix consistency checks
- required field presence for the chosen profile
- controlled vocabulary checks where the XML standard supports them
- diff‑based regression checks for releases and pipeline updates

## References

- XML 1.0 (W3C): https://www.w3.org/TR/xml/
- XML Schema 1.1 (W3C): https://www.w3.org/TR/xmlschema11-1/
- Relax NG (OASIS): https://relaxng.org/spec-20011203.html
- TEI Guidelines: https://tei-c.org/guidelines/
- EAD (Library of Congress): https://www.loc.gov/ead/
- METS (Library of Congress): https://www.loc.gov/standards/mets/
- MODS (Library of Congress): https://www.loc.gov/standards/mods/

# XML (Extensible Markup Language)

XML is a hierarchical, structured document format widely used across libraries, archives, and textual scholarship communities. Cultural heritage institutions have long traditions of XML-based modelling (e.g., TEI, EAD, METS, MODS). These formats are expressive and suitable for preservation and interchange.

## When to use XML

- Data is inherently hierarchical (e.g., manuscripts, complex textual structures).
- Archival metadata using EAD/EAC-CPF.
- Scholarly text encoding using TEI.
- Preservation-grade metadata is required.
- Level 1/2 interoperability where XML is already the institutional standard.

## When not to use XML

- Level 3 semantic interoperability without conversion to RDF/Linked Data.
- APIs that must deliver lightweight JSON payloads by default.
- Cases where graph-based structures are required (prefer RDF).


## Relevance to Cultural Heritage (CH Cloud)

- Important for archival, manuscript, and documentation workflows.
- XML-based provider data often needs XML→RDF transformation pipelines for Level 2/3 interoperability.


## Technical considerations

### Schema governance
- Define and govern schemas using **XSD** and/or **Relax NG**.
- Version schemas explicitly and avoid silent breaking changes.

### Namespaces
- Apply namespaces consistently and document conventions.

### Transformation workflows
- XSLT is common for deterministic transformations.
- Custom converters may be required for mapping to JSON-LD/RDF and project-specific profiles.

## References 

- XML 1.0 (W3C): https://www.w3.org/TR/xml/
- XML Schema (XSD, W3C): https://www.w3.org/TR/xmlschema11-1/
- Relax NG (OASIS): https://relaxng.org/spec-20011203.html
- TEI Guidelines: https://tei-c.org/guidelines/
- EAD (Library of Congress): https://www.loc.gov/ead/
- METS (Library of Congress): https://www.loc.gov/standards/mets/
- MODS (Library of Congress): https://www.loc.gov/standards/mods/

# CSV / TSV (Comma-Separated / Tab-Separated Values)

CSV/TSV are lightweight, plain-text tabular formats used for representing lists, tables, records, inventories, and statistical data. Many cultural heritage institutions export metadata and catalogue records as spreadsheets, making CSV/TSV a common “lowest barrier” exchange format.


## When to use CSV/TSV

- Simple, tabular metadata (inventories, event lists, register tables).
- Initial onboarding where source systems cannot provide richer formats.
- Level 1 interoperability as a minimal submission option.
- Bulk updates and mapping workflows.

## When not to use CSV/TSV

- Hierarchical or nested structures (multi-part objects, complex relationships).
- When semantics and rich relationships are required (prefer RDF/JSON-LD).
- When multilingual, ontology-aligned metadata is needed without a clear mapping layer.


## Relevance to Cultural Heritage (CH Cloud)

- Useful ingestion format for providers without semantic or XML export capabilities.
- Should be accompanied by schema/mapping instructions to support transformation and validation.


## Technical considerations

### Required explicit conventions
Providers should define:
- encoding (UTF-8 strongly recommended),
- delimiter and quoting rules,
- header conventions,
- column semantics (what each field means).

### Schema and validation options
- **CSVW** (W3C) for expressing metadata and schema for CSV tables
- JSON Schema for row-level structural checks (when transformed)
- Ingestion templates and mapping specifications (project conventions)


## References (informative)

- RFC 4180 (CSV): https://www.rfc-editor.org/rfc/rfc4180
- CSV on the Web (CSVW, W3C): https://www.w3.org/TR/tabular-data-model/
- CSVW Metadata (W3C): https://www.w3.org/TR/tabular-metadata/

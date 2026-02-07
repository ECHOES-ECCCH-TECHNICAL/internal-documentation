# CSV and TSV 

CSV and TSV are lightweight, plain‑text formats for tabular data.
They are widely used for inventories, exports from collection management systems, and low‑barrier data exchange between partners with different technical capacity.

This page provides practical, non‑normative guidance for using CSV and TSV as interoperability‑friendly exchange formats in CH Cloud workflows.

## What CSV and TSV are good for

CSV and TSV are a good fit when you need:

- simple tables (inventories, registers, lookup tables, event lists)
- low‑barrier onboarding from spreadsheet‑like exports
- bulk updates where rows map cleanly to records
- transformation pipelines where CSV is the input to a mapping step (CSV to JSON, JSON‑LD, or RDF)

CSV and TSV are commonly used as a baseline exchange option, especially when providers cannot expose richer APIs or structured semantic formats yet.

## When CSV and TSV are not a good fit

Avoid using CSV and TSV as the primary format when you need:

- hierarchical or nested structures (compound objects, multipart works, complex relationships)
- explicit semantics and linking (identity management, controlled vocabularies, graph relationships)
- multilingual, ontology‑aligned modelling without an accompanying mapping layer
- lossless representation of rich descriptive structures (prefer XML or semantic formats)

In these cases, use CSV only as a staging format and convert to a richer representation.

## Recommended conventions

Providers should publish the conventions below together with the file set.

### 1) Encoding, delimiter, and quoting

- encoding: UTF‑8 (strongly recommended)
- delimiter: comma for CSV, tab for TSV, declare which one is used
- quoting: declare quoting rules for delimiters and newlines, aligned to your chosen CSV dialect
- line endings: tolerate both LF and CRLF

### 2) Header row and column semantics

- include a single header row
- document each column’s meaning:

    - datatype
    - cardinality
    - units
    - language handling
    - controlled vocabulary, if used

- define missing value rules (empty versus explicit null markers)

### 3) Identifiers and keys

- include a stable identifier column where feasible (for example `id`, `record_id`, `uri`)
- if identifiers are not available, document uniqueness constraints (composite keys) and collision handling
- if identifiers are URIs, keep them stable and resolvable where intended

### 4) Dates, numbers, and language

- use ISO date formats where feasible (`YYYY-MM-DD`)
- use `.` as decimal separator (avoid locale‑specific formats)
- for multilingual strings, define a strategy:

    - separate columns per language, or
    - a controlled language‑tagged pattern

## Schema and validation

CSV itself does not carry schema.
For robust interoperability, attach one of the following:

- CSV on the Web (CSVW) metadata for column types, constraints, and mappings to RDF
- project templates, meaning a controlled column set plus validation rules
- validation after transformation, validating the produced JSON, JSON‑LD, or RDF using JSON Schema and or SHACL

Recommended validation checks:

- consistent column set and ordering, if templates are used
- datatype checks (dates, numbers, URIs)
- cardinality checks for required fields
- controlled vocabulary checks for coded values
- identifier uniqueness and referential integrity where foreign keys are used

## Operational considerations

- size: large files should be split predictably, for example per collection or date window, and accompanied by a manifest describing parts
- provenance: record source export date, system version, and transformation steps
- change detection: if re‑exported periodically, use stable identifiers to support diffs and incremental ingestion

## References

- RFC 4180 (CSV): https://www.rfc-editor.org/rfc/rfc4180
- CSV on the Web model (W3C): https://www.w3.org/TR/tabular-data-model/
- CSVW metadata (W3C): https://www.w3.org/TR/tabular-metadata/

[]()# RO-Crate

RO-Crate is a lightweight, machine-actionable packaging format that uses **JSON-LD** to describe files, metadata, provenance, workflows, and relationships. It is designed for research data packaging and reproducibility.

RO-Crate metadata is stored in `ro-crate-metadata.json` (JSON-LD).

## When to use RO-Crate

- Bundling datasets with metadata, provenance, or workflow documentation.
- Scenarios requiring reproducibility or clear explanation of dataset structure.
- Level 2 and Level 3 ingestion for complex datasets with processing context.

## When not to use RO-Crate

- Extremely large datasets where metadata overhead becomes significant without clear benefits.
- Simple file transfer with minimal metadata requirements (BagIt may be simpler).

## Relevance to Cultural Heritage (CH Cloud)

- Strong fit for datasets accompanied by digitisation or processing workflows.
- Supports structured metadata for ingestion and validation.


## Technical considerations

- `ro-crate-metadata.json` is the canonical metadata entry point.
- Profiles allow specialization for community needs (including CH-specific profiles).
- Validation can be automated using profile rules; align with shared vocabularies where possible.


## References (informative)

- RO-Crate specification: https://www.researchobject.org/ro-crate/
- RO-Crate 1.1: https://www.researchobject.org/ro-crate/1.1/
- JSON-LD (W3C): https://www.w3.org/TR/json-ld11/

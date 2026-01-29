# BagIt

BagIt is a packaging format designed to support **fixity and integrity** during transfer and archival ingestion. A “bag” contains payload files plus manifests (checksums) and optional metadata, enabling receivers to validate that a transfer is complete and unmodified.


## When to use BagIt

- Transferring collections between institutions.
- Ingestion workflows where data integrity is required.
- Level 1 or Level 2 dataset uploads delivered as packaged bundles.

## When not to use BagIt

- Dynamic datasets requiring frequent partial updates.
- API-based dataset delivery where packaging is unnecessary.


## Relevance to Cultural Heritage (CH Cloud)

- Suitable for ingestion packages for bulk transfers or offline exchange scenarios.


## Technical considerations

- Checksums provide fixity; choose algorithms aligned with organisational policy.
- Include documentation and metadata in a structured way (e.g., `bag-info.txt` and project-specific metadata files).
- Define directory layout and naming conventions to support automation.


## References (informative)

- BagIt File Packaging Format (IETF RFC 8493): https://www.rfc-editor.org/rfc/rfc8493

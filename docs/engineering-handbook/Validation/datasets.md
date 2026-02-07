# Dataset Validation

This page provides **living implementation guidance** for validating datasets against the normative rules defined in the **D6.2 deliverable**.
The authoritative requirements remain the project’s REQ-* statements; this page explains how to collect evidence and run checks consistently.


## Scope

Applies to:
- datasets registered/exposed in the federation (public or restricted),
- dataset metadata records (machine‑readable),
- dataset access endpoints where present (download/query/retrieval),
- derived/enriched datasets where provenance must be traceable.


## Inputs: evidence package

### Minimum evidence (must be provided)
- dataset identifier + dataset version (or immutable release identifier)
- machine‑readable metadata record location (URL/path)
- licence / rights statement in metadata (machine‑readable where possible)
- owner/steward + contact point
- provenance statement where applicable (especially for derived/enriched outputs)
- schema/profile references where applicable
- if L3 claimed: RDF + SHACL shapes + SHACL validation report

### Recommended evidence
- changelog or release notes per version
- checksums for large binaries
- persistence statement for identifiers/URLs (and redirect policy, if changed)
- transformation description (if exported/converted from another representation)


## Validation by interoperability level

### L1 (baseline) static checks
Typical checks:
- metadata exists and is machine‑readable
- mandatory metadata fields are present (id, title/description, licence, contact)
- stable identifier is present and consistent across artefacts

Common failure patterns:
- licence/contact missing or only free text
- identifier exists but is not stable (temporary URL, local path)

### L2  static checks (structure, semantics, provenance where applicable)
Typical checks:
- identifier stability and version/supersession evidence (no silent overwrite of releases)
- schema/profile reference where applicable (and sample validates when a schema exists)
- semantic representation or deterministic transform where applicable (e.g., JSON‑LD metadata)
- controlled vocabulary identifiers/mappings where applicable
- provenance/lineage for derived/enriched datasets (inputs, tools, parameters)
- release versioning and change history

Common failure patterns:
- version exists but overwrites the previous release without supersession notes
- controlled terms are non-resolvable strings with no mapping
- provenance is narrative-only and not tied to artefacts/versions

### L3  static + operational checks (semantic assets and monitoring where declared)
Typical checks:
- RDF representation is available where declared
- SHACL shapes are provided, versioned, accessible, and validation outputs are reproducible
- URI stability/deprecation discipline exists for published URIs
- semantic drift monitoring evidence exists where declared/required

Common failure patterns:
- shapes exist but are not versioned or not accessible
- SHACL report cannot be reproduced (inputs/versions not captured)
- URIs change without deprecation or mapping plan


## Output: dataset conformance report 

The dataset conformance report should include:
- dataset id + version and claimed level
- requirement-by-requirement results (using REQ-* identifiers where applicable)
- validation classes used (static/dynamic/operational/manual)
- evidence pointers (archived metadata, schemas, reports, logs)
- remediation guidance for failed checks

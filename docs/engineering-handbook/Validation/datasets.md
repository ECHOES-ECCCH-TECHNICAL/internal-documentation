# Dataset validation

This page provides **implementation guidance** for validating datasets against the normative rules in D6.2 Chapter 9 (§9.3.1).
The authoritative requirements remain the REQ-* statements referenced in the PDF.


## Scope

Applies to:
- datasets registered/exposed in the federation (public or restricted),
- dataset metadata records (machine-readable),
- dataset access endpoints where present (download/query/retrieval).



## Inputs (evidence package)

Minimum evidence items:
- dataset identifier + dataset version (or immutable release identifier),
- machine-readable metadata record location (URL/path),
- licence/rights statement in metadata,
- contact/ownership metadata (stewardship),
- provenance metadata where applicable,
- schema/profile references where applicable,
- if L3 claimed: RDF + SHACL shapes + SHACL validation report.

Recommended evidence items:
- changelog or release notes for versions,
- checksum(s) for large binaries,
- persistence statement for identifiers/URLs.



## Validation by interoperability level

### L1 static checks (REQ-META-001/002/003)

Checklist:
- [ ] Metadata exists and is machine-readable (REQ-META-001)
- [ ] Mandatory metadata fields present (REQ-META-002)
- [ ] Stable identifier present (REQ-META-003)

Typical evidence:
- metadata file/record (JSON/JSON-LD/XML) archived as validation artefact
- screenshot or log of successful schema parse (if schema exists)

Common failure patterns:
- missing licence/contact
- “identifier” present but not stable (temporary URL, local path)



### L2 static checks (REQ-META-004/005/006, REQ-SEM-001/002/003, REQ-PROV-001/002/003)

Checklist:
- Identifier stability and version/supersession evidence (REQ-META-004)
- Schema/profile reference where applicable (REQ-META-005)
- JSON-LD metadata or deterministic transform output where applicable (REQ-META-006)
- Controlled vocabulary IDs/mappings where applicable (REQ-SEM-001/002/003)
- Provenance/lineage for derived/enriched datasets where applicable (REQ-PROV-001/003)
- Release versioning and change history (REQ-PROV-002)

Typical evidence:
- version table (version → release date → changes → supersedes)
- transformation description and deterministic output sample (if transform used)
- vocabulary references (URI-based) + mapping artefact location (if used)
- provenance statements including tools/parameters for derived datasets

Common failure patterns:
- version exists but overwrites previous release
- vocabulary identifiers are non-resolvable strings with no mapping
- provenance is narrative only, not machine-actionable



### L3 static + operational checks (REQ-SEM-004/005/010, REQ-MON-010)

Checklist:
- RDF representation available (REQ-SEM-004)
- SHACL shapes provided and SHACL validation report passes (REQ-SEM-005)
- URI stability/deprecation discipline evidence (REQ-SEM-010)
- Semantic drift monitoring evidence where applicable (REQ-MON-010)

Typical evidence:
- RDF dump or SPARQL endpoint reference + version tag
- SHACL shapes (versioned) + validation output (pass/fail + error list)
- URI policy (how deprecation is signalled; no silent disappearance)
- monitoring outputs (trend reports, drift reports, alert history)

Common failure patterns:
- SHACL shapes provided but not versioned / not accessible
- SHACL report exists but is not reproducible (no input/version captured)
- URIs change between releases without deprecation/mapping plan



## Output expectations

The dataset conformance report should include:
- dataset id + version
- claimed level
- requirement-by-requirement results with evidence pointers
- validation class used (static/dynamic/operational/manual)

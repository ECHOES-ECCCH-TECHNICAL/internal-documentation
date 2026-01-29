# Semantic validation 

## Inputs (evidence package)

Minimum:
- asset identifier + version
- authoritative location (URI)
- declared dependencies/imports/references
- governance contact / maintenance contact
- changelog or change policy (where required)
- if L3 claimed: RDF + SHACL shapes + SHACL report

Recommended:
- sentinel queries/checks (for SPARQL endpoints)
- drift monitoring outputs (trend reports, alerts)
- deprecation policy for URIs


## L2 static checks (REQ-SEM-007/002/003/008/009)

Checklist:
- Versioning, changelog, maintenance contact, change policy (REQ-SEM-007)
- Stable identifiers; dereferenceable where provider-controlled (REQ-SEM-002)
- Language tags for multilingual labels where applicable (REQ-SEM-003)
- Mapping traceability to source/target versions where applicable (REQ-SEM-008)
- JSON-LD context integrity where used (REQ-SEM-009)

Common evidence:
- SKOS concept scheme + version IRI
- mapping file with explicit source/target version identifiers
- JSON-LD @context resolvability proof + deterministic expansion sample


## L3 static + operational checks (REQ-SEM-004/005/010, REQ-MON-010)

Checklist:
- RDF representation available (REQ-SEM-004)
- SHACL shapes and validation report (REQ-SEM-005 where constraints claimed)
- URI stability/deprecation discipline (REQ-SEM-010)
- Drift monitoring evidence where applicable (REQ-MON-010)

Common evidence:
- SHACL shapes (versioned) + validation output tied to input version
- monitoring reports: broken URIs, SHACL trend pass/fail, mapping drift reports


## Output expectations

The semantic conformance report should reference:
- artefact locations + versions
- validation outputs (SHACL reports, context expansion checks)
- drift monitoring evidence (if required by claimed level)

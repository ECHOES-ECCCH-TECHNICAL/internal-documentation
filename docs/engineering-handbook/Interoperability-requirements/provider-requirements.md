# Interoperability requirements (provider obligations)

This page mirrors the **normative requirements** defined in the official deliverable (PDF), Chapter 5.  
It is provided for **operator/provider convenience** and for linking to living implementation assets (templates, checklists, example evidence packages).  
If any conflict exists, the **PDF is authoritative**.

---

## What this chapter covers

The interoperability framework is **evidence-driven** and used for:
- onboarding decisions,
- assigning L1/L2/L3 levels,
- validation and revalidation over time.

Requirements are written to be **objectively verifiable** via artefacts and/or runtime behaviour.

---

## Interpretation rules

- **MUST/SHALL**: mandatory; failure blocks the claimed level (or blocks onboarding if explicitly blocking)
- **SHOULD**: strong recommendation; normally non-blocking unless stated
- **MAY**: optional

Evidence rule: **missing evidence is treated as non-compliance** for mandatory requirements.

---

## Cross-cutting requirement groups (canonical IDs)

### Metadata & semantics (L1→L3)
Core IDs: `REQ-META-001..006`, `REQ-SEM-001..010`, `REQ-PROV-001..003`, `REQ-MON-010` (L3 semantic drift).

### APIs & services (L1→L3)
Core IDs: `REQ-API-001..020` (as applicable), especially OpenAPI, conformance, error model, pagination, versioning/deprecation, and health/readiness.

### Deployment & operability (hosted)
Core IDs: `REQ-DEP-001`, `REQ-DEP-004/005/007/008/010/011/013/015`.

### Security & access control
Core IDs: `SEC-01` (blocking), `SEC-03`, and for restricted resources `SEC-04/07/09/11`, plus `SEC-15/16/17/18`.

### Monitoring & lifecycle
Core IDs: `REQ-MON-001/002/004/006/009/011/012` (as applicable).

---

## Resource types: what evidence is expected

### Datasets
Minimum evidence:
- machine-readable metadata + identifier + licence (`REQ-META-001/002/003`)
- L2+: versioning/supersession (`REQ-META-004`), schema/profile where relevant (`REQ-META-005`), JSON-LD or deterministic transform (`REQ-META-006`)
- derived/enriched outputs: provenance/versioning (`REQ-PROV-*`)
- L3: RDF + SHACL + validation report (`REQ-SEM-004/005`) + semantic drift monitoring (`REQ-MON-010`)

### Applications
Minimum evidence:
- metadata baseline (`REQ-META-001/002/003`)
- if hosted: TLS + endpoint classification (`SEC-01`, `SEC-03`) + incident contact (`REQ-MON-001`)
- if restricted: AAI integration and access enforcement (`SEC-04/07/09/11`)
- if APIs exist: applicable `REQ-API-*`

### APIs / Web services
Minimum evidence:
- L1+: service identification (`REQ-API-001`), TLS (`SEC-01`), endpoint classification (`SEC-03`)
- L2+: OpenAPI + conformance (`REQ-API-002/003`), error model (`REQ-API-007`), pagination (`REQ-API-010`), versioning/deprecation (`REQ-API-013/014/015`), health/readiness (`REQ-API-016/017`)
- restricted: AAI/token validation/access matrix evidence (`SEC-04/07/09/11`)

### Semantic artefacts
Minimum evidence:
- versioned identifiers + owner/contact
- resolvable/versioned JSON-LD contexts where used (`REQ-SEM-009`)
- stable vocab identifiers and language tagging where applicable (`REQ-SEM-002/003`)
- L3: RDF + SHACL + validation report (`REQ-SEM-004/005`) + drift monitoring (`REQ-MON-010`)

### Workflows
Minimum evidence:
- workflow metadata baseline
- provenance/lineage/versioning for outputs where applicable (`REQ-PROV-*`)
- if exposed as a service: apply `REQ-API-*`, `REQ-DEP-*`, security and monitoring obligations

### External repositories / integration
Minimum evidence:
- statement of what is authoritative vs transformed/cached
- OpenAPI where L2+ APIs are exposed
- provenance of transforms and mapping discipline where semantics are involved
- rights/licence propagation evidence (no silent policy changes)

---

## Level assignment summary (L1/L2/L3)

A resource is assigned the **highest level** where:
1) all **blocking** requirements pass,
2) all applicable **mandatory and level-gating** requirements pass,
3) required evidence exists.

### Prohibited practices (must not occur)
- overwriting published versions of artefacts without version bump,
- silent contract/behaviour changes without versioning and changelog,
- bypassing declared security mechanisms,
- inconsistent policy enforcement (declared vs implemented),
- silent semantic meaning changes (URIs/contexts/mappings) without deprecation/transition discipline.

---

## Living documentation assets (recommended to keep in the wiki)

These items are *not* good candidates for the PDF (they evolve), but are valuable here:

- Evidence package templates (dataset/app/api/workflow)
- Endpoint inventory template (public/restricted/internal)
- OpenAPI contract checklist + conformance test how-to
- SHACL validation how-to + drift monitoring runbook
- Example conformance reports and “minimum evidence bundles”

(Add links here as you create them.)

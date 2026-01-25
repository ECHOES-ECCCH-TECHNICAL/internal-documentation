# Change control & versioning (D6.2 Chapter 10)

This page operationalises the normative change request (CR) lifecycle, backward compatibility policy, semantic versioning, and deprecation discipline.

---

## What triggers an update

Updates MAY be triggered by:
- new project needs (new resource types, workflows),
- external standards changes (e.g., OpenAPI, SHACL, IIIF, OIDC/OAuth),
- security advisories,
- operational evidence (recurring failures indicating unclear or impractical requirements).

---

## CR lifecycle (mandatory)

### 1) CR submission (required fields)
- title
- requestor
- scope + rationale
- impacted identifiers (REQ/SEC/NODE)
- backward compatibility analysis
- proposed effective date
- draft migration approach
- supporting links/evidence

### 2) Impact assessment (mandatory)
Assess impact across:
- **interoperability/levels** (what levels change, what is gating),
- **validation/tooling** (tests affected, new checks),
- **migration burden** (providers/nodes/operators).

### 3) Draft publication
A draft MUST include:
- diff summary (added/changed/deprecated),
- proposed migration rules,
- review window.

### 4) Review and approval
- technical review (TVT/OFT as applicable),
- governance approval (IGB for normative impacts),
- decision recorded with unique ID.

### 5) Release and communication
Publish updated framework version and provider/operator guidance.

---

## Backward compatibility policy

Updates are classified as:
- **Patch**: clarifications, editorial corrections (no new obligations).
- **Minor**: new optional recommendations or new checks that do not change mandatory thresholds.
- **Major**: new mandatory requirements, changed gating rules, or changed level definitions.

Major changes MUST include migration periods and explicit deprecation schedules.

---

## Framework versioning

The framework SHALL use semantic versioning: **MAJOR.MINOR.PATCH**.

Each published version MUST include:
- release date,
- changelog,
- migration guidance (if not patch-level),
- list of deprecated items.

---

## Deprecation discipline

When a requirement, template, or validation rule is deprecated:
- it MUST remain supported for a defined deprecation window,
- replacements MUST be provided,
- providers MUST be given an upgrade path.

Deprecations MUST NOT silently reduce interoperability assurances.

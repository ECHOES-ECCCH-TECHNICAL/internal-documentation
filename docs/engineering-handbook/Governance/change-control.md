# Change control

This page operationalises the Change Request lifecycle, backward compatibility policy, semantic versioning, and deprecation discipline used to maintain the interoperability framework.

Normative baseline: the change management and versioning controls in D6.2.

## What triggers an update

Updates MAY be triggered by:

- new project needs, for example new resource types, new workflows, pipeline requirements
- changes in external standards, for example OpenAPI, SHACL, IIIF, OIDC and OAuth profiles
- security advisories requiring stricter controls
- operational evidence, for example recurring conformance failures indicating unclear or impractical requirements

## Change Request lifecycle

All updates MUST follow a formal Change Request lifecycle.

### 1) CR submission

A CR submission MUST include:

- title
- requestor
- scope and rationale
- impacted chapters and identifiers, REQ, SEC, NODE
- backward compatibility analysis
- proposed effective date
- draft migration approach
- supporting links and evidence

### 2) Impact assessment

Assess impact across:

- interoperability and levels, levels affected and gating rules impacted
- validation and tooling, tests affected and new checks required
- migration impact on providers, nodes, and operators

### 3) Draft update publication

A draft MUST include:

- diff summary, added, changed, deprecated requirements, rules, templates
- proposed migration rules
- review window

### 4) Review and approval

- technical review by TVT and or OFT as applicable
- governance approval by IGB for normative impacts
- recorded decision with a unique ID

### 5) Release and communication

Publish the updated framework version and provider and operator guidance.

## Backward compatibility policy

Updates are classified as:

- Patch: clarifications and editorial corrections, no new obligations
- Minor: new optional recommendations or new checks that do not change mandatory thresholds
- Major: new mandatory requirements, changed gating rules, or changed level definitions

Major changes MUST include migration periods and an explicit deprecation schedule.

## Framework versioning

The interoperability framework SHALL use semantic versioning: MAJOR.MINOR.PATCH.

Versioning applies to:

- requirements catalogue, REQ, SEC, NODE
- level definitions
- validation workflow and test rules
- node requirements
- templates

Each published version MUST include:

- release date
- change log
- migration guidance, if not patch level
- list of deprecated items, REQ IDs, templates, test suites

## Deprecation discipline

When a requirement, template, or validation rule is deprecated:

- it MUST remain supported for a defined deprecation window
- replacements MUST be provided, new REQ ID or updated template
- providers MUST be given an upgrade path

Deprecations MUST NOT silently reduce interoperability assurances.
If a requirement is removed, equivalent assurance MUST be maintained through replacement controls or revised level definitions.

## Template governance

To support consistent onboarding and validation, templates SHALL be maintained as versioned artefacts and MUST:

- map fields directly to relevant REQ and SEC identifiers
- provide validation guidance, static, dynamic, operational checks
- be change controlled through the Change Request lifecycle defined in this page

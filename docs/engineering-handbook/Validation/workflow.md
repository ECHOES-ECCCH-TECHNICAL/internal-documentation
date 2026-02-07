# Validation Workflow

This page expands the normative validation workflow into operational steps with checklists and expected outputs.
It is designed to be used by validators and providers to prepare evidence packages and run repeatable checks.


## 1) Submission checklist (provider)

A submission package should include:

- resource identifier + version (or immutable release identifier)
- declared interoperability level and resource type(s)
- machine-readable metadata record location
- required artefacts (OpenAPI/schema/SHACL/etc., as applicable)
- runtime endpoints (if applicable) and access classification (public/restricted)
- owner/steward contact + escalation route
- links to change notes (release notes/changelog), where applicable


## 2) Validator triage

The validator:

1. confirms scope and claimed level/type,
2. checks that the evidence package is complete,
3. selects the applicable checklists and validation classes (static/dynamic/operational/manual),
4. prepares a validation run plan (including whether staging environments are used).


## 3) Execute validation runs

### 3.1 Static validation
- parse and validate contracts/schemas/shapes
- validate required metadata fields and identifier rules
- confirm versioning and change documentation exists

### 3.2 Dynamic validation (where runtime endpoints exist)
- probe representative endpoints (positive + negative tests)
- run contract conformance tests (where test suites exist)
- verify access rules for restricted endpoints

### 3.3 Operational validation (where applicable)
- verify health/readiness endpoints and behaviour
- confirm telemetry accessibility for federation analytics where required/declared
- evaluate drift monitoring outputs for semantic assets where required/declared

### 3.4 Supervised/manual validation (only when needed)
Used for workflows that cannot be validated reliably without a UI or human action.
Example: **application feedback capture** validation:
- confirm a visible UI trigger exists (e.g., “Feedback” button)
- confirm informed consent is displayed before data capture
- confirm pseudonymous handling for authenticated users (OIDC `sub`) and anonymous guest submissions
- capture a network trace proving end-to-end submission to the survey endpoint
- verify graceful degradation when the evaluation backend is unavailable (does not block core functionality)

## 4) Outputs checklist (validator)

Every validation run should produce:

- conformance report (requirement-by-requirement, with evidence pointers)
- raw validator outputs (logs, lint reports, SHACL reports, probe results)
- a minimal evidence index (paths/URLs, timestamps, checksums where feasible)
- remediation guidance for each failure (what to change and how to re-test)

## 5) Closure and reassessment

- Mark results PASS/FAIL only when evidence is archived.
- Reassessment is triggered by:
- 
    - new versions/releases,
    - schema/profile/policy changes,
    - dependency upgrades that affect behaviour,
    - persistent monitoring failures (drift, availability, auth failures).

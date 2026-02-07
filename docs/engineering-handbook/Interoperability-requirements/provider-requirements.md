# Interoperability requirements for providers

This page mirrors the normative provider obligations defined in D6.2 for onboarding CH Cloud resources:

- datasets
- services and APIs
- applications
- workflows
- semantic artefacts
- integrations

## What this page covers

The interoperability framework is evidence driven and used for:

- onboarding decisions
- assigning L1, L2, and L3 interoperability levels
- validation and revalidation over time

Requirements are written to be objectively verifiable via submitted artefacts and or runtime behaviour.

## Interpretation rules

- Blocking: failure blocks onboarding, for example SEC-01 TLS for any externally reachable endpoint
- Level gating: failure blocks the claimed level and triggers downgrade to the highest satisfied lower level
- Mandatory: MUST or SHALL requirements required for applicable scope
- Recommended: SHOULD requirements that strengthen robustness and are normally non blocking unless governance makes them gating

Evidence sufficiency rule:

- missing evidence is treated as non compliance for mandatory requirements

## Cross cutting requirement groups

Groups apply as relevant to the resource type.
See the applicability matrices in D6.2 for the authoritative mapping.

### Metadata and discovery

Core IDs:

- REQ-META-001 to REQ-META-006

### Semantics and knowledge integration

Core IDs:

- REQ-SEM-001 to REQ-SEM-010 where controlled fields, vocabularies, mappings, contexts, RDF, or SHACL constraints apply

### Provenance and lineage

Core IDs:

- REQ-PROV-001 to REQ-PROV-003 where transformations, enrichment, or derived outputs exist

### APIs and services

Core IDs:

- REQ-API-001 to REQ-API-020 where interfaces exist

Includes OpenAPI contract and conformance, error model, pagination, versioning and deprecation, health and readiness, and conditional semantic interfaces.

### Deployment and operability

Core IDs:

- REQ-DEP-* for hosted or deployed runtime resources

Includes externalised configuration, portability documentation, repeatable deployment, immutable artefacts, and dependency discipline.

### Security and access control

Core IDs:

- SEC-01 TLS and HTTPS for externally reachable endpoints, blocking
- SEC-03 endpoint classification, public, restricted, internal

For restricted resources and services:

- SEC-04, SEC-07, SEC-09, SEC-11 for authentication, token validation, authorisation enforcement, fail closed behaviour

Supporting obligations commonly include:

- SEC-15, SEC-16, SEC-17, SEC-18 for security logging and traceability, no hardcoded secrets, secrets storage and rotation

### Monitoring, lifecycle, and drift control

Core IDs:

- REQ-MON-001, 002, 004, 005, 006, 007, 008, 009, 010, 011, 012, 013 as applicable

### Data quality

Core IDs:

- REQ-DQ-* for datasets where applicable

### Application evaluation integration

Core IDs:

- REQ-APP-001 for applications where applicable

## Level model and assignment rules

A resource is assigned the highest level for which:

1. all blocking requirements are satisfied
2. all applicable mandatory and level gating requirements for that level are satisfied
3. required evidence exists

Levels are cumulative:

- L2 includes all applicable L1 obligations
- L3 includes all applicable L2 and L1 obligations

If a higher level gating requirement fails, the resource may still be onboarded at the highest lower level whose requirements are satisfied.

## Requirements by level

### Level 1

Minimum onboarding baseline.

Mandatory requirement set for all resource types:

- REQ-META-001 discovery metadata
- REQ-META-002 required metadata fields including licence and reuse statement
- REQ-META-003 globally unique stable identifier

If the resource exposes any externally reachable endpoint:

- SEC-01 blocking TLS and HTTPS enforcement
- SEC-03 endpoint classification, public, restricted, internal

If the resource is operated as a runtime service:

- REQ-MON-001 responsible party and incident contact

Minimum evidence package for L1:

- metadata record satisfying REQ-META-001 and REQ-META-002
- identifier evidence for REQ-META-003
- endpoint inventory and classification if endpoints exist, SEC-03
- TLS proof if endpoints exist, SEC-01
- incident and responsible contact if runtime service exists, REQ-MON-001

Typical block and downgrade conditions for L1:

- any exposed endpoint without TLS blocks onboarding, SEC-01
- missing licence or reuse statement prevents L1 assignment, REQ-META-002
- missing stable identifier prevents L1 assignment, REQ-META-003

### Level 2

Interoperable operations and contracts.

L2 includes all applicable L1 requirements plus the items below, where applicable.

Metadata and semantics:

- REQ-META-004 versioning and supersession discipline
- REQ-META-005 schema or profile declaration where schemas exist
- REQ-META-006 JSON-LD metadata or deterministic transform
- REQ-SEM-001, 002, 003 controlled vocabulary identifiers, stable vocabulary identifiers, language tagging where applicable
- REQ-SEM-009 resolvable and versioned JSON-LD context if used
- REQ-SEM-006 provenance separation for enrichment and derivation where applicable
- REQ-PROV-001, 002, 003 provenance, versioning, and lineage for derived outputs where applicable

APIs and services:

- REQ-API-002 OpenAPI 3.x contract
- REQ-API-003 contract conformance test evidence
- REQ-API-007 machine readable error model
- REQ-API-010 pagination for unbounded collections
- REQ-API-013, 014, 015 versioning, deprecation, no breaking changes within a major version
- REQ-API-016, 017 health and readiness endpoints

Deployment and operability:

- REQ-DEP-004, 005 externalised configuration and portability documentation
- REQ-DEP-007, 008 repeatable deployment and immutable versioned artefacts
- REQ-DEP-010 health and readiness support for orchestration and monitoring
- REQ-DEP-011 logging without secrets and tokens
- REQ-DEP-015 declared external runtime dependencies and graceful failure handling where applicable

Monitoring:

- REQ-MON-002 availability and error rate monitoring
- REQ-MON-004 structured logs and correlation, no secrets and no raw tokens
- REQ-MON-009 contract drift detection in CI and CD for APIs

For restricted services:

- REQ-MON-007, 008 monitoring detects auth failures and unintended anonymous access paths

Security and access control for restricted resources:

- SEC-04 federated authentication integration
- SEC-07 token validation correctness, issuer, audience, signature, expiry
- SEC-09 authorisation enforcement consistency
- SEC-11 fail closed behaviour
- plus SEC-15, 16, 17, 18 as applicable

Lifecycle reassessment:

- REQ-MON-011 revalidation triggers on major changes, release, schema, policy, auth changes, persistent operational failures

Minimum evidence package for L2:

- all L1 evidence
- versioning and supersession policy evidence, REQ-META-004
- JSON-LD metadata or deterministic transform artefacts, REQ-META-006
- schema or profile references where applicable, REQ-META-005
- vocabulary identifier and mapping evidence where applicable, REQ-SEM-001, 002, 003
- provenance and lineage evidence where transformations exist, REQ-PROV-001, 003 plus release history, REQ-PROV-002

For APIs:

- OpenAPI plus conformance test report
- error model evidence
- versioning and deprecation policy evidence
- health and readiness results

For hosted deployments:

- deployment documentation and immutable release artefacts
- logging policy evidence
- monitoring configuration evidence

For restricted resources:

- federated authentication integration evidence
- token validation checks
- authorisation enforcement tests
- security event logging policy

Typical downgrade conditions for L2:

- missing OpenAPI contract or contract mismatch for an API, REQ-API-002, 003
- restricted service without federated authentication integration or incorrect token validation, SEC-04, 07
- missing health and readiness for hosted services, REQ-API-016, 017 or REQ-DEP-010
- missing provenance for derived or enriched outputs, REQ-PROV-001, 003

### Level 3

Advanced semantic and lifecycle guarantees.

L3 includes all applicable L1 and L2 requirements plus the items below, where applicable.

Semantic interoperability:

- REQ-SEM-004 RDF representation accessible
- REQ-SEM-005 SHACL shapes and validation report where constraints are claimed
- REQ-SEM-010 URI stability and deprecation discipline
- REQ-MON-010 semantic and schema drift monitoring for L3 RDF and SHACL assets

Monitoring and lifecycle:

- REQ-MON-006 deployed version exposure and changelog correlation, mandatory for L3
- REQ-MON-012 remediation plan or level downgrade on critical L3 conformance failures

APIs exposing semantic interfaces:

- REQ-API-019 RDF representations via service interfaces
- REQ-API-020 if SPARQL is provided, declare supported features and limits

Minimum evidence package for L3:

- all L2 evidence
- RDF distribution and access mechanism plus URI policy, REQ-SEM-004, 010
- SHACL shapes plus validation report, REQ-SEM-005
- evidence of semantic drift monitoring runs, REQ-MON-010
- version exposure plus changelog correlation evidence for hosted runtime, REQ-MON-006
- remediation and downgrade discipline evidence, REQ-MON-012

## Resource types and minimum evidence expectations

These lists are summaries.
The resource type applicability matrices in D6.2 define the authoritative mapping.

### Datasets

Minimum evidence:

- machine readable metadata plus identifier plus licence, REQ-META-001, 002, 003
- L2 and above: versioning and supersession, REQ-META-004; schema and profile where relevant, REQ-META-005; JSON-LD or deterministic transform, REQ-META-006
- derived and enriched outputs: provenance, versioning, lineage, REQ-PROV-*
- L3 semantic claim: RDF plus SHACL plus validation report, REQ-SEM-004, 005, plus drift monitoring, REQ-MON-010
- data quality where applicable: REQ-DQ-*

### Applications

Minimum evidence:

- metadata baseline, REQ-META-001, 002, 003
- if endpoints exist: TLS plus endpoint classification, SEC-01, SEC-03
- if hosted: deployment and operability evidence, REQ-DEP-* plus monitoring evidence, REQ-MON-* as applicable
- if restricted: authentication and enforcement, SEC-04, 07, 09, 11
- L2 and above where applicable: evaluation feedback mechanism evidence, REQ-APP-001
- L2 and above where applicable: telemetry accessibility, REQ-MON-013

### APIs and web services

Minimum evidence:

- L1: service identification, REQ-API-001; media types plus UTF-8 behaviour, REQ-API-005, 006; TLS, SEC-01; endpoint classification, SEC-03
- L2 and above: OpenAPI plus conformance, REQ-API-002, 003; error model, REQ-API-007; pagination, REQ-API-010; versioning and deprecation, REQ-API-013, 014, 015; health and readiness, REQ-API-016, 017
- restricted: authentication, token validation, access enforcement evidence, SEC-04, 07, 09, 11
- monitoring and drift: availability and error monitoring plus logs, REQ-MON-002, 004; CI contract drift detection, REQ-MON-009; restricted auth failure and anonymous path monitoring, REQ-MON-007, 008

### Semantic artefacts

Includes vocabularies, ontologies, mappings, and shapes.

Minimum evidence:

- versioned identifiers plus owner and contact plus change policy, REQ-SEM-007
- stable term URIs and dereferenceability where provider controlled, REQ-SEM-002
- language tagging for multilingual labels where applicable, REQ-SEM-003
- mapping traceability where mappings exist, REQ-SEM-008
- if JSON-LD contexts are used: resolvable and versioned contexts, REQ-SEM-009
- L3 constraints and claims: RDF plus SHACL plus validation report, REQ-SEM-004, 005, plus drift monitoring, REQ-MON-010

### Workflows

Minimum evidence:

- workflow metadata baseline plus stable identifier, REQ-META-001, 002, 003
- workflow version and change history, REQ-PROV-002
- lineage, inputs and processing steps for outputs, REQ-PROV-003
- provenance capture and separation for derived outputs where applicable, REQ-PROV-001
- if executed as a service: apply API plus deployment plus monitoring runtime requirements, REQ-DEP-* and REQ-MON-* as applicable
- if restricted: authentication and enforcement, SEC-04, 07, 09
- if workflow outputs RDF assets and claims L3: RDF and SHACL evidence plus drift monitoring, REQ-SEM-004, 005 and REQ-MON-010

### External repositories and integration cases

Applies only where CH Cloud integrates or federates with external repositories.

Integration must ensure at minimum:

- discovery metadata and reuse conditions are available, REQ-META-001, 002, 003
- access policy enforcement is consistent for restricted resources, SEC-01 and SEC-04, 07, 09 where applicable
- monitoring detects integration drift for critical dependencies, REQ-MON-002, 011

A provider may satisfy these obligations by supplying mapping and bridge services that meet applicable API, security, and monitoring requirements.

## Prohibited practices

The following must not occur:

- overwriting published versions of artefacts without explicit versioning or supersession
- silent contract and behaviour changes without versioning and a changelog
- bypassing declared security mechanisms
- inconsistent policy enforcement, declared versus implemented
- silent semantic meaning changes, URIs, contexts, mappings, without deprecation and transition discipline


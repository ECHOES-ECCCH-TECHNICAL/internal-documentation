# Storage patterns

This page provides implementation guidance for storage that supports CH data types (large binaries, derived artefacts, semantic files) while satisfying node storage and synchronisation requirements.


## Object storage (S3-compatible) reference pattern

Recommended for:

- images, 3D assets, audiovisual files
- workflow outputs and derived artefacts

Implementation guidance:

- bucket naming conventions and lifecycle policies
- versioning strategy for immutable artefacts (do not overwrite published versions; explicit supersession)
- integrity controls (checksums) for large objects


## Access-policy alignment checklist (NODE-STO-02)

Key rule: **storage exposure must match declared access policy**.

Implementation guidance:

- public objects are anonymously readable **only if explicitly declared public**
- restricted objects require **authenticated/authorised** access at the enforcement point (gateway/service layer)
- adopt **deny-by-default** for restricted data and least-privilege IAM policies
- audit logs record policy decisions without leaking secrets/tokens



## Immutability and cache discipline (NODE-SYNC-02 / NODE-SYNC-03)

Implementation guidance:

- never overwrite published immutable versions of:
    - deployable artefacts
    - published API contracts/specifications
    - semantic shapes/constraints
- introduce explicit version identifiers and supersession links
- for caches that serve metadata or policy decisions:
    - define TTL and/or invalidation rules
    - verify updates propagate within a bounded time window



## Backup and recovery for stateful services (NODE-STO-03)

Implementation guidance:

- backup cadence and retention policy (aligned with criticality)
- restore testing procedure (record dates and outcomes)
- documented RTO/RPO targets for critical services
- maintain evidence of periodic restore drills for onboarding and revalidation

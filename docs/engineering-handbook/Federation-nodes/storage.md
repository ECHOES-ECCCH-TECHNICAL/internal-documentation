# Storage patterns and access-policy alignment (Living Documentation for D6.2 Chapter 8 §8.2.3)

This page provides implementation guidance for storage that supports CH data types (large binaries, derived artefacts, semantic files) while satisfying node security and policy requirements.


## Object storage (S3-compatible) reference pattern

Recommended for:
- images, 3D assets, audiovisual files
- workflow outputs and derived artefacts

Implementation guidance:
- bucket naming conventions and lifecycle policies
- versioning strategy for immutable artefacts (never overwrite published versions)
- integrity controls (checksums) for large objects


## Access-policy alignment checklist

Key rule: storage exposure must match declared access policy.

Implementation guidance:
- public objects are anonymously readable only if explicitly declared public
- restricted objects require authentication/authorisation at the enforcement point (gateway/service layer)
- audit logs for policy decisions (no secrets)

## Backup and recovery for stateful services

Implementation guidance:
- backup cadence and retention policy
- restore testing procedure
- documented RTO/RPO targets for critical services

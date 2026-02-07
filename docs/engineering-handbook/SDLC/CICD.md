# CI/CD

CI/CD turns delivery into a routine, repeatable process.
It provides fast feedback on every change, enforces quality gates, and creates an audit trail that supports interoperability assurance across partners.

## Baseline pipeline stages

Recommended baseline stages:

1. checkout and dependency resolution
2. linting and static analysis
3. security scans, secret scanning and dependency scanning
4. unit tests, fast feedback
5. integration tests, contracts and dependencies
6. package artefacts, images and binaries, and tag releases
7. deploy to staging, if required by policy
8. post‑deploy validation, smoke tests
9. promote to production, approval gate where required

Failures should be visible and actionable.
A failing pipeline should block promotion.

## Quality gates

Practical minimum gates for merge and promotion:

- unit tests pass
- integration tests pass for relevant components
- OpenAPI and contract validation passes where applicable
- no secrets detected in changes
- no critical CVEs in release artefacts, or an approved exception exists
- peer review approval

## Release traceability

A release should be traceable across the full chain:

- commit → tag → build → artefact digest → deployment

Recommended practices:

- build immutable artefacts, deploy by digest, not `latest`
- expose `/version` or equivalent
- retain CI logs and artefacts for a defined period

## Environment promotion model

Promote the same artefact through environments:

- staging validates the release candidate
- production receives the identical artefact, same digest
- rollbacks re‑point to a known‑good artefact

## Security in CI/CD

Minimum security controls:

- secret scanning on pull requests
- dependency scanning, SCA, on pull requests and nightly
- container scanning on release images
- policy‑as‑code checks where applicable, IaC rules and RBAC constraints

## Related pages

- [Testing](testing.md)
- [Deployment, environments, and versioning](deployment-environments-and-versioning.md)
- [Security](security.md)

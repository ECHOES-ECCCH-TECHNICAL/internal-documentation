# Code Versioning and Open-Source Practice

In a distributed, multi-partner project, version control is the foundation for accountability and collaboration. Open-source practices further support transparency, reuse, and long-term sustainability.

This page describes practical Git workflows, semantic versioning, and repository governance patterns.


## Baseline expectations

- all code and infrastructure definitions are in Git
- changes to shared branches flow through PR/MR review
- releases use Semantic Versioning (SemVer) where applicable
- repositories declare a licence and contribution rules
- public repositories are preferred unless restrictions are justified


## Branching and collaboration (recommended)

A simple, effective model for many teams:
- `main` (stable)
- feature branches: `feature/<name>`
- fixes: `fix/<name>`
- optional `release/<x.y.z>` branch for stabilisation

Trunk-based development is acceptable when CI is strong and teams can keep changes small and well-tested.


## Semantic Versioning (SemVer)

Use `MAJOR.MINOR.PATCH`:
- MAJOR: breaking changes
- MINOR: backward-compatible features
- PATCH: backward-compatible bug fixes

Recommended release artefacts:
- changelog entry (human-readable)
- tag and release notes
- migration notes for breaking changes
- interface contract version notes (OpenAPI/event schemas) where relevant


## Open-source and contribution governance

### Contribution flow
- issues track work and decisions
- PR/MR includes rationale, tests, documentation updates
- CI gates must pass before merge
- peer review required

Where required by governance, apply a contribution mechanism (CLA or DCO).

### Required repository files (recommended)
- `README.md` (purpose, quick start)
- `LICENSE`
- `CONTRIBUTING.md`
- `CODE_OF_CONDUCT.md` (optional but useful)
- `SECURITY.md` (reporting and disclosure)
- `CHANGELOG.md` (or GitHub Releases discipline)


## Licensing guidance (pragmatic)

- software: Apache-2.0 / MIT commonly chosen; copyleft only when justified
- documentation: CC BY 4.0 or CC0 depending on reuse intent

Also review dependency licences for compatibility.


## Related pages
- [Code reviews](code-reviews.md)
- [CI/CD](CICD.md)

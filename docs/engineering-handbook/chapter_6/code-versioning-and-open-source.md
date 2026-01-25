# Code Versioning and Open-Source Nature

In a large, distributed project like ECHOES, version control and disciplined release management are essential to understand **who changed what, when, and why**, and to prevent accidental overwrites. Equally important is an open-source posture that supports transparency, reuse, and long-term sustainability.



## Version Control Best Practices (Git + SemVer)

### Baseline Expectations

All project code is maintained in **Git** repositories (e.g., GitHub/GitLab/Gitea) with the following practices:

- Teams should adopt a clear branching strategy and use pull/merge requests for changes to shared branches
- Releases should follow **Semantic Versioning (SemVer)** to make compatibility predictable across components

### Starting with Git (Minimum Workflow)

- **Commit small, focused changes** with meaningful messages
- **Push to a shared remote repository** regularly
- **Use branches** to avoid direct work on `main`
- **Keep repository history clean and auditable** (no "dump commits" as the norm)

### Branching Models

Choose one branching model and document it clearly. A simple, effective model for many teams:

#### Recommended Branch Structure

- **`main`**: Stable, production-ready code
- **`develop`** (optional): Integration branch for upcoming release
- **`feature/<name>`**: New features or major changes
- **`fix/<name>`**: Bug fixes / hotfixes
- **`release/<x.y.z>`**: Stabilization for a specific release (docs, final QA)

#### Alternative Options

- **Git Flow**: Suitable for larger teams with heavier processes
- **Trunk-based development**: Suitable for fast iteration; requires strong CI discipline

!!! tip "Consistency Matters"
Whichever model you choose, document it in the repository (README/CONTRIBUTING) and keep it consistent across components where feasible.

### Pull Requests and Code Reviews

All changes to shared branches (e.g., `main`, `develop`) should go through pull/merge requests that:

- Link to an issue or work item
- Describe what changed and why
- Keep changes small and reviewable when possible
- Ensure at least one peer review prior to merge

#### Review Focus Areas

- **Correctness and clarity** of the implementation
- **Security and privacy implications** of the changes
- **Compatibility impact** on existing systems
- **Adherence to project conventions** (not personal style preferences)

### Semantic Versioning (SemVer)

Use `MAJOR.MINOR.PATCH` format (e.g., `v2.3.1`):

| Version Component | When to Increment | Example |
|-------------------|-------------------|---------|
| **MAJOR** | Incompatible changes (breaking API/contract behavior) | `1.0.0` → `2.0.0` |
| **MINOR** | Backward-compatible feature additions | `1.0.0` → `1.1.0` |
| **PATCH** | Backward-compatible bug fixes | `1.0.0` → `1.0.1` |

#### Recommended Artifacts Per Release

- Changelog entries (human-readable)
- Machine-readable version tags
- Release notes (especially for breaking changes)
- Explicit API/contract version notes where relevant

### Automation and CI Integration

Pull/merge requests should trigger automated checks where applicable:

- Linting and static code analysis
- Unit tests
- Build and package checks
- Security scanning (SCA, secret scanning) for relevant components



## Open-Source Contribution Policies

ECHOES software outputs are developed with an open-source approach to support transparency, reuse, and sustainability. External contributions are encouraged under a process that protects quality, security, and project integrity.

### Contribution Process

Contributions should follow this workflow:

- Flow through the **issue tracker + PR/MR workflow**
- Trigger **automated checks** (tests/lint/security scans as applicable) before merge
- Require **peer review** for all incoming changes
- Use an **accepted contribution mechanism** (e.g., CLA or DCO) where required by governance

#### Non-Code Contributions

The following non-code contributions are explicitly in scope and welcome:

- Issue reporting and triage
- Documentation improvements
- Usability feedback and examples

### Licensing Guidance

A single project-wide licensing model may be agreed later. Until then, each repository should:

- Clearly declare its license
- Check dependencies for license compatibility
- Include a `LICENSE` file and (where feasible) consistent headers

#### Recommended Licenses

| Asset Type | Recommended Licenses | Notes |
|------------|---------------------|-------|
| Software / source code | Apache-2.0 (preferred), MIT, GPL-3.0 (case-by-case) | Prefer permissive licenses for broad reuse; use copyleft only when strategically required |
| Documentation / non-code content | CC0-1.0, CC BY 4.0, CC BY-SA 4.0 | Choose based on attribution and share-alike needs |

### Repository Governance and Required Files

Repositories should include the following baseline governance controls:

| File / Control | Purpose |
|----------------|---------|
| `README.md` | Description, setup instructions, usage examples, and relevant links |
| `CONTRIBUTING.md` | How to propose changes, commit/PR expectations, and contribution guidelines |
| `CODE_OF_CONDUCT.md` | Collaboration norms and reporting path for issues |
| Mandatory peer review | Quality, maintainability, and security checks |
| CI pipeline gates | Automated tests and checks before merge |
| Release integrity (optional) | Signed releases (e.g., GPG/Sigstore) for critical components |

!!! tip "Maintain Consistency"
Keeping these files aligned across repositories reduces friction for contributors and reviewers, and establishes clear project standards.
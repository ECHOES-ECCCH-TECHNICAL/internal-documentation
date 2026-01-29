# Code Versioning and Open-Source Nature

In software development, especially in large, distributed projects like ECHOES, tracking who changed what, when, and why is fundamental. This not only ensures accountability but also avoids accidental overwrites, enables safe collaboration, and supports long-term maintenance. Equally important is how we share and license our work: by adopting open-source principles, the project fosters transparency, interoperability, and reuse, which are key to cultural heritage preservation and innovation.

## Version Control Best Practices (Git + SemVer)

### Baseline Expectations

All project code is maintained in **Git** repositories (e.g., GitHub/GitLab/Gitea) with the following practices:

- Teams should adopt a clear branching strategy and use pull/merge requests for changes to shared branches
- Releases should follow **Semantic Versioning (SemVer)** to make compatibility predictable across components
- All project-related code must be stored in Git repositories, typically hosted on platforms like GitHub or GitLab
- Public repositories should be used for most project code unless specific components require restricted access

### Starting with Git (Minimum Workflow)

Git is the de facto standard for version control and should be used by all development teams. Even basic Git usage provides a huge improvement over manual file versioning or email-based collaboration. At minimum, teams should:

- **Commit small, focused changes** with meaningful messages (e.g., "correct metadata export logic" not "fix bug")
- **Push to a shared remote repository** regularly to ensure work is backed up and visible to team members
- **Use branches** to avoid direct work on `main` and enable parallel development
- **Keep repository history clean and auditable** (no "dump commits" as the norm)
- Use clear, descriptive commit messages that explain what changed and why

### Branching Models

Choose one branching model and document it clearly. A simple, effective model for many teams:

#### Recommended Branch Structure

A good branching model helps teams develop features independently, fix bugs quickly, and release stable versions confidently. The recommended simple but effective model includes:

- **`main`**: Stable, production-ready code - the stable branch where production-ready code lives
- **`develop`** (optional): Integration branch for upcoming release - the integration branch where features are merged before a release
- **`feature/<name>`**: New features or major changes - used for new features or major changes
- **`fix/<name>`**: Bug fixes / hotfixes - for bug fixes or hotfixes
- **`release/<x.y.z>`**: Stabilization for a specific release (docs, final QA) - for preparing a specific release, including documentation or final tweaks

#### Alternative Options

More complex branching models are available depending on team size and needs:

- **Git Flow**: Suitable for larger teams with heavier processes - can be used for larger teams but may be overkill for smaller ones
- **Trunk-based development**: Suitable for fast iteration; requires strong CI discipline - an option if teams prefer simplicity and fast iterations

!!! tip "Consistency Matters"
Whichever model you choose, document it in the repository (README/CONTRIBUTING) and keep it consistent across components where feasible. This reduces friction for contributors moving between different parts of the project.

### Pull Requests and Code Reviews

All changes to shared branches (e.g., `main`, `develop`) should go through pull/merge requests that:

- **Link to an issue or work item** - ensuring traceability and context
- **Describe what changed and why** - providing clear rationale for reviewers
- **Keep changes small and reviewable when possible** - use small, focused commits with meaningful messages
- **Ensure at least one peer review prior to merge** - maintain code quality and knowledge sharing

Tools like GitHub's built-in review system or standalone tools help with inline comments, discussions, and approvals.

#### Review Focus Areas

Before merging, each pull request should be reviewed by at least one other developer, focusing on:

- **Correctness and clarity** of the implementation - does it work as intended and is the code understandable?
- **Security and privacy implications** of the changes - could this introduce vulnerabilities or data exposure?
- **Compatibility impact** on existing systems - will this break existing integrations or APIs?
- **Adherence to project conventions** (not personal style preferences) - follows established patterns and standards

Reviews should focus on these substantive issues rather than personal style preferences, keeping the process constructive and efficient.

### Semantic Versioning (SemVer)

To keep releases consistent and predictable, all code should follow **Semantic Versioning**. Use `MAJOR.MINOR.PATCH` format (e.g., `v2.3.1`):

| Version Component | When to Increment | Description | Example |
|-------------------|-------------------|-------------|---------|
| **MAJOR** | Incompatible changes (breaking API/contract behavior) | When you make incompatible API changes | `1.0.0` → `2.0.0` |
| **MINOR** | Backward-compatible feature additions | When you add functionality in a backward-compatible manner | `1.0.0` → `1.1.0` |
| **PATCH** | Backward-compatible bug fixes | When you make backward-compatible bug fixes | `1.0.0` → `1.0.1` |

This versioning model helps downstream users and integrators understand whether an update is safe to apply without needing a deep technical review. It makes software updates clear and predictable, helping both developers and users understand the impact of a change before adopting it.

#### Recommended Artifacts Per Release

Each versioned release should include:

- **Changelog entries** (human-readable) - documenting all changes in accessible language
- **Machine-readable version tags** - enabling automated dependency management
- **Release notes** (especially for breaking changes) - highlighting important updates and migration guidance
- **Explicit API/contract version notes** where relevant - clarifying interface compatibility

### Automation and CI Integration

Pull/merge requests should trigger automated checks where applicable:

- **Linting and static code analysis** - catching style and quality issues automatically
- **Unit tests** - verifying core functionality remains intact
- **Build and package checks** - ensuring the code compiles and packages correctly
- **Security scanning** (SCA, secret scanning) for relevant components - identifying vulnerabilities early

This automation ensures that changes won't break existing functionality and makes reviews faster and more objective. Tools like GitHub Actions or GitLab CI can be configured to run these checks automatically.

## Open-Source Contribution Policies

ECHOES software outputs are developed with an open-source approach to support transparency, reuse, and long-term sustainability in the cultural heritage domain. External contributions are encouraged under a process that protects quality, security, and project integrity.

### Contribution Process

Contributions should be submitted via the project's issue tracker and pull/merge request workflow, following this recommended process:

- **Flow through the issue tracker + PR/MR workflow** - all changes start with a documented issue or proposal
- **Trigger automated checks** (tests/lint/security scans as applicable) before merge - ensuring quality standards
- **Require peer review** for all incoming changes - maintaining code quality and knowledge sharing
- **Use an accepted contribution mechanism** (e.g., CLA or DCO) where required by governance - protecting legal clarity

Repositories should apply automated checks (tests, linting, and security scans where applicable) before changes are merged, and maintainers should ensure peer review of incoming changes. Where required by project governance, contributors may be asked to accept a project-defined contribution mechanism (e.g., CLA or DCO).

#### Non-Code Contributions

The following non-code contributions are explicitly in scope and welcome, as they are valuable and should be supported:

- **Issue reporting and triage** - helping identify and prioritize problems
- **Documentation improvements** - enhancing clarity and completeness of project documentation
- **Usability feedback and examples** - providing real-world usage insights and demonstration code

### Licensing Guidance

A single project-wide licensing model may be agreed later. Until then, each repository should:

- **Clearly declare its license** in a LICENSE file
- **Check dependencies for license compatibility** - ensuring legal compliance across the stack
- **Include a `LICENSE` file** and (where feasible) consistent headers in source files

#### Recommended Licenses

The following licenses are recommended based on asset type and project goals:

| Asset Type | Recommended Licenses | Notes |
|------------|---------------------|-------|
| **Software / source code** | Apache-2.0 (preferred), MIT, GPL-3.0 (case-by-case) | Prefer permissive licenses for broad reuse; use copyleft (GPL) only when strategically required. Apache-2.0 is preferred for its patent protection and broad compatibility. |
| **Documentation / non-code content** | CC0-1.0, CC BY 4.0, CC BY-SA 4.0 | Choose based on attribution and share-alike needs. CC0 for maximum freedom, CC BY for attribution, CC BY-SA for copyleft-style sharing. |

Repositories should include a LICENSE file and, where feasible, apply license headers consistently across source files to maintain clear licensing status.

### Repository Governance and Required Files

Repositories should include the following baseline governance controls to support contributor onboarding and maintain quality:

| File / Control | Purpose | Details |
|----------------|---------|---------|
| **README.md** | Description, setup instructions, usage examples, and relevant links | Project description, setup instructions, usage examples, and links to related resources |
| **CONTRIBUTING.md** | How to propose changes, commit/PR expectations, and contribution guidelines | Explains how to propose changes, commit message conventions, and pull request expectations |
| **CODE_OF_CONDUCT.md** | Collaboration norms and reporting path for issues | Establishes collaboration norms and provides a reporting path for conduct issues |
| **Mandatory peer review** | Quality, maintainability, and security checks | Ensures all changes are reviewed for correctness, security, and maintainability |
| **CI pipeline gates** | Automated tests and checks before merge | Tests and automated quality checks that must pass before code can be merged |
| **Release integrity (optional)** | Signed releases (e.g., GPG/Sigstore) for critical components | Cryptographically signed releases for security-critical components, using tools like GPG or Sigstore |

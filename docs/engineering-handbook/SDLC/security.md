# Security

Secure development and deployment practices are essential when components handle sensitive cultural data, connect across institutional boundaries, or operate in public environments. This page focuses on **SDLC and operational security practices** that support interoperability and long-term trust across partners.


## Baseline expectations

Every component should:
- enforce TLS/HTTPS for network endpoints
- integrate authentication/authorisation where required
- protect secrets (no hardcoding, no repo commits)
- scan dependencies and containers for known vulnerabilities
- log security-relevant events (auth failures, access denials) without exposing sensitive data
- provide a clear incident and update process


## Secure secrets management

Secrets (API keys, DB passwords, encryption keys, service tokens) MUST never be hardcoded or committed to version control.

Recommended approaches (choose based on environment):
- environment variables (simple cases)
- Kubernetes secrets (prefer KMS-backed where possible)
- Vault / cloud secrets managers (production, multi-service deployments)

CI/CD rules:
- scope secrets per environment (least privilege)
- mask secrets in logs
- rotate secrets and keep an audit trail
- use secret scanning (and treat findings as blockers)


## Continuous security testing and compliance checks

Automate security checks in pipelines:
- **SAST** (source code scanning)
- **SCA** (dependency vulnerability scanning)
- **container image scanning**
- **DAST** (where applicable for web services)
- **secret scanning**

Recommended gate policy (typical baseline):
- fail builds on secrets detected
- fail builds on critical CVEs unless an approved exception exists
- fail builds on critical container vulnerabilities in release images


## Data protection controls (minimum technical baseline)

Where restricted/sensitive data is processed:
- encrypt in transit (TLS)
- encrypt at rest where feasible (storage + backups)
- enforce least-privilege access
- maintain access logs/audit trails
- apply data minimization and retention rules

Avoid emitting personal data to logs, traces, or events; use pseudonymous identifiers where needed for analytics and evaluation.


## Incident management and secure update policy

Have a defined process for:
- detection and reporting
- severity assessment and containment
- remediation and recovery
- partner communication and post-incident review

Update urgency guidance (illustrative):
- critical vulnerabilities: patch within 24–48h
- high severity: patch within ~1 week
- medium/low: next planned release cycle

Keep records of incidents, decisions, and remediation evidence.


## Evidence artefacts (what to keep)

- CI outputs for security scans (SAST/SCA/container/secret scanning)
- token validation tests (where applicable)
- incident records and remediation notes (for material incidents)
- security configuration summaries (TLS, authz policy, headers where applicable)


## Related pages
- [CI/CD](CICD.md)
- [Deployment, environments, and versioning](deployment-environments-and-versioning.md)
- [Continuous monitoring and feedback loops](continuous-monitoring-and-feedback-loops.md)

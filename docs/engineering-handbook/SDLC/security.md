# Security, Data Protection, and Secrets Privacy

Secure development and deployment practices are essential when components handle sensitive cultural data, connect across institutional boundaries, and operate in public environments. This is not only about protecting software, but also about protecting partner trust and sustaining the CH Cloud as a reliable ecosystem.




## Secure Secrets Management

Secrets (API keys, database passwords, encryption keys, service tokens) must never be hardcoded or committed to version control. They should be managed through dedicated mechanisms and injected at runtime.

### Why Secrets Management Matters

| Reason | Benefit |
|--------|---------|
| **Security** | Reduces blast radius if code/repositories leak |
| **Rotation** | Supports regular credential changes without code updates |
| **Auditability** | Enables "who accessed what, when" tracking |
| **Separation of concerns** | Developers do not require production credentials |

### Recommended Approaches

Choose the appropriate secrets management approach based on your deployment environment:

| Approach                        | Description | Best For |
|---------------------------------|-------------|----------|
| **Environment variables**       | Inject secrets as env vars at runtime | Simple deployments, containers |
| **HashiCorp Vault**             | Central secrets management with access control | Production environments, multiple services |
| **Cloud provider secrets**      | AWS Secrets Manager / GCP Secret Manager / Azure Key Vault | Cloud-native deployments |
| **Kubernetes Secrets** (base64) | K8s built-in secret primitives (prefer KMS-backed when possible) | Orchestrated services |


### Secrets in CI/CD Pipelines

Most CI/CD platforms provide secure secret injection mechanisms:

- **GitHub Actions**: Repository/environment secrets
- **GitLab CI**: Masked/protected variables
- **Jenkins**: Credentials plugin

#### Operational Rules for CI/CD Secrets

- **Mark secrets as masked** to prevent log exposure
- **Avoid printing environment variables** in pipeline logs
- **Scope secrets to environments** and apply least privilege principles
- **Rotate secrets regularly** and audit access patterns

!!! warning "Never Commit Secrets"
Use pre-commit hooks and secret scanning tools to prevent accidental commits of credentials to version control.

### Example: secret rotation without code changes

A typical “good practice” rotation scenario:

- A database password or API token is rotated in the secrets manager.
- The deployment pipeline re-deploys the component (or triggers a rolling restart) to pick up the new value.
- No code change is required; the change is tracked via deployment logs/audit events.
- A post-deploy check confirms connectivity and authentication still succeed.

## Continuous Security Testing and Compliance Checks

Security is continuous, not a one-time effort. Automated checks should be integrated into pipelines to detect issues early and enforce baseline standards.

### Security Testing Categories

| Category | What It Checks | Example Tools |
|----------|----------------|---------------|
| **SAST** (Static Application Security Testing) | Insecure patterns in source code | Bandit, SonarQube, Semgrep |
| **Dependency scanning (SCA)** | Known vulnerable libraries | Dependabot, Snyk, OWASP Dependency-Check, Renovate |
| **Container scanning** | Image vulnerabilities | Trivy, Clair, Grype |
| **DAST** (Dynamic Application Security Testing) | Runtime/web vulnerabilities | OWASP ZAP, Burp Suite |
| **Secret scanning** | Committed credentials | TruffleHog, GitGuardian, git-secrets |

### Dependency Management

Practical guidance for managing dependencies securely:

- **Keep dependencies updated** using automated PRs via Dependabot or Renovate
- **Monitor security advisories** for your dependency ecosystem
- **Pin major versions** but allow patch/minor updates where safe
- **Use lock files** for reproducible builds (`package-lock.json`, `poetry.lock`, `Pipfile.lock`, etc.)
- **Review dependency licenses** for compliance with project requirements

### Container Security

If using containers, follow these security practices:

- **Prefer minimal, well-maintained base images** appropriate to your runtime ecosystem.
- **Run as non-root** where feasible to limit potential impact.
- **Scan images regularly** and rebuild/patch frequently.
- **Remove unnecessary packages/tools** to reduce attack surface.
- **Use multi-stage builds** to keep build tools out of runtime images.
- **Sign and verify images** (and/or verify provenance) to strengthen supply-chain security.

### Compliance and Policy Enforcement

Use policy-as-code tools to enforce security and compliance controls automatically:

| Tool | Purpose | Best for |
|---|---|---|
| **OPA** (Open Policy Agent) | Policy enforcement across the stack | General-purpose policy decisions |
| **Checkov** | IaC security scanning | Terraform, CloudFormation, Kubernetes manifests |
| **Kyverno** | Kubernetes-native policy management | K8s admission control and validation |

### Example: security gates in a delivery pipeline

A common baseline for CI/CD gating:

- Fail the pipeline if **secret scanning** detects credentials in changes.
- Fail the pipeline if **dependency scanning** reports a critical CVE without an approved exception.
- Fail the pipeline if **container scanning** reports critical vulnerabilities in the release image.
- Require approval for production deployment if policy checks identify elevated risk.

## Data Protection and Privacy Controls

Components handling restricted or sensitive data must apply data protection controls appropriate to the dataset classification and partner agreements. The objective is to prevent accidental exposure, enable traceability, and ensure appropriate handling over the data lifecycle.

### Data classification (minimum)

| Class | Examples | Baseline controls |
|---|---|---|
| **Public** | Open metadata, public content | Standard security controls |
| **Restricted** | Partner-only datasets, licensed content | AuthN/AuthZ, encrypted transit, access logging |
| **Sensitive** | Personal data, embargoed collections | Strong access control, encryption at rest, minimization, retention limits |

### Minimum technical controls

- **Encryption in transit** (TLS) for all network communication.
- **Encryption at rest** for stored datasets and backups where feasible.
- **Access control** using least privilege and role-based access.
- **Audit logging** for access to restricted/sensitive data (who/what/when).
- **Data minimization**: collect/store only what is required for the use case.
- **Retention and deletion**: define retention periods and deletion processes where applicable.
- **Backups and recovery**: protect backups with controls consistent with the data classification.

### Example: handling restricted datasets across institutions

A typical secure handling pattern:

- Access is granted via role-based authorization (partner roles).
- Data is transferred only over TLS and stored in encrypted volumes/buckets.
- Access is logged and reviewed periodically.
- Derived exports are minimized (only necessary fields) and retained according to an agreed schedule.



## Incident Management and Secure Update Policies

Even with strong prevention measures, incidents can occur. A defined response process minimizes impact and maintains trust across the consortium.

### Incident Response Lifecycle

Follow this structured approach to security incidents:

| Phase | Actions | Key Outcomes |
|-------|---------|--------------|
| **1. Detection & Reporting** | Monitor alerts/logs; provide reporting channels; acknowledge reports promptly | Incident identified and logged |
| **2. Assessment** | Determine severity and scope; identify affected systems/data; classify impact (e.g., CVSS) | Impact understood and prioritized |
| **3. Containment** | Isolate systems; revoke credentials; block malicious traffic | Threat contained and spread prevented |
| **4. Remediation** | Patch/fix vulnerabilities; update configuration; deploy new versions | Root cause addressed |
| **5. Communication** | Notify affected partners/users; be factual; document lessons learned | Stakeholders informed transparently |
| **6. Post-incident Review** | Root cause analysis; update controls; improve detection/response | Future incidents prevented |

### Vulnerability Disclosure Policy

Establish clear expectations for responsible disclosure:

- **Define disclosure timeline** (e.g., 90 days for non-critical issues)
- **Provide contact point** (security email or reporting path)
- **Clarify acknowledgement/credit policy** for security researchers
- **Coordinate remediation** before public disclosure when appropriate
- **Maintain a security advisory page** for historical reference

### Security Update Policy

Manage security updates with appropriate urgency and process:

#### Prioritization by Severity

- **Critical vulnerabilities**: Patch within 24-48 hours
- **High severity**: Patch within 1 week
- **Medium severity**: Include in next regular release cycle
- **Low severity**: Address during planned maintenance

#### Update Best Practices

- **Test patches even under time pressure** to avoid introducing regressions
- **Communicate changes and impact** to affected stakeholders
- **Provide rollback procedures** in case of issues
- **Retain records** of incidents, decisions, and responses for auditability
- **Document lessons learned** to improve future response

---

## External references

### OWASP (application security)
- **OWASP Top 10 (Web Application Security Risks)** 
  https://owasp.org/www-project-top-ten/
- **OWASP ASVS (Application Security Verification Standard)**
  https://owasp.org/www-project-application-security-verification-standard/
- **OWASP Cheat Sheet Series** 
  https://cheatsheetseries.owasp.org/

### NIST (secure development + identity)
- **NIST SP 800-218 (SSDF)** 
  https://csrc.nist.gov/pubs/sp/800/218/final
- **NIST SP 800-63 (Digital Identity Guidelines)**
  https://pages.nist.gov/800-63-4/

### Supply-chain security
- **SLSA (Supply-chain Levels for Software Artifacts)** https://slsa.dev/
- **OpenSSF SLSA project** https://openssf.org/projects/slsa/

### Infrastructure hardening (containers / Kubernetes)
- **Kubernetes Security (official docs)**  https://kubernetes.io/docs/concepts/security/
- **Kubernetes: Secrets good practices (official docs)** https://kubernetes.io/docs/concepts/security/secrets-good-practices/
- **Kubernetes Pod Security Standards (official docs)** https://kubernetes.io/docs/concepts/security/pod-security-standards/

### Configuration baselines
- **CIS Benchmarks** https://www.cisecurity.org/cis-benchmarks

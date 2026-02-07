# Environments and Infrastructure as Code

Components should be promoted through environments with increasing blast radius (e.g., dev → test/staging → production). The environment model should be explicit and reproducible.

## Environment baseline

| Environment | Purpose | Typical properties |
|---|---|---|
| Dev | Rapid iteration | Lower controls, synthetic data, developer-owned |
| Test/Staging | Production-like validation | Production-like config, controlled test data, promotion gates |
| Production | Service delivery | Strict change control, observability, backups, incident process |

## Configuration and secrets

- Treat configuration as code where possible (versioned templates, schema validation).
- **Never commit secrets**; use a secrets manager or environment-specific secret distribution.
- Prefer explicit configuration schemas and validation to prevent partial/invalid deployments.

## Practical patterns

| Pattern | Why it helps |
|---|---|
| Deploy by **digest**, not by mutable tags (e.g., avoid `latest`) | Guarantees the same artifact is running everywhere |
| Validate configuration via **schema checks** before startup | Prevents partial config from causing runtime failures |
| Separate config per environment but keep **one config structure** | Reduces surprises during promotion |
| Store secrets in a manager and inject at runtime | Prevents credential leakage and enables rotation |



## Infrastructure as Code (IaC)

Managing infrastructure manually is risky and hard to audit. Prefer Infrastructure as Code (IaC) so that environments are reproducible, reviewable, versioned, and shareable across teams.

### Benefits of IaC

- **Consistent environments** across test, staging, and production
- **Auditable change history** with version control integration
- **Fast rebuild** in case of failure or disaster recovery
- **Portable blueprints** across providers (cloud/on-premises)

### Tooling overview

| Tool | Focus | Language | Best for |
|---|---|---|---|
| **Terraform** | Infrastructure provisioning | HCL | Cloud resources (VMs, networks, storage) |
| **Ansible** | Configuration management | YAML | Installing software, managing configurations |

### Lightweight deployment options

Even lightweight deployments benefit from codification:

- **Docker Compose** for small, single-host deployments
- **Kubernetes manifests/Helm** for orchestrated services

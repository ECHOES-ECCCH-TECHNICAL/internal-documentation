# Deployment and infrastructure references (D6.2 §3.3)

This page lists commonly adopted standards and tooling patterns for interoperable deployment across heterogeneous environments (on-premise and cloud).

## Deployment models (high-level)
- On-premise deployment may be required for highly sensitive data where local control is mandatory.
- Cloud-native deployment supports scalable, globally accessible services.

## Open container and orchestration standards
- OCI (Open Container Initiative) specifications for container formats and runtimes
- Kubernetes for orchestration of containerised services
- Common ecosystem tools: Helm (packaging), service mesh patterns (where applicable)

## Infrastructure-as-Code and automation
Declarative infrastructure tooling supports repeatable deployments and consistent environments:
- Terraform / Ansible / Pulumi (representative examples)

!!! note
Treat this page as a living reference list. Keep concrete runbooks, environment-specific examples, and operational scripts in the repository (not in the PDF deliverable).

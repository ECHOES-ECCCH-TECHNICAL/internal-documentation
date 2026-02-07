# Infrastructure as Code and Process Codification

CH Cloud components are operated across multiple partners and environments. To reduce drift and “tribal knowledge”, infrastructure and operational processes should be expressed as **code**: executable, version-controlled artefacts that are reviewable and reproducible.

This page provides practical guidance and reference examples.


## What to codify

### Infrastructure definitions
- Terraform / OpenTofu (cloud resources, networks, storage)
- Ansible (configuration and orchestration)
- Dockerfiles and container build scripts
- Docker Compose (local/dev stacks)
- Kubernetes manifests and Helm charts

### Operational processes
- CI/CD workflows (`.gitlab-ci.yml`, GitHub Actions, Jenkinsfiles)
- monitoring setup, dashboards, and alert rules
- backup/restore procedures as scripts
- deployment runbooks and verification scripts
- policy-as-code (RBAC, network policies, admission rules)


## Why codification matters

| Benefit | Operational impact |
|---|---|
| Reproducibility | environments can be rebuilt consistently |
| Auditability | changes are tracked and reviewable |
| Automation | processes are triggerable and testable |
| Disaster recovery | faster rebuild from source-controlled artefacts |
| Consistency | less manual error and reduced drift |
| Collaboration | shared change process via PR/MR review |


## Minimum expectations (pragmatic baseline)

- infrastructure definitions are version-controlled
- environment differences are explicit (dev/staging/prod variables), not ad-hoc edits
- secrets are never committed; injected via a secrets manager mechanism
- changes use PR/MR review with CI validation (lint/plan/schema checks)
- “plan/dry-run” is used where tooling supports it (Terraform plan, Helm diff)


## Testing and validation for IaC

Recommended checks:
- linting (`ansible-lint`, `terraform fmt/validate`, YAML/schema checks)
- policy checks (e.g., IaC security scanners) where appropriate
- smoke verification after apply (service health, connectivity)
- periodic drift audits (declared vs actual state)


## Reference examples (illustrative)

> These examples are **illustrative**. Adapt structure and values to your component and environment.

### Example: Ansible playbook (service deploy)
```yaml
---
- name: Deploy metadata service
  hosts: metadata_servers
  become: yes
  vars:
    service_version: "v2.1.0"
  tasks:
    - name: Pull container image
      docker_image:
        name: "echoes/metadata-service"
        tag: "{{ service_version }}"
        source: pull
    - name: Start service container
      docker_container:
        name: metadata-service
        image: "echoes/metadata-service:{{ service_version }}"
        state: started
        restart_policy: unless-stopped
        ports:
          - "8080:8080"
```

### Example: Docker Compose (local/dev)
```yaml
version: "3.8"
services:
  app:
    build: .
    ports: ["8080:8080"]
  postgres:
    image: postgres:14-alpine
    environment:
      POSTGRES_PASSWORD: dev_password
```

### Example: Kubernetes deployment (snippet)
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: metadata-service
spec:
  replicas: 2
  template:
    spec:
      containers:
        - name: metadata-service
          image: echoes/metadata-service:v2.1.0
          readinessProbe:
            httpGet:
              path: /ready
              port: 8080
```


## Related pages
- [Deployment, environments, and versioning](deployment-environments-and-versioning.md)
- [CI/CD](CICD.md)
- [Security](security.md)

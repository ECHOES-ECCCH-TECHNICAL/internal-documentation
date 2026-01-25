# Deployment and infrastructure (from D6.2 §3.3)

Interoperability depends not only on data formats and APIs, but also on consistent deployment and infrastructure practices. Standardised, scalable, and modular deployment approaches enable services to integrate across heterogeneous platforms and provider environments.

!!! note "Normative boundary"
The official deliverable (PDF) defines the authoritative interoperability requirements.  
This page provides maintained implementation guidance and reference material; it does not introduce new MUST/SHALL obligations.

## Infrastructure models and deployment patterns

### On-premise deployment
On-premise deployments are often required for high data sensitivity or strict institutional control. Interoperability is achieved by:
- exposing services through stable, standards-based APIs,
- adopting consistent identity and access mechanisms,
- using repeatable deployment patterns that can be audited and reproduced.

### Cloud-native deployment
Public cloud providers (e.g., AWS, Azure, GCP) enable scalable, globally accessible services. Interoperability across cloud boundaries benefits from:
- portable packaging and runtime assumptions (containers),
- standard orchestration and service discovery patterns,
- consistent contract and versioning practices across providers.

## Standards and frameworks supporting interoperable deployment

### Open container and orchestration standards
- **OCI (Open Container Initiative)**: specifications for container images and runtimes
- **Kubernetes**: de facto standard for orchestration of containerised services

Common ecosystem tooling (examples; not mandatory):
- **Helm**: packaging and release management for Kubernetes
- **Istio** (service mesh): traffic management, observability, policy enforcement (where justified)
- **KubeEdge**: edge-native deployment patterns (where edge use cases exist)

### Infrastructure-as-Code (IaC) and automation
Declarative IaC tools support repeatable provisioning and reduce environment drift across providers:
- **Terraform**, **Ansible**, **Pulumi** (representative examples)

Recommended practice:
- treat IaC as versioned artefacts in source control,
- provide environment-specific overlays without diverging core logic,
- document prerequisites and assumptions explicitly.

### CI/CD and DevOps pipelines
Version-controlled deployment workflows support repeatability and traceability:
- **GitOps** approaches (e.g., Argo CD, Flux) for declarative, audited deployments
- CI/CD tools (e.g., Jenkins, GitLab CI) to standardise build/test/deploy pipelines

Recommended practice:
- use consistent pipeline stages (build → test → security checks → deploy),
- publish release artefacts and deployment manifests with version identifiers,
- keep secrets out of repositories; integrate with a secrets manager.

## Platform standards enabling interoperability (selected references)

### FIWARE and NGSI
FIWARE provides open-source components for context information management and is commonly deployed via Docker/Kubernetes. It includes the **NGSI** API family, used in some data space and smart systems contexts.

### oneM2M and ETSI standards
- **oneM2M**: reference models for interoperability across IoT platforms
- **ETSI NFV** and **ETSI MEC**: architectures for virtualised network functions and edge computing

!!! tip "Scope guidance"
Treat FIWARE/NGSI, oneM2M, and ETSI references as optional, context-driven standards.  
If they become relevant for CH Cloud components (e.g., sensor/time-series or edge scenarios), document the rationale, integration boundary, and interoperability contracts.

## Practical checklist (for teams)
- Use container images that are OCI-compliant and reproducible.
- Prefer Kubernetes-native deployment patterns for portability (when orchestration is required).
- Manage infrastructure with versioned IaC.
- Use CI/CD (or GitOps) to make deployments repeatable and auditable.
- Keep API contracts and versioning explicit and stable across environments.

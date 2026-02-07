# Node runtime models

This page provides **implementation guidance** for node execution models that can satisfy node requirements in D6.2.
It is **non-binding**: the normative requirements remain the **NODE-*** statements in D6.2 (Federation and Node Requirements).



## Supported execution models (guidance)

Nodes SHOULD document at least one execution model used at the site (for onboarding evidence), e.g.:

- Kubernetes/OpenShift-native execution for containerised services and workflows
- OpenStack/VM-based execution for components requiring VM-level isolation or specialised environments
- Hybrid execution (services containerised; compute-heavy workloads scheduled on CPU/GPU pools)

Regardless of model, operators should be able to evidence:

- isolation boundaries and quotas (NODE-CMP-01)
- accurate time synchronisation (NODE-CMP-02)
- restricted admin surfaces (NODE-SEC-02)
- monitoring coverage and health/readiness probing for hosted services (NODE-MON-01/03)



## Reference pattern A: Kubernetes/OpenShift-native services

Typical characteristics:

- container images built as immutable artefacts
- deployment via manifests/Helm/Kustomize
- namespaces/projects provide isolation boundaries
- ingress with TLS termination and controlled routing

Operational checklist (implementation guidance):

- quotas and limits (CPU/RAM) enforced per namespace/project
- GPU scheduling enabled only where needed (device plugins, node selectors, tolerations)
- time synchronisation validated cluster-wide
- optional: runtime version exposed (`/version` endpoint or service metadata) for correlation



## Reference pattern B: OpenStack/VM-based execution

When useful:

- legacy stacks
- strict VM-level isolation
- specialised OS/kernel requirements

Operational checklist:

- network segmentation and admin-surface restriction via security groups and private networks
- TLS termination for externally reachable endpoints
- immutable image strategy where feasible (golden images, versioned builds)
- logging/metrics export consistent with federation requirements



## Reference pattern C: Hybrid services + compute pools (CPU/GPU)

Typical approach:

- user-facing APIs/services remain containerised
- compute-heavy workloads executed as batch jobs, workflow steps, or queued workers
- GPU pools exposed via scheduler controls

Operational checklist:

- quotas, fair-use, and priority classes defined
- GPU availability and scheduling interface documented
- provenance captures processing environment identifiers for reproducibility (where GPU/HPC is exposed)

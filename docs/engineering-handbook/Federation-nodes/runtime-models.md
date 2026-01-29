# Node runtime models and reference patterns

This page provides **implementation guidance** for node execution models that satisfy the node requirements in the deliverable.
It is **non-binding**: the normative requirements remain the NODE-* statements in D6.2 Chapter 8.

---

## Supported execution models

Nodes must support at least one execution model:
- Kubernetes/OpenShift-native execution for containerised services and workflows
- OpenStack/VM-based execution for components requiring VM isolation or specialised environments
- Hybrid execution (services containerised; compute-heavy workloads scheduled on CPU/GPU pools)



## Reference pattern A: Kubernetes/OpenShift-native services

Typical characteristics:
- container images built as immutable artefacts
- deployment via manifests/Helm/Kustomize
- namespaces/projects provide isolation boundaries
- ingress with TLS termination and controlled routing

Operational checklist (implementation guidance):
- quotas and limits (CPU/RAM) enforced per namespace/project
- GPU scheduling enabled only where needed (node selectors, tolerations, device plugins)
- time synchronisation validated cluster-wide
- runtime version exposed (`/version` endpoint or service metadata)


## Reference pattern B: OpenStack/VM-based execution

When useful:
- legacy stacks
- strict VM-level isolation
- specialised OS/kernel requirements

Operational checklist:
- network segmentation and admin-surface restriction by security groups
- TLS termination for externally reachable endpoints
- immutable image strategy where feasible
- logging/metrics export consistent with federation requirements


## Reference pattern C: Hybrid services + compute pools (CPU/GPU)

Typical approach:
- user-facing APIs/services remain containerised
- compute-heavy workloads executed as batch jobs, workflow steps, or queued workers
- GPU pools exposed via scheduler controls

Operational checklist:
- quotas, fair-use, and priority classes defined
- GPU availability and scheduling interface documented
- provenance captures environment identifiers for reproducibility

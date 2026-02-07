# Node conformance evidence package

This page provides operator-facing templates and checklists to produce the **Node onboard evidence package** required for CH Cloud federation nodes.

Normative baseline: the **NODE-*** requirements and related **SEC-*** / **REQ-MON-*** constraints in D6.2 (Federation and Node Requirements), plus the validation and reassessment discipline (e.g., REQ-MON-011 triggers).


## Evidence rules (apply to all sections)

- Provide **versioned artefacts** (or stable links) with: last-updated date, owner, and change history where applicable.
- For each artefact, list the **requirement IDs** it supports (e.g., NODE-NET-02, NODE-AAI-01).
- Evidence must be **reproducible** (commands, configs, test outputs) and **auditable** (who approved, when).
- If a mandatory requirement is applicable but evidence is missing, treat it as **non-compliance**.


## Evidence package template

### 0) Evidence metadata
- node identifier / name:
- operator organisation:
- evidence package version:
- D6.2 / framework version used:
- date prepared:
- primary contact:
- scope note (what node types / services are in-scope for this evidence):

### 1) Node classification and roles
- node type(s) (non-exclusive): compute / data / service / integration / control-plane participant
- responsibility statement (RACI) covering:
    - Node Operator (platform availability / security)
    - Service Provider (service behaviour / contract conformance)
    - Data Provider (metadata / provenance / access policy)
    - Federation Operator (registries / trust / monitoring integration)
- incident / escalation contact (REQ-MON-001 alignment)

### 2) Ingress and endpoint stability
- published ingress endpoints (base URLs, DNS names, ingress IPs where relevant)
- DNS stability statement (ownership and lifecycle)
- routing approach (gateway / ingress controller / reverse proxy)
- TLS approach (certificate issuer, renewal automation, rotation procedure)

### 3) Security posture
- endpoint classification policy (public / restricted / internal) (SEC-03 alignment)
- admin surface restriction statement (management UIs/APIs not publicly exposed) (NODE-SEC-02)
- secrets mechanism for hosted services (vault / K8s secrets / equivalent) + access controls (NODE-SEC-01)
- security logging posture summary (high-level; no secret/token leakage)

#### 3a) Restricted services (only if the node hosts restricted services)
- IdP / AAI integration summary (e.g., OIDC provider used)
- token validation configuration summary (SEC-07 alignment):
    - issuer(s)
    - audience(s)
    - signature verification method / key rotation handling
    - lifetime/expiry handling
    - bounded clock-skew tolerance
- policy enforcement point (PEP) declaration (SEC-09 alignment):
    - where enforcement happens (gateway / service / both)
    - policy evaluation dependency (if any)
    - fail-closed behaviour statement (SEC-11)

### 4) Runtime capability
- supported execution model(s): containers / VMs / hybrid
- isolation and quotas approach (CPU/RAM/GPU) (NODE-CMP-01)
- time synchronisation approach (NTP/chrony) + expected drift bounds (NODE-CMP-02)

### 5) Registry / discovery integration and drift control
- registry/discovery integration method:
    - what metadata is published (node endpoints, service endpoints, versions)
    - where it is published (registry/catalogue mechanism)
    - who maintains it (role/owner)
- drift-control statement (NODE-REG-02):
    - how runtime vs registry consistency is verified
    - how quickly registry updates follow deployments
    - revalidation trigger path when drift is detected (REQ-MON-011 alignment)

### 6) Storage capability
- storage model(s) used (S3/Ceph/other)
- access-policy enforcement approach (NODE-STO-02):
    - public objects only if declared public
    - restricted objects require authenticated/authorised access
    - deny-by-default stance for restricted
- backup/restore approach for **stateful services** (NODE-STO-03), including:
    - backup cadence and retention
    - restore testing evidence (dates/results)
    - RPO/RTO targets (where defined)

### 7) Monitoring integration
- node monitoring coverage summary (NODE-MON-01):
    - ingress availability
    - platform/storage health relevant to hosted resources
- health/readiness probing approach for hosted services (NODE-MON-03)
- logs/metrics pipeline description (NODE-MON-04 guidance):
    - standard paths / exporters / collection mechanism
    - retention and access controls
    - controls preventing secret/token leakage
- revalidation trigger process and operational escalation (NODE-MON-05; REQ-MON-011 alignment)

### 8) Optional capability HPC/GPU (only if exposed)
- scheduling/quotas for GPU/HPC resources
- how GPU/HPC-backed services still satisfy applicable API/DEP/SEC/MON/PROV requirements
- processing environment identifiers captured for reproducibility (where applicable)

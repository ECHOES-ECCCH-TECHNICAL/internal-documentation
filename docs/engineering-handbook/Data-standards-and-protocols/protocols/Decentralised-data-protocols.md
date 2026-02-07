# Decentralised Data Protocols 

This page surveys **decentralised data protocol patterns** that can be relevant for CH Cloud services, especially where data ownership, fine‑grained sharing, and privacy constraints are central (e.g., **user-generated content**, **personal workspaces**, **private annotations**, **preferences**).


## 1. What “decentralised data” means in practice

A decentralised approach typically introduces at least one of the following shifts:

- **Storage decentralisation:** data is stored outside the application provider’s primary infrastructure (e.g., in user- or institution-controlled stores).
- **Identity decentralisation:** identity is expressed as resolvable identifiers (URIs/DIDs) rather than platform accounts.
- **Policy decentralisation:** access control is attached to the data resource itself (policy travels with the resource).
- **Portability-by-design:** users can move data between tools without exporting from a single vendor platform.

In cultural heritage settings, the decentralised pattern is most compelling for **personal or group-owned derivative data** (annotations, notes, preferences, working sets), while institutional “source-of-truth” catalogues typically remain centralised and curated.


## 2. When decentralised protocols are a good fit (CH Cloud context)

Consider decentralised protocols when you need:

- **Clear ownership boundaries:** institutional records remain institutional; user/group annotations remain user/group.
- **Fine-grained sharing:** share per resource, per group, per time window, with explicit policy.
- **Privacy-preserving personalisation:** store preferences/profile data outside the service provider.
- **Tool portability:** users can switch tools while keeping their annotations/workspaces.
- **Cross-organisation collaboration:** teams work on shared artefacts without copying everything into a single platform.

### When they are usually *not* a good fit
- Bulk publication / large-scale dataset delivery (high throughput, stable institution-owned APIs).
- High-volume ingestion pipelines for collections.
- Media delivery at scale (images/video/3D) as the primary workload.
- Scenarios requiring strict, institution-controlled API surfaces as the only access method.


## 3. Solid (Social Linked Data Protocol)

**Solid** is a W3C-led initiative for **decentralised, user-controlled data storage** using **Pods** (Personal Online Data Stores). It applies Linked Data principles and standard web technologies to enable reading/writing structured data while keeping control of personal or user-owned data with the data subject (or the organisation acting on their behalf), rather than with a single application platform.

Although Solid is not specific to cultural heritage, it is relevant for CH Cloud scenarios involving:
- private or group annotations,
- personal workspaces and working sets,
- preferences and saved queries,
- privacy-focused user profiling for research support (where appropriate).

### 3.1 Core concepts (at a glance)
Solid combines several building blocks:
- **Pods:** user-controlled storage locations for data
- **WebID:** user identity expressed as a URI
- **Solid-OIDC:** OpenID Connect–based authentication for Solid ecosystems
- **Authorisation:** machine-readable access control (WAC and/or ACP)
- **Linked Data resources:** data stored/exchanged using RDF-based representations (e.g., Turtle, JSON-LD)

Operationally, Solid behaves like a web of **dereferenceable resources** with controlled read/write access.

### 3.2 Typical architecture pattern (CH Cloud)
A common CH Cloud-aligned pattern is a **split authority** model:

- **Institutional catalogue (source-of-truth):** records, identifiers, provenance, rights statements.
- **User- or group-owned Pod:** personal annotations, preferences, intermediate research outputs.
- **Application/tool:** reads from the institutional catalogue and writes user-owned artefacts to the Pod.

This yields:
- portability of annotations between tools,
- strong privacy controls,
- reduced vendor lock-in,
- explicit ownership boundaries.

### 3.3 Data formats and interaction model
- Solid is **Linked Data–native** and commonly uses RDF serialisations such as **Turtle** and **JSON-LD**.
- Interaction uses standard HTTP methods:
    - `GET` retrieve resources
    - `POST` create resources
    - `PUT` replace resources
    - `PATCH` partial updates (e.g., RDF patching)

### 3.4 Identity, authentication, and authorisation
- Identity is represented as **WebID** (a URI identifying an agent).
- Authentication commonly uses **Solid-OIDC**.
- Authorisation is expressed as machine-readable policy:
    - **WAC** (Web Access Control): ACL-based model
    - **ACP** (Access Control Policy): newer, more expressive policy model

**Practical note:** If your CH Cloud service already uses OIDC-based authentication, Solid-OIDC aligns conceptually, but integration details (token audience, identity mapping, group claims) must be designed explicitly.

### 3.5 Notifications and change awareness
Some Solid implementations support real-time update mechanisms (notifications). This is useful for:
- collaborative annotation (multiple contributors),
- synchronisation of working sets,
- “watching” resources for changes.



## 4. Interoperability considerations (recommended checklist)

When proposing a decentralised protocol integration, document at least:

### 4.1 Ownership and governance
- What data remains institutional vs user/group-owned?
- Who is the **owner/steward** for each artefact class?
- What is the retention/deletion policy for user-owned content?
- How are deprecations and migrations handled (when vocabularies or schemas evolve)?

### 4.2 Access control and consent
- What is the consent model for storing/sharing personal or user-owned content?
- Is access controlled at resource level, container level, or both?
- How are group memberships represented and managed?
- What is the default policy (“private by default” is typically safest)?

### 4.3 Identifiers and semantic stability
- Ensure stable URIs for artefacts intended for linking.
- Version vocabularies/ontologies/shapes used to describe Pod resources.
- Avoid silent semantic drift in contexts and mappings.

### 4.4 Operational reliability
- Define expected availability and failure modes:
    - What happens if a Pod is offline?
    - How does the application degrade gracefully?
- Define caching rules and conflict resolution for collaborative editing.
- Record enough telemetry (at least at application level) to troubleshoot failures without leaking sensitive content.


## 5. Example scenario: personal annotations stored in a Pod

A curator uses an application to annotate a CH object:

- The object record remains in an institutional catalogue (institution-controlled).
- The annotation record is stored in the curator’s Pod (user-controlled).
- The application reads institutional metadata and writes personal annotations to the Pod.
- Access policies allow sharing annotations with a research group, but not publicly.

This pattern supports:
- portability of annotations between tools,
- clearer ownership boundaries,
- stronger privacy controls.


## 6. References (primary sources)

- Solid project (W3C): https://www.w3.org/standards/semanticweb/data#solid
- Solid specification hub: https://solidproject.org/TR/
- Solid OIDC (authentication): https://solidproject.org/TR/oidc
- WebID (identity): https://www.w3.org/wiki/WebID
- WAC (Web Access Control): https://solidproject.org/TR/wac
- ACP (Access Control Policy): https://solid.github.io/authorization-panel/acp-specification/
- Linked Data principles (W3C): https://www.w3.org/DesignIssues/LinkedData.html

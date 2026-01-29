# Solid (Social Linked Data Protocol)

Solid is a W3C-led initiative for **decentralized, user-controlled data storage** using Pods (Personal Online Data Stores). It applies Linked Data principles and standard web technologies to enable reading and writing structured data in a way that keeps control of personal data with the user (or data subject), rather than with a single platform.

Although Solid is not specific to cultural heritage, it introduces concepts that may be relevant for **user-generated content** and **personalized services** in CH Cloud contexts:

- Fine-grained access control over personal data
- Machine-readable authorization models (WAC and ACP)
- Read/write APIs for Linked Data resources
- Potential support for personalized annotations, preferences, and user profiles

Solid’s approach aligns with FAIR and broader “human-centric” data management discussions in European data spaces.


## What Solid is (at a glance)

Solid combines several building blocks:

- **Pods**: user-controlled storage locations for data
- **WebID**: user identity expressed as a URI
- **Solid-OIDC**: OpenID Connect–based authentication for Solid
- **Authorization**: policies controlling who can access which resources (WAC and/or ACP)
- **Linked Data resources**: data stored and exchanged using RDF-based representations

In practice, Solid behaves like a web of **dereferenceable resources** with controlled read/write access.


## When to use Solid

Solid is best suited to scenarios where individuals (or institutions acting on behalf of individuals) need control over data and sharing:

- User-owned data scenarios (private annotations, preferences, saved searches)
- Research environments where individuals curate their own observations/metadata
- Components requiring read/write interaction with Linked Data resources
- Collaborative workflows where per-user access control is essential

## When not to use Solid

Solid is usually not appropriate for:

- General-purpose institutional dataset delivery (bulk publication at scale)
- Bulk ingestion pipelines for large CH collections
- Cases where providers require stable, institution-controlled APIs as the primary interface
- Media delivery at scale (images, video, 3D) — Solid can reference media, but is not a media delivery protocol


## Relevance to Cultural Heritage (CH Cloud)

Solid may be relevant for:
- future user-generated content and annotation systems,
- personal workspaces for researchers/curators,
- privacy-preserving personalization (preferences and profiles),
- experiments with decentralized approaches to access control.

Solid is **not** expected to be a mandatory mechanism for institutional dataset exposure, but it provides useful patterns for privacy and decentralization that could influence future CH Cloud service designs.


## Technical considerations

### Data model and formats
- Solid is **Linked Data–native** and commonly uses RDF serializations such as **Turtle** and **JSON-LD**.
- Resources should have stable identifiers (URIs) to support linking and reuse.

### HTTP interaction model
Solid uses standard HTTP for resource interaction, typically including:
- `GET` for retrieving resources
- `POST` for creating resources
- `PUT` for replacing resources
- `PATCH` for partial updates (e.g., RDF patching)

### Identity and authentication
- Identity is based on **WebID** (a URI identifying an agent).
- Authentication commonly uses **Solid-OIDC** (OpenID Connect for Solid ecosystems).

### Authorization and access control
Solid supports machine-readable authorization models that enable fine-grained access control:
- **WAC (Web Access Control)**: access control lists for resources
- **ACP (Access Control Policy)**: newer policy model with richer expressiveness

### Notifications / real-time updates
Some Solid implementations support real-time update mechanisms (e.g., notifications), enabling clients to react when resources change.


## Example scenario: Personal annotations stored in a Pod

A curator uses an application to annotate a CH object. Instead of storing annotations in the application’s database, the annotation is stored in the curator’s Pod:

- The object record remains in an institutional catalog (institution-controlled).
- The annotation record is stored in the user’s Pod (user-controlled).
- The application reads institutional metadata and writes personal annotations to the Pod.
- Access policies allow sharing annotations with a research group, but not publicly.

This pattern supports:
- portability of user annotations between tools,
- clearer data ownership boundaries,
- stronger privacy controls.

## References 
- Solid project (W3C): https://www.w3.org/standards/semanticweb/data#solid
- Solid specification hub: https://solidproject.org/TR/
- Solid OIDC (authentication): https://solidproject.org/TR/oidc
- WebID (identity): https://www.w3.org/wiki/WebID
- WAC (Web Access Control): https://solidproject.org/TR/wac
- ACP (Access Control Policy): https://solid.github.io/authorization-panel/acp-specification/
- Linked Data principles (W3C): https://www.w3.org/DesignIssues/LinkedData.html

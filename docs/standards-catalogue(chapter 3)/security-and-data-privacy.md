# Security and data privacy (from D6.2 §3.4)

Security and data privacy are foundational to interoperability within the Cultural Heritage Cloud (CH Cloud). Distributed services, applications, data pipelines, and catalogues can only interoperate reliably when they share a common trust framework, including:
- unified identity and authentication mechanisms,
- consistent authorisation rules,
- secure transport and storage practices,
- machine-actionable rights and access restrictions,
- reproducible deployment security practices,
- verifiable audit and provenance metadata.

!!! note "Normative boundary"
The official deliverable (PDF) defines the authoritative requirements and compliance rules.  
This page provides maintained implementation guidance and reference material for consistent implementation across partners and environments.
Legal and organisational aspects are handled in D6.1.


## 3.4.1 Authentication infrastructure (AAI): EGI Check-in as Identity Provider

**Baseline expectation:** services requiring authentication integrate with **EGI Check-in** to ensure unified login experience and consistent identity semantics across the infrastructure.

### Capabilities relevant for interoperability
- **OIDC**: standard authentication for web and API clients
- **OAuth 2.0**: token-based authorisation for services and automation
- **SAML 2.0**: integration with eduGAIN and institutional IdPs (where required)
- **JWT access tokens**: self-contained tokens enabling local verification
- **Account linking**: supports multiple IdPs under one stable identity
- **Group/role attributes**: enables downstream policy enforcement

### Required identity semantics
- each user is represented by a **persistent unique subject identifier (`sub`)**
- linked identities are merged under a **single stable identity**

**Implementation guidance:**
- avoid creating local user identities that conflict with Check-in’s global subject identifiers
- use the stable identity for access control, provenance metadata, audit trails, and membership history

### Supported protocols
- **OpenID Connect (OIDC)**: recommended for web and API services
- **OAuth2**: service-to-service and delegated authorisation
- **SAML2**: backward compatibility where required

### Supported authentication flows
Services should support one or more flows as appropriate:
- **Authorization Code Flow**: interactive web portals and browser clients
- **Client Credentials Flow**: background jobs and microservices (service-to-service)
- **Device Authorization Flow**: CLI tools and limited UI devices
- **Refresh Token Flow**: session renewal for long-running apps

### Token lifetimes (defaults)
- access token: **1 hour**
- refresh token: **up to 30 days**
  Token lifetimes are enforced by the IdP and should not be extended by clients.

### Required token validation behaviour
Every service should validate:
- signature (via JWKS)
- issuer (`iss`)
- audience (`aud`)
- expiry (`exp`)
- not-before (`nbf`)
- required scopes/entitlements

**Security rule:** tokens must not be logged or stored in plaintext.


## 3.4.2 Authorisation models (RBAC/ABAC and policy enforcement)

Authorisation determines what authenticated users/systems may do. A consistent model is based on:
- Check-in entitlements (roles),
- group membership (virtual organisations and subgroups),
- resource-level rights metadata,
- optional attribute-based restrictions.

### Role and group model
Check-in provides role/group membership via entitlement strings.

**Typical entitlement patterns (examples):**
- `urn:mace:egi.eu:group:vo.chcloud.eu:role=member#aai.egi.eu`
- `urn:mace:egi.eu:group:vo.chcloud.eu:role=admin#aai.egi.eu`
- `urn:mace:egi.eu:group:vo.chcloud.eu:collection-x:role=curator#aai.egi.eu`

Entitlements encode:
- VO identifier,
- optional subgroup (domain/collection/project),
- role,
- authoritative namespace.

### Required authorisation behaviour
- extract roles/groups from OIDC entitlements
- map entitlements to local permissions using documented rules
- avoid maintaining independent/conflicting role stores
- enforce consistent responses:
    - `401 Unauthorized`: missing/invalid token
    - `403 Forbidden`: valid token but insufficient permissions

### RBAC and ABAC support
- **RBAC**: roles define broad capabilities (viewer/editor/curator/admin)
- **ABAC**: attributes constrain access (sensitivity, embargo, rights, affiliation)
  Services may combine both (e.g., role grants write; attribute gates resource access).

### Machine-to-machine authorisation
- OAuth2 Client Credentials flow
- short-lived JWTs
- mTLS where appropriate for internal service links

---

## 3.4.3 API security standards

APIs are the primary interoperability mechanism and must behave securely across institutional boundaries.

### Transport security
- HTTPS/TLS **1.2+** for all services
- disable plain HTTP (redirect or reject)
- prefer strong cipher suites; avoid deprecated algorithms
- internal services may enforce **mTLS** where appropriate

### Token handling
- accept only OIDC JWTs issued by EGI Check-in (where auth applies)
- pass tokens via `Authorization: Bearer <token>`
- cookies only for browser flows and must be `Secure` + `HttpOnly`
- never log access tokens
- validate signature/time/audience/expiry

### API authorisation patterns
- **Method-level** rules: endpoint-by-endpoint role requirements
- **Resource-level** rules: rights/attributes per resource (public/restricted/embargoed/sensitive)

### Standard security headers (configurable)
- Strict-Transport-Security
- Content-Security-Policy
- X-Content-Type-Options
- Referrer-Policy
- Cross-Origin-Resource-Policy

---

## 3.4.4 Data privacy and protection (GDPR-supporting technical practices)

This documentation does not define legal obligations; it specifies technical mechanisms that support compliance and consistent interoperable behaviour.

### Data minimisation and redaction
- avoid exposing personal data unnecessarily
- provide configurable redaction pipelines
- explicitly mark sensitive fields where applicable

### Pseudonymisation
- use persistent pseudonyms for internal linking
- avoid embedding personal identifiers in filenames, URLs, manifests

### Logging and auditability
Logs should include:
- timestamp
- user/service identity (token claims)
- operation performed
- resource identifier

Logs must not include:
- access tokens
- passwords
- full payloads containing personal data (unless explicitly justified and protected)

### Provenance for privacy decisions
Maintain provenance trails for:
- which service produced/modified data
- how transformations impacted personal data
- which access policies were applied

---

## 3.4.5 Rights management and technical enforcement

Rights and licence metadata may drive technical enforcement decisions (access control and workflow restrictions such as embargoes or culturally sensitive material).

**Implementation guidance:** services performing authorisation/policy enforcement should be able to consume machine-readable rights/licence metadata and apply consistent enforcement when required.

Example mapping:
- Public domain / CC0: full download; derivatives permitted
- CC BY: sharing allowed; attribution must propagate in metadata
- Restricted: block full-resolution; allow previews
- Embargoed: hide until embargo expiry
- Culturally sensitive: restrict to specific groups

(See the dedicated “rights and licensing” guidance page for vocabularies and mapping patterns.)


## 3.4.6 Security in deployment and infrastructure (links to §3.3)

Deployment security impacts interoperability and trust.

### Container and runtime security
- use signed OCI-compliant images
- perform vulnerability scanning in CI pipelines
- avoid hardcoded secrets in images or manifests

### Secret management
- use vault-based secret stores (e.g., Vault / KMS-backed secrets)
- rotate secrets regularly
- never embed secrets in repositories

### Network security
- expose only required ports
- segment internal traffic
- protect external endpoints behind gateways/ingress controllers

### Monitoring and incident response
- standardised logging formats (e.g., OpenTelemetry)
- health endpoints (e.g., `/healthz`, `/readyz`)
- support centralised alerting for downtime/anomalous activity


## 3.4.7 Security expectations by interoperability level (overview)

- **Level 1 (Basic)**: HTTPS mandatory; optional authentication; basic access restrictions
- **Level 2 (Enhanced)**: mandatory AAI integration (EGI Check-in); OIDC tokens; RBAC; protected APIs
- **Level 3 (Full)**: fine-grained ABAC; rights-aware policy enforcement; provenance tracking; encrypted service-to-service communication (mTLS)

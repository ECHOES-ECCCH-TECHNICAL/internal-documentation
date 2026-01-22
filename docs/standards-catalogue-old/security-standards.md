# Security and data privacy (D6.2 §3.4)

This page summarises reference security standards and interoperability-oriented security practices required for consistent cross-provider trust.

## AAI: EGI Check-in integration (D6.2 §3.4.1)

All services requiring authentication should integrate with EGI Check-in to ensure consistent identity semantics across the infrastructure.

### Capabilities relevant for interoperability
- OIDC for web and API-based clients
- OAuth 2.0 for token-based authorisation and automation
- SAML 2.0 for institutional IdPs where required
- JWT access tokens for local verification
- account linking and group/role attributes for policy enforcement

### Supported authentication flows
Services should support one or more of:
- Authorization Code Flow (interactive browser login)
- Client Credentials Flow (service-to-service)
- Device Authorization Flow (CLI and limited UI devices)
- Refresh Token Flow (session renewal)

### Token lifetimes (defaults)
- Access token: 1 hour
- Refresh token: up to 30 days

### Required token validation behaviour
Services should validate:
- signature (JWKS)
- issuer (`iss`), audience (`aud`)
- expiry (`exp`) and not-before (`nbf`)
- required scopes/entitlements

Tokens must not be logged or stored in plaintext.

## Authorisation models (D6.2 §3.4.2)
CH Cloud services typically combine:
- RBAC (role-based access control)
- ABAC (attribute-based access control) for sensitivity/embargo/rights/affiliation-based constraints

Interoperable behaviour should clearly distinguish:
- `401 Unauthorized` for missing/invalid token
- `403 Forbidden` for valid token but insufficient permissions

## API security standards (D6.2 §3.4.3)

### Transport security
- HTTPS / TLS (minimum TLS 1.2) for all services
- disable plain HTTP (redirect or reject)
- consider mTLS for service-to-service links where appropriate

### Token handling
- accept OIDC (JWT) tokens issued by the federated IdP
- accept tokens via `Authorization: Bearer <token>` (cookies only for browser flows, secured)
- never store tokens in logs
- validate token signature/time/audience/expiry

### Standard security headers
Implement configurable security headers (not hardcoded), e.g.:
- Strict-Transport-Security
- Content-Security-Policy
- X-Content-Type-Options
- Referrer-Policy
- Cross-Origin-Resource-Policy

## Data privacy technical practices (GDPR-supporting) (D6.2 §3.4.4)
Interoperability requires privacy-related metadata and behaviours to be consistent across systems.

Recommended technical practices:
- data minimisation and redaction pipelines
- pseudonymisation (use stable pseudonyms; avoid personal identifiers in URLs/manifests)
- logging/auditability without exposing personal data

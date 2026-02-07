# Security and Data Privacy

This page provides **living, practical guidance** and configuration examples for implementing security and privacy controls in CH Cloud services and applications.
It complements the normative requirements in the **D6.2 deliverable** (security/AAI integration, governance and compliance, validation and conformance testing) by focusing on *how to implement controls*, *what to log*, and *what evidence to retain*.

**Audience:** service providers, application developers, platform operators, validators.

> This page is **non‑normative**: it offers recommended patterns and examples. Providers may adopt different tooling as long as the outcomes satisfy the project’s requirements and validation expectations.


## 1) Authentication integration (EGI Check‑in / OIDC)

### Supported flows (typical)

| Flow | Use case | Implementation priority |
|---|---|---|
| Authorization Code | Interactive web portals and browser-based apps | **Required for L2+ user-facing apps** |
| Client Credentials | Service-to-service automation | Required for workflows / backend jobs |
| Device Authorization | CLI tools | Optional |
| Refresh Tokens | Long-running sessions | Recommended (where appropriate) |

### OIDC discovery (recommended)
Avoid hardcoding issuer or JWKS URLs. Prefer OIDC discovery and cache results:

- Discovery document: `…/.well-known/openid-configuration`
- Derive `issuer`, `jwks_uri`, and `userinfo_endpoint` from discovery metadata
- Refresh cached discovery metadata periodically

### JWT validation (minimum checks)
**Always validate signature first**, then claims. Typical checks include:

- signature verification against JWKS (with caching)
- `iss` matches expected issuer
- `aud` includes your client/service audience (and optionally `azp` for some setups)
- `exp` not expired (use a small leeway for clock skew)
- `nbf` (if present) and other time-based constraints
- token type / scopes (where applicable)

```python
import requests
import jwt

DISCOVERY_URL = "https://aai.egi.eu/auth/realms/egi/.well-known/openid-configuration"

def load_oidc_config():
    return requests.get(DISCOVERY_URL, timeout=10).json()

def load_jwks(jwks_uri: str):
    return requests.get(jwks_uri, timeout=10).json()

def validate_token(token: str, expected_audience: str):
    # 1) Load OIDC config (cached in production)
    oidc = load_oidc_config()
    issuer = oidc["issuer"]
    jwks_uri = oidc["jwks_uri"]

    # 2) Fetch key set (cached in production)
    jwks = load_jwks(jwks_uri)

    # 3) Resolve signing key from KID
    header = jwt.get_unverified_header(token)
    kid = header.get("kid")
    key = next(k for k in jwks["keys"] if k["kid"] == kid)

    # 4) Verify signature + claims
    claims = jwt.decode(
        token,
        key=jwt.algorithms.RSAAlgorithm.from_jwk(key),
        algorithms=["RS256"],
        audience=expected_audience,
        issuer=issuer,
        leeway=60,  # clock skew tolerance (seconds)
    )
    return claims
```

**Response code guidance (typical):**
```
Missing token           → 401 Unauthorized
Invalid signature       → 401 Unauthorized
Expired token           → 401 Unauthorized
Valid token, no perms   → 403 Forbidden
```

### Framework examples

=== "FastAPI (Python)"
```python
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer

security = HTTPBearer()

async def validate_egi_token(credentials=Depends(security)):
    token = credentials.credentials
    try:
        claims = validate_token(token, expected_audience="your-client-id")
        return claims
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication token"
        )
```


## 2) Authorization patterns (RBAC/ABAC)

### Entitlements and group/role claims
EGI Check‑in deployments commonly express group/role membership via entitlement-style claims such as:

```
urn:mace:egi.eu:group:<vo>:<subgroup>:role=<role>#aai.egi.eu
```

Examples:
- `urn:mace:egi.eu:group:vo.chcloud.eu:role=member#aai.egi.eu`
- `urn:mace:egi.eu:group:vo.chcloud.eu:datasets:role=curator#aai.egi.eu`
- `urn:mace:egi.eu:group:vo.chcloud.eu:admin:role=admin#aai.egi.eu`

**Important:** entitlements may be **absent** unless requested via scopes, and some clients may receive them via **UserInfo** rather than in the access token.

### Requesting scopes (least privilege)
Request only what is necessary. For entitlements/group information, request one (or both) of:
- `eduperson_entitlement`
- `entitlements`

Typical baseline scopes for user-facing services:
- `openid profile email` (+ one entitlement scope as needed)

### UserInfo fallback (recommended)
Use UserInfo when:
- the access token is opaque to the client, or
- entitlements are not present in the token, or
- you need a consistent attribute retrieval mechanism.

```bash
ACCESS_TOKEN="…"
curl -s   -H "Authorization: Bearer ${ACCESS_TOKEN}"   "https://aai.egi.eu/auth/realms/egi/protocol/openid-connect/userinfo"
```

### RBAC mapping (example)
```yaml
roles:
  viewer:
    permissions:
      - read:datasets
      - read:metadata
    entitlements:
      - "urn:mace:egi.eu:group:vo.chcloud.eu:role=member"

  editor:
    permissions:
      - read:datasets
      - write:datasets
      - read:metadata
      - write:metadata
    entitlements:
      - "urn:mace:egi.eu:group:vo.chcloud.eu:role=editor"

  admin:
    permissions:
      - "*"
    entitlements:
      - "urn:mace:egi.eu:group:vo.chcloud.eu:role=admin"
```

### ABAC (attribute-based) example
Use ABAC when decisions depend on resource attributes (embargo/sensitivity) or user attributes (affiliation).

```python
from datetime import datetime

def check_access(user_claims, resource):
    # RBAC baseline (example)
    if not has_role(user_claims, "viewer"):
        return False

    # Embargo rule (example)
    if resource.embargo_until and resource.embargo_until > datetime.utcnow():
        return has_role(user_claims, "curator")

    # Sensitivity rule (example)
    if resource.sensitivity == "high":
        return user_claims.get("affiliation") in resource.allowed_affiliations

    return True
```

**Security rule of thumb:** authorisation must **fail closed** when policy cannot be evaluated (missing claims, missing policy, backend unavailable).


## 3) Transport and API security

### TLS/HTTPS configuration

**NGINX example:**
```nginx
server {
    listen 443 ssl http2;
    server_name api.example.org;

    ssl_certificate /path/to/cert.pem;
    ssl_certificate_key /path/to/key.pem;
    ssl_protocols TLSv1.2 TLSv1.3;

    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header X-Frame-Options "DENY" always;
    add_header Content-Security-Policy "default-src 'self'" always;
    add_header Referrer-Policy "strict-origin-when-cross-origin" always;

    location / {
        proxy_pass http://backend:8000;
        proxy_set_header X-Forwarded-Proto https;
    }
}

server {
    listen 80;
    server_name api.example.org;
    return 301 https://$server_name$request_uri;
}
```

**Kubernetes Ingress example:**
```yaml
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: ch-cloud-api
  annotations:
    nginx.ingress.kubernetes.io/ssl-redirect: "true"
    nginx.ingress.kubernetes.io/force-ssl-redirect: "true"
    nginx.ingress.kubernetes.io/configuration-snippet: |
      more_set_headers "Strict-Transport-Security: max-age=31536000; includeSubDomains";
      more_set_headers "X-Content-Type-Options: nosniff";
      more_set_headers "X-Frame-Options: DENY";
spec:
  tls:
  - hosts:
    - api.chcloud.eu
    secretName: api-tls-cert
  rules:
  - host: api.chcloud.eu
    http:
      paths:
      - path: /
        pathType: Prefix
        backend:
          service:
            name: api-service
            port:
              number: 8000
```


## 4) Privacy-aware logging and data minimisation

### Logging principles (recommended)
- Do **not** log raw access tokens, refresh tokens, or client secrets.
- Avoid logging PII unless strictly necessary; prefer **pseudonymous identifiers**.
- Record **request ids**, timestamps, endpoint/action, and outcome for auditability.
- Redact sensitive fields consistently.
- Align retention and access to logs with the project’s governance process.

### Privacy-aware logging pattern (example)
```python
import logging
import json
from datetime import datetime

class PrivacyAwareLogger:
    SENSITIVE_FIELDS = {
        "password", "token", "access_token", "refresh_token",
        "authorization", "api_key", "secret"
    }

    def log_request(self, subject_id, operation, resource_id, outcome, **metadata):
        log_entry = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "subject_id": subject_id,           # pseudonymous id (see below)
            "operation": operation,
            "resource_id": resource_id,
            "outcome": outcome,                 # success/denied/error
            "metadata": self._redact_sensitive(metadata),
        }
        logging.info(json.dumps(log_entry))

    def _redact_sensitive(self, data):
        if isinstance(data, dict):
            return {
                k: "***REDACTED***" if k.lower() in self.SENSITIVE_FIELDS else v
                for k, v in data.items()
            }
        return data
```

### Pseudonymous identity (recommended)
For authenticated users, prefer the **OIDC `sub`** claim (subject identifier) as the stable pseudonymous key.
To reduce cross-system correlation, you may hash it before storing/logging.

```python
import hashlib

def pseudonymous_subject(sub: str, salt: str) -> str:
    # Stable within the project, not reversible without the salt
    return hashlib.sha256(f"{sub}:{salt}".encode("utf-8")).hexdigest()[:16]
```

**Guest users:** avoid persistent identifiers unless a use case and legal basis exist. Prefer anonymous, session-scoped identifiers.

---

## 5) Evaluation data collection (feedback mechanisms)

Where applications integrate **user feedback capture** (e.g., in-app surveys), implement the following privacy controls:

- **Informed consent** is shown before any data capture:
    - purpose of collection,
    - retention period,
    - use of pseudonymous identifiers for authenticated users,
    - confirmation that guests remain anonymous (where applicable).
- **Pseudonymous profiling** for authenticated users:
    - include a pseudonymous identifier derived from OIDC `sub` (not email/name).
- **Guest submissions** contain no persistent user identifier.
- **Data minimisation:** collect only what is required by the evaluation framework.
- **Secure transport:** transmit data only over HTTPS; do not embed secrets in client code.
- **Logging:** do not log full payloads where they contain user-provided free text; store only what is necessary for debugging and audit.


## 6) Deployment security

### Secret management (examples)

=== "Kubernetes Secrets"
```yaml
apiVersion: v1
kind: Secret
metadata:
  name: api-secrets
type: Opaque
stringData:
  DATABASE_URL: "postgresql://user:pass@db:5432/chcloud"
  OIDC_CLIENT_SECRET: "your-secret-here"
```

=== "HashiCorp Vault"
```bash
vault kv put secret/chcloud/api   db_password="secure-password"   oidc_secret="client-secret"

vault kv get -field=db_password secret/chcloud/api
```

=== "GitHub Actions"
```yaml
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - name: Deploy
        env:
          DATABASE_URL: ${{ secrets.DATABASE_URL }}
          OIDC_SECRET: ${{ secrets.OIDC_CLIENT_SECRET }}
        run: |
          echo "Deploying with secured credentials"
```

### Container security scanning (example)
```yaml
# .gitlab-ci.yml example
container_scanning:
  stage: test
  image: docker:latest
  services:
    - docker:dind
  script:
    - docker build -t $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA .
    - docker run --rm -v /var/run/docker.sock:/var/run/docker.sock         aquasec/trivy image --severity HIGH,CRITICAL         $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA
  only:
    - merge_requests
    - main
```


## 7) Rights and policy enforcement

### Metadata-driven access control (example)
```python
from datetime import datetime

class RightsEnforcer:
    def check_download_permission(self, resource, user_claims):
        license_uri = resource.metadata.get("license")

        # Public domain - always allow
        if license_uri in [
            "http://creativecommons.org/publicdomain/zero/1.0/",
            "https://creativecommons.org/publicdomain/mark/1.0/"
        ]:
            return True, "full"

        # CC BY - allow, but ensure attribution obligations are visible to the user
        if license_uri and "creativecommons.org/licenses/by" in license_uri:
            return True, "full_with_attribution"

        # Restricted - enforce group/role membership
        if resource.access_level == "restricted":
            if not self._has_access_role(user_claims, resource):
                return False, None
            return True, "preview"

        # Embargoed - enforce time-based access
        if resource.embargo_until and resource.embargo_until > datetime.utcnow():
            if not self._is_curator(user_claims):
                return False, None

        return True, "full"

    def _has_access_role(self, claims, resource):
        required_group = resource.metadata.get("access_group")
        user_groups = claims.get("eduperson_entitlement", []) or claims.get("entitlements", [])
        return any(required_group in g for g in user_groups)

    def _is_curator(self, claims):
        groups = claims.get("eduperson_entitlement", []) or claims.get("entitlements", [])
        return any("role=curator" in g for g in groups)
```


## 8) Security testing checklist (pre-onboarding)

```bash
#!/bin/bash
set -euo pipefail

BASE_URL="https://api.example.org"

echo "1) TLS check"
curl -sI "${BASE_URL}" | grep -i "strict-transport-security" >/dev/null || echo "Missing HSTS header"

echo "2) Unauthenticated access blocked (restricted endpoint example)"
status=$(curl -s -o /dev/null -w "%{http_code}" "${BASE_URL}/protected" || true)
[ "$status" = "401" ] && echo "✓ Unauthenticated access blocked" || echo "Auth not enforced (expected 401)"

echo "3) Security headers"
curl -sI "${BASE_URL}" | grep -i "x-content-type-options" >/dev/null || echo "Missing X-Content-Type-Options header"

echo "4) Secrets scanning (repo)"
gitleaks detect --source . --verbose || echo "Secrets detected in repo"
```


## 9) Common implementation mistakes

| Mistake | Impact | Fix |
|---|---|---|
| Logging full JWT tokens | Token leakage | Log only minimal claims (e.g., hashed `sub`, `iss`) |
| Validating only `exp`, not signature | Token forgery | Verify signature first and validate `iss`/`aud` |
| Hardcoded client secrets | Credential exposure | Use secret managers / environment injection |
| Not checking `aud` | Token reuse across services | Validate audience matches your service |
| Using HTTP in token exchanges | MITM risk | Enforce HTTPS everywhere |
| Treating entitlements as always present | Authz bypass or false denies | Request scopes + use UserInfo fallback |
| Persisting guest identifiers by default | Privacy risk | Keep guests anonymous unless justified and consented |


## References

**EGI Check‑in**
- Documentation: https://docs.egi.eu/users/aai/check-in/
- OIDC discovery: https://aai.egi.eu/auth/realms/egi/.well-known/openid-configuration

**Standards**
- OpenID Connect: https://openid.net/specs/openid-connect-core-1_0.html
- OAuth 2.0: https://datatracker.ietf.org/doc/html/rfc6749
- JWT: https://datatracker.ietf.org/doc/html/rfc7519

**Security resources**
- OWASP API Security Top 10: https://owasp.org/API-Security/
- OWASP ASVS: https://owasp.org/www-project-application-security-verification-standard/

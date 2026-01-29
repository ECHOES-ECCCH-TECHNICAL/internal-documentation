# Security and Data Privacy

This page provides implementation guidance, configuration examples, and tooling
recommendations supporting the security requirements defined in **D6.2 Section 2.4**.


## Authentication Integration

### Supported EGI Check-in Flows

| Flow | Use Case | Implementation Priority |
|------|----------|------------------------|
| Authorization Code | Interactive web portals | **Required for L2+** |
| Client Credentials | Service-to-service automation | Required for workflows |
| Device Authorization | CLI tools | Optional |
| Refresh Tokens | Long-running sessions | Recommended |

### JWT Validation Implementation

**Minimum validation checks:**
```python
# Python example (pseudocode)
def validate_token(token):
    # 1. Decode header to get key ID
    header = jwt.get_unverified_header(token)
    
    # 2. Fetch JWKS from EGI Check-in
    jwks = requests.get("https://aai.egi.eu/auth/realms/egi/protocol/openid-connect/certs")
    
    # 3. Verify signature
    public_key = jwks.get_key(header['kid'])
    
    # 4. Decode and validate claims
    claims = jwt.decode(
        token,
        public_key,
        algorithms=['RS256'],
        audience='your-client-id',
        issuer='https://aai.egi.eu/auth/realms/egi'
    )
    
    # 5. Check expiry (exp) and not-before (nbf)
    # Already handled by jwt.decode with validation
    
    return claims
```

**Response codes:**
```
Missing token          → 401 Unauthorized
Invalid signature      → 401 Unauthorized  
Expired token         → 401 Unauthorized
Valid token, no perms → 403 Forbidden
```

### Framework-Specific Examples

=== "FastAPI (Python)"
```python
    from fastapi import Depends, HTTPException, status
    from fastapi.security import HTTPBearer
    
    security = HTTPBearer()
    
    async def validate_egi_token(credentials = Depends(security)):
        token = credentials.credentials
        try:
            claims = validate_token(token)  # From above
            return claims
        except JWTError:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authentication token"
            )
```

=== "Express (Node.js)"
```javascript
    const jwt = require('jsonwebtoken');
    const jwksClient = require('jwks-rsa');
    
    const client = jwksClient({
      jwksUri: 'https://aai.egi.eu/auth/realms/egi/protocol/openid-connect/certs'
    });
    
    function getKey(header, callback) {
      client.getSigningKey(header.kid, (err, key) => {
        callback(null, key.publicKey || key.rsaPublicKey);
      });
    }
    
    function validateToken(req, res, next) {
      const token = req.headers.authorization?.split(' ')[1];
      
      jwt.verify(token, getKey, {
        audience: 'your-client-id',
        issuer: 'https://aai.egi.eu/auth/realms/egi',
        algorithms: ['RS256']
      }, (err, decoded) => {
        if (err) return res.status(401).json({ error: 'Invalid token' });
        req.user = decoded;
        next();
      });
    }
```


## Authorization Patterns

### Entitlement Structure

EGI Check-in provides entitlements in this format:
```
urn:mace:egi.eu:group:<vo>:<subgroup>:role=<role>#aai.egi.eu

Examples:
urn:mace:egi.eu:group:vo.chcloud.eu:role=member#aai.egi.eu
urn:mace:egi.eu:group:vo.chcloud.eu:datasets:role=curator#aai.egi.eu
urn:mace:egi.eu:group:vo.chcloud.eu:admin:role=admin#aai.egi.eu
```

## Fetching entitlements (groups/roles) from EGI Check-in

EGI Check-in can expose group/role information as OIDC claims. In practice, entitlements should be treated as **optional unless explicitly requested via scopes**, and implementations should include a **robust fallback**:

1) Prefer reading entitlements directly from validated JWT claims (ID token or access token), if present.
2) Otherwise call the OIDC **UserInfo** endpoint and read them from the UserInfo response.

### Scopes to request

Request only what is required (least privilege). For entitlements, request one (or both) of:

- `eduperson_entitlement`
- `entitlements`

Typical baseline scopes for user-facing services:
- `openid profile email` (+ one of the entitlement scopes above)

### Where entitlements appear

Entitlements may appear as:
- `eduperson_entitlement` (common in research/AAI setups)
- `entitlements` (alternative claim name)

### UserInfo fallback

UserInfo should be used when:
- the access token is not locally interpretable (e.g., opaque to the client), or
- the token does not carry entitlements, or
- a consistent mechanism is required to fetch user attributes.


**cURL example:**
```bash
ACCESS_TOKEN="…"
curl -s \
  -H "Authorization: Bearer ${ACCESS_TOKEN}" \
  "https://aai.egi.eu/auth/realms/egi/protocol/openid-connect/userinfo"


### RBAC Mapping Example
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

### ABAC (Attribute-Based) Example
```python
def check_access(user_claims, resource):
    # RBAC check
    if not has_role(user_claims, 'viewer'):
        return False
    
    # ABAC checks
    if resource.embargo_until > datetime.now():
        # Embargoed - only curators
        return has_role(user_claims, 'curator')
    
    if resource.sensitivity == 'high':
        # Sensitive - check affiliation
        return user_claims.get('affiliation') in resource.allowed_affiliations
    
    # Public resource with viewer role
    return True
```


## API Security

### TLS/HTTPS Configuration

**NGINX example:**
```nginx
server {
    listen 443 ssl http2;
    server_name api.example.org;
    
    # TLS configuration
    ssl_certificate /path/to/cert.pem;
    ssl_certificate_key /path/to/key.pem;
    ssl_protocols TLSv1.2 TLSv1.3;
    ssl_ciphers 'ECDHE-RSA-AES128-GCM-SHA256:ECDHE-RSA-AES256-GCM-SHA384';
    ssl_prefer_server_ciphers on;
    
    # Security headers
    add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;
    add_header X-Content-Type-Options "nosniff" always;
    add_header X-Frame-Options "DENY" always;
    add_header Content-Security-Policy "default-src 'self'" always;
    add_header Referrer-Policy "strict-origin-when-cross-origin" always;
    
    # Disable plain HTTP (redirect handled separately)
    
    location / {
        proxy_pass http://backend:8000;
        proxy_set_header X-Forwarded-Proto https;
    }
}

# Redirect HTTP to HTTPS
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


## Privacy and Logging

### Privacy-Aware Logging Pattern
```python
import logging
import json
from datetime import datetime

class PrivacyAwareLogger:
    SENSITIVE_FIELDS = ['password', 'token', 'access_token', 'refresh_token', 
                       'authorization', 'api_key', 'secret']
    
    def log_request(self, user_id, operation, resource_id, outcome, **metadata):
        log_entry = {
            'timestamp': datetime.utcnow().isoformat(),
            'user_id': user_id,  # pseudonymized ID from token
            'operation': operation,
            'resource_id': resource_id,
            'outcome': outcome,  # success/denied/error
            'metadata': self._redact_sensitive(metadata)
        }
        logging.info(json.dumps(log_entry))
    
    def _redact_sensitive(self, data):
        if isinstance(data, dict):
            return {
                k: '***REDACTED***' if k.lower() in self.SENSITIVE_FIELDS else v
                for k, v in data.items()
            }
        return data
```

### Pseudonymization Example
```python
import hashlib

def pseudonymize_user_id(email, salt='stable-project-salt'):
    """Create stable pseudonym for internal use"""
    return hashlib.sha256(f"{email}{salt}".encode()).hexdigest()[:16]

# Usage in logs
logger.log_request(
    user_id=pseudonymize_user_id(user.email),
    operation='download_dataset',
    resource_id='dataset-12345',
    outcome='success'
)
```


## Deployment Security

### Secret Management Examples

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
    
    ---
    apiVersion: apps/v1
    kind: Deployment
    spec:
      template:
        spec:
          containers:
          - name: api
            env:
            - name: DATABASE_URL
              valueFrom:
                secretKeyRef:
                  name: api-secrets
                  key: DATABASE_URL
            - name: OIDC_CLIENT_SECRET
              valueFrom:
                secretKeyRef:
                  name: api-secrets
                  key: OIDC_CLIENT_SECRET
```

=== "HashiCorp Vault"
```bash
    # Store secret
    vault kv put secret/chcloud/api \
      db_password="secure-password" \
      oidc_secret="client-secret"
    
    # Retrieve in application
    vault kv get -field=db_password secret/chcloud/api
```

=== "GitHub Actions"
```yaml
    # .github/workflows/deploy.yml
    jobs:
      deploy:
        runs-on: ubuntu-latest
        steps:
          - name: Deploy
            env:
              DATABASE_URL: ${{ secrets.DATABASE_URL }}
              OIDC_SECRET: ${{ secrets.OIDC_CLIENT_SECRET }}
            run: |
              # Secrets are automatically masked in logs
              echo "Deploying with secured credentials"
```

### Container Security Scanning
```yaml
# .gitlab-ci.yml example
container_scanning:
  stage: test
  image: docker:latest
  services:
    - docker:dind
  script:
    - docker build -t $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA .
    - docker run --rm -v /var/run/docker.sock:/var/run/docker.sock \
        aquasec/trivy image --severity HIGH,CRITICAL \
        $CI_REGISTRY_IMAGE:$CI_COMMIT_SHA
  only:
    - merge_requests
    - main
```


## Rights Enforcement

### Metadata-Driven Access Control
```python
class RightsEnforcer:
    def check_download_permission(self, resource, user_claims):
        license_uri = resource.metadata.get('license')
        
        # Public domain - always allow
        if license_uri in ['http://creativecommons.org/publicdomain/zero/1.0/', 
                          'https://creativecommons.org/publicdomain/mark/1.0/']:
            return True, 'full'
        
        # CC BY - require attribution tracking
        if 'creativecommons.org/licenses/by' in license_uri:
            return True, 'full_with_attribution'
        
        # Restricted - check permissions
        if resource.access_level == 'restricted':
            if not self._has_access_role(user_claims, resource):
                return False, None
            return True, 'preview'  # Allow preview only
        
        # Embargoed - check date
        if resource.embargo_until and resource.embargo_until > datetime.now():
            if not self._is_curator(user_claims):
                return False, None
        
        return True, 'full'
    
    def _has_access_role(self, claims, resource):
        required_group = resource.metadata.get('access_group')
        user_groups = claims.get('eduperson_entitlement', [])
        return any(required_group in g for g in user_groups)
```



## Security Testing Checklist

### Pre-Onboarding Validation
```bash
#!/bin/bash
# security-check.sh

# 1. TLS check
curl -sI https://api.example.org | grep -i "strict-transport-security" || echo "Missing HSTS header"

# 2. Token validation
response=$(curl -s -o /dev/null -w "%{http_code}" https://api.example.org/protected)
[ "$response" == "401" ] && echo "✓ Unauthenticated access blocked" || echo "Auth not enforced"

# 3. Security headers
curl -sI https://api.example.org | grep -i "x-content-type-options" || echo "Missing security headers"

# 4. Secret scanning
gitleaks detect --source . --verbose || echo "Secrets detected in repo"
```


## Common Implementation Mistakes

| Mistake | Impact | Fix |
|---------|--------|-----|
| Logging full JWT tokens | Token leakage | Log only claims (sub, iss) |
| Validating only `exp`, not signature | Token forgery possible | Always verify signature first |
| Hardcoded client secrets | Credential exposure | Use environment variables/vault |
| Not checking `aud` claim | Token reuse across services | Validate audience matches your service |
| Using HTTP for token exchange | MITM attacks | Enforce HTTPS everywhere |
| Not implementing token refresh | Poor UX (frequent re-login) | Support refresh token flow |


## References

**EGI Check-in:**
- Documentation: https://docs.egi.eu/users/aai/check-in/
- OIDC endpoints: https://aai.egi.eu/auth/realms/egi/.well-known/openid-configuration

**Standards:**
- OpenID Connect: https://openid.net/specs/openid-connect-core-1_0.html
- OAuth 2.0: https://datatracker.ietf.org/doc/html/rfc6749
- JWT: https://datatracker.ietf.org/doc/html/rfc7519

**Security Resources:**
- OWASP API Security Top 10: https://owasp.org/API-Security/
- OWASP ASVS: https://owasp.org/www-project-application-security-verification-standard/
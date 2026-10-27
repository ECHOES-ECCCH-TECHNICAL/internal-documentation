# VTL early-pilot L1 observations

Observation: October 2026. Six externally routed service endpoints were checked by the provider. Real host names, namespaces and the original log timestamp details are not reproduced here. The provider retains the unsanitized probe outputs.

## SEC-01: six sampled HTTPS routes

| Public route label | Service category | TLS termination | HTTPS code | TLS verification | HTTP redirect |
|---|---|---|---|---|---|
| IIIF A | IIIF | edge | 403 | successful | 302 to HTTPS |
| IIIF B | IIIF | edge | 403 | successful | 302 to HTTPS |
| API A | API | edge | 404 | successful | 302 to HTTPS |
| API B | API | edge | 404 | successful | 302 to HTTPS |
| UI A | Web UI | edge | 200 | successful | 302 to HTTPS |
| UI B | Web UI | edge | 200 | successful | 302 to HTTPS |

These are provider-reported observations for the six assessed public Routes, not a proof that no other exposed interface exists. HTTP 403/404 at `/` does not indicate a certificate verification failure.

## SEC-03: classification

The provider classified application entry points as PUBLIC, RESTRICTED or INTERNAL, including separate treatment of public published content, user-specific resources and operator services. The detailed endpoint/matcher inventory is retained in the controlled-access original report. Classification does not establish per-object authorization correctness (SEC-09).

## REQ-DEP-011: backend logging probe

The provider reported a GET healthcheck request with a synthetic query marker, HTTP 204, and the following redacted *illustrative excerpts of the supplied response record*:

```text
DEBUG Slf4jMDCFilter - statusCode 204, path: /api/healthcheck/start-state, method: GET
INFO  Slf4jMDCFilter - path: /api/healthcheck/start-state, method: GET
```

The synthetic marker was absent in the supplied log excerpts. This positive scoped check does not verify all code paths or sinks for secret-free logging.

## Working status

Provider observations support SEC-01 and SEC-03 within the assessed pilot. No application-wide L1 level has been assigned. The rights statement and application-wide logging evidence remain incomplete. Provider contact details and exact deployed host names have been withheld from this public derivative.

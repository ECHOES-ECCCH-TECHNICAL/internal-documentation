# Identifier and URI Management

This page provides **living, practical guidance** for designing and operating identifiers that remain stable over time, support interoperability, and enable reliable citation and linking across the CH Cloud.

## Why persistent identifiers matter

Stable identifiers are foundational to interoperability because they:

- enable **citation and scholarly reference**,
- support long-term access and durable links,
- make cross-provider linking and reconciliation possible (enrichment, deduplication, alignment),
- reduce integration costs by preventing “identifier churn” across releases and migrations.

## Core principles

These principles address common failure modes in distributed ecosystems:

1. **Global uniqueness** - identifiers MUST be unique across the federation.
2. **Stability** - never reassign an identifier to a different entity.
3. **Provider control** - prefer identifiers under a domain you control and can maintain for the long term.
4. **Avoid volatility** - do not embed timestamps, environment names, “new/latest”, or internal file paths in canonical identifiers.
5. **Publish move policies** - if a resource moves, keep the identifier stable and use **HTTP redirects** (301/308) or equivalent persistence mechanisms.
6. **Version without churn** - represent normal updates via metadata/versioning, not by changing the canonical identifier.


## Choosing an identifier type

Use an identifier type that matches your stewardship, citation, and resolution needs.

| Identifier type | Best for | Example |
|---|---|---|
| **DOI** | Published datasets; formal citation | `https://doi.org/10.5281/zenodo.1234567` |
| **Handle** | Institutional repositories | `https://hdl.handle.net/1234/5678` |
| **ARK** | Archives and cultural-heritage stewardship patterns | `https://ark.example.org/ark:/12345/abc123` |
| **HTTP(S) URI** | Linked data, APIs, semantic assets, internal CH Cloud entity IDs | `https://museum.example.org/id/object/12345` |

### Practical guidance
- Use **DOIs** where *citation* and formal publication is the priority (datasets, curated releases).
- Use **HTTP(S) URIs** where you need *tight integration with APIs and linked data* (recommended for entity identifiers and semantic artefacts).
- Use **ARK/Handle** if your institution already operates PID infrastructure and has a clear long-term stewardship commitment.


## URI design patterns

### Recommended URI patterns (examples)

Prefer readable, type-scoped paths with stable semantics:

- `https://museum.example.org/id/object/12345`
- `https://museum.example.org/id/person/artist-456`
- `https://museum.example.org/id/concept/medieval-art`
- `https://museum.example.org/id/dataset/collection-x`

Recommended characteristics:
- stable base domain under institutional control,
- explicit resource-type segment (`id/object`, `id/person`, …),
- opaque identifiers where appropriate (avoid leaking internal database structure),
- consistent casing and separators (lowercase + hyphens is typical),
- no coupling to deployment environments.

### Anti-patterns (and why they fail)

| Anti-pattern | Example | Why it fails | Better alternative |
|---|---|---|---|
| Query-string identifiers | `https://museum.example.org/page.php?id=12345` | Often coupled to legacy routing; harder to govern | `https://museum.example.org/id/object/12345` |
| Volatile path segments | `…/objects/new/12345` | “new/latest” becomes incorrect; breaks consumer assumptions | Stable type-scoped IDs |
| Internal-only addressing | `https://192.168.1.100/object/12345` | Not resolvable outside a local network | Public domain + proxy if needed |
| Embedded timestamps | `…/object/12345-20240101` | Forces new IDs for normal updates | Keep ID stable; version separately |
| Environment-coupled IDs | `https://staging.museum.example.org/id/object/12345` | Breaks promotion; confuses consumers | One canonical ID across environments |


## Dereferenceability and content negotiation

If you publish HTTP(S) URIs as identifiers, decide whether they are **dereferenceable** (resolvable) and document the expectation.

Common patterns:

- **303 redirects** from an identifier URI to:
  - a human HTML page, and/or
  - a machine-readable representation (RDF/JSON-LD/Turtle).
- **Content negotiation** to serve HTML vs RDF depending on the `Accept` header.

**Rule of thumb:** if you claim dereferenceability, treat broken resolution as a monitoring/incident issue, not “best effort”.


## Versioning and provenance without changing identifiers

Keep the canonical identifier stable and represent change via:

- explicit **version** fields in metadata (`version`, `dateModified`, release tag),
- release notes / changelogs for datasets and services,
- provenance relations (e.g., `prov:wasDerivedFrom`, supersession links),
- named graphs or versioned distributions (where L3 patterns apply).

Example concept:

- Canonical ID: `https://museum.example.org/id/object/12345`
- Distribution (versioned): `https://museum.example.org/download/object/12345/v2.jsonld`
- Provenance: the v2 distribution `prov:wasDerivedFrom` the v1 distribution


## Deprecation and tombstones 

When an identifier can no longer resolve to the original resource (e.g., withdrawn content), avoid silent failures.

Recommended behaviours:

- **Deprecation notice:** maintain a landing/tombstone page that explains what happened.
- **Redirect to successor** when a clear replacement exists (301/308 + human-readable note).
- **410 Gone** for intentionally removed resources, ideally with a tombstone explanation (where appropriate).

Always document:

- who to contact,
- what changed,
- whether a successor/mapping exists,
- the effective date of the change.


## Privacy and security considerations

- Do not embed **PII** (names/emails) in identifier strings.
- Avoid identifiers that expose sensitive locations or internal system structure.
- If access is restricted, the identifier may still be public (for citation/discovery), but access must be controlled via authn/authz at retrieval time.


## Illustrative example: DOI minting with DataCite

This example shows a typical process. Actual steps vary by institutional membership and policy.

### 1) Obtain DataCite access
- Register with DataCite directly or via consortium membership.
- Define internal governance: who can mint DOIs, when, and for which assets.

### 2) Prepare DataCite metadata (XML example)
```xml
<?xml version="1.0" encoding="UTF-8"?>
<resource xmlns="http://datacite.org/schema/kernel-4">
  <identifier identifierType="DOI">10.5281/MUSEUM.12345</identifier>
  <creators>
    <creator>
      <creatorName>National Heritage Museum</creatorName>
    </creator>
  </creators>
  <titles>
    <title>Medieval Manuscript Collection Digital Archive</title>
  </titles>
  <publisher>National Heritage Museum</publisher>
  <publicationYear>2024</publicationYear>
  <resourceType resourceTypeGeneral="Dataset">Image Collection</resourceType>
</resource>
```

### 3) Mint DOI via API (example)
```bash
curl -X POST "https://api.datacite.org/dois" \
  -H "Content-Type: application/vnd.api+json" \
  -u "YOUR_CLIENT_ID:YOUR_PASSWORD" \
  -d @doi_payload.json
```

### 4) Set DOI resolution target
Ensure the DOI resolves to a stable landing page or dataset record that:

- provides access/distributions where permitted,
- exposes licence/rights clearly,
- provides version/change information.


## References
- DataCite DOI documentation: https://support.datacite.org/
- IETF URI specification: https://www.rfc-editor.org/rfc/rfc3986
- W3C : https://www.w3.org/TR/cooluris/

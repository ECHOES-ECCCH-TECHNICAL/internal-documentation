# Identifier and URI Management

This page provides **practical, non-normative** guidance and examples to support **D6.2 §4.2.2.8 (Identifier Rules)**. It is intended to help providers design and operate identifiers that remain stable over time, support interoperability, and enable reliable citation and linking across the CH Cloud.



## Why persistent identifiers (PIDs) matter

Stable identifiers:
- enable citation and reference (including scholarly reuse),
- support long-term access and durable links,
- facilitate integration across systems (linking, enrichment, reconciliation),
- are required for consistent L2+ interoperability patterns.



## Core rules (operational interpretation)

These rules reflect common failure modes observed in distributed environments:

- Use **globally unique identifiers** for all resources and entities.
- Prefer **HTTP(S) URIs** where feasible (dereferenceable, web-native).
- Avoid embedding volatile information (e.g., file paths, timestamps, “new”, environment names).
- **Never reassign** an existing identifier to a different entity.
- If a resource moves, use **redirection** (e.g., HTTP 301/308) and keep the identifier stable.



## Choosing an identifier type

| Type | Best for | Example |
|---|---|---|
| **DOI** | Published datasets, formal citation | `https://doi.org/10.5281/zenodo.1234567` |
| **Handle** | Institutional repositories | `https://hdl.handle.net/1234/5678` |
| **ARK** | Archives, cultural heritage | `https://ark.example.org/ark:/12345/abc123` |
| **HTTP(S) URI** | Linked data, semantic web, internal CH Cloud identifiers | `https://museum.example.org/id/object/12345` |

### Practical guidance
- Use **DOIs** where citation and scholarly publishing is the primary requirement.
- Use **HTTP(S) URIs** where you want tight integration with linked data and APIs (recommended for entity identifiers and semantic artefacts).
- Use **ARK/Handle** when aligned with institutional PID infrastructure and long-term stewardship commitments.



## Good URI patterns

Prefer readable, hierarchical, and type-scoped paths:

- `https://museum.example.org/id/object/12345`
- `https://museum.example.org/id/person/artist-456`
- `https://museum.example.org/id/concept/medieval-art`

Recommended properties:

- stable base domain under institutional control,
- explicit resource type segment (`id/object`, `id/person`, `id/concept`),
- opaque identifiers where appropriate (avoid leaking internal database structure),
- consistent casing and separators (lowercase + hyphens is typical).



## Bad URI patterns (anti-patterns)

| Anti-pattern | Example | Why it fails | Better alternative |
|---|---|---|---|
| Query-string identifiers | `https://museum.example.org/page.php?id=12345` | Harder to govern and often coupled to legacy CMS routing | `https://museum.example.org/id/object/12345` |
| Volatile path segments | `https://museum.example.org/objects/new/12345` | “new” and similar labels become outdated and misleading | Use stable type-scoped IDs |
| Internal-only addressing | `https://192.168.1.100/object/12345` | Not resolvable from outside the local network | Use a public domain; proxy if needed |
| Embedding timestamps | `.../object/12345-20240101` | Forces new identifiers for normal updates | Keep ID stable; version separately |
| Environment-coupled IDs | `https://staging.museum.example.org/id/object/12345` | Breaks promotion and confuses consumers | Use one canonical ID; environments serve the same IDs |


## Versioning and provenance without changing identifiers

Keep identifiers stable and represent change via:

- version fields in metadata (e.g., `version`, `modified`),
- release tags and changelogs (software/datasets),
- named graphs or provenance metadata (L3 patterns),
- separate “versioned resources” only when the version itself must be citable.

Example patterns:

- Stable ID: `https://museum.example.org/id/object/12345`
- Versioned snapshot (optional): `https://museum.example.org/id/object/12345?version=2` (only if governed and documented)
- Provenance metadata links: `prov:wasDerivedFrom`, `dcterms:modified`, etc.



## Implementation example: DOI minting with DataCite (illustrative)

This example shows one typical process. Actual steps vary by institutional membership and policy.

### 1) Obtain DataCite access
- Register with DataCite directly or via an institutional consortium membership.
- Define who is permitted to mint DOIs and under what conditions.

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
  <descriptions>
    <description descriptionType="Abstract">
      Complete digitization of 150 medieval manuscripts...
    </description>
  </descriptions>
</resource>
```

### 3) Mint DOI via API (example)

```bash
curl -X POST https://api.datacite.org/dois \
  -H "Content-Type: application/vnd.api+json" \
  -u "YOUR_CLIENT_ID:YOUR_PASSWORD" \
  -d @doi_payload.json
```

### 4) Configure resolution target (example payload)

```json
{
  "data": {
    "type": "dois",
    "attributes": {
      "doi": "10.5281/MUSEUM.12345",
      "url": "https://museum.example.org/collection/medieval-manuscripts",
      "xml": "..."
    }
  }
}
```

## References 
- DataCite DOI documentation: https://support.datacite.org/
- IETF URI specification (RFC 3986): https://www.rfc-editor.org/rfc/rfc3986
- W3C Cool URIs for the Semantic Web: https://www.w3.org/TR/cooluris/

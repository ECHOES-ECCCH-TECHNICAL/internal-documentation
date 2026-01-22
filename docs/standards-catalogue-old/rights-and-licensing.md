# Rights and licensing metadata (D6.2 §3.5)

This page provides reference guidance on expressing rights and reuse conditions as machine-readable metadata and translating them into predictable technical behaviours.


## Purpose of legal interoperability in the CH Cloud
In a distributed multi-provider environment, datasets originate from institutions operating under different rights, restrictions, and legal frameworks. Interoperability requires that:
- legal constraints travel with data,
- systems interpret them consistently,
- access controls respect them automatically,
- downstream services do not violate conditions unintentionally.

## Machine-readable rights and license metadata
Prefer widely adopted rights frameworks and URI-based expressions, including:
- Creative Commons licenses (e.g., CC0, CC BY, CC BY-SA, CC BY-NC)
- RightsStatements.org (cultural heritage focused statements)
- DCTERMS rights metadata (e.g., `dcterms:rights`, `dcterms:license`)
- IIIF `rights` property for image-based objects
- Europeana/EDM rights properties (e.g., `edm:rights`)

### Practical guidance
- ensure each digital object or dataset includes a clear rights statement
- express rights in machine-actionable form where possible (URI-based)
- support multiple rights where needed (e.g., one for metadata, one for media)
- preserve rights across transformation, ingestion, export, and aggregation

## Legal constraints as technical access rules (mapping examples)

| Legal condition | Typical technical behaviour |
|---|---|
| Copyrighted content | restricted download; watermarking; login required |
| Non-commercial licence | disable commercial-use workflows; usage disclaimers |
| No-derivatives licence | disable derivative generation (e.g., 3D reconstruction, AI enhancement) |
| Embargoed material | block access until embargo expiry; hide fields if required |
| Sensitive cultural heritage | role-based or affiliation-based restrictions |
| No known copyright | allow open access to high-resolution derivatives |
| Donor/agreement-based restrictions | project- or group-based access rules |

## Personal data handling (GDPR-supporting technical obligations)
Where datasets contain personal data, systems should support:
- pseudonymisation (stable identifiers; avoid personal data in URLs/identifiers)
- data minimisation (process/store only what is necessary)
- purpose limitation tagging where relevant
- auditability without exposing personal data

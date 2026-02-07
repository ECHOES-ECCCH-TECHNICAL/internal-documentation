# JPEG / PNG / WebP (Access Images)

JPEG, PNG, and WebP are common formats for **access delivery** of images in web applications and APIs.
They are typically produced as derivatives from preservation masters (e.g., TIFF) and optimised for browsing, portals, and tool integration.

This page provides **practical, non‑normative** guidance for selecting and producing access images.

## When to use each format

Rule of thumb:

| Format | Best for | Notes |
|---|---|---|
| **JPEG** | Photographic content | Lossy compression; tune quality; avoid repeated recompression |
| **PNG** | Line art, diagrams, UI captures, transparency | Lossless; typically larger than JPEG for photographs |
| **WebP** | Web delivery where supported | Often smaller than JPEG/PNG; supports lossy/lossless and alpha |

## When not to use these as masters

- Do not use JPEG/WebP (lossy) as the sole preservation master when fidelity is required.
- PNG can be preservation‑worthy for some born‑digital artefacts, but is not a universal archival master format.

## Interoperability considerations

### 1) Deterministic derivatives

If you publish access images, document:

- conversion settings (quality, resizing rules),
- naming conventions and mapping to the master identifier,
- whether embedded metadata is preserved or stripped.

### 2) Metadata and privacy

- Ensure rights/licence information is present in the repository record (and, if suitable, in embedded metadata).
- Consider stripping sensitive embedded metadata (e.g., GPS) from public derivatives while preserving it internally where justified.

### 3) Performance and caching

- Use cache headers appropriate to immutability (versioned URLs allow long cache lifetimes).
- Prefer pre-generated thumbnails for portal UIs to avoid repeated on‑the‑fly resizing.

## Validation checks

- Confirm dimensions/thumbnail sizes match documented rules.
- Confirm derivatives are generated from the intended master version.
- Confirm rights/licence metadata is preserved in the repository record.
- Spot-check colour profile handling to avoid unexpected shifts.

## References

- JPEG overview (Library of Congress): https://www.loc.gov/preservation/digital/formats/fdd/fdd000017.shtml
- PNG specification (W3C): https://www.w3.org/TR/png/
- WebP: https://developers.google.com/speed/webp

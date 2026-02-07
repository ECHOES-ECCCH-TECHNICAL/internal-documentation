# Images in the CH Cloud

This page provides practical, non‑normative guidance for handling image assets in a federated environment:

- choosing formats for preservation masters and access delivery
- preserving and exposing technical and rights metadata consistently
- generating deterministic derivatives (thumbnails, web images, tiles)
- publishing interoperable access via IIIF when appropriate

It complements project deliverables by focusing on implementation decisions and reproducible workflows.

## Recommended format strategy

Use a two‑tier approach wherever feasible.

| Purpose | Recommended formats | Notes |
|---|---|---|
| Preservation master | TIFF (lossless) | Prefer lossless compression (LZW/ZIP) if needed; avoid lossy recompression |
| Access and web delivery | JPEG, PNG, WebP | Choose by content type (photos vs line art), licensing, and delivery needs |
| Interoperable tiled delivery | IIIF Image API derivatives | Enables deep zoom, regions, standard viewers, and consistent integration |

Rule of thumb: treat the preservation master as the reference source; publish access derivatives and IIIF tiles as derived outputs with recorded parameters.

## Metadata preservation and privacy

### What to preserve

Extract and preserve, at minimum:

- technical metadata: dimensions, bit depth, colour profile, compression, checksums
- descriptive and rights metadata: creator, rights statement, licence URI, source, capture date
- embedded metadata if present: EXIF, IPTC, XMP

### Practical rules

- Treat the master as the metadata source of record.
- If derivatives are produced, preserve metadata at least in the repository record (or sidecar JSON/XMP), even if you strip embedded metadata from public derivatives.
- Be explicit about privacy:

  - do not leak sensitive EXIF fields (for example GPS) where it is inappropriate
  - ensure published rights and licence statements match institutional policy
  - avoid embedding internal operator names or emails in public derivatives

## Derivative generation

If you generate derivatives, record:

- tool and version (for example ImageMagick version)
- conversion parameters (resize rules, quality, colour conversion)
- naming convention and mapping to the master asset id
- checksums for published outputs (recommended for distribution integrity)


## IIIF integration

IIIF is a strong choice when:

- you need deep zoom and tiled access
- you want to reuse standard viewers and tools across providers
- you want a standard manifest structure for compound objects and annotation workflows

### What to publish

- IIIF Image API endpoint(s) for image services
- IIIF Presentation manifests describing objects, canvases, and metadata
- optional Change Discovery feeds for incremental synchronisation

### Minimal Presentation 3 manifest

```json
{
  "@context": "https://iiif.io/api/presentation/3/context.json",
  "id": "https://museum.example.org/iiif/obj-12345/manifest",
  "type": "Manifest",
  "label": { "en": ["Portrait of a Nobleman"] },
  "rights": "https://creativecommons.org/licenses/by/4.0/",
  "items": [
    {
      "id": "https://museum.example.org/iiif/obj-12345/canvas/1",
      "type": "Canvas",
      "height": 4000,
      "width": 3000
    }
  ]
}
```

## Common pitfalls

| Pitfall | Why it matters | Safer pattern |
|---|---|---|
| Using only local IDs (for example `12345`) | Not globally resolvable | Use stable HTTPS identifiers and keep them consistent |
| Lossy recompression of masters | Irreversible quality loss | Keep a lossless master; derive access outputs separately |
| Stripping metadata without retaining it | Loses provenance and rights context | Extract and store metadata in records or sidecars |
| Undocumented derivative parameters | Not reproducible; hard to audit | Record conversion settings and tool versions |
| Publishing only “latest” | Breaks traceability | Publish versioned artefacts or immutable digests |

## References

- IIIF Presentation API 3.0: https://iiif.io/api/presentation/3.0/
- IIIF Image API 3.0: https://iiif.io/api/image/3.0/
- IPTC Photo Metadata: https://www.iptc.org/standards/photo-metadata/

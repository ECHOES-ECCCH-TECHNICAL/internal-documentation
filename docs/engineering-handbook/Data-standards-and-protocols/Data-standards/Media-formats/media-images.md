# Images: Formats, Metadata Preservation, and IIIF

This page provides **practical, non-normative** guidance and examples to support **D6.2 §4.2.2.5 (Images)**. It is intended to help providers handle image assets consistently across preservation, access delivery, and interoperability services (including IIIF).



## Recommended image formats

| Purpose | Recommended formats | Notes |
|---|---|---|
| Preservation master | **TIFF** (lossless) | Prefer lossless compression (LZW/ZIP) if needed; avoid lossy recompression |
| Access / web delivery | **JPEG**, **PNG**, **WebP** | Select format based on content type (photos vs. line art), licensing, and delivery needs |
| Interoperable image delivery (L2+) | **IIIF Image API** derivatives | Enables tiled access, deep zoom, and standardized integration |



## Metadata handling (ingestion and derivatives)

### What to preserve
During ingestion, metadata should be **extractable and preserved**, including (where available):

- Technical metadata: dimensions, bit depth, color profile, compression, checksums
- Descriptive/rights metadata: creator, rights statement, licence URI, source, capture date
- Embedded fields: EXIF / IPTC / XMP (as provided)

### Practical rules
- Treat the **preservation master** as the metadata source of record where possible.
- If you generate derivatives, ensure you preserve metadata **at least in the repository**, even if you remove embedded metadata from public derivatives for privacy or size reasons.
- Prefer a deterministic mapping into your repository metadata model (e.g., store extracted metadata as JSON/XMP sidecar, and link it to the asset identifier).


## Scenario: Museum digitizing a painting collection

This scenario shows one common workflow: capture a preservation master, generate access derivatives, and publish via IIIF.

### Step 1: Capture (preservation master)

Recommended capture characteristics depend on institutional digitisation policy and equipment; typical high-quality capture settings:

- Format: **TIFF** (uncompressed or lossless compression: LZW/ZIP)
- Resolution: expressed as **pixel dimensions** and/or **PPI at target size** (avoid relying on “DPI” alone)
- Color space: Adobe RGB or ProPhoto RGB (institutional policy-dependent)
- Bit depth: **16-bit per channel** for high-quality originals
- Embedded metadata: EXIF, IPTC, XMP (as provided)
- Integrity: compute and store checksums (e.g., SHA-256)

Example file:
- `obj-12345_preservation_master.tif` (e.g., 150 MB)

### Step 2: Generate access derivatives (web)

Below uses ImageMagick (illustrative). Prefer deterministic naming and store derivative parameters in build logs.

#### 2a) Web access JPEG (keep metadata unless you have a reason to strip)

```bash
magick obj-12345_preservation_master.tif \
  -quality 85 \
  -resize 2000x2000\> \
  -sampling-factor 4:2:0 \
  obj-12345_access.jpg
```

#### 2b) Thumbnail

```bash
magick obj-12345_preservation_master.tif \
  -quality 85 \
  -resize 400x400\> \
  obj-12345_thumbnail.jpg
```


Key point: if you strip, ensure metadata is preserved elsewhere (repository record, sidecar, manifest).

### Step 3: IIIF integration (L2+)

At L2+, ensure IIIF compatibility for interoperable delivery.

- Use **IIIF Presentation API** for manifests (object/canvas/annotations)
- Use **IIIF Image API** for image services (tiling, region requests, sizes)

#### Minimal IIIF Presentation 3 manifest 

```json
{
  "@context": "https://iiif.io/api/presentation/3/context.json",
  "id": "https://museum.example.org/iiif/obj-12345/manifest",
  "type": "Manifest",
  "label": { "en": ["Portrait of a Nobleman"] },
  "rights": "https://creativecommons.org/licenses/by/4.0/",
  "metadata": [
    { "label": { "en": ["Artist"] }, "value": { "en": ["Hans Holbein the Younger"] } },
    { "label": { "en": ["Date"] }, "value": { "en": ["c. 1540"] } }
  ],
  "items": [
    {
      "id": "https://museum.example.org/iiif/obj-12345/canvas/1",
      "type": "Canvas",
      "height": 4000,
      "width": 3000,
      "items": [
        {
          "id": "https://museum.example.org/iiif/obj-12345/page/1",
          "type": "AnnotationPage",
          "items": [
            {
              "id": "https://museum.example.org/iiif/obj-12345/annotation/1",
              "type": "Annotation",
              "motivation": "painting",
              "body": {
                "id": "https://iiif.museum.example.org/obj-12345/full/max/0/default.jpg",
                "type": "Image",
                "format": "image/jpeg",
                "height": 4000,
                "width": 3000,
                "service": [
                  {
                    "id": "https://iiif.museum.example.org/obj-12345",
                    "type": "ImageService3",
                    "profile": "level2"
                  }
                ]
              },
              "target": "https://museum.example.org/iiif/obj-12345/canvas/1"
            }
          ]
        }
      ]
    }
  ]
}
```


## Common pitfalls 

| Pitfall | Why it matters | Safer pattern |
|---|---|---|
| Using only local IDs (e.g., `12345`) | Not globally resolvable | Use stable HTTPS identifiers and link them consistently |
| Recompressing masters as lossy | Irreversible quality loss | Keep a lossless preservation master; derive access images separately |
| Stripping metadata without retaining it | Loses provenance/rights/technical context | Extract/store metadata in repository records or sidecars |
| Undocumented derivative parameters | Hard to reproduce and audit | Record conversion settings in pipeline logs or configuration |
| Publishing “latest” without immutability | Breaks traceability | Publish versioned assets or immutable digests and record them |



## References 
- IIIF Presentation API 3.0: https://iiif.io/api/presentation/3.0/
- IIIF Image API 3.0: https://iiif.io/api/image/3.0/

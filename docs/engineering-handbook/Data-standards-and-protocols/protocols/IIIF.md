# IIIF (International Image Interoperability Framework)

IIIF is a family of community standards defining REST-based APIs for consistent access to high‑resolution images and associated metadata across institutions. It defines predictable URL patterns and **JSON‑LD–based manifests** that describe digital objects, sequences, annotations, and structure.

Visual media (scanned manuscripts, artworks, photographs, maps) are a major part of cultural heritage collections. IIIF supports interoperability by enabling:

- consistent, high-performance image delivery (tiling, regions, multiple resolutions),
- interoperability between viewers (e.g., Mirador, Universal Viewer),
- integration with annotation tools via Web Annotation,
- structured manifests for complex objects (multi-page manuscripts, albums, compound objects),
- synchronization patterns via Change Discovery.


## When to use IIIF

Use IIIF when you need interoperable, web-accessible delivery of images and their structure:

- Publishing images of cultural heritage objects for the web.
- Supporting deep zoom, region selection, tiling, or multi-resolution viewing.
- Supporting annotation workflows (crowdsourcing, scholarly annotation, transcription).
- Integrating with existing IIIF-capable viewers and tools.

## When not to use IIIF

IIIF may be unnecessary or insufficient in these cases:

- Non-image media (3D, audio) unless wrapped appropriately in IIIF Presentation; use media-specific standards where available.
- Preservation-quality delivery of original masters (e.g., TIFF masters); IIIF is primarily for access/derivatives, not preservation packaging.
- Simple use cases limited to thumbnails or low-resolution previews (a basic static delivery approach may be enough).

## Relevance to Cultural Heritage (CH Cloud)

- Strong candidate for **Level 1 and Level 2** interoperability for image-based collections.
- Likely to be highly relevant for user-facing CH Cloud tools consuming **IIIF manifests**.
- Enables tool reuse across institutions (viewer/annotation interoperability).

## Technical considerations

### IIIF Image API

The IIIF Image API defines operations through URL parameters, typically including:
- **region** (full or cropped),
- **size** (scaled),
- **rotation**,
- **quality**,
- **format** (e.g., JPEG/PNG/WebP).

This supports tiled delivery and efficient zooming for large images.

### IIIF Presentation API

The Presentation API defines **Manifests** (JSON-LD) describing the structure and metadata of digital objects:
- object-level metadata,
- sequences/canvases for pages or views,
- links to image services,
- integration points for annotations.

### Annotations

IIIF integrates with the W3C **Web Annotation** model, enabling:
- textual annotations,
- transcriptions,
- semantic tags,
- links to controlled vocabularies.

### Change Discovery

The IIIF Change Discovery API provides a mechanism for synchronization and updates across systems (e.g., notifying aggregators and consumers about changes to manifests).

### Operational expectations

- Stable, persistent URLs are required for image services and manifests.
- Access control and authentication may be necessary for restricted collections; ensure consistent behavior for authorized clients.
- Ensure caching/CDN strategies align with image delivery patterns and update frequency.

## References 

- IIIF Consortium (overview): https://iiif.io/
- IIIF Image API (spec): https://iiif.io/api/image/
- IIIF Presentation API (spec): https://iiif.io/api/presentation/
- IIIF Change Discovery API (spec): https://iiif.io/api/discovery/
- W3C Web Annotation Data Model: https://www.w3.org/TR/annotation-model/
- Mirador viewer: https://projectmirador.org/
- Universal Viewer: https://universalviewer.io/

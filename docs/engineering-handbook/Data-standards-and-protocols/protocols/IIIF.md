# IIIF

IIIF is a family of community standards defining REST-based APIs for consistent access to high‑resolution images and associated metadata across institutions.
It provides predictable URL patterns, tiled image delivery, and **JSON‑LD manifests** that describe digital objects, structure, and annotations.


## 1. What IIIF enables (in practice)

IIIF supports interoperability by making it easier to:
- deliver images efficiently at multiple resolutions (deep zoom, tiling, regions),
- use standard viewers and annotation tools across collections,
- publish structured representations of complex objects (multi-page manuscripts, albums, compound objects),
- support scholarly and crowdsourced annotation workflows,
- synchronise changes in published manifests for downstream consumers (aggregators, portals).



## 2. When to use IIIF

Use IIIF when you need interoperable, web-accessible delivery of images and their structure, for example:
- publishing images of cultural heritage objects for web access,
- supporting deep zoom, region selection, tiling, or multi-resolution viewing,
- supporting annotation workflows (scholarly annotation, crowdsourcing, transcription),
- integrating with existing IIIF-capable viewers and tools (e.g., Mirador, Universal Viewer),
- supporting downstream aggregation and synchronisation.



## 3. When IIIF is not sufficient (or may be unnecessary)

IIIF may be unnecessary or insufficient in these cases:
- **Non-image media** (3D, audio, video) unless represented via IIIF Presentation with appropriate media handling; use media‑specific standards where available.
- **Preservation packaging** for original masters (e.g., archival TIFF) — IIIF is primarily for *access* and derivatives, not preservation packaging.
- **Very simple access needs** limited to thumbnails or low‑resolution previews, where static delivery may be enough.



## 4. Core IIIF APIs (overview)

### 4.1 IIIF Image API
The Image API defines operations through URL parameters, typically including:
- **region** (full or cropped),
- **size** (scaled),
- **rotation**,
- **quality**,
- **format** (e.g., JPEG/PNG/WebP).

This enables tiled delivery and efficient zooming for large images, and supports interoperability with IIIF‑capable viewers.

### 4.2 IIIF Presentation API
The Presentation API defines **Manifests** (JSON‑LD) describing the structure and metadata of digital objects:
- object-level descriptive metadata,
- canvases for pages/views,
- links to image services,
- navigation structure (ranges, sequences),
- annotation integration points.

In practice, the manifest is the primary interoperable object that downstream tools consume.

### 4.3 Annotations (Web Annotation model)
IIIF integrates with the W3C **Web Annotation** model, enabling:
- textual notes,
- transcriptions,
- semantic tags,
- links to controlled vocabularies,
- comment threads (tool-dependent).

Annotation interoperability improves when targets (canvases, regions) are stable and URIs remain persistent.

### 4.4 Change Discovery
The IIIF Change Discovery API provides mechanisms to publish change feeds so consumers can:
- detect new/updated/deleted manifests,
- incrementally synchronise content,
- keep portals and aggregators up to date without crawling everything.



## 5. Federation and operational considerations (recommended)

### 5.1 URL stability and persistence
- Treat manifest URLs and image service URLs as persistent identifiers.
- Avoid changing URL patterns; if changes are unavoidable, provide redirects and documented migration strategies.

### 5.2 Access control and restricted collections
- If collections are restricted, enforce consistent authentication/authorisation behaviour for IIIF endpoints.
- Document what is protected (manifests, image services, annotations) and what clients should expect (401/403 behaviour, token flows).
- Ensure viewer compatibility for protected resources (some viewers require specific auth patterns).

### 5.3 Caching and performance
- IIIF benefits strongly from caching/CDNs due to repeated tile access.
- Document cache headers and invalidation strategy (especially when images or manifests change).
- Define reasonable limits to protect against abusive tile patterns (rate limiting, concurrency limits).

### 5.4 Monitoring and change management
- Monitor availability and latency of image services and manifest endpoints.
- Track error rates (including viewer‑visible failures).
- Treat manifest changes as contract changes: versioning and change notifications help consumers avoid breakage.



## 6. Typical CH Cloud patterns (examples)

### Pattern A: Institution publishes IIIF; tools consume it
- Institution publishes Image API + Presentation manifests.
- CH Cloud portals/viewers consume manifests directly.
- Annotations may be stored locally or in a dedicated annotation service.

### Pattern B: Aggregator/portal uses Change Discovery
- Institutions publish change feeds.
- Aggregators synchronise updates and keep discovery/indices current.

### Pattern C: Restricted collections with federated access
- IIIF endpoints require federated authentication.
- Viewer access is granted based on group membership or user role.
- Logs and monitoring support auditing without exposing sensitive content.



## 7. References (primary sources)

- IIIF Consortium (overview): https://iiif.io/
- IIIF Image API: https://iiif.io/api/image/
- IIIF Presentation API: https://iiif.io/api/presentation/
- IIIF Change Discovery API: https://iiif.io/api/discovery/
- W3C Web Annotation Data Model: https://www.w3.org/TR/annotation-model/
- Mirador viewer: https://projectmirador.org/
- Universal Viewer: https://universalviewer.io/

# OBJ (Wavefront Object)

OBJ is a simple, widely supported ASCII format for polygonal 3D meshes. It is broadly compatible with 3D modelling and visualization tools and is often used as a legacy exchange format.

## When to use OBJ

- Basic 3D mesh exports.
- Broad tool compatibility is required.
- Level 1 or Level 2 ingestion where the primary need is geometry interchange.

## When not to use OBJ

- When semantic information must accompany geometry (materials, annotations, provenance) without a sidecar mechanism.
- Point clouds or highly detailed scientific scans.
- When compact binary packaging and modern runtime efficiency are required.


## Relevance to Cultural Heritage (CH Cloud)

- Suitable as a compatibility format for 3D assets.
- Requires sidecar metadata (RDF, JSON-LD, XML) to provide semantic context.

## Technical considerations

- Often paired with an `.mtl` file for material definitions.
- No native semantic annotations or rich metadata model.
- Coordinate system, unit scale, and orientation must be documented explicitly.

## References (informative)

- OBJ file format (overview): https://en.wikipedia.org/wiki/Wavefront_.obj_file

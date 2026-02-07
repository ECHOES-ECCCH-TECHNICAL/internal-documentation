# OBJ

OBJ is a simple, widely supported ASCII format for polygonal 3D meshes.
It is commonly used as a compatibility exchange format across many tools, but it is not optimised for modern web delivery.

This page provides practical, non‑normative guidance for handling OBJ assets in CH Cloud workflows.

## When to use OBJ

- basic mesh interchange where broad tool compatibility is required
- legacy export and import workflows where a provider cannot produce glTF or GLB yet
- ingestion pipelines where OBJ is an intermediate step before normalisation

## When not to use OBJ

- when you need compact packaging and efficient runtime delivery (prefer GLB)
- when you require rich semantics to travel with geometry without a sidecar mechanism
- for point clouds or measurement‑grade scan sources

## Interoperability considerations

### Materials and external files

OBJ commonly relies on a companion MTL file and external texture files.
Publish:

- a complete package (OBJ, MTL, textures)
- a manifest of included files
- checksums for integrity

### Units, orientation, and coordinate conventions

OBJ has no universal convention for units or orientation.
Document:

- units (m, cm, mm)
- coordinate system orientation (Y‑up, Z‑up)
- whether coordinates are local or georeferenced, and which CRS applies

### Sidecar metadata

OBJ has no standard embedded metadata model.
Provide descriptive, rights, and provenance metadata via:

- repository record fields, and or
- sidecar JSON or JSON‑LD linked to the asset identifier

### Recommended modernisation path

Where feasible, publish GLB as the preferred delivery derivative and retain OBJ as a compatibility export.

## Validation checks

- confirm that mesh and textures load correctly in a reference tool
- confirm unit scale and orientation against a known reference asset
- confirm the package is complete (no missing textures)
- record provenance: source asset id plus conversion parameters

## References

- OBJ overview: https://en.wikipedia.org/wiki/Wavefront_.obj_file

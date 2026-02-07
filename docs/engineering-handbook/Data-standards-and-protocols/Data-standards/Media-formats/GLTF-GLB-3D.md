# glTF / GLB 

glTF and GLB are modern, web‑native formats optimised for fast loading and rendering.
**GLB** is the binary packaging of **glTF** (single‑file distribution) and is generally preferred for delivery.

This page provides **practical, non‑normative** guidance for adopting glTF/GLB for CH Cloud 3D visualisation and interoperability.

## When to use glTF / GLB

- Interactive 3D viewers and web delivery.
- Dissemination derivatives of complex 3D sources (scans/meshes) after appropriate processing.
- Portal integration where predictable runtime performance matters.

## When not to use glTF / GLB

- Raw scientific scanning outputs where measurement‑grade point clouds must be preserved unchanged (store raw sources separately).
- Workflows requiring extremely high precision without documented conversion parameters and validation.

## Interoperability considerations

### Units, scale, and orientation
- Document coordinate system, units, and orientation conventions.
- Ensure the exported model’s unit scale is explicit and consistent across assets (avoid silent “centimetres vs metres” drift).
- Validate “up axis” expectations across target viewers (e.g., Y‑up vs Z‑up) and standardise within a collection.

### Textures and external dependencies
- Prefer **GLB** for delivery to avoid missing external texture files.
- If using `.gltf` with external resources, publish a package manifest that lists required files and checksums.
- Use consistent texture naming and avoid implicit relative paths that can break when assets are moved.

### Metadata and semantics
glTF does not provide a rich, standard semantic metadata model.
Recommended practice:

- store descriptive/rights/provenance metadata in repository records, and/or
- provide a sidecar JSON/JSON‑LD record linked to the asset identifier.

### Derivative parameters
Record at minimum:

- source format (OBJ, PLY, scan pipeline output, etc.),
- simplification/decimation settings,
- texture baking settings,
- any compression steps applied,
- toolchain names and versions.

## Validation checks

- Load in a reference viewer (smoke test) and confirm textures/materials render as expected.
- Confirm scale/orientation conventions against a known reference asset.
- For `.gltf` packages: confirm all external resources (textures) are present and paths resolve.
- Record checksums for delivered files and keep conversion logs alongside the asset record.

## References

- glTF specification (Khronos): https://registry.khronos.org/glTF/
- Three.js: https://threejs.org/
- Babylon.js: https://www.babylonjs.com/

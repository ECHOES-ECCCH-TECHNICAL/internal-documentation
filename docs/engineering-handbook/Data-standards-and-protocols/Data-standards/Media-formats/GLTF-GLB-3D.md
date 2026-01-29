# glTF / GLB

glTF and GLB are modern, web-native 3D formats optimized for fast loading, rendering, and interchange. GLB is the binary packaging of glTF. These formats are widely used for web-based cultural heritage visualization due to efficiency and strong ecosystem support.



## When to use glTF / GLB

- Interactive 3D viewers and web delivery.
- Compact binary packaging (GLB) is preferred.
- Level 1 or Level 2 integration of 3D content in web tools and portals.

## When not to use glTF / GLB

- Raw scientific scans (dense point clouds, LiDAR) without conversion/downsampling.
- Cases where extremely high precision is required for research-grade analysis.


## Relevance to Cultural Heritage (CH Cloud)

- Strong candidate for web visualization workflows.
- Can be accompanied by JSON-LD metadata describing capture context, provenance, and object-level semantics.


## Technical considerations

- **GLB**: binary bundle; easier distribution.
- **glTF**: JSON + external resources.
- Works well with WebGL ecosystems (e.g., Three.js, Babylon.js).
- Unit/scale definitions must be explicit for interoperability.


## References (informative)

- glTF specification (Khronos): https://registry.khronos.org/glTF/
- Three.js: https://threejs.org/
- Babylon.js: https://www.babylonjs.com/

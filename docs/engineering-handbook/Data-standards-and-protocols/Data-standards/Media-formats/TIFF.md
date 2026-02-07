# TIFF

TIFF is a high‑quality, lossless raster image format widely used in digitisation and preservation workflows.
It supports long‑term durability and can embed rich metadata (EXIF, IPTC, XMP).

This page provides practical, non‑normative guidance for using TIFF in CH Cloud workflows.

## When to use TIFF

- preservation masters for long‑term storage
- digitisation workflows requiring high fidelity (lossless capture)
- as a source master for generating access derivatives or IIIF tiles

## When not to use TIFF

- direct web or API delivery at scale (file sizes are typically too large)
- scenarios with strict storage constraints unless tiered storage and lifecycle policies exist

## Interoperability considerations

### Compression and bit depth

- prefer lossless compression (LZW, ZIP) where appropriate
- avoid lossy compression for masters
- document bit depth and colour space as part of technical metadata

### Metadata extraction and preservation

- extract EXIF, IPTC, XMP and preserve them in the repository metadata model or sidecars
- do not rely on embedded metadata alone for governance or rights assertions

### Identifier and versioning discipline

- link every TIFF master to a stable asset identifier
- if masters are replaced (re‑scan, re‑process), publish a supersession relationship rather than silently overwriting

## Validation checks

- file readability in standard tooling
- technical metadata extraction success (dimensions, bit depth, colour profile)
- checksums computed and recorded (integrity)
- consistency between embedded metadata and repository record where relevant

## References

- TIFF (Adobe historical spec): https://www.adobe.io/open/standards/TIFF.html
- Library of Congress FDD (TIFF): https://www.loc.gov/preservation/digital/formats/fdd/fdd000022.shtml
- IPTC Photo Metadata: https://www.iptc.org/standards/photo-metadata/

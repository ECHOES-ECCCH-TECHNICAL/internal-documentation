# TIFF (Tagged Image File Format)

TIFF is a high-quality, lossless raster image format commonly used in digitization and preservation workflows. TIFF supports long-term durability and fidelity and can embed rich metadata (EXIF, IPTC, XMP).


## When to use TIFF

- Preservation masters for long-term storage.
- Digitization workflows requiring high fidelity (lossless capture).
- As a source master from which IIIF services generate access derivatives.

## When not to use TIFF

- Web/API delivery at scale (TIFF files are typically too large).
- Situations with strict storage constraints unless supported by tiered storage.


## Relevance to Cultural Heritage (CH Cloud)

- Likely accepted as a preservation-grade input format.
- TIFF masters are commonly converted to IIIF-compatible tiles/derivatives for access and interoperability.


## Technical considerations

- Prefer lossless compression options (e.g., LZW/ZIP) where appropriate.
- Ensure consistent metadata extraction and preservation during ingestion.
- Plan storage and transfer strategies for large file sizes.


## References (informative)

- TIFF (Adobe, historical spec): https://www.adobe.io/open/standards/TIFF.html
- IPTC Photo Metadata: https://www.iptc.org/standards/photo-metadata/

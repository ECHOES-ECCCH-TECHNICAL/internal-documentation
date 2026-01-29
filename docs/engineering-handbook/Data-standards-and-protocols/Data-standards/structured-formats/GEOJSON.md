# GeoJSON / WKT (Geospatial Vector Encodings)

GeoJSON and WKT are standard encodings for geospatial vector features. GeoJSON is JSON-based and widely used in web mapping; WKT is a textual geometry encoding commonly used in GIS databases. They are useful for archaeological sites, footprints, georeferenced points, and bounding boxes.

## When to use GeoJSON / WKT

- Representing points, lines, polygons for geospatial metadata.
- Level 1 or Level 2 onboarding of location-based features.
- Integration with web GIS frameworks and spatial indexing.

## When not to use GeoJSON / WKT

- Raster geospatial data (e.g., GeoTIFF imagery).
- Complex geodetic transformations requiring specialized GIS formats/workflows.

## Relevance to Cultural Heritage (CH Cloud)

- Important for services that support spatial search, map interfaces, and archaeological datasets.


## Technical considerations

- GeoJSON assumes WGS 84 longitude/latitude (EPSG:4326) per RFC 7946.
- For WKT in databases, document SRID and coordinate ordering.
- Validate geometry types and coordinate validity to avoid ingestion errors.


## References (informative)

- GeoJSON (RFC 7946): https://www.rfc-editor.org/rfc/rfc7946
- OGC Simple Features (WKT context): https://www.ogc.org/standards/sfa

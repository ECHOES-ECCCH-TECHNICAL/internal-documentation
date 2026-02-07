# GeoJSON and WKT

GeoJSON and WKT are standard encodings for geospatial vector geometries, including points, lines, and polygons.
They are commonly used to represent archaeological sites, footprints, bounding boxes, tracks, and spatial extents in cultural heritage datasets.

This page provides practical, non‑normative guidance for using GeoJSON and WKT in CH Cloud interoperability workflows.

## When to use GeoJSON and WKT

Use GeoJSON and or WKT when you need:

- spatial metadata for discovery (map search, bounding box filters)
- exchange of vector features (points, lines, polygons) between institutions
- storage of geometries in GIS databases (WKT is common in database contexts)
- lightweight delivery to web mapping clients (GeoJSON)

## When not to use GeoJSON and WKT

GeoJSON and WKT are not suitable as the primary format when:

- you are working with raster geospatial data (use GeoTIFF or COG)
- you require complex geodetic workflows and transformations as preserved artefacts (use dedicated GIS workflows)
- you need dense 3D geometry or point clouds (use appropriate 3D formats)

## Recommended conventions

### 1) Coordinate reference system

- GeoJSON assumes WGS84 longitude and latitude (EPSG:4326) per RFC 7946.
- WKT should be accompanied by an explicit SRID or CRS declaration (for example an EPSG code) and an explicit coordinate ordering rule.

If you use a local CRS (projected coordinates), document transformation assumptions and publish both:

- the original geometry (WKT with SRID), and
- a WGS84 representation (GeoJSON) where feasible for portal mapping

### 2) Geometry validity

Validate:

- polygon closure and ring ordering where relevant
- coordinate bounds (avoid invalid longitude and latitude ranges)
- geometry type correctness (Point, LineString, Polygon, Multi*)
- self‑intersections where required by downstream tooling

### 3) Feature identity and attribution

- provide stable identifiers for features (for example `feature_id`)
- include provenance fields (source, capture date, method, precision)
- document uncertainty if the geometry is approximate (bounding box versus surveyed outline)

## Interoperability patterns

- discovery layer: store bounding boxes or points as GeoJSON for map UI
- exchange layer: provide WKT with SRID for GIS‑native ingestion
- semantic layer: link geometry to entities using URIs and publish mappings to controlled place vocabularies where relevant

## References

- GeoJSON specification (RFC 7946): https://www.rfc-editor.org/rfc/rfc7946
- OGC Simple Features (WKT context): https://www.ogc.org/standards/sfa

# MAST Catalogs

MAST provides access to several hosted catalogs via the `Catalogs` class.

## Pan-STARRS (PS1)

Query sources from the Pan-STARRS catalog.

```python
from astroquery.mast import Catalogs
ps1_sources = Catalogs.query_region(coord, radius=0.1, catalog="Panstarrs", table="mean")
```

## HSC (Hubble Source Catalog)

```python
hsc_sources = Catalogs.query_region(coord, radius=0.1, catalog="HSC")
```

## GAIA

```python
gaia_sources = Catalogs.query_region(coord, radius=0.1, catalog="GAIA")
```

## GSC (Guide Star Catalog)

```python
gsc_sources = Catalogs.query_region(coord, radius=0.1, catalog="GSC242")
```

## Criteria-based Catalog Queries

```python
filtered_sources = Catalogs.query_criteria(catalog="HSC", 
                                         mag_v=(10, 15), 
                                         n_detections=(5, 100))
```

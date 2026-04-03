# Advanced MAST Features

## Login and Authentication

Required for accessing proprietary or non-public data.

```python
from astroquery.mast import Observations
# Login with a token from https://auth.mast.stsci.edu/
Observations.login(token="YOUR_MAST_TOKEN")
```

## Cutout Services

Specialized cutout classes for mission data:

- `Tesscut` (TESS)
- `Zcut` (GALEX, etc.)
- `Hapcut` (Hubble Advanced Products)

```python
from astroquery.mast import Tesscut
manifest = Tesscut.download_cutouts(coord, size=5)
```

## Asynchronous Queries

For large datasets, use the `_async` versions of query methods.

```python
from astroquery.mast import Observations
job = Observations.query_region_async(coord, radius=1*u.deg)
# Wait for result
result_table = job.get_results()
```

## Local File Management

MAST products are downloaded to a local cache directory (defaults to `./mastDownload`).

```python
# Change download location
manifest = Observations.download_products(products, download_dir="/path/to/data")
```

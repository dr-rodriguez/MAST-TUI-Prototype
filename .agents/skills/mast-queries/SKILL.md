---
name: mast-queries
description: Provides guidance and patterns for querying the Mikulski Archive for Space Telescopes (MAST) using the `astroquery.mast` library. Use this skill when implementing features that search for astronomical observations, catalogs, or missions (HST, JWST, TESS, etc.) and downloading data products.
---

# MAST Queries (astroquery.mast)

This skill provides patterns for interacting with the MAST archive.

## Core Workflow

### 1. Searching for Observations
The `Observations` class is the primary interface for finding data across multiple missions.

```python
from astroquery.mast import Observations
import astropy.units as u
from astropy.coordinates import SkyCoord

# By Object Name
obs_table = Observations.query_object("M101", radius=".02 deg")

# By Region (Coordinates)
coord = SkyCoord(ra=210.80, dec=54.34, unit=(u.deg, u.deg))
obs_table = Observations.query_region(coord, radius=0.2*u.deg)

# By Criteria (Filtering)
filtered_obs = Observations.query_criteria(
    target_name="M101", 
    instrument_name="WFC3/UVIS",
    project="HST"
)
```

### 2. Retrieving and Downloading Data
Accessing data is a two-step process: listing products, then downloading.

```python
# Get product list for a set of observations
product_list = Observations.get_product_list(obs_table[0:1])

# Filter products (e.g., only minimum recommended products)
filtered_products = Observations.filter_products(product_list, 
                                               extension="fits",
                                               mrp_only=True)

# Download
manifest = Observations.download_products(filtered_products)
```

## Specialized Queries

For more specific use cases, refer to the following:

- **Mission-Specific Searches**: [missions.md](references/missions.md) - HST, JWST, TESS, Galex, etc.
- **Catalogs**: [catalogs.md](references/catalogs.md) - Pan-STARRS, HSC, GAIA, etc.
- **Advanced Features**: [advanced.md](references/advanced.md) - Login/Auth, Cutouts (Tesscut), and asynchronous queries.

## Design Patterns

- **Async Queries**: Use `query_region_async` for long-running searches to avoid blocking the UI.
- **Coordinate Handling**: Always use `astropy.coordinates.SkyCoord` for robust positional queries.
- **Table Management**: Search results are `astropy.table.Table` objects. Use standard table operations for further filtering.

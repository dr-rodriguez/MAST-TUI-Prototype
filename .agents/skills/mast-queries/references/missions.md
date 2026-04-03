# Mission-Specific Searches in MAST

MAST supports several missions with specialized query interfaces via `MastMissions`.

## HST (Hubble Space Telescope)

```python
from astroquery.mast import MastMissions
hst_search = MastMissions(mission='HST')
results = hst_search.query_region(coord)
```

## JWST (James Webb Space Telescope)

JWST queries often use `Observations` but can also be tailored via `MastMissions`.

```python
from astroquery.mast import Observations
jwst_obs = Observations.query_criteria(project="JWST", 
                                     instrument_name="NIRCAM/IMAGE")
```

## TESS (Transiting Exoplanet Survey Satellite)

TESS data is often accessed via `Tesscut` for full-frame image cutouts.

```python
from astroquery.mast import Tesscut
# Query available sectors
sectors = Tesscut.get_sectors(coord)
# Download cutout
manifest = Tesscut.download_cutouts(coord, size=5)
```

## Galex, IUE, Kepler

These and other legacy missions can be queried via their specific mission designations in `MastMissions` or `Observations.query_criteria(project="KEPLER")`.

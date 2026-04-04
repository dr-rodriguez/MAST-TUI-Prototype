from astroquery.mast import Observations


class MastClient:
    """Client for interacting with the MAST archive."""

    def query_observations(self, object_name: str, radius: str = "0.02 deg"):
        """
        Query MAST for observations around a specific object.

        Args:
            object_name: Name of the astronomical object (e.g., 'M31').
            radius: Search radius with units (e.g., '0.02 deg').

        Returns:
            An astropy.table.Table of observations.
        """
        return Observations.query_object(object_name, radius=radius)

    def query_criteria(self, **filters):
        """
        Query MAST for observations based on specific criteria.

        Args:
            **filters: Keyword arguments for query_criteria (e.g., obs_collection='HST').

        Returns:
            An astropy.table.Table of observations.
        """
        # Remove empty filters to avoid issues with query_criteria
        active_filters = {k: v for k, v in filters.items() if v}
        return Observations.query_criteria(**active_filters)

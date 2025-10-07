"""Calculate the angular separation between two sky positions."""

from astropy.coordinates import SkyCoord
import astropy.units as u


def angular_separation(
    ra1_deg: float, dec1_deg: float, ra2_deg: float, dec2_deg: float
):
    """Calculate the angular separation between two sky positions.

    Returns:
    -------
    float
        Angular separation in arcseconds.
    """
    c1 = SkyCoord(ra1_deg * u.deg, dec1_deg * u.deg, frame="icrs")
    c2 = SkyCoord(ra2_deg * u.deg, dec2_deg * u.deg, frame="icrs")
    return c1.separation(c2).arcsecond

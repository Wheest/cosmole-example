from astropy.coordinates import SkyCoord
import astropy.units as u


def convert_equatorial_to_galactic(ra_deg: float, dec_deg: float):
    """
    Convert RA/Dec (ICRS) to Galactic coordinates.

    Parameters
    ----------
    ra_deg : float
        Right ascension in degrees.
    dec_deg : float
        Declination in degrees.

    Returns
    -------
    tuple
        Galactic longitude (l) and latitude (b) in degrees.
    """
    coord = SkyCoord(ra=ra_deg * u.degree, dec=dec_deg * u.degree, frame="icrs")
    gal = coord.galactic
    return gal.l.degree, gal.b.degree

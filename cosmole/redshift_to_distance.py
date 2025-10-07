"""Convert redshift to comoving distance using astropy and Planck18 cosmology."""

from astropy.cosmology import Planck18 as cosmo


def redshift_to_distance(z: float):
    """Convert redshift to comoving distance using Planck18 cosmology.

    Parameters
    ----------
    z : float
        Redshift.

    Returns:
    -------
    float
        Comoving distance in megaparsecs (Mpc).
    """
    return cosmo.comoving_distance(z).value

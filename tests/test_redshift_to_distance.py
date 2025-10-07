import pytest
from astropy.cosmology import Planck18 as cosmo
from cosmole import redshift_to_distance

def test_redshift_to_distance():
    z = 0.5
    d = redshift_to_distance(z)
    expected = cosmo.comoving_distance(z).value
    assert pytest.approx(d, rel=1e-6) == expected

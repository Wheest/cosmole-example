import pytest
from astropy.coordinates import SkyCoord
import astropy.units as u
from cosmole import angular_separation


def test_angular_separation():
    ra1, dec1 = 10.0, 20.0
    ra2, dec2 = 10.1, 20.1
    sep = angular_separation(ra1, dec1, ra2, dec2)
    c1 = SkyCoord(ra1 * u.deg, dec1 * u.deg, frame="icrs")
    c2 = SkyCoord(ra2 * u.deg, dec2 * u.deg, frame="icrs")
    expected = c1.separation(c2).arcsecond
    assert pytest.approx(sep, rel=1e-6) == expected

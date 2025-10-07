import pytest
from astropy.coordinates import SkyCoord
import astropy.units as u
from cosmole import convert_equatorial_to_galactic


def test_convert_equatorial_to_galactic():
    ra, dec = 83.82208, -5.39111  # Approx location of Orion Nebula
    l, b = convert_equatorial_to_galactic(ra, dec)  # noqa: E741
    coord = SkyCoord(ra=ra * u.deg, dec=dec * u.deg, frame="icrs").galactic
    assert pytest.approx(l, rel=1e-6) == coord.l.degree
    assert pytest.approx(b, rel=1e-6) == coord.b.degree

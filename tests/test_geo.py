from os import access
import pytest

from ipinfo import handler
from vtrace import geo


def test_geolocation_class():
    access_token = "access_token"

    geolocator = geo.Geolocator(access_token=access_token)
    assert isinstance(geolocator, geo.Geolocator)

    assert geolocator.access_token == access_token
    assert isinstance(geolocator.handler, handler.Handler)


def test_geolocation_service(monkeypatch):
    def mock_response(*args, **kwargs):
        return (list(), list())

    monkeypatch.setattr(geo.Geolocator, "geolocate", mock_response)

    access_token = "access_token"
    ip_address = "192.168.1.1"

    geolocator = geo.Geolocator(access_token=access_token)
    details = geolocator.geolocate(ip_address=ip_address)

    print(details)

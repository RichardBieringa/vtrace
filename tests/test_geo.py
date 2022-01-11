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
        return geo.GeoLocationDetails(
            bogon=False,
            ip="142.250.179.174",
            latitude="52.3740",
            longitude="4.8897",
            country_name="Netherlands",
            hostname="ams15s41-in-f14.1e100.net",
            city="Amsterdam",
            country="NL",
            region="North Holland",
            loc="52.3740,4.8897",
            org="AS15169 Google LLC",
            postal="1012",
            timezone="Europe/Amsterdam",
        )

    monkeypatch.setattr(geo.Geolocator, "geolocate", mock_response)

    access_token = "access_token"
    ip_address = "192.168.1.1"

    geolocator = geo.Geolocator(access_token=access_token)
    details = geolocator.geolocate(ip_address=ip_address)

    assert isinstance(details, geo.GeoLocationDetails)

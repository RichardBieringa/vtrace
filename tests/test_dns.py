import pytest
import socket

from vtrace import dns


def test_dns_resolve_valid_hostname():
    assert type(dns.get_ip_address("google.com")) is str


def test_dns_resolve_invalid_hostname():
    with pytest.raises(ValueError):
        dns.get_ip_address("@@@@@@@@@")


def test_dns_unresolvable_host():
    with pytest.raises(socket.gaierror):
        dns.get_ip_address("this-host-does-not-exist.but.is.valid")

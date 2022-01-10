import pytest
from vtrace import utils


@pytest.mark.parametrize(
    "ipv4_address",
    [
        "0.0.0.0",
        "255.255.255.255",
        "127.0.0.1",
        "192.168.1.1",
    ],
)
def test_is_ipv4_address(ipv4_address):
    assert utils.is_valid_ipv4_address(ipv4_address)


@pytest.mark.parametrize(
    "non_ipv4_address",
    [
        "-0.0.0.0",
        "-1.0.0.0",
        "256.255.255.255",
        "255.255.255.256",
        "my.ip.address.is",
        "my.ip.address.is",
        "!.0.0.0",
    ],
)
def test_is_not_ipv4_address(non_ipv4_address):
    assert not utils.is_valid_ipv4_address(non_ipv4_address)


@pytest.mark.parametrize(
    "ipv6_address",
    [
        "FE80::8329",
        "FE80::FFFF:8329",
        "FE80::B3FF:FFFF:8329",
        "FE80::0202:B3FF:FFFF:8329",
        "FE80::0000:0202:B3FF:FFFF:8329",
        "FE80::0000:0000:0202:B3FF:FFFF:8329",
        "FE80:0000:0000:0000:0202:B3FF:FFFF:8329",
        "fe80::21d8:f50:c295:c4be",
        "2001:cdba:0000:0000:0000:0000:3257:9652",
        "2001:cdba:0:0:0:0:3257:9652",
        "2001:cdba::3257:9652",
        "2001:cdba::1222",
        "21DA:D3:0:2F3B:2AA:FF:FE28:9C5A",
        "2001:cdba::1:2:3:3257:9652",
    ],
)
def test_is_ipv6_address(ipv6_address):
    assert utils.is_valid_ipv6_address(ipv6_address)


@pytest.mark.parametrize(
    "non_ipv6_address",
    [
        "0.0.0.0",
        "255.255.255.255",
        "my.ip.address.is",
    ],
)
def test_is_not_ipv6_address(non_ipv6_address):
    assert not utils.is_valid_ipv6_address(non_ipv6_address)


@pytest.mark.parametrize(
    "hostname",
    [
        "google.com",
        "9tails.io",
        "sub.domain.com",
        "localhost",
    ],
)
def test_is_hostname(hostname):
    assert utils.is_valid_hostname(hostname)


@pytest.mark.parametrize(
    "non_hostname",
    [
        "https://google.com",
        "https://www.google.com",
        "ftp://www.google.com",
    ],
)
def test_is_not_hostname(non_hostname):
    assert not utils.is_valid_hostname(non_hostname)

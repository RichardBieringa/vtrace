import pytest
from scapy import sendrecv

from vtrace import traceroute


def test_source_dest_ports(monkeypatch):
    def mock_response(*args, **kwargs):
        print("Test")
        return (list(), list())

    monkeypatch.setattr(sendrecv, "sr", mock_response)
    results = traceroute.traceroute("google.com")

    assert results == []


def test_traceroute_sortable():
    results = [
        traceroute.TraceRouteResult(5, "192.168.1.1", 100.00),
        traceroute.TraceRouteResult(3, "192.168.1.1", 100.00),
        traceroute.TraceRouteResult(1, "192.168.1.1", 100.00),
        traceroute.TraceRouteResult(2, "192.168.1.1", 100.00),
        traceroute.TraceRouteResult(8, "192.168.1.1", 100.00),
    ]

    results.sort()

    assert results[0].ttl < results[1].ttl
    results.sort(reverse=True)

    assert results[1].ttl < results[0].ttl

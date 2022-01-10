import enum
import logging

from typing import List
from dataclasses import dataclass

from scapy.layers import inet
from scapy import sendrecv

from vtrace import dns


@dataclass
class TraceRouteResult:
    """Represents the return value of the traceroute command"""

    ttl: int
    ip: str
    rtt: float


class TraceRouteProtocols(enum.Enum):
    """Represents the types of traceroute requests the user can make"""

    TCP_SYN = enum.auto()
    UDP = enum.auto()
    DNS = enum.auto()


MIN_TTL = 1
MAX_TTL = 30


def traceroute(
    target: str, protocol: TraceRouteProtocols = TraceRouteProtocols.TCP_SYN
) -> List[TraceRouteResult]:
    """Performs a traceroute request to the given host"""

    logging.info("Traceroute::traceroute(%s)", target)
    ip_addr = dns.get_ip_address(target)

    ttl = (0, MAX_TTL)
    source_port = inet.RandShort()
    destination_port = 80

    network = inet.IP(dst=ip_addr, id=inet.RandShort(), ttl=ttl)
    transport = inet.TCP(dport=destination_port, sport=source_port)

    packet = network / transport

    ans, unans = sendrecv.sr(packet, timeout=2, verbose=0)

    seen = {}
    results = []
    for send, receive in ans:
        # Prevent duplicate entries
        if receive.src not in seen:

            # Add it to the hash map to prevent duplicates
            seen[receive.src] = True

            # Calculates the Round-Trip-Time in miliseconds
            rtt = (receive.time - send.sent_time) * 1000

            entry = TraceRouteResult(send.ttl, receive.src, rtt)
            results.append(entry)

    return results

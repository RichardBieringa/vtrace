import click

from vtrace import traceroute
from vtrace import dns
from vtrace import utils


@click.command()
@click.argument("target", nargs=1)
@click.option("-m", "--min-ttl", default=1, type=int)
@click.option("-M", "--max-ttl", default=64, type=int)
@click.option("-s", "--source-port", default=None, type=int)
@click.option("-d", "--destination-port", default=80, type=int)
@click.option("-t", "--timeout", default=3, type=int)
@click.option("-T", "--tcp", default=0, type=bool, is_flag=True)
@click.option("-I", "--icmp", default=0, type=bool, is_flag=True)
@click.option("-U", "--udp", default=0, type=bool, is_flag=True)
def main(
    target: str,
    min_ttl: int,
    max_ttl: int,
    source_port: int,
    destination_port: int,
    timeout: int,
    tcp: bool,
    icmp: bool,
    udp: bool,
) -> None:
    """Visually trace the route to a target"""

    if utils.is_valid_ipv4_address(target):
        ip_address = target
    else:
        ip_address = dns.get_ip_address(target)

    # Allow only one mode (TCP/UDP/ICMP)
    if len([x for x in [tcp, udp, icmp] if x == True]) > 1:
        raise ValueError("Can not combine TCP/UDP/ICMP flags (-T/-U/-I)")

    # Set the protocol based on the flag value, defaults to TCP_SYN
    protocol = traceroute.TraceRouteProtocol.TCP_SYN
    if udp:
        protocol = traceroute.TraceRouteProtocol.UDP
    elif icmp:
        protocol = traceroute.TraceRouteProtocol.ICMP

    # Perform the traceroute
    results = traceroute.traceroute(
        target_ip=ip_address,
        protocol=protocol,
        min_ttl=min_ttl,
        max_ttl=max_ttl,
        source_port=source_port,
        destination_port=destination_port,
        timeout=timeout,
    )

    print(f"traceroute to {target} ({ip_address}), {max_ttl} hops max")
    for entry in results:
        print(f"{entry.ttl}\t{entry.ip}\t{entry.rtt:.2f}ms")


if __name__ == "__main__":
    main()  # pylint: disable=no-value-for-parameter

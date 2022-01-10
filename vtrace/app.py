import click
import re


from vtrace import traceroute
from vtrace import dns


@click.command()
@click.argument("target", nargs=1)
@click.option("-m", "--max-ttl", default=64, type=int)
@click.option("-p", "--port", default=443, type=int)
def main(target: str, max_ttl: int, port: int) -> None:
    """Visually trace the route to a target"""

    ip_address = None

    # Check to see if the user passed an IP Address
    ip_regex = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    if ip_regex.match(target):
        ip_address = target
    else:
        # Check to see if the user passed a DNS compliant hostname
        if not dns.is_valid_hostname(target):
            raise ValueError("Target is not a valid hostname")
        else:
            ip_address = dns.get_ip_address(target)

    # Perform the traceroute
    results = traceroute.traceroute(
        ip_address, protocol=traceroute.TraceRouteProtocols.TCP_SYN
    )

    print(f"traceroute to {target} ({ip_address}), 64 hops max")
    for entry in results:
        print(f"{entry.ttl}\t{entry.ip}\t{entry.rtt:.2f}ms")


if __name__ == "__main__":
    main()

import click
import typing

import dns


@click.command()
@click.argument("hostname", nargs=1)
def main(hostname: str) -> None:
    """Visually trace the route to a host"""

    ip_addrs = dns.get_ip_address(hostname)
    print(ip_addrs)


if __name__ == "__main__":
    main()

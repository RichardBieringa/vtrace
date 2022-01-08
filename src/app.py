import click
import typing
from dns import is_valid_hostname


@click.command()
@click.argument("hostname", nargs=1)
def main(hostname: str) -> None:
    """Visually trace the route to a host"""
    print(is_valid_hostname(hostname))


if __name__ == "__main__":
    main()

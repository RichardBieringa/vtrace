import click
import typing

@click.command()
@click.option("--verbose", is_flag=True)
@click.argument("host", nargs=1)
def main(host: str) -> None:
    """Visually trace the route to a host"""
    print(f"Hello {host}!")


if __name__ == "__main__":
    main()

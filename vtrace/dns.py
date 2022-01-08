import socket
import re
from typing import List


def is_valid_hostname(hostname: str) -> bool:
    """Returns True if the hostname is valid"""

    host_re = re.compile(
        "^(([a-zA-Z0-9]|[a-zA-Z0-9][a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9]|[A-Za-z0-9][A-Za-z0-9\-]*[A-Za-z0-9])$"
    )
    matches = host_re.match(hostname)

    if matches:
        return True
    else:
        return False


def get_ip_address(hostname: str, port: int = 443) -> List[int]:
    """Gets the IP address given a valid hostname

    Uses socket.getaddrinfo
    https://docs.python.org/3/library/socket.html#socket.getaddrinfo"""

    if not is_valid_hostname(hostname):
        raise ValueError(f"Hostname: {hostname} is not valid.")

    print(socket.getaddrinfo(host=hostname, port=port, type=socket.SOCK_STREAM))

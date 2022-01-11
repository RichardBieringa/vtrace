import os
import ipinfo
from typing import Optional

try:
    import dotenv

    dotenv.load_dotenv()
except ImportError:
    print("Dotenv not loaded")


class Geolocator:
    """Allows the user to look up geolocation info from an IP address"""

    def __init__(self, access_token: Optional[str] = None) -> None:
        # Fetch access_token from environment variables if unspecified
        if not access_token:
            access_token = os.environ.get("IP_INFO_ACCESS_TOKEN")

        self.access_token = access_token
        self.handler = ipinfo.getHandler(access_token)

    def geolocate(self, ip_address: str, timeout: int = 2) -> None:
        """Synchronously request geolocation for an IP address"""
        details = self.handler.getDetails(ip_address, timeout)

        print(details)
        return details

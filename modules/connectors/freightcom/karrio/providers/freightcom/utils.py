import base64
from typing import Optional
import math

from karrio import lib
from karrio.core import Settings as BaseSettings


class Settings(BaseSettings):
    """Freightcom connection settings."""

    username: str
    password: str
    api_key: str

    account_country_code: str = None
    metadata: dict = {}
    config: dict = {}

    @property
    def server_url(self):
        return (
            "https://customer-external-api.ssd-test.freightcom.com"
            if self.test_mode
            else "https://external-api.freightcom.com"
        )

    @property
    def carrier_name(self):
        return "freightcom"

    @property
    def connection_config(self) -> lib.units.Options:
        from karrio.providers.freightcom.units import ConnectionConfig

        return lib.to_connection_config(
            self.config or {},
            option_type=ConnectionConfig,
        )

def download_label(file_url: str) -> str:
    return lib.request(
        decoder=lambda b: base64.encodebytes(b).decode("utf-8"),
        url=file_url,
    )


def ceil(value: Optional[float]) -> Optional[int]:
    if value is None:
        return None
    return math.ceil(value)

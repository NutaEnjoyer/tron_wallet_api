from typing import Tuple

from tronpy.async_tron import AsyncTron
from tronpy.providers import AsyncHTTPProvider


class TronGrid:
    def __init__(self, api_key: str):
        self.provider = AsyncHTTPProvider(
            endpoint_uri="https://api.trongrid.io",
            api_key=api_key
        )
        self.tron = AsyncTron(provider=self.provider)

    async def get_wallet_info(self, address: str) -> Tuple[float, int, int]:
        """
        Params: 
            address: str 
        Returns: 
            (balance: float, bandwidth: int, energy: int)
        """
        acc = await self.tron.get_account(address)
        balance = acc.get('balance', 0) / 1_000_000
        resources = await self.tron.get_account_resource(address)
        bandwidth = resources.get('freeNetLimit', 0)
        energy = resources.get('TotalEnergyLimit', 0)

        return (balance, bandwidth, energy)

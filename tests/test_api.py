import pytest
from httpx import AsyncClient, ASGITransport
from app.app import app
from app.api.wallet.router import get_tron_grid, get_wallet_service

class DummyTronGrid:
    async def get_wallet_info(self, address: str):
        return (1.23, 100, 200)

class DummyWalletRequestService:
    async def create_wallet_request(self, address, wallet_info):
        return None
    async def get_last_wallet_requests(self, skip: int = 0, limit: int = 10):
        return []

@pytest.mark.asyncio
async def test_get_wallets():
    app.dependency_overrides[get_tron_grid] = lambda: DummyTronGrid()
    app.dependency_overrides[get_wallet_service] = lambda: DummyWalletRequestService()
    transport = ASGITransport(app=app)
    async with AsyncClient(base_url="http://test", transport=transport) as ac:
        print("IN")
        response = await ac.get("/api/wallets")
    print(f'{response.text=}')
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    app.dependency_overrides = {}
import pytest
from app.services.wallet import WalletRequestService
from app.schemas.wallet import WalletInfo

import asyncio

@pytest.mark.asyncio
async def test_create_wallet_request(monkeypatch):
    class DummySession:
        async def __aenter__(self): return self
        async def __aexit__(self, exc_type, exc, tb): pass
        def add(self, obj): self.obj = obj
        async def commit(self): pass
        async def refresh(self, obj): pass
    
    service = WalletRequestService(session=lambda: DummySession())
    wallet_info = WalletInfo(balance=1.23, bandwidth=100, energy=200)
    result = await service.create_wallet_request("TTestAddress", wallet_info)
    assert result.address == "TTestAddress"
    assert result.balance == 1.23
    assert result.bandwidth == 100
    assert result.energy == 200
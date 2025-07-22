from fastapi import APIRouter, Depends, HTTPException, status, Query
from app.services.wallet import WalletRequestService
from app.schemas.wallet import WalletDB, WalletInfo
from app.tron_grid.tron_grid import TronGrid
from app.core.config import settings
from typing import List


router = APIRouter(
    prefix="/wallets",
    tags=["Wallet Management"]
)


def get_wallet_service() -> WalletRequestService:
    return WalletRequestService()

def get_tron_grid() -> TronGrid:
    return TronGrid(settings.TRONGRID_API_KEY)


@router.post(
    "",
    response_model=WalletInfo,
    summary="Get wallet's info",
    description="Retrieve a wallet's info"
)
async def get_wallet_info(
    wallet_address: str,
    service: WalletRequestService = Depends(get_wallet_service),
    tron: TronGrid = Depends(get_tron_grid)
) -> WalletInfo:
    try:
        info = await tron.get_wallet_info(wallet_address)

        wallet_info = WalletInfo(
            balance = info[0],
            bandwidth = info[1],
            energy = info[2]
        )

        await service.create_wallet_request(
            address=wallet_address,
            wallet_info=wallet_info
        )

        return wallet_info
    
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))


@router.get(
    "",
    response_model=List[WalletDB],
    summary="Get last wallet requests",
    description="Get a paginated list of last wallet requests"
)
async def get_last_wallet_requests(
    skip: int = Query(0, ge=0, description="Number of records to skip"),
    limit: int = Query(10, ge=1, le=100, description="Max records to return"),
    service: WalletRequestService = Depends(get_wallet_service)
) -> List[WalletDB]:
    try:
        return await service.get_last_wallet_requests(skip=skip, limit=limit)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))

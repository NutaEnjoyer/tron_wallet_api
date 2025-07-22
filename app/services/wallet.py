from fastapi import HTTPException
from sqlalchemy import select

from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from app.core.database import new_session
from app.schemas.wallet import WalletInfo, WalletDB
from app.models.wallet import WalletRequest


class WalletRequestService:
    def __init__(self, session: async_sessionmaker[AsyncSession] = new_session):
        self.session = session

    async def create_wallet_request(self, address: str, wallet_info: WalletInfo):
        async with self.session() as session:
            wallet_dict = wallet_info.model_dump()
            db_wallet = WalletRequest(
                address=address,
                **wallet_dict
            )
            session.add(db_wallet)
            await session.commit()
            await session.refresh(db_wallet)

            return db_wallet

    async def get_last_wallet_requests(self, skip: int = 0, limit: int = 10):
        async with self.session() as session:
            result = await session.execute(
                select(WalletRequest).order_by(WalletRequest.id.desc()).offset(skip).limit(limit)
            )
            wallets = result.scalars().all()
            return wallets


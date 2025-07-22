from sqlalchemy import DateTime, Integer, BigInteger, Float, String, Enum as SQLEnum
from sqlalchemy.orm import mapped_column, Mapped

from app.models.base import Base


class WalletRequest(Base):
    __tablename__ = "wallet_requests"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    address: Mapped[str] = mapped_column(String, index=True, nullable=False)
    balance: Mapped[float] = mapped_column(Float)
    bandwidth: Mapped[int] = mapped_column(BigInteger)
    energy: Mapped[int] = mapped_column(BigInteger)

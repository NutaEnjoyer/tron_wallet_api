from pydantic import BaseModel


class WalletInfo(BaseModel):
    balance: float
    bandwidth: int
    energy: int


class WalletDB(WalletInfo):
    id: int | None = None
    address: str

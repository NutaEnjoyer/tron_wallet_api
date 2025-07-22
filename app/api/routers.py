from fastapi import APIRouter
from app.api.wallet.router import router as wallet_router


routers = APIRouter(
    prefix="/api",
    tags=["API"],
    responses={
        404: {"description": "Not found"},
        500: {"description": "Internal server error"},
    },
)

router_list = [
    wallet_router
]

for router in router_list:
    routers.include_router(router)


def get_api_router() -> APIRouter:
    return routers

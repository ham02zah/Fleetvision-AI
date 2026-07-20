from app.api.v1.auth import router as auth_router
from app.api.v1.users import router as users_router
from app.api.v1.fleet import router as fleet_router

__all__ = [
    "auth_router",
    "users_router",
    "fleet_router",
]

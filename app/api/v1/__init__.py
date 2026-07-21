from app.api.v1.auth import router as auth_router
from app.api.v1.users import router as users_router
from app.api.v1.fleet import router as fleet_router
from app.api.v1.vehicle import router as vehicle_router
from app.api.v1.driver import router as driver_router
from app.api.v1.trip import router as trip_router
from app.api.v1.maintenance import router as maintenance_router

__all__ = [
    "auth_router",
    "users_router",
    "fleet_router",
    "vehicle_router",
    "driver_router",
    "trip_router",
    "maintenance_router",
]
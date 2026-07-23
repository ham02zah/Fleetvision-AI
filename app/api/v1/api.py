from fastapi import APIRouter

from app.api.v1.auth import router as auth_router
from app.api.v1.driver import router as driver_router
from app.api.v1.fleet import router as fleet_router
from app.api.v1.users import router as user_router
from app.api.v1.vehicle import router as vehicle_router
from app.api.v1.trip import router as trip_router

from app.api.v1.endpoints.database import router as database_router
from app.api.v1.endpoints.health import router as health_router
from app.api.v1.maintenance import router as maintenance_router
from app.api.v1.vehicle_status import router as vehicle_status_router

api_router = APIRouter()

# Health & Database
api_router.include_router(health_router)
api_router.include_router(database_router)

# Authentication
api_router.include_router(auth_router)

# Main API
api_router.include_router(user_router)
api_router.include_router(fleet_router)
api_router.include_router(driver_router)
api_router.include_router(vehicle_router)
api_router.include_router(trip_router)
api_router.include_router(maintenance_router)
api_router.include_router(vehicle_status_router)

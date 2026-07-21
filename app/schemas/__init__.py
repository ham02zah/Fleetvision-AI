from app.schemas.fleet import (
    FleetCreate,
    FleetListResponse,
    FleetResponse,
    FleetUpdate,
)

from app.schemas.user import (
    UserCreate,
    UserListResponse,
    UserPublic,
    UserResponse,
    UserUpdate,
)

from app.schemas.driver import (
    DriverCreate,
    DriverUpdate,
    DriverResponse,
    DriverSummary,
    DriverListResponse,
)

from app.schemas.trip import (
    TripCreate,
    TripUpdate,
    TripResponse,
    TripSummary,
    TripListResponse,
)

from app.schemas.maintenance import (
    MaintenanceCreate,
    MaintenanceUpdate,
    MaintenanceResponse,
    MaintenanceListResponse,
)

__all__ = [
    # Users
    "UserCreate",
    "UserResponse",
    "UserUpdate",
    "UserPublic",
    "UserListResponse",

    # Fleets
    "FleetCreate",
    "FleetUpdate",
    "FleetResponse",
    "FleetListResponse",

    # Drivers
    "DriverCreate",
    "DriverUpdate",
    "DriverResponse",
    "DriverSummary",
    "DriverListResponse",

    # Trips
    "TripCreate",
    "TripUpdate",
    "TripResponse",
    "TripCreate",
    "TripSummary",
    "TripListResponse",

    "MaintenanceCreate",
    "MaintenanceUpdate",
    "MaintenanceResponse",
    "MaintenanceListResponse",
]
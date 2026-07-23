from app.models.user import User
from app.models.fleet import Fleet
from app.models.vehicle import Vehicle
from app.models.driver import Driver
from app.models.trip import Trip
from app.models.maintenance import Maintenance
from app.models.telemetry import Telemetry
from app.models.vehicle_status import VehicleStatus

__all__ = [
    "User",
    "Fleet",
    "Vehicle",
    "Driver",
    "Trip",
    "Maintenance",
    "Telemetry",
    "VehicleStatus",
]
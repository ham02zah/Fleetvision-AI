from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict

from app.models.trip import TripStatus


class TripBase(BaseModel):
    fleet_id: UUID
    vehicle_id: UUID
    driver_id: UUID

    origin: str
    destination: str

    departure_time: datetime
    arrival_time: datetime | None = None

    distance_km: float | None = None
    average_speed: float | None = None
    fuel_used_liters: float | None = None

    notes: str | None = None

    status: TripStatus = TripStatus.PLANNED


class TripCreate(TripBase):
    pass


class TripUpdate(BaseModel):
    origin: str | None = None
    destination: str | None = None

    departure_time: datetime | None = None
    arrival_time: datetime | None = None

    distance_km: float | None = None
    average_speed: float | None = None
    fuel_used_liters: float | None = None

    notes: str | None = None

    status: TripStatus | None = None


class TripResponse(TripBase):
    id: UUID
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class TripSummary(BaseModel):
    id: UUID
    origin: str
    destination: str
    status: TripStatus

    model_config = ConfigDict(from_attributes=True)


class TripListResponse(BaseModel):
    items: list[TripSummary]
    total: int
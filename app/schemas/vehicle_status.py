from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict

from app.models.vehicle_status import VehicleState


class VehicleStatusBase(BaseModel):
    vehicle_id: UUID

    latitude: float
    longitude: float

    speed: float = 0
    heading: float = 0

    ignition: bool = False
    engine_running: bool = False

    state: VehicleState = VehicleState.OFFLINE

    last_seen: datetime


class VehicleStatusCreate(VehicleStatusBase):
    pass


class VehicleStatusUpdate(BaseModel):
    latitude: float | None = None
    longitude: float | None = None

    speed: float | None = None
    heading: float | None = None

    ignition: bool | None = None
    engine_running: bool | None = None

    state: VehicleState | None = None

    last_seen: datetime | None = None


class VehicleStatusResponse(VehicleStatusBase):
    id: UUID

    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class VehicleStatusListResponse(BaseModel):
    items: list[VehicleStatusResponse]
    total: int
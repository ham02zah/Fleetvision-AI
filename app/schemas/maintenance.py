from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict

from app.models.maintenance import (
    MaintenanceStatus,
    MaintenanceType,
)


class MaintenanceBase(BaseModel):
    vehicle_id: UUID

    maintenance_type: MaintenanceType
    status: MaintenanceStatus = MaintenanceStatus.SCHEDULED

    service_date: datetime
    next_service_date: datetime | None = None

    mileage: float | None = None
    cost: float | None = None

    service_center: str | None = None
    technician: str | None = None

    notes: str | None = None


class MaintenanceCreate(MaintenanceBase):
    """
    Schema used when creating a maintenance record.
    """
    pass


class MaintenanceUpdate(BaseModel):
    maintenance_type: MaintenanceType | None = None
    status: MaintenanceStatus | None = None

    service_date: datetime | None = None
    next_service_date: datetime | None = None

    mileage: float | None = None
    cost: float | None = None

    service_center: str | None = None
    technician: str | None = None

    notes: str | None = None


class MaintenanceResponse(MaintenanceBase):
    id: UUID

    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(
        from_attributes=True,
    )


class MaintenanceListResponse(BaseModel):
    items: list[MaintenanceResponse]
    total: int
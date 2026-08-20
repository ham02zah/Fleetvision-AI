
from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict

from app.models.alert import (
    AlertSeverity,
    AlertStatus,
    AlertType,
)


# ==========================================================
# Base Alert
# ==========================================================


class AlertBase(BaseModel):
    vehicle_id: UUID

    title: str

    description: str

    alert_type: AlertType

    severity: AlertSeverity


# ==========================================================
# Create Alert
# ==========================================================


class AlertCreate(AlertBase):
    pass


# ==========================================================
# Update Alert Status
# ==========================================================


class AlertStatusUpdate(BaseModel):
    status: AlertStatus


# ==========================================================
# Alert Response
# ==========================================================


class AlertResponse(AlertBase):
    id: UUID

    status: AlertStatus

    created_at: datetime

    updated_at: datetime

    acknowledged_at: datetime | None = None

    resolved_at: datetime | None = None

    model_config = ConfigDict(
        from_attributes=True,
    )


# ==========================================================
# Alert List Response
# ==========================================================


class AlertListResponse(BaseModel):
    alerts: list[AlertResponse]

    total: int

    skip: int

    limit: int


# ==========================================================
# Alert Statistics
# ==========================================================


class AlertStatisticsResponse(BaseModel):
    total_alerts: int

    active_alerts: int

    acknowledged_alerts: int

    resolved_alerts: int

    low_alerts: int

    medium_alerts: int

    high_alerts: int

    critical_alerts: int


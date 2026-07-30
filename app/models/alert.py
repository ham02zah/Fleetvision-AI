from __future__ import annotations

from enum import Enum
from uuid import UUID, uuid4
from datetime import datetime, timezone

from sqlalchemy import (
    String,
    Text,
    DateTime,
    Enum as SQLEnum,
    ForeignKey,
)

from sqlalchemy.dialects.postgresql import UUID as PG_UUID

from sqlalchemy.orm import (
    relationship,
    Mapped,
    mapped_column,
)

from app.database.base import Base


# --------------------------------------------------
# Alert Severity
# --------------------------------------------------

class AlertSeverity(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"


# --------------------------------------------------
# Alert Type
# --------------------------------------------------

class AlertType(str, Enum):
    SPEEDING = "SPEEDING"

    FATIGUE = "FATIGUE"

    COLLISION = "COLLISION"

    MAINTENANCE = "MAINTENANCE"

    ENGINE = "ENGINE"

    FUEL = "FUEL"

    BATTERY = "BATTERY"

    GEOFENCE = "GEOFENCE"

    AI_RISK = "AI_RISK"


# --------------------------------------------------
# Alert Status
# --------------------------------------------------

class AlertStatus(str, Enum):
    ACTIVE = "ACTIVE"

    ACKNOWLEDGED = "ACKNOWLEDGED"

    RESOLVED = "RESOLVED"


# --------------------------------------------------
# Alert Model
# --------------------------------------------------

class Alert(Base):

    __tablename__ = "alerts"

    id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
    )

    vehicle_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey(
            "vehicles.id",
            ondelete="CASCADE",
        ),
        nullable=False,
    )

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    description: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    alert_type: Mapped[AlertType] = mapped_column(
        SQLEnum(
            AlertType,
            name="alert_type_enum",
        ),
        nullable=False,
    )

    severity: Mapped[AlertSeverity] = mapped_column(
        SQLEnum(
            AlertSeverity,
            name="alert_severity_enum",
        ),
        nullable=False,
    )

    status: Mapped[AlertStatus] = mapped_column(
        SQLEnum(
            AlertStatus,
            name="alert_status_enum",
        ),
        default=AlertStatus.ACTIVE,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )

    vehicle = relationship(
        "Vehicle",
        back_populates="alerts",
    )
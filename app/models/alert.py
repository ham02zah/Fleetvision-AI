from __future__ import annotations

from datetime import datetime, timezone
from enum import Enum
from uuid import UUID, uuid4

from sqlalchemy import (
    DateTime,
    Enum as SQLEnum,
    ForeignKey,
    String,
    Text,
)
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base


# ==========================================================
# Alert Severity
# ==========================================================


class AlertSeverity(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"


# ==========================================================
# Alert Type
# ==========================================================


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


# ==========================================================
# Alert Status
# ==========================================================


class AlertStatus(str, Enum):
    ACTIVE = "ACTIVE"
    ACKNOWLEDGED = "ACKNOWLEDGED"
    RESOLVED = "RESOLVED"


# ==========================================================
# Alert Model
# ==========================================================


class Alert(Base):
    __tablename__ = "alerts"

    # ------------------------------------------------------
    # Primary Key
    # ------------------------------------------------------

    id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
    )

    # ------------------------------------------------------
    # Vehicle
    # ------------------------------------------------------

    vehicle_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey(
            "vehicles.id",
            ondelete="CASCADE",
        ),
        nullable=False,
    )

    # ------------------------------------------------------
    # Alert Information
    # ------------------------------------------------------

    title: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    description: Mapped[str] = mapped_column(
        Text,
        nullable=False,
    )

    # ------------------------------------------------------
    # Alert Classification
    # ------------------------------------------------------

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

    # ------------------------------------------------------
    # Alert Lifecycle
    # ------------------------------------------------------

    status: Mapped[AlertStatus] = mapped_column(
        SQLEnum(
            AlertStatus,
            name="alert_status_enum",
        ),
        nullable=False,
        default=AlertStatus.ACTIVE,
    )

    # ------------------------------------------------------
    # Timestamps
    # ------------------------------------------------------

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )

    acknowledged_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
        default=None,
    )

    resolved_at: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
        default=None,
    )

    # ------------------------------------------------------
    # Vehicle Relationship
    # ------------------------------------------------------

    vehicle = relationship(
        "Vehicle",
        back_populates="alerts",
    )


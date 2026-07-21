from enum import Enum
from uuid import uuid4

from sqlalchemy import (
    String,
    Float,
    DateTime,
    ForeignKey,
    Text,
    Enum as SQLEnum,
)

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from app.database.base import Base
from app.database.mixins import TimestampMixin


class MaintenanceStatus(str, Enum):
    SCHEDULED = "scheduled"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class MaintenanceType(str, Enum):
    OIL_CHANGE = "oil_change"
    TIRE_ROTATION = "tire_rotation"
    BRAKE_SERVICE = "brake_service"
    ENGINE_SERVICE = "engine_service"
    BATTERY = "battery"
    INSPECTION = "inspection"
    OTHER = "other"


class Maintenance(Base, TimestampMixin):
    __tablename__ = "maintenance_records"

    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
    )

    vehicle_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("vehicles.id", ondelete="CASCADE"),
        nullable=False,
    )

    maintenance_type: Mapped[MaintenanceType] = mapped_column(
        SQLEnum(
            MaintenanceType,
            name="maintenance_type_enum",
        ),
        nullable=False,
    )

    status: Mapped[MaintenanceStatus] = mapped_column(
        SQLEnum(
            MaintenanceStatus,
            name="maintenance_status_enum",
        ),
        default=MaintenanceStatus.SCHEDULED,
        nullable=False,
    )

    service_date: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )

    next_service_date: Mapped[DateTime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    mileage: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    cost: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    service_center: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    technician: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    notes: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    vehicle = relationship(
        "Vehicle",
        back_populates="maintenance_records",
    )
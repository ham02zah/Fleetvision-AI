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
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base import Base
from app.database.mixins import TimestampMixin


class TripStatus(str, Enum):
    PLANNED = "planned"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class Trip(Base, TimestampMixin):
    __tablename__ = "trips"

    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
    )

    fleet_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("fleets.id", ondelete="CASCADE"),
        nullable=False,
    )

    vehicle_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("vehicles.id", ondelete="CASCADE"),
        nullable=False,
    )

    driver_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey("drivers.id", ondelete="CASCADE"),
        nullable=False,
    )

    origin: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    destination: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    departure_time: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )

    arrival_time: Mapped[DateTime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    distance_km: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    average_speed: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    fuel_used_liters: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    notes: Mapped[str | None] = mapped_column(
        Text,
        nullable=True,
    )

    status: Mapped[TripStatus] = mapped_column(
        SQLEnum(
            TripStatus,
            name="trip_status_enum",
        ),
        default=TripStatus.PLANNED,
        nullable=False,
    )

    fleet = relationship(
        "Fleet",
        back_populates="trips",
    )

    vehicle = relationship(
        "Vehicle",
        back_populates="trips",
    )

    driver = relationship(
        "Driver",
        back_populates="trips",
    )
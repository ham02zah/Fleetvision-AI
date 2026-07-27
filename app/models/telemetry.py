from datetime import datetime, timezone
from enum import Enum
from uuid import UUID, uuid4

from sqlalchemy import (
    Boolean,
    DateTime,
    Enum as SQLEnum,
    Float,
    ForeignKey,
)
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from app.database.base import Base


class VehicleState(str, Enum):
    OFFLINE = "offline"
    IDLE = "idle"
    MOVING = "moving"
    PARKED = "parked"


class Telemetry(Base):
    __tablename__ = "telemetry"

    id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
    )

    vehicle_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("vehicles.id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )

    latitude: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    longitude: Mapped[float] = mapped_column(
        Float,
        nullable=False,
    )

    speed: Mapped[float] = mapped_column(
        Float,
        default=0,
    )

    heading: Mapped[float] = mapped_column(
        Float,
        default=0,
    )

    ignition: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )

    engine_running: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )

    fuel: Mapped[float] = mapped_column(
        Float,
        default=100,
    )

    engine_temp: Mapped[float] = mapped_column(
        Float,
        default=85,
    )

    odometer: Mapped[float] = mapped_column(
        Float,
        default=0,
    )

    state: Mapped[VehicleState] = mapped_column(
        SQLEnum(
            VehicleState,
            name="telemetry_state_enum",
        ),
        default=VehicleState.MOVING,
    )

    recorded_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
    )

    vehicle = relationship(
        "Vehicle",
        back_populates="telemetry_records",
    )
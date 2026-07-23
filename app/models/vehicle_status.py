from enum import Enum
from uuid import uuid4

from sqlalchemy import (
    Boolean,
    DateTime,
    Enum as SQLEnum,
    Float,
    ForeignKey,
)

from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from app.database.base import Base
from app.database.mixins import TimestampMixin


class VehicleState(str, Enum):
    OFFLINE = "offline"
    IDLE = "idle"
    MOVING = "moving"
    PARKED = "parked"


class VehicleStatus(Base, TimestampMixin):
    __tablename__ = "vehicle_status"

    id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid4,
    )

    vehicle_id: Mapped[UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey(
            "vehicles.id",
            ondelete="CASCADE",
        ),
        unique=True,
        nullable=False,
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
        default=False,
    )

    engine_running: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    state: Mapped[VehicleState] = mapped_column(
        SQLEnum(
            VehicleState,
            name="vehicle_state_enum",
        ),
        default=VehicleState.OFFLINE,
    )

    last_seen: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )

    vehicle = relationship(
        "Vehicle",
        back_populates="status",
    )
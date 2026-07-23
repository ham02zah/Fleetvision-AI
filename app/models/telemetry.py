from uuid import uuid4

from sqlalchemy import (
    Float,
    DateTime,
    ForeignKey,
    Boolean,
)

from sqlalchemy.dialects.postgresql import UUID

from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from app.database.base import Base
from app.database.mixins import TimestampMixin


class Telemetry(Base, TimestampMixin):
    __tablename__ = "telemetry"

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
        nullable=False,
    )

    engine_temperature: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    fuel_level: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    battery_voltage: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    rpm: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    odometer: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    harsh_braking: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    harsh_acceleration: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
    )

    ignition_on: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
    )

    recorded_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
    )

    vehicle = relationship(
        "Vehicle",
        back_populates="telemetry_records",
    )
from __future__ import annotations

from uuid import UUID

from sqlalchemy import (
    Boolean,
    ForeignKey,
    Integer,
    String,
)
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base_model import BaseModel


class Vehicle(BaseModel):
    """
    Vehicle model.
    """

    __tablename__ = "vehicles"

    fleet_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("fleets.id", ondelete="CASCADE"),
        nullable=False,
    )

    registration_number: Mapped[str] = mapped_column(
        String(30),
        unique=True,
        nullable=False,
    )

    vin: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        nullable=False,
    )

    make: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    model: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )

    year: Mapped[int] = mapped_column(
    Integer,
    nullable=False,
    )

    color: Mapped[str | None] = mapped_column(
        String(50),
        nullable=True,
    )

    fuel_type: Mapped[str | None] = mapped_column(
        String(30),
        nullable=True,
    )

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    fleet = relationship(
        "Fleet",
        back_populates="vehicles",
    )
from __future__ import annotations

from datetime import date
from uuid import UUID

from sqlalchemy import Boolean, Date, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID as PG_UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database.base_model import BaseModel


class Driver(BaseModel):
    """
    Driver model.
    """

    __tablename__ = "drivers"

    fleet_id: Mapped[UUID] = mapped_column(
        PG_UUID(as_uuid=True),
        ForeignKey("fleets.id", ondelete="CASCADE"),
        nullable=False,
    )

    full_name: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        nullable=False,
    )

    phone: Mapped[str] = mapped_column(
        String(30),
        nullable=False,
    )

    license_number: Mapped[str] = mapped_column(
        String(100),
        unique=True,
        nullable=False,
    )

    license_expiry: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    hire_date: Mapped[date] = mapped_column(
        Date,
        nullable=False,
    )

    emergency_contact: Mapped[str | None] = mapped_column(
        String(150),
        nullable=True,
    )

    emergency_phone: Mapped[str | None] = mapped_column(
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
        back_populates="drivers",
    )

    trips = relationship(
    "Trip",
    back_populates="driver",
    cascade="all, delete-orphan",
    )
from __future__ import annotations

from sqlalchemy import Boolean
from sqlalchemy import Index
from sqlalchemy import String
from sqlalchemy.orm import (
    Mapped,
    mapped_column,
    relationship,
)

from app.database.base_model import BaseModel


class Fleet(BaseModel):
    """
    Fleet owned by a company.

    A fleet contains multiple vehicles and drivers.
    """

    __tablename__ = "fleets"

    __table_args__ = (
        Index("ix_fleets_company_name", "company_name"),
    )

    # =====================================================
    # Fleet Information
    # =====================================================

    name: Mapped[str] = mapped_column(
        String(120),
        unique=True,
        nullable=False,
        index=True,
    )

    description: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    # =====================================================
    # Company Information
    # =====================================================

    company_name: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    contact_email: Mapped[str | None] = mapped_column(
        String(255),
        nullable=True,
    )

    contact_phone: Mapped[str | None] = mapped_column(
        String(30),
        nullable=True,
    )

    address: Mapped[str | None] = mapped_column(
    String(255),
    nullable=True,
    )


    # =====================================================
    # Status
    # =====================================================

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )

    

    # =====================================================
    # String Representation
    # =====================================================

    def __repr__(self) -> str:
        return (
            f"Fleet("
            f"id={self.id}, "
            f"name='{self.name}', "
            f"company='{self.company_name}'"
            f")"
        )
    
    country: Mapped[str] = mapped_column(
    String(80),
    nullable=False,
    )

    city: Mapped[str] = mapped_column(
        String(80),
        nullable=False,
    )

    timezone: Mapped[str] = mapped_column(
        String(50),
        default="UTC",
        nullable=False,
    )

    vehicles = relationship(
        "Vehicle",
        back_populates="fleet",
        cascade="all, delete-orphan",
    )
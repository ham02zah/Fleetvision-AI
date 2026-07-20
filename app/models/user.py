from __future__ import annotations

from datetime import datetime
from enum import Enum

from sqlalchemy import Boolean
from sqlalchemy import DateTime
from sqlalchemy import Enum as SQLAlchemyEnum
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.database.base_model import BaseModel


class UserRole(str, Enum):
    """
    Available user roles.

    Admin
        Full system access.

    Fleet Manager
        Manages drivers, vehicles,
        maintenance and alerts.

    Driver
        Uses the mobile application.

    Viewer
        Read-only dashboard access.
    """

    ADMIN = "admin"

    FLEET_MANAGER = "fleet_manager"

    DRIVER = "driver"

    VIEWER = "viewer"


class User(BaseModel):
    """
    FleetVision user.
    """

    __tablename__ = "users"

    full_name: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    email: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        index=True,
        nullable=False,
    )

    hashed_password: Mapped[str] = mapped_column(
        String(255),
        nullable=False,
    )

    role: Mapped[UserRole] = mapped_column(
        SQLAlchemyEnum(UserRole),
        default=UserRole.VIEWER,
        nullable=False,
    )

    phone_number: Mapped[str | None] = mapped_column(
        String(25),
        nullable=True,
    )

    profile_image: Mapped[str | None] = mapped_column(
        String(500),
        nullable=True,
    )

    is_verified: Mapped[bool] = mapped_column(
        Boolean,
        default=False,
        nullable=False,
    )

    last_login: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True),
        nullable=True,
    )

    def __repr__(self) -> str:
        return (
            f"User("
            f"id={self.id}, "
            f"email='{self.email}', "
            f"role='{self.role.value}'"
            f")"
        )
    
    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False,
    )    
from __future__ import annotations

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class FleetBase(BaseModel):
    """
    Shared fleet fields.
    """

    name: str = Field(
        ...,
        min_length=2,
        max_length=100,
        examples=["North Region Fleet"],
    )

    company_name: str = Field(
        ...,
        min_length=2,
        max_length=150,
        examples=["FleetVision Logistics"],
    )

    description: str | None = Field(
        default=None,
        max_length=500,
    )

    contact_email: EmailStr

    contact_phone: str | None = Field(
        default=None,
        max_length=25,
    )

    country: str = Field(
    ...,
    min_length=2,
    max_length=80,
    examples=["Pakistan"],
)

    city: str = Field(
    ...,
    min_length=2,
    max_length=80,
    examples=["Islamabad"],
)

    timezone: str = Field(
    default="UTC",
    max_length=50,
    examples=["Asia/Karachi"],
)


class FleetCreate(FleetBase):
    """
    Create fleet request.
    """
    pass


class FleetUpdate(BaseModel):
    """
    Update fleet request.
    """

    name: str | None = Field(default=None, min_length=2, max_length=100)
    company_name: str | None = Field(default=None, min_length=2, max_length=150)
    description: str | None = Field(default=None, max_length=500)
    contact_email: EmailStr | None = None
    contact_phone: str | None = Field(default=None, max_length=25)
    address: str | None = Field(default=None, max_length=255)


class FleetResponse(FleetBase):
    """
    Fleet response model.
    """

    model_config = ConfigDict(from_attributes=True)

    id: UUID
    is_active: bool
    created_at: datetime
    updated_at: datetime

class FleetSummary(BaseModel):
    """
    Lightweight fleet information.
    """

    model_config = ConfigDict(from_attributes=True)

    id: UUID

    name: str

    company_name: str

    is_active: bool

class FleetListResponse(BaseModel):
    """
    Paginated fleet response.
    """

    total: int

    fleets: list[FleetSummary]
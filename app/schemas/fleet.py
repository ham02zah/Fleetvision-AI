from __future__ import annotations

from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class FleetCreate(BaseModel):
    """
    Request for creating a fleet.
    """

    name: str = Field(
        min_length=2,
        max_length=120,
    )

    description: str | None = Field(
        default=None,
        max_length=500,
    )

    company_name: str = Field(
        min_length=2,
        max_length=150,
    )

    contact_email: EmailStr | None = None

    contact_phone: str | None = None

    address: str | None = None

    country: str

    city: str

    timezone: str


class FleetUpdate(BaseModel):
    """
    Request for updating a fleet.
    """

    name: str | None = None

    description: str | None = None

    company_name: str | None = None

    contact_email: EmailStr | None = None

    contact_phone: str | None = None

    address: str | None = None

    country: str | None = None

    city: str | None = None

    timezone: str | None = None

    is_active: bool | None = None


class FleetResponse(BaseModel):
    """
    Fleet returned to clients.
    """

    model_config = ConfigDict(
        from_attributes=True,
    )

    id: UUID

    name: str

    description: str | None

    company_name: str

    contact_email: EmailStr | None

    contact_phone: str | None

    address: str | None

    country: str

    city: str

    timezone: str

    is_active: bool

class FleetListResponse(BaseModel):
    """
    List of fleets returned to clients.
    """

    fleets: list[FleetResponse]

    total: int    

class FleetSummary(BaseModel):
    """
    Lightweight fleet representation.
    """

    model_config = ConfigDict(
        from_attributes=True,
    )

    id: UUID

    name: str

    company_name: str

    city: str

    country: str

    is_active: bool


class FleetListResponse(BaseModel):
    """
    Paginated fleet list.
    """

    total: int

    fleets: list[FleetSummary]    

class FleetListResponse(BaseModel):
    """
    Paginated fleet list.
    """

    total: int

    skip: int

    limit: int

    fleets: list[FleetResponse]    
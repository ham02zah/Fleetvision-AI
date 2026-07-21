from __future__ import annotations

from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field


class VehicleCreate(BaseModel):
    """
    Request for creating a vehicle.
    """

    fleet_id: UUID

    make: str = Field(
        min_length=2,
        max_length=80,
    )

    model: str = Field(
        min_length=1,
        max_length=80,
    )

    year: int = Field(
        ge=1980,
        le=2100,
    )

    registration_number: str = Field(
        min_length=3,
        max_length=30,
    )

    vin: str = Field(
        min_length=17,
        max_length=17,
    )

    fuel_type: str

    color: str | None = None


class VehicleUpdate(BaseModel):
    """
    Request for updating a vehicle.
    """

    make: str | None = None
    model: str | None = None
    year: int | None = None
    registration_number: str | None = None
    vin: str | None = None
    fuel_type: str | None = None
    color: str | None = None
    is_active: bool | None = None


class VehicleResponse(BaseModel):
    """
    Vehicle returned to clients.
    """

    model_config = ConfigDict(
        from_attributes=True,
    )

    id: UUID
    fleet_id: UUID

    make: str
    model: str
    year: int

    registration_number: str
    vin: str

    fuel_type: str
    color: str | None

    is_active: bool


class VehicleSummary(BaseModel):
    """
    Lightweight vehicle response.
    """

    model_config = ConfigDict(
        from_attributes=True,
    )

    id: UUID
    make: str
    model: str
    registration_number: str
    is_active: bool


class VehicleListResponse(BaseModel):
    """
    Vehicle list response.
    """

    total: int
    skip: int
    limit: int

    vehicles: list[VehicleSummary]
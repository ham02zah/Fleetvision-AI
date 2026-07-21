from __future__ import annotations

from datetime import date
from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr, Field


class DriverCreate(BaseModel):
    fleet_id: UUID

    full_name: str = Field(
        min_length=3,
        max_length=150,
    )

    email: EmailStr

    phone: str = Field(
        min_length=7,
        max_length=30,
    )

    license_number: str = Field(
        min_length=3,
        max_length=100,
    )

    license_expiry: date

    hire_date: date

    emergency_contact: str | None = None

    emergency_phone: str | None = None


class DriverUpdate(BaseModel):
    full_name: str | None = None
    email: EmailStr | None = None
    phone: str | None = None
    license_number: str | None = None
    license_expiry: date | None = None
    hire_date: date | None = None
    emergency_contact: str | None = None
    emergency_phone: str | None = None
    is_active: bool | None = None


class DriverResponse(BaseModel):
    model_config = ConfigDict(
        from_attributes=True
    )

    id: UUID
    fleet_id: UUID

    full_name: str
    email: EmailStr
    phone: str

    license_number: str
    license_expiry: date
    hire_date: date

    emergency_contact: str | None
    emergency_phone: str | None

    is_active: bool


class DriverSummary(BaseModel):
    model_config = ConfigDict(
        from_attributes=True
    )

    id: UUID
    full_name: str
    email: EmailStr
    phone: str
    is_active: bool


class DriverListResponse(BaseModel):
    total: int
    skip: int
    limit: int

    drivers: list[DriverSummary]
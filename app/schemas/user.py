from __future__ import annotations

from datetime import datetime
from uuid import UUID

from pydantic import BaseModel
from pydantic import ConfigDict
from pydantic import EmailStr
from pydantic import Field

from app.models.user import UserRole


class UserBase(BaseModel):
    """
    Shared user fields.
    """

    full_name: str = Field(
        ...,
        min_length=2,
        max_length=150,
        examples=["John Doe"],
    )

    email: EmailStr

    phone_number: str | None = Field(
        default=None,
        max_length=25,
        examples=["+923001234567"],
    )

    profile_image: str | None = None


class UserCreate(UserBase):
    """
    Payload for creating a user.
    """

    password: str = Field(
        ...,
        min_length=8,
        max_length=128,
        examples=["StrongPassword123!"],
    )

    role: UserRole = UserRole.VIEWER


class UserUpdate(BaseModel):
    """
    Payload for updating a user.
    All fields are optional.
    """

    full_name: str | None = Field(default=None, min_length=2, max_length=150)

    phone_number: str | None = Field(default=None, max_length=25)

    profile_image: str | None = None

    role: UserRole | None = None

    is_verified: bool | None = None

    is_active: bool | None = None


class UserResponse(UserBase):
    """
    Returned after reading or creating a user.
    """

    model_config = ConfigDict(from_attributes=True)

    id: UUID

    role: UserRole

    is_verified: bool

    is_active: bool

    created_at: datetime

    updated_at: datetime

    last_login: datetime | None = None


class UserPublic(BaseModel):
    """
    Lightweight public profile.
    """

    model_config = ConfigDict(from_attributes=True)

    id: UUID

    full_name: str

    profile_image: str | None = None

    role: UserRole


class UserListResponse(BaseModel):
    """
    Response for paginated user lists.
    """

    total: int

    users: list[UserResponse]
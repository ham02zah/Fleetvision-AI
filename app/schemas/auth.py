from __future__ import annotations

from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr, Field

from app.models.user import UserRole


class LoginRequest(BaseModel):
    """
    User login request.
    """

    email: EmailStr

    password: str = Field(
        min_length=8,
        max_length=128,
    )


class RefreshTokenRequest(BaseModel):
    """
    Refresh access token request.
    """

    refresh_token: str = Field(
        min_length=20,
    )


class TokenResponse(BaseModel):
    """
    Authentication response.
    """

    access_token: str

    refresh_token: str

    token_type: str = "bearer"


class TokenPayload(BaseModel):
    """
    Decoded JWT payload.
    """

    sub: str

    email: EmailStr

    type: str

    role: str | None = None

    exp: int

    iat: int


class RegisterRequest(BaseModel):
    """
    User registration request.
    """

    full_name: str = Field(
        min_length=2,
        max_length=150,
    )

    email: EmailStr

    password: str = Field(
        min_length=8,
        max_length=128,
    )


class UserResponse(BaseModel):
    """
    User response returned to clients.
    """

    model_config = ConfigDict(from_attributes=True)

    id: UUID

    full_name: str

    email: EmailStr

    role: UserRole

    is_active: bool

    is_verified: bool
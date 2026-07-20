from __future__ import annotations

from datetime import UTC, datetime, timedelta
from typing import Any
from uuid import UUID

import jwt
from pwdlib import PasswordHash

from app.core.config import settings

# Configure the password hasher using recommended defaults.
password_hasher = PasswordHash.recommended()


def hash_password(password: str) -> str:
    """
    Hash a plaintext password.
    """
    return password_hasher.hash(password)


def verify_password(password: str, hashed_password: str) -> bool:
    """
    Verify a plaintext password against a stored hash.
    """
    return password_hasher.verify(password, hashed_password)


def create_access_token(
    *,
    user_id: UUID,
    email: str,
    role: str,
) -> str:
    """
    Create a short-lived JWT access token.
    """
    expires_at = datetime.now(UTC) + timedelta(
        minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload: dict[str, Any] = {
        "sub": str(user_id),
        "email": email,
        "role": role,
        "type": "access",
        "exp": expires_at,
        "iat": datetime.now(UTC),
    }

    return jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=settings.JWT_ALGORITHM,
    )


def create_refresh_token(
    *,
    user_id: UUID,
    email: str,
) -> str:
    """
    Create a long-lived JWT refresh token.
    """
    expires_at = datetime.now(UTC) + timedelta(
        days=settings.REFRESH_TOKEN_EXPIRE_DAYS
    )

    payload: dict[str, Any] = {
        "sub": str(user_id),
        "email": email,
        "type": "refresh",
        "exp": expires_at,
        "iat": datetime.now(UTC),
    }

    return jwt.encode(
        payload,
        settings.SECRET_KEY,
        algorithm=settings.JWT_ALGORITHM,
    )


def decode_token(token: str) -> dict[str, Any]:
    """
    Decode and validate a JWT.

    Raises:
        jwt.InvalidTokenError
            If the token is invalid or expired.
    """
    return jwt.decode(
        token,
        settings.SECRET_KEY,
        algorithms=[settings.JWT_ALGORITHM],
    )
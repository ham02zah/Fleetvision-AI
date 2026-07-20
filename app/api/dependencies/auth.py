from __future__ import annotations

from uuid import UUID

import jwt
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session


from app.core.config import settings
from app.core.security import decode_token
from app.database import get_db
from app.models.user import User
from app.repositories.user_repository import UserRepository

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/v1/auth/login"
)


def get_current_user(
    token: str = Depends(oauth2_scheme),
    db: Session = Depends(get_db),
) -> User:
    """
    Return the authenticated user.
    """

    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials.",
        headers={"WWW-Authenticate": "Bearer"},
    )

    try:
        payload = decode_token(token)

        user_id = UUID(payload["sub"])

    except (jwt.InvalidTokenError, KeyError, ValueError):
        raise credentials_exception

    repo = UserRepository(db)

    user = repo.get_by_id(user_id)

    if user is None:
        raise credentials_exception

    if not user.is_active:
        raise HTTPException(
            status_code=403,
            detail="Inactive user.",
        )

    return user

def require_admin(
    current_user: User = Depends(get_current_user),
) -> User:
    if current_user.role.value != "admin":
        raise HTTPException(
            status_code=403,
            detail="Administrator access required.",
        )

    return current_user


def require_manager(
    current_user: User = Depends(get_current_user),
) -> User:
    if current_user.role.value != "fleet_manager":
        raise HTTPException(
            status_code=403,
            detail="Fleet Manager access required.",
        )

    return current_user


def require_driver(
    current_user: User = Depends(get_current_user),
) -> User:
    if current_user.role.value != "driver":
        raise HTTPException(
            status_code=403,
            detail="Driver access required.",
        )

    return current_user
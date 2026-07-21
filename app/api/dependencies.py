from __future__ import annotations

from fastapi import Depends
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/api/v1/auth/login",
)


def get_token(
    token: str = Depends(oauth2_scheme),
) -> str:
    """
    Extract JWT token from Authorization header.
    """
    return token
from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.auth import (
    LoginRequest,
    RegisterRequest,
    TokenResponse,
    UserResponse,
)
from app.services.auth_service import AuthService

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.get("/health")
def auth_health():
    return {
        "module": "authentication",
        "status": "healthy",
    }


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Register a new user",
)
def register(
    payload: RegisterRequest,
    db: Session = Depends(get_db),
):
    service = AuthService(db)

    try:
        user = service.register(payload)
        return user

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(exc),
        )

@router.post(
    "/login",
    response_model=TokenResponse,
    summary="User Login",
)
def login(
    payload: LoginRequest,
    db: Session = Depends(get_db),
):
    service = AuthService(db)

    try:
        return service.authenticate(
            payload.email,
            payload.password,
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(exc),
        )        
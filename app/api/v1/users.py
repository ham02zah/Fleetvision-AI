from __future__ import annotations
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.api.dependencies import (
    get_current_user,
    require_admin,
)
from app.database import get_db
from app.exceptions import (
    UserAlreadyExistsError,
    UserNotFoundError,
)
from app.models.user import User
from app.schemas.user import (
    UserCreate,
    UserListResponse,
    UserResponse,
    UserUpdate,
)
from app.services.user_service import UserService

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)

@router.get(
    "/me",
    response_model=UserResponse,
    summary="Current User",
)
def get_current_profile(
    current_user: User = Depends(get_current_user),
):
    """
    Return the authenticated user's profile.
    """
    return current_user

@router.get(
    "",
    response_model=UserListResponse,
    summary="List Users",
)
def list_users(
    skip: int = Query(
        0,
        ge=0,
    ),
    limit: int = Query(
        20,
        ge=1,
        le=100,
    ),
    _: User = Depends(require_admin),
    db: Session = Depends(get_db),
):
    """
    Return a paginated list of users.

    Admin only.
    """

    service = UserService(db)

    total, users = service.list_users(
        skip=skip,
        limit=limit,
    )

    return UserListResponse(
        total=total,
        users=users,
    )

@router.post(
    "",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
    summary="Create User",
)
def create_user(
    payload: UserCreate,
    _: User = Depends(require_admin),
    db: Session = Depends(get_db),
):
    """
    Create a new user.

    Admin only.
    """

    service = UserService(db)

    try:
        return service.create_user(payload)

    except UserAlreadyExistsError as exc:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(exc),
        )
    
    
@router.get(
    "/{user_id}",
    response_model=UserResponse,
    summary="Get User",
)
def get_user(
    user_id: UUID,
    _: User = Depends(require_admin),
    db: Session = Depends(get_db),
):
    """
    Retrieve a single user by ID.

    Admin only.
    """

    service = UserService(db)

    try:
        return service.get_user(user_id)

    except UserNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        )

@router.patch(
    "/{user_id}",
    response_model=UserResponse,
    summary="Update User",
)
def update_user(
    user_id: UUID,
    payload: UserUpdate,
    _: User = Depends(require_admin),
    db: Session = Depends(get_db),
):
    """
    Update a user.

    Admin only.
    """

    service = UserService(db)

    try:
        return service.update_user(
            user_id,
            payload,
        )

    except UserNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        )

@router.delete(
    "/{user_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete User",
)
def delete_user(
    user_id: UUID,
    _: User = Depends(require_admin),
    db: Session = Depends(get_db),
):
    """
    Delete a user.

    Admin only.
    """

    service = UserService(db)

    try:
        service.delete_user(user_id)

    except UserNotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        )

    return None


    
from __future__ import annotations

from sqlalchemy.orm import Session

from app.core.security import (
    create_access_token,
    create_refresh_token,
    hash_password,
    verify_password,
)
from app.models.user import User, UserRole
from app.repositories.user_repository import UserRepository
from app.schemas.auth import RegisterRequest, TokenResponse


class AuthService:
    """
    Authentication business logic.
    """

    def __init__(self, db: Session):
        self.repository = UserRepository(db)

    def register(self, request: RegisterRequest) -> User:
        """
        Register a new user.
        """

        existing = self.repository.get_by_email(request.email)

        if existing:
            raise ValueError("Email is already registered.")

        user = User(
            full_name=request.full_name,
            email=request.email,
            hashed_password=hash_password(request.password),
            role=UserRole.ADMIN,
            is_active=True,
            is_verified=True,
        )

        return self.repository.create(user)

    def authenticate(
        self,
        email: str,
        password: str,
    ) -> TokenResponse:
        """
        Authenticate a user and issue JWT tokens.
        """

        user = self.repository.get_by_email(email)

        if user is None:
            raise ValueError("Invalid email or password.")

        if not verify_password(
            password,
            user.hashed_password,
        ):
            raise ValueError("Invalid email or password.")

        return TokenResponse(
            access_token=create_access_token(
                user_id=user.id,
                email=user.email,
                role=user.role.value,
            ),
            refresh_token=create_refresh_token(
                user_id=user.id,
                email=user.email,
            ),
        )
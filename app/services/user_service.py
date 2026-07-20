from __future__ import annotations

from uuid import UUID

from app.exceptions import (
    UserAlreadyExistsError,
    UserNotFoundError,
)
from sqlalchemy.orm import Session

from app.core.security import hash_password
from app.models.user import User
from app.repositories.user_repository import UserRepository
from app.schemas.user import UserCreate, UserUpdate


class UserService:
    """
    Business logic for user management.
    """

    def __init__(self, db: Session):
        self.repo = UserRepository(db)

    def create_user(self, payload: UserCreate) -> User:
        """
        Create a new user.
        """

        if self.repo.exists(payload.email):
            raise UserAlreadyExistsError()

        user = User(
            full_name=payload.full_name,
            email=payload.email,
            hashed_password=hash_password(payload.password),
            role=payload.role,
            phone_number=payload.phone_number,
            profile_image=payload.profile_image,
        )

        return self.repo.create(user)

    def get_user(self, user_id: UUID) -> User:
        """
        Retrieve a user by ID.
        """

        user = self.repo.get_by_id(user_id)

        if user is None:
            raise UserNotFoundError()

        return user

    def get_user_by_email(self, email: str) -> User | None:
        """
        Retrieve a user by email.
        """

        return self.repo.get_by_email(email)

    def list_users(
        self,
        skip: int = 0,
        limit: int = 50,
    ) -> tuple[int, list[User]]:
        """
        Return paginated users.
        """

        total = self.repo.count()

        users = self.repo.get_all(
            skip=skip,
            limit=limit,
        )

        return total, users

    def update_user(
        self,
        user_id: UUID,
        payload: UserUpdate,
    ) -> User:
        """
        Update user profile.
        """

        user = self.get_user(user_id)

        update_data = payload.model_dump(exclude_unset=True)

        for field, value in update_data.items():
            setattr(user, field, value)

        return self.repo.update(user)

    def delete_user(
        self,
        user_id: UUID,
    ) -> None:
        """
        Delete a user.
        """

        user = self.get_user(user_id)

        self.repo.delete(user)
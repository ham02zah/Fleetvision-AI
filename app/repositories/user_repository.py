from __future__ import annotations

from uuid import UUID

from sqlalchemy.orm import Session

from app.models.user import User


class UserRepository:
    """
    Repository for User database operations.
    """

    def __init__(self, db: Session):
        self.db = db

    def create(self, user: User) -> User:
        """
        Create a new user.
        """
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_by_id(self, user_id: UUID) -> User | None:
        """
        Get user by primary key.
        """
        return self.db.get(User, user_id)

    def get_by_email(self, email: str) -> User | None:
        """
        Get user by email.
        """
        return (
            self.db.query(User)
            .filter(User.email == email)
            .first()
        )

    def list_users(self) -> list[User]:
        """
        Return all users.
        """
        return (
            self.db.query(User)
            .order_by(User.created_at.desc())
            .all()
        )

    def update(self, user: User) -> User:
        """
        Persist changes to a user.
        """
        self.db.commit()
        self.db.refresh(user)
        return user

    def delete(self, user: User) -> None:
        """
        Delete a user.
        """
        self.db.delete(user)
        self.db.commit()
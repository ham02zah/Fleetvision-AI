from __future__ import annotations

from uuid import UUID

from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.fleet import Fleet


class FleetRepository:
    """
    Repository responsible for Fleet database operations.
    """

    def __init__(self, db: Session):
        self.db = db

    # --------------------------------------------------
    # Create
    # --------------------------------------------------

    def create(
        self,
        fleet: Fleet,
    ) -> Fleet:
        self.db.add(fleet)
        self.db.commit()
        self.db.refresh(fleet)
        return fleet

    # --------------------------------------------------
    # Read
    # --------------------------------------------------

    def get_by_id(
        self,
        fleet_id: UUID,
    ) -> Fleet | None:
        return (
            self.db.query(Fleet)
            .filter(Fleet.id == fleet_id)
            .first()
        )

    def get_by_name(
        self,
        name: str,
    ) -> Fleet | None:
        return (
            self.db.query(Fleet)
            .filter(Fleet.name == name)
            .first()
        )

    def exists(
        self,
        name: str,
    ) -> bool:
        return self.get_by_name(name) is not None

    def get_all(
        self,
        skip: int = 0,
        limit: int = 50,
    ) -> list[Fleet]:
        return (
            self.db.query(Fleet)
            .offset(skip)
            .limit(limit)
            .all()
        )

    def count(self) -> int:
        return (
            self.db.query(func.count(Fleet.id))
            .scalar()
        )

    # --------------------------------------------------
    # Update
    # --------------------------------------------------

    def update(
        self,
        fleet: Fleet,
    ) -> Fleet:
        self.db.commit()
        self.db.refresh(fleet)
        return fleet

    # --------------------------------------------------
    # Delete
    # --------------------------------------------------

    def delete(
        self,
        fleet: Fleet,
    ) -> None:
        self.db.delete(fleet)
        self.db.commit()
from __future__ import annotations

from uuid import UUID

from sqlalchemy import or_
from sqlalchemy.orm import Session

from app.models.fleet import Fleet


class FleetRepository:
    """
    Repository for Fleet database operations.
    """

    def __init__(self, db: Session):
        self.db = db

    def create(self, fleet: Fleet) -> Fleet:
        """
        Create a new fleet.
        """
        self.db.add(fleet)
        self.db.commit()
        self.db.refresh(fleet)
        return fleet

    def get_by_id(
        self,
        fleet_id: UUID,
    ) -> Fleet | None:
        """
        Get a fleet by its ID.
        """
        return self.db.get(
            Fleet,
            fleet_id,
        )

    def get_by_name(
        self,
        name: str,
    ) -> Fleet | None:
        """
        Get a fleet by its name.
        """
        return (
            self.db.query(Fleet)
            .filter(Fleet.name == name)
            .first()
        )

    def list(
        self,
        skip: int = 0,
        limit: int = 50,
        search: str | None = None,
        sort_by: str = "created_at",
        order: str = "desc",
    ) -> list[Fleet]:
        """
        List fleets with optional search and sorting.
        """

        query = self.db.query(Fleet)

        if search:
            query = query.filter(
                or_(
                    Fleet.name.ilike(f"%{search}%"),
                    Fleet.company_name.ilike(f"%{search}%"),
                )
            )

        sort_column = getattr(Fleet, sort_by, Fleet.created_at)

        if order.lower() == "asc":
            query = query.order_by(sort_column.asc())
        else:
            query = query.order_by(sort_column.desc())

        return (
            query.offset(skip)
            .limit(limit)
            .all()
        )

    def count(
        self,
        search: str | None = None,
    ) -> int:
        """
        Count fleets with optional search.
        """
        query = self.db.query(Fleet)

        if search:
            query = query.filter(
                or_(
                    Fleet.name.ilike(f"%{search}%"),
                    Fleet.company_name.ilike(f"%{search}%"),
                )
            )

        return query.count()

    def update(
        self,
        fleet: Fleet,
    ) -> Fleet:
        """
        Update a fleet.
        """
        self.db.commit()
        self.db.refresh(fleet)
        return fleet

    def delete(
        self,
        fleet: Fleet,
    ) -> None:
        """
        Delete a fleet.
        """
        self.db.delete(fleet)
        self.db.commit()
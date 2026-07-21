from __future__ import annotations

from uuid import UUID

from sqlalchemy import or_
from sqlalchemy.orm import Session

from app.models.vehicle import Vehicle


class VehicleRepository:
    """
    Repository for Vehicle database operations.
    """

    def __init__(self, db: Session):
        self.db = db

    def create(
        self,
        vehicle: Vehicle,
    ) -> Vehicle:
        self.db.add(vehicle)
        self.db.commit()
        self.db.refresh(vehicle)
        return vehicle

    def get_by_id(
        self,
        vehicle_id: UUID,
    ) -> Vehicle | None:
        return self.db.get(
            Vehicle,
            vehicle_id,
        )

    def get_by_registration(
        self,
        registration_number: str,
    ) -> Vehicle | None:
        return (
            self.db.query(Vehicle)
            .filter(
                Vehicle.registration_number == registration_number
            )
            .first()
        )

    def get_by_vin(
        self,
        vin: str,
    ) -> Vehicle | None:
        return (
            self.db.query(Vehicle)
            .filter(
                Vehicle.vin == vin
            )
            .first()
        )

    def list(
        self,
        skip: int = 0,
        limit: int = 50,
        search: str | None = None,
        sort_by: str = "created_at",
        order: str = "desc",
    ) -> list[Vehicle]:

        query = self.db.query(Vehicle)

        if search:
            query = query.filter(
                or_(
                    Vehicle.make.ilike(f"%{search}%"),
                    Vehicle.model.ilike(f"%{search}%"),
                    Vehicle.registration_number.ilike(f"%{search}%"),
                )
            )

        sort_column = getattr(
            Vehicle,
            sort_by,
            Vehicle.created_at,
        )

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

        query = self.db.query(Vehicle)

        if search:
            query = query.filter(
                or_(
                    Vehicle.make.ilike(f"%{search}%"),
                    Vehicle.model.ilike(f"%{search}%"),
                    Vehicle.registration_number.ilike(f"%{search}%"),
                )
            )

        return query.count()

    def update(
        self,
        vehicle: Vehicle,
    ) -> Vehicle:
        self.db.commit()
        self.db.refresh(vehicle)
        return vehicle

    def delete(
        self,
        vehicle: Vehicle,
    ) -> None:
        self.db.delete(vehicle)
        self.db.commit()
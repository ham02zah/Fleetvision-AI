from __future__ import annotations

from uuid import UUID

from sqlalchemy.orm import Session

from app.exceptions import (
    FleetAlreadyExistsError,
    FleetNotFoundError,
)
from app.models.fleet import Fleet
from app.repositories.fleet_repository import FleetRepository
from app.schemas.fleet import (
    FleetCreate,
    FleetUpdate,
)


class FleetService:
    """
    Business logic for fleet management.
    """

    def __init__(self, db: Session):
        self.repo = FleetRepository(db)

    # --------------------------------------------------
    # Create Fleet
    # --------------------------------------------------

    def create_fleet(
        self,
        payload: FleetCreate,
    ) -> Fleet:

        if self.repo.exists(payload.name):
            raise FleetAlreadyExistsError()

        fleet = Fleet(
        name=payload.name,
        company_name=payload.company_name,
        description=payload.description,
        contact_email=payload.contact_email,
        contact_phone=payload.contact_phone,
        country=payload.country,
        city=payload.city,
        timezone=payload.timezone,
    )

        return self.repo.create(fleet)

    # --------------------------------------------------
    # Read Fleet
    # --------------------------------------------------

    def get_fleet(
        self,
        fleet_id: UUID,
    ) -> Fleet:

        fleet = self.repo.get_by_id(fleet_id)

        if fleet is None:
            raise FleetNotFoundError()

        return fleet

    def list_fleets(
        self,
        skip: int = 0,
        limit: int = 50,
    ) -> tuple[int, list[Fleet]]:

        total = self.repo.count()

        fleets = self.repo.get_all(
            skip=skip,
            limit=limit,
        )

        return total, fleets

    # --------------------------------------------------
    # Update Fleet
    # --------------------------------------------------

    def update_fleet(
        self,
        fleet_id: UUID,
        payload: FleetUpdate,
    ) -> Fleet:

        fleet = self.get_fleet(fleet_id)

        update_data = payload.model_dump(
            exclude_unset=True
        )

        for field, value in update_data.items():
            setattr(fleet, field, value)

        return self.repo.update(fleet)

    # --------------------------------------------------
    # Delete Fleet
    # --------------------------------------------------

    def delete_fleet(
        self,
        fleet_id: UUID,
    ) -> None:

        fleet = self.get_fleet(fleet_id)

        self.repo.delete(fleet)
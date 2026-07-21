from __future__ import annotations

from uuid import UUID

from app.models.fleet import Fleet
from app.repositories.fleet_repository import FleetRepository
from app.schemas.fleet import FleetCreate, FleetUpdate


class FleetService:
    """
    Fleet business logic.
    """

    def __init__(self, db):
        self.repository = FleetRepository(db)

    def create_fleet(
        self,
        request: FleetCreate,
    ) -> Fleet:
        """
        Create a new fleet.
        """

        existing = self.repository.get_by_name(request.name)

        if existing:
            raise ValueError("A fleet with this name already exists.")

        fleet = Fleet(
            name=request.name,
            description=request.description,
            company_name=request.company_name,
            contact_email=request.contact_email,
            contact_phone=request.contact_phone,
            address=request.address,
            country=request.country,
            city=request.city,
            timezone=request.timezone,
            is_active=True,
        )

        return self.repository.create(fleet)

    def get_fleet(
        self,
        fleet_id: UUID,
    ) -> Fleet:
        """
        Get a fleet by ID.
        """

        fleet = self.repository.get_by_id(fleet_id)

        if fleet is None:
            raise ValueError("Fleet not found.")

        return fleet

    def list_fleets(
        self,
        skip: int = 0,
        limit: int = 50,
        search: str | None = None,
        sort_by: str = "created_at",
        order: str = "desc",
    ):
        """
        List fleets with pagination, search, and sorting.
        """

        total = self.repository.count(search)

        fleets = self.repository.list(
            skip=skip,
            limit=limit,
            search=search,
            sort_by=sort_by,
            order=order,
        )

        return {
            "total": total,
            "skip": skip,
            "limit": limit,
            "fleets": fleets,
        }

    def update_fleet(
        self,
        fleet_id: UUID,
        request: FleetUpdate,
    ) -> Fleet:
        """
        Update an existing fleet.
        """

        fleet = self.get_fleet(fleet_id)

        data = request.model_dump(exclude_unset=True)

        for field, value in data.items():
            setattr(fleet, field, value)

        return self.repository.update(fleet)

    def delete_fleet(
        self,
        fleet_id: UUID,
    ) -> None:
        """
        Delete a fleet.
        """

        fleet = self.get_fleet(fleet_id)

        self.repository.delete(fleet)
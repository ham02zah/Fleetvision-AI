from __future__ import annotations

from uuid import UUID

from app.models.vehicle import Vehicle
from app.repositories.vehicle_repository import VehicleRepository
from app.schemas.vehicle import (
    VehicleCreate,
    VehicleUpdate,
)


class VehicleService:
    """
    Vehicle business logic.
    """

    def __init__(self, db):
        self.repository = VehicleRepository(db)

    def create_vehicle(
        self,
        request: VehicleCreate,
    ) -> Vehicle:
        """
        Create a new vehicle.
        """

        if self.repository.get_by_registration(
            request.registration_number
        ):
            raise ValueError(
                "Vehicle registration number already exists."
            )

        if self.repository.get_by_vin(
            request.vin
        ):
            raise ValueError(
                "Vehicle VIN already exists."
            )

        vehicle = Vehicle(
            fleet_id=request.fleet_id,
            make=request.make,
            model=request.model,
            year=request.year,
            registration_number=request.registration_number,
            vin=request.vin,
            fuel_type=request.fuel_type,
            color=request.color,
            is_active=True,
        )

        return self.repository.create(vehicle)

    def get_vehicle(
        self,
        vehicle_id: UUID,
    ) -> Vehicle:
        """
        Get a vehicle by ID.
        """

        vehicle = self.repository.get_by_id(vehicle_id)

        if vehicle is None:
            raise ValueError("Vehicle not found.")

        return vehicle

    def list_vehicles(
        self,
        skip: int = 0,
        limit: int = 50,
        search: str | None = None,
        sort_by: str = "created_at",
        order: str = "desc",
    ):
        """
        Return paginated vehicle list.
        """

        total = self.repository.count(search)

        vehicles = self.repository.list(
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
            "vehicles": vehicles,
        }

    def update_vehicle(
        self,
        vehicle_id: UUID,
        request: VehicleUpdate,
    ) -> Vehicle:
        """
        Update a vehicle.
        """

        vehicle = self.get_vehicle(vehicle_id)

        data = request.model_dump(
            exclude_unset=True,
        )

        for field, value in data.items():
            setattr(vehicle, field, value)

        return self.repository.update(vehicle)

    def delete_vehicle(
        self,
        vehicle_id: UUID,
    ) -> None:
        """
        Delete a vehicle.
        """

        vehicle = self.get_vehicle(vehicle_id)

        self.repository.delete(vehicle)
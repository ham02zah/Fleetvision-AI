from __future__ import annotations

from uuid import UUID

from app.models.driver import Driver
from app.repositories.driver_repository import DriverRepository
from app.schemas.driver import DriverCreate, DriverUpdate


class DriverService:
    """
    Driver business logic.
    """

    def __init__(self, db):
        self.repository = DriverRepository(db)

    def create_driver(
        self,
        request: DriverCreate,
    ) -> Driver:

        if self.repository.get_by_email(request.email):
            raise ValueError("Driver email already exists.")

        if self.repository.get_by_license(request.license_number):
            raise ValueError("License number already exists.")

        driver = Driver(
            fleet_id=request.fleet_id,
            full_name=request.full_name,
            email=request.email,
            phone=request.phone,
            license_number=request.license_number,
            license_expiry=request.license_expiry,
            hire_date=request.hire_date,
            emergency_contact=request.emergency_contact,
            emergency_phone=request.emergency_phone,
            is_active=True,
        )

        return self.repository.create(driver)

    def get_driver(
        self,
        driver_id: UUID,
    ) -> Driver:

        driver = self.repository.get_by_id(driver_id)

        if driver is None:
            raise ValueError("Driver not found.")

        return driver

    def list_drivers(
        self,
        skip=0,
        limit=50,
        search=None,
        sort_by="created_at",
        order="desc",
    ):

        total = self.repository.count(search)

        drivers = self.repository.list(
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
            "drivers": drivers,
        }

    def update_driver(
        self,
        driver_id: UUID,
        request: DriverUpdate,
    ) -> Driver:

        driver = self.get_driver(driver_id)

        data = request.model_dump(exclude_unset=True)

        for field, value in data.items():
            setattr(driver, field, value)

        return self.repository.update(driver)

    def delete_driver(
        self,
        driver_id: UUID,
    ):

        driver = self.get_driver(driver_id)

        self.repository.delete(driver)
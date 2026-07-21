from __future__ import annotations

from uuid import UUID

from sqlalchemy import or_
from sqlalchemy.orm import Session

from app.models.driver import Driver


class DriverRepository:

    def __init__(self, db: Session):
        self.db = db

    def create(self, driver: Driver) -> Driver:
        self.db.add(driver)
        self.db.commit()
        self.db.refresh(driver)
        return driver

    def get_by_id(self, driver_id: UUID):
        return self.db.get(
            Driver,
            driver_id,
        )

    def get_by_email(self, email: str):
        return (
            self.db.query(Driver)
            .filter(
                Driver.email == email
            )
            .first()
        )

    def get_by_license(
        self,
        license_number: str,
    ):
        return (
            self.db.query(Driver)
            .filter(
                Driver.license_number == license_number
            )
            .first()
        )

    def list(
        self,
        skip=0,
        limit=50,
        search=None,
        sort_by="created_at",
        order="desc",
    ):

        query = self.db.query(Driver)

        if search:
            query = query.filter(
                or_(
                    Driver.full_name.ilike(f"%{search}%"),
                    Driver.email.ilike(f"%{search}%"),
                    Driver.phone.ilike(f"%{search}%"),
                )
            )

        sort_column = getattr(
            Driver,
            sort_by,
            Driver.created_at,
        )

        if order.lower() == "asc":
            query = query.order_by(
                sort_column.asc()
            )
        else:
            query = query.order_by(
                sort_column.desc()
            )

        return (
            query.offset(skip)
            .limit(limit)
            .all()
        )

    def count(self, search=None):

        query = self.db.query(Driver)

        if search:
            query = query.filter(
                or_(
                    Driver.full_name.ilike(f"%{search}%"),
                    Driver.email.ilike(f"%{search}%"),
                    Driver.phone.ilike(f"%{search}%"),
                )
            )

        return query.count()

    def update(
        self,
        driver: Driver,
    ):
        self.db.commit()
        self.db.refresh(driver)
        return driver

    def delete(
        self,
        driver: Driver,
    ):
        self.db.delete(driver)
        self.db.commit()
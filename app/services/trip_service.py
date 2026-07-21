from uuid import UUID

from sqlalchemy import select
from sqlalchemy.orm import Session

from app.models.trip import Trip
from app.schemas.trip import TripCreate, TripUpdate


class TripService:
    def __init__(self, db: Session):
        self.db = db

    def create_trip(self, trip_data: TripCreate) -> Trip:
        trip = Trip(**trip_data.model_dump())

        self.db.add(trip)
        self.db.commit()
        self.db.refresh(trip)

        return trip

    def get_trip(self, trip_id: UUID) -> Trip | None:
        return self.db.get(Trip, trip_id)

    def list_trips(self) -> list[Trip]:
        stmt = select(Trip).order_by(Trip.departure_time.desc())
        return list(self.db.scalars(stmt).all())

    def update_trip(
        self,
        trip_id: UUID,
        trip_data: TripUpdate,
    ) -> Trip | None:

        trip = self.get_trip(trip_id)

        if not trip:
            return None

        updates = trip_data.model_dump(exclude_unset=True)

        for key, value in updates.items():
            setattr(trip, key, value)

        self.db.commit()
        self.db.refresh(trip)

        return trip

    def delete_trip(self, trip_id: UUID) -> bool:
        trip = self.get_trip(trip_id)

        if not trip:
            return False

        self.db.delete(trip)
        self.db.commit()

        return True
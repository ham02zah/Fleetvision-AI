from datetime import datetime, timezone
from uuid import UUID

from sqlalchemy import desc
from sqlalchemy.orm import Session, joinedload

from app.models.vehicle_status import (
    VehicleStatus,
    VehicleState,
)
from app.schemas.vehicle_status import (
    VehicleStatusCreate,
    VehicleStatusUpdate,
)
from app.services.redis_service import RedisService


class VehicleStatusService:
    def __init__(self, db: Session):
        self.db = db
        self.redis_service = RedisService()

    def create_status(self, data: VehicleStatusCreate):
        status = VehicleStatus(**data.model_dump())

        self.db.add(status)
        self.db.commit()
        self.db.refresh(status)

        return status

    def list_statuses(self):
        return self.db.query(VehicleStatus).all()

    def get_status(self, status_id: UUID):
        return (
            self.db.query(VehicleStatus)
            .filter(VehicleStatus.id == status_id)
            .first()
        )

    def update_status(
        self,
        status_id: UUID,
        data: VehicleStatusUpdate,
    ):
        status = self.get_status(status_id)

        if not status:
            return None

        values = data.model_dump(exclude_unset=True)

        for key, value in values.items():
            setattr(status, key, value)

        self.db.commit()
        self.db.refresh(status)

        return status

    def upsert_vehicle_status(
        self,
        payload: dict,
    ):
        """
        Create or update the latest status for a vehicle.
        """

        vehicle_status = (
            self.db.query(VehicleStatus)
            .filter(
                VehicleStatus.vehicle_id == payload["vehicle_id"]
            )
            .first()
        )

        state = (
            VehicleState.MOVING
            if payload["speed"] > 0
            else VehicleState.PARKED
        )

        if vehicle_status:

            vehicle_status.latitude = payload["latitude"]
            vehicle_status.longitude = payload["longitude"]
            vehicle_status.speed = payload["speed"]
            vehicle_status.heading = payload.get("heading", 0)
            vehicle_status.ignition = payload.get("ignition", True)
            vehicle_status.engine_running = payload.get(
                "engine_running",
                True,
            )
            vehicle_status.state = state
            vehicle_status.last_seen = datetime.now(timezone.utc)

        else:

            vehicle_status = VehicleStatus(
                vehicle_id=payload["vehicle_id"],
                latitude=payload["latitude"],
                longitude=payload["longitude"],
                speed=payload["speed"],
                heading=payload.get("heading", 0),
                ignition=payload.get("ignition", True),
                engine_running=payload.get(
                    "engine_running",
                    True,
                ),
                state=state,
                last_seen=datetime.now(timezone.utc),
            )

            self.db.add(vehicle_status)

        self.db.commit()
        self.db.refresh(vehicle_status)

        return vehicle_status

    def delete_status(
        self,
        status_id: UUID,
    ):
        status = self.get_status(status_id)

        if not status:
            return False

        self.db.delete(status)
        self.db.commit()

        return True

    # ==========================================================
    # Phase 3 - Part 5
    # ==========================================================

    def get_all_statuses(self):
        """
        Return every vehicle status ordered by last update.
        """

        return (
            self.db.query(VehicleStatus)
            .options(
                joinedload(VehicleStatus.vehicle)
            )
            .order_by(
                desc(VehicleStatus.last_seen)
            )
            .all()
        )

    def get_status_by_vehicle(
        self,
        vehicle_id: UUID,
    ):
        """
        Return latest status of a specific vehicle.
        """

        return (
            self.db.query(VehicleStatus)
            .filter(
                VehicleStatus.vehicle_id == vehicle_id
            )
            .options(
                joinedload(VehicleStatus.vehicle)
            )
            .first()
        )

    def get_live_statuses(self):
        """
        Return vehicles whose engines are running.
        """

        return (
            self.db.query(VehicleStatus)
            .filter(
                VehicleStatus.engine_running.is_(True)
            )
            .options(
                joinedload(VehicleStatus.vehicle)
            )
            .order_by(
                desc(VehicleStatus.last_seen)
            )
            .all()
        )

    def get_map_locations(self):
        """
            Lightweight endpoint for the live fleet map.
        """

        rows = (
            self.db.query(VehicleStatus)
            .order_by(
            desc(VehicleStatus.last_seen)
        )
        .all()
    )

        return (
            {
                "vehicle_id": str(row.vehicle_id),
                "latitude": row.latitude,
                "longitude": row.longitude,
                "speed": row.speed,
                "heading": row.heading,
                "state": row.state.value,
                "engine_running": row.engine_running,
                "last_seen": row.last_seen,
            }
            for row in rows
        )
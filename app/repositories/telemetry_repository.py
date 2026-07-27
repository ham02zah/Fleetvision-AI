from uuid import UUID

from sqlalchemy.orm import Session

from app.models.telemetry import Telemetry


class TelemetryRepository:
    """
    Database operations for telemetry.
    """

    @staticmethod
    def create(
        db: Session,
        telemetry: Telemetry,
    ) -> Telemetry:

        db.add(telemetry)
        db.commit()
        db.refresh(telemetry)

        return telemetry

    @staticmethod
    def get_latest_by_vehicle(
        db: Session,
        vehicle_id: UUID,
    ) -> Telemetry | None:

        return (
            db.query(Telemetry)
            .filter(
                Telemetry.vehicle_id == vehicle_id
            )
            .order_by(
                Telemetry.recorded_at.desc()
            )
            .first()
        )

    @staticmethod
    def get_recent_by_vehicle(
        db,
        vehicle_id,
        limit: int = 50,
    ):
        return (
            db.query(Telemetry)
            .filter(
                Telemetry.vehicle_id == vehicle_id
            )
            .order_by(
                Telemetry.recorded_at.desc()
            )
            .limit(limit)
            .all()
        )
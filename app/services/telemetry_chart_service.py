from sqlalchemy.orm import Session

from app.models.telemetry import Telemetry


class TelemetryChartService:

    @staticmethod
    def speed_trend(db: Session):

        rows = (
            db.query(Telemetry)
            .order_by(Telemetry.recorded_at)
            .limit(30)
            .all()
        )

        return [
            {
                "time": r.recorded_at,
                "speed": r.speed,
            }
            for r in rows
        ]

    @staticmethod
    def fuel_trend(db: Session):

        rows = (
            db.query(Telemetry)
            .order_by(Telemetry.recorded_at)
            .limit(30)
            .all()
        )

        return [
            {
                "time": r.recorded_at,
                "fuel": r.fuel,
            }
            for r in rows
        ]

    @staticmethod
    def engine_temperature(
        db: Session,
    ):

        rows = (
            db.query(Telemetry)
            .order_by(Telemetry.recorded_at)
            .limit(30)
            .all()
        )

        return [
            {
                "time": r.recorded_at,
                "temperature": r.engine_temp,
            }
            for r in rows
        ]

    @staticmethod
    def vehicle_utilization(
        db: Session,
    ):

        rows = (
            db.query(Telemetry)
            .all()
        )

        moving = len(
            [x for x in rows if x.speed > 0]
        )

        parked = len(rows) - moving

        return {
            "moving": moving,
            "parked": parked,
        }

    @staticmethod
    def risk_distribution(
        db: Session,
    ):

        rows = db.query(Telemetry).all()

        low = 0
        medium = 0
        high = 0

        for row in rows:

            if row.speed < 40:
                low += 1

            elif row.speed < 80:
                medium += 1

            else:
                high += 1

        return {

            "low": low,

            "medium": medium,

            "high": high,

        }
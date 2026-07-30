from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.ai_prediction import AIPrediction
from app.models.vehicle import Vehicle
from app.models.alert import Alert
from app.models.telemetry import Telemetry


class AnalyticsRepository:

    @staticmethod
    def fleet_summary(db: Session):

        total_vehicles = db.query(Vehicle).count()

        active_vehicles = (
            db.query(Vehicle)
            .filter(Vehicle.is_active == True)
            .count()
        )

        total_predictions = (
            db.query(AIPrediction)
            .count()
        )

        average_health = (
            db.query(
                func.avg(
                    AIPrediction.health_score
                )
            ).scalar()
            or 0
        )

        average_driver = (
            db.query(
                func.avg(
                    AIPrediction.driver_score
                )
            ).scalar()
            or 0
        )

        average_speed = (
            db.query(
                func.avg(
                    Telemetry.speed
                )
            ).scalar()
            or 0
        )

        high_risk = (
            db.query(AIPrediction)
            .filter(
                AIPrediction.risk_level == "HIGH"
            )
            .count()
        )

        maintenance = (
            db.query(AIPrediction)
            .filter(
                AIPrediction.maintenance_level != "GOOD"
            )
            .count()
        )

        alerts = db.query(Alert).count()

        return {

            "total_vehicles": total_vehicles,

            "active_vehicles": active_vehicles,

            "total_predictions": total_predictions,

            "average_health_score": round(
                average_health,
                2,
            ),

            "average_driver_score": round(
                average_driver,
                2,
            ),

            "average_speed": round(
                average_speed,
                2,
            ),

            "high_risk_predictions": high_risk,

            "maintenance_required": maintenance,

            "active_alerts": alerts,

        }

    @staticmethod
    def risk_distribution(db: Session):

        return {

            "low": db.query(AIPrediction).filter(
                AIPrediction.risk_level == "LOW"
            ).count(),

            "medium": db.query(AIPrediction).filter(
                AIPrediction.risk_level == "MEDIUM"
            ).count(),

            "high": db.query(AIPrediction).filter(
                AIPrediction.risk_level == "HIGH"
            ).count(),

            "critical": db.query(AIPrediction).filter(
                AIPrediction.risk_level == "CRITICAL"
            ).count(),

        }

    @staticmethod
    def vehicle_health(db: Session):

        return db.query(
            AIPrediction
        ).all()
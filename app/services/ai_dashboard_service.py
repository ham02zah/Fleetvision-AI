from uuid import UUID

from sqlalchemy.orm import Session

from app.models.vehicle import Vehicle
from app.models.telemetry import Telemetry

from app.ai.intelligence.intelligence_service import (
    AIIntelligenceService,
)


class AIDashboardService:

    @staticmethod
    def get_dashboard(
        db: Session,
        vehicle_id: UUID,
    ):

        vehicle = (
            db.query(Vehicle)
            .filter(
                Vehicle.id == vehicle_id
            )
            .first()
        )

        if vehicle is None:

            return {
                "success": False,
                "message": "Vehicle not found",
            }

        latest = (
            db.query(Telemetry)
            .filter(
                Telemetry.vehicle_id == vehicle_id
            )
            .order_by(
                Telemetry.recorded_at.desc()
            )
            .first()
        )

        if latest is None:

            return {
                "success": False,
                "message": "No telemetry found",
            }

        ai = AIIntelligenceService.analyze(
            telemetry=latest,
            previous_speed=max(
                latest.speed - 10,
                0,
            ),
        )

        return {

            "success": True,

            "vehicle": {

                "id": str(vehicle.id),

                "registration": vehicle.registration_number,

                "make": vehicle.make,

                "model": vehicle.model,

                "year": vehicle.year,

            },

            "telemetry": {

                "speed": latest.speed,

                "fuel": latest.fuel,

                "engine_temperature": latest.engine_temp,

                "latitude": latest.latitude,

                "longitude": latest.longitude,

                "recorded_at": latest.recorded_at,

            },

            "speed_prediction":
                ai["speed_prediction"],

            "risk_analysis":
                ai["risk_analysis"],

            "maintenance_prediction":
                ai["maintenance_analysis"],

            "driver_score":
                ai["driver_score"],

            "anomaly_detection":
                ai["advanced_anomaly_analysis"],

            "recommendations":
                ai["recommendations"],

            "overall_decision":
                ai["ai_decision"],

            "vehicle_health":
                ai["vehicle_health"],
        }
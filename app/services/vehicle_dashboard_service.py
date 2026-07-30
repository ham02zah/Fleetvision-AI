from sqlalchemy.orm import Session

from app.models.vehicle import Vehicle
from app.models.telemetry import Telemetry

from app.ai.intelligence.intelligence_service import (
    AIIntelligenceService,
)
from uuid import UUID

class VehicleDashboardService:
    """
    Vehicle Detail Dashboard Service.

    Returns:
    - Vehicle information
    - Latest telemetry
    - AI analysis
    - Location
    - Health
    """

    @staticmethod
    def get_vehicle_details(
        db: Session,
        vehicle_id: UUID,
    ):
        """
        Returns complete dashboard data for one vehicle.
        """

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
                "success": True,
                "vehicle": {
                    "id": vehicle.id,
                    "name": getattr(vehicle, "name", None),
                    "plate_number": getattr(
                        vehicle,
                        "plate_number",
                        None,
                    ),
                    "status": getattr(
                        vehicle,
                        "status",
                        None,
                    ),
                },
                "latest_telemetry": None,
                "ai_analysis": None,
            }

        ai_result = AIIntelligenceService.analyze(
            telemetry=latest,
            previous_speed=max(
                latest.speed - 10,
                0,
            ),
        )

        return {

            "success": True,

            "vehicle": {

                "id": vehicle.id,

                "name": getattr(
                    vehicle,
                    "name",
                    None,
                ),

                "plate_number": getattr(
                    vehicle,
                    "plate_number",
                    None,
                ),

                "status": getattr(
                    vehicle,
                    "status",
                    None,
                ),
            },

            "latest_telemetry": {

                "speed": latest.speed,

                "fuel": latest.fuel,

                "engine_temp": latest.engine_temp,

                "latitude": latest.latitude,

                "longitude": latest.longitude,

                "heading": getattr(
                    latest,
                    "heading",
                    None,
                ),

                "timestamp": latest.recorded_at,
            },

            "location": {

                "latitude": latest.latitude,

                "longitude": latest.longitude,
            },

            "ai_analysis": ai_result,
        }
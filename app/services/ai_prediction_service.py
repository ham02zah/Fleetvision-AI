from sqlalchemy.orm import Session

from app.models.ai_prediction import AIPrediction
from app.repositories.ai_prediction_repository import (
    AIPredictionRepository,
)


class AIPredictionService:

    @staticmethod
    def save(
        db: Session,
        telemetry,
        prediction,
    ):

        ai_prediction = AIPrediction(

            vehicle_id=telemetry.vehicle_id,

            risk_level=prediction["risk_analysis"][
                "risk_level"
            ],

            maintenance_level=prediction[
                "maintenance_analysis"
            ]["maintenance_level"],

            health_score=prediction[
                "vehicle_health"
            ]["health_score"],

            driver_score=prediction[
                "driver_score"
            ]["score"],

            predicted_speed=prediction[
                "speed_prediction"
            ]["predicted_speed"],

            decision=prediction[
                "ai_decision"
            ]["overall_status"],
        )

        return AIPredictionRepository.create(
            db,
            ai_prediction,
        )
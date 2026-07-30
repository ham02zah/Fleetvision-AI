from sqlalchemy.orm import Session

from app.ai.intelligence.intelligence_service import (
    AIIntelligenceService,
)

from app.models.telemetry import Telemetry

from app.repositories.telemetry_repository import (
    TelemetryRepository,
)

from app.schemas.telemetry import (
    TelemetryCreate,
    TelemetryPredictionResponse,
)

from app.services.alert_generation_service import (
    AlertGenerationService,
)

from app.services.ai_prediction_service import (
    AIPredictionService,
)


class TelemetryService:
    """
    Stores telemetry.

    Runs AI.

    Generates alerts.

    Returns AI analysis.
    """

    @staticmethod
    def create(
        db: Session,
        telemetry_data: TelemetryCreate,
    ) -> TelemetryPredictionResponse:

        previous = (
            TelemetryRepository.get_latest_by_vehicle(
                db=db,
                vehicle_id=telemetry_data.vehicle_id,
            )
        )

        previous_speed = (
            previous.speed
            if previous
            else 0.0
        )

        telemetry = Telemetry(
            vehicle_id=telemetry_data.vehicle_id,
            latitude=telemetry_data.latitude,
            longitude=telemetry_data.longitude,
            speed=telemetry_data.speed,
            heading=telemetry_data.heading,
            ignition=telemetry_data.ignition,
            engine_running=telemetry_data.engine_running,
            fuel=telemetry_data.fuel,
            engine_temp=telemetry_data.engine_temp,
            odometer=telemetry_data.odometer,
            state=telemetry_data.state,
        )

        telemetry = TelemetryRepository.create(
            db=db,
            telemetry=telemetry,
        )

        ai_result = AIIntelligenceService.analyze(
            telemetry=telemetry,
            previous_speed=previous_speed,
        )

        alerts = AlertGenerationService.generate(
            db=db,
            vehicle_id=telemetry.vehicle_id,
            telemetry=telemetry,
            ai_result=ai_result,
        )

        ai_result["generated_alerts"] = len(alerts)

        prediction = AIIntelligenceService.analyze(
        telemetry=telemetry,
        previous_speed=previous_speed,
        )

        AIPredictionService.save(
        db=db,
        telemetry=telemetry,
        prediction=prediction,
        )

        return prediction
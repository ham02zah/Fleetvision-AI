from fastapi import APIRouter

from app.schemas.ai import (
    AIAnalysisRequest,
)

from app.ai.intelligence.intelligence_service import (
    AIIntelligenceService,
)

from app.models.telemetry import Telemetry


router = APIRouter(
    prefix="/ai",
    tags=["AI Intelligence"],
)



@router.post("/analyze")
def analyze_vehicle(
    request: AIAnalysisRequest,
):


    telemetry = Telemetry(

        vehicle_id=request.vehicle_id,

        latitude=request.latitude,

        longitude=request.longitude,

        speed=request.speed,

        heading=request.heading,

        ignition=request.ignition,

        engine_running=request.engine_running,

        fuel=request.fuel,

        engine_temp=request.engine_temp,

        odometer=request.odometer,

    )


    result = AIIntelligenceService.analyze(

        telemetry=telemetry,

        previous_speed=request.previous_speed,

    )


    return result
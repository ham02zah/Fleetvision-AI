from fastapi import APIRouter


from app.ai.inference.speed_predictor import (
    predict_speed,
)

from app.ai.inference.risk_detector import (
    detect_speed_risk,
)


from app.ai.intelligence.intelligence_service import (
    AIIntelligenceService,
)


from app.models.telemetry import Telemetry


from app.api.v1.ai.schemas import (
    SpeedPredictionRequest,
    SpeedPredictionResponse,
    AIAnalysisRequest,
)


from app.schemas.ai import (
    RiskDetectionRequest,
)



router = APIRouter(
    prefix="/ai",
    tags=["Artificial Intelligence"],
)





@router.post(
    "/predict-speed",
    response_model=SpeedPredictionResponse,
)
async def predict_vehicle_speed(
    request: SpeedPredictionRequest,
):

    return predict_speed(
        speed=request.speed,
        previous_speed=request.previous_speed,
    )






@router.post(
    "/detect-risk",
)
async def detect_vehicle_risk(
    request: RiskDetectionRequest,
):

    return detect_speed_risk(
        speed=request.speed,
        previous_speed=request.previous_speed,
    )







@router.post(
    "/analyze",
)
async def analyze_vehicle(
    request: AIAnalysisRequest,
):
    """
    Complete AI fleet intelligence analysis.
    """


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
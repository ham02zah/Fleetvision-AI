from fastapi import APIRouter

from app.ai.inference.speed_predictor import predict_speed

from app.api.v1.ai.schemas import (
    SpeedPredictionRequest,
    SpeedPredictionResponse,
)

from app.ai.inference.risk_detector import detect_speed_risk
from app.schemas.ai import RiskDetectionRequest

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
    """
    Predict vehicle speed using the trained ML model.
    """

    return predict_speed(
        speed=request.speed,
        previous_speed=request.previous_speed,
    )

@router.post("/detect-risk")
async def detect_vehicle_risk(
    request: RiskDetectionRequest,
):
    return detect_speed_risk(
        speed=request.speed,
        previous_speed=request.previous_speed,
    )
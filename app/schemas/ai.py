from pydantic import BaseModel


class SpeedPredictionRequest(BaseModel):
    speed: float
    previous_speed: float = 0.0


class RiskDetectionRequest(BaseModel):
    speed: float
    previous_speed: float = 0.0
from pydantic import BaseModel


class SpeedPredictionRequest(BaseModel):
    speed: float
    previous_speed: float = 0.0


class SpeedPredictionResponse(BaseModel):
    current_speed: float
    predicted_speed: float
    speed_difference: float
    overspeed: bool
    risk_level: str
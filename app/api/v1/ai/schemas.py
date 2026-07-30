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



class AIAnalysisRequest(BaseModel):
    """
    Complete telemetry input
    for AI Intelligence Engine.
    """

    vehicle_id: str

    latitude: float

    longitude: float

    speed: float

    heading: float | None = None

    ignition: int

    engine_running: int

    fuel: float

    engine_temp: float

    odometer: float

    previous_speed: float = 0.0
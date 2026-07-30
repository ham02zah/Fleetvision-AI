from pydantic import BaseModel


class SpeedPredictionRequest(BaseModel):
    speed: float
    previous_speed: float = 0.0


class RiskDetectionRequest(BaseModel):
    speed: float
    previous_speed: float = 0.0

from pydantic import BaseModel


class AIAnalysisRequest(BaseModel):

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
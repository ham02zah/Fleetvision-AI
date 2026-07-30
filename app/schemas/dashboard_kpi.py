from datetime import datetime

from pydantic import BaseModel


class DashboardSummaryResponse(BaseModel):

    total_vehicles: int

    active_vehicles: int

    total_predictions: int

    total_alerts: int

    average_health_score: float

    average_driver_score: float

    average_speed: float


class SpeedTrendResponse(BaseModel):

    timestamp: datetime

    speed: float


class HealthTrendResponse(BaseModel):

    timestamp: datetime

    health_score: float


class DriverLeaderboardResponse(BaseModel):

    vehicle_id: str

    driver_score: float

    health_score: float

    risk_level: str


class VehicleRiskResponse(BaseModel):

    vehicle_id: str

    risk_level: str

    health_score: float

    maintenance_level: str

    predicted_speed: float


class DecisionHistoryResponse(BaseModel):

    timestamp: datetime

    decision: str

    risk_level: str

    health_score: float
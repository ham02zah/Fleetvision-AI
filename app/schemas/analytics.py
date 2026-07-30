from pydantic import BaseModel


class FleetSummaryResponse(BaseModel):

    total_vehicles: int

    active_vehicles: int

    total_predictions: int

    average_health_score: float

    average_driver_score: float

    average_speed: float

    high_risk_predictions: int

    maintenance_required: int

    active_alerts: int


class RiskDistributionResponse(BaseModel):

    low: int

    medium: int

    high: int

    critical: int


class VehicleHealthResponse(BaseModel):

    vehicle_id: str

    health_score: float

    driver_score: float

    risk_level: str

    maintenance_level: str

    predicted_speed: float
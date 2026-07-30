from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

from app.models.telemetry import VehicleState


# ==========================================================
# Incoming Telemetry
# ==========================================================

class TelemetryCreate(BaseModel):

    vehicle_id: UUID

    latitude: float = Field(..., ge=-90, le=90)
    longitude: float = Field(..., ge=-180, le=180)

    speed: float
    heading: float = 0

    ignition: bool = True
    engine_running: bool = True

    fuel: float = 100
    engine_temp: float = 85
    odometer: float = 0

    state: VehicleState = VehicleState.MOVING


# ==========================================================
# Stored Telemetry
# ==========================================================

class TelemetryResponse(BaseModel):

    id: UUID
    vehicle_id: UUID

    latitude: float
    longitude: float

    speed: float
    heading: float

    ignition: bool
    engine_running: bool

    fuel: float
    engine_temp: float
    odometer: float

    state: VehicleState

    recorded_at: datetime

    model_config = ConfigDict(from_attributes=True)


# ==========================================================
# Speed Prediction
# ==========================================================

class SpeedPredictionResponse(BaseModel):

    current_speed: float
    predicted_speed: float
    speed_difference: float
    overspeed: bool
    risk_level: str


# ==========================================================
# Risk
# ==========================================================

class RiskAnalysisResponse(BaseModel):

    current_speed: float
    previous_speed: float
    speed_change: float
    acceleration: float
    overspeed: bool
    risk_level: str
    timestamp: str


# ==========================================================
# Maintenance
# ==========================================================

class MaintenanceAnalysisResponse(BaseModel):

    maintenance_score: int
    maintenance_level: str
    service_required: bool
    timestamp: str


# ==========================================================
# Vehicle Health
# ==========================================================

class VehicleHealthResponse(BaseModel):

    health_score: int
    status: str
    issues: list[str]


# ==========================================================
# Driver Behaviour
# ==========================================================

class DriverBehaviorResponse(BaseModel):

    score: int
    grade: str

    # AI returns "behavior"
    behavior: str

    # AI returns "issues"
    issues: list[str]


# ==========================================================
# Basic Anomaly
# ==========================================================

class AnomalyAnalysisResponse(BaseModel):

    anomaly_count: int
    has_anomaly: bool
    anomalies: list[str]


# ==========================================================
# Advanced Anomaly
# ==========================================================

class AdvancedAnomalyResponse(BaseModel):

    has_anomaly: bool
    anomaly_count: int
    anomalies: list[str]


# ==========================================================
# Recommendations
# ==========================================================

class RecommendationResponse(BaseModel):

    recommendations: list[str]


# ==========================================================
# Explainability
# ==========================================================

class ExplainabilityResponse(BaseModel):

    explanations: list[str]


# ==========================================================
# AI Decision
# ==========================================================

class AIDecisionResponse(BaseModel):

    overall_status: str
    priority: str
    action: str
    confidence: float
    reason: list[str]


# ==========================================================
# Feature Engineering
# ==========================================================

class EngineeredFeaturesResponse(BaseModel):

    latitude: float
    longitude: float

    speed: float
    heading: float

    ignition: int
    engine_running: int

    previous_speed: float
    speed_change: float
    acceleration: float

    is_moving: int
    is_speeding: int
    overspeed: int
    ignition_conflict: int


# ==========================================================
# Final Response
# ==========================================================

class TelemetryPredictionResponse(BaseModel):

    speed_prediction: SpeedPredictionResponse

    risk_analysis: RiskAnalysisResponse

    maintenance_analysis: MaintenanceAnalysisResponse

    vehicle_health: VehicleHealthResponse

    driver_score: DriverBehaviorResponse

    anomaly_analysis: AnomalyAnalysisResponse

    advanced_anomaly_analysis: AdvancedAnomalyResponse

    recommendations: RecommendationResponse

    ai_decision: AIDecisionResponse

    explanations: ExplainabilityResponse

    engineered_features: EngineeredFeaturesResponse

    generated_alerts: int
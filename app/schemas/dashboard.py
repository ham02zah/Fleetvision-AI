from pydantic import BaseModel


class FleetOverviewResponse(BaseModel):
    """
    Fleet overview statistics.
    """

    total_vehicles: int

    active_vehicles: int

    inactive_vehicles: int

    moving_vehicles: int

    parked_vehicles: int


class FleetHealthResponse(BaseModel):
    """
    Fleet maintenance statistics.
    """

    healthy: int

    warning: int

    critical: int


class AISummaryResponse(BaseModel):
    """
    AI statistics.
    """

    low_risk: int

    medium_risk: int

    high_risk: int

    overspeed_events: int


class LiveDashboardResponse(BaseModel):
    """
    Dashboard response.
    """

    overview: FleetOverviewResponse

    fleet_health: FleetHealthResponse

    ai_summary: AISummaryResponse
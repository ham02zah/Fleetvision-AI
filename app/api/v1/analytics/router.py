from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db

from app.services.analytics_service import (
    AnalyticsService,
)

from app.schemas.analytics import (
    FleetSummaryResponse,
    RiskDistributionResponse,
    VehicleHealthResponse,
)

router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"],
)


@router.get(
    "/summary",
    response_model=FleetSummaryResponse,
)
def fleet_summary(
    db: Session = Depends(get_db),
):

    return AnalyticsService.fleet_summary(
        db
    )


@router.get(
    "/risk-distribution",
    response_model=RiskDistributionResponse,
)
def risk_distribution(
    db: Session = Depends(get_db),
):

    return AnalyticsService.risk_distribution(
        db
    )


@router.get(
    "/vehicle-health",
    response_model=list[VehicleHealthResponse],
)
def vehicle_health(
    db: Session = Depends(get_db),
):

    return AnalyticsService.vehicle_health(
        db
    )
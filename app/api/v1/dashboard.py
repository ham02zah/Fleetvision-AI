from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db

from app.services.dashboard_service import DashboardService
from app.services.dashboard_analytics_service import (
    DashboardAnalyticsService,
)
from app.services.vehicle_dashboard_service import (
    VehicleDashboardService,
)

from uuid import UUID

from app.services.ai_dashboard_service import (
    AIDashboardService,
)

from app.services.analytics_service import (
    AnalyticsService,
)

router = APIRouter(
    prefix="/dashboard",
    tags=["Dashboard"],
)


@router.get(
    "/overview",
    summary="Fleet Dashboard Overview",
)
def dashboard_overview(
    db: Session = Depends(get_db),
):
    return DashboardService.get_overview(db)


@router.get(
    "/health",
    summary="Dashboard Health",
)
def dashboard_health():
    return {
        "dashboard": "online",
        "status": "healthy",
    }


@router.get(
    "/analytics",
    summary="Fleet Analytics",
)
def analytics(
    db: Session = Depends(get_db),
):
    return DashboardAnalyticsService.fleet_overview(db)


@router.get(
    "/vehicle/{vehicle_id}",
    summary="Vehicle Dashboard",
)
def vehicle_dashboard(
    vehicle_id: UUID,
    db: Session = Depends(get_db),
):
    return VehicleDashboardService.get_vehicle_details(
        db=db,
        vehicle_id=vehicle_id,
    )

@router.get(
    "/ai/{vehicle_id}",
    summary="AI Dashboard",
)
def ai_dashboard(
    vehicle_id: UUID,
    db: Session = Depends(get_db),
):
    return AIDashboardService.get_dashboard(
        db=db,
        vehicle_id=vehicle_id,
    )

@router.get(
    "/charts/speed/{vehicle_id}",
    summary="Speed History",
)
def speed_history(
    vehicle_id: UUID,
    db: Session = Depends(get_db),
):

    return AnalyticsService.speed_history(
        db,
        vehicle_id,
    )

@router.get(
    "/charts/fuel/{vehicle_id}",
    summary="Fuel History",
)
def fuel_history(
    vehicle_id: UUID,
    db: Session = Depends(get_db),
):

    return AnalyticsService.fuel_history(
        db,
        vehicle_id,
    )

@router.get(
    "/charts/temperature/{vehicle_id}",
    summary="Engine Temperature",
)
def engine_temperature(
    vehicle_id: UUID,
    db: Session = Depends(get_db),
):

    return AnalyticsService.engine_temperature_history(
        db,
        vehicle_id,
    )

@router.get(
    "/charts/route/{vehicle_id}",
    summary="GPS Route",
)
def gps_route(
    vehicle_id: UUID,
    db: Session = Depends(get_db),
):

    return AnalyticsService.gps_history(
        db,
        vehicle_id,
    )


# -------------------------
# KPI DASHBOARD
# -------------------------

@router.get(
    "/kpi",
    summary="Fleet KPI Dashboard",
)
def dashboard_kpi(
    db: Session = Depends(get_db),
):
    return AnalyticsService.fleet_summary(db)

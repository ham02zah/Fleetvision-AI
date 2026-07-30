from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db

from app.services.telemetry_chart_service import (
    TelemetryChartService,
)

router = APIRouter(
    prefix="/telemetry",
    tags=["Telemetry Charts"],
)


@router.get("/speed-trend")
def speed_trend(db: Session = Depends(get_db)):
    return TelemetryChartService.speed_trend(db)


@router.get("/fuel-trend")
def fuel_trend(db: Session = Depends(get_db)):
    return TelemetryChartService.fuel_trend(db)


@router.get("/engine-temperature")
def engine_temperature(
    db: Session = Depends(get_db),
):
    return TelemetryChartService.engine_temperature(
        db
    )


@router.get("/vehicle-utilization")
def utilization(
    db: Session = Depends(get_db),
):
    return TelemetryChartService.vehicle_utilization(
        db
    )


@router.get("/risk-distribution")
def risks(
    db: Session = Depends(get_db),
):
    return TelemetryChartService.risk_distribution(
        db
    )
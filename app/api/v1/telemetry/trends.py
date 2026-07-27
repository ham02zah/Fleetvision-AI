from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from uuid import UUID

from app.database.session import get_db
from app.ai.intelligence.trend_service import (
    TrendService,
)

router = APIRouter(
    prefix="/telemetry",
    tags=["Telemetry"],
)


@router.get(
    "/trends/{vehicle_id}"
)
def telemetry_trends(
    vehicle_id: UUID,
    db: Session = Depends(get_db),
):
    return TrendService.analyze_vehicle(
        db,
        vehicle_id,
    )
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.telemetry import (
    TelemetryCreate,
    TelemetryPredictionResponse,
)
from app.services.telemetry_service import TelemetryService

router = APIRouter(
    prefix="/telemetry",
    tags=["Telemetry"],
)


@router.post(
    "",
    response_model=TelemetryPredictionResponse,
)
def create_telemetry(
    telemetry: TelemetryCreate,
    db: Session = Depends(get_db),
):
    """
    Store telemetry and run AI analysis.
    """

    return TelemetryService.create(
        db=db,
        telemetry_data=telemetry,
    )
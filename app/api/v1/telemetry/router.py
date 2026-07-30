from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database.session import get_db

from app.schemas.telemetry import (
    TelemetryCreate,
    TelemetryPredictionResponse,
)

from app.services.telemetry_service import (
    TelemetryService,
)

from app.services.alert_service import (
    AlertService,
)

router = APIRouter(
    prefix="/telemetry",
    tags=["Telemetry"],
)


@router.post(
    "",
    response_model=TelemetryPredictionResponse,
    summary="Create Telemetry",
)
def create_telemetry(
    telemetry: TelemetryCreate,
    db: Session = Depends(get_db),
):
    """
    Store telemetry.

    Run AI prediction.

    Generate alerts automatically.

    Return AI prediction.
    """

    prediction = TelemetryService.create(
        db=db,
        telemetry_data=telemetry,
    )


    return prediction
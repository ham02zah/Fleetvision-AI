from fastapi import APIRouter
from fastapi import Depends

from sqlalchemy.orm import Session

from app.database.session import get_db

from app.services.alert_service import AlertService
from app.services.alert_statistics_service import (
    AlertStatisticsService,
)

router = APIRouter(
    prefix="/alerts",
    tags=["Alerts"],
)


@router.get("")
def get_alerts(
    db: Session = Depends(get_db),
):
    return AlertService.get_all(db)


@router.get("/statistics")
def statistics(
    db: Session = Depends(get_db),
):
    return AlertStatisticsService.get_statistics(db)
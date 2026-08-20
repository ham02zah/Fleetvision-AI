from __future__ import annotations

from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query, status
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.models.alert import (
    AlertSeverity,
    AlertStatus,
    AlertType,
)
from app.schemas.alert import (
    AlertCreate,
    AlertListResponse,
    AlertResponse,
    AlertStatisticsResponse,
    AlertStatusUpdate,
)
from app.services.alert_service import AlertService


router = APIRouter(
    prefix="/alerts",
    tags=["Alerts"],
)


# ==========================================================
# CREATE ALERT
# ==========================================================

@router.post(
    "",
    response_model=AlertResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_alert(
    payload: AlertCreate,
    db: Session = Depends(get_db),
):
    return AlertService.create_alert(
        db=db,
        vehicle_id=payload.vehicle_id,
        title=payload.title,
        description=payload.description,
        alert_type=payload.alert_type,
        severity=payload.severity,
    )


# ==========================================================
# GET ALL ALERTS
# ==========================================================

@router.get(
    "",
    response_model=AlertListResponse,
)
def get_alerts(
    skip: int = Query(
        default=0,
        ge=0,
    ),
    limit: int = Query(
        default=100,
        ge=1,
        le=500,
    ),
    db: Session = Depends(get_db),
):
    alerts = AlertService.get_all_alerts(
        db,
        skip=skip,
        limit=limit,
    )

    return {
        "alerts": alerts,
        "total": len(alerts),
        "skip": skip,
        "limit": limit,
    }


# ==========================================================
# GET ACTIVE ALERTS
# ==========================================================

@router.get(
    "/status/active",
    response_model=list[AlertResponse],
)
def get_active_alerts(
    skip: int = Query(
        default=0,
        ge=0,
    ),
    limit: int = Query(
        default=100,
        ge=1,
        le=500,
    ),
    db: Session = Depends(get_db),
):
    return AlertService.get_active_alerts(
        db,
        skip=skip,
        limit=limit,
    )


# ==========================================================
# GET ACTIVE VEHICLE ALERTS
# ==========================================================

@router.get(
    "/vehicle/{vehicle_id}/active",
    response_model=list[AlertResponse],
)
def get_active_vehicle_alerts(
    vehicle_id: UUID,
    skip: int = Query(
        default=0,
        ge=0,
    ),
    limit: int = Query(
        default=100,
        ge=1,
        le=500,
    ),
    db: Session = Depends(get_db),
):
    return AlertService.get_active_vehicle_alerts(
        db,
        vehicle_id,
        skip=skip,
        limit=limit,
    )


# ==========================================================
# GET VEHICLE ALERTS
# ==========================================================

@router.get(
    "/vehicle/{vehicle_id}",
    response_model=list[AlertResponse],
)
def get_vehicle_alerts(
    vehicle_id: UUID,
    skip: int = Query(
        default=0,
        ge=0,
    ),
    limit: int = Query(
        default=100,
        ge=1,
        le=500,
    ),
    db: Session = Depends(get_db),
):
    return AlertService.get_vehicle_alerts(
        db,
        vehicle_id,
        skip=skip,
        limit=limit,
    )


# ==========================================================
# FILTER BY STATUS
# ==========================================================

@router.get(
    "/filter/status/{alert_status}",
    response_model=list[AlertResponse],
)
def get_alerts_by_status(
    alert_status: AlertStatus,
    skip: int = Query(
        default=0,
        ge=0,
    ),
    limit: int = Query(
        default=100,
        ge=1,
        le=500,
    ),
    db: Session = Depends(get_db),
):
    return AlertService.get_alerts_by_status(
        db,
        alert_status,
        skip=skip,
        limit=limit,
    )


# ==========================================================
# FILTER BY SEVERITY
# ==========================================================

@router.get(
    "/filter/severity/{severity}",
    response_model=list[AlertResponse],
)
def get_alerts_by_severity(
    severity: AlertSeverity,
    skip: int = Query(
        default=0,
        ge=0,
    ),
    limit: int = Query(
        default=100,
        ge=1,
        le=500,
    ),
    db: Session = Depends(get_db),
):
    return AlertService.get_alerts_by_severity(
        db,
        severity,
        skip=skip,
        limit=limit,
    )


# ==========================================================
# FILTER BY TYPE
# ==========================================================

@router.get(
    "/filter/type/{alert_type}",
    response_model=list[AlertResponse],
)
def get_alerts_by_type(
    alert_type: AlertType,
    skip: int = Query(
        default=0,
        ge=0,
    ),
    limit: int = Query(
        default=100,
        ge=1,
        le=500,
    ),
    db: Session = Depends(get_db),
):
    return AlertService.get_alerts_by_type(
        db,
        alert_type,
        skip=skip,
        limit=limit,
    )


# ==========================================================
# STATISTICS
# ==========================================================

@router.get(
    "/statistics",
    response_model=AlertStatisticsResponse,
)
def get_statistics(
    db: Session = Depends(get_db),
):
    return AlertService.dashboard_stats(db)


# ==========================================================
# ACKNOWLEDGE
# ==========================================================

@router.patch(
    "/{alert_id}/acknowledge",
    response_model=AlertResponse,
)
def acknowledge_alert(
    alert_id: UUID,
    db: Session = Depends(get_db),
):
    alert = AlertService.acknowledge_alert(
        db,
        alert_id,
    )

    if alert is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Alert not found",
        )

    return alert


# ==========================================================
# RESOLVE
# ==========================================================

@router.patch(
    "/{alert_id}/resolve",
    response_model=AlertResponse,
)
def resolve_alert(
    alert_id: UUID,
    db: Session = Depends(get_db),
):
    alert = AlertService.resolve_alert(
        db,
        alert_id,
    )

    if alert is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Alert not found",
        )

    return alert


# ==========================================================
# UPDATE STATUS
# ==========================================================

@router.patch(
    "/{alert_id}/status",
    response_model=AlertResponse,
)
def update_alert_status(
    alert_id: UUID,
    payload: AlertStatusUpdate,
    db: Session = Depends(get_db),
):
    alert = AlertService.update_alert_status(
        db,
        alert_id,
        payload.status,
    )

    if alert is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Alert not found",
        )

    return alert


# ==========================================================
# GET ALERT BY ID
# ==========================================================

@router.get(
    "/{alert_id}",
    response_model=AlertResponse,
)
def get_alert(
    alert_id: UUID,
    db: Session = Depends(get_db),
):
    alert = AlertService.get_alert(
        db,
        alert_id,
    )

    if alert is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Alert not found",
        )

    return alert


# ==========================================================
# DELETE
# ==========================================================

@router.delete(
    "/{alert_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_alert(
    alert_id: UUID,
    db: Session = Depends(get_db),
):
    deleted = AlertService.delete_alert(
        db,
        alert_id,
    )

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Alert not found",
        )

    return None
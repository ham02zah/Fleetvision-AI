from __future__ import annotations

from uuid import UUID

from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.fleet import (
    FleetCreate,
    FleetUpdate,
    FleetResponse,
    FleetListResponse,
)
from app.services.fleet_service import FleetService

router = APIRouter(
    prefix="/fleets",
    tags=["Fleet"],
)


@router.post(
    "",
    response_model=FleetResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_fleet(
    payload: FleetCreate,
    db: Session = Depends(get_db),
):
    service = FleetService(db)
    return service.create_fleet(payload)


@router.get(
    "/{fleet_id}",
    response_model=FleetResponse,
)
def get_fleet(
    fleet_id: UUID,
    db: Session = Depends(get_db),
):
    service = FleetService(db)
    return service.get_fleet(fleet_id)


@router.get(
    "",
    response_model=FleetListResponse,
)
def list_fleets(
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=100),
    db: Session = Depends(get_db),
):
    service = FleetService(db)

    total, fleets = service.list_fleets(
        skip=skip,
        limit=limit,
    )

    return FleetListResponse(
        total=total,
        fleets=fleets,
    )


@router.put(
    "/{fleet_id}",
    response_model=FleetResponse,
)
def update_fleet(
    fleet_id: UUID,
    payload: FleetUpdate,
    db: Session = Depends(get_db),
):
    service = FleetService(db)
    return service.update_fleet(
        fleet_id,
        payload,
    )


@router.delete(
    "/{fleet_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_fleet(
    fleet_id: UUID,
    db: Session = Depends(get_db),
):
    service = FleetService(db)
    service.delete_fleet(fleet_id)

   
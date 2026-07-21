from __future__ import annotations

from uuid import UUID

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
    Query,
    status,
)
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.schemas.fleet import (
    FleetCreate,
    FleetListResponse,
    FleetResponse,
    FleetUpdate,
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

    try:
        return service.create_fleet(payload)

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(exc),
        )


@router.get(
    "/{fleet_id}",
    response_model=FleetResponse,
)
def get_fleet(
    fleet_id: UUID,
    db: Session = Depends(get_db),
):
    service = FleetService(db)

    try:
        return service.get_fleet(fleet_id)

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        )


@router.get(
    "",
    response_model=FleetListResponse,
)
def list_fleets(
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=100),
    search: str | None = Query(None),
    sort_by: str = Query("created_at"),
    order: str = Query("desc"),
    db: Session = Depends(get_db),
):
    service = FleetService(db)

    return service.list_fleets(
        skip=skip,
        limit=limit,
        search=search,
        sort_by=sort_by,
        order=order,
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

    try:
        return service.update_fleet(
            fleet_id,
            payload,
        )

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
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

    try:
        service.delete_fleet(fleet_id)

    except ValueError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc),
        )
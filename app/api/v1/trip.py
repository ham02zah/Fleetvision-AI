from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.session import get_db

from app.schemas.trip import (
    TripCreate,
    TripUpdate,
    TripResponse,
    TripListResponse,
)

from app.services.trip_service import TripService

router = APIRouter(
    prefix="/trips",
    tags=["Trips"],
)


@router.post(
    "",
    response_model=TripResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_trip(
    trip: TripCreate,
    db: Session = Depends(get_db),
):
    service = TripService(db)
    return service.create_trip(trip)


@router.get(
    "",
    response_model=TripListResponse,
)
def list_trips(
    db: Session = Depends(get_db),
):
    service = TripService(db)

    return {
        "items": service.list_trips(),
        "total": len(service.list_trips()),
    }


@router.get(
    "/{trip_id}",
    response_model=TripResponse,
)
def get_trip(
    trip_id: UUID,
    db: Session = Depends(get_db),
):
    service = TripService(db)

    trip = service.get_trip(trip_id)

    if not trip:
        raise HTTPException(
            status_code=404,
            detail="Trip not found",
        )

    return trip


@router.put(
    "/{trip_id}",
    response_model=TripResponse,
)
def update_trip(
    trip_id: UUID,
    trip: TripUpdate,
    db: Session = Depends(get_db),
):
    service = TripService(db)

    updated = service.update_trip(
        trip_id,
        trip,
    )

    if not updated:
        raise HTTPException(
            status_code=404,
            detail="Trip not found",
        )

    return updated


@router.delete(
    "/{trip_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_trip(
    trip_id: UUID,
    db: Session = Depends(get_db),
):
    service = TripService(db)

    deleted = service.delete_trip(trip_id)

    if not deleted:
        raise HTTPException(
            status_code=404,
            detail="Trip not found",
        )

    return None
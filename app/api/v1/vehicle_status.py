from uuid import UUID

from fastapi import (
    APIRouter,
    Depends,
    HTTPException,
)
from sqlalchemy.orm import Session

from app.database.session import get_db
from app.services.vehicle_status_service import VehicleStatusService

router = APIRouter(
    prefix="/vehicle-status",
    tags=["Vehicle Status"],
)


@router.get(
    "",
    summary="Get latest status of all vehicles",
)
def get_all_vehicle_status(
    db: Session = Depends(get_db),
):
    service = VehicleStatusService(db)

    return service.get_all_statuses()


@router.get(
    "/live",
    summary="Get all live vehicles",
)
def get_live_vehicle_status(
    db: Session = Depends(get_db),
):
    service = VehicleStatusService(db)

    return service.get_live_statuses()

@router.get(
    "/map",
    summary="Vehicle map locations",
)
def get_vehicle_map(
    db: Session = Depends(get_db),
):
    service = VehicleStatusService(db)

    return service.get_map_locations()

@router.get(
    "/{vehicle_id}",
    summary="Get vehicle status by vehicle ID",
)
def get_vehicle_status(
    vehicle_id: UUID,
    db: Session = Depends(get_db),
):
    service = VehicleStatusService(db)

    vehicle = service.get_status_by_vehicle(vehicle_id)

    if vehicle is None:
        raise HTTPException(
            status_code=404,
            detail="Vehicle status not found",
        )

    return vehicle
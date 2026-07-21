from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.driver import (
    DriverCreate,
    DriverUpdate,
    DriverResponse,
    DriverListResponse,
)
from app.services.driver_service import DriverService

router = APIRouter(
    prefix="/drivers",
    tags=["Drivers"],
)


@router.post(
    "",
    response_model=DriverResponse,
)
def create_driver(
    payload: DriverCreate,
    db: Session = Depends(get_db),
):

    service = DriverService(db)

    try:
        return service.create_driver(payload)

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e),
        )


@router.get(
    "",
    response_model=DriverListResponse,
)
def list_drivers(
    skip: int = 0,
    limit: int = 50,
    search: str | None = None,
    sort_by: str = "created_at",
    order: str = "desc",
    db: Session = Depends(get_db),
):

    service = DriverService(db)

    return service.list_drivers(
        skip,
        limit,
        search,
        sort_by,
        order,
    )


@router.get(
    "/{driver_id}",
    response_model=DriverResponse,
)
def get_driver(
    driver_id: UUID,
    db: Session = Depends(get_db),
):

    service = DriverService(db)

    try:
        return service.get_driver(driver_id)

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e),
        )


@router.put(
    "/{driver_id}",
    response_model=DriverResponse,
)
def update_driver(
    driver_id: UUID,
    payload: DriverUpdate,
    db: Session = Depends(get_db),
):

    service = DriverService(db)

    try:
        return service.update_driver(
            driver_id,
            payload,
        )

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e),
        )


@router.delete(
    "/{driver_id}",
)
def delete_driver(
    driver_id: UUID,
    db: Session = Depends(get_db),
):

    service = DriverService(db)

    try:
        service.delete_driver(driver_id)

        return {
            "message": "Driver deleted successfully."
        }

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e),
        )
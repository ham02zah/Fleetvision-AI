from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database.session import get_db

from app.schemas.maintenance import (
    MaintenanceCreate,
    MaintenanceUpdate,
    MaintenanceResponse,
    MaintenanceListResponse,
)

from app.services.maintenance_service import MaintenanceService

router = APIRouter(
    prefix="/maintenance",
    tags=["Maintenance"],
)


@router.post(
    "",
    response_model=MaintenanceResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_maintenance(
    maintenance: MaintenanceCreate,
    db: Session = Depends(get_db),
):
    service = MaintenanceService(db)

    return service.create_maintenance(maintenance)


@router.get(
    "",
    response_model=MaintenanceListResponse,
)
def list_maintenance(
    db: Session = Depends(get_db),
):
    service = MaintenanceService(db)

    items = service.list_maintenance()

    return {
        "items": items,
        "total": len(items),
    }


@router.get(
    "/{maintenance_id}",
    response_model=MaintenanceResponse,
)
def get_maintenance(
    maintenance_id: UUID,
    db: Session = Depends(get_db),
):
    service = MaintenanceService(db)

    maintenance = service.get_maintenance(
        maintenance_id,
    )

    if not maintenance:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Maintenance record not found",
        )

    return maintenance


@router.put(
    "/{maintenance_id}",
    response_model=MaintenanceResponse,
)
def update_maintenance(
    maintenance_id: UUID,
    maintenance: MaintenanceUpdate,
    db: Session = Depends(get_db),
):
    service = MaintenanceService(db)

    updated = service.update_maintenance(
        maintenance_id,
        maintenance,
    )

    if not updated:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Maintenance record not found",
        )

    return updated


@router.delete(
    "/{maintenance_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_maintenance(
    maintenance_id: UUID,
    db: Session = Depends(get_db),
):
    service = MaintenanceService(db)

    deleted = service.delete_maintenance(
        maintenance_id,
    )

    if not deleted:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Maintenance record not found",
        )

    return None
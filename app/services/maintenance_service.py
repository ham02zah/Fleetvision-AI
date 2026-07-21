from uuid import UUID

from sqlalchemy.orm import Session

from app.models.maintenance import Maintenance
from app.schemas.maintenance import (
    MaintenanceCreate,
    MaintenanceUpdate,
)


class MaintenanceService:
    def __init__(self, db: Session):
        self.db = db

    def create_maintenance(
        self,
        maintenance: MaintenanceCreate,
    ) -> Maintenance:

        db_maintenance = Maintenance(
            **maintenance.model_dump()
        )

        self.db.add(db_maintenance)
        self.db.commit()
        self.db.refresh(db_maintenance)

        return db_maintenance

    def list_maintenance(self) -> list[Maintenance]:

        return (
            self.db.query(Maintenance)
            .all()
        )

    def get_maintenance(
        self,
        maintenance_id: UUID,
    ) -> Maintenance | None:

        return (
            self.db.query(Maintenance)
            .filter(
                Maintenance.id == maintenance_id
            )
            .first()
        )

    def update_maintenance(
        self,
        maintenance_id: UUID,
        maintenance: MaintenanceUpdate,
    ) -> Maintenance | None:

        db_maintenance = self.get_maintenance(
            maintenance_id
        )

        if not db_maintenance:
            return None

        update_data = maintenance.model_dump(
            exclude_unset=True
        )

        for key, value in update_data.items():
            setattr(
                db_maintenance,
                key,
                value,
            )

        self.db.commit()
        self.db.refresh(db_maintenance)

        return db_maintenance

    def delete_maintenance(
        self,
        maintenance_id: UUID,
    ) -> bool:

        db_maintenance = self.get_maintenance(
            maintenance_id
        )

        if not db_maintenance:
            return False

        self.db.delete(db_maintenance)
        self.db.commit()

        return True
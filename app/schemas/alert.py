from datetime import datetime
from uuid import UUID

from pydantic import BaseModel


class AlertResponse(BaseModel):
    id: UUID

    vehicle_id: UUID

    title: str

    description: str

    severity: str

    is_read: bool

    created_at: datetime

    class Config:
        from_attributes = True
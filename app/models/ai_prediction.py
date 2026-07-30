import uuid

from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.database.base_model import BaseModel


class AIPrediction(BaseModel):
    """
    Stores every AI prediction generated from telemetry.
    """

    __tablename__ = "ai_predictions"

    vehicle_id: Mapped[uuid.UUID] = mapped_column(
        UUID(as_uuid=True),
        ForeignKey(
            "vehicles.id",
            ondelete="CASCADE",
        ),
        nullable=False,
    )

    risk_level: Mapped[str] = mapped_column(
        String(30),
    )

    maintenance_level: Mapped[str] = mapped_column(
        String(30),
    )

    health_score: Mapped[float] = mapped_column(
        Float,
    )

    driver_score: Mapped[float] = mapped_column(
        Float,
    )

    predicted_speed: Mapped[float] = mapped_column(
        Float,
    )

    decision: Mapped[str] = mapped_column(
        String(50),
    )
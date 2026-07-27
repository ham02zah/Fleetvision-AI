from sqlalchemy.orm import Session

from app.ai.intelligence.history_analyzer import (
    HistoryAnalyzer,
)
from app.repositories.telemetry_repository import (
    TelemetryRepository,
)


class TrendService:
    """
    Historical telemetry intelligence.
    """

    @staticmethod
    def analyze_vehicle(
        db: Session,
        vehicle_id,
    ):
        records = (
            TelemetryRepository
            .get_recent_by_vehicle(
                db,
                vehicle_id,
                limit=50,
            )
        )

        return HistoryAnalyzer.analyze(
            records
        )
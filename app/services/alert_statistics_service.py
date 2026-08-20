from __future__ import annotations

from sqlalchemy.orm import Session

from app.repositories.alert_repository import AlertRepository


class AlertStatisticsService:
    """
    Provides alert statistics for dashboards and analytics.

    Business logic related to alert statistics belongs here.
    Database access remains inside AlertRepository.
    """

    @staticmethod
    def get_dashboard_statistics(
        db: Session,
    ) -> dict[str, int]:
        """
        Return aggregated alert statistics for the dashboard.
        """

        return AlertRepository.dashboard_stats(db)
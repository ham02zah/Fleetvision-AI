from uuid import UUID

from sqlalchemy.orm import Session

from app.models.alert import (
    Alert,
    AlertSeverity,
    AlertStatus,
)
from app.repositories.alert_repository import AlertRepository


class AlertDashboardService:
    """
    Dashboard service for alert-related information.

    This service is responsible for preparing alert data
    for dashboard consumers.

    Database operations remain inside AlertRepository.
    """

    # ======================================================
    # ALL ALERTS
    # ======================================================

    @staticmethod
    def get_all_alerts(
        db: Session,
        *,
        skip: int = 0,
        limit: int = 100,
    ) -> dict:

        alerts = AlertRepository.get_all(
            db,
            skip=skip,
            limit=limit,
        )

        return {
            "count": len(alerts),
            "alerts": alerts,
        }

    # ======================================================
    # ACTIVE ALERTS
    # ======================================================

    @staticmethod
    def get_active_alerts(
        db: Session,
        *,
        skip: int = 0,
        limit: int = 100,
    ) -> dict:

        alerts = AlertRepository.get_active(
            db,
            skip=skip,
            limit=limit,
        )

        return {
            "count": len(alerts),
            "alerts": alerts,
        }

    # ======================================================
    # RESOLVED ALERTS
    # ======================================================

    @staticmethod
    def get_resolved_alerts(
        db: Session,
        *,
        skip: int = 0,
        limit: int = 100,
    ) -> dict:

        alerts = AlertRepository.get_by_status(
            db,
            AlertStatus.RESOLVED,
            skip=skip,
            limit=limit,
        )

        return {
            "count": len(alerts),
            "alerts": alerts,
        }

    # ======================================================
    # ACKNOWLEDGED ALERTS
    # ======================================================

    @staticmethod
    def get_acknowledged_alerts(
        db: Session,
        *,
        skip: int = 0,
        limit: int = 100,
    ) -> dict:

        alerts = AlertRepository.get_by_status(
            db,
            AlertStatus.ACKNOWLEDGED,
            skip=skip,
            limit=limit,
        )

        return {
            "count": len(alerts),
            "alerts": alerts,
        }

    # ======================================================
    # CRITICAL ALERTS
    # ======================================================

    @staticmethod
    def get_critical_alerts(
        db: Session,
        *,
        skip: int = 0,
        limit: int = 100,
    ) -> dict:

        alerts = AlertRepository.get_by_severity(
            db,
            AlertSeverity.CRITICAL,
            skip=skip,
            limit=limit,
        )

        return {
            "count": len(alerts),
            "alerts": alerts,
        }

    # ======================================================
    # VEHICLE ALERTS
    # ======================================================

    @staticmethod
    def get_vehicle_alerts(
        db: Session,
        vehicle_id: UUID,
        *,
        skip: int = 0,
        limit: int = 100,
    ) -> dict:

        alerts = AlertRepository.get_by_vehicle(
            db,
            vehicle_id,
            skip=skip,
            limit=limit,
        )

        return {
            "count": len(alerts),
            "alerts": alerts,
        }

    # ======================================================
    # VEHICLE ACTIVE ALERTS
    # ======================================================

    @staticmethod
    def get_vehicle_active_alerts(
        db: Session,
        vehicle_id: UUID,
        *,
        skip: int = 0,
        limit: int = 100,
    ) -> dict:

        alerts = AlertRepository.get_active_by_vehicle(
            db,
            vehicle_id,
            skip=skip,
            limit=limit,
        )

        return {
            "count": len(alerts),
            "alerts": alerts,
        }

    # ======================================================
    # STATISTICS
    # ======================================================

    @staticmethod
    def statistics(
        db: Session,
    ) -> dict[str, int]:

        return AlertRepository.dashboard_stats(db)


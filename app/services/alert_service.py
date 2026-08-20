from __future__ import annotations

from typing import Sequence
from uuid import UUID

from sqlalchemy.orm import Session

from app.models.alert import (
    Alert,
    AlertSeverity,
    AlertStatus,
    AlertType,
)
from app.repositories.alert_repository import AlertRepository

from app.services.alert_statistics_service import (
    AlertStatisticsService,
)

class AlertService:
    """
    Business logic layer for FleetVision alerts.

    The service delegates database operations to
    AlertRepository and provides application-level
    alert operations.
    """

    # ======================================================
    # CREATE
    # ======================================================

    @staticmethod
    def create_alert(
        db: Session,
        *,
        vehicle_id: UUID,
        title: str,
        description: str,
        alert_type: AlertType,
        severity: AlertSeverity,
    ) -> Alert:

        return AlertRepository.create(
            db=db,
            vehicle_id=vehicle_id,
            title=title,
            description=description,
            alert_type=alert_type,
            severity=severity,
        )

    # ======================================================
    # GET ALL
    # ======================================================

    @staticmethod
    def get_all_alerts(
        db: Session,
        *,
        skip: int = 0,
        limit: int = 100,
    ) -> Sequence[Alert]:

        return AlertRepository.get_all(
            db,
            skip=skip,
            limit=limit,
        )

    # ======================================================
    # GET ALERT
    # ======================================================

    @staticmethod
    def get_alert(
        db: Session,
        alert_id: UUID,
    ) -> Alert | None:

        return AlertRepository.get_by_id(
            db,
            alert_id,
        )

    # ======================================================
    # GET VEHICLE ALERTS
    # ======================================================

    @staticmethod
    def get_vehicle_alerts(
        db: Session,
        vehicle_id: UUID,
        *,
        skip: int = 0,
        limit: int = 100,
    ) -> Sequence[Alert]:

        return AlertRepository.get_by_vehicle(
            db,
            vehicle_id,
            skip=skip,
            limit=limit,
        )

    # ======================================================
    # GET ACTIVE ALERTS
    # ======================================================

    @staticmethod
    def get_active_alerts(
        db: Session,
        *,
        skip: int = 0,
        limit: int = 100,
    ) -> Sequence[Alert]:

        return AlertRepository.get_active(
            db,
            skip=skip,
            limit=limit,
        )

    # ======================================================
    # GET ACTIVE VEHICLE ALERTS
    # ======================================================

    @staticmethod
    def get_active_vehicle_alerts(
        db: Session,
        vehicle_id: UUID,
        *,
        skip: int = 0,
        limit: int = 100,
    ) -> Sequence[Alert]:

        return AlertRepository.get_active_by_vehicle(
            db,
            vehicle_id,
            skip=skip,
            limit=limit,
        )


    # ======================================================
    # GET ACTIVE ALERT BY VEHICLE + TYPE
    # ======================================================

    @staticmethod
    def get_active_alert_by_vehicle_and_type(
        db: Session,
        vehicle_id: UUID,
        alert_type: AlertType,
    ) -> Alert | None:

        return AlertRepository.get_active_by_vehicle_and_type(
            db,
            vehicle_id,
            alert_type,
        )
    
    # ======================================================
    # FILTER BY STATUS
    # ======================================================

    @staticmethod
    def get_alerts_by_status(
        db: Session,
        status: AlertStatus,
        *,
        skip: int = 0,
        limit: int = 100,
    ) -> Sequence[Alert]:

        return AlertRepository.get_by_status(
            db,
            status,
            skip=skip,
            limit=limit,
        )

    # ======================================================
    # FILTER BY SEVERITY
    # ======================================================

    @staticmethod
    def get_alerts_by_severity(
        db: Session,
        severity: AlertSeverity,
        *,
        skip: int = 0,
        limit: int = 100,
    ) -> Sequence[Alert]:

        return AlertRepository.get_by_severity(
            db,
            severity,
            skip=skip,
            limit=limit,
        )

    # ======================================================
    # FILTER BY TYPE
    # ======================================================

    @staticmethod
    def get_alerts_by_type(
        db: Session,
        alert_type: AlertType,
        *,
        skip: int = 0,
        limit: int = 100,
    ) -> Sequence[Alert]:

        return AlertRepository.get_by_type(
            db,
            alert_type,
            skip=skip,
            limit=limit,
        )

    # ======================================================
    # ACKNOWLEDGE
    # ======================================================

    @staticmethod
    def acknowledge_alert(
        db: Session,
        alert_id: UUID,
    ) -> Alert | None:

        return AlertRepository.acknowledge(
            db,
            alert_id,
        )

    # ======================================================
    # RESOLVE
    # ======================================================

    @staticmethod
    def resolve_alert(
        db: Session,
        alert_id: UUID,
    ) -> Alert | None:

        return AlertRepository.resolve(
            db,
            alert_id,
        )

    # ======================================================
    # UPDATE STATUS
    # ======================================================

    @staticmethod
    def update_alert_status(
        db: Session,
        alert_id: UUID,
        status: AlertStatus,
    ) -> Alert | None:

        return AlertRepository.update_status(
            db,
            alert_id,
            status,
        )

    # ======================================================
    # DELETE
    # ======================================================

    @staticmethod
    def delete_alert(
        db: Session,
        alert_id: UUID,
    ) -> bool:

        return AlertRepository.delete(
            db,
            alert_id,
        )

    # ======================================================
    # DASHBOARD STATISTICS
    # ======================================================

    @staticmethod
    def dashboard_stats(
        db: Session,
    ) -> dict[str, int]:

        return AlertStatisticsService.get_dashboard_statistics(
            db
        )
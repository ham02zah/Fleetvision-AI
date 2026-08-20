
from __future__ import annotations

from datetime import datetime, timezone
from typing import Sequence
from uuid import UUID

from sqlalchemy import func, select
from sqlalchemy.orm import Session

from app.models.alert import (
    Alert,
    AlertSeverity,
    AlertStatus,
    AlertType,
)


class AlertRepository:
    """
    Database access layer for FleetVision alerts.

    This repository contains database operations only.
    Business logic belongs in AlertService.
    """

    # ======================================================
    # CREATE
    # ======================================================

    @staticmethod
    def create(
        db: Session,
        *,
        vehicle_id: UUID,
        title: str,
        description: str,
        alert_type: AlertType,
        severity: AlertSeverity,
        status: AlertStatus = AlertStatus.ACTIVE,
    ) -> Alert:

        alert = Alert(
            vehicle_id=vehicle_id,
            title=title,
            description=description,
            alert_type=alert_type,
            severity=severity,
            status=status,
        )

        db.add(alert)
        db.commit()
        db.refresh(alert)

        return alert

    # ======================================================
    # GET BY ID
    # ======================================================

    @staticmethod
    def get_by_id(
        db: Session,
        alert_id: UUID,
    ) -> Alert | None:

        statement = (
            select(Alert)
            .where(Alert.id == alert_id)
        )

        return db.scalars(statement).first()

    # ======================================================
    # GET ALL
    # ======================================================

    @staticmethod
    def get_all(
        db: Session,
        *,
        skip: int = 0,
        limit: int = 100,
    ) -> Sequence[Alert]:

        statement = (
            select(Alert)
            .order_by(Alert.created_at.desc())
            .offset(skip)
            .limit(limit)
        )

        return db.scalars(statement).all()

    # ======================================================
    # GET BY VEHICLE
    # ======================================================

    @staticmethod
    def get_by_vehicle(
        db: Session,
        vehicle_id: UUID,
        *,
        skip: int = 0,
        limit: int = 100,
    ) -> Sequence[Alert]:

        statement = (
            select(Alert)
            .where(Alert.vehicle_id == vehicle_id)
            .order_by(Alert.created_at.desc())
            .offset(skip)
            .limit(limit)
        )

        return db.scalars(statement).all()

    # ======================================================
    # GET ACTIVE ALERTS
    # ======================================================

    @staticmethod
    def get_active(
        db: Session,
        *,
        skip: int = 0,
        limit: int = 100,
    ) -> Sequence[Alert]:

        statement = (
            select(Alert)
            .where(
                Alert.status == AlertStatus.ACTIVE
            )
            .order_by(Alert.created_at.desc())
            .offset(skip)
            .limit(limit)
        )

        return db.scalars(statement).all()

    # ======================================================
    # GET ACTIVE ALERTS FOR VEHICLE
    # ======================================================

    @staticmethod
    def get_active_by_vehicle(
        db: Session,
        vehicle_id: UUID,
        *,
        skip: int = 0,
        limit: int = 100,
    ) -> Sequence[Alert]:

        statement = (
            select(Alert)
            .where(
                Alert.vehicle_id == vehicle_id,
                Alert.status == AlertStatus.ACTIVE,
            )
            .order_by(Alert.created_at.desc())
            .offset(skip)
            .limit(limit)
        )

        return db.scalars(statement).all()


    # ======================================================
    # GET ACTIVE ALERT BY VEHICLE + TYPE
    # ======================================================

    @staticmethod
    def get_active_by_vehicle_and_type(
        db: Session,
        vehicle_id: UUID,
        alert_type: AlertType,
    ) -> Alert | None:

        statement = (
            select(Alert)
            .where(
                Alert.vehicle_id == vehicle_id,
                Alert.alert_type == alert_type,
                Alert.status == AlertStatus.ACTIVE,
            )
            .order_by(Alert.created_at.desc())
        )

        return db.scalars(statement).first()
    
    # ======================================================
    # FILTER BY STATUS
    # ======================================================

    @staticmethod
    def get_by_status(
        db: Session,
        status: AlertStatus,
        *,
        skip: int = 0,
        limit: int = 100,
    ) -> Sequence[Alert]:

        statement = (
            select(Alert)
            .where(Alert.status == status)
            .order_by(Alert.created_at.desc())
            .offset(skip)
            .limit(limit)
        )

        return db.scalars(statement).all()

    # ======================================================
    # FILTER BY SEVERITY
    # ======================================================

    @staticmethod
    def get_by_severity(
        db: Session,
        severity: AlertSeverity,
        *,
        skip: int = 0,
        limit: int = 100,
    ) -> Sequence[Alert]:

        statement = (
            select(Alert)
            .where(Alert.severity == severity)
            .order_by(Alert.created_at.desc())
            .offset(skip)
            .limit(limit)
        )

        return db.scalars(statement).all()

    # ======================================================
    # FILTER BY TYPE
    # ======================================================

    @staticmethod
    def get_by_type(
        db: Session,
        alert_type: AlertType,
        *,
        skip: int = 0,
        limit: int = 100,
    ) -> Sequence[Alert]:

        statement = (
            select(Alert)
            .where(Alert.alert_type == alert_type)
            .order_by(Alert.created_at.desc())
            .offset(skip)
            .limit(limit)
        )

        return db.scalars(statement).all()

    # ======================================================
    # ACKNOWLEDGE
    # ======================================================

    @staticmethod
    def acknowledge(
        db: Session,
        alert_id: UUID,
    ) -> Alert | None:

        alert = AlertRepository.get_by_id(
            db,
            alert_id,
        )

        if alert is None:
            return None

        alert.status = AlertStatus.ACKNOWLEDGED
        alert.acknowledged_at = datetime.now(timezone.utc)

        db.commit()
        db.refresh(alert)

        return alert

    # ======================================================
    # RESOLVE
    # ======================================================

    @staticmethod
    def resolve(
        db: Session,
        alert_id: UUID,
    ) -> Alert | None:

        alert = AlertRepository.get_by_id(
            db,
            alert_id,
        )

        if alert is None:
            return None

        alert.status = AlertStatus.RESOLVED
        alert.resolved_at = datetime.now(timezone.utc)

        db.commit()
        db.refresh(alert)

        return alert

    # ======================================================
    # UPDATE STATUS
    # ======================================================

    @staticmethod
    def update_status(
        db: Session,
        alert_id: UUID,
        status: AlertStatus,
    ) -> Alert | None:

        alert = AlertRepository.get_by_id(
            db,
            alert_id,
        )

        if alert is None:
            return None

        alert.status = status

        now = datetime.now(timezone.utc)

        if status == AlertStatus.ACKNOWLEDGED:
            alert.acknowledged_at = now

        elif status == AlertStatus.RESOLVED:
            alert.resolved_at = now

        db.commit()
        db.refresh(alert)

        return alert

    # ======================================================
    # DELETE
    # ======================================================

    @staticmethod
    def delete(
        db: Session,
        alert_id: UUID,
    ) -> bool:

        alert = AlertRepository.get_by_id(
            db,
            alert_id,
        )

        if alert is None:
            return False

        db.delete(alert)
        db.commit()

        return True

    # ======================================================
    # COUNT
    # ======================================================

    @staticmethod
    def count(
        db: Session,
    ) -> int:

        statement = select(
            func.count(Alert.id)
        )

        return db.scalar(statement) or 0

    # ======================================================
    # COUNT BY STATUS
    # ======================================================

    @staticmethod
    def count_by_status(
        db: Session,
        status: AlertStatus,
    ) -> int:

        statement = (
            select(func.count(Alert.id))
            .where(Alert.status == status)
        )

        return db.scalar(statement) or 0

    # ======================================================
    # COUNT BY SEVERITY
    # ======================================================

    @staticmethod
    def count_by_severity(
        db: Session,
        severity: AlertSeverity,
    ) -> int:

        statement = (
            select(func.count(Alert.id))
            .where(Alert.severity == severity)
        )

        return db.scalar(statement) or 0

    # ======================================================
    # DASHBOARD STATISTICS
    # ======================================================

    @staticmethod
    def dashboard_stats(
        db: Session,
    ) -> dict[str, int]:

        total = AlertRepository.count(db)

        active = AlertRepository.count_by_status(
            db,
            AlertStatus.ACTIVE,
        )

        acknowledged = AlertRepository.count_by_status(
            db,
            AlertStatus.ACKNOWLEDGED,
        )

        resolved = AlertRepository.count_by_status(
            db,
            AlertStatus.RESOLVED,
        )

        low = AlertRepository.count_by_severity(
            db,
            AlertSeverity.LOW,
        )

        medium = AlertRepository.count_by_severity(
            db,
            AlertSeverity.MEDIUM,
        )

        high = AlertRepository.count_by_severity(
            db,
            AlertSeverity.HIGH,
        )

        critical = AlertRepository.count_by_severity(
            db,
            AlertSeverity.CRITICAL,
        )

        return {
            "total_alerts": total,
            "active_alerts": active,
            "acknowledged_alerts": acknowledged,
            "resolved_alerts": resolved,
            "low_alerts": low,
            "medium_alerts": medium,
            "high_alerts": high,
            "critical_alerts": critical,
        }

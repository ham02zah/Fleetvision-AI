from sqlalchemy.orm import Session

from app.models.alert import (
    Alert,
    AlertSeverity,
    AlertStatus,
    AlertType,
)
from app.repositories.alert_repository import (
    AlertRepository,
)


class AlertGenerationService:
    """
    Generates FleetVision alerts from telemetry
    and AI analysis.

    Prevents duplicate ACTIVE alerts for the
    same vehicle and alert type.
    """

    # ======================================================
    # THRESHOLDS
    # ======================================================

    SPEED_THRESHOLD = 120.0
    FUEL_THRESHOLD = 15.0
    ENGINE_TEMP_THRESHOLD = 105.0

    # ======================================================
    # CREATE DEDUPLICATED ALERT
    # ======================================================

    @staticmethod
    def create_alert_if_not_active(
        db: Session,
        *,
        vehicle_id,
        title: str,
        description: str,
        alert_type: AlertType,
        severity: AlertSeverity,
    ) -> Alert | None:

        existing_alert = (
            AlertRepository.get_active_by_vehicle_and_type(
                db=db,
                vehicle_id=vehicle_id,
                alert_type=alert_type,
            )
        )

        if existing_alert is not None:
            return None

        alert = Alert(
            vehicle_id=vehicle_id,
            title=title,
            description=description,
            alert_type=alert_type,
            severity=severity,
            status=AlertStatus.ACTIVE,
        )

        db.add(alert)

        return alert

    # ======================================================
    # GENERATE
    # ======================================================

    @staticmethod
    def generate(
        db: Session,
        vehicle_id,
        telemetry,
        ai_result: dict,
    ) -> list[Alert]:

        created_alerts: list[Alert] = []

        # ==================================================
        # SPEED
        # ==================================================

        if telemetry.speed >= AlertGenerationService.SPEED_THRESHOLD:

            alert = AlertGenerationService.create_alert_if_not_active(
                db=db,
                vehicle_id=vehicle_id,
                title="Overspeed Detected",
                description=(
                    f"Vehicle reached "
                    f"{telemetry.speed:.1f} km/h."
                ),
                alert_type=AlertType.SPEEDING,
                severity=AlertSeverity.HIGH,
            )

            if alert is not None:
                created_alerts.append(alert)

        # ==================================================
        # FUEL
        # ==================================================

        if telemetry.fuel <= AlertGenerationService.FUEL_THRESHOLD:

            alert = AlertGenerationService.create_alert_if_not_active(
                db=db,
                vehicle_id=vehicle_id,
                title="Low Fuel",
                description=(
                    f"Fuel remaining: "
                    f"{telemetry.fuel:.1f}%."
                ),
                alert_type=AlertType.FUEL,
                severity=AlertSeverity.MEDIUM,
            )

            if alert is not None:
                created_alerts.append(alert)

        # ==================================================
        # ENGINE TEMPERATURE
        # ==================================================

        if (
            telemetry.engine_temp
            >= AlertGenerationService.ENGINE_TEMP_THRESHOLD
        ):

            alert = AlertGenerationService.create_alert_if_not_active(
                db=db,
                vehicle_id=vehicle_id,
                title="Engine Temperature High",
                description=(
                    f"Engine temperature is "
                    f"{telemetry.engine_temp:.1f}°C."
                ),
                alert_type=AlertType.ENGINE,
                severity=AlertSeverity.CRITICAL,
            )

            if alert is not None:
                created_alerts.append(alert)

        # ==================================================
        # AI MAINTENANCE
        # ==================================================

        maintenance = ai_result.get(
            "maintenance_analysis",
            {},
        )

        if maintenance.get("maintenance_level") == "critical":

            alert = AlertGenerationService.create_alert_if_not_active(
                db=db,
                vehicle_id=vehicle_id,
                title="Maintenance Required",
                description=(
                    "AI recommends immediate maintenance."
                ),
                alert_type=AlertType.MAINTENANCE,
                severity=AlertSeverity.HIGH,
            )

            if alert is not None:
                created_alerts.append(alert)

        # ==================================================
        # AI RISK
        # ==================================================

        risk = ai_result.get(
            "risk_analysis",
            {},
        )

        if risk.get("risk_level") == "critical":

            alert = AlertGenerationService.create_alert_if_not_active(
                db=db,
                vehicle_id=vehicle_id,
                title="Critical Driving Risk",
                description=(
                    "AI detected dangerous driving."
                ),
                alert_type=AlertType.AI_RISK,
                severity=AlertSeverity.CRITICAL,
            )

            if alert is not None:
                created_alerts.append(alert)

        # ==================================================
        # SAVE
        # ==================================================

        if created_alerts:

            db.commit()

            for alert in created_alerts:
                db.refresh(alert)

        return created_alerts
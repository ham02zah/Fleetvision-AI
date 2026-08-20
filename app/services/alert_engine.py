from sqlalchemy.orm import Session

from app.models.alert import (
    Alert,
    AlertSeverity,
    AlertStatus,
    AlertType,
)
from app.models.telemetry import Telemetry


class AlertEngine:
    """
    Automatic Alert Generator.

    Generates alerts from telemetry and optional AI results.
    """

    @staticmethod
    def process(
        db: Session,
        telemetry: Telemetry,
        ai_result: dict | None = None,
    ):

        created_alerts = []

        created_alerts.extend(
            AlertEngine.check_speed(
                db,
                telemetry,
            )
        )

        created_alerts.extend(
            AlertEngine.check_fuel(
                db,
                telemetry,
            )
        )

        created_alerts.extend(
            AlertEngine.check_engine_temperature(
                db,
                telemetry,
            )
        )

        if ai_result:
            created_alerts.extend(
                AlertEngine.check_ai(
                    db,
                    telemetry,
                    ai_result,
                )
            )

        if created_alerts:
            db.commit()

            for alert in created_alerts:
                db.refresh(alert)

        return created_alerts

    # ======================================================
    # CREATE ALERT
    # ======================================================

    @staticmethod
    def create_alert(
        db: Session,
        telemetry: Telemetry,
        title: str,
        description: str,
        alert_type: AlertType,
        severity: AlertSeverity,
    ) -> Alert:

        alert = Alert(
            vehicle_id=telemetry.vehicle_id,
            title=title,
            description=description,
            alert_type=alert_type,
            severity=severity,
            status=AlertStatus.ACTIVE,
        )

        db.add(alert)

        return alert

    # ======================================================
    # SPEED
    # ======================================================

    @staticmethod
    def check_speed(
        db: Session,
        telemetry: Telemetry,
    ) -> list[Alert]:

        if telemetry.speed > 120:

            return [
                AlertEngine.create_alert(
                    db=db,
                    telemetry=telemetry,
                    title="Overspeed",
                    description=(
                        f"Vehicle reached "
                        f"{telemetry.speed:.1f} km/h"
                    ),
                    alert_type=AlertType.SPEEDING,
                    severity=AlertSeverity.HIGH,
                )
            ]

        return []

    # ======================================================
    # FUEL
    # ======================================================

    @staticmethod
    def check_fuel(
        db: Session,
        telemetry: Telemetry,
    ) -> list[Alert]:

        if telemetry.fuel < 10:

            return [
                AlertEngine.create_alert(
                    db=db,
                    telemetry=telemetry,
                    title="Low Fuel",
                    description=(
                        f"Fuel level is "
                        f"{telemetry.fuel:.1f}%"
                    ),
                    alert_type=AlertType.FUEL,
                    severity=AlertSeverity.MEDIUM,
                )
            ]

        return []

    # ======================================================
    # ENGINE TEMPERATURE
    # ======================================================

    @staticmethod
    def check_engine_temperature(
        db: Session,
        telemetry: Telemetry,
    ) -> list[Alert]:

        if telemetry.engine_temp > 105:

            return [
                AlertEngine.create_alert(
                    db=db,
                    telemetry=telemetry,
                    title="Engine Overheating",
                    description=(
                        f"Temperature "
                        f"{telemetry.engine_temp:.1f}°C"
                    ),
                    alert_type=AlertType.ENGINE,
                    severity=AlertSeverity.CRITICAL,
                )
            ]

        return []

    # ======================================================
    # AI
    # ======================================================

    @staticmethod
    def check_ai(
        db: Session,
        telemetry: Telemetry,
        ai_result: dict,
    ) -> list[Alert]:

        if ai_result.get("risk") == "HIGH":

            return [
                AlertEngine.create_alert(
                    db=db,
                    telemetry=telemetry,
                    title="AI Risk Detected",
                    description=ai_result.get(
                        "reason",
                        "AI detected abnormal behavior.",
                    ),
                    alert_type=AlertType.AI_RISK,
                    severity=AlertSeverity.CRITICAL,
                )
            ]

        return []
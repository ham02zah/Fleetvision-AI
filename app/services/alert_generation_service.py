from sqlalchemy.orm import Session

from app.models.alert import (
    Alert,
    AlertSeverity,
    AlertStatus,
    AlertType,
)


class AlertGenerationService:
    """
    Automatically creates alerts
    based on AI analysis.
    """

    @staticmethod
    def generate(
        db: Session,
        vehicle_id,
        telemetry,
        ai_result,
    ):

        created_alerts = []

        #######################################################
        # SPEED ALERT
        #######################################################

        if telemetry.speed >= 120:

            alert = Alert(
                vehicle_id=vehicle_id,
                title="Overspeed Detected",
                description=f"Vehicle reached {telemetry.speed} km/h",
                alert_type=AlertType.SPEEDING,
                severity=AlertSeverity.HIGH,
                status=AlertStatus.ACTIVE,
            )

            db.add(alert)

            created_alerts.append(alert)

        #######################################################
        # FUEL ALERT
        #######################################################

        if telemetry.fuel <= 15:

            alert = Alert(
                vehicle_id=vehicle_id,
                title="Low Fuel",
                description=f"Fuel remaining: {telemetry.fuel}%",
                alert_type=AlertType.FUEL,
                severity=AlertSeverity.MEDIUM,
                status=AlertStatus.ACTIVE,
            )

            db.add(alert)

            created_alerts.append(alert)

        #######################################################
        # ENGINE ALERT
        #######################################################

        if telemetry.engine_temp >= 105:

            alert = Alert(
                vehicle_id=vehicle_id,
                title="Engine Temperature High",
                description=f"Engine temperature is {telemetry.engine_temp}°C",
                alert_type=AlertType.ENGINE,
                severity=AlertSeverity.CRITICAL,
                status=AlertStatus.ACTIVE,
            )

            db.add(alert)

            created_alerts.append(alert)

        #######################################################
        # MAINTENANCE ALERT
        #######################################################

        maintenance = ai_result.get(
            "maintenance_analysis",
            {},
        )

        if (
            maintenance.get("maintenance_level")
            == "critical"
        ):

            alert = Alert(
                vehicle_id=vehicle_id,
                title="Maintenance Required",
                description="AI recommends immediate maintenance.",
                alert_type=AlertType.MAINTENANCE,
                severity=AlertSeverity.HIGH,
                status=AlertStatus.ACTIVE,
            )

            db.add(alert)

            created_alerts.append(alert)

        #######################################################
        # AI RISK ALERT
        #######################################################

        risk = ai_result.get(
            "risk_analysis",
            {},
        )

        if risk.get("risk_level") == "critical":

            alert = Alert(
                vehicle_id=vehicle_id,
                title="Critical Driving Risk",
                description="AI detected dangerous driving.",
                alert_type=AlertType.AI_RISK,
                severity=AlertSeverity.CRITICAL,
                status=AlertStatus.ACTIVE,
            )

            db.add(alert)

            created_alerts.append(alert)

        db.commit()

        for alert in created_alerts:
            db.refresh(alert)

        return created_alerts
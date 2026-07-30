from sqlalchemy.orm import Session

from app.models.alert import Alert
from app.models.telemetry import Telemetry
from app.models.alert import AlertSeverity


class AlertEngine:
    """
    Automatic Alert Generator.

    Generates alerts from telemetry.
    """

    @staticmethod
    def process(
        db: Session,
        telemetry: Telemetry,
        ai_result: dict | None = None,
    ):

        AlertEngine.check_speed(
            db,
            telemetry,
        )

        AlertEngine.check_fuel(
            db,
            telemetry,
        )

        AlertEngine.check_engine_temperature(
            db,
            telemetry,
        )

        if ai_result:

            AlertEngine.check_ai(
                db,
                telemetry,
                ai_result,
            )

        db.commit()

    @staticmethod
    def create_alert(
        db: Session,
        telemetry: Telemetry,
        title: str,
        description: str,
        severity: AlertSeverity,
    ):

        alert = Alert(
            vehicle_id=telemetry.vehicle_id,
            title=title,
            description=description,
            severity=severity,
        )

        db.add(alert)

    @staticmethod
    def check_speed(
        db: Session,
        telemetry: Telemetry,
    ):

        if telemetry.speed > 120:

            AlertEngine.create_alert(
                db=db,
                telemetry=telemetry,
                title="Overspeed",
                description=f"Vehicle reached {telemetry.speed:.1f} km/h",
                severity=AlertSeverity.HIGH,
            )

    @staticmethod
    def check_fuel(
        db: Session,
        telemetry: Telemetry,
    ):

        if telemetry.fuel < 10:

            AlertEngine.create_alert(
                db=db,
                telemetry=telemetry,
                title="Low Fuel",
                description=f"Fuel level is {telemetry.fuel:.1f}%",
                severity=AlertSeverity.MEDIUM,
            )

    @staticmethod
    def check_engine_temperature(
        db: Session,
        telemetry: Telemetry,
    ):

        if telemetry.engine_temp > 105:

            AlertEngine.create_alert(
                db=db,
                telemetry=telemetry,
                title="Engine Overheating",
                description=f"Temperature {telemetry.engine_temp:.1f}°C",
                severity=AlertSeverity.CRITICAL,
            )

    @staticmethod
    def check_ai(
        db: Session,
        telemetry: Telemetry,
        ai_result: dict,
    ):

        if ai_result.get("risk") == "HIGH":

            AlertEngine.create_alert(
                db=db,
                telemetry=telemetry,
                title="AI Risk Detected",
                description=ai_result.get(
                    "reason",
                    "AI detected abnormal behavior.",
                ),
                severity=AlertSeverity.CRITICAL,
            )
            
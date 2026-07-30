from app.ai.alerts.alert_models import AIAlert


class AlertEngine:

    @staticmethod
    def generate(

        telemetry,

        ai_result,

    ):

        alerts = []

        speed = telemetry.speed

        if speed >= 120:

            alerts.append(

                AIAlert.create(

                    vehicle_id=telemetry.vehicle_id,

                    level="CRITICAL",

                    category="OVERSPEED",

                    title="Overspeed Detected",

                    message=f"Vehicle moving at {speed} km/h.",

                )

            )

        risk = ai_result["risk_analysis"]["risk_level"]

        if risk == "HIGH":

            alerts.append(

                AIAlert.create(

                    vehicle_id=telemetry.vehicle_id,

                    level="HIGH",

                    category="RISK",

                    title="High Driving Risk",

                    message="Driver behaviour requires attention.",

                )

            )

        maintenance = ai_result["maintenance_analysis"]["maintenance_level"]

        if maintenance == "HIGH":

            alerts.append(

                AIAlert.create(

                    vehicle_id=telemetry.vehicle_id,

                    level="HIGH",

                    category="MAINTENANCE",

                    title="Maintenance Required",

                    message="Vehicle should be serviced immediately.",

                )

            )

        if ai_result["anomaly_analysis"]["has_anomaly"]:

            alerts.append(

                AIAlert.create(

                    vehicle_id=telemetry.vehicle_id,

                    level="CRITICAL",

                    category="ANOMALY",

                    title="Anomaly Detected",

                    message="Unexpected vehicle behaviour detected.",

                )

            )

        return alerts
from app.ai.explainability import explanation_templates as t


class ExplainabilityEngine:

    @staticmethod
    def generate(
        *,
        telemetry,
        risk_level,
        maintenance_level,
        health_score,
        driver_grade,
        anomalies,
    ):

        explanations = []

        if telemetry.fuel < 15:
            explanations.append(t.LOW_FUEL)

        if telemetry.engine_temp > 110:
            explanations.append(t.HIGH_ENGINE_TEMP)

        if telemetry.speed > 120:
            explanations.append(t.OVERSPEED)

        if (
            telemetry.engine_running
            and not telemetry.ignition
        ):
            explanations.append(
                t.IGNITION_ENGINE
            )

        if health_score < 40:
            explanations.append(
                t.LOW_HEALTH
            )

        if driver_grade in [
            "D",
            "F",
        ]:
            explanations.append(
                t.HARSH_ACCELERATION
            )

        if anomalies:

            for anomaly in anomalies:

                explanations.append(
                    anomaly
                )

        if not explanations:

            explanations.append(
                t.NORMAL
            )

        return explanations
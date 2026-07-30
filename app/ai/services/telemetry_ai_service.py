from app.ai.intelligence.intelligence_service import (
    AIIntelligenceService,
)

from app.ai.alerts.alert_engine import AlertEngine

from app.ai.alerts.alert_history import AlertHistory


class TelemetryAIService:

    @staticmethod
    def analyze(

        telemetry,

        previous_speed=0.0,

    ):

        ai_result = AIIntelligenceService.analyze(

            telemetry,

            previous_speed,

        )

        alerts = AlertEngine.generate(

            telemetry,

            ai_result,

        )

        for alert in alerts:

            AlertHistory.add(alert)

        return {

            "analysis": ai_result,

            "alerts": alerts,

        }
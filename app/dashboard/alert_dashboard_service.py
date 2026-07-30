from app.ai.alerts.alert_history import (
    AlertHistory,
)


class AlertDashboardService:

    @staticmethod
    def summary():

        alerts = AlertHistory.all()

        critical = len(

            [

                a

                for a in alerts

                if a.level == "CRITICAL"

            ]

        )

        return {

            "critical_alerts": critical,

            "total_alerts": len(alerts),

        }
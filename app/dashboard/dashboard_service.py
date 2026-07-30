from app.dashboard.statistics_service import (
    StatisticsService,
)

from app.dashboard.health_service import (
    HealthDashboardService,
)

from app.dashboard.alert_dashboard_service import (
    AlertDashboardService,
)


class DashboardService:

    @staticmethod
    def overview():

        stats = StatisticsService.statistics()

        health = HealthDashboardService.summary()

        alerts = AlertDashboardService.summary()

        return {

            "total_vehicles": stats["total_vehicles"],

            "online_vehicles": stats["online_vehicles"],

            "moving_vehicles": stats["moving_vehicles"],

            "critical_alerts": alerts["critical_alerts"],

            "average_health": health["average_health"],

            "average_driver_score": health["average_driver_score"],

        }
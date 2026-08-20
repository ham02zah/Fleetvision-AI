from app.analytics.fleet_statistics import (
    FleetStatisticsCalculator,
)

from app.analytics.fleet_health import (
    FleetHealthCalculator,
)

from app.analytics.fleet_risk import (
    FleetRiskCalculator,
)


class FleetAnalyticsService:
    """
    Central fleet analytics service.

    This class combines every analytics
    calculation into one response.
    """

    @staticmethod
    def generate(
        telemetry_records,
        health_scores,
        risk_scores,
    ):

        statistics = (
            FleetStatisticsCalculator.calculate(
                telemetry_records
            )
        )

        health = (
            FleetHealthCalculator.calculate(
                health_scores
            )
        )

        risk = (
            FleetRiskCalculator.calculate(
                risk_scores
            )
        )

        return {

            "fleet_statistics": statistics,

            "fleet_health": health,

            "fleet_risk": risk,

        }
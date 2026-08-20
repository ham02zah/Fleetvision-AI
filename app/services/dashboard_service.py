from sqlalchemy.orm import Session

from app.repositories.dashboard_repository import (
    DashboardRepository,
)

from app.services.alert_dashboard_service import (
    AlertDashboardService,
)

class DashboardService:

    @staticmethod
    def summary(db: Session):

        return DashboardRepository.summary(db)

    @staticmethod
    def speed_trend(db: Session):

        telemetry = DashboardRepository.speed_trend(db)

        return [

            {

                "timestamp": t.recorded_at,

                "speed": t.speed,

            }

            for t in telemetry

        ]

    @staticmethod
    def health_trend(db: Session):

        predictions = DashboardRepository.health_trend(db)

        return [

            {

                "timestamp": p.created_at,

                "health_score": p.health_score,

            }

            for p in predictions

        ]

    @staticmethod
    def leaderboard(db: Session):

        predictions = DashboardRepository.leaderboard(db)

        return [

            {

                "vehicle_id": str(
                    p.vehicle_id
                ),

                "driver_score": p.driver_score,

                "health_score": p.health_score,

                "risk_level": p.risk_level,

            }

            for p in predictions

        ]

    @staticmethod
    def risky_vehicles(db: Session):

        predictions = DashboardRepository.risky_vehicles(db)

        return [

            {

                "vehicle_id": str(
                    p.vehicle_id
                ),

                "risk_level": p.risk_level,

                "health_score": p.health_score,

                "maintenance_level": p.maintenance_level,

                "predicted_speed": p.predicted_speed,

            }

            for p in predictions

        ]

    @staticmethod
    def decision_history(db: Session):

        predictions = DashboardRepository.decision_history(db)

        return [

            {

                "timestamp": p.created_at,

                "decision": p.decision,

                "risk_level": p.risk_level,

                "health_score": p.health_score,

            }

            for p in predictions

        ]

 
    @staticmethod
    def get_overview(db: Session):
        """
        Returns the complete dashboard overview
        for the frontend.
        """

        return {
            "summary": DashboardRepository.summary(db),
            "speed_trend": DashboardService.speed_trend(db),
            "health_trend": DashboardService.health_trend(db),
            "leaderboard": DashboardService.leaderboard(db),
            "risky_vehicles": DashboardService.risky_vehicles(db),
            "decision_history": DashboardService.decision_history(db),
            "alerts": AlertDashboardService.statistics(db),
        }

  
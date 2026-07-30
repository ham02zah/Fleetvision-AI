from sqlalchemy.orm import Session

from app.repositories.analytics_repository import (
    AnalyticsRepository,
)


class AnalyticsService:

    @staticmethod
    def fleet_summary(db: Session):

        return AnalyticsRepository.fleet_summary(
            db
        )

    @staticmethod
    def risk_distribution(db: Session):

        return AnalyticsRepository.risk_distribution(
            db
        )

    @staticmethod
    def vehicle_health(db: Session):

        predictions = AnalyticsRepository.vehicle_health(
            db
        )

        response = []

        for prediction in predictions:

            response.append(

                {

                    "vehicle_id": str(
                        prediction.vehicle_id
                    ),

                    "health_score":
                        prediction.health_score,

                    "driver_score":
                        prediction.driver_score,

                    "risk_level":
                        prediction.risk_level,

                    "maintenance_level":
                        prediction.maintenance_level,

                    "predicted_speed":
                        prediction.predicted_speed,

                }

            )

        return response
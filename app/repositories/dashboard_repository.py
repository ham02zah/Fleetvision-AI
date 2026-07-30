from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.ai_prediction import AIPrediction
from app.models.alert import Alert
from app.models.telemetry import Telemetry
from app.models.vehicle import Vehicle


class DashboardRepository:

    @staticmethod
    def summary(db: Session):

        return {

            "total_vehicles":

                db.query(Vehicle).count(),

            "active_vehicles":

                db.query(Vehicle)
                .filter(
                    Vehicle.is_active == True
                )
                .count(),

            "total_predictions":

                db.query(AIPrediction)
                .count(),

            "total_alerts":

                db.query(Alert)
                .count(),

            "average_health_score":

                round(

                    db.query(
                        func.avg(
                            AIPrediction.health_score
                        )
                    ).scalar() or 0,

                    2,
                ),

            "average_driver_score":

                round(

                    db.query(
                        func.avg(
                            AIPrediction.driver_score
                        )
                    ).scalar() or 0,

                    2,
                ),

            "average_speed":

                round(

                    db.query(
                        func.avg(
                            Telemetry.speed
                        )
                    ).scalar() or 0,

                    2,
                ),

        }

    @staticmethod
    def speed_trend(db: Session):

        return (

            db.query(Telemetry)

            .order_by(
                Telemetry.recorded_at.desc()
            )

            .limit(30)

            .all()

        )

    @staticmethod
    def health_trend(db: Session):

        return (

            db.query(AIPrediction)

            .order_by(
                AIPrediction.created_at.desc()
            )

            .limit(30)

            .all()

        )

    @staticmethod
    def leaderboard(db: Session):

        return (

            db.query(AIPrediction)

            .order_by(
                AIPrediction.driver_score.desc()
            )

            .limit(20)

            .all()

        )

    @staticmethod
    def risky_vehicles(db: Session):

        return (

            db.query(AIPrediction)

            .order_by(
                AIPrediction.health_score.asc()
            )

            .limit(20)

            .all()

        )

    @staticmethod
    def decision_history(db: Session):

        return (

            db.query(AIPrediction)

            .order_by(
                AIPrediction.created_at.desc()
            )

            .limit(50)

            .all()

        )
from datetime import datetime, timedelta, timezone

from sqlalchemy import func
from sqlalchemy.orm import Session

from app.models.alert import Alert
from app.models.alert import AlertSeverity


class AlertStatisticsService:
    """
    Alert Dashboard Statistics.
    """

    @staticmethod
    def get_statistics(db: Session):

        total_alerts = (
            db.query(Alert)
            .count()
        )

        critical = (
            db.query(Alert)
            .filter(
                Alert.severity == AlertSeverity.CRITICAL
            )
            .count()
        )

        high = (
            db.query(Alert)
            .filter(
                Alert.severity == AlertSeverity.HIGH
            )
            .count()
        )

        medium = (
            db.query(Alert)
            .filter(
                Alert.severity == AlertSeverity.MEDIUM
            )
            .count()
        )

        low = (
            db.query(Alert)
            .filter(
                Alert.severity == AlertSeverity.LOW
            )
            .count()
        )

        resolved = (
            db.query(Alert)
            .filter(
                Alert.is_resolved == True
            )
            .count()
        )

        unresolved = (
            db.query(Alert)
            .filter(
                Alert.is_resolved == False
            )
            .count()
        )

        today = datetime.now(timezone.utc)

        today_start = datetime(
            today.year,
            today.month,
            today.day,
            tzinfo=timezone.utc,
        )

        today_alerts = (
            db.query(Alert)
            .filter(
                Alert.created_at >= today_start
            )
            .count()
        )

        week_start = today - timedelta(days=7)

        weekly_alerts = (
            db.query(Alert)
            .filter(
                Alert.created_at >= week_start
            )
            .count()
        )

        top_vehicle = (
            db.query(
                Alert.vehicle_id,
                func.count(Alert.id)
            )
            .group_by(Alert.vehicle_id)
            .order_by(
                func.count(Alert.id).desc()
            )
            .first()
        )

        return {

            "summary": {

                "total_alerts": total_alerts,

                "resolved": resolved,

                "unresolved": unresolved,

                "today": today_alerts,

                "last_7_days": weekly_alerts,

            },

            "severity": {

                "critical": critical,

                "high": high,

                "medium": medium,

                "low": low,

            },

            "top_vehicle": (

                None

                if top_vehicle is None

                else {

                    "vehicle_id": str(
                        top_vehicle[0]
                    ),

                    "alerts": top_vehicle[1],

                }

            )

        }
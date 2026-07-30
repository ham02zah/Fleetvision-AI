from uuid import UUID

from sqlalchemy.orm import Session

from app.models.alert import Alert


class AlertDashboardService:
    """
    Dashboard service for viewing alerts.
    """

    @staticmethod
    def get_all_alerts(db: Session):

        alerts = (
            db.query(Alert)
            .order_by(Alert.created_at.desc())
            .all()
        )

        return {
            "count": len(alerts),
            "alerts": alerts,
        }

    @staticmethod
    def get_open_alerts(db: Session):

        alerts = (
            db.query(Alert)
            .filter(Alert.is_resolved == False)
            .order_by(Alert.created_at.desc())
            .all()
        )

        return {
            "count": len(alerts),
            "alerts": alerts,
        }

    @staticmethod
    def get_resolved_alerts(db: Session):

        alerts = (
            db.query(Alert)
            .filter(Alert.is_resolved == True)
            .order_by(Alert.created_at.desc())
            .all()
        )

        return {
            "count": len(alerts),
            "alerts": alerts,
        }

    @staticmethod
    def get_critical_alerts(db: Session):

        alerts = (
            db.query(Alert)
            .filter(Alert.severity == "CRITICAL")
            .order_by(Alert.created_at.desc())
            .all()
        )

        return {
            "count": len(alerts),
            "alerts": alerts,
        }

    @staticmethod
    def get_vehicle_alerts(
        db: Session,
        vehicle_id: UUID,
    ):

        alerts = (
            db.query(Alert)
            .filter(Alert.vehicle_id == vehicle_id)
            .order_by(Alert.created_at.desc())
            .all()
        )

        return {
            "count": len(alerts),
            "alerts": alerts,
        }
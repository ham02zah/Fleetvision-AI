from uuid import UUID

from sqlalchemy.orm import Session

from app.models.alert import Alert


class AlertService:
    """
    Alert Management Service

    Handles:

    • Fetch alerts
    • Fetch unread alerts
    • Mark alert as read
    • Delete alert
    • Dashboard statistics
    """

    @staticmethod
    def get_all_alerts(
        db: Session,
    ):

        return (
            db.query(Alert)
            .order_by(
                Alert.created_at.desc()
            )
            .all()
        )

    @staticmethod
    def get_unread_alerts(
        db: Session,
    ):

        return (
            db.query(Alert)
            .filter(
                Alert.is_read == False
            )
            .order_by(
                Alert.created_at.desc()
            )
            .all()
        )

    @staticmethod
    def get_alert(
        db: Session,
        alert_id: UUID,
    ):

        return (
            db.query(Alert)
            .filter(
                Alert.id == alert_id
            )
            .first()
        )

    @staticmethod
    def mark_as_read(
        db: Session,
        alert_id: UUID,
    ):

        alert = (
            db.query(Alert)
            .filter(
                Alert.id == alert_id
            )
            .first()
        )

        if alert is None:

            return None

        alert.is_read = True

        db.commit()

        db.refresh(alert)

        return alert

    @staticmethod
    def delete_alert(
        db: Session,
        alert_id: UUID,
    ):

        alert = (
            db.query(Alert)
            .filter(
                Alert.id == alert_id
            )
            .first()
        )

        if alert is None:

            return False

        db.delete(alert)

        db.commit()

        return True

    @staticmethod
    def dashboard_stats(
        db: Session,
    ):

        total = (
            db.query(Alert)
            .count()
        )

        unread = (
            db.query(Alert)
            .filter(
                Alert.is_read == False
            )
            .count()
        )

        critical = (
            db.query(Alert)
            .filter(
                Alert.severity == "critical"
            )
            .count()
        )

        warning = (
            db.query(Alert)
            .filter(
                Alert.severity == "warning"
            )
            .count()
        )

        info = (
            db.query(Alert)
            .filter(
                Alert.severity == "info"
            )
            .count()
        )

        return {

            "total_alerts": total,

            "unread_alerts": unread,

            "critical_alerts": critical,

            "warning_alerts": warning,

            "info_alerts": info,

        }
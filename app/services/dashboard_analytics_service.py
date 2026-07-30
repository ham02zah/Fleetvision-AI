from sqlalchemy.orm import Session

from app.models.vehicle_status import VehicleStatus


class DashboardAnalyticsService:
    """
    Dashboard analytics service.
    """

    @staticmethod
    def fleet_overview(db: Session):

        vehicles = db.query(VehicleStatus).all()

        total = len(vehicles)

        moving = sum(
            1 for v in vehicles
            if getattr(v, "speed", 0) > 0
        )

        stopped = total - moving

        avg_speed = (
            round(
                sum(v.speed for v in vehicles) / total,
                2,
            )
            if total
            else 0
        )

        return {
            "total_vehicles": total,
            "moving": moving,
            "stopped": stopped,
            "average_speed": avg_speed,
        }
from sqlalchemy.orm import Session

from app.models.ai_prediction import AIPrediction


class AIPredictionRepository:

    @staticmethod
    def create(
        db: Session,
        prediction: AIPrediction,
    ):

        print("\nRepository.create()")

        db.add(prediction)

        print("Added to session")

        db.flush()

        print("Flush successful")

        db.commit()

        print("Commit successful")

        db.refresh(prediction)

        print("Refresh successful")

        return prediction

    @staticmethod
    def latest(
        db: Session,
        vehicle_id,
    ):

        return (
            db.query(AIPrediction)
            .filter(
                AIPrediction.vehicle_id == vehicle_id
            )
            .order_by(
                AIPrediction.created_at.desc()
            )
            .first()
        )

    @staticmethod
    def history(
        db: Session,
        vehicle_id,
    ):

        return (
            db.query(AIPrediction)
            .filter(
                AIPrediction.vehicle_id == vehicle_id
            )
            .order_by(
                AIPrediction.created_at.desc()
            )
            .all()
        )
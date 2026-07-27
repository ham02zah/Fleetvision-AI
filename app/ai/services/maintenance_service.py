from app.ai.inference.maintenance_predictor import (
    predict_maintenance,
)


class MaintenanceAIService:
    """
    Wrapper around maintenance prediction.
    """

    @staticmethod
    def analyze(
        fuel: float,
        engine_temp: float,
        odometer: float,
        speed: float,
    ):
        return predict_maintenance(
            fuel=fuel,
            engine_temp=engine_temp,
            odometer=odometer,
            speed=speed,
        )
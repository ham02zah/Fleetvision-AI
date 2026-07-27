from app.ai.anomaly.advanced_anomaly_detector import (
    AdvancedAnomalyDetector,
)


class AnomalyService:
    """
    Runs anomaly detection.
    """

    @staticmethod
    def analyze(
        *,
        speed,
        previous_speed,
        latitude,
        longitude,
        fuel,
        engine_temp,
        ignition,
        engine_running,
    ):

        return AdvancedAnomalyDetector.analyze(
            speed=speed,
            previous_speed=previous_speed,
            latitude=latitude,
            longitude=longitude,
            fuel=fuel,
            engine_temp=engine_temp,
            ignition=ignition,
            engine_running=engine_running,
        )
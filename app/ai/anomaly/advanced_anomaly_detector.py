class AdvancedAnomalyDetector:
    """
    Enterprise anomaly detector.

    Detects abnormal vehicle behaviour
    before machine learning models are introduced.
    """

    @staticmethod
    def analyze(
        *,
        speed: float,
        previous_speed: float,
        latitude: float,
        longitude: float,
        fuel: float,
        engine_temp: float,
        ignition: bool,
        engine_running: bool,
    ):
        anomalies = []

        ####################################################
        # Speed spike
        ####################################################

        if abs(speed - previous_speed) > 40:
            anomalies.append(
                "Sudden speed spike detected."
            )

        ####################################################
        # Impossible speed
        ####################################################

        if speed > 180:
            anomalies.append(
                "Impossible vehicle speed."
            )

        ####################################################
        # Engine temperature
        ####################################################

        if engine_temp >= 110:
            anomalies.append(
                "Critical engine temperature."
            )

        ####################################################
        # Fuel
        ####################################################

        if fuel <= 5:
            anomalies.append(
                "Critically low fuel."
            )

        ####################################################
        # Ignition inconsistency
        ####################################################

        if engine_running and not ignition:
            anomalies.append(
                "Engine running while ignition is OFF."
            )

        ####################################################
        # Vehicle movement
        ####################################################

        if speed > 0 and not engine_running:
            anomalies.append(
                "Vehicle moving while engine is OFF."
            )

        ####################################################
        # GPS validation
        ####################################################

        if latitude < -90 or latitude > 90:
            anomalies.append(
                "Invalid latitude received."
            )

        if longitude < -180 or longitude > 180:
            anomalies.append(
                "Invalid longitude received."
            )

        ####################################################
        # Final response
        ####################################################

        return {
            "has_anomaly": len(anomalies) > 0,
            "anomaly_count": len(anomalies),
            "anomalies": anomalies,
        }
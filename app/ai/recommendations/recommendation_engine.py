class RecommendationEngine:
    """
    Generates recommendations using
    outputs from all AI modules.
    """

    @staticmethod
    def generate(
        *,
        speed: float,
        fuel: float,
        engine_temp: float,
        risk_level: str,
        maintenance_level: str,
        health_status: str,
        driver_grade: str,
    ):
        recommendations = []

        ###########################################################
        # SPEED
        ###########################################################

        if speed >= 100:
            recommendations.append(
                "Reduce vehicle speed immediately."
            )

        ###########################################################
        # RISK
        ###########################################################

        if risk_level == "HIGH":
            recommendations.append(
                "High driving risk detected. Drive carefully."
            )

        elif risk_level == "MEDIUM":
            recommendations.append(
                "Moderate driving risk. Monitor driver behaviour."
            )

        ###########################################################
        # FUEL
        ###########################################################

        if fuel <= 15:
            recommendations.append(
                "Refuel vehicle as soon as possible."
            )

        elif fuel <= 30:
            recommendations.append(
                "Fuel level is getting low."
            )

        ###########################################################
        # ENGINE TEMPERATURE
        ###########################################################

        if engine_temp >= 110:
            recommendations.append(
                "Inspect engine cooling system immediately."
            )

        elif engine_temp >= 100:
            recommendations.append(
                "Monitor engine temperature."
            )

        ###########################################################
        # MAINTENANCE
        ###########################################################

        if maintenance_level == "HIGH":
            recommendations.append(
                "Schedule maintenance immediately."
            )

        elif maintenance_level == "MEDIUM":
            recommendations.append(
                "Vehicle maintenance is recommended soon."
            )

        ###########################################################
        # HEALTH
        ###########################################################

        if health_status == "POOR":
            recommendations.append(
                "Vehicle should not be used for long-distance trips."
            )

        elif health_status == "FAIR":
            recommendations.append(
                "Vehicle condition should be monitored."
            )

        ###########################################################
        # DRIVER
        ###########################################################

        if driver_grade == "D":
            recommendations.append(
                "Driver coaching is recommended."
            )

        elif driver_grade == "C":
            recommendations.append(
                "Encourage smoother driving habits."
            )

        ###########################################################
        # DEFAULT
        ###########################################################

        if not recommendations:
            recommendations.append(
                "Vehicle is operating normally."
            )

        return {
            "recommendations": recommendations,
            "total": len(recommendations),
        }
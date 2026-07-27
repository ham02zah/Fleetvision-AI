class VehicleHealthScore:
    """
    Calculates overall vehicle health score.
    """

    @staticmethod
    def calculate(
        *,
        speed: float,
        fuel: float,
        engine_temp: float,
        odometer: float,
        risk_level: str,
        maintenance_level: str,
    ):
        score = 100
        issues = []

        # Fuel
        if fuel < 20:
            score -= 20
            issues.append("Low fuel level")

        elif fuel < 40:
            score -= 10

        # Engine temperature
        if engine_temp >= 110:
            score -= 25
            issues.append("High engine temperature")

        elif engine_temp >= 95:
            score -= 10

        # Speed
        if speed >= 100:
            score -= 15
            issues.append("Overspeed detected")

        elif speed >= 80:
            score -= 5

        # Vehicle mileage
        if odometer >= 200000:
            score -= 20
            issues.append("High vehicle mileage")

        elif odometer >= 100000:
            score -= 10

        # AI Risk
        if risk_level == "HIGH":
            score -= 15

        elif risk_level == "MEDIUM":
            score -= 8

        # Maintenance
        if maintenance_level == "HIGH":
            score -= 15

        elif maintenance_level == "MEDIUM":
            score -= 8

        score = max(0, min(100, score))

        if score >= 85:
            status = "EXCELLENT"

        elif score >= 70:
            status = "GOOD"

        elif score >= 50:
            status = "FAIR"

        else:
            status = "POOR"

        return {
            "health_score": score,
            "status": status,
            "issues": issues,
        }
class DriverBehaviorAnalyzer:
    """
    Driver behaviour scoring engine.
    """

    @staticmethod
    def analyze(
        *,
        speed: float,
        previous_speed: float,
        fuel: float,
        engine_temp: float,
    ):
        score = 100
        violations = []

        acceleration = speed - previous_speed

        if speed >= 100:
            score -= 25
            violations.append("Overspeed")

        elif speed >= 80:
            score -= 10

        if acceleration >= 20:
            score -= 10
            violations.append("Harsh acceleration")

        elif acceleration <= -20:
            score -= 10
            violations.append("Harsh braking")

        if fuel < 20:
            score -= 5
            violations.append("Low fuel")

        if engine_temp >= 110:
            score -= 10
            violations.append("High engine temperature")

        score = max(0, min(score, 100))

        if score >= 90:
            grade = "A"
            behaviour = "SAFE"

        elif score >= 75:
            grade = "B"
            behaviour = "GOOD"

        elif score >= 60:
            grade = "C"
            behaviour = "AVERAGE"

        elif score >= 40:
            grade = "D"
            behaviour = "AGGRESSIVE"

        else:
            grade = "F"
            behaviour = "DANGEROUS"

        return {
            "score": score,
            "grade": grade,
            "behaviour": behaviour,
            "violations": violations,
        }
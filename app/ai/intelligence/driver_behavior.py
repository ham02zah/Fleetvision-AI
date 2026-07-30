class DriverBehaviorAnalyzer:
    """
    Analyzes driver behavior from telemetry data.
    """

    @staticmethod
    def analyze(
        speed,
        previous_speed=0.0,
        fuel=None,
        engine_temp=None,
    ):
        """
        Analyze driving style.

        Returns driver grade,
        score and behavior insights.
        """

        score = 100

        issues = []


        # Speed analysis
        if speed >= 100:

            score -= 15

            issues.append(
                "High speed detected"
            )


        # Acceleration analysis

        acceleration = (
            speed - previous_speed
        )


        if acceleration > 20:

            score -= 10

            issues.append(
                "Harsh acceleration detected"
            )


        if acceleration < -20:

            score -= 5

            issues.append(
                "Harsh braking detected"
            )


        # Fuel behavior

        if fuel is not None:

            if fuel < 15:

                score -= 10

                issues.append(
                    "Low fuel level"
                )


        # Engine temperature

        if engine_temp is not None:

            if engine_temp > 110:

                score -= 15

                issues.append(
                    "Engine overheating"
                )


        # Keep score valid

        score = max(
            score,
            0
        )


        # Grade calculation

        if score >= 90:

            grade = "A"

            behavior = "Excellent"


        elif score >= 75:

            grade = "B"

            behavior = "Good"


        elif score >= 50:

            grade = "C"

            behavior = "Moderate"


        else:

            grade = "D"

            behavior = "Risky"



        return {

            "score": score,

            "grade": grade,

            "behavior": behavior,

            "issues": issues,

        }
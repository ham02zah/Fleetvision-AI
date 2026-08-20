class FleetHealthCalculator:
    """
    Calculates fleet health.
    """

    @staticmethod
    def calculate(
        vehicle_health_scores,
    ):

        if not vehicle_health_scores:

            return {

                "score": 0,

                "status": "UNKNOWN",

            }

        score = sum(
            vehicle_health_scores
        ) / len(
            vehicle_health_scores
        )

        if score >= 85:

            status = "EXCELLENT"

        elif score >= 70:

            status = "GOOD"

        elif score >= 50:

            status = "FAIR"

        else:

            status = "POOR"

        return {

            "score": round(
                score,
                2,
            ),

            "status": status,

        }
class BehaviorAnalyzer:
    """
    Analyzes driving behavior from telemetry.
    """


    @staticmethod
    def analyze(df):

        speeding_events = 0
        harsh_acceleration_events = 0


        if "speed" in df.columns:

            speeding_events = (
                df["speed"] > 100
            ).sum()


        if "acceleration" in df.columns:

            harsh_acceleration_events = (
                abs(df["acceleration"]) > 20
            ).sum()



        score = 100


        score -= speeding_events * 2

        score -= (
            harsh_acceleration_events * 3
        )


        score = max(
            score,
            0
        )


        if score >= 80:

            status = "SAFE"

            risk = "LOW"


        elif score >= 50:

            status = "MODERATE"

            risk = "MEDIUM"


        else:

            status = "DANGEROUS"

            risk = "HIGH"



        recommendations = []


        if speeding_events:

            recommendations.append(
                "Reduce speeding frequency"
            )


        if harsh_acceleration_events:

            recommendations.append(
                "Avoid aggressive acceleration"
            )


        if not recommendations:

            recommendations.append(
                "Driver behavior is good"
            )


        return {

            "driver_score": round(
                score,
                2
            ),

            "behavior_status": status,

            "speeding_events":
                int(speeding_events),

            "harsh_acceleration_events":
                int(harsh_acceleration_events),

            "risk_level": risk,

            "recommendations":
                recommendations,

        }
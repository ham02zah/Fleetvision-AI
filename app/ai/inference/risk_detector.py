from datetime import datetime, timezone

from app.ai.utils.feature_builder import build_features


def detect_speed_risk(
    speed: float,
    previous_speed: float = 0.0,
    timestamp: datetime | None = None,
):
    """
    Detect overspeed and driving risk.
    """

    if timestamp is None:
        timestamp = datetime.now(timezone.utc)

    features = build_features(
        speed=speed,
        previous_speed=previous_speed,
        timestamp=timestamp,
    )

    speed_change = features["speed_change"]
    acceleration = features["acceleration"]

    ########################################################
    # Risk Level
    ########################################################

    if speed >= 120:
        risk = "HIGH"
        risk_score = 95

    elif speed >= 100:
        risk = "HIGH"
        risk_score = 85

    elif speed >= 80:
        risk = "MEDIUM"
        risk_score = 60

    elif speed >= 50:
        risk = "LOW"
        risk_score = 30

    else:
        risk = "LOW"
        risk_score = 10

    ########################################################

    return {

        "current_speed": speed,

        "previous_speed": previous_speed,

        "speed_change": round(speed_change,2),

        "acceleration": round(acceleration,2),

        "overspeed": speed >= 100,

        "risk_level": risk,

        "risk_score": risk_score,

        "timestamp": timestamp.isoformat(),

    }
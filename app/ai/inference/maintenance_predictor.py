from app.ai.utils.maintenance_features import (
    build_maintenance_features,
)


def predict_maintenance(
    fuel: float,
    engine_temp: float,
    odometer: float,
    speed: float,
):
    """
    Predict maintenance requirements.
    """

    features = build_maintenance_features(
        fuel=fuel,
        engine_temp=engine_temp,
        odometer=odometer,
        speed=speed,
    )

    score = features["maintenance_score"]

    issues = []

    if features["high_temperature"]:
        issues.append("High engine temperature")

    if features["low_fuel"]:
        issues.append("Low fuel")

    if features["high_mileage"]:
        issues.append("High vehicle mileage")

    if features["aggressive_driving"]:
        issues.append("Aggressive driving detected")

    if score >= 85:
        level = "LOW"
        remaining = 10000

    elif score >= 60:
        level = "MEDIUM"
        remaining = 5000

    else:
        level = "HIGH"
        remaining = 1000

    service_required = score < 85

    if level == "LOW":
        recommendation = "Vehicle condition is good."

    elif level == "MEDIUM":
        recommendation = (
            "Schedule maintenance within one week."
        )

    else:
        recommendation = (
            "Immediate inspection recommended."
        )

    return {
        "maintenance_score": score,
        "maintenance_level": level,
        "service_required": service_required,
        "estimated_remaining_km": remaining,
        "issues": issues,
        "recommendation": recommendation,
        "timestamp": features["timestamp"].isoformat(),
    }
from datetime import datetime


def build_maintenance_features(
    fuel: float,
    engine_temp: float,
    odometer: float,
    speed: float,
):
    """
    Build features for maintenance prediction.
    """

    high_temperature = engine_temp >= 100

    low_fuel = fuel <= 15

    high_mileage = odometer >= 100000

    aggressive_driving = speed >= 100

    maintenance_score = 100

    if high_temperature:
        maintenance_score -= 30

    if low_fuel:
        maintenance_score -= 10

    if high_mileage:
        maintenance_score -= 25

    if aggressive_driving:
        maintenance_score -= 20

    maintenance_score = max(
        maintenance_score,
        0,
    )

    return {
        "fuel": fuel,
        "engine_temp": engine_temp,
        "odometer": odometer,
        "speed": speed,
        "high_temperature": high_temperature,
        "low_fuel": low_fuel,
        "high_mileage": high_mileage,
        "aggressive_driving": aggressive_driving,
        "maintenance_score": maintenance_score,
        "timestamp": datetime.utcnow(),
    }
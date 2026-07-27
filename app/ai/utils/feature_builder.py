from datetime import datetime, UTC


def build_features(
    speed: float,
    previous_speed: float = 0.0,
    timestamp: datetime | None = None,
) -> dict:
    """
    Build ML features from incoming telemetry.
    """

    if timestamp is None:
        timestamp = datetime.now(UTC)

    hour = timestamp.hour
    day = timestamp.day
    month = timestamp.month
    day_of_week = timestamp.weekday()
    week_of_year = int(timestamp.strftime("%U"))

    is_weekend = day_of_week >= 5

    is_night = (
        hour >= 20
        or hour < 6
    )

    speed_change = speed - previous_speed

    acceleration = speed_change

    is_moving = speed > 0

    is_speeding = speed >= 100

    speed_normalized = speed / 100.0

    return {
        "hour": hour,
        "day": day,
        "month": month,
        "day_of_week": day_of_week,
        "week_of_year": week_of_year,
        "is_weekend": is_weekend,
        "is_night": is_night,
        "previous_speed": previous_speed,
        "speed_change": speed_change,
        "acceleration": acceleration,
        "is_moving": is_moving,
        "is_speeding": is_speeding,
        "speed_normalized": speed_normalized,
    }
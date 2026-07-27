from enum import Enum


class AnomalyType(str, Enum):
    """
    Supported anomaly categories.
    """

    OVER_SPEED = "OVER_SPEED"

    HIGH_ENGINE_TEMP = "HIGH_ENGINE_TEMP"

    LOW_FUEL = "LOW_FUEL"

    RAPID_ACCELERATION = "RAPID_ACCELERATION"

    ENGINE_RUNNING_WITHOUT_IGNITION = (
        "ENGINE_RUNNING_WITHOUT_IGNITION"
    )

    VEHICLE_MOVING_ENGINE_OFF = (
        "VEHICLE_MOVING_ENGINE_OFF"
    )

    POOR_HEALTH = "POOR_HEALTH"
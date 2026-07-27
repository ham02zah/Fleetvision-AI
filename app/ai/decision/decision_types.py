from enum import Enum


class DecisionPriority(str, Enum):
    LOW = "LOW"
    MEDIUM = "MEDIUM"
    HIGH = "HIGH"
    CRITICAL = "CRITICAL"


class VehicleDecision(str, Enum):
    CONTINUE = "CONTINUE DRIVING"
    SCHEDULE_SERVICE = "SCHEDULE SERVICE"
    REDUCE_SPEED = "REDUCE SPEED"
    INSPECT_ENGINE = "INSPECT ENGINE"
    STOP_IMMEDIATELY = "STOP VEHICLE IMMEDIATELY"
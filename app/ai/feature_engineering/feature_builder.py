from datetime import datetime


class FeatureBuilder:
    """
    Converts raw telemetry into ML features.
    """

    @staticmethod
    def build(
        *,
        telemetry,
        previous_speed: float,
    ):

        acceleration = (
            telemetry.speed - previous_speed
        )

        overspeed = (
            telemetry.speed >= 120
        )

        low_fuel = (
            telemetry.fuel <= 15
        )

        overheating = (
            telemetry.engine_temp >= 110
        )

        ignition_conflict = (
            telemetry.engine_running
            and
            not telemetry.ignition
        )

        hour = datetime.utcnow().hour

        return {

            "speed": telemetry.speed,

            "fuel": telemetry.fuel,

            "engine_temp": telemetry.engine_temp,

            "odometer": telemetry.odometer,

            "acceleration": acceleration,

            "overspeed": int(overspeed),

            "low_fuel": int(low_fuel),

            "overheating": int(overheating),

            "ignition_conflict": int(
                ignition_conflict
            ),

            "hour": hour,

        }
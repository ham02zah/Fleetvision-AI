class PredictionValidator:
    """
    Validate prediction inputs.
    """

    @staticmethod
    def validate(
        speed,
        previous_speed,
    ):

        if speed is None:
            raise ValueError("speed cannot be None")

        if previous_speed is None:
            raise ValueError(
                "previous_speed cannot be None"
            )

        speed = float(speed)
        previous_speed = float(previous_speed)

        if speed < 0:

            raise ValueError(
                "speed must be positive"
            )

        if speed > 300:

            raise ValueError(
                "speed exceeds maximum"
            )

        if previous_speed < 0:

            raise ValueError(
                "previous_speed must be positive"
            )

        return speed, previous_speed
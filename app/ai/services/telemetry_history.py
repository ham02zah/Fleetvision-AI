class TelemetryHistory:

    """
    Stores previous telemetry values.

    Temporary in-memory cache.
    """

    _history = {}

    @classmethod
    def get_previous_speed(
        cls,
        vehicle_id,
    ):

        return cls._history.get(
            vehicle_id,
            0.0,
        )

    @classmethod
    def update(
        cls,
        vehicle_id,
        speed,
    ):

        cls._history[vehicle_id] = speed
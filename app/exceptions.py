class FleetAlreadyExistsError(Exception):
    """
    Raised when a fleet with the same name already exists.
    """

    def __init__(self):
        super().__init__(
            "Fleet with this name already exists."
        )


class FleetNotFoundError(Exception):
    """
    Raised when a fleet cannot be found.
    """

    def __init__(self):
        super().__init__(
            "Fleet not found."
        )


class FleetInactiveError(Exception):
    """
    Raised when an inactive fleet is used.
    """

    def __init__(self):
        super().__init__(
            "Fleet is inactive."
        )
from app.exceptions.base import FleetVisionException


class FleetAlreadyExistsError(FleetVisionException):
    """
    Raised when a fleet with the same name already exists.
    """

    def __init__(self):
        super().__init__(
            message="Fleet with this name already exists.",
            status_code=409,
        )


class FleetNotFoundError(FleetVisionException):
    """
    Raised when a fleet cannot be found.
    """

    def __init__(self):
        super().__init__(
            message="Fleet not found.",
            status_code=404,
        )


class FleetInactiveError(FleetVisionException):
    """
    Raised when a fleet is inactive.
    """

    def __init__(self):
        super().__init__(
            message="Fleet is inactive.",
            status_code=400,
        )
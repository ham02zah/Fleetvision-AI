from __future__ import annotations


class FleetVisionException(Exception):
    """
    Base exception for the FleetVision application.
    """

    default_message = "FleetVision error."

    def __init__(self, message: str | None = None):
        self.message = message or self.default_message
        super().__init__(self.message)
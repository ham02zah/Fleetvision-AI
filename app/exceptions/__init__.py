from app.exceptions.base import FleetVisionException

from app.exceptions.user import (
    InvalidCredentialsError,
    UserAlreadyExistsError,
    UserInactiveError,
    UserNotFoundError,
)

from app.exceptions.fleet import (
    FleetAlreadyExistsError,
    FleetNotFoundError,
    FleetInactiveError,
)

__all__ = [
    "FleetVisionException",

    "UserAlreadyExistsError",
    "UserNotFoundError",
    "InvalidCredentialsError",
    "UserInactiveError",

    "FleetAlreadyExistsError",
    "FleetNotFoundError",
    "FleetInactiveError",
]
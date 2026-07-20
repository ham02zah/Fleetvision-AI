from __future__ import annotations

from app.exceptions.base import FleetVisionException


class UserAlreadyExistsError(FleetVisionException):
    default_message = "A user with this email already exists."


class UserNotFoundError(FleetVisionException):
    default_message = "User not found."


class InvalidCredentialsError(FleetVisionException):
    default_message = "Invalid email or password."


class UserInactiveError(FleetVisionException):
    default_message = "This account has been deactivated."
from __future__ import annotations

from datetime import datetime, UTC

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

from app.exceptions import (
    InvalidCredentialsError,
    UserAlreadyExistsError,
    UserInactiveError,
    UserNotFoundError,
)

from app.exceptions import (
    FleetAlreadyExistsError,
    FleetNotFoundError,
)


def _error_response(
    *,
    status_code: int,
    error_type: str,
    message: str,
):
    return JSONResponse(
        status_code=status_code,
        content={
            "success": False,
            "error": {
                "type": error_type,
                "message": message,
            },
            "timestamp": datetime.now(
                UTC
            ).isoformat(),
        },
    )


def register_exception_handlers(
    app: FastAPI,
):
    @app.exception_handler(
        UserNotFoundError
    )
    async def user_not_found(
        request: Request,
        exc: UserNotFoundError,
    ):
        return _error_response(
            status_code=404,
            error_type="UserNotFound",
            message=str(exc),
        )

    @app.exception_handler(
        UserAlreadyExistsError
    )
    async def user_exists(
        request: Request,
        exc: UserAlreadyExistsError,
    ):
        return _error_response(
            status_code=409,
            error_type="UserAlreadyExists",
            message=str(exc),
        )

    @app.exception_handler(
        InvalidCredentialsError
    )
    async def invalid_credentials(
        request: Request,
        exc: InvalidCredentialsError,
    ):
        return _error_response(
            status_code=401,
            error_type="InvalidCredentials",
            message=str(exc),
        )

    @app.exception_handler(
        UserInactiveError
    )
    async def inactive_user(
        request: Request,
        exc: UserInactiveError,
    ):
        return _error_response(
            status_code=403,
            error_type="InactiveUser",
            message=str(exc),
        )

    @app.exception_handler(
        HTTPException
    )
    async def http_exception(
        request: Request,
        exc: HTTPException,
    ):
        return _error_response(
            status_code=exc.status_code,
            error_type="HTTPException",
            message=str(exc.detail),
        )

    @app.exception_handler(
        Exception
    )
    async def internal_error(
        request: Request,
        exc: Exception,
    ):
        return _error_response(
            status_code=500,
            error_type="InternalServerError",
            message="Unexpected server error.",
        )
    
    @app.exception_handler(
        FleetAlreadyExistsError
    )
    async def fleet_exists(
        request: Request,
        exc: FleetAlreadyExistsError,
    ):
        return _error_response(
            status_code=409,
            error_type="FleetAlreadyExists",
            message=str(exc),
        )

    @app.exception_handler(
        FleetNotFoundError
    )
    async def fleet_not_found(
        request: Request,
        exc: FleetNotFoundError,
    ):
        return _error_response(
            status_code=404,
            error_type="FleetNotFound",
            message=str(exc),
        )
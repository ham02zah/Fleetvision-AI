from __future__ import annotations

from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.v1.api import api_router
from app.core.config import settings
from app.core.exception_handlers import register_exception_handlers
from app.core.logging import logger
from app.core.openapi import tags_metadata


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Application lifecycle.
    """
    logger.info("FleetVision AI starting...")

    yield

    logger.info("FleetVision AI shutting down...")


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="""
FleetVision AI Backend

Enterprise fleet intelligence platform.

## Features

- JWT Authentication
- User Management
- Fleet Management
- Driver Monitoring
- Vehicle Telemetry
- Predictive Maintenance
- AI Anomaly Detection
- REST API
- PostgreSQL
- Redis
- Docker
- Kubernetes
""",
    debug=settings.DEBUG,
    lifespan=lifespan,
    openapi_tags=tags_metadata,
)

register_exception_handlers(app)


@app.get(
    "/",
    tags=["System"],
    summary="Root Endpoint",
)
async def root():
    return {
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "running",
    }


@app.get(
    "/health",
    tags=["System"],
    summary="Health Check",
)
async def health_check():
    return {
        "status": "healthy",
        "application": settings.APP_NAME,
    }


# Register all API v1 routes
app.include_router(
    api_router,
    prefix="/api/v1",
)
from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.v1.api import api_router
from app.core.config import settings
from app.core.exception_handlers import register_exception_handlers
from app.core.logging import logger
from app.core.openapi import tags_metadata


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("FleetVision AI starting...")
    yield
    logger.info("FleetVision AI shutting down...")


app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
    description="FleetVision AI Backend",
    debug=settings.DEBUG,
    lifespan=lifespan,
    openapi_tags=tags_metadata,
)

register_exception_handlers(app)

app.include_router(
    api_router,
    prefix="/api/v1",
)


@app.get("/")
async def root():
    return {
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "running",
    }


@app.get("/health")
async def health():
    return {
        "status": "healthy",
    }


if __name__ == "__main__":
    print("\n===== ROUTES =====")
    for route in app.routes:
        if hasattr(route, "path"):
            print(route.path)
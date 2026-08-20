from fastapi.middleware.cors import CORSMiddleware
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

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

register_exception_handlers(app)


# ============================================================
# API V1
# ============================================================

app.include_router(
    api_router,
    prefix="/api/v1",
)


# ============================================================
# ROOT
# ============================================================

@app.get("/")
async def root():
    return {
        "application": settings.APP_NAME,
        "version": settings.APP_VERSION,
        "status": "running",
    }


# ============================================================
# HEALTH
# ============================================================

@app.get("/health")
async def health():
    return {
        "status": "healthy",
    }


if __name__ == "__main__":
    print("\n===== ROUTES =====")

    for route in app.routes:
        if hasattr(route, "path"):
            print(
                getattr(route, "methods", None),
                route.path,
            )
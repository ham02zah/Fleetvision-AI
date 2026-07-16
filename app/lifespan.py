from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.core.logger import logger


@asynccontextmanager
async def lifespan(app: FastAPI):

    logger.info("FleetVision AI starting...")

    yield

    logger.info("FleetVision AI shutting down...")
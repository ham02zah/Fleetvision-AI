from fastapi import APIRouter

from app.api.v1.ai.router import router as ai_router
from app.api.v1.telemetry.router import router as telemetry_router

router = APIRouter()

router.include_router(ai_router)
router.include_router(telemetry_router)
from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.dependencies import get_db

router = APIRouter()


@router.get("/database", tags=["Database"])
async def database_health(
    db: Session = Depends(get_db),
):
    """
    Simple endpoint to verify that dependency injection
    is working correctly.

    A real SQL query will be added in the next step.
    """

    return {
        "message": "Database session created successfully"
    }
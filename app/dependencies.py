from collections.abc import Generator

from sqlalchemy.orm import Session

from app.database.session import SessionLocal


def get_db() -> Generator[Session, None, None]:
    """
    Create a database session for each request.

    The session is automatically closed after the request
    finishes, even if an exception occurs.
    """
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()
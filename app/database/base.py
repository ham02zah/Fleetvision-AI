from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    """
    Base class for every SQLAlchemy model.

    Example:

    class User(Base):
        ...

    """
    pass
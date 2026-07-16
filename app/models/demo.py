from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.database.base_model import BaseModel


class Demo(BaseModel):

    __tablename__ = "demo"

    name: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
    )
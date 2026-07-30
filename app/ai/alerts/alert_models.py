from dataclasses import dataclass
from datetime import datetime


@dataclass
class AIAlert:

    level: str

    category: str

    title: str

    message: str

    timestamp: str

    vehicle_id: str

    @staticmethod
    def create(

        vehicle_id,

        level,

        category,

        title,

        message,

    ):

        return AIAlert(

            vehicle_id=vehicle_id,

            level=level,

            category=category,

            title=title,

            message=message,

            timestamp=datetime.utcnow().isoformat(),

        )
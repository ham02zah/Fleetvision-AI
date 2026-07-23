import json

import redis

from app.core.config import settings


class RedisService:
    def __init__(self):
        self.redis = redis.Redis(
            host=settings.REDIS_HOST,
            port=settings.REDIS_PORT,
            decode_responses=True,
        )

    def publish_vehicle_data(
        self,
        payload: dict,
    ):
        self.redis.xadd(
            "vehicle_stream",
            {
                "vehicle_id": str(payload["vehicle_id"]),
                "data": json.dumps(payload),
            },
        )

    def read_stream(
        self,
        last_id="0",
    ):
        return self.redis.xread(
            {
                "vehicle_stream": last_id,
            },
            count=50,
            block=1000,
        )
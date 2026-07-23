import json
import time

from app.database.session import SessionLocal
from app.services.redis_service import RedisService
from app.services.vehicle_status_service import VehicleStatusService

redis_service = RedisService()

last_id = "0"

print("=" * 60)
print("FleetVision Stream Worker Started")
print("=" * 60)

while True:

    db = SessionLocal()

    try:

        messages = redis_service.read_stream(last_id)

        if messages:

            service = VehicleStatusService(db)

            for stream_name, entries in messages:

                for message_id, data in entries:

                    last_id = message_id

                    payload = json.loads(data["data"])

                    service.upsert_vehicle_status(payload)

                    print(
                        f"✓ Updated vehicle {payload['vehicle_id']} "
                        f"| Speed: {payload['speed']} km/h"
                    )

    except Exception as e:

        print(f"Worker Error: {e}")

    finally:

        db.close()

    time.sleep(0.2)
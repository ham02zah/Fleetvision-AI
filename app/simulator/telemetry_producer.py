import random
import time
from uuid import uuid4

from sqlalchemy.orm import Session

from app.database.session import SessionLocal
from app.models.vehicle import Vehicle
from app.services.redis_service import RedisService

redis_service = RedisService()

db: Session = SessionLocal()

vehicles = db.query(Vehicle).all()

if not vehicles:
    raise Exception(
        "No vehicles found. Please create at least one vehicle before running the simulator."
    )

vehicle_ids = [str(vehicle.id) for vehicle in vehicles]

print("=" * 60)
print(f"Loaded {len(vehicle_ids)} vehicle(s)")
print("=" * 60)

while True:

    telemetry = {
        "vehicle_id": random.choice(vehicle_ids),
        "latitude": round(random.uniform(24.85, 24.95), 6),
        "longitude": round(random.uniform(67.00, 67.20), 6),
        "speed": random.randint(40, 120),
        "heading": random.randint(0, 359),
        "ignition": True,
        "engine_running": True,
        "fuel": random.randint(15, 100),
        "engine_temp": random.randint(75, 110),
        "odometer": random.randint(10000, 90000),
        "trip_id": str(uuid4()),
    }

    redis_service.publish_vehicle_data(telemetry)

    print("Published:", telemetry)

    time.sleep(2)
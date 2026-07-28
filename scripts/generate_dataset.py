import random
import uuid
from datetime import datetime, timedelta
from pathlib import Path

import pandas as pd


TOTAL_RECORDS = 10000

TOTAL_VEHICLES = 100

OUTPUT = Path("datasets/raw/vehicle_status.csv")


random.seed(42)


states = [
    "MOVING",
    "IDLE",
    "PARKED",
]


base_time = datetime.utcnow()


rows = []


for _ in range(TOTAL_RECORDS):

    vehicle_id = str(uuid.uuid4())

    speed = round(
        random.uniform(0, 140),
        2,
    )

    ignition = speed > 0

    engine_running = ignition

    state = random.choices(
        states,
        weights=[70, 20, 10],
    )[0]

    latitude = round(
        random.uniform(24.75, 25.10),
        6,
    )

    longitude = round(
        random.uniform(66.90, 67.30),
        6,
    )

    heading = random.randint(
        0,
        359,
    )

    timestamp = (
        base_time
        -
        timedelta(
            seconds=random.randint(
                0,
                86400,
            )
        )
    )

    rows.append(
        {

            "id": str(uuid.uuid4()),

            "vehicle_id": vehicle_id,

            "latitude": latitude,

            "longitude": longitude,

            "speed": speed,

            "heading": heading,

            "ignition": ignition,

            "engine_running": engine_running,

            "state": state,

            "last_seen": timestamp,

            "created_at": timestamp,

            "updated_at": timestamp,

        }
    )


df = pd.DataFrame(rows)

OUTPUT.parent.mkdir(
    parents=True,
    exist_ok=True,
)

df.to_csv(
    OUTPUT,
    index=False,
)

print()

print("=" * 60)

print("DATASET CREATED")

print("=" * 60)

print()

print("Rows :", len(df))

print("Vehicles :", df["vehicle_id"].nunique())

print()

print(df.head())
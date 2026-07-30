import sys
from pathlib import Path

sys.path.append(
    str(
        Path(__file__).resolve().parents[1]
    )
)

from app.models.telemetry import Telemetry

from app.ai.services.telemetry_ai_service import (
    TelemetryAIService,
)

from app.ai.services.telemetry_history import (
    TelemetryHistory,
)


telemetry_stream = [

    {
        "vehicle_id": "truck_01",
        "speed": 45,
    },

    {
        "vehicle_id": "truck_01",
        "speed": 72,
    },

    {
        "vehicle_id": "truck_01",
        "speed": 115,
    },

    {
        "vehicle_id": "truck_01",
        "speed": 130,
    },

]

for item in telemetry_stream:

    previous_speed = (
        TelemetryHistory.get_previous_speed(
            item["vehicle_id"]
        )
    )

    telemetry = Telemetry(

        vehicle_id=item["vehicle_id"],

        latitude=24.86,

        longitude=67.01,

        speed=item["speed"],

        heading=180,

        ignition=1,

        engine_running=1,

        fuel=70,

        engine_temp=90,

        odometer=55000,

    )

    result = TelemetryAIService.analyze(

        telemetry=telemetry,

        previous_speed=previous_speed,

    )

    print()

    print("=" * 60)

    print(
        "Speed:",
        item["speed"],
    )

    print(
        "Previous:",
        previous_speed,
    )

    print()

    print(result)

    TelemetryHistory.update(

        item["vehicle_id"],

        item["speed"],

    )
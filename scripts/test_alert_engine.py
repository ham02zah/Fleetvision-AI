import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from app.models.telemetry import Telemetry

from app.ai.services.telemetry_ai_service import TelemetryAIService


telemetry = Telemetry(

    vehicle_id="truck_01",

    latitude=24.86,

    longitude=67.01,

    speed=130,

    heading=180,

    ignition=1,

    engine_running=1,

    fuel=18,

    engine_temp=112,

    odometer=95000,

)

result = TelemetryAIService.analyze(

    telemetry=telemetry,

    previous_speed=90,

)

print()

print("=" * 60)

print("AI RESULT")

print("=" * 60)

print(result["analysis"])

print()

print("=" * 60)

print("ALERTS")

print("=" * 60)

for alert in result["alerts"]:

    print(alert)
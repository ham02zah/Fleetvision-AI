import sys
from pathlib import Path

# Add project root to Python path
sys.path.append(
    str(Path(__file__).resolve().parents[1])
)


from app.ai.intelligence.intelligence_service import (
    AIIntelligenceService,
)

from app.models.telemetry import Telemetry



telemetry = Telemetry(

    speed=95,

    fuel=60,

    engine_temp=85,

    odometer=45000,

    latitude=24.8607,

    longitude=67.0011,

    ignition=1,

    engine_running=1,

)


result = AIIntelligenceService.analyze(
    telemetry=telemetry,
    previous_speed=70,
)


print("=" * 60)

print("AI INTELLIGENCE RESULT")

print("=" * 60)


for key, value in result.items():

    print("\n")
    print(key)

    print(value)
import requests
import json

BASE = "http://127.0.0.1:8000/api/v1/ai"

tests = [
    (
        "/predict-speed",
        {
            "speed": 60,
            "previous_speed": 55
        }
    ),
    (
        "/detect-risk",
        {
            "speed": 130,
            "previous_speed": 70
        }
    ),
    (
        "/analyze",
        {
            "speed": 145,
            "previous_speed": 80,
            "fuel": 8,
            "engine_temp": 121,
            "odometer": 220000,
            "latitude": 33.6844,
            "longitude": 73.0479,
            "heading": 180,
            "ignition": True,
            "engine_running": True
        }
    )
]

for endpoint, payload in tests:
    print("=" * 80)
    print(endpoint)
    response = requests.post(BASE + endpoint, json=payload)
    print("Status:", response.status_code)
    print(json.dumps(response.json(), indent=4))
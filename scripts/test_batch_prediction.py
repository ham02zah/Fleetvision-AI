import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

from app.ai.inference.batch_predictor import BatchPredictor

records = [
    {
        "speed": 45,
        "previous_speed": 40,
    },
    {
        "speed": 90,
        "previous_speed": 80,
    },
    {
        "speed": 125,
        "previous_speed": 118,
    },
]

results = BatchPredictor.predict(records)

for result in results:
    print(result)
from pathlib import Path
from datetime import datetime
import json


LOG_FILE = Path("logs/predictions.log")

LOG_FILE.parent.mkdir(
    parents=True,
    exist_ok=True,
)


class PredictionLogger:

    @staticmethod
    def log(result):

        record = {

            "timestamp": datetime.utcnow().isoformat(),

            "prediction": result,

        }

        with open(
            LOG_FILE,
            "a",
        ) as file:

            file.write(
                json.dumps(record)
            )

            file.write("\n")
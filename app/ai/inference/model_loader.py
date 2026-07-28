from pathlib import Path

import joblib


_speed_model = None


def load_speed_model():

    global _speed_model

    if _speed_model is not None:

        return _speed_model

    latest_file = Path("models/latest.txt")

    if latest_file.exists():

        version = latest_file.read_text().strip()

        model_path = (
            Path("models")
            / version
            / "model.pkl"
        )

    else:

        model_path = Path(
            "models/speed_prediction_model.pkl"
        )

    _speed_model = joblib.load(model_path)

    print()

    print("Loaded Model")

    print(model_path)

    print()

    return _speed_model
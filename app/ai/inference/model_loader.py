from pathlib import Path

import joblib


MODEL_PATH = Path("models/speed_prediction_model.pkl")

_speed_model = None


def load_speed_model():
    """
    Load the trained speed prediction model once
    and keep it cached in memory.
    """

    global _speed_model

    if _speed_model is None:

        if not MODEL_PATH.exists():
            raise FileNotFoundError(
                f"Speed model not found: {MODEL_PATH}"
            )

        _speed_model = joblib.load(MODEL_PATH)

        print("✓ Speed prediction model loaded.")

    return _speed_model
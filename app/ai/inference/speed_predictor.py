from datetime import datetime

import pandas as pd

from app.ai.inference.model_loader import load_speed_model
from app.ai.utils.feature_builder import build_features


def predict_speed(
    speed: float,
    previous_speed: float = 0.0,
    timestamp: datetime | None = None,
):
    """
    Predict next vehicle speed.
    """

    model = load_speed_model()

    features = build_features(
        speed=speed,
        previous_speed=previous_speed,
        timestamp=timestamp,
    )

    X = pd.DataFrame(
        [[
            features["hour"],
            features["day"],
            features["month"],
            features["day_of_week"],
            features["week_of_year"],
            features["is_weekend"],
            features["is_night"],
            features["previous_speed"],
            features["speed_change"],
            features["acceleration"],
            features["is_moving"],
            features["is_speeding"],
            features["speed_normalized"],
        ]],
        columns=model.feature_names_in_,
    )

    prediction = float(model.predict(X)[0])

    return {
        "current_speed": speed,
        "predicted_speed": round(prediction, 2),
        "speed_difference": round(prediction - speed, 2),
        "overspeed": prediction >= 100,
        "risk_level": (
            "HIGH"
            if prediction >= 100
            else "MEDIUM"
            if prediction >= 80
            else "LOW"
        ),
    }
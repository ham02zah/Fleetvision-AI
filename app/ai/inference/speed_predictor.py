import pandas as pd

from app.ai.inference.model_loader import load_speed_model
from app.ai.inference.prediction_logger import PredictionLogger
from app.ai.inference.prediction_validator import PredictionValidator


def predict_speed(
    speed,
    previous_speed,
):

    speed, previous_speed = PredictionValidator.validate(
        speed,
        previous_speed,
    )

    model = load_speed_model()

    sample = pd.DataFrame(
        [
            {
                "latitude": 25.0,
                "longitude": 67.0,
                "heading": 180,

                "ignition": 1,
                "engine_running": 1,
                "state": 1,

                "hour": 12,
                "minute": 0,
                "day": 1,
                "month": 1,

                "day_of_week": 1,
                "week_of_year": 1,

                "is_weekend": 0,
                "is_night": 0,

                "previous_speed": previous_speed,

                "speed_change": speed - previous_speed,

                "acceleration": speed - previous_speed,

                "is_moving": int(speed > 0),

                "is_speeding": int(speed >= 100),

                "speed_normalized": speed / 140,

                "speed_category_encoded": (
                    4
                    if speed >= 90
                    else 3
                    if speed >= 60
                    else 2
                    if speed >= 30
                    else 1
                    if speed > 0
                    else 0
                ),
            }
        ]
    )

    # Keep only the columns the trained model expects,
    # in the correct order.
    sample = sample.reindex(
        columns=model.feature_names_in_,
        fill_value=0,
    )

    prediction = float(model.predict(sample)[0])

    difference = round(
        prediction - speed,
        2,
    )

    if prediction >= 100:
        risk = "HIGH"
    elif prediction >= 70:
        risk = "MEDIUM"
    else:
        risk = "LOW"

    result = {
        "current_speed": speed,
        "predicted_speed": round(prediction, 2),
        "speed_difference": difference,
        "overspeed": prediction >= 100,
        "risk_level": risk,
    }

    PredictionLogger.log(result)

    return result
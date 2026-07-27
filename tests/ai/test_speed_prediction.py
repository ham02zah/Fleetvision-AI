from app.ai.inference.speed_predictor import predict_speed


def test_speed_prediction():

    result = predict_speed(
        speed=120,
        previous_speed=100,
    )

    assert isinstance(result, dict)

    assert "predicted_speed" in result

    assert "risk_level" in result

    assert result["current_speed"] == 120
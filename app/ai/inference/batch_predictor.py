from app.ai.inference.speed_predictor import (
    predict_speed,
)


class BatchPredictor:

    @staticmethod
    def predict(records):

        predictions = []

        for record in records:

            predictions.append(

                predict_speed(

                    speed=record["speed"],

                    previous_speed=record[
                        "previous_speed"
                    ],

                )

            )

        return predictions
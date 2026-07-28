from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)

import numpy as np


class ModelEvaluator:

    @staticmethod
    def evaluate(model, X_test, y_test):

        predictions = model.predict(X_test)

        mae = mean_absolute_error(
            y_test,
            predictions,
        )

        rmse = np.sqrt(
            mean_squared_error(
                y_test,
                predictions,
            )
        )

        r2 = r2_score(
            y_test,
            predictions,
        )

        mape = (
            np.mean(
                np.abs(
                    (y_test - predictions)
                    / np.maximum(y_test, 1)
                )
            )
            * 100
        )

        return {

            "predictions": predictions,

            "MAE": round(mae, 3),

            "RMSE": round(rmse, 3),

            "R2": round(r2, 3),

            "MAPE": round(mape, 2),

        }
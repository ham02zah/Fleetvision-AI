from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)

import numpy as np


class ModelEvaluator:
    """
    Evaluates trained model.
    """

    @staticmethod
    def evaluate(

        model,

        X_test,

        y_test,

    ):

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

        return {

            "MAE": round(mae, 2),

            "RMSE": round(rmse, 2),

            "R2": round(r2, 4),

        }
from app.ai.training.hyperparameter_tuner import (
    HyperparameterTuner,
)


class ModelTrainer:
    """
    Train the optimized ML model.
    """

    @staticmethod
    def train(
        X_train,
        y_train,
    ):

        return HyperparameterTuner.tune(

            X_train,

            y_train,

        )
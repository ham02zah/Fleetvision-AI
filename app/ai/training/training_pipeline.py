from app.ai.training.data_loader import DataLoader
from app.ai.training.dataset_splitter import DatasetSplitter
from app.ai.training.model_trainer import ModelTrainer
from app.ai.training.model_evaluator import ModelEvaluator
from app.ai.training.model_saver import ModelSaver
from app.ai.evaluation.evaluation_pipeline import (EvaluationPipeline,)
from app.ai.versioning.model_version import (ModelVersion,)


class TrainingPipeline:
    """
    Complete ML Training Pipeline.
    """

    @staticmethod
    def run():

        print("\nLoading dataset...")

        df = DataLoader.load(
            "datasets/processed/vehicle_features.csv"
        )

        print(df.head())

        X_train, X_test, y_train, y_test = DatasetSplitter.split(df)

        print("\n================================")
        print("HYPERPARAMETER OPTIMIZATION")
        print("================================")

        model = ModelTrainer.train(
            X_train,
            y_train,
        )

        print("\nOptimization completed.")

        print("\nEvaluating...")

        metrics = EvaluationPipeline.run(
        model,
        X_test,
        y_test,
        )

        print(metrics)

        ModelSaver.save(
        model,
        "models/speed_prediction_model.pkl",
       )

        ModelVersion.save(
        model,
        metrics,
        )

        print("\nTraining completed.")

        return metrics
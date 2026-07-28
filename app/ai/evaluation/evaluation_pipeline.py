from app.ai.evaluation.model_evaluator import (
    ModelEvaluator,
)

from app.ai.evaluation.feature_importance import (
    FeatureImportance,
)

from app.ai.evaluation.visualization import (
    Visualization,
)


class EvaluationPipeline:

    @staticmethod
    def run(
        model,
        X_test,
        y_test,
    ):

        metrics = ModelEvaluator.evaluate(

            model,

            X_test,

            y_test,

        )

        FeatureImportance.save(

            model,

            X_test.columns,

        )

        Visualization.save_predictions(

            y_test,

            metrics["predictions"],

        )

        serializable_metrics = {
        key: value
        for key, value in metrics.items()
        if key != "predictions"
        }

        return serializable_metrics
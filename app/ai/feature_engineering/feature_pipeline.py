from app.ai.feature_engineering.feature_builder import (
    FeatureBuilder,
)

from app.ai.feature_engineering.feature_scaler import (
    FeatureScaler,
)

from app.ai.feature_engineering.feature_validator import (
    FeatureValidator,
)


class FeaturePipeline:
    """
    Complete feature engineering pipeline.
    """

    @staticmethod
    def process(
        *,
        telemetry,
        previous_speed,
    ):

        features = FeatureBuilder.build(
            telemetry=telemetry,
            previous_speed=previous_speed,
        )

        features = FeatureScaler.scale(
            features
        )

        features = FeatureValidator.validate(
            features
        )

        return features
import pandas as pd

from app.ai.feature_engineering.feature_generator import (
    FeatureGenerator,
)

from app.ai.feature_engineering.feature_validator import (
    FeatureValidator,
)


class FeaturePipeline:
    """
    Central feature engineering pipeline.

    Converts telemetry into ML-ready features.
    """


    @staticmethod
    def process(
        telemetry,
        previous_speed=0.0,
    ):
        """
        Generate engineered telemetry features.
        """


        # Create dataframe
        df = pd.DataFrame(
            [
                {

                    "latitude": telemetry.latitude,

                    "longitude": telemetry.longitude,

                    "speed": telemetry.speed,

                    "heading": telemetry.heading,

                    "ignition": int(
                        telemetry.ignition
                    ),

                    "engine_running": int(
                        telemetry.engine_running
                    ),

                    "previous_speed": previous_speed,

                    "speed_change":
                        telemetry.speed - previous_speed,

                    "acceleration":
                        telemetry.speed - previous_speed,


                    "is_moving": int(
                        telemetry.speed > 0
                    ),


                    "is_speeding": int(
                        telemetry.speed >= 100
                    ),

                }
            ]
        )


        # Validate dataframe

        df = FeatureValidator.validate(
            df
        )


        # Generate additional features

        df = FeatureGenerator.generate(
            df
        )


        # Return dictionary because
        # AIIntelligenceService returns JSON-like output

        features = df.to_dict(
        orient="records"
        )[0]

        features["feature_count"] = len(features)

        return features
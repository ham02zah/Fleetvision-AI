class FeatureValidator:
    """
    Ensures feature values are valid.
    """

    @staticmethod
    def validate(features):

        for key, value in features.items():

            if isinstance(
                value,
                float,
            ):

                if value < 0:

                    features[key] = 0.0

        return features
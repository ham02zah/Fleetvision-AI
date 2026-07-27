class FeatureScaler:
    """
    Normalize numerical values.
    """

    @staticmethod
    def scale(features):

        features["speed"] /= 200

        features["fuel"] /= 100

        features["engine_temp"] /= 150

        features["odometer"] /= 500000

        features["acceleration"] /= 100

        features["hour"] /= 24

        return features
import pandas as pd


class FeatureSelector:
    """
    Keeps only ML features.
    """

    @staticmethod
    def select(df: pd.DataFrame) -> pd.DataFrame:

        features = [

            "latitude",

            "longitude",

            "speed",

            "heading",

            "ignition",

            "engine_running",

            "overspeed",

            "overheating",

            "low_fuel",

            "ignition_conflict",

        ]

        existing = [
            c
            for c in features
            if c in df.columns
        ]

        return df[existing]
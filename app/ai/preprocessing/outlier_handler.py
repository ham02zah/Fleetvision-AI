import pandas as pd


class OutlierHandler:
    """
    Removes impossible telemetry values.
    """

    @staticmethod
    def clean(df: pd.DataFrame) -> pd.DataFrame:

        df = df.copy()

        if "speed" in df.columns:
            df = df[
                (df["speed"] >= 0)
                &
                (df["speed"] <= 220)
            ]

        if "latitude" in df.columns:
            df = df[
                (df["latitude"] >= -90)
                &
                (df["latitude"] <= 90)
            ]

        if "longitude" in df.columns:
            df = df[
                (df["longitude"] >= -180)
                &
                (df["longitude"] <= 180)
            ]

        return df
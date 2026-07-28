import pandas as pd


class Encoder:
    """
    Converts categorical values
    into ML-ready numeric values.
    """

    @staticmethod
    def encode(df: pd.DataFrame) -> pd.DataFrame:

        df = df.copy()

        boolean_columns = [
            "ignition",
            "engine_running",
        ]

        for column in boolean_columns:

            if column in df.columns:

                df[column] = (
                    df[column]
                    .astype(int)
                )

        if "state" in df.columns:

            mapping = {
                "moving": 1,
                "idle": 2,
                "parked": 3,
                "offline": 4,
            }

            df["state"] = (
                df["state"]
                .astype(str)
                .str.lower()
                .map(mapping)
            )

        return df
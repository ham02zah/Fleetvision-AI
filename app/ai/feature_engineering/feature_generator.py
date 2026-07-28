import pandas as pd


class FeatureGenerator:
    """
    Generates additional ML features from telemetry data.
    """

    @staticmethod
    def generate(df: pd.DataFrame) -> pd.DataFrame:
        """
        Create engineered features.
        """

        df = df.copy()

        # -------------------------
        # Overspeed Detection
        # -------------------------
        if "speed" in df.columns:
            df["overspeed"] = (
                df["speed"] > 120
            ).astype(int)

        # -------------------------
        # Engine Overheating
        # -------------------------
        if "engine_temp" in df.columns:
            df["overheating"] = (
                df["engine_temp"] > 110
            ).astype(int)

        # -------------------------
        # Low Fuel Warning
        # -------------------------
        if "fuel" in df.columns:
            df["low_fuel"] = (
                df["fuel"] < 15
            ).astype(int)

        # -------------------------
        # Ignition Conflict
        # -------------------------
        if (
            "engine_running" in df.columns
            and "ignition" in df.columns
        ):
            df["ignition_conflict"] = (
                (
                    df["engine_running"] == 1
                )
                &
                (
                    df["ignition"] == 0
                )
            ).astype(int)

        return df
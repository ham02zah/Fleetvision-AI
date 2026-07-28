from pathlib import Path

import numpy as np
import pandas as pd

from app.ai.preprocessing.preprocessing_pipeline import (
    PreprocessingPipeline,
)

RAW_DATASET = Path("datasets/raw/vehicle_status.csv")
OUTPUT_DATASET = Path("datasets/processed/vehicle_features.csv")


class FeaturePipeline:

    @staticmethod
    def run():

        print("\nLoading dataset...")

        df = pd.read_csv(RAW_DATASET)

        df["last_seen"] = pd.to_datetime(df["last_seen"])

        print("Running preprocessing...")

        df = PreprocessingPipeline.process(df)

        print("Generating time features...")

        df["hour"] = df["last_seen"].dt.hour
        df["minute"] = df["last_seen"].dt.minute
        df["day"] = df["last_seen"].dt.day
        df["month"] = df["last_seen"].dt.month
        df["day_of_week"] = df["last_seen"].dt.dayofweek
        df["week_of_year"] = (
            df["last_seen"]
            .dt.isocalendar()
            .week
            .astype(int)
        )

        df["is_weekend"] = (
            df["day_of_week"] >= 5
        ).astype(int)

        df["is_night"] = (
            ((df["hour"] >= 20) | (df["hour"] < 6))
        ).astype(int)

        print("Generating speed features...")

        df = df.sort_values(
            ["vehicle_id", "last_seen"]
        )

        df["previous_speed"] = (
            df.groupby("vehicle_id")["speed"]
            .shift(1)
            .fillna(0)
        )

        df["speed_change"] = (
            df["speed"] - df["previous_speed"]
        )

        df["acceleration"] = df["speed_change"]

        df["is_moving"] = (
            df["speed"] > 0
        ).astype(int)

        df["is_speeding"] = (
            df["speed"] >= 100
        ).astype(int)

        df["speed_normalized"] = (
            df["speed"] /
            max(df["speed"].max(), 1)
        )

        df["speed_category"] = np.select(
            [
                df["speed"] == 0,
                df["speed"] < 30,
                df["speed"] < 60,
                df["speed"] < 90,
                df["speed"] >= 90,
            ],
            [
                "Stopped",
                "Slow",
                "City",
                "Highway",
                "Overspeed",
            ],
            default="Unknown",
        )

        print("Encoding categorical features...")

        state_map = {
            "MOVING": 1,
            "IDLE": 2,
            "PARKED": 3,
            "OFFLINE": 4,
        }

        df["state"] = (
            df["state"]
            .astype(str)
            .str.upper()
            .map(state_map)
            .fillna(0)
            .astype(int)
        )

        speed_map = {
            "Stopped": 0,
            "Slow": 1,
            "City": 2,
            "Highway": 3,
            "Overspeed": 4,
            "Unknown": 5,
        }

        df["speed_category_encoded"] = (
            df["speed_category"]
            .map(speed_map)
            .astype(int)
        )

        print("Removing non-ML columns...")

        df = df.drop(
            columns=[
                "id",
                "vehicle_id",
                "last_seen",
                "created_at",
                "updated_at",
                "speed_category",
            ],
            errors="ignore",
        )

        OUTPUT_DATASET.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

        df.to_csv(
            OUTPUT_DATASET,
            index=False,
        )

        print("\nSaved dataset:")
        print(OUTPUT_DATASET)

        return df
from pathlib import Path

import numpy as np
import pandas as pd


RAW_DATASET = Path("datasets/raw/vehicle_status.csv")
OUTPUT_DATASET = Path("datasets/processed/vehicle_features.csv")


def load_dataset() -> pd.DataFrame:
    """
    Load raw telemetry dataset.
    """
    df = pd.read_csv(RAW_DATASET)

    df["last_seen"] = pd.to_datetime(df["last_seen"])

    return df


def create_time_features(
    df: pd.DataFrame,
) -> pd.DataFrame:
    """
    Create time-based ML features.
    """

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
    )

    df["is_night"] = (
        (df["hour"] >= 20)
        | (df["hour"] < 6)
    )

    return df

def create_speed_features(
    df: pd.DataFrame,
) -> pd.DataFrame:
    """
    Create speed-related ML features.
    """

    df = df.sort_values(
        ["vehicle_id", "last_seen"]
    )

    # Previous speed for each vehicle
    df["previous_speed"] = (
        df.groupby("vehicle_id")["speed"]
        .shift(1)
    )

    # Speed difference
    df["speed_change"] = (
        df["speed"] - df["previous_speed"]
    )

    df["speed_change"] = (
        df["speed_change"]
        .fillna(0)
    )

    # Estimated acceleration
    df["acceleration"] = df["speed_change"]

    # Vehicle moving?
    df["is_moving"] = df["speed"] > 0

    # Overspeed flag
    df["is_speeding"] = df["speed"] >= 100

    # Normalize speed (0–1)
    max_speed = max(
        df["speed"].max(),
        1,
    )

    df["speed_normalized"] = (
        df["speed"] / max_speed
    )

    # Speed categories
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

    return df

def save_dataset(
    df: pd.DataFrame,
):
    """
    Save processed dataset.
    """

    OUTPUT_DATASET.parent.mkdir(
        parents=True,
        exist_ok=True,
    )

    df.to_csv(
        OUTPUT_DATASET,
        index=False,
    )

    print(f"Saved: {OUTPUT_DATASET}")


def main():

    df = load_dataset()

    df = create_time_features(df)

    df = create_speed_features(df)

    print(df.head())

    save_dataset(df)

if __name__ == "__main__":
    main()
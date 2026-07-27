from pathlib import Path

import joblib
import pandas as pd

from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score,
)
from sklearn.model_selection import train_test_split


DATASET = Path("datasets/processed/vehicle_features.csv")
MODEL_DIR = Path("models")
MODEL_PATH = MODEL_DIR / "speed_prediction_model.pkl"


FEATURE_COLUMNS = [
    "hour",
    "day",
    "month",
    "day_of_week",
    "week_of_year",
    "is_weekend",
    "is_night",
    "previous_speed",
    "speed_change",
    "acceleration",
    "is_moving",
    "is_speeding",
    "speed_normalized",
]


TARGET_COLUMN = "speed"


def load_dataset() -> pd.DataFrame:
    """
    Load engineered dataset.
    """
    df = pd.read_csv(DATASET)

    return df


def preprocess(df: pd.DataFrame):
    """
    Prepare features.
    """
    df = df.copy()

    df["previous_speed"] = df["previous_speed"].fillna(0)

    X = df[FEATURE_COLUMNS]

    y = df[TARGET_COLUMN]

    return X, y


def train_model(X_train, y_train):
    """
    Train Random Forest model.
    """
    model = RandomForestRegressor(
        n_estimators=200,
        max_depth=12,
        random_state=42,
        n_jobs=-1,
    )

    model.fit(X_train, y_train)

    return model


def evaluate(model, X_test, y_test):
    """
    Evaluate model.
    """
    predictions = model.predict(X_test)

    mae = mean_absolute_error(
        y_test,
        predictions,
    )

    mse = mean_squared_error(
    y_test,
    predictions,
    )

    rmse = mse ** 0.5

    r2 = r2_score(
        y_test,
        predictions,
    )

    print("\nModel Evaluation")
    print("-" * 40)
    print(f"MAE  : {mae:.2f}")
    print(f"RMSE : {rmse:.2f}")
    print(f"R²   : {r2:.4f}")


def save_model(model):
    """
    Save trained model.
    """
    MODEL_DIR.mkdir(
        parents=True,
        exist_ok=True,
    )

    joblib.dump(
        model,
        MODEL_PATH,
    )

    print(f"\nModel saved to: {MODEL_PATH}")


def main():
    df = load_dataset()

    X, y = preprocess(df)

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42,
    )

    model = train_model(
        X_train,
        y_train,
    )

    evaluate(
        model,
        X_test,
        y_test,
    )

    save_model(model)


if __name__ == "__main__":
    main()
import os
import sys

sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "..",
        )
    )
)

import pandas as pd

from app.ai.feature_engineering.feature_pipeline import (
    FeaturePipeline,
)

print("=" * 60)
print("LOADING DATASET")
print("=" * 60)

df = pd.read_csv(
    "datasets/processed/vehicle_features.csv"
)

print(df.head())

print()

print("=" * 60)
print("GENERATING FEATURES")
print("=" * 60)

features = FeaturePipeline.process(df)

print(features.head())

print()

print("=" * 60)
print("FEATURE COLUMNS")
print("=" * 60)

print(features.columns.tolist())

print()

print("=" * 60)
print("SHAPE")
print("=" * 60)

print(features.shape)
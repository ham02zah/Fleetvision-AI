import sys
from pathlib import Path

# Add project root to Python path
ROOT = Path(__file__).resolve().parents[1]
sys.path.append(str(ROOT))

import pandas as pd

from app.ai.preprocessing.preprocessing_pipeline import (
    PreprocessingPipeline,
)

print("=" * 60)
print("LOADING DATASET")
print("=" * 60)

df = pd.read_csv("datasets/raw/vehicle_status.csv")

print(df.head())

print("\n")

print("=" * 60)
print("RUNNING PREPROCESSING")
print("=" * 60)

processed = PreprocessingPipeline.process(df)

print(processed.head())

print("\n")

print("=" * 60)
print("SHAPE")
print("=" * 60)

print(processed.shape)

print("\n")

print("=" * 60)
print("COLUMNS")
print("=" * 60)

print(processed.columns.tolist())
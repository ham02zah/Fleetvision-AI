import sys
from pathlib import Path

# Add project root to Python path
sys.path.append(str(Path(__file__).resolve().parents[1]))

import pandas as pd

from app.ai.preprocessing.preprocessing_pipeline import (
    PreprocessingPipeline,
)

print("=" * 60)
print("LOADING RAW DATASET")
print("=" * 60)

df = pd.read_csv("datasets/raw/vehicle_status.csv")

print(df.head())

print("\nRunning preprocessing pipeline...\n")

processed = PreprocessingPipeline.process(df)

output_path = "datasets/processed/vehicle_status_processed.csv"

processed.to_csv(
    output_path,
    index=False,
)

print("=" * 60)
print("SUCCESS")
print("=" * 60)

print(f"Processed dataset saved to:\n{output_path}")

print("\nShape:", processed.shape)

print("\nColumns:")

print(processed.columns.tolist())

print("\nPreview:")

print(processed.head())
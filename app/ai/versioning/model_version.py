import json
import shutil
from pathlib import Path

import joblib

from app.ai.versioning.metadata_builder import (
    MetadataBuilder,
)


class ModelVersion:

    ROOT = Path("models")


    @classmethod
    def save(
        cls,
        model,
        metrics,
    ):

        cls.ROOT.mkdir(
            exist_ok=True,
        )

        versions = [

            d

            for d in cls.ROOT.iterdir()

            if d.is_dir()

            and d.name.startswith("v")

        ]

        version_number = len(versions) + 1

        version_dir = cls.ROOT / f"v{version_number}"

        version_dir.mkdir()

        joblib.dump(

            model,

            version_dir / "model.pkl",

        )

        metadata = MetadataBuilder.build(
            metrics
        )

        with open(
            version_dir / "metadata.json",
            "w",
        ) as file:

            json.dump(
                metadata,
                file,
                indent=4,
            )

        with open(
            version_dir / "metrics.json",
            "w",
        ) as file:

            json.dump(
                metrics,
                file,
                indent=4,
            )

        feature_csv = cls.ROOT / "feature_importance.csv"

        if feature_csv.exists():

            shutil.copy(
                feature_csv,
                version_dir / "feature_importance.csv",
            )

        latest = cls.ROOT / "latest.txt"

        latest.write_text(
            f"v{version_number}"
        )

        print()

        print("=" * 60)

        print(f"Saved Version : v{version_number}")

        print(version_dir)

        print("=" * 60)

        return version_dir
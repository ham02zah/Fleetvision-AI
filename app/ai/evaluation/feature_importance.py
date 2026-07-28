from pathlib import Path

import pandas as pd


class FeatureImportance:

    @staticmethod
    def save(model, columns):

        importance = pd.DataFrame({

            "Feature": columns,

            "Importance": model.feature_importances_,

        })

        importance = importance.sort_values(
            by="Importance",
            ascending=False,
        )

        output = Path(
            "models/feature_importance.csv"
        )

        importance.to_csv(
            output,
            index=False,
        )

        print()

        print("Feature importance saved:")

        print(output)

        return importance
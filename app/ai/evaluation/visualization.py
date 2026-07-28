from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


class Visualization:

    @staticmethod
    def save_predictions(
        y_test,
        predictions,
    ):

        Path("models").mkdir(
            exist_ok=True
        )

        results = pd.DataFrame({

            "Actual": y_test,

            "Predicted": predictions,

        })

        results.to_csv(

            "models/predictions.csv",

            index=False,

        )

        plt.figure(figsize=(8, 6))

        plt.scatter(
            y_test,
            predictions,
        )

        plt.xlabel("Actual Speed")

        plt.ylabel("Predicted Speed")

        plt.title("Actual vs Predicted")

        plt.tight_layout()

        plt.savefig(

            "models/actual_vs_predicted.png"

        )

        plt.close()

        residuals = y_test - predictions

        plt.figure(figsize=(8, 6))

        plt.scatter(
            predictions,
            residuals,
        )

        plt.axhline(
            0,
            linestyle="--",
        )

        plt.xlabel("Predicted")

        plt.ylabel("Residual")

        plt.title("Residual Plot")

        plt.tight_layout()

        plt.savefig(

            "models/residual_plot.png"

        )

        plt.close()

        print()

        print("Evaluation graphs saved.")
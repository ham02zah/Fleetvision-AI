import joblib
import os


class ModelSaver:
    """
    Saves trained model.
    """

    @staticmethod
    def save(

        model,

        path,

    ):

        os.makedirs(

            os.path.dirname(path),

            exist_ok=True,

        )

        joblib.dump(

            model,

            path,

        )

        print(

            f"\nModel saved to:\n{path}"

        )
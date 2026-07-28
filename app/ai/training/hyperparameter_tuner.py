from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import GridSearchCV


class HyperparameterTuner:
    """
    Finds the best Random Forest model.
    """

    @staticmethod
    def tune(
        X_train,
        y_train,
    ):

        parameter_grid = {

            "n_estimators": [
                100,
                150,
                200,
            ],

            "max_depth": [
                None,
                10,
                20,
            ],

            "min_samples_split": [
                2,
                5,
            ],

            "min_samples_leaf": [
                1,
                2,
            ],

        }

        model = RandomForestRegressor(
            random_state=42,
            n_jobs=-1,
        )

        grid = GridSearchCV(

            estimator=model,

            param_grid=parameter_grid,

            cv=5,

            scoring="neg_mean_absolute_error",

            n_jobs=-1,

            verbose=2,

        )

        grid.fit(
            X_train,
            y_train,
        )

        print("\nBest Parameters")
        print(grid.best_params_)

        print("\nBest CV Score")
        print(grid.best_score_)

        return grid.best_estimator_
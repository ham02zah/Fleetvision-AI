import pandas as pd


class MissingValueHandler:
    """
    Handles missing values.
    """

    @staticmethod
    def fill(df: pd.DataFrame) -> pd.DataFrame:

        df = df.copy()

        numeric_columns = df.select_dtypes(
            include="number"
        ).columns

        categorical_columns = df.select_dtypes(
            exclude="number"
        ).columns

        for column in numeric_columns:

            df[column] = df[column].fillna(
                df[column].median()
            )

        for column in categorical_columns:

            mode = df[column].mode()

            if len(mode):

                df[column] = df[column].fillna(
                    mode.iloc[0]
                )

        return df
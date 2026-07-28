import pandas as pd


class DataCleaner:
    """
    Performs basic dataset cleaning.
    """

    @staticmethod
    def clean(df: pd.DataFrame) -> pd.DataFrame:

        df = df.copy()

        # Remove duplicate rows
        df = df.drop_duplicates()

        # Remove duplicate IDs
        if "id" in df.columns:
            df = df.drop_duplicates(subset=["id"])

        # Standardize column names
        df.columns = [
            column.strip().lower()
            for column in df.columns
        ]

        return df